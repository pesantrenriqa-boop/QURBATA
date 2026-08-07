#!/usr/bin/env python3
"""QURBATA Jilid 1 Composer v6 — fixed 1/2/3-unit practice from page 1.

Pedagogical contract implemented here:
- every READING page has 24 slots arranged as 8 x L1, 8 x L2, 8 x L3;
- slots 1-8 are one-unit objects, 9-16 two-unit objects, 17-24 three-unit objects;
- Jilid 1 display policy is DISCONNECTED_NO_SPACE for all multi-unit objects;
- short vowels are staged: FATHAH -> KASRAH -> DHAMMAH -> MIXED;
- letter availability follows GLE family order; future letters cannot leak into a page;
- pages 20 and 40 remain dedicated LETTER_NAMES pages;
- Quran source traceability is preserved from the candidate pools.

This is REVIEW_CANDIDATE content. Stage boundaries live in the V3 progression CSV
so they can be revised without changing the composer runtime.
"""
from __future__ import annotations

import argparse
import csv
import importlib.util
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[4]
V4_PATH = ROOT / "content/qwo/composer/runtime/jilid1_page_composer_v4.py"
GLE_PATH = ROOT / "content/qwo/lpe/runtime/grapheme_learning_engine_v1.py"
GLE_REGISTRY = ROOT / "content/qwo/lpe/JILID-1-GRAPHEME-FAMILY-REGISTRY-V1.csv"
PROGRESSION = ROOT / "content/qwo/lpe/JILID-1-PEDAGOGICAL-PROGRESSION-V3.csv"
CRE_PAGE_REGISTRY = ROOT / "content/qwo/registry/JILID-1-PAGE-CONTENT-REGISTRY-V2.csv"
LETTER_NAMES = ROOT / "content/qwo/lpe/JILID-1-LETTER-NAME-REGISTRY-V1.csv"
DEFAULT_OUTPUT = ROOT / "content/qwo/composer/output/jilid-1-v6-pedagogical"
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


V4 = load_module(V4_PATH, "qurbata_j1_v4_for_v6")
GLE = load_module(GLE_PATH, "qurbata_gle_for_v6")


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


def canonical_base(base: str) -> str:
    # Treat Quranic alif carriers as members of the ALIF visual family for ordering/filtering.
    return "ا" if base in {"أ", "إ", "آ", "ٱ"} else base


def unit_bases(text: str) -> list[str]:
    return [canonical_base(V4.PUE.unit_base(unit)) for unit in V4.PUE.grapheme_units(text)]


def unit_marks(text: str) -> list[str]:
    result: list[str] = []
    for unit in V4.PUE.grapheme_units(text):
        marks = V4.PUE.unit_marks(unit)
        result.append(marks[0] if marks else "")
    return result


def stage_allows(text: str, stage: str) -> bool:
    marks = unit_marks(text)
    if not marks or any(mark not in {"َ", "ِ", "ُ"} for mark in marks):
        return False
    if stage == "MIXED":
        return True
    expected = MARKS.get(stage)
    return expected is not None and all(mark == expected for mark in marks)


def progression_rows() -> dict[int, dict[str, str]]:
    rows = read_csv(PROGRESSION)
    if len(rows) != 40:
        raise ValueError(f"PROGRESSION_PAGE_COUNT expected=40 actual={len(rows)}")
    result = {int(row["Page"]): row for row in rows}
    if set(result) != set(range(1, 41)):
        raise ValueError("PROGRESSION_PAGE_SET_INVALID")
    for page, row in result.items():
        expected = 0 if page in SPECIAL_PAGES else 8
        for key in ("L1Slots", "L2Slots", "L3Slots"):
            if int(row[key]) != expected:
                raise ValueError(f"FIXED_LENGTH_SLOT_POLICY page={page} field={key} actual={row[key]}")
        if page in SPECIAL_PAGES and row["SpecialInjection"] != "LETTER_NAMES":
            raise ValueError(f"LETTER_NAME_INJECTION_REQUIRED page={page}")
    return result


def candidate_key(candidate, new_letters: set[str], rank: dict[str, tuple[int, int]]):
    bases = unit_bases(candidate.text)
    new_hits = sum(base in new_letters for base in bases)
    base_rank = tuple(rank.get(base, (999, 999)) for base in bases)
    return (-new_hits, base_rank, candidate.text, candidate.source_ref)


def compatible(pool, active_letters: set[str], stage: str):
    result = []
    for candidate in pool:
        bases = unit_bases(candidate.text)
        if not bases or any(base not in active_letters for base in bases):
            continue
        if not stage_allows(candidate.text, stage):
            continue
        result.append(candidate)
    return result


def choose(candidates, count: int, page: int, length: int):
    if not candidates:
        raise ValueError(f"PEDAGOGICAL_POOL_EMPTY page={page} length={length}")
    # Rotate pages for variety. Repetition is pedagogically allowed when an early active pool
    # is smaller than eight objects; this is intentional drill, not an accidental duplicate.
    start = ((page - 1) * 5 + length * 3) % len(candidates)
    rotated = candidates[start:] + candidates[:start]
    if len(rotated) >= count:
        return rotated[:count]
    selected = []
    while len(selected) < count:
        selected.extend(rotated[: count - len(selected)])
    return selected


def display_code(stage: str, length: int) -> tuple[str, str]:
    stage_id = {"FATHAH": "F", "KASRAH": "K", "DHAMMAH": "D", "MIXED": "M"}[stage]
    stage_name = {"FATHAH": "fathah", "KASRAH": "kasrah", "DHAMMAH": "dhammah", "MIXED": "campuran harakat dasar"}[stage]
    code = f"J1-L{length}-{stage_id}"
    desc = f"Membaca {length} satuan huruf {stage_name} dalam bentuk terpisah tanpa spasi."
    return code, desc


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT.relative_to(ROOT)))
    args = parser.parse_args()
    output_dir = Path(args.output_dir)
    output_dir = output_dir if output_dir.is_absolute() else ROOT / output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    progression = progression_rows()
    cre_rows = read_csv(CRE_PAGE_REGISTRY)
    cre_by_page = {int(row["Page"]): row for row in cre_rows}
    if set(cre_by_page) != set(range(1, 41)):
        raise ValueError("CRE_PAGE_SET_INVALID")

    families = GLE.load_registry(GLE_REGISTRY)
    gle_issues = GLE.validate_registry(families)
    if gle_issues:
        raise ValueError("GLE_INVALID " + " | ".join(gle_issues))
    rank = GLE.build_letter_rank(families)

    foundation = V4.foundation_candidates(V4.DEFAULT_FOUNDATION)
    triples = V4.triple_word_candidates(V4.DEFAULT_CORPUS)
    pools = {
        1: [item for item in foundation if item.unit_length == 1],
        2: [item for item in foundation if item.unit_length == 2],
        3: triples,
    }

    seen_texts: set[tuple[int, str]] = set()
    reading_rows: list[dict[str, Any]] = []
    metadata_rows: list[dict[str, Any]] = []

    for page in range(1, 41):
        plan = progression[page]
        cre = cre_by_page[page]
        if page in SPECIAL_PAGES:
            metadata_rows.append({
                "Page": page,
                "HarakatStage": "SPECIAL",
                "NewLetters": "",
                "ActiveLetters": plan["ActiveLetters"],
                "CompetencyCodes": "LETTER_NAMES",
                "CompetencyDescriptions": "Mengenal dan menyebut nama huruf hijaiyah.",
                "MemorizationCode": cre["MemorizationCode"],
                "MemorizationDescription": cre["MemorizationDescription"],
                "MemorizationStage": cre["MemorizationStage"],
                "ArabicCode": cre["ArabicCode"],
                "ArabicDescription": cre["ArabicDescription"],
                "AkhlaqCode": cre["AkhlaqCode"],
                "AkhlaqDescription": cre["AkhlaqDescription"],
                "AssessmentCode": cre["AssessmentCode"],
                "AssessmentDescription": cre["AssessmentDescription"],
                "FooterProfile": cre["FooterProfile"],
                "SpecialInjection": "LETTER_NAMES",
                "Status": "PEDAGOGICAL_REVIEW_CANDIDATE_V6",
            })
            continue

        stage = plan["HarakatStage"]
        active_letters = set(plan["ActiveLetters"])
        new_letters = set(plan["NewLetters"])
        page_codes: list[tuple[str, str]] = []

        for length in (1, 2, 3):
            filtered = compatible(pools[length], active_letters, stage)
            filtered.sort(key=lambda item: candidate_key(item, new_letters, rank))
            chosen = choose(filtered, 8, page, length)
            code, description = display_code(stage, length)
            page_codes.append((code, description))
            for offset, candidate in enumerate(chosen):
                slot = (length - 1) * 8 + offset + 1
                key = (length, candidate.text)
                state = "REVIEW" if key in seen_texts else "NEW"
                repeated_in_page = sum(1 for earlier in chosen[:offset] if earlier.text == candidate.text) > 0
                seen_texts.add(key)
                reading_rows.append({
                    "Jilid": 1,
                    "Page": page,
                    "Slot": slot,
                    "RowBand": "L1_ROWS_1_2" if length == 1 else ("L2_ROWS_3_4" if length == 2 else "L3_ROWS_5_6"),
                    "ObjectID": f"J1V6-P{page:02d}-S{slot:02d}",
                    "CanonicalKey": candidate.key,
                    "ObjectType": candidate.object_type,
                    "ArabicObject": candidate.text,
                    "UnitLength": length,
                    "HarakatStage": stage,
                    "LearningState": state,
                    "PracticeRepeatWithinPage": "YES" if repeated_in_page else "NO",
                    "DisplayJoinPolicy": "DISCONNECTED_NO_SPACE",
                    "CompetencyCode": code,
                    "CompetencyDescription": description,
                    "SourceCompetencyCode": candidate.competency,
                    "SourceRef": candidate.source_ref,
                    "SpecialInjection": "NONE",
                    "Status": "PEDAGOGICAL_REVIEW_CANDIDATE_V6",
                })

        metadata_rows.append({
            "Page": page,
            "HarakatStage": stage,
            "NewLetters": plan["NewLetters"],
            "ActiveLetters": plan["ActiveLetters"],
            "CompetencyCodes": " | ".join(code for code, _ in page_codes),
            "CompetencyDescriptions": " | ".join(desc for _, desc in page_codes),
            "MemorizationCode": cre["MemorizationCode"],
            "MemorizationDescription": cre["MemorizationDescription"],
            "MemorizationStage": cre["MemorizationStage"],
            "ArabicCode": cre["ArabicCode"],
            "ArabicDescription": cre["ArabicDescription"],
            "AkhlaqCode": cre["AkhlaqCode"],
            "AkhlaqDescription": cre["AkhlaqDescription"],
            "AssessmentCode": cre["AssessmentCode"],
            "AssessmentDescription": cre["AssessmentDescription"],
            "FooterProfile": cre["FooterProfile"],
            "SpecialInjection": "NONE",
            "Status": "PEDAGOGICAL_REVIEW_CANDIDATE_V6",
        })

    letter_names = V4.load_letter_names(LETTER_NAMES)
    injection_rows = [{
        "Page": int(row["TargetPage"]),
        "Sequence": int(row["Sequence"]),
        "ContentType": "LETTER_NAME",
        "Letter": row["Letter"],
        "LetterNameArabic": row["LetterNameArabic"],
        "Status": "PEDAGOGICAL_REVIEW_CANDIDATE_V6",
    } for row in letter_names]

    write_csv(output_dir / "JILID-1-READING-OBJECTS-V6.csv", reading_rows)
    write_csv(output_dir / "JILID-1-PAGE-METADATA-V6.csv", metadata_rows)
    write_csv(output_dir / "JILID-1-INJECTION-CONTENT-V6.csv", injection_rows)

    by_length = defaultdict(int)
    for row in reading_rows:
        by_length[int(row["UnitLength"])] += 1
    print("JILID1_COMPOSER_V6=PASS")
    print(f"READING_ROWS={len(reading_rows)}")
    print(f"L1_ROWS={by_length[1]}")
    print(f"L2_ROWS={by_length[2]}")
    print(f"L3_ROWS={by_length[3]}")
    print("SLOT_PATTERN=8_L1|8_L2|8_L3")
    print("DISPLAY_JOIN_POLICY=DISCONNECTED_NO_SPACE")
    print("PAGE1_HARAKAT_STAGE=FATHAH")
    print("SPECIAL_PAGES=20,40")
    print(f"OUTPUT_DIR={output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
