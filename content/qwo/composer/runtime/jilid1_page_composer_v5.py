#!/usr/bin/env python3
"""QURBATA Jilid 1 Composer v5 integration layer.

V5 composes with the proven v4 engine while adding two authoritative layers:
- GLE v1 determines deterministic L1 grapheme-family introduction order.
- CRE v2 supplies page-level memorization, Arabic, akhlaq, assessment and footer metadata.

The v4 pedagogical selection rules, LPE progression, special LETTER_NAMES pages,
and Quran-source preservation remain authoritative. This is still a
REVIEW_CANDIDATE build; memorization text bodies remain pending in the registry.
"""
from __future__ import annotations

import argparse
import csv
import importlib.util
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[4]
V4_PATH = ROOT / "content/qwo/composer/runtime/jilid1_page_composer_v4.py"
GLE_PATH = ROOT / "content/qwo/lpe/runtime/grapheme_learning_engine_v1.py"
GLE_REGISTRY = ROOT / "content/qwo/lpe/JILID-1-GRAPHEME-FAMILY-REGISTRY-V1.csv"
CRE_PAGE_REGISTRY = ROOT / "content/qwo/registry/JILID-1-PAGE-CONTENT-REGISTRY-V2.csv"
DEFAULT_OUTPUT = ROOT / "content/qwo/composer/output/jilid-1-v5-integrated"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"MODULE_IMPORT_FAILED: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


V4 = load_module(V4_PATH, "qurbata_j1_composer_v4_for_v5")
GLE = load_module(GLE_PATH, "qurbata_gle_v1_for_v5")
ORIGINAL_FOUNDATION_CANDIDATES = V4.foundation_candidates


def load_csv(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        raise FileNotFoundError(path)
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        raise ValueError(f"EMPTY_OUTPUT {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader(); writer.writerows(rows)


def gle_foundation_candidates(path: Path):
    candidates = ORIGINAL_FOUNDATION_CANDIDATES(path)
    families = GLE.load_registry(GLE_REGISTRY)
    issues = GLE.validate_registry(families)
    if issues:
        raise ValueError("GLE_REGISTRY_INVALID " + " | ".join(issues))
    rank = GLE.build_letter_rank(families)
    mark_rank = {"َ": 1, "ِ": 2, "ُ": 3}

    def key(item):
        units = V4.PUE.grapheme_units(item.text)
        first_base = V4.PUE.unit_base(units[0]) if units else ""
        first_marks = V4.PUE.unit_marks(units[0]) if units else ()
        first_mark = first_marks[0] if first_marks else ""
        return (
            item.unit_length,
            rank.get(first_base, (999, 999)),
            mark_rank.get(first_mark, 99),
            item.text,
            item.source_ref,
        )

    return sorted(candidates, key=key)


def build_v4_args(output_dir: Path) -> argparse.Namespace:
    return argparse.Namespace(
        progression=V4.DEFAULT_PROGRESSION,
        composition=V4.DEFAULT_COMPOSITION,
        foundation=V4.DEFAULT_FOUNDATION,
        corpus=V4.DEFAULT_CORPUS,
        letter_names=V4.DEFAULT_LETTER_NAMES,
        output_dir=output_dir,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT.relative_to(ROOT)))
    args = parser.parse_args()
    output_dir = Path(args.output_dir)
    output_dir = output_dir if output_dir.is_absolute() else ROOT / output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    # Inject GLE ordering into the already validated v4 composition engine.
    V4.foundation_candidates = gle_foundation_candidates
    V4.compose(build_v4_args(output_dir))

    reading_v4 = load_csv(output_dir / "JILID-1-READING-OBJECTS-V4.csv")
    injections_v4 = load_csv(output_dir / "JILID-1-INJECTION-CONTENT-V4.csv")
    cre_rows = load_csv(CRE_PAGE_REGISTRY)
    if len(cre_rows) != 40:
        raise ValueError(f"CRE_PAGE_COUNT expected=40 actual={len(cre_rows)}")
    cre_by_page = {int(row["Page"]): row for row in cre_rows}

    reading_v5: list[dict[str, str]] = []
    for row in reading_v4:
        page = int(row["Page"])
        cre = cre_by_page[page]
        merged = dict(row)
        merged["ObjectID"] = merged["ObjectID"].replace("J1V4-", "J1V5-")
        merged["MemorizationCode"] = cre["MemorizationCode"]
        merged["MemorizationDescription"] = cre["MemorizationDescription"]
        merged["MemorizationStage"] = cre["MemorizationStage"]
        merged["ArabicCode"] = cre["ArabicCode"]
        merged["ArabicDescription"] = cre["ArabicDescription"]
        merged["AkhlaqCode"] = cre["AkhlaqCode"]
        merged["AkhlaqDescription"] = cre["AkhlaqDescription"]
        merged["AssessmentCode"] = cre["AssessmentCode"]
        merged["AssessmentDescription"] = cre["AssessmentDescription"]
        merged["FooterProfile"] = cre["FooterProfile"]
        merged["Status"] = "INTEGRATED_REVIEW_CANDIDATE_V5"
        reading_v5.append(merged)

    # Build one authoritative metadata row per instructional page.
    competency_by_page: dict[int, list[tuple[str, str]]] = {page: [] for page in range(1, 41)}
    for row in reading_v5:
        page = int(row["Page"])
        pair = (row["CompetencyCode"], row["CompetencyDescription"])
        if pair not in competency_by_page[page]:
            competency_by_page[page].append(pair)

    metadata_v5: list[dict[str, str]] = []
    for page in range(1, 41):
        cre = cre_by_page[page]
        pairs = competency_by_page[page]
        if page in V4.SPECIAL_PAGES:
            competency_codes = "LETTER_NAMES"
            competency_descriptions = "Mengenal dan menyebut nama huruf hijaiyah."
            special_injection = "LETTER_NAMES"
        else:
            competency_codes = " | ".join(code for code, _ in pairs)
            competency_descriptions = " | ".join(desc for _, desc in pairs)
            special_injection = "NONE"
        metadata_v5.append({
            "Page": str(page),
            "CompetencyCodes": competency_codes,
            "CompetencyDescriptions": competency_descriptions,
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
            "SpecialInjection": special_injection,
            "Status": "INTEGRATED_REVIEW_CANDIDATE_V5",
        })

    injection_v5 = []
    for row in injections_v4:
        item = dict(row)
        item["Status"] = "INTEGRATED_REVIEW_CANDIDATE_V5"
        injection_v5.append(item)

    reading_output = output_dir / "JILID-1-READING-OBJECTS-V5.csv"
    metadata_output = output_dir / "JILID-1-PAGE-METADATA-V5.csv"
    injection_output = output_dir / "JILID-1-INJECTION-CONTENT-V5.csv"
    write_csv(reading_output, reading_v5)
    write_csv(metadata_output, metadata_v5)
    write_csv(injection_output, injection_v5)

    print("JILID1_COMPOSER_V5=PASS")
    print(f"READING_ROWS={len(reading_v5)}")
    print(f"METADATA_PAGES={len(metadata_v5)}")
    print(f"LETTER_NAME_ROWS={len(injection_v5)}")
    print("GLE_INTEGRATION=ENABLED")
    print("CRE_V2_INTEGRATION=ENABLED")
    print(f"READING_OUTPUT={reading_output}")
    print(f"METADATA_OUTPUT={metadata_output}")
    print(f"INJECTION_OUTPUT={injection_output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
