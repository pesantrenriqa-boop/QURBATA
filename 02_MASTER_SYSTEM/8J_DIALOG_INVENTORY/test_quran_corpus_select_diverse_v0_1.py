#!/usr/bin/env python3
"""Deterministic selection tests; synthetic words, not Quran citations."""
import importlib.util
import unittest
from pathlib import Path

module_path = Path(__file__).with_name("quran_corpus_select_diverse_v0_1.py")
spec = importlib.util.spec_from_file_location("diverse", module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class DiverseTests(unittest.TestCase):
    def test_distinct_words_and_surahs(self):
        data = [
            {"surah": 1, "ayah": 1, "token_index": 1, "exact_uthmani": "A"},
            {"surah": 1, "ayah": 2, "token_index": 1, "exact_uthmani": "A"},
            {"surah": 2, "ayah": 1, "token_index": 1, "exact_uthmani": "B"},
            {"surah": 3, "ayah": 1, "token_index": 1, "exact_uthmani": "C"},
        ]
        selected = module.select_diverse(data, 3)
        self.assertEqual(len(selected), 3)
        self.assertEqual(len({x["exact_uthmani"] for x in selected}), 3)
        self.assertEqual(len({x["surah"] for x in selected}), 3)

    def test_limit_and_stability(self):
        data = [
            {"surah": 2, "ayah": 1, "token_index": 1, "exact_uthmani": "B"},
            {"surah": 1, "ayah": 1, "token_index": 1, "exact_uthmani": "A"},
        ]
        self.assertEqual(module.select_diverse(data, 1), module.select_diverse(list(reversed(data)), 1))
        self.assertEqual(len(module.select_diverse(data, 1)), 1)

if __name__ == "__main__":
    unittest.main()
