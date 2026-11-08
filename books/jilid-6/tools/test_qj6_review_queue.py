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
