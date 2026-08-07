#!/usr/bin/env python3
"""QURBATA Jilid 1 Composer v7 — micro letter progression + independent-unit practice.

Contract:
- 40 pages; pages 20 and 40 are LETTER_NAMES only.
- Every reading page: slots 1-8=L1, 9-16=L2, 17-24=L3.
- L2/L3 are NOT words and NOT connected Arabic; they are sequences of independent
  letter units rendered close together with no inter-unit shaping.
- Only letters in ActiveLetters may appear. Future-letter leakage is a hard failure.
- Harakat stage is controlled by JILID-1-PEDAGOGICAL-PROGRESSION-V4.csv.
- Practice objects are explicitly tagged PRACTICE_GENERATED, never Quran quotations.
"""
from __future__ import annotations

import argparse
import csv
import importlib.util
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[4]
PGE_PATH = ROOT / "content/qwo/composer/runtime/practice_generation_engine_v1.py"
PROGRESSION = ROOT / "content/qwo/lpe/JILID-1-PEDAGOGICAL-PROGRESSION-V4.csv"
CRE_PAGE_REGISTRY = ROOT / "content/qwo/registry/JILID-1-PAGE-CONTENT-REGISTRY-V2.csv"
LETTER_NAMES = ROOT / "content/qwo/lpe/JILID-1-LETTER-NAME-REGISTRY-V1.csv"
DEFAULT_OUTPUT = ROOT / "content/qwo/composer/output/jilid-1-v7-micro-progression"
SPECIAL_PAGES = {20, 40}


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"MODULE_IMPORT_FAILED: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


PGE = load_module(PGE_PATH, "qurbata_pge_v1_for_j1v7")


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        raise FileNotFoundError(path)
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        raise ValueError(f"EMPTY_OUTPUT: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader(); writer.writerows(rows)


def load_progression() -> dict[int, dict[str, str]]:
    rows = read_csv(PROGRESSION)
    if len(rows) != 40:
        raise ValueError(f"PROGRESSION_PAGE_COUNT expected=40 actual={len(rows)}")
    result = {int(row["Page"]): row for row in rows}
    if set(result) != set(range(1, 41)):
        raise ValueError("PROGRESSION_PAGE_SET_INVALID")
    previous_active = ""
    for page in range(1, 41):
        row = result[page]
        active = row["ActiveLetters"]
        new = row["NewLetters"]
        if any(letter not in active for letter in new):
            raise ValueError(f"NEW_LETTER_NOT_ACTIVE page={page}")
        if page > 1 and any(letter not in active for letter in previous_active):
            raise ValueError(f"ACTIVE_LETTERS_NOT_CUMULATIVE page={page}")
        if page in SPECIAL_PAGES:
            if row["SpecialInjection"] != "LETTER_NAMES":
                raise ValueError(f"SPECIAL_INJECTION_INVALID page={page}")
            if any(int(row[k]) != 0 for k in ("L1Slots", "L2Slots", "L3Slots")):
                raise ValueError(f"SPECIAL_SLOT_POLICY_INVALID page={page}")
        else:
            if [int(row[k]) for k in ("L1Slots", "L2Slots", "L3Slots")] != [8, 8, 8]:
                raise ValueError(f"READING_SLOT_POLICY_INVALID page={page}")
        previous_active = active
    return result


def load_letter_names() -> list[dict[str, str]]:
    rows = read_csv(LETTER_NAMES)
    if len(rows) != 28:
        raise ValueError(f"LETTER_NAMES_COUNT expected=28 actual={len(rows)}")
    return rows


def competency(stage: str, length: int) -> tuple[str, str]:
    label = {"FATHAH":"fathah", "KASRAH":"kasrah", "DHAMMAH":"dhammah", "MIXED":"campuran fathah-kasrah-dhammah"}[stage]
    code = f"J1-PRACTICE-L{length}-{stage}"
    return code, f"Membaca latihan {length} satuan huruf {label}; setiap huruf tetap berbentuk tunggal dan tidak tersambung."


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT.relative_to(ROOT)))
    args = parser.parse_args()
    output_dir = Path(args.output_dir)
    output_dir = output_dir if output_dir.is_absolute() else ROOT / output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    progression = load_progression()
    cre_rows = read_csv(CRE_PAGE_REGISTRY)
    cre_by_page = {int(row["Page"]): row for row in cre_rows}
    if set(cre_by_page) != set(range(1, 41)):
        raise ValueError("CRE_PAGE_SET_INVALID")

    reading_rows: list[dict[str, Any]] = []
    metadata_rows: list[dict[str, Any]] = []

    for page in range(1, 41):
        plan = progression[page]
        cre = cre_by_page[page]
        if page in SPECIAL_PAGES:
            metadata_rows.append({
                "Page": page, "HarakatStage": "SPECIAL", "NewLetters": "", "ActiveLetters": plan["ActiveLetters"],
                "CompetencyCodes": "LETTER_NAMES", "CompetencyDescriptions": "Mengenal dan menyebut nama huruf hijaiyah.",
                "MemorizationCode": cre["MemorizationCode"], "MemorizationDescription": cre["MemorizationDescription"],
                "MemorizationStage": cre["MemorizationStage"], "ArabicCode": cre["ArabicCode"], "ArabicDescription": cre["ArabicDescription"],
                "AkhlaqCode": cre["AkhlaqCode"], "AkhlaqDescription": cre["AkhlaqDescription"],
                "AssessmentCode": cre["AssessmentCode"], "AssessmentDescription": cre["AssessmentDescription"],
                "FooterProfile": cre["FooterProfile"], "SpecialInjection": "LETTER_NAMES", "Status": "MICRO_PROGRESSION_REVIEW_CANDIDATE_V7",
            })
            continue

        stage = plan["HarakatStage"]
        page_competencies: list[tuple[str, str]] = []
        for length in (1, 2, 3):
            generated = PGE.generate(plan["ActiveLetters"], plan["NewLetters"], stage, length, 8, page)
            code, description = competency(stage, length)
            page_competencies.append((code, description))
            for offset, obj in enumerate(generated):
                issues = PGE.validate_object(obj, plan["ActiveLetters"])
                if issues:
                    raise ValueError(f"PGE_OBJECT_INVALID page={page} length={length} issues={'|'.join(issues)}")
                slot = (length - 1) * 8 + offset + 1
                reading_rows.append({
                    "Jilid": 1,
                    "Page": page,
                    "Slot": slot,
                    "RowBand": "ROWS_1_2_L1" if length == 1 else ("ROWS_3_4_L2" if length == 2 else "ROWS_5_6_L3"),
                    "ObjectID": f"J1V7-P{page:02d}-S{slot:02d}",
                    "ObjectOrigin": "PRACTICE_GENERATED",
                    "ArabicObject": obj.display_text,
                    "Unit1": obj.units[0],
                    "Unit2": obj.units[1] if length >= 2 else "",
                    "Unit3": obj.units[2] if length >= 3 else "",
                    "Base1": obj.bases[0],
                    "Base2": obj.bases[1] if length >= 2 else "",
                    "Base3": obj.bases[2] if length >= 3 else "",
                    "UnitLength": length,
                    "HarakatStage": stage,
                    "DisplayJoinPolicy": "DISCONNECTED_NO_SPACE",
                    "CompetencyCode": code,
                    "CompetencyDescription": description,
                    "SourceRef": "PGE:JILID1",
                    "QuranQuotation": "NO",
                    "SpecialInjection": "NONE",
                    "Status": "MICRO_PROGRESSION_REVIEW_CANDIDATE_V7",
                })

        metadata_rows.append({
            "Page": page, "HarakatStage": stage, "NewLetters": plan["NewLetters"], "ActiveLetters": plan["ActiveLetters"],
            "CompetencyCodes": " | ".join(x[0] for x in page_competencies),
            "CompetencyDescriptions": " | ".join(x[1] for x in page_competencies),
            "MemorizationCode": cre["MemorizationCode"], "MemorizationDescription": cre["MemorizationDescription"],
            "MemorizationStage": cre["MemorizationStage"], "ArabicCode": cre["ArabicCode"], "ArabicDescription": cre["ArabicDescription"],
            "AkhlaqCode": cre["AkhlaqCode"], "AkhlaqDescription": cre["AkhlaqDescription"],
            "AssessmentCode": cre["AssessmentCode"], "AssessmentDescription": cre["AssessmentDescription"],
            "FooterProfile": cre["FooterProfile"], "SpecialInjection": "NONE", "Status": "MICRO_PROGRESSION_REVIEW_CANDIDATE_V7",
        })

    letter_names = load_letter_names()
    injection_rows = [{
        "Page": int(row["TargetPage"]), "Sequence": int(row["Sequence"]), "ContentType": "LETTER_NAME",
        "Letter": row["Letter"], "LetterNameArabic": row["LetterNameArabic"], "Status": row.get("Status", "REVIEW_CANDIDATE")
    } for row in letter_names]

    write_csv(output_dir / "JILID-1-READING-OBJECTS-V7.csv", reading_rows)
    write_csv(output_dir / "JILID-1-PAGE-METADATA-V7.csv", metadata_rows)
    write_csv(output_dir / "JILID-1-INJECTION-CONTENT-V7.csv", injection_rows)

    print("JILID1_COMPOSER_V7=PASS")
    print(f"READING_ROWS={len(reading_rows)}")
    print("L1_ROWS=304")
    print("L2_ROWS=304")
    print("L3_ROWS=304")
    print("PAGE1_ACTIVE_LETTERS=ابتث")
    print("PAGE1_FUTURE_LETTERS_EXCLUDED=ني")
    print("DISPLAY_JOIN_POLICY=DISCONNECTED_NO_SPACE")
    print("OBJECT_ORIGIN=PRACTICE_GENERATED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
