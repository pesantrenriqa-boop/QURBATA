#!/usr/bin/env python3
"""Regression gate for Jilid 1 Composer V3 output."""
from __future__ import annotations

import argparse
import csv
import importlib.util
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
LPE_PATH = ROOT / "content/qwo/lpe/runtime/lpe_engine_v1.py"
DEFAULT_PROGRESSION = ROOT / "content/qwo/lpe/JILID-1-40-PAGE-PROGRESSION-V2.csv"
DEFAULT_COMPOSITION = ROOT / "content/qwo/lpe/JILID-1-COMPOSITION-MATRIX-V1.csv"
DEFAULT_READING = ROOT / "content/qwo/composer/output/jilid-1-v3-lpe/JILID-1-READING-OBJECTS-V3.csv"
DEFAULT_METADATA = ROOT / "content/qwo/composer/output/jilid-1-v3-lpe/JILID-1-PAGE-METADATA-V3.csv"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"MODULE_IMPORT_FAILED: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


LPE = load_module(LPE_PATH, "qurbata_lpe_gate_v1")


def rows(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        raise FileNotFoundError(path)
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def load_composition(path: Path) -> dict[int, dict[str, int]]:
    result = {}
    for row in rows(path):
        page = int(row["Page"])
        result[page] = {key: int(row[key]) for key in ("L1New","L1Review","L2New","L2Review","L3New","L3Review")}
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--reading", default=str(DEFAULT_READING.relative_to(ROOT)))
    parser.add_argument("--metadata", default=str(DEFAULT_METADATA.relative_to(ROOT)))
    parser.add_argument("--progression", default=str(DEFAULT_PROGRESSION.relative_to(ROOT)))
    parser.add_argument("--composition", default=str(DEFAULT_COMPOSITION.relative_to(ROOT)))
    args = parser.parse_args()

    def resolve(value: str) -> Path:
        path = Path(value)
        return path if path.is_absolute() else ROOT / path

    reading = rows(resolve(args.reading))
    metadata = rows(resolve(args.metadata))
    progression = LPE.load_progression(resolve(args.progression))
    composition = load_composition(resolve(args.composition))
    issues: list[str] = []

    grouped: dict[int, list[dict[str, str]]] = defaultdict(list)
    for row in reading:
        grouped[int(row["Page"])].append(row)

    if sorted(grouped) != list(range(1, 41)):
        issues.append("PAGE_SEQUENCE_MUST_BE_1_TO_40")
    if len(reading) != 960:
        issues.append(f"TOTAL_ROWS expected=960 actual={len(reading)}")
    if len(metadata) != 40:
        issues.append(f"METADATA_ROWS expected=40 actual={len(metadata)}")

    prior_texts: set[str] = set()
    for page in range(1, 41):
        page_rows = grouped.get(page, [])
        if len(page_rows) != 24:
            issues.append(f"PAGE_OBJECT_COUNT page={page} actual={len(page_rows)}")
            continue
        if len({row["ArabicObject"] for row in page_rows}) != 24:
            issues.append(f"DUPLICATE_WITHIN_PAGE page={page}")
        if any(row["ObjectType"].upper() == "AWAIL_AL_SUWAR" for row in page_rows):
            issues.append(f"AWAILUS_SUWAR_FORBIDDEN page={page}")

        actual = Counter((int(row["UnitLength"]), row["LearningState"].upper()) for row in page_rows)
        expected = composition[page]
        mapping = {
            (1,"NEW"): expected["L1New"], (1,"REVIEW"): expected["L1Review"],
            (2,"NEW"): expected["L2New"], (2,"REVIEW"): expected["L2Review"],
            (3,"NEW"): expected["L3New"], (3,"REVIEW"): expected["L3Review"],
        }
        for key, count in mapping.items():
            if actual[key] != count:
                issues.append(f"COMPOSITION_MISMATCH page={page} key={key} expected={count} actual={actual[key]}")

        for row in page_rows:
            length = int(row["UnitLength"])
            if LPE.validate_page_object(page=page, object_type=row["ObjectType"], unit_length=length, rules=progression):
                issues.append(f"LPE_OBJECT_REJECTED page={page} slot={row['Slot']}")
            if not row["CompetencyCode"].strip() or not row["CompetencyDescription"].strip():
                issues.append(f"COMPETENCY_METADATA_MISSING page={page} slot={row['Slot']}")
            if row["LearningState"].upper() == "REVIEW" and row["ArabicObject"] not in prior_texts:
                issues.append(f"REVIEW_NOT_PREVIOUSLY_INTRODUCED page={page} slot={row['Slot']} text={row['ArabicObject']}")
        prior_texts.update(row["ArabicObject"] for row in page_rows if row["LearningState"].upper() == "NEW")

    metadata_by_page = {int(row["Page"]): row for row in metadata}
    for page in range(1, 41):
        row = metadata_by_page.get(page)
        if not row:
            issues.append(f"PAGE_METADATA_MISSING page={page}")
            continue
        if not row["CompetencyCodes"].strip() or not row["CompetencyDescriptions"].strip():
            issues.append(f"PAGE_COMPETENCY_DISPLAY_MISSING page={page}")
        if not row["MemorizationDescription"].strip():
            issues.append(f"MEMORIZATION_DESCRIPTION_MISSING page={page}")
        if not row["ArabicDescription"].strip():
            issues.append(f"ARABIC_DESCRIPTION_MISSING page={page}")
        expected_injection = progression[page].special_injection
        if row["SpecialInjection"].strip().upper() != expected_injection:
            issues.append(f"INJECTION_MISMATCH page={page} expected={expected_injection} actual={row['SpecialInjection']}")

    print(f"COMPOSER_ROWS={len(reading)}")
    print(f"COMPOSER_PAGES={len(grouped)}")
    print(f"LPE_OUTPUT_ISSUES={len(issues)}")
    print("PAGE20_INJECTION=" + (metadata_by_page.get(20, {}).get("SpecialInjection", "MISSING")))
    print("PAGE40_INJECTION=" + (metadata_by_page.get(40, {}).get("SpecialInjection", "MISSING")))
    if issues:
        for issue in issues[:50]:
            print("ISSUE=" + issue)
        print("JILID1_COMPOSER_LPE_GATE=FAIL")
        return 1
    print("AWAILUS_SUWAR=0")
    print("JILID1_COMPOSER_LPE_GATE=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
