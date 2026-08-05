#!/usr/bin/env python3
"""Final readiness gate for generating QURBATA volumes 1-8."""
from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
REPORT = ROOT / "content/qwo/production/generated/CANDIDATE-SUFFICIENCY-REPORT-V1.csv"
COMPOSITION = ROOT / "content/qwo/production/generated/QURBATA-1-8-COMPOSITION-V1.csv"
EXPECTED_COMPETENCIES = {f"C{i:04d}" for i in range(1, 42)}
EXPECTED_VOLUMES = {str(i) for i in range(1, 9)}


def load(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        raise RuntimeError(f"MISSING_FILE {path}")
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> int:
    try:
        report = load(REPORT)
        composition = load(COMPOSITION)
    except RuntimeError as exc:
        print(exc, file=sys.stderr)
        return 2

    report_ids = {row.get("CompetencyID", "") for row in report}
    shortages = [row for row in report if row.get("Status") != "PASS"]
    if report_ids != EXPECTED_COMPETENCIES:
        print("READINESS_FAIL competency_report_incomplete", file=sys.stderr)
        return 3
    if shortages:
        print(f"READINESS_FAIL shortage_count={len(shortages)}", file=sys.stderr)
        return 4

    if not composition:
        print("READINESS_FAIL empty_composition", file=sys.stderr)
        return 5

    volumes = {row.get("Volume", "") for row in composition}
    competencies = {row.get("CompetencyID", "") for row in composition}
    keys = [row.get("CanonicalKey", "") for row in composition]
    sources = [row.get("SourceRef", "") for row in composition]
    positions = Counter((row.get("Volume", ""), row.get("PageSequence", "")) for row in composition)

    if volumes != EXPECTED_VOLUMES:
        print(f"READINESS_FAIL volumes={sorted(volumes)}", file=sys.stderr)
        return 6
    if competencies != EXPECTED_COMPETENCIES:
        print("READINESS_FAIL composition_competency_coverage", file=sys.stderr)
        return 7
    if len(keys) != len(set(keys)):
        print("READINESS_FAIL duplicate_canonical_key", file=sys.stderr)
        return 8
    if any(not source or ":" not in source for source in sources):
        print("READINESS_FAIL invalid_source_ref", file=sys.stderr)
        return 9
    if any(count != 24 for count in positions.values()):
        print("READINESS_FAIL page_object_count", file=sys.stderr)
        return 10

    print(f"COMPOSITION_ROWS={len(composition)}")
    print(f"UNIQUE_OBJECTS={len(set(keys))}")
    print(f"VOLUMES={len(volumes)}")
    print(f"COMPETENCIES={len(competencies)}")
    print("READY_TO_GENERATE_QURBATA_1_8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
