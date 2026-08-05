#!/usr/bin/env python3
"""Label generated Quran objects and audit candidate sufficiency C0001-C0041."""
from __future__ import annotations

import argparse
import csv
import importlib.util
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
ENGINE_PATH = ROOT / "content/qwo/pedagogy/runtime/pedagogical_engine.py"
RULES_PATH = ROOT / "content/qwo/pedagogy/PEDAGOGICAL-RULE-MATRIX-V1.csv"
MINIMUMS_PATH = ROOT / "content/qwo/pedagogy/CANDIDATE-MINIMUM-REQUIREMENTS-V1.csv"
DEFAULT_OBJECTS = ROOT / "content/qwo/production/generated/MASTER-QURAN-OBJECTS-V1.csv"
TYPE_MAP = {"QWO": "WORD", "QPO": "PHRASE", "AYAH_FRAGMENT": "AYAH_FRAGMENT", "FULL_AYAH": "FULL_AYAH"}


def load_engine():
    spec = importlib.util.spec_from_file_location("qurbata_pedagogical_engine", ENGINE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("ENGINE_IMPORT_FAILED")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def load_csv(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        raise FileNotFoundError(f"REQUIRED_FILE_NOT_FOUND {path}")
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def compatible_type(object_type: str, cid: str) -> str:
    if cid.startswith("C000") and cid <= "C0006":
        return "WORD_FRAGMENT" if cid in {"C0005", "C0006"} else "LETTER"
    return TYPE_MAP.get(object_type, object_type)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--objects", default=str(DEFAULT_OBJECTS.relative_to(ROOT)))
    parser.add_argument("--labeled-output", default="content/qwo/production/generated/LABELED-QURAN-OBJECTS-V1.csv")
    parser.add_argument("--report-output", default="content/qwo/production/generated/CANDIDATE-SUFFICIENCY-REPORT-V1.csv")
    args = parser.parse_args()

    objects_path = Path(args.objects)
    objects_path = objects_path if objects_path.is_absolute() else ROOT / objects_path
    try:
        objects = load_csv(objects_path)
        minimum_rows = load_csv(MINIMUMS_PATH)
        engine = load_engine()
        rules = engine.load_rules(RULES_PATH)
    except (FileNotFoundError, RuntimeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2

    labels: list[dict[str, str]] = []
    unique_by_competency: dict[str, set[str]] = defaultdict(set)
    for obj in objects:
        raw_type = obj["ObjectType"]
        for cid in sorted(rules):
            object_type = compatible_type(raw_type, cid)
            decision = engine.validate(obj["Text"], object_type, cid, rules)
            if decision.passed:
                labels.append({
                    "CanonicalKey": obj["CanonicalKey"],
                    "ObjectType": raw_type,
                    "Text": obj["Text"],
                    "SourceRef": obj["SourceRef"],
                    "CompetencyID": cid,
                })
                unique_by_competency[cid].add(obj["CanonicalKey"])

    labeled_path = Path(args.labeled_output)
    labeled_path = labeled_path if labeled_path.is_absolute() else ROOT / labeled_path
    labeled_path.parent.mkdir(parents=True, exist_ok=True)
    with labeled_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["CanonicalKey", "ObjectType", "Text", "SourceRef", "CompetencyID"])
        writer.writeheader()
        writer.writerows(labels)

    report: list[dict[str, str]] = []
    shortages = 0
    for row in minimum_rows:
        cid = row["CompetencyID"]
        minimum = int(row["MinimumUniqueCandidates"])
        actual = len(unique_by_competency.get(cid, set()))
        status = "PASS" if actual >= minimum else "SHORTAGE"
        shortages += status == "SHORTAGE"
        report.append({
            "CompetencyID": cid,
            "MinimumUniqueCandidates": str(minimum),
            "ActualUniqueCandidates": str(actual),
            "Status": status,
            "Gap": str(max(0, minimum - actual)),
        })

    report_path = Path(args.report_output)
    report_path = report_path if report_path.is_absolute() else ROOT / report_path
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with report_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["CompetencyID", "MinimumUniqueCandidates", "ActualUniqueCandidates", "Status", "Gap"])
        writer.writeheader()
        writer.writerows(report)

    print(f"OBJECTS={len(objects)}")
    print(f"LABEL_ROWS={len(labels)}")
    print(f"SHORTAGE_COMPETENCIES={shortages}")
    print(f"REPORT={report_path}")
    if shortages:
        print("CANDIDATE_POOL_STATUS=SHORTAGE")
        return 3
    print("CANDIDATE_POOL_STATUS=READY_CANDIDATE_POOL")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
