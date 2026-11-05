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
        expected_empty = sum(row["review_status"] == "EMPTY" for row in self.rows)
        self.assertEqual((result["filled"], result["empty"]),
                         (len(self.rows) - expected_empty, expected_empty))

    def test_release_holds_identify_unfilled_and_missing_waqf_la(self):
        holds = MODULE.audit()["release_holds"]
        unfilled = {item["slot_id"] for item in holds if item["reason"] == "unfilled_slot"}
        glyph_missing = {item["slot_id"] for item in holds if item["reason"] == "waqf_la_glyph_missing"}
        expected_empty = {row["slot_id"] for row in self.rows if row["review_status"] == "EMPTY"}
        expected_missing = {row["slot_id"] for row in self.rows
                            if row["page_id"] == "QJ6-P017"
                            and row["review_status"] != "EMPTY"
                            and "لا" not in row["text_uthmani"]}
        self.assertEqual(unfilled, expected_empty)
        self.assertEqual(glyph_missing, expected_missing)
        expected_source = {row['slot_id'] for row in self.rows if row['review_status'] != 'EMPTY' and row['source_verified'].lower() != 'yes'}
        expected_competency = {row['slot_id'] for row in self.rows if row['review_status'] != 'EMPTY' and row['competency_verified'].lower() != 'yes'}
        self.assertEqual({item['slot_id'] for item in holds if item['reason'] == 'source_unverified'}, expected_source)
        self.assertEqual({item['slot_id'] for item in holds if item['reason'] == 'competency_unverified'}, expected_competency)
        expected_research = {row['slot_id'] for row in self.rows if row['review_status'] == 'RESEARCH'}
        self.assertEqual({item['slot_id'] for item in holds if item['reason'] == 'research_review_pending'}, expected_research)
        expected_p017 = {row['slot_id'] for row in self.rows if row['page_id'] == 'QJ6-P017' and row['review_status'] != 'EMPTY'}
        self.assertEqual(len(holds), sum(map(len, (expected_empty, expected_missing, expected_source, expected_competency, expected_research))) + 3 + len(expected_p017))

    def test_research_hold_persists_after_verification_flags_change(self):
        def change(rows):
            row = next(row for row in rows if row["slot_id"] == "QJ6-P022-S09")
            row["source_verified"] = "yes"
            row["competency_verified"] = "yes"
        result = self.audit_mutation(change)
        holds = result["release_holds"]
        self.assertIn(
            {"slot_id": "QJ6-P022-S09", "reason": "research_review_pending"},
            holds,
        )
        self.assertFalse(result["print_approved"])

    def test_competency_verification_requires_reviewer(self):
        def change(rows):
            row = next(row for row in rows if row["slot_id"] == "QJ6-P002-S09")
            row["competency_verified"] = "yes"
            row["reviewer"] = ""
        result = self.audit_mutation(change)
        self.assertTrue(any("competency verified without reviewer" in error for error in result["errors"]))
        self.assertFalse(result["print_approved"])

    def test_source_verification_requires_source_id(self):
        def change(rows):
            row = next(row for row in rows if row["slot_id"] == "QJ6-P002-S09")
            row["source_verified"] = "yes"
            row["source_id"] = ""
        result = self.audit_mutation(change)
        self.assertTrue(any("source verified without source_id" in error for error in result["errors"]))
        self.assertFalse(result["print_approved"])

    def test_hold_summary_counts_records_and_distinct_slots(self):
        from collections import Counter
        result = MODULE.audit()
        holds = result["release_holds"]
        summary = result["release_hold_summary"]
        self.assertEqual(summary["hold_records"], len(holds))
        self.assertEqual(summary["unique_held_slots"],
                         len({item["slot_id"] for item in holds}))
        self.assertEqual(summary["by_reason"],
                         dict(sorted(Counter(item["reason"] for item in holds).items())))
        self.assertEqual(summary["unique_held_slots"], 360)
        self.assertGreater(summary["hold_records"], summary["unique_held_slots"])

    def test_populated_p017_cases_require_independent_msi_review(self):
        expected = {row["slot_id"] for row in self.rows
                    if row["page_id"] == "QJ6-P017" and row["review_status"] != "EMPTY"}
        holds = MODULE.audit()["release_holds"]
        self.assertEqual(
            {item["slot_id"] for item in holds if item["reason"] == "waqf_la_msi_review_pending"},
            expected,
        )

    def test_three_msi_sign_cases_remain_on_independent_hold(self):
        expected = {"QJ6-P015-S01", "QJ6-P015-S06", "QJ6-P016-S03"}
        holds = MODULE.audit()["release_holds"]
        self.assertEqual(
            {item["slot_id"] for item in holds if item["reason"] == "msi_sign_collation_pending"},
            expected,
        )

    def test_msi_hold_persists_even_with_both_verification_flags(self):
        def change(rows):
            row = next(row for row in rows if row["slot_id"] == "QJ6-P015-S01")
            row["source_verified"] = "yes"
            row["competency_verified"] = "yes"
            row["reviewer"] = "TEST ONLY"
        result = self.audit_mutation(change)
        self.assertIn(
            {"slot_id": "QJ6-P015-S01", "reason": "msi_sign_collation_pending"},
            result["release_holds"],
        )
        self.assertFalse(result["print_approved"])

    def test_out_of_range_slot_id_is_rejected(self):
        for invalid in ("QJ6-P041-S01", "QJ6-P001-S10", "QJ6-P1-S01"):
            with self.subTest(slot_id=invalid):
                def change(rows):
                    next(row for row in rows if row["slot_id"] == "QJ6-P001-S01")["slot_id"] = invalid
                result = self.audit_mutation(change)
                self.assertTrue(any("Unexpected slot IDs" in e for e in result["errors"]))
                self.assertFalse(result["print_approved"])

    def test_whole_page_material_reclassification_is_rejected(self):
        for page_id, wrong_kind in (
            ("QJ6-P018", "tartil"),
            ("QJ6-P028", "tartil"),
            ("QJ6-P036", "tartil"),
            ("QJ6-P038", "tartil"),
            ("QJ6-P002", "hafalan"),
        ):
            with self.subTest(page_id=page_id):
                def change(rows):
                    for row in rows:
                        if row["page_id"] == page_id:
                            row["kind"] = wrong_kind
                result = self.audit_mutation(change)
                self.assertTrue(any("expected material kind" in e for e in result["errors"]))
                self.assertFalse(result["print_approved"])

    def test_mixed_competency_on_one_page_is_rejected(self):
        def change(rows):
            next(row for row in rows if row["slot_id"] == "QJ6-P002-S09")["competency"] = "Wrong target"
        result = self.audit_mutation(change)
        self.assertTrue(any("inconsistent or blank page competency" in e for e in result["errors"]))

    def test_mixed_material_kind_on_one_page_is_rejected(self):
        def change(rows):
            next(row for row in rows if row["slot_id"] == "QJ6-P002-S09")["kind"] = "hafalan"
        result = self.audit_mutation(change)
        self.assertTrue(any("mixed material kinds within page" in e for e in result["errors"]))

    def test_unknown_slot_kind_fails_closed(self):
        for invalid in ("", "tartil ", "unknown", "print-ready"):
            with self.subTest(kind=invalid):
                def change(rows):
                    next(row for row in rows if row["slot_id"] == "QJ6-P002-S09")["kind"] = invalid
                result = self.audit_mutation(change)
                self.assertTrue(any("unknown slot kind" in error for error in result["errors"]))
                self.assertFalse(result["print_approved"])

    def test_unknown_review_status_fails_closed(self):
        for invalid in ("APPROVED", "PRINT_READY", "", "CANDIDATE "):
            with self.subTest(status=invalid):
                def change(rows):
                    next(row for row in rows if row["slot_id"] == "QJ6-P002-S09")["review_status"] = invalid
                result = self.audit_mutation(change)
                self.assertTrue(any("unknown review_status" in error for error in result["errors"]))
                self.assertFalse(result["print_approved"])

    def test_empty_slot_accepts_blank_flags(self):
        result = self.audit_mutation(lambda rows: None)
        self.assertEqual(result["errors"], [])

    def test_empty_slot_cannot_be_marked_verified(self):
        def change(rows):
            next(row for row in rows if row["slot_id"] == "QJ6-P018-S01")["source_verified"] = "yes"
        self.assertTrue(any("invalid verification flag" in x for x in self.audit_mutation(change)["errors"]))

    def test_all_empty_slots_reject_verified_flags(self):
        for slot_id in ("QJ6-P017-S01", "QJ6-P018-S01", "QJ6-P036-S01"):
            for field in ("source_verified", "competency_verified"):
                with self.subTest(slot_id=slot_id, field=field):
                    def change(rows):
                        next(row for row in rows if row["slot_id"] == slot_id)[field] = "yes"
                    self.assertTrue(any("invalid verification flag" in x
                                        for x in self.audit_mutation(change)["errors"]))

    def test_candidate_requires_explicit_verification_flag(self):
        def change(rows):
            next(row for row in rows if row["slot_id"] == "QJ6-P015-S01")["source_verified"] = ""
        self.assertTrue(any("invalid verification flag" in x for x in self.audit_mutation(change)["errors"]))

    def test_internal_source_text_mismatch_is_error(self):
        def change(rows):
            row = next(row for row in rows if row["source_id"].startswith("QJ6-P"))
            row["text_uthmani"] += "X"
        self.assertTrue(any("internal source text differs" in x for x in self.audit_mutation(change)["errors"]))

    def test_p017_cannot_be_verified_without_explicit_waqf_la(self):
        for slot_id in ("QJ6-P017-S02", "QJ6-P017-S04"):
            for field in ("source_verified", "competency_verified"):
                with self.subTest(slot_id=slot_id, field=field):
                    def change(rows):
                        next(row for row in rows if row["slot_id"] == slot_id)[field] = "yes"
                    self.assertTrue(any("cannot verify waqf-la" in x
                                        for x in self.audit_mutation(change)["errors"]))

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
