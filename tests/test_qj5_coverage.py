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

    def test_missing_page_rejected(self):
        lines = [s for s in self.original.splitlines() if not s.startswith("| P040 |")]
        _, errors = module.audit("\n".join(lines))
        self.assertTrue(any("missing pages" in e for e in errors))

if __name__ == "__main__":
    unittest.main()
