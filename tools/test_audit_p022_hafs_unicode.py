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
        self.assertIn('re.search(r"\\bQS\\s+', source)
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
            archive.write_bytes(b"synthetic fixture")
            data = root / "verses.csv"
            data.write_text("sura_no,aya_no,aya_text_unicode\n105,4,SLOT_01\n", encoding="utf-8")
            register = root / "register.md"
            slots = [f"SLOT_{i:02d} [KANDIDAT QS {ref}]" for i, ref in enumerate(module.REFERENCES, 1)]
            slots[0] = "SLOT_01 [KANDIDAT QS 1:1]"
            register.write_text("| P022 | Ikhfa syafawi | " + " | ".join(slots) + " | — |\n", encoding="utf-8")
            output = root / "report.json"
            argv = ["checker", "--archive", str(archive), "--data", str(data),
                    "--register", str(register), "--output", str(output)]
            with patch.object(module, "sha256", return_value=module.EXPECTED_SHA256):
                with patch.object(sys, "argv", argv):
                    with self.assertRaises(SystemExit) as error:
                        module.main()
            self.assertIn("source reference mismatch at K01", str(error.exception))
            self.assertFalse(output.exists())

if __name__ == "__main__":
    unittest.main()
