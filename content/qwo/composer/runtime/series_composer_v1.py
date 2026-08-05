#!/usr/bin/env python3
"""Compose QURBATA volumes 1-8 from labeled Quran objects.

The composer is deterministic, dependency-aware, and never silently repeats a
CanonicalKey. A shortage raises an explicit error instead of borrowing a later
competency.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DEFAULT_LABELED = ROOT / "content/qwo/production/generated/LABELED-QURAN-OBJECTS-V1.csv"
DEFAULT_ALLOCATION = ROOT / "content/qwo/composer/SERIES-COMPETENCY-ALLOCATION-V1.csv"


def load_csv(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        raise FileNotFoundError(f"REQUIRED_FILE_NOT_FOUND {path}")
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def competency_range(start: str, end: str) -> list[str]:
    first, last = int(start[1:]), int(end[1:])
    return [f"C{number:04d}" for number in range(first, last + 1)]


def stable_score(volume: int, cid: str, key: str) -> str:
    return hashlib.sha256(f"{volume}|{cid}|{key}".encode("utf-8")).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--labeled", default=str(DEFAULT_LABELED.relative_to(ROOT)))
    parser.add_argument("--allocation", default=str(DEFAULT_ALLOCATION.relative_to(ROOT)))
    parser.add_argument("--objects-per-competency", type=int, default=24)
    parser.add_argument("--output", default="content/qwo/production/generated/QURBATA-1-8-COMPOSITION-V1.csv")
    args = parser.parse_args()

    labeled_path = Path(args.labeled)
    labeled_path = labeled_path if labeled_path.is_absolute() else ROOT / labeled_path
    allocation_path = Path(args.allocation)
    allocation_path = allocation_path if allocation_path.is_absolute() else ROOT / allocation_path
    output_path = Path(args.output)
    output_path = output_path if output_path.is_absolute() else ROOT / output_path

    labeled = load_csv(labeled_path)
    allocation = load_csv(allocation_path)
    pools: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in labeled:
        pools[row["CompetencyID"]].append(row)

    used: set[str] = set()
    output: list[dict[str, str]] = []
    page = 0
    for volume_row in allocation:
        volume = int(volume_row["Volume"])
        for cid in competency_range(volume_row["CompetencyStart"], volume_row["CompetencyEnd"]):
            candidates = sorted(
                (row for row in pools.get(cid, []) if row["CanonicalKey"] not in used),
                key=lambda row: stable_score(volume, cid, row["CanonicalKey"]),
            )
            required = args.objects_per_competency
            if len(candidates) < required:
                raise RuntimeError(
                    f"SHORTAGE volume={volume} competency={cid} required={required} available={len(candidates)}"
                )
            selected = candidates[:required]
            page += 1
            for position, row in enumerate(selected, start=1):
                used.add(row["CanonicalKey"])
                output.append({
                    "Volume": str(volume),
                    "PageSequence": str(page),
                    "CompetencyID": cid,
                    "Position": str(position),
                    "CanonicalKey": row["CanonicalKey"],
                    "ObjectType": row["ObjectType"],
                    "Text": row["Text"],
                    "SourceRef": row["SourceRef"],
                })

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=[
            "Volume", "PageSequence", "CompetencyID", "Position",
            "CanonicalKey", "ObjectType", "Text", "SourceRef",
        ])
        writer.writeheader()
        writer.writerows(output)

    print(f"COMPOSITION_ROWS={len(output)}")
    print(f"UNIQUE_OBJECTS={len(used)}")
    print(f"OUTPUT={output_path}")
    print("SERIES_COMPOSER_STATUS=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
