import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).parents[2] / "scripts" / "quran" / "import_whole_quran_qwo.py"
SPEC = importlib.util.spec_from_file_location("qwo_importer", MODULE_PATH)
assert SPEC and SPEC.loader
qwo = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(qwo)


class QwoImporterRegressionTest(unittest.TestCase):
    def test_canonical_targets(self):
        cases = [
            ({"SHORT_VOWELS"}, 3, "QT-UK-009"),
            ({"MAD_ALIF"}, 3, "QT-UK-011"),
            ({"MAD_YA"}, 3, "QT-UK-014"),
            ({"MAD_WAW"}, 3, "QT-UK-015"),
            ({"TANWIN_FATH"}, 3, "QT-UK-019"),
            ({"TANWIN_DAMM"}, 3, "QT-UK-020"),
            ({"TANWIN_KASR"}, 3, "QT-UK-020"),
            ({"SHADDA"}, 3, "QT-UK-023"),
            ({"ALIF_MAQSURAH"}, 3, "QT-UK-032"),
        ]
        for tags, length, expected in cases:
            with self.subTest(tags=tags):
                self.assertEqual(qwo.target_competency(tags, length), expected)

    def test_minimum_volume_follows_framework(self):
        self.assertEqual(qwo.inferred_min_volume("QT-UK-009", 3), 2)
        self.assertEqual(qwo.inferred_min_volume("QT-UK-019", 3), 3)
        self.assertEqual(qwo.inferred_min_volume("QT-UK-020", 3), 4)
        self.assertEqual(qwo.inferred_min_volume("QT-UK-023", 3), 5)
        self.assertEqual(qwo.inferred_min_volume("QT-UK-032", 3), 6)

    def test_legacy_code_is_rejected(self):
        row = {
            "TargetCompetency": "QT-U-TANWIN",
            "RequiredCompetencies": "QT-UK-009",
            "AllowedFromJilid": 4,
            "Surah": 112,
            "Ayah": 1,
            "Status": "REVIEW",
            "SourceStatus": "QURAN_CANDIDATE",
        }
        errors = qwo.validate_generated_row(row)
        self.assertTrue(any("unknown target competency" in error for error in errors))

    def test_active_requires_verified_source(self):
        row = {
            "TargetCompetency": "QT-UK-020",
            "RequiredCompetencies": "QT-UK-019",
            "AllowedFromJilid": 4,
            "Surah": 112,
            "Ayah": 1,
            "Status": "ACTIVE",
            "SourceStatus": "QURAN_CANDIDATE",
        }
        errors = qwo.validate_generated_row(row)
        self.assertIn("ACTIVE object must have QURAN_VERIFIED source", errors)

    def test_early_volume_is_rejected(self):
        row = {
            "TargetCompetency": "QT-UK-023",
            "RequiredCompetencies": "QT-UK-020;QT-UK-021;QT-UK-022",
            "AllowedFromJilid": 4,
            "Surah": 112,
            "Ayah": 2,
            "Status": "HOLD",
            "SourceStatus": "QURAN_CANDIDATE",
        }
        errors = qwo.validate_generated_row(row)
        self.assertTrue(any("earlier than" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
