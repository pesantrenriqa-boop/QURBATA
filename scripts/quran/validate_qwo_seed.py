#!/usr/bin/env python3
"""Validate curated QURBATA Word Object seed CSV files.

This validator is intentionally stricter than the whole-Quran importer. It is
used for small curated datasets that may later be promoted to ACTIVE and fed to
the page generator.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

REQUIRED_COLUMNS = [
    "QWO_ID", "ObjectType", "ArabicTextUthmani", "ArabicTextNormalized",
    "Surah", "Ayah", "WordPosition", "OccurrenceFrequency", "LetterCount",
    "FeatureTags", "TargetCompetency", "RequiredCompetencies",
    "CumulativeCompetencies", "DifficultyScore", "PedagogicalScore",
    "AllowedFromJilid", "AllowedFromPage", "ReviewWeight", "SourceType",
    "SourceStatus", "ReusePolicy", "Status",
]

VALID_STATUSES = {"ACTIVE", "REVIEW", "HOLD", "DEPRECATED"}
VALID_SOURCE_STATUSES = {"QURAN_VERIFIED", "QURAN_CANDIDATE", "HOLD"}
VALID_REUSE_POLICIES = {"UNIQUE_BLOCK_10", "REUSE_ALLOWED", "HOLD"}
CODE_RE = re.compile(r"^QT-UK-\d{3}$")
QWO_RE = re.compile(r"^QWO-\d{6}$")
ARABIC_RE = re.compile(r"[\u0600-\u06ff]")

MIN_VOLUME = {
    "QT-UK-001": 1, "QT-UK-002": 1, "QT-UK-003": 1, "QT-UK-004": 1,
    "QT-UK-005": 1, "QT-UK-006": 1, "QT-UK-007": 1, "QT-UK-008": 1,
    "QT-UK-009": 2, "QT-UK-010": 2, "QT-UK-011": 2, "QT-UK-012": 2,
    "QT-UK-013": 2, "QT-UK-014": 3, "QT-UK-015": 3, "QT-UK-016": 3,
    "QT-UK-017": 3, "QT-UK-018": 3, "QT-UK-019": 3, "QT-UK-020": 4,
    "QT-UK-021": 4, "QT-UK-022": 4, "QT-UK-023": 5, "QT-UK-024": 4,
    "QT-UK-025": 5, "QT-UK-026": 1, "QT-UK-027": 1, "QT-UK-028": 6,
    "QT-UK-029": 7, "QT-UK-030": 8, "QT-UK-031": 3, "QT-UK-032": 6,
    "QT-UK-033": 4, "QT-UK-034": 5,
}


def split_codes(value: str) -> list[str]:
    return [part.strip() for part in value.replace("|", ";").split(";") if part.strip()]


def as_int(row_no: int, row: dict[str, str], field: str, low: int, high: int, errors: list[str]) -> int | None:
    try:
        value = int(row.get(field, ""))
    except ValueError:
        errors.append(f"row {row_no}: {field} must be an integer")
        return None
    if not low <= value <= high:
        errors.append(f"row {row_no}: {field} must be between {low} and {high}")
    return value


def validate_row(row_no: int, row: dict[str, str], seen_ids: set[str], errors: list[str]) -> None:
    qwo_id = row.get("QWO_ID", "").strip()
    if not QWO_RE.fullmatch(qwo_id):
        errors.append(f"row {row_no}: invalid QWO_ID {qwo_id!r}")
    elif qwo_id in seen_ids:
        errors.append(f"row {row_no}: duplicate QWO_ID {qwo_id}")
    seen_ids.add(qwo_id)

    if row.get("ObjectType") != "QWO":
        errors.append(f"row {row_no}: ObjectType must be QWO")
    if not ARABIC_RE.search(row.get("ArabicTextUthmani", "")):
        errors.append(f"row {row_no}: ArabicTextUthmani must contain Arabic text")
    if not row.get("ArabicTextNormalized", "").strip():
        errors.append(f"row {row_no}: ArabicTextNormalized is required")

    as_int(row_no, row, "Surah", 1, 114, errors)
    as_int(row_no, row, "Ayah", 1, 286, errors)
    as_int(row_no, row, "WordPosition", 1, 999, errors)
    as_int(row_no, row, "OccurrenceFrequency", 1, 999999, errors)
    as_int(row_no, row, "LetterCount", 1, 99, errors)
    as_int(row_no, row, "DifficultyScore", 1, 100, errors)
    as_int(row_no, row, "PedagogicalScore", 1, 100, errors)
    volume = as_int(row_no, row, "AllowedFromJilid", 1, 8, errors)
    as_int(row_no, row, "AllowedFromPage", 1, 40, errors)
    as_int(row_no, row, "ReviewWeight", 1, 100, errors)

    target = row.get("TargetCompetency", "").strip()
    required = split_codes(row.get("RequiredCompetencies", ""))
    cumulative = split_codes(row.get("CumulativeCompetencies", ""))
    for code in [target, *required, *cumulative]:
        if not CODE_RE.fullmatch(code):
            errors.append(f"row {row_no}: non-canonical competency code {code!r}")
        elif code not in MIN_VOLUME:
            errors.append(f"row {row_no}: unknown competency code {code}")

    if target and target not in cumulative:
        errors.append(f"row {row_no}: target must be included in CumulativeCompetencies")
    if not set(required).issubset(cumulative):
        errors.append(f"row {row_no}: RequiredCompetencies must be a subset of CumulativeCompetencies")
    if volume is not None and target in MIN_VOLUME and volume < MIN_VOLUME[target]:
        errors.append(
            f"row {row_no}: {target} cannot start in Jilid {volume}; minimum is {MIN_VOLUME[target]}"
        )

    status = row.get("Status", "")
    source_status = row.get("SourceStatus", "")
    if status not in VALID_STATUSES:
        errors.append(f"row {row_no}: invalid Status {status!r}")
    if source_status not in VALID_SOURCE_STATUSES:
        errors.append(f"row {row_no}: invalid SourceStatus {source_status!r}")
    if row.get("ReusePolicy", "") not in VALID_REUSE_POLICIES:
        errors.append(f"row {row_no}: invalid ReusePolicy {row.get('ReusePolicy')!r}")
    if status == "ACTIVE" and source_status != "QURAN_VERIFIED":
        errors.append(f"row {row_no}: ACTIVE requires SourceStatus=QURAN_VERIFIED")
    if status == "ACTIVE" and not required:
        errors.append(f"row {row_no}: ACTIVE requires explicit RequiredCompetencies")


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames != REQUIRED_COLUMNS:
            missing = [name for name in REQUIRED_COLUMNS if name not in (reader.fieldnames or [])]
            extra = [name for name in (reader.fieldnames or []) if name not in REQUIRED_COLUMNS]
            errors.append(f"header mismatch; missing={missing}, extra={extra}")
            return errors
        seen_ids: set[str] = set()
        for row_no, row in enumerate(reader, start=2):
            validate_row(row_no, row, seen_ids, errors)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_file", type=Path)
    args = parser.parse_args()
    errors = validate(args.csv_file)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"FAILED: {len(errors)} validation error(s)", file=sys.stderr)
        return 1
    print(f"VALID: {args.csv_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
