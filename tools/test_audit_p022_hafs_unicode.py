"""Offline smoke tests; synthetic data only, not Quran source certification."""
import csv
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("audit_p022_hafs_unicode.py")

class CheckerTests(unittest.TestCase):
    def test_rejects_wrong_archive_hash_without_report(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            archive = root / "unverified.zip"
            archive.write_bytes(b"not the official archive")
            data = root / "verses.csv"
            data.write_text("sura_no,aya_no,aya_text_unicode\n", encoding="utf-8")
            register = root / "register.md"
            register.write_text("| P022 | Ikhfa syafawi |\n", encoding="utf-8")
            output = root / "report.json"
            result = subprocess.run([sys.executable, str(SCRIPT), "--archive", str(archive),
                "--data", str(data), "--register", str(register), "--output", str(output)],
                text=True, capture_output=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("SHA-256 mismatch", result.stderr)
            self.assertFalse(output.exists())

    def test_expected_reference_manifest_has_sixteen_distinct_slots(self):
        import importlib.util
        spec = importlib.util.spec_from_file_location("checker", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.assertEqual(len(module.REFERENCES), 16)
        self.assertEqual(len(set(module.REFERENCES)), 16)
        self.assertEqual(len(module.EXPECTED_SHA256), 64)

    def test_source_digest_has_expected_hex_format(self):
        import importlib.util
        spec = importlib.util.spec_from_file_location("checker", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.assertRegex(module.EXPECTED_SHA256, r"^[0-9a-f]{64}$")

    def test_sha256_computes_known_fixture(self):
        import importlib.util
        spec = importlib.util.spec_from_file_location("checker", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "fixture.bin"
            path.write_bytes(b"abc")
            self.assertEqual(module.sha256(path),
                             "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad")

    def test_p022_column_offset_matches_register_layout(self):
        import importlib.util
        spec = importlib.util.spec_from_file_location("checker", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "register.md"
            slots = [f"SLOT_{i:02d} [KANDIDAT QS 1:1]" for i in range(1, 17)]
            path.write_text("| P022 | Ikhfa syafawi | " + " | ".join(slots) +
                            " | — | — | 0/24 |\n", encoding="utf-8")
            row = next(line for line in path.read_text(encoding="utf-8").splitlines()
                       if line.startswith("| P022 | Ikhfa syafawi |"))
            cells = [value.strip() for value in row.split("|")[3:19]]
            self.assertEqual(len(cells), 16)
            self.assertTrue(cells[0].startswith("SLOT_01 "))
            self.assertTrue(cells[-1].startswith("SLOT_16 "))
            self.assertIn('match.split("|")[3:19]', SCRIPT.read_text(encoding="utf-8"))

    def test_reference_guard_present(self):
        source = SCRIPT.read_text(encoding="utf-8")
        self.assertIn('re.findall(r"\\bQS\\s+', source)
        self.assertIn("source reference mismatch", source)

    def test_reference_mismatch_fails_closed_with_verified_fixture(self):
        from unittest.mock import patch
        import importlib.util
        spec = importlib.util.spec_from_file_location("checker", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            archive = root / "synthetic.zip"
            import zipfile
            with zipfile.ZipFile(archive, "w") as z:
                z.writestr("verses.csv", "sura_no,aya_no,aya_text_unicode\n105,4,SLOT_01\n")
            data = root / "verses.csv"
            data.write_text("sura_no,aya_no,aya_text_unicode\n105,4,SLOT_01\n", encoding="utf-8")
            register = root / "register.md"
            slots = [f"SLOT_{i:02d} [KANDIDAT QS {ref}]" for i, ref in enumerate(module.REFERENCES, 1)]
            slots[0] = "SLOT_01 [KANDIDAT QS 1:1]"
            register.write_text("| P022 | Ikhfa syafawi | " + " | ".join(slots) + " | — |\n", encoding="utf-8")
            output = root / "report.json"
            argv = ["checker", "--archive", str(archive), "--data", str(data),
                    "--register", str(register), "--output", str(output)]
            with patch.object(module, "EXPECTED_SHA256", module.sha256(archive)):
                with patch.object(sys, "argv", argv):
                    with self.assertRaises(SystemExit) as error:
                        module.main()
            self.assertIn("source reference mismatch at K01", str(error.exception))
            self.assertFalse(output.exists())

    def test_dataset_must_match_member_of_verified_zip(self):
        import importlib.util
        import zipfile
        spec = importlib.util.spec_from_file_location("checker", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            archive = root / "synthetic.zip"
            with zipfile.ZipFile(archive, "w") as z:
                z.writestr("official.csv", "sura_no,aya_no,aya_text_unicode\\n")
            data = root / "source.csv"
            data.write_text("sura_no,aya_no,aya_text_unicode\\n", encoding="utf-8")
            self.assertEqual(module.verify_dataset_in_archive(archive, data), "official.csv")
            data.write_text("altered", encoding="utf-8")
            with self.assertRaises(SystemExit) as error:
                module.verify_dataset_in_archive(archive, data)
            self.assertIn("not byte-identical", str(error.exception))

    def test_duplicate_verse_rows_fail_closed(self):
        from unittest.mock import patch
        import importlib.util
        import zipfile
        spec = importlib.util.spec_from_file_location("checker", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            csv_bytes = b"sura_no,aya_no,aya_text_unicode\n105,4,first\n105,4,second\n"
            archive = root / "fixture.zip"
            with zipfile.ZipFile(archive, "w") as z:
                z.writestr("verses.csv", csv_bytes)
            data = root / "verses.csv"
            data.write_bytes(csv_bytes)
            register = root / "register.md"
            register.write_text("| P022 | Ikhfa syafawi |\n", encoding="utf-8")
            report = root / "report.json"
            argv = ["checker", "--archive", str(archive), "--data", str(data),
                    "--register", str(register), "--output", str(report)]
            with patch.object(module, "EXPECTED_SHA256", module.sha256(archive)):
                with patch.object(sys, "argv", argv):
                    with self.assertRaises(SystemExit) as error:
                        module.main()
            self.assertIn("duplicate verse reference", str(error.exception))
            self.assertFalse(report.exists())

    def test_main_row_selection_requires_unique_full_width_row(self):
        source = SCRIPT.read_text(encoding="utf-8")
        self.assertIn('len(candidates) != 1', source)
        self.assertIn('len(x.split("|")) >= 19', source)
        self.assertIn('expected exactly one 16-slot main P022 row', source)

    def test_duplicate_main_rows_fail_closed_without_report(self):
        from unittest.mock import patch
        import importlib.util
        import zipfile
        spec = importlib.util.spec_from_file_location("checker", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            archive = root / "fixture.zip"
            csv_data = "sura_no,aya_no,aya_text_unicode\n105,4,SLOT_01\n"
            with zipfile.ZipFile(archive, "w") as z:
                z.writestr("verses.csv", csv_data)
            data = root / "verses.csv"
            data.write_text(csv_data, encoding="utf-8")
            slots = [f"SLOT_{i:02d} [KANDIDAT QS {ref}]"
                     for i, ref in enumerate(module.REFERENCES, 1)]
            row = "| P022 | Ikhfa syafawi | " + " | ".join(slots) + " | — |\n"
            register = root / "register.md"
            register.write_text(row + row, encoding="utf-8")
            output = root / "report.json"
            argv = ["checker", "--archive", str(archive), "--data", str(data),
                    "--register", str(register), "--output", str(output)]
            with patch.object(module, "EXPECTED_SHA256", module.sha256(archive)):
                with patch.object(sys, "argv", argv):
                    with self.assertRaises(SystemExit) as error:
                        module.main()
            self.assertIn("found 2", str(error.exception))
            self.assertFalse(output.exists())

    def test_existing_report_is_never_overwritten(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            output = root / "existing.json"
            original = b'{"approved": false, "historic": true}'
            output.write_bytes(original)
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "--archive", str(root / "missing.zip"),
                 "--data", str(root / "missing.csv"),
                 "--register", str(root / "missing.md"),
                 "--output", str(output)],
                text=True, capture_output=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("output report already exists", result.stderr)
            self.assertEqual(output.read_bytes(), original)

    def test_all_sixteen_synthetic_matches_generate_screening_only(self):
        from unittest.mock import patch
        import importlib.util
        import zipfile
        spec = importlib.util.spec_from_file_location("checker", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            csv_text = "sura_no,aya_no,aya_text_unicode\n"
            for i, ref in enumerate(module.REFERENCES, 1):
                sura, aya = ref.split(":")
                csv_text += f"{sura},{aya},BEFORE SLOT_{i:02d} AFTER\n"
            archive = root / "fixture.zip"
            with zipfile.ZipFile(archive, "w") as z:
                z.writestr("verses.csv", csv_text)
            data = root / "verses.csv"
            data.write_text(csv_text, encoding="utf-8")
            slots = [f"SLOT_{i:02d} [KANDIDAT QS {ref}]"
                     for i, ref in enumerate(module.REFERENCES, 1)]
            register = root / "register.md"
            register.write_text(
                "| P022 | Ikhfa syafawi | " + " | ".join(slots) + " | — |\n"
                "| P022 | Ikhfa syafawi | supporting note | HOLD |\n",
                encoding="utf-8")
            output = root / "screening.json"
            argv = ["checker", "--archive", str(archive), "--data", str(data),
                    "--register", str(register), "--output", str(output)]
            with patch.object(module, "EXPECTED_SHA256", module.sha256(archive)):
                with patch.object(sys, "argv", argv):
                    module.main()
            report = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(len(report["slots"]), 16)
            self.assertTrue(all(x["status"] == "EXACT_MATCH" for x in report["slots"]))
            self.assertTrue(report["sha256_verified"])
            self.assertEqual(report["archive_sha256"], module.sha256(archive))
            self.assertEqual(report["dataset_sha256"], module.sha256(data))
            self.assertEqual(report["register_sha256"], module.sha256(register))
            self.assertIs(report["screening_only"], True)
            self.assertIs(report["print_approved"], False)
            self.assertNotIn("print_ready", report)

    def test_empty_source_dataset_fails_closed_without_report(self):
        from unittest.mock import patch
        import importlib.util
        import zipfile
        spec = importlib.util.spec_from_file_location("checker", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            csv_data = "sura_no,aya_no,aya_text_unicode\n"
            archive = root / "fixture.zip"
            with zipfile.ZipFile(archive, "w") as z:
                z.writestr("verses.csv", csv_data)
            data = root / "verses.csv"
            data.write_text(csv_data, encoding="utf-8")
            register = root / "register.md"
            register.write_text("| P022 | Ikhfa syafawi |\n", encoding="utf-8")
            output = root / "report.json"
            argv = ["checker", "--archive", str(archive), "--data", str(data),
                    "--register", str(register), "--output", str(output)]
            with patch.object(module, "EXPECTED_SHA256", module.sha256(archive)):
                with patch.object(sys, "argv", argv):
                    with self.assertRaises(SystemExit) as error:
                        module.main()
            self.assertIn("nonempty list of verse objects", str(error.exception))
            self.assertFalse(output.exists())

    def test_unicode_mismatch_exits_nonzero_but_retains_screening_report(self):
        from unittest.mock import patch
        import importlib.util
        import zipfile
        spec = importlib.util.spec_from_file_location("checker", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            csv_text = "sura_no,aya_no,aya_text_unicode\n"
            for i, ref in enumerate(module.REFERENCES, 1):
                sura, aya = ref.split(":")
                value = "DIFFERENT" if i == 16 else f"SLOT_{i:02d}"
                csv_text += f"{sura},{aya},{value}\n"
            archive = root / "fixture.zip"
            with zipfile.ZipFile(archive, "w") as z:
                z.writestr("verses.csv", csv_text)
            data = root / "verses.csv"
            data.write_text(csv_text, encoding="utf-8")
            slots = [f"SLOT_{i:02d} [KANDIDAT QS {ref}]"
                     for i, ref in enumerate(module.REFERENCES, 1)]
            register = root / "register.md"
            register.write_text("| P022 | Ikhfa syafawi | " + " | ".join(slots) + " | — |\n",
                                encoding="utf-8")
            output = root / "screening.json"
            argv = ["checker", "--archive", str(archive), "--data", str(data),
                    "--register", str(register), "--output", str(output)]
            with patch.object(module, "EXPECTED_SHA256", module.sha256(archive)):
                with patch.object(sys, "argv", argv):
                    with self.assertRaises(SystemExit) as error:
                        module.main()
            self.assertIn("failed exact Unicode screening", str(error.exception))
            report = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(len(report["slots"]), 16)
            self.assertEqual(report["slots"][-1]["status"], "HOLD_REVIEW")
            self.assertIs(report["print_approved"], False)

    def test_source_parser_rejects_ambiguous_json_and_missing_csv_headers(self):
        from unittest.mock import patch
        import importlib.util
        import zipfile
        spec = importlib.util.spec_from_file_location("checker", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            ambiguous = root / "verses.json"
            ambiguous.write_text(json.dumps({"first": [], "second": []}), encoding="utf-8")
            with self.assertRaises(SystemExit) as error:
                module.read_rows(ambiguous)
            self.assertIn("exactly one verse list", str(error.exception))
            incomplete = root / "verses.csv"
            incomplete.write_text("sura_no,aya_no\n105,4\n", encoding="utf-8")
            with self.assertRaises(SystemExit) as error:
                module.read_rows(incomplete)
            self.assertIn("missing required Quran verse columns", str(error.exception))

    def test_invalid_verse_coordinates_fail_closed(self):
        from unittest.mock import patch
        import importlib.util
        import zipfile
        spec = importlib.util.spec_from_file_location("checker", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        for sura, aya in [(0, 4), (115, 1), (105, 0), (105, -1)]:
            with self.subTest(sura=sura, aya=aya), tempfile.TemporaryDirectory() as d:
                root = Path(d)
                csv_data = f"sura_no,aya_no,aya_text_unicode\n{sura},{aya},synthetic\n"
                archive = root / "fixture.zip"
                with zipfile.ZipFile(archive, "w") as z:
                    z.writestr("verses.csv", csv_data)
                data = root / "verses.csv"
                data.write_text(csv_data, encoding="utf-8")
                register = root / "register.md"
                register.write_text("| P022 | Ikhfa syafawi |\n", encoding="utf-8")
                output = root / "report.json"
                argv = ["checker", "--archive", str(archive), "--data", str(data),
                        "--register", str(register), "--output", str(output)]
                with patch.object(module, "EXPECTED_SHA256", module.sha256(archive)):
                    with patch.object(sys, "argv", argv):
                        with self.assertRaises(SystemExit) as error:
                            module.main()
                self.assertIn("invalid Quran verse coordinates", str(error.exception))
                self.assertFalse(output.exists())

    def test_duplicate_csv_header_is_rejected(self):
        import importlib.util
        spec = importlib.util.spec_from_file_location("checker", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as d:
            data = Path(d) / "verses.csv"
            data.write_text(
                "sura_no,aya_no,aya_text_unicode,aya_text_unicode\n"
                "105,4,original,shadowed\n", encoding="utf-8"
            )
            with self.assertRaises(SystemExit) as error:
                module.read_rows(data)
            self.assertIn("duplicate column headers", str(error.exception))

    def test_multiple_qs_citations_in_one_slot_fail_closed(self):
        from unittest.mock import patch
        import importlib.util
        import zipfile
        spec = importlib.util.spec_from_file_location("checker", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            csv_text = "sura_no,aya_no,aya_text_unicode\n"
            for i, ref in enumerate(module.REFERENCES, 1):
                sura, aya = ref.split(":")
                csv_text += f"{sura},{aya},SLOT_{i:02d}\n"
            archive = root / "fixture.zip"
            with zipfile.ZipFile(archive, "w") as z:
                z.writestr("verses.csv", csv_text)
            data = root / "verses.csv"
            data.write_text(csv_text, encoding="utf-8")
            slots = [f"SLOT_{i:02d} [KANDIDAT QS {ref}]"
                     for i, ref in enumerate(module.REFERENCES, 1)]
            slots[0] += " [ALTERNATIF QS 2:8]"
            register = root / "register.md"
            register.write_text("| P022 | Ikhfa syafawi | " + " | ".join(slots) + " | — |\n",
                                encoding="utf-8")
            output = root / "screening.json"
            argv = ["checker", "--archive", str(archive), "--data", str(data),
                    "--register", str(register), "--output", str(output)]
            with patch.object(module, "EXPECTED_SHA256", module.sha256(archive)):
                with patch.object(sys, "argv", argv):
                    with self.assertRaises(SystemExit) as error:
                        module.main()
            self.assertIn("ambiguous citations", str(error.exception))
            self.assertFalse(output.exists())

if __name__ == "__main__":
    unittest.main()
