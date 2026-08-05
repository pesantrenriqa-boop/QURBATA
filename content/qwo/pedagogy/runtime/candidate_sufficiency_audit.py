#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DEFAULT_THRESHOLDS = ROOT / "content/qwo/pedagogy/CANDIDATE-MINIMUM-REQUIREMENTS-V1.csv"


def load_thresholds(path: Path) -> dict[str, int]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    return {row["CompetencyID"]: int(row["MinimumUniqueCandidates"]) for row in rows}


def audit(candidates_path: Path, thresholds_path: Path) -> tuple[list[dict[str, str]], bool]:
    thresholds = load_thresholds(thresholds_path)
    unique: dict[str, set[str]] = defaultdict(set)

    with candidates_path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        required = {"CompetencyID", "CanonicalKey", "Passed", "SourceRef"}
        missing = required - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"candidate file missing columns: {sorted(missing)}")
        for row in reader:
            if row["Passed"].strip().upper() != "PASS":
                continue
            if not row["SourceRef"].strip():
                continue
            unique[row["CompetencyID"].strip()].add(row["CanonicalKey"].strip())

    report: list[dict[str, str]] = []
    all_pass = True
    for cid in sorted(thresholds):
        available = len(unique.get(cid, set()))
        minimum = thresholds[cid]
        status = "PASS" if available >= minimum else "SHORTAGE"
        if status == "SHORTAGE":
            all_pass = False
        report.append({
            "CompetencyID": cid,
            "AvailableUniqueCandidates": str(available),
            "MinimumRequired": str(minimum),
            "Gap": str(max(0, minimum - available)),
            "Status": status,
        })
    return report, all_pass


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("candidates", type=Path, help="CSV hasil pelabelan corpus")
    parser.add_argument("--thresholds", type=Path, default=DEFAULT_THRESHOLDS)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    report, all_pass = audit(args.candidates, args.thresholds)
    output = args.output
    if output:
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(report[0]))
            writer.writeheader()
            writer.writerows(report)
    for row in report:
        print(",".join(row.values()))
    print("READY_CANDIDATE_POOL" if all_pass else "SHORTAGE_DETECTED")
    return 0 if all_pass else 2


if __name__ == "__main__":
    raise SystemExit(main())
