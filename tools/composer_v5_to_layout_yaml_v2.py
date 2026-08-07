#!/usr/bin/env python3
"""Convert integrated Jilid 1 Composer v5 CSV outputs into 40 layout YAML pages.

Reading pages contain 24 canonical objects. Pages 20 and 40 are dedicated
LETTER_NAMES pages and contain 14 letter-name entries instead of reading objects.
All human-readable page metadata is sourced from Composer v5 / CRE output.
"""
from __future__ import annotations

import argparse
import csv
import importlib.util
import sys
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
PUE_PATH = ROOT / "content/qwo/pedagogy/runtime/pedagogical_unit_engine.py"
DEFAULT_DIR = ROOT / "content/qwo/composer/output/jilid-1-v5-integrated"
SPECIAL_PAGES = {20, 40}


def load_pue():
    spec = importlib.util.spec_from_file_location("qurbata_pue_layout_v2", PUE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("PUE_IMPORT_FAILED")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


PUE = load_pue()


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        raise FileNotFoundError(path)
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def split_units(text: str) -> list[str]:
    units = PUE.grapheme_units(text)
    if not units:
        raise ValueError(f"NO_PEDAGOGICAL_UNITS: {text!r}")
    for unit in units:
        decision = PUE.validate_short_vowel_unit(unit)
        if not decision.passed:
            raise ValueError(f"INVALID_SHORT_UNIT: {unit!r} from {text!r} reasons={'|'.join(decision.reasons)}")
    return units


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", default=str(DEFAULT_DIR.relative_to(ROOT)))
    parser.add_argument("--output-dir", default="books/jilid-1/data-generated-v5-native")
    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    input_dir = input_dir if input_dir.is_absolute() else ROOT / input_dir
    output_dir = Path(args.output_dir)
    output_dir = output_dir if output_dir.is_absolute() else ROOT / output_dir

    reading = read_csv(input_dir / "JILID-1-READING-OBJECTS-V5.csv")
    metadata = read_csv(input_dir / "JILID-1-PAGE-METADATA-V5.csv")
    injections = read_csv(input_dir / "JILID-1-INJECTION-CONTENT-V5.csv")

    reading_by_page: dict[int, list[dict[str, str]]] = defaultdict(list)
    for row in reading:
        reading_by_page[int(row["Page"])].append(row)
    meta_by_page = {int(row["Page"]): row for row in metadata}
    injection_by_page: dict[int, list[dict[str, str]]] = defaultdict(list)
    for row in injections:
        injection_by_page[int(row["Page"])].append(row)

    if set(meta_by_page) != set(range(1, 41)):
        raise ValueError("METADATA_PAGES_MUST_BE_1_TO_40")
    expected_reading_pages = {p for p in range(1, 41) if p not in SPECIAL_PAGES}
    if set(reading_by_page) != expected_reading_pages:
        raise ValueError("READING_PAGE_SET_INVALID")
    for page in SPECIAL_PAGES:
        if len(injection_by_page[page]) != 14:
            raise ValueError(f"LETTER_NAME_COUNT page={page} actual={len(injection_by_page[page])}")

    output_dir.mkdir(parents=True, exist_ok=True)
    total_reading = 0
    total_letter_names = 0

    for page in range(1, 41):
        meta = meta_by_page[page]
        page_data: dict = {
            "schema_version": 2,
            "book": "QURBATA",
            "volume": 1,
            "page": page,
            "status": "integrated-v5-layout-review-candidate",
            "layout": "canonical-j1-v2",
            "source": str(input_dir).replace("\\", "/"),
            "page_role": meta.get("PageRole", ""),
            "identity": {"title": "QURBATA", "subtitle": f"JILID 1 • HALAMAN {page:02d}"},
            "targets": {
                "material_progress": f"{page:02d} / 40",
                "competency_codes": meta.get("CompetencyCodes", ""),
                "competency_descriptions": meta.get("CompetencyDescriptions", ""),
                "memorization_code": meta.get("MemorizationCode", ""),
                "memorization": meta.get("MemorizationDescription", ""),
                "memorization_stage": meta.get("MemorizationStage", ""),
                "arabic_code": meta.get("ArabicCode", ""),
                "arabic_language": meta.get("ArabicDescription", ""),
                "akhlaq_code": meta.get("AkhlaqCode", ""),
                "akhlaq": meta.get("AkhlaqDescription", ""),
                "assessment_code": meta.get("AssessmentCode", ""),
                "assessment": meta.get("AssessmentDescription", ""),
            },
            "special_injection": meta.get("SpecialInjection", "NONE"),
            "footer": {
                "profile": meta.get("FooterProfile", "J1_STANDARD_V2"),
                "teacher_label": "Nama Guru",
                "date_label": "Tanggal",
                "score_label": "Nilai",
            },
        }

        if page in SPECIAL_PAGES:
            page_data["page_kind"] = "LETTER_NAMES"
            page_data["objects"] = []
            entries = []
            for row in sorted(injection_by_page[page], key=lambda r: int(r["Sequence"])):
                entries.append({
                    "sequence": int(row["Sequence"]),
                    "letter": row["Letter"],
                    "letter_name_arabic": row["LetterNameArabic"],
                    "status": row.get("Status", "REVIEW_CANDIDATE"),
                })
            page_data["letter_names"] = entries
            total_letter_names += len(entries)
        else:
            page_data["page_kind"] = "READING"
            rows = sorted(reading_by_page[page], key=lambda r: int(r["Slot"]))
            if len(rows) != 24:
                raise ValueError(f"PAGE_OBJECT_COUNT page={page} actual={len(rows)}")
            objects = []
            for row in rows:
                text = row["ArabicObject"]
                units = split_units(text)
                if len(units) != int(row["UnitLength"]):
                    raise ValueError(f"UNIT_LENGTH_MISMATCH page={page} slot={row['Slot']}")
                objects.append({
                    "slot": int(row["Slot"]),
                    "object_id": row["ObjectID"],
                    "object_type": row["ObjectType"],
                    "competency_code": row["CompetencyCode"],
                    "competency_description": row["CompetencyDescription"],
                    "learning_state": row["LearningState"],
                    "source_ref": row["SourceRef"],
                    "text": text,
                    "unit_length": int(row["UnitLength"]),
                    "render_mode": "qae-native-short-vowel",
                    "tokens": units,
                })
            page_data["objects"] = objects
            page_data["letter_names"] = []
            total_reading += len(objects)

        (output_dir / f"page-{page:03d}.yaml").write_text(
            yaml.safe_dump(page_data, allow_unicode=True, sort_keys=False), encoding="utf-8"
        )

    print("PAGES_WRITTEN=40")
    print(f"READING_OBJECTS_WRITTEN={total_reading}")
    print(f"LETTER_NAMES_WRITTEN={total_letter_names}")
    print(f"OUTPUT_DIR={output_dir.relative_to(ROOT) if output_dir.is_relative_to(ROOT) else output_dir}")
    print("LAYOUT_ADAPTER_V2=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
