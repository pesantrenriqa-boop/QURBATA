#!/usr/bin/env python3
from __future__ import annotations

import csv
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DEPENDENCY = ROOT / "content/qwo/competency/QURBATA-COMPETENCY-DEPENDENCY-MAP-V1.csv"
FIXTURES = ROOT / "content/qwo/pedagogy/tests/REAL-OBJECT-ACCEPTANCE-FIXTURES-V1.csv"


def fail(message: str) -> None:
    raise AssertionError(message)


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> int:
    competencies = load_csv(DEPENDENCY)
    fixtures = load_csv(FIXTURES)
    expected_ids = [row["CompetencyID"].strip() for row in competencies]
    positive = defaultdict(int)
    negative = defaultdict(int)

    for row in fixtures:
        cid = row["CompetencyID"].strip()
        if row["Expected"].strip() == "PASS":
            positive[cid] += 1
        else:
            negative[cid] += 1

    missing_positive = [cid for cid in expected_ids if positive[cid] == 0]
    if missing_positive:
        fail(f"Competencies without positive real-object fixture: {missing_positive}")

    unknown = sorted((set(positive) | set(negative)) - set(expected_ids))
    if unknown:
        fail(f"Fixtures reference unknown competencies: {unknown}")

    print(f"PASS positive coverage: {len(expected_ids)}/{len(expected_ids)} competencies")
    print(f"Negative fixtures available for {sum(1 for cid in expected_ids if negative[cid])} competencies")
    print("QURBATA competency coverage gate: VERIFIED_PASS")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
