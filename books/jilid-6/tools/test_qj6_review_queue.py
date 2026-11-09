"""Review queue must preserve release holds without granting approval."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("qj6_review_queue", HERE / "qj6-review-queue.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ReviewQueueRegression(unittest.TestCase):
    def test_queue_matches_unique_held_slots(self):
        queue = MODULE.build_queue()
        audit = MODULE.MODULE.audit()
        self.assertEqual(len(queue), audit["release_hold_summary"]["unique_held_slots"])
        self.assertEqual(len({r["slot_id"] for r in queue}), len(queue))
        self.assertTrue(all(r["hold_reasons"] for r in queue))
        self.assertEqual(sum(r["review_status"] == "EMPTY" for r in queue), 25)

    def test_review_queue_preserves_verbatim_quranic_excerpts(self):
        import csv
        with (HERE / "QJ6-slots.csv").open(encoding="utf-8-sig", newline="") as f:
            originals = {r["slot_id"]: r for r in csv.DictReader(f)}
        queue = MODULE.build_queue()
        for row in queue:
            with self.subTest(slot_id=row["slot_id"]):
                original = originals[row["slot_id"]]
                for field in ("text_uthmani", "surah", "ayah_start", "ayah_end"):
                    self.assertEqual(row[field], original[field])
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "review.csv"
            MODULE.export(output)
            with output.open(encoding="utf-8", newline="") as f:
                exported = list(csv.DictReader(f))
            self.assertEqual(
                [(r["slot_id"], r["text_uthmani"]) for r in exported],
                [(r["slot_id"], r["text_uthmani"]) for r in queue],
            )

    def test_row_fingerprints_match_original_register_and_detect_changes(self):
        import csv
        import hashlib
        import json
        with (HERE / "QJ6-slots.csv").open(encoding="utf-8-sig", newline="") as f:
            originals = {r["slot_id"]: r for r in csv.DictReader(f)}
        for record in MODULE.build_queue():
            row = originals[record["slot_id"]]
            canonical = json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
            expected = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
            self.assertEqual(record["row_sha256"], expected)
            modified = dict(row)
            modified["notes"] += " changed"
            altered = json.dumps(modified, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
            self.assertNotEqual(record["row_sha256"], hashlib.sha256(altered.encode("utf-8")).hexdigest())

    def test_reviewer_worksheet_never_prefills_decisions(self):
        import csv
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "worksheet.csv"
            count = MODULE.export_review_worksheet(output)
            with output.open(encoding="utf-8", newline="") as f:
                rows = list(csv.DictReader(f))
            self.assertEqual(len(rows), count)
            self.assertEqual(count, len(MODULE.build_queue()))
            for row in rows:
                for field in MODULE.DECISION_FIELDS:
                    self.assertEqual(row[field], "", f"{row['slot_id']}: {field}")
                self.assertEqual(len(row["row_sha256"]), 64)
        self.assertFalse(MODULE.MODULE.audit()["print_approved"])

    def test_worksheet_validator_rejects_stale_and_unsubstantiated_decisions(self):
        import csv
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "worksheet.csv"
            MODULE.export_review_worksheet(path)
            self.assertEqual(MODULE.validate_review_worksheet(path), [])
            with path.open(encoding="utf-8", newline="") as f:
                rows = list(csv.DictReader(f))
            rows[0]["decision"] = "APPROVE"
            rows[0]["row_sha256"] = "0" * 64
            with path.open("w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=MODULE.FIELDS + MODULE.DECISION_FIELDS)
                writer.writeheader()
                writer.writerows(rows)
            errors = MODULE.validate_review_worksheet(path)
            self.assertTrue(any("row_sha256" in error for error in errors))
            self.assertTrue(any("decision missing reviewer_name" in error for error in errors))
            self.assertFalse(MODULE.MODULE.audit()["print_approved"])

    def test_worksheet_rejects_empty_approval_and_invalid_date(self):
        import csv
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "worksheet.csv"
            MODULE.export_review_worksheet(path)
            with path.open(encoding="utf-8", newline="") as f:
                rows = list(csv.DictReader(f))
            empty = next(row for row in rows if row["review_status"] == "EMPTY")
            empty.update({
                "decision": "APPROVE", "reviewer_name": "Reviewer",
                "review_date": "2026-02-30", "mushaf_edition": "pending",
                "evidence_reference": "pending", "tajwid_rule": "pending",
                "curriculum_evidence": "pending",
            })
            with path.open("w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=MODULE.FIELDS + MODULE.DECISION_FIELDS)
                writer.writeheader()
                writer.writerows(rows)
            issues = MODULE.validate_review_worksheet(path)
            self.assertTrue(any("cannot approve an unfilled slot" in x for x in issues))
            self.assertTrue(any("real YYYY-MM-DD date" in x for x in issues))

    def test_empty_evidence_intake_has_no_invented_verses_or_approvals(self):
        import csv
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "empty-evidence.csv"
            count = MODULE.export_empty_slot_evidence(path)
            with path.open(encoding="utf-8", newline="") as f:
                rows = list(csv.DictReader(f))
            self.assertEqual(count, 25)
            self.assertEqual(len(rows), count)
            self.assertEqual(len({r["slot_id"] for r in rows}), count)
            for row in rows:
                self.assertTrue(row["slot_id"])
                self.assertTrue(row["page_id"])
                self.assertEqual(len(row["row_sha256"]), 64)
                for field in MODULE.EMPTY_EVIDENCE_FIELDS[4:]:
                    self.assertEqual(row[field], "")
        self.assertFalse(MODULE.MODULE.audit()["print_approved"])

    def test_empty_evidence_rejects_stale_row_fingerprint(self):
        import csv
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "intake.csv"
            MODULE.export_empty_slot_evidence(path)
            self.assertEqual(MODULE.validate_empty_slot_evidence(path), [])
            with path.open(encoding="utf-8", newline="") as f:
                rows = list(csv.DictReader(f))
            rows[0]["row_sha256"] = "0" * 64
            with path.open("w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=MODULE.EMPTY_EVIDENCE_FIELDS)
                writer.writeheader()
                writer.writerows(rows)
            issues = MODULE.validate_empty_slot_evidence(path)
            self.assertTrue(any("stale or changed register row_sha256" in e for e in issues))

    def test_empty_evidence_validation_requires_page_specific_evidence(self):
        import csv
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "intake.csv"
            MODULE.export_empty_slot_evidence(path)
            self.assertEqual(MODULE.validate_empty_slot_evidence(path), [])
            with path.open(encoding="utf-8", newline="") as f:
                rows = list(csv.DictReader(f))
            p017 = next(r for r in rows if r["page_id"] == "QJ6-P017")
            p018 = next(r for r in rows if r["page_id"] == "QJ6-P018")
            p017["proposed_surah"] = "2"
            p018["proposed_surah"] = "2"
            with path.open("w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=MODULE.EMPTY_EVIDENCE_FIELDS)
                writer.writeheader()
                writer.writerows(rows)
            errors = MODULE.validate_empty_slot_evidence(path)
            self.assertTrue(any("waqf_sign_position" in x for x in errors))
            self.assertTrue(any("hafalan_unit_approval_id" in x for x in errors))

    def test_evidence_intake_detects_partial_record_without_surah(self):
        import csv
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "intake.csv"
            MODULE.export_empty_slot_evidence(path)
            with path.open(encoding="utf-8", newline="") as f:
                rows = list(csv.DictReader(f))
            rows[0]["reviewer_name"] = "Reviewer"
            with path.open("w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=MODULE.EMPTY_EVIDENCE_FIELDS)
                writer.writeheader()
                writer.writerows(rows)
            issues = MODULE.validate_empty_slot_evidence(path)
            self.assertTrue(any("proposed evidence missing proposed_surah" in x for x in issues))

    def test_validators_report_malformed_csv_rows_without_crashing(self):
        import csv
        with tempfile.TemporaryDirectory() as directory:
            for exporter, validator, fields in (
                (MODULE.export_review_worksheet, MODULE.validate_review_worksheet,
                 MODULE.FIELDS + MODULE.DECISION_FIELDS),
                (MODULE.export_empty_slot_evidence, MODULE.validate_empty_slot_evidence,
                 MODULE.EMPTY_EVIDENCE_FIELDS),
            ):
                path = Path(directory) / (fields[0] + str(len(fields)) + ".csv")
                exporter(path)
                with path.open(encoding="utf-8", newline="") as f:
                    rows = list(csv.reader(f))
                rows[1].append("unexpected-extra-column")
                rows[2] = rows[2][:-1]
                with path.open("w", encoding="utf-8", newline="") as f:
                    csv.writer(f).writerows(rows)
                issues = validator(path)
                self.assertTrue(any("malformed CSV field count" in issue for issue in issues))

    def test_evidence_rejects_invalid_surah_and_reversed_ayah_range(self):
        import csv
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "intake.csv"
            MODULE.export_empty_slot_evidence(path)
            with path.open(encoding="utf-8", newline="") as f:
                rows = list(csv.DictReader(f))
            row = next(r for r in rows if r["page_id"] == "QJ6-P017")
            row.update({
                "proposed_surah": "115", "proposed_ayah_start": "9",
                "proposed_ayah_end": "3", "mushaf_edition": "pending",
                "edition_page_or_link": "pending", "reviewer_name": "Reviewer",
                "decision_id": "pending", "prerequisite_and_duplicate_check": "pending",
                "waqf_sign_position": "pending",
            })
            with path.open("w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=MODULE.EMPTY_EVIDENCE_FIELDS)
                writer.writeheader()
                writer.writerows(rows)
            errors = MODULE.validate_empty_slot_evidence(path)
            self.assertTrue(any("surah number outside 1-114" in e for e in errors))
            self.assertTrue(any("invalid ayah range" in e for e in errors))

    def test_evidence_rejects_nonnumeric_surah_identifier(self):
        import csv
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "intake.csv"
            MODULE.export_empty_slot_evidence(path)
            with path.open(encoding="utf-8", newline="") as f:
                rows = list(csv.DictReader(f))
            row = next(r for r in rows if r["page_id"] == "QJ6-P018")
            row.update({
                "proposed_surah": "Al-Baqarah", "proposed_ayah_start": "1",
                "proposed_ayah_end": "2", "mushaf_edition": "pending",
                "edition_page_or_link": "pending", "reviewer_name": "Reviewer",
                "decision_id": "pending", "prerequisite_and_duplicate_check": "pending",
                "hafalan_unit_approval_id": "pending",
            })
            with path.open("w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=MODULE.EMPTY_EVIDENCE_FIELDS)
                writer.writeheader()
                writer.writerows(rows)
            errors = MODULE.validate_empty_slot_evidence(path)
            self.assertTrue(any("surah must be a numeric ID" in e for e in errors))

    def test_evidence_rejects_placeholder_as_primary_reference(self):
        import csv
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "intake.csv"
            MODULE.export_empty_slot_evidence(path)
            with path.open(encoding="utf-8", newline="") as f:
                rows = list(csv.DictReader(f))
            row = next(r for r in rows if r["page_id"] == "QJ6-P018")
            row.update({
                "proposed_surah": "2", "proposed_ayah_start": "1",
                "proposed_ayah_end": "2", "mushaf_edition": "pending",
                "edition_page_or_link": "TBD", "reviewer_name": "Reviewer",
                "decision_id": "TODO", "prerequisite_and_duplicate_check": "N/A",
                "hafalan_unit_approval_id": "pending",
            })
            with path.open("w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=MODULE.EMPTY_EVIDENCE_FIELDS)
                writer.writeheader()
                writer.writerows(rows)
            issues = MODULE.validate_empty_slot_evidence(path)
            self.assertTrue(any("placeholder is not evidence for mushaf_edition" in e for e in issues))
            self.assertTrue(any("placeholder is not evidence for hafalan_unit_approval_id" in e for e in issues))

    def test_review_decision_rejects_placeholder_evidence(self):
        import csv
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "worksheet.csv"
            MODULE.export_review_worksheet(path)
            with path.open(encoding="utf-8", newline="") as f:
                rows = list(csv.DictReader(f))
            row = next(r for r in rows if r["review_status"] == "CANDIDATE")
            row.update({
                "decision": "REVISE", "reviewer_name": "Reviewer",
                "review_date": "2026-11-09", "mushaf_edition": "pending",
                "evidence_reference": "TBD", "tajwid_rule": "TODO",
                "curriculum_evidence": "N/A",
            })
            with path.open("w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=MODULE.FIELDS + MODULE.DECISION_FIELDS)
                writer.writeheader()
                writer.writerows(rows)
            issues = MODULE.validate_review_worksheet(path)
            self.assertTrue(any("placeholder is not reviewer evidence for mushaf_edition" in e for e in issues))
            self.assertTrue(any("placeholder is not reviewer evidence for curriculum_evidence" in e for e in issues))

    def test_research_row_cannot_be_approved_without_register_revision(self):
        import csv
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "worksheet.csv"
            MODULE.export_review_worksheet(path)
            with path.open(encoding="utf-8", newline="") as f:
                rows = list(csv.DictReader(f))
            research = next(r for r in rows if r["review_status"] == "RESEARCH")
            research.update({
                "decision": "APPROVE", "reviewer_name": "Reviewer",
                "review_date": "2026-11-09", "mushaf_edition": "MSI",
                "evidence_reference": "page evidence", "tajwid_rule": "rule evidence",
                "curriculum_evidence": "curriculum evidence",
            })
            with path.open("w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=MODULE.FIELDS + MODULE.DECISION_FIELDS)
                writer.writeheader()
                writer.writerows(rows)
            issues = MODULE.validate_review_worksheet(path)
            self.assertTrue(any("research slot needs a revised register" in e for e in issues))

    def test_evidence_rejects_ayah_above_quran_wide_maximum(self):
        import csv
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "intake.csv"
            MODULE.export_empty_slot_evidence(path)
            with path.open(encoding="utf-8", newline="") as f:
                rows = list(csv.DictReader(f))
            row = next(r for r in rows if r["page_id"] == "QJ6-P018")
            row.update({
                "proposed_surah": "2", "proposed_ayah_start": "1",
                "proposed_ayah_end": "287", "mushaf_edition": "MSI",
                "edition_page_or_link": "source page", "reviewer_name": "Reviewer",
                "decision_id": "review-1", "prerequisite_and_duplicate_check": "checked",
                "hafalan_unit_approval_id": "curriculum-1",
            })
            with path.open("w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=MODULE.EMPTY_EVIDENCE_FIELDS)
                writer.writeheader()
                writer.writerows(rows)
            issues = MODULE.validate_empty_slot_evidence(path)
            self.assertTrue(any("Quran-wide maximum 286" in e for e in issues))

    def test_review_worksheet_rejects_orphaned_reviewer_fields(self):
        import csv
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "worksheet.csv"
            MODULE.export_review_worksheet(path)
            with path.open(encoding="utf-8", newline="") as f:
                rows = list(csv.DictReader(f))
            rows[0]["reviewer_name"] = "Reviewer"
            rows[0]["evidence_reference"] = "unreviewed source"
            with path.open("w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=MODULE.FIELDS + MODULE.DECISION_FIELDS)
                writer.writeheader()
                writer.writerows(rows)
            issues = MODULE.validate_review_worksheet(path)
            self.assertTrue(any("reviewer fields entered without a decision" in e for e in issues))

    def test_revise_and_reject_require_review_rationale(self):
        import csv
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "worksheet.csv"
            MODULE.export_review_worksheet(path)
            with path.open(encoding="utf-8", newline="") as f:
                rows = list(csv.DictReader(f))
            for row, decision in zip(rows[:2], ("REVISE", "REJECT")):
                row.update({
                    "decision": decision, "reviewer_name": "Reviewer",
                    "review_date": "2026-11-09", "mushaf_edition": "MSI",
                    "evidence_reference": "source page", "tajwid_rule": "rule evidence",
                    "curriculum_evidence": "curriculum reference",
                })
            with path.open("w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=MODULE.FIELDS + MODULE.DECISION_FIELDS)
                writer.writeheader()
                writer.writerows(rows)
            issues = MODULE.validate_review_worksheet(path)
            self.assertTrue(any("REVISE requires review_notes" in e for e in issues))
            self.assertTrue(any("REJECT requires review_notes" in e for e in issues))

    def test_queue_is_prioritized_and_exportable(self):
        queue = MODULE.build_queue()
        self.assertTrue(all(r["review_status"] == "EMPTY" for r in queue[:25]))
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "review.csv"
            self.assertEqual(MODULE.export(output), len(queue))
            self.assertIn("hold_reasons", output.read_text(encoding="utf-8"))
        self.assertFalse(MODULE.MODULE.audit()["print_approved"])


if __name__ == "__main__":
    unittest.main()
