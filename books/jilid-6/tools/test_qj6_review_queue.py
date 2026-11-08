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
