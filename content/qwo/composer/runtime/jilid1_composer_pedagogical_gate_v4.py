#!/usr/bin/env python3
"""Regression gate for Jilid 1 Composer v6 pedagogical contract."""
from __future__ import annotations

import argparse
import csv
import importlib.util
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
PUE_PATH = ROOT / "content/qwo/pedagogy/runtime/pedagogical_unit_engine.py"
PROGRESSION = ROOT / "content/qwo/lpe/JILID-1-PEDAGOGICAL-PROGRESSION-V3.csv"
DEFAULT_DIR = ROOT / "content/qwo/composer/output/jilid-1-v6-pedagogical"
SPECIAL_PAGES = {20, 40}
MARKS = {"FATHAH": "َ", "KASRAH": "ِ", "DHAMMAH": "ُ"}


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"MODULE_IMPORT_FAILED: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


PUE = load_module(PUE_PATH, "qurbata_pue_gate_v4")


def rows(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        raise FileNotFoundError(path)
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def base_family(base: str) -> str:
    return "ا" if base in {"أ", "إ", "آ", "ٱ"} else base


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default=str(DEFAULT_DIR.relative_to(ROOT)))
    args = parser.parse_args()
    output_dir = Path(args.output_dir)
    output_dir = output_dir if output_dir.is_absolute() else ROOT / output_dir

    reading = rows(output_dir / "JILID-1-READING-OBJECTS-V6.csv")
    metadata = rows(output_dir / "JILID-1-PAGE-METADATA-V6.csv")
    injections = rows(output_dir / "JILID-1-INJECTION-CONTENT-V6.csv")
    progression = {int(row["Page"]): row for row in rows(PROGRESSION)}
    issues: list[str] = []

    grouped: dict[int, list[dict[str, str]]] = defaultdict(list)
    for row in reading:
        grouped[int(row["Page"])].append(row)

    expected_pages = [p for p in range(1, 41) if p not in SPECIAL_PAGES]
    if sorted(grouped) != expected_pages:
        issues.append("READING_PAGE_SET_INVALID")
    if len(reading) != 912:
        issues.append(f"READING_ROWS expected=912 actual={len(reading)}")

    for page in expected_pages:
        page_rows = sorted(grouped[page], key=lambda r: int(r["Slot"]))
        if len(page_rows) != 24:
            issues.append(f"PAGE_SLOT_COUNT page={page} actual={len(page_rows)}")
            continue
        lengths = [int(row["UnitLength"]) for row in page_rows]
        if lengths[:8] != [1] * 8:
            issues.append(f"L1_SLOT_BAND_INVALID page={page}")
        if lengths[8:16] != [2] * 8:
            issues.append(f"L2_SLOT_BAND_INVALID page={page}")
        if lengths[16:24] != [3] * 8:
            issues.append(f"L3_SLOT_BAND_INVALID page={page}")

        stage = progression[page]["HarakatStage"]
        active = set(progression[page]["ActiveLetters"])
        for row in page_rows:
            if row.get("DisplayJoinPolicy") != "DISCONNECTED_NO_SPACE":
                issues.append(f"JOIN_POLICY_INVALID page={page} slot={row['Slot']}")
            units = PUE.grapheme_units(row["ArabicObject"])
            if len(units) != int(row["UnitLength"]):
                issues.append(f"UNIT_LENGTH_INVALID page={page} slot={row['Slot']}")
                continue
            for unit in units:
                base = base_family(PUE.unit_base(unit))
                if base not in active:
                    issues.append(f"FUTURE_LETTER_LEAK page={page} slot={row['Slot']} base={base}")
                marks = PUE.unit_marks(unit)
                mark = marks[0] if marks else ""
                if stage in MARKS and mark != MARKS[stage]:
                    issues.append(f"HARAKAT_STAGE_VIOLATION page={page} slot={row['Slot']} stage={stage}")
                if stage == "MIXED" and mark not in set(MARKS.values()):
                    issues.append(f"MIXED_MARK_INVALID page={page} slot={row['Slot']}")

    if len(metadata) != 40:
        issues.append(f"METADATA_PAGES expected=40 actual={len(metadata)}")
    counts = Counter(int(row["Page"]) for row in injections)
    if counts != Counter({20: 14, 40: 14}):
        issues.append(f"LETTER_NAME_DISTRIBUTION_INVALID actual={dict(counts)}")

    page1 = sorted(grouped.get(1, []), key=lambda r: int(r["Slot"]))
    if page1 and any(row["HarakatStage"] != "FATHAH" for row in page1):
        issues.append("PAGE1_MUST_BE_FATHAH_ONLY")

    print(f"V6_READING_ROWS={len(reading)}")
    print(f"V6_READING_PAGES={len(grouped)}")
    print("V6_SLOT_PATTERN=8_L1|8_L2|8_L3")
    print("V6_DISPLAY_JOIN_POLICY=DISCONNECTED_NO_SPACE")
    print("V6_PAGE1_HARAKAT=FATHAH_ONLY")
    print(f"V6_PEDAGOGICAL_ISSUES={len(issues)}")
    if issues:
        for issue in issues[:80]:
            print("ISSUE=" + issue)
        print("JILID1_COMPOSER_PEDAGOGICAL_GATE_V4=FAIL")
        return 1
    print("PAGE20_READING_OBJECTS=0")
    print("PAGE40_READING_OBJECTS=0")
    print("JILID1_COMPOSER_PEDAGOGICAL_GATE_V4=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
