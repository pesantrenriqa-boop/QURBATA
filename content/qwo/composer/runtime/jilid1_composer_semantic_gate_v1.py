#!/usr/bin/env python3
"""Semantic validation gate for QURBATA Jilid 1 composer output.

This gate verifies more than row counts and duplicate checks. It confirms that:
- LETTER objects contain exactly one Arabic base letter and one short vowel.
- WORD_FRAGMENT objects contain exactly two grapheme units.
- Each fragment unit carries exactly one short vowel.
- C0005 begins with a non-connecting letter.
- C0006 begins with a connecting letter.
- Awailus-suwar placement is exact on pages 20 and 30.
- All 864 reading objects are globally unique.
"""

from __future__ import annotations

import argparse
import csv
import re
import unicodedata
from collections import Counter
from pathlib import Path

BASE_RE = re.compile(r"[\u0621-\u063A\u0641-\u064A\u0671]")
SHORT_MARKS = {"َ", "ِ", "ُ"}
NON_CONNECTORS = set("ادذرزوأإآٱؤءى")
AWAIL_PAGE_20 = ["الٓمٓ", "الٓمٓصٓ", "الٓر", "الٓمٓر", "كٓهيعٓصٓ", "طه", "طسٓمٓ"]
AWAIL_PAGE_30 = ["طسٓ", "يسٓ", "صٓ", "حمٓ", "عٓسٓقٓ", "قٓ", "نٓ"]


def grapheme_units(text: str) -> list[str]:
    units: list[str] = []
    for ch in unicodedata.normalize("NFC", text):
        if BASE_RE.fullmatch(ch):
            units.append(ch)
        elif units and unicodedata.combining(ch):
            units[-1] += ch
    return units


def unit_base(unit: str) -> str:
    return next((ch for ch in unit if BASE_RE.fullmatch(ch)), "")


def unit_marks(unit: str) -> list[str]:
    return [ch for ch in unit if unicodedata.combining(ch)]


def validate_letter(text: str) -> list[str]:
    units = grapheme_units(text)
    if len(units) != 1:
        return [f"LETTER_UNIT_COUNT actual={len(units)}"]
    marks = unit_marks(units[0])
    issues: list[str] = []
    if len(marks) != 1:
        issues.append(f"LETTER_MARK_COUNT actual={len(marks)}")
    elif marks[0] not in SHORT_MARKS:
        issues.append(f"LETTER_MARK_NOT_SHORT mark={marks[0]}")
    return issues


def validate_fragment(text: str, competency: str) -> list[str]:
    units = grapheme_units(text)
    issues: list[str] = []
    if len(units) != 2:
        return [f"FRAGMENT_UNIT_COUNT actual={len(units)}"]

    for index, unit in enumerate(units, start=1):
        marks = unit_marks(unit)
        if len(marks) != 1:
            issues.append(f"FRAGMENT_UNIT_{index}_MARK_COUNT actual={len(marks)}")
        elif marks[0] not in SHORT_MARKS:
            issues.append(f"FRAGMENT_UNIT_{index}_MARK_NOT_SHORT mark={marks[0]}")

    first = unit_base(units[0])
    if competency == "C0005" and first not in NON_CONNECTORS:
        issues.append(f"C0005_CONNECTIVITY first={first}")
    if competency == "C0006" and first in NON_CONNECTORS:
        issues.append(f"C0006_CONNECTIVITY first={first}")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        default="content/qwo/composer/output/jilid-1-v2/JILID-1-READING-OBJECTS-V2.csv",
    )
    parser.add_argument(
        "--report",
        default="content/qwo/composer/output/jilid-1-v2/JILID-1-SEMANTIC-GATE-V1.csv",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.is_file():
        print(f"INPUT_NOT_FOUND {input_path}")
        return 2

    with input_path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))

    issues: list[dict[str, str]] = []
    texts: list[str] = []

    for row in rows:
        page = row["Page"]
        slot = row["Slot"]
        object_type = row["ObjectType"]
        text = unicodedata.normalize("NFC", row["ArabicObject"])
        competency = row["PrimaryCompetency"]
        texts.append(text)

        row_issues: list[str] = []
        if object_type == "LETTER":
            row_issues.extend(validate_letter(text))
        elif object_type == "WORD_FRAGMENT":
            row_issues.extend(validate_fragment(text, competency))
        elif object_type == "AWAIL_AL_SUWAR":
            expected_page = "20" if text in AWAIL_PAGE_20 else "30" if text in AWAIL_PAGE_30 else ""
            if not expected_page:
                row_issues.append("UNKNOWN_AWAIL")
            elif page != expected_page:
                row_issues.append(f"AWAIL_WRONG_PAGE expected={expected_page}")
        else:
            row_issues.append(f"UNKNOWN_OBJECT_TYPE type={object_type}")

        for reason in row_issues:
            issues.append({
                "Page": page,
                "Slot": slot,
                "ObjectType": object_type,
                "ArabicObject": text,
                "PrimaryCompetency": competency,
                "Reason": reason,
            })

    duplicate_count = len(texts) - len(set(texts))
    if len(rows) != 864:
        issues.append({"Page": "", "Slot": "", "ObjectType": "GLOBAL", "ArabicObject": "", "PrimaryCompetency": "", "Reason": f"ROW_COUNT actual={len(rows)} expected=864"})
    if duplicate_count:
        issues.append({"Page": "", "Slot": "", "ObjectType": "GLOBAL", "ArabicObject": "", "PrimaryCompetency": "", "Reason": f"GLOBAL_DUPLICATES count={duplicate_count}"})

    page_counts = Counter(row["Page"] for row in rows)
    for page in map(str, range(1, 37)):
        if page_counts.get(page, 0) != 24:
            issues.append({"Page": page, "Slot": "", "ObjectType": "GLOBAL", "ArabicObject": "", "PrimaryCompetency": "", "Reason": f"PAGE_OBJECT_COUNT actual={page_counts.get(page, 0)} expected=24"})

    awail_20 = [row["ArabicObject"] for row in rows if row["Page"] == "20" and row["ObjectType"] == "AWAIL_AL_SUWAR"]
    awail_30 = [row["ArabicObject"] for row in rows if row["Page"] == "30" and row["ObjectType"] == "AWAIL_AL_SUWAR"]
    if awail_20 != AWAIL_PAGE_20:
        issues.append({"Page": "20", "Slot": "", "ObjectType": "AWAIL_AL_SUWAR", "ArabicObject": "|".join(awail_20), "PrimaryCompetency": "SPECIAL_AWAIL", "Reason": "AWAIL_PAGE_20_SEQUENCE"})
    if awail_30 != AWAIL_PAGE_30:
        issues.append({"Page": "30", "Slot": "", "ObjectType": "AWAIL_AL_SUWAR", "ArabicObject": "|".join(awail_30), "PrimaryCompetency": "SPECIAL_AWAIL", "Reason": "AWAIL_PAGE_30_SEQUENCE"})

    report_path = Path(args.report)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with report_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["Page", "Slot", "ObjectType", "ArabicObject", "PrimaryCompetency", "Reason"])
        writer.writeheader()
        writer.writerows(issues)

    print(f"SEMANTIC_ISSUES={len(issues)}")
    print(f"REPORT={report_path}")
    if issues:
        print("JILID1_COMPOSER_SEMANTIC_GATE=FAIL")
        return 1
    print("JILID1_COMPOSER_SEMANTIC_GATE=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
