#!/usr/bin/env python3
"""Regression gate for Jilid 1 Composer v4 output."""
from __future__ import annotations

import argparse
import csv
import importlib.util
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
LPE_PATH = ROOT / "content/qwo/lpe/runtime/lpe_engine_v1.py"
PED_PATH = ROOT / "content/qwo/pedagogy/runtime/pedagogical_engine.py"
RULES_PATH = ROOT / "content/qwo/pedagogy/PEDAGOGICAL-RULE-MATRIX-V1.csv"
DEFAULT_PROGRESSION = ROOT / "content/qwo/lpe/JILID-1-40-PAGE-PROGRESSION-V2.csv"
DEFAULT_COMPOSITION = ROOT / "content/qwo/lpe/JILID-1-COMPOSITION-MATRIX-V2.csv"
DEFAULT_READING = ROOT / "content/qwo/composer/output/jilid-1-v4-lpe/JILID-1-READING-OBJECTS-V4.csv"
DEFAULT_METADATA = ROOT / "content/qwo/composer/output/jilid-1-v4-lpe/JILID-1-PAGE-METADATA-V4.csv"
DEFAULT_INJECTION = ROOT / "content/qwo/composer/output/jilid-1-v4-lpe/JILID-1-INJECTION-CONTENT-V4.csv"
SPECIAL_PAGES = {20, 40}


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"MODULE_IMPORT_FAILED: {path}")
    module = importlib.util.module_from_spec(spec); sys.modules[name] = module; spec.loader.exec_module(module); return module


LPE = load_module(LPE_PATH, "qurbata_lpe_gate_v2")
PED = load_module(PED_PATH, "qurbata_ped_gate_v2")
PED_RULES = PED.load_rules(RULES_PATH)


def rows(path: Path) -> list[dict[str, str]]:
    if not path.is_file(): raise FileNotFoundError(path)
    with path.open(encoding="utf-8-sig", newline="") as handle: return list(csv.DictReader(handle))


def resolve(value: str) -> Path:
    path = Path(value); return path if path.is_absolute() else ROOT / path


def load_composition(path: Path) -> dict[int, dict[str, int]]:
    result = {}
    for row in rows(path):
        page = int(row["Page"])
        result[page] = {key: int(row[key]) for key in ("L1New","L1Review","L2New","L2Review","L3New","L3Review")}
    return result


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--reading", default=str(DEFAULT_READING.relative_to(ROOT)))
    ap.add_argument("--metadata", default=str(DEFAULT_METADATA.relative_to(ROOT)))
    ap.add_argument("--injection", default=str(DEFAULT_INJECTION.relative_to(ROOT)))
    ap.add_argument("--progression", default=str(DEFAULT_PROGRESSION.relative_to(ROOT)))
    ap.add_argument("--composition", default=str(DEFAULT_COMPOSITION.relative_to(ROOT)))
    args = ap.parse_args()

    reading, metadata, injection = rows(resolve(args.reading)), rows(resolve(args.metadata)), rows(resolve(args.injection))
    progression = LPE.load_progression(resolve(args.progression)); composition = load_composition(resolve(args.composition))
    issues: list[str] = []
    grouped: dict[int, list[dict[str, str]]] = defaultdict(list)
    for row in reading: grouped[int(row["Page"])].append(row)

    if len(reading) != 912: issues.append(f"TOTAL_READING_ROWS expected=912 actual={len(reading)}")
    if len(metadata) != 40: issues.append(f"METADATA_ROWS expected=40 actual={len(metadata)}")
    if len(injection) != 28: issues.append(f"LETTER_NAME_ROWS expected=28 actual={len(injection)}")
    if set(grouped) != set(range(1,41)) - SPECIAL_PAGES: issues.append(f"READING_PAGE_SET_INVALID actual={sorted(grouped)}")

    prior_texts: set[str] = set()
    for page in range(1,41):
        page_rows = grouped.get(page, [])
        expected_count = 0 if page in SPECIAL_PAGES else 24
        if len(page_rows) != expected_count: issues.append(f"PAGE_OBJECT_COUNT page={page} expected={expected_count} actual={len(page_rows)}")
        if not page_rows: continue
        if len({r["ArabicObject"] for r in page_rows}) != len(page_rows): issues.append(f"DUPLICATE_WITHIN_PAGE page={page}")
        if any(r["ObjectType"].upper()=="AWAIL_AL_SUWAR" for r in page_rows): issues.append(f"AWAILUS_SUWAR_FORBIDDEN page={page}")
        actual = Counter((int(r["UnitLength"]), r["LearningState"].upper()) for r in page_rows)
        expected = composition[page]
        mapping = {(1,"NEW"):expected["L1New"],(1,"REVIEW"):expected["L1Review"],(2,"NEW"):expected["L2New"],(2,"REVIEW"):expected["L2Review"],(3,"NEW"):expected["L3New"],(3,"REVIEW"):expected["L3Review"]}
        for key,count in mapping.items():
            if actual[key] != count: issues.append(f"COMPOSITION_MISMATCH page={page} key={key} expected={count} actual={actual[key]}")
        for r in page_rows:
            length = int(r["UnitLength"])
            if LPE.validate_page_object(page=page, object_type=r["ObjectType"], unit_length=length, rules=progression): issues.append(f"LPE_OBJECT_REJECTED page={page} slot={r['Slot']}")
            if not r["CompetencyCode"].strip() or not r["CompetencyDescription"].strip(): issues.append(f"COMPETENCY_METADATA_MISSING page={page} slot={r['Slot']}")
            if not PED.validate(r["ArabicObject"], r["ObjectType"], r["CompetencyCode"], PED_RULES).passed: issues.append(f"PEDAGOGICAL_RULE_REJECTED page={page} slot={r['Slot']} text={r['ArabicObject']}")
            if r["LearningState"].upper()=="REVIEW" and r["ArabicObject"] not in prior_texts: issues.append(f"REVIEW_NOT_PREVIOUSLY_INTRODUCED page={page} slot={r['Slot']}")
        prior_texts.update(r["ArabicObject"] for r in page_rows if r["LearningState"].upper()=="NEW")

    metadata_by_page = {int(r["Page"]):r for r in metadata}
    for page in range(1,41):
        row = metadata_by_page.get(page)
        if not row: issues.append(f"PAGE_METADATA_MISSING page={page}"); continue
        if not row["CompetencyCodes"].strip() or not row["CompetencyDescriptions"].strip(): issues.append(f"PAGE_COMPETENCY_DISPLAY_MISSING page={page}")
        if not row["MemorizationDescription"].strip(): issues.append(f"MEMORIZATION_DESCRIPTION_MISSING page={page}")
        if not row["ArabicDescription"].strip(): issues.append(f"ARABIC_DESCRIPTION_MISSING page={page}")
        if row["SpecialInjection"].strip().upper() != progression[page].special_injection: issues.append(f"INJECTION_MISMATCH page={page}")

    injection_counts = Counter(int(r["Page"]) for r in injection)
    if injection_counts != Counter({20:14,40:14}): issues.append(f"LETTER_NAME_DISTRIBUTION actual={dict(injection_counts)}")
    if any(r["ContentType"] != "LETTER_NAME" for r in injection): issues.append("INJECTION_CONTENT_TYPE_INVALID")

    print(f"COMPOSER_READING_ROWS={len(reading)}")
    print(f"READING_PAGES={len(grouped)}")
    print(f"LETTER_NAME_ROWS={len(injection)}")
    print(f"LPE_OUTPUT_ISSUES={len(issues)}")
    print(f"PAGE20_READING_OBJECTS={len(grouped.get(20,[]))}")
    print(f"PAGE40_READING_OBJECTS={len(grouped.get(40,[]))}")
    print(f"PAGE20_LETTER_NAMES={injection_counts[20]}")
    print(f"PAGE40_LETTER_NAMES={injection_counts[40]}")
    if issues:
        for issue in issues[:60]: print("ISSUE="+issue)
        print("JILID1_COMPOSER_LPE_GATE_V2=FAIL"); return 1
    print("AWAILUS_SUWAR=0")
    print("JILID1_COMPOSER_LPE_GATE_V2=PASS"); return 0

if __name__ == "__main__":
    raise SystemExit(main())
