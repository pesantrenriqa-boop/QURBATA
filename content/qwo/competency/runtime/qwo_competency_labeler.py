#!/usr/bin/env python3
"""Label QURBATA QWO candidates against the permanent competency map.

Launch-focused V1: reads audited QWO CSV and emits competency-labelled CSV.
It does not assign books or pages and never promotes candidate status.
"""
from __future__ import annotations

import argparse
import csv
import unicodedata
from pathlib import Path

PRIMARY_MAP = {
    "LENGTH_1_2": "C0005",
    "CONNECTED_3_PLUS": "C0007",
    "NON_CONNECTOR_TRANSITION": "C0011",
    "MIXED_REVIEW": "C0013",
    "MAD_ALIF": "C0014",
    "MAD_YA": "C0015",
    "MAD_WAWU": "C0016",
    "TANWIN_FATH": "C0017",
    "TANWIN_KASR": "C0018",
    "TANWIN_DAMM": "C0019",
    "SUKUN": "C0020",
    "TASYDID": "C0024",
    "ALIF_LAM": "C0025",
    "TA_MARBUTAH": "C0026",
    "ALIF_MAQSHURAH": "C0027",
    "HAMZAH": "C0028",
}

FEATURE_MAP = {key: value for key, value in PRIMARY_MAP.items() if key != "MIXED_REVIEW"}


def strip_marks(text: str) -> str:
    return "".join(
        ch for ch in unicodedata.normalize("NFD", text)
        if unicodedata.category(ch) != "Mn"
    ).replace("ٱ", "ا")


def label(row: dict[str, str]) -> tuple[str, str]:
    primary = PRIMARY_MAP.get(row.get("TargetCompetency", ""), "C0013")
    secondary: set[str] = set()

    for feature in row.get("StrictFeatures", "").split("|"):
        competency = FEATURE_MAP.get(feature)
        if competency and competency != primary:
            secondary.add(competency)

    base = strip_marks(row.get("ArabicWord", ""))
    if "الله" in base:
        if base == "الله":
            primary = "C0031"
        elif base.startswith(("بالله", "لله", "والله", "فالله", "تالله")):
            primary = "C0032"
        else:
            primary = "C0030"

    letter_count = sum("ء" <= ch <= "ي" or ch == "ى" for ch in base)
    if letter_count >= 5 and primary not in {"C0030", "C0031", "C0032"}:
        secondary.add("C0013")
    elif letter_count == 4:
        secondary.add("C0012")

    secondary.discard(primary)
    return primary, "|".join(sorted(secondary))


def run(input_path: Path, output_path: Path) -> None:
    with input_path.open(encoding="utf-8-sig", newline="") as source:
        rows = list(csv.DictReader(source))
    if not rows:
        raise ValueError("QWO input is empty")

    output_fields = list(rows[0]) + ["PrimaryCompetencyID", "SecondaryCompetencyIDs"]
    with output_path.open("w", encoding="utf-8-sig", newline="") as target:
        writer = csv.DictWriter(target, fieldnames=output_fields)
        writer.writeheader()
        for row in rows:
            primary, secondary = label(row)
            row["PrimaryCompetencyID"] = primary
            row["SecondaryCompetencyIDs"] = secondary
            writer.writerow(row)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    run(args.input, args.output)


if __name__ == "__main__":
    main()
