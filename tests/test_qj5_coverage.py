"""Regression tests for the read-only Jilid 5 coverage auditor."""
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("qj5_coverage", ROOT / "scripts/audit_qj5_coverage.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

REGISTER = ROOT / "02_MASTER_SYSTEM/BANK_REFERENSI_PER_KOMPETENSI/REGISTER_24_KELOMPOK_JILID_5.md"

class CoverageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original = REGISTER.read_text(encoding="utf-8")

    def test_original_has_40_pages_and_consistent_capacity(self):
        rows, errors = module.audit(self.original)
        self.assertFalse(errors, errors)
        self.assertEqual(len(rows), 40)
        self.assertEqual(sum(r[2] for r in rows), 480)
        self.assertEqual(sum(r[1] + r[3] for r in rows), 480)
        self.assertEqual(next(r for r in rows if r[0] == "P013")[2], 16)
        # Do not hardcode 468/12: valid future candidate edits must not break CI.

    def test_duplicate_page_rejected(self):
        line = next(s for s in self.original.splitlines() if s.startswith("| P013 |"))
        _, errors = module.audit(self.original + "\n" + line)
        self.assertTrue(any("duplicate page" in e for e in errors))

    def test_unreferenced_p013_candidate_rejected(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P013 |"):
                cells = line.split("|")
                # K03 is a blank cell; replace only that slot.
                self.assertEqual(cells[5].strip(), "—")
                cells[5] = " kandidat tanpa rujukan "
                lines[i] = "|".join(cells)
                break
        _, errors = module.audit("\n".join(lines))
        self.assertTrue(any("expected exactly one known Mad Farq reference" in e for e in errors))

    def test_duplicate_mad_farq_locus_rejected(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P013 |"):
                cells = line.split("|")
                # Duplicate the known QS 27:59 reference in K03.
                cells[5] = " آللَّهُ خَيْرٌ [KANDIDAT QS 27:59] "
                lines[i] = "|".join(cells)
                break
        _, errors = module.audit("\n".join(lines))
        self.assertTrue(any("duplicate Quran locus" in e for e in errors))

    def test_sah_cannot_exceed_filled_candidates(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P013 |"):
                lines[i] = line.replace("| 0/16 |", "| 5/16 |")
                break
        _, errors = module.audit("\n".join(lines))
        self.assertTrue(any("Sah count exceeds filled candidates" in e for e in errors))

    def test_inactive_slot_on_later_page_rejected(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P040 |"):
                cells = line.split("|")
                self.assertEqual(cells[11].strip(), "—")
                cells[11] = " kandidat tidak aktif "
                lines[i] = "|".join(cells)
                break
        _, errors = module.audit("\n".join(lines))
        self.assertTrue(any("inactive K slots contain data" in e for e in errors))

    def test_p013_rejects_unapproved_quran_locus(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P013 |"):
                cells = line.split("|")
                cells[5] = " contoh uji [KANDIDAT QS 27:590] "
                lines[i] = "|".join(cells)
                break
        _, errors = module.audit("\n".join(lines))
        self.assertTrue(any("expected exactly one known Mad Farq reference" in e for e in errors))

    def test_p013_rejects_multiple_references_in_one_slot(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P013 |"):
                cells = line.split("|")
                cells[5] = " contoh uji [KANDIDAT QS 27:59; QS 6:143] "
                lines[i] = "|".join(cells)
                break
        _, errors = module.audit("\n".join(lines))
        self.assertTrue(any("expected exactly one known Mad Farq reference" in e for e in errors))

    def test_p013_rejects_reference_with_letter_suffix(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P013 |"):
                cells = line.split("|")
                cells[5] = " contoh uji [KANDIDAT QS 27:59abc] "
                lines[i] = "|".join(cells)
                break
        _, errors = module.audit("\n".join(lines))
        self.assertTrue(any("expected exactly one known Mad Farq reference" in e for e in errors))

    def test_p013_rejects_reference_with_extra_colon(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P013 |"):
                cells = line.split("|")
                cells[5] = " contoh uji [KANDIDAT QS 27:59:2] "
                lines[i] = "|".join(cells)
                break
        _, errors = module.audit("\n".join(lines))
        self.assertTrue(any("expected exactly one known Mad Farq reference" in e for e in errors))

    def test_p013_rejects_hidden_malformed_second_reference(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P013 |"):
                cells = line.split("|")
                cells[5] = " contoh uji [KANDIDAT QS 27:59; QS 27:590] "
                lines[i] = "|".join(cells)
                break
        _, errors = module.audit("\n".join(lines))
        self.assertTrue(any("expected exactly one known Mad Farq reference" in e for e in errors))

    def test_repeated_phrases_are_advisory_only(self):
        groups = module.repeated_phrases(self.original)
        self.assertTrue(any(page == "P016" and slots == ["K03", "K04"]
                            for page, _, slots in groups))
        self.assertTrue(any(page == "P013" and slots == ["K02", "K07"]
                            for page, _, slots in groups))
        _, errors = module.audit(self.original)
        self.assertFalse(errors, errors)

    def test_repeated_phrases_ignore_inactive_and_review_notes(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P040 |"):
                cells = line.split("|")
                cells[3] = "نَصٌّ [review A]"
                cells[4] = "نَصٌّ [review B]"
                lines[i] = "|".join(cells)
                break
        groups = module.repeated_phrases("\n".join(lines))
        self.assertTrue(any(page == "P040" and slots == ["K01", "K02"]
                            for page, _, slots in groups))

    def test_repeated_quran_loci_are_advisory(self):
        groups = module.repeated_quran_loci(self.original)
        self.assertTrue(any(page == "P016" and reference == "QS 106:3"
                            and {"K03", "K04", "K05"}.issubset(set(slots))
                            for page, reference, slots in groups))
        self.assertTrue(any(page == "P011" and reference == "QS 80:33"
                            and {"K04", "K12"}.issubset(set(slots))
                            for page, reference, slots in groups))
        _, errors = module.audit(self.original)
        self.assertFalse(errors, errors)

    def test_source_advisory_ignores_review_note_cross_references(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P040 |"):
                cells = line.split("|")
                cells[3] = "نَصٌّ [KANDIDAT QS 17:70; AUDIT: lihat QS 2:2]"
                cells[4] = "نَصٌّ آخر [KANDIDAT QS 2:3; AUDIT: lihat QS 2:2]"
                lines[i] = "|".join(cells)
                break
        groups = module.repeated_quran_loci("\n".join(lines))
        self.assertFalse(any(page == "P040" and reference == "QS 2:2"
                             for page, reference, _ in groups))

    def test_source_advisory_is_not_a_sah_decision(self):
        groups = module.repeated_quran_loci(self.original)
        self.assertTrue(groups)
        rows, errors = module.audit(self.original)
        self.assertFalse(errors, errors)
        self.assertEqual(next(row for row in rows if row[0] == "P013")[4], "0/16")

    def test_current_duplicate_baseline_requires_review_not_auto_replacement(self):
        # Snapshot of advisory group counts for the current 40-page register.
        # Any future change must be reviewed; counts are not acceptance criteria.
        text_groups = module.repeated_phrases(self.original)
        source_groups = module.repeated_quran_loci(self.original)
        self.assertEqual(len(text_groups), 9)
        self.assertEqual(len(source_groups), 18)
        self.assertTrue(any(page == "P040" and reference == "QS 17:70"
                            and slots == ["K03", "K06"]
                            for page, reference, slots in source_groups))

    def test_source_advisory_does_not_count_bare_qs_in_notes(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P040 |"):
                cells = line.split("|")
                cells[3] = "نَصٌّ [AUDIT: QS 2:2; tanpa label KANDIDAT]"
                cells[4] = "نَصٌّ آخر [AUDIT: QS 2:2; tanpa label KANDIDAT]"
                lines[i] = "|".join(cells)
                break
        groups = module.repeated_quran_loci("\n".join(lines))
        self.assertFalse(any(page == "P040" and reference == "QS 2:2"
                             for page, reference, _ in groups))

    def test_source_advisory_does_not_read_inactive_slots(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P040 |"):
                cells = line.split("|")
                cells[11] = "uji [KANDIDAT QS 2:2]"
                cells[12] = "uji [KANDIDAT QS 2:2]"
                lines[i] = "|".join(cells)
                break
        groups = module.repeated_quran_loci("\n".join(lines))
        self.assertFalse(any(page == "P040" and reference == "QS 2:2"
                             for page, reference, _ in groups))
        _, errors = module.audit("\n".join(lines))
        self.assertTrue(any("inactive K slots" in e for e in errors))

    def test_source_advisory_finds_candidate_after_audit_note(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P040 |"):
                cells = line.split("|")
                cells[3] = "أَوَّلٌ [AUDIT: periksa waqaf; KANDIDAT QS 2:2]"
                cells[4] = "ثَانٍ [AUDIT: periksa rasm; KANDIDAT QS 2:2]"
                lines[i] = "|".join(cells)
                break
        groups = module.repeated_quran_loci("\n".join(lines))
        self.assertTrue(any(page == "P040" and reference == "QS 2:2"
                            and slots == ["K01", "K02"]
                            for page, reference, slots in groups))

    def test_p016_first_slot_source_label_after_audit_note(self):
        # The real register starts K01's annotation with AUDIT, not KANDIDAT.
        line = next(line for line in self.original.splitlines()
                    if line.startswith("| P016 |"))
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        self.assertIn("AUDIT:", cells[2])
        self.assertIn("KANDIDAT QS 106:1", cells[2])
        # Reuse its genuine annotation in K02 to prove source detection.
        lines = self.original.splitlines()
        for i, row in enumerate(lines):
            if row.startswith("| P016 |"):
                parts = row.split("|")
                parts[4] = parts[3]
                lines[i] = "|".join(parts)
                break
        groups = module.repeated_quran_loci("\n".join(lines))
        self.assertTrue(any(page == "P016" and reference == "QS 106:1"
                            and slots == ["K01", "K02"]
                            for page, reference, slots in groups))

    def test_murajaah_source_recognized_but_not_hadith(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P036 |"):
                cells = line.split("|")
                cells[4] = cells[3]  # Repeat the genuine P036 K01 MUROJAAH source in K02
                lines[i] = "|".join(cells)
                break
        groups = module.repeated_quran_loci("\n".join(lines))
        self.assertTrue(any(page == "P036" and reference == "QS 112:1"
                            and slots == ["K01", "K02"]
                            for page, reference, slots in groups))
        self.assertFalse(any(page == "P038" and "BUKHARI" in reference
                             for page, reference, _ in groups))

    def test_current_register_source_families_are_explicit(self):
        # Snapshot of source metadata, not a claim of Quranic or hadith validity.
        counts = {"quran": 0, "arabic": 0, "hadith": 0}
        for line in self.original.splitlines():
            if not line.startswith("| P") or not line[3:6].isdigit():
                continue
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if len(cells) != 19:
                continue
            capacity = 16 if int(cells[0][1:]) <= 20 else 8
            for value in cells[2:2 + capacity]:
                if not value or value == "—":
                    continue
                if "BAHASA ARAB" in value:
                    counts["arabic"] += 1
                elif "KANDIDAT HADIS" in value:
                    counts["hadith"] += 1
                elif "KANDIDAT QS " in value or (
                    "KANDIDAT;" in value
                    and ("MUROJAAH QS " in value or "HAFALAN UNIT QS " in value)
                ):
                    counts["quran"] += 1
                else:
                    self.fail("Unclassified source marker in register: " + cells[0])
        self.assertEqual(counts, {"quran": 457, "arabic": 8, "hadith": 3})

    def test_p013_ignores_qs_cross_reference_in_review_note(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P013 |"):
                cells = line.split("|")
                cells[3] = cells[3].replace(
                    "KANDIDAT QS 27:59",
                    "AUDIT: bandingkan QS 6:143; KANDIDAT QS 27:59",
                )
                lines[i] = "|".join(cells)
                break
        _, errors = module.audit("\n".join(lines))
        self.assertFalse(any("P013 K01: expected exactly one" in error
                             for error in errors), errors)

    def test_p013_rejects_two_declared_sources(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P013 |"):
                cells = line.split("|")
                cells[3] = cells[3].replace(
                    "KANDIDAT QS 27:59",
                    "KANDIDAT QS 27:59; KANDIDAT QS 6:143",
                )
                lines[i] = "|".join(cells)
                break
        _, errors = module.audit("\n".join(lines))
        self.assertTrue(any("P013 K01: expected exactly one" in error
                            for error in errors), errors)

    def test_p013_allows_audit_cross_reference_after_declared_source(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P013 |"):
                cells = line.split("|")
                cells[3] = cells[3].replace(
                    "KANDIDAT QS 27:59",
                    "KANDIDAT QS 27:59; AUDIT: bandingkan QS 6:143",
                )
                lines[i] = "|".join(cells)
                break
        _, errors = module.audit("\n".join(lines))
        self.assertFalse(any("P013 K01: expected exactly one" in e
                             for e in errors), errors)

    def test_p036_hafalan_incomplete_surah_is_advisory(self):
        warnings = module.p036_hafalan_advisory(self.original)
        self.assertTrue(any("QS 113:5" in warning for warning in warnings))
        self.assertFalse(any("differs from documented" in warning
                             for warning in warnings), warnings)
        _, errors = module.audit(self.original)
        self.assertFalse(errors, errors)

    def test_p036_hafalan_advisory_handles_missing_page(self):
        content = "\n".join(
            line for line in self.original.splitlines()
            if not line.startswith("| P036 |")
        )
        self.assertTrue(any("missing" in warning
                            for warning in module.p036_hafalan_advisory(content)))

    def test_p036_warns_when_hafalan_sources_are_swapped(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P036 |"):
                cells = line.split("|")
                cells[3], cells[4] = cells[4], cells[3]
                lines[i] = "|".join(cells)
                break
        warnings = module.p036_hafalan_advisory("\n".join(lines))
        self.assertTrue(any("P036 K01:" in w for w in warnings), warnings)
        self.assertTrue(any("P036 K02:" in w for w in warnings), warnings)

    def test_p036_warns_when_hafalan_source_is_missing(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P036 |"):
                cells = line.split("|")
                cells[8] = " — "  # K06, originally QS 113:2
                lines[i] = "|".join(cells)
                break
        warnings = module.p036_hafalan_advisory("\n".join(lines))
        self.assertTrue(any("P036 K06:" in w for w in warnings), warnings)

    def test_missing_page_rejected(self):
        lines = [s for s in self.original.splitlines() if not s.startswith("| P040 |")]
        _, errors = module.audit("\n".join(lines))
        self.assertTrue(any("missing pages" in e for e in errors))

if __name__ == "__main__":
    unittest.main()
