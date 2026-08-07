#!/usr/bin/env python3
"""Convert verified Jilid 1 composer CSV into 36 canonical layout YAML pages."""
from __future__ import annotations

import argparse
import csv
import unicodedata
from collections import defaultdict
from pathlib import Path

import yaml

SHORT_MARKS = {"َ", "ِ", "ُ"}


def split_short_units(text: str) -> list[str]:
    units: list[str] = []
    for char in unicodedata.normalize("NFC", text):
        if unicodedata.category(char).startswith("L"):
            units.append(char)
        elif units and unicodedata.category(char).startswith("M"):
            units[-1] += char
    for unit in units:
        marks = [char for char in unicodedata.normalize("NFD", unit) if unicodedata.category(char).startswith("M")]
        if len(marks) != 1 or marks[0] not in SHORT_MARKS:
            raise ValueError(f"INVALID_SHORT_UNIT: {unit!r} from {text!r}")
    return units


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        default="content/qwo/composer/output/jilid-1-pue-v1/JILID-1-READING-OBJECTS-V2.csv",
    )
    parser.add_argument("--output-dir", default="books/jilid-1/data-generated-pue-v1")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_dir = Path(args.output_dir)
    if not input_path.is_file():
        raise FileNotFoundError(input_path)

    with input_path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))

    grouped: dict[int, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[int(row["Page"])].append(row)

    if sorted(grouped) != list(range(1, 37)):
        raise ValueError("COMPOSER_PAGES_MUST_BE_1_TO_36")

    output_dir.mkdir(parents=True, exist_ok=True)
    total_objects = 0

    for page in range(1, 37):
        page_rows = sorted(grouped[page], key=lambda row: int(row["Slot"]))
        if len(page_rows) != 24:
            raise ValueError(f"PAGE_OBJECT_COUNT page={page} actual={len(page_rows)}")

        objects = []
        competencies: list[str] = []
        for row in page_rows:
            object_type = row["ObjectType"]
            text = row["ArabicObject"]
            competency = row["PrimaryCompetency"]
            if competency not in competencies:
                competencies.append(competency)
            item = {
                "slot": int(row["Slot"]),
                "object_id": row["ObjectID"],
                "object_type": object_type,
                "competency": competency,
                "source_ref": row["SourceRef"],
                "text": text,
            }
            if object_type in {"LETTER", "WORD_FRAGMENT"}:
                item["render_mode"] = "qae-short-vowel"
                item["tokens"] = split_short_units(text)
            elif object_type == "AWAIL_AL_SUWAR":
                item["render_mode"] = "raw-quran"
                item["tokens"] = []
            else:
                raise ValueError(f"UNSUPPORTED_OBJECT_TYPE: {object_type}")
            objects.append(item)

        data = {
            "schema_version": 1,
            "book": "QURBATA",
            "volume": 1,
            "page": page,
            "status": "composer-verified-layout-candidate",
            "layout": "canonical-24-slot-v1",
            "source": str(input_path).replace("\\", "/"),
            "identity": {
                "title": "QURBATA",
                "subtitle": f"JILID 1 • HALAMAN {page:02d}",
            },
            "targets": {
                "material_progress": f"{page:02d} / 36",
                "competencies": " | ".join(competencies),
                "memorization": "—",
                "nidom_hadith": "—",
                "arabic_language": "—",
            },
            "objects": objects,
            "footer": {
                "teacher_label": "Nama Guru",
                "date_label": "Tanggal",
                "score_label": "Nilai",
            },
        }
        output_path = output_dir / f"page-{page:03d}.yaml"
        output_path.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
        total_objects += len(objects)

    print(f"PAGES_WRITTEN={len(grouped)}")
    print(f"OBJECTS_WRITTEN={total_objects}")
    print(f"OUTPUT_DIR={output_dir}")
    print("LAYOUT_ADAPTER_STATUS=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
