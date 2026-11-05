"""Regression tests for the committed Jilid 6 register audit gates."""
import csv
import importlib.util
from pathlib import Path
import tempfile
import unittest

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("qj6_register_audit", HERE / "audit-qj6-register.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class RegisterAuditRegression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with (HERE / "QJ6-slots.csv").open(encoding="utf-8-sig", newline="") as handle:
            cls.rows = list(csv.DictReader(handle))

    def audit_mutation(self, mutator):
        rows = [dict(row) for row in self.rows]
        mutator(rows)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "slots.csv"
            with path.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=MODULE.EXPECTED_FIELDS)
                writer.writeheader()
                writer.writerows(rows)
            return MODULE.audit(path)

    def test_committed_register_has_no_structural_errors(self):
        result = MODULE.audit()
        self.assertEqual(result["errors"], [])
        self.assertEqual((result["filled"], result["empty"]), (335, 25))

    def test_empty_slot_accepts_blank_flags(self):
        result = self.audit_mutation(lambda rows: None)
        self.assertEqual(result["errors"], [])

    def test_empty_slot_cannot_be_marked_verified(self):
        def change(rows):
            next(row for row in rows if row["slot_id"] == "QJ6-P018-S01")["source_verified"] = "yes"
        self.assertTrue(any("invalid verification flag" in x for x in self.audit_mutation(change)["errors"]))

    def test_candidate_requires_explicit_verification_flag(self):
        def change(rows):
            next(row for row in rows if row["slot_id"] == "QJ6-P015-S01")["source_verified"] = ""
        self.assertTrue(any("invalid verification flag" in x for x in self.audit_mutation(change)["errors"]))

    def test_internal_source_text_mismatch_is_error(self):
        def change(rows):
            row = next(row for row in rows if row["source_id"].startswith("QJ6-P"))
            row["text_uthmani"] += "X"
        self.assertTrue(any("internal source text differs" in x for x in self.audit_mutation(change)["errors"]))

    def test_priority_waqf_glyph_removal_is_error(self):
        for slot_id, glyph in (
            ("QJ6-P015-S01", "ۘ"),
            ("QJ6-P015-S06", "ۘ"),
            ("QJ6-P016-S03", "ۚ"),
        ):
            with self.subTest(slot_id=slot_id):
                def change(rows):
                    row = next(row for row in rows if row["slot_id"] == slot_id)
                    row["text_uthmani"] = row["text_uthmani"].replace(glyph, "")
                self.assertTrue(any("expected online-source sign" in x
                                    for x in self.audit_mutation(change)["errors"]))


if __name__ == "__main__":
    unittest.main()
