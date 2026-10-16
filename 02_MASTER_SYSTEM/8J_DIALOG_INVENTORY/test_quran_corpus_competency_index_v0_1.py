#!/usr/bin/env python3
"""Offline regression tests for QURBATA corpus indexing (no mushaf data shipped)."""
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MODULE = ROOT / "quran_corpus_competency_index_v0_1.py"
spec = importlib.util.spec_from_file_location("qurbata_index", MODULE)
index = importlib.util.module_from_spec(spec)
spec.loader.exec_module(index)

class IndexTests(unittest.TestCase):
    def test_features_are_candidates_not_verification(self):
        self.assertIn("tanwin_fath", index.features("أَفْوَاجًا"))
        self.assertIn("tanwin_kasr", index.features("خَوْفٍ"))
        self.assertIn("tanwin_damm", index.features("سَلَامٌ"))
        self.assertIn("mad_alif_candidate", index.features("قَالَ"))
        self.assertIn("mad_ya_candidate", index.features("الرَّحِيمِ"))
        self.assertIn("mad_waw_candidate", index.features("يَقُولُ"))

    def test_small_fixture_and_provenance(self):
        with tempfile.TemporaryDirectory() as td:
            source = Path(td) / "sample.tsv"
            target = Path(td) / "out"
            source.write_text(
                "surah\tayah\ttoken_index\tuthmani\n"
                "1\t1\t1\tسَلَامٌ\n"
                "2\t1\t1\tقَالَ\n", encoding="utf-8")
            run = subprocess.run([sys.executable, str(MODULE), str(source), str(target)],
                                 capture_output=True, text=True)
            self.assertEqual(run.returncode, 0, run.stderr)
            report = json.loads((target / "report.json").read_text(encoding="utf-8"))
            self.assertEqual(report["token_occurrences"], 2)
            self.assertEqual(report["surahs_seen"], 2)
            self.assertFalse(report["surah_coverage_complete"])
            self.assertIn(3, report["missing_surahs"])
            self.assertEqual(len(report["source_file_sha256"]), 64)
            self.assertEqual(report["status"], "AUTO-CANDIDATE / NOT FOR PRINT")

    def test_duplicate_location_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            source = Path(td) / "dup.tsv"
            source.write_text(
                "surah\tayah\ttoken_index\tuthmani\n"
                "1\t1\t1\tقَالَ\n1\t1\t1\tكَانَ\n", encoding="utf-8")
            run = subprocess.run([sys.executable, str(MODULE), str(source), str(Path(td) / "out")],
                                 capture_output=True, text=True)
            self.assertNotEqual(run.returncode, 0)
            self.assertIn("Duplicate location", run.stderr)

if __name__ == "__main__":
    unittest.main()
