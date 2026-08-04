from pathlib import Path
import csv
import importlib.util

MODULE_PATH = Path(__file__).resolve().parents[2] / "scripts" / "quran" / "validate_qwo_seed.py"
spec = importlib.util.spec_from_file_location("validate_qwo_seed", MODULE_PATH)
validator = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(validator)


def write_csv(path: Path, row: dict[str, str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=validator.REQUIRED_COLUMNS)
        writer.writeheader()
        writer.writerow(row)


def valid_row() -> dict[str, str]:
    return {
        "QWO_ID": "QWO-000001",
        "ObjectType": "QWO",
        "ArabicTextUthmani": "خَلَقَ",
        "ArabicTextNormalized": "خلق",
        "Surah": "96",
        "Ayah": "2",
        "WordPosition": "1",
        "OccurrenceFrequency": "0",
        "LetterCount": "3",
        "FeatureTags": "SHORT_VOWELS",
        "TargetCompetency": "QT-UK-009",
        "RequiredCompetencies": "QT-UK-001;QT-UK-008",
        "CumulativeCompetencies": "QT-UK-001;QT-UK-008;QT-UK-009",
        "DifficultyScore": "22",
        "PedagogicalScore": "99",
        "AllowedFromJilid": "2",
        "AllowedFromPage": "1",
        "ReviewWeight": "99",
        "SourceType": "CURATED_QURAN_SEED",
        "SourceStatus": "QURAN_VERIFIED",
        "ReusePolicy": "UNIQUE_BLOCK_10",
        "Status": "REVIEW",
    }


def test_valid_seed_passes(tmp_path: Path) -> None:
    path = tmp_path / "seed.csv"
    write_csv(path, valid_row())
    assert validator.validate(path) == []


def test_legacy_code_is_rejected(tmp_path: Path) -> None:
    row = valid_row()
    row["TargetCompetency"] = "QT-U-009"
    path = tmp_path / "seed.csv"
    write_csv(path, row)
    errors = validator.validate(path)
    assert any("non-canonical competency code" in error for error in errors)


def test_active_requires_verified_source(tmp_path: Path) -> None:
    row = valid_row()
    row["Status"] = "ACTIVE"
    row["SourceStatus"] = "QURAN_CANDIDATE"
    path = tmp_path / "seed.csv"
    write_csv(path, row)
    errors = validator.validate(path)
    assert any("ACTIVE requires SourceStatus=QURAN_VERIFIED" in error for error in errors)


def test_volume_floor_is_enforced(tmp_path: Path) -> None:
    row = valid_row()
    row["TargetCompetency"] = "QT-UK-023"
    row["CumulativeCompetencies"] += ";QT-UK-023"
    row["AllowedFromJilid"] = "4"
    path = tmp_path / "seed.csv"
    write_csv(path, row)
    errors = validator.validate(path)
    assert any("minimum is 5" in error for error in errors)
