#!/usr/bin/env python3
"""Regression gate for Jilid 1 Composer v7 micro-progression output."""
from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
OUTPUT = ROOT / "content/qwo/composer/output/jilid-1-v7-micro-progression"
READING = OUTPUT / "JILID-1-READING-OBJECTS-V7.csv"
METADATA = OUTPUT / "JILID-1-PAGE-METADATA-V7.csv"
INJECTION = OUTPUT / "JILID-1-INJECTION-CONTENT-V7.csv"
SPECIAL_PAGES = {20, 40}


def rows(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        raise FileNotFoundError(path)
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> int:
    reading = rows(READING)
    metadata = rows(METADATA)
    injection = rows(INJECTION)
    issues: list[str] = []

    if len(reading) != 912:
        issues.append(f"READING_ROWS actual={len(reading)} expected=912")
    if len(metadata) != 40:
        issues.append(f"METADATA_ROWS actual={len(metadata)} expected=40")
    if len(injection) != 28:
        issues.append(f"LETTER_NAME_ROWS actual={len(injection)} expected=28")

    meta_by_page = {int(r["Page"]): r for r in metadata}
    by_page: dict[int, list[dict[str, str]]] = defaultdict(list)
    for row in reading:
        by_page[int(row["Page"])].append(row)
    if set(by_page) != {p for p in range(1, 41) if p not in SPECIAL_PAGES}:
        issues.append("READING_PAGE_SET_INVALID")

    adjacent_duplicate_count = 0
    for page, page_rows in sorted(by_page.items()):
        slots = sorted(int(r["Slot"]) for r in page_rows)
        if slots != list(range(1, 25)):
            issues.append(f"SLOT_SEQUENCE page={page}")
        lengths = Counter(int(r["UnitLength"]) for r in page_rows)
        if lengths != Counter({1:8, 2:8, 3:8}):
            issues.append(f"LENGTH_DISTRIBUTION page={page} actual={dict(lengths)}")
        for r in page_rows:
            length = int(r["UnitLength"])
            expected_band = "ROWS_1_2_L1" if length == 1 else ("ROWS_3_4_L2" if length == 2 else "ROWS_5_6_L3")
            if r["RowBand"] != expected_band:
                issues.append(f"ROW_BAND page={page} slot={r['Slot']}")
            if r["DisplayJoinPolicy"] != "DISCONNECTED_NO_SPACE":
                issues.append(f"JOIN_POLICY page={page} slot={r['Slot']}")
            if r["ObjectOrigin"] != "PRACTICE_GENERATED" or r["QuranQuotation"] != "NO":
                issues.append(f"ORIGIN_POLICY page={page} slot={r['Slot']}")
            bases = [r[f"Base{i}"] for i in range(1, length+1)]
            meta = meta_by_page[page]
            active = set(meta["ActiveLetters"])
            if any(base not in active for base in bases):
                issues.append(f"FUTURE_LETTER_LEAKAGE page={page} slot={r['Slot']} bases={''.join(bases)}")
            if length > 1 and any(bases[i] == bases[i+1] for i in range(length-1)):
                adjacent_duplicate_count += 1
                issues.append(f"ADJACENT_DUPLICATE_BASE page={page} slot={r['Slot']} bases={''.join(bases)}")

    page1 = sorted(by_page.get(1, []), key=lambda r: int(r["Slot"]))
    page1_bases = {r[f"Base{i}"] for r in page1 for i in range(1, int(r["UnitLength"])+1)}
    if not page1_bases <= set("ابتث"):
        issues.append(f"PAGE1_LETTER_SET actual={''.join(sorted(page1_bases))}")
    if "ن" in page1_bases or "ي" in page1_bases:
        issues.append("PAGE1_FUTURE_NUN_YA_LEAKAGE")
    if any(r["HarakatStage"] != "FATHAH" for r in page1):
        issues.append("PAGE1_NOT_FATHAH_ONLY")

    page1_l1 = [r["Base1"] for r in page1 if r["UnitLength"] == "1"]
    expected_page1_l1 = list("ابتثابتث")
    if page1_l1 != expected_page1_l1:
        issues.append(f"PAGE1_L1_ORDER actual={''.join(page1_l1)} expected={''.join(expected_page1_l1)}")

    page20_reading = len(by_page.get(20, []))
    page40_reading = len(by_page.get(40, []))
    page20_names = sum(1 for r in injection if r["Page"] == "20")
    page40_names = sum(1 for r in injection if r["Page"] == "40")
    if page20_reading or page40_reading:
        issues.append("SPECIAL_PAGE_HAS_READING")
    if page20_names != 14 or page40_names != 14:
        issues.append(f"LETTER_NAME_DISTRIBUTION p20={page20_names} p40={page40_names}")

    print(f"V7_READING_ROWS={len(reading)}")
    print("V7_SLOT_PATTERN=8_L1|8_L2|8_L3")
    print("V7_PAGE1_ACTIVE_LETTERS=ابتث")
    print(f"V7_PAGE1_BASES={''.join(sorted(page1_bases))}")
    print(f"V7_PAGE1_L1_ORDER={''.join(page1_l1)}")
    print("V7_PAGE1_NUN_YA=FORBIDDEN")
    print(f"V7_ADJACENT_DUPLICATES={adjacent_duplicate_count}")
    print("V7_DISPLAY_JOIN_POLICY=DISCONNECTED_NO_SPACE")
    print(f"V7_MICRO_PROGRESSION_ISSUES={len(issues)}")
    print(f"PAGE20_READING_OBJECTS={page20_reading}")
    print(f"PAGE40_READING_OBJECTS={page40_reading}")
    if issues:
        for issue in issues[:30]:
            print(f"ISSUE={issue}")
        print("JILID1_COMPOSER_MICRO_PROGRESSION_GATE_V5=FAIL")
        return 1
    print("JILID1_COMPOSER_MICRO_PROGRESSION_GATE_V5=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
