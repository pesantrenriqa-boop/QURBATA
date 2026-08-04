#!/usr/bin/env python3
"""Compose QURBATA Jilid 1 candidate pages from a Tanzil-style Uthmani corpus.

Input line format: surah|ayah|text
Output: 36 reading pages x 24 unique Quran-sourced objects.
Pages 37-40 remain non-QWO pages: evaluation, hafalan, Arabic integration,
and final evaluation.
"""

from __future__ import annotations

import argparse
import csv
import re
import unicodedata
from collections import Counter
from pathlib import Path

BASE_RE = re.compile(r"[\u0621-\u063A\u0641-\u064A\u066E\u066F\u0671\u0672-\u06D3]")
BASIC = {"َ": "FATHA", "ِ": "KASRA", "ُ": "DAMMA"}
NON_CONNECTORS = set("ادذرزوأإآٱؤءى")
AWAIL = ["الٓمٓ", "الٓمٓصٓ", "الٓر", "الٓمٓر", "كٓهيعٓصٓ", "طه", "طسٓمٓ", "طسٓ", "يسٓ", "صٓ", "حمٓ", "عٓسٓقٓ", "قٓ", "نٓ"]


def clean_token(token: str) -> str:
    output: list[str] = []
    for char in unicodedata.normalize("NFC", token):
        code = ord(char)
        if BASE_RE.fullmatch(char):
            output.append(char)
        elif output and unicodedata.combining(char):
            if not (0x06D6 <= code <= 0x06ED or 0x08D4 <= code <= 0x08FF):
                output.append(char)
    return "".join(output)


def grapheme_units(text: str) -> list[str]:
    result: list[str] = []
    for char in text:
        if BASE_RE.fullmatch(char):
            result.append(char)
        elif result and unicodedata.combining(char):
            result[-1] += char
    return result


def base(unit: str) -> str:
    return next((char for char in unit if BASE_RE.fullmatch(char)), "")


def marks(unit: str) -> str:
    return "".join(char for char in unit if unicodedata.combining(char))


def is_basic_unit(unit: str) -> bool:
    unit_marks = marks(unit)
    return len(unit_marks) == 1 and unit_marks in BASIC


def is_safe_pair(first: str, second: str) -> bool:
    if not is_basic_unit(first) or not is_basic_unit(second):
        return False
    first_marks = marks(first)
    second_base = base(second)
    if first_marks == "َ" and second_base in "اأإآٱى":
        return False
    if first_marks == "ِ" and second_base == "ي":
        return False
    if first_marks == "ُ" and second_base == "و":
        return False
    return True


def load_occurrences(path: Path) -> list[tuple[int, int, int, str, list[str]]]:
    rows: list[tuple[int, int, int, str, list[str]]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        parts = line.split("|", 2)
        if len(parts) != 3 or not parts[0].isdigit() or not parts[1].isdigit():
            continue
        surah, ayah, text = int(parts[0]), int(parts[1]), parts[2]
        for token_index, token in enumerate(text.split(), 1):
            rows.append((surah, ayah, token_index, token, grapheme_units(clean_token(token))))
    return rows


def build(corpus: Path, output: Path) -> None:
    occurrences = load_occurrences(corpus)
    singles: dict[str, tuple] = {}
    connected: dict[str, tuple] = {}
    disconnected: dict[str, tuple] = {}
    awail_map: dict[str, tuple] = {}

    for surah, ayah, token_index, token, units in occurrences:
        if token in AWAIL and token not in awail_map:
            awail_map[token] = (surah, ayah, token_index, token)
        for position, unit in enumerate(units, 1):
            if is_basic_unit(unit):
                singles.setdefault(unit, (surah, ayah, token_index, position, token, base(unit), BASIC[marks(unit)]))
        for index in range(len(units) - 1):
            first, second = units[index], units[index + 1]
            if not is_safe_pair(first, second):
                continue
            surface = unicodedata.normalize("NFC", first + second)
            metadata = (surah, ayah, token_index, index + 1, token)
            target = disconnected if base(first) in NON_CONNECTORS else connected
            target.setdefault(surface, metadata)

    letter_order = list("ابتثجحخدذرزسشصضطظعغفقكلمنهويءأإؤئٱىة")
    vowel_order = {"FATHA": 0, "KASRA": 1, "DAMMA": 2}
    single_items = sorted(
        singles.items(),
        key=lambda item: (
            letter_order.index(item[1][5]) if item[1][5] in letter_order else 99,
            vowel_order[item[1][6]],
            item[0],
        ),
    )
    disconnected_items = sorted(disconnected.items())
    connected_items = sorted(connected.items())

    pages: list[dict[str, object]] = []
    used: set[str] = set()

    def add(page: int, slot: int, obj: str, object_type: str, competency: str, metadata: tuple, note: str) -> None:
        if obj in used:
            raise ValueError(f"Repeated Arabic object: {obj}")
        used.add(obj)
        surah, ayah, token_index = metadata[:3]
        token = metadata[4] if len(metadata) > 4 else metadata[3]
        pages.append({
            "Jilid": 1,
            "Page": page,
            "Slot": slot,
            "ObjectID": f"J1-P{page:02d}-S{slot:02d}",
            "ObjectType": object_type,
            "ArabicObject": obj,
            "PrimaryCompetency": competency,
            "SourceRef": f"{surah}:{ayah}",
            "TokenIndex": token_index,
            "SourceToken": token,
            "Status": "CANDIDATE_PAGE",
            "Notes": note,
        })

    single_index = 0
    for page in range(1, 5):
        for slot in range(1, 25):
            obj, metadata = single_items[single_index]
            single_index += 1
            competency = {"FATHA": "C0002", "KASRA": "C0003", "DAMMA": "C0004"}[metadata[6]]
            add(page, slot, obj, "LETTER", competency, metadata, "Huruf tunggal dari token Al-Quran")

    disconnected_index = connected_index = 0
    for page in range(5, 37):
        slot = 1
        if page in (20, 30):
            selected_awail = AWAIL[:7] if page == 20 else AWAIL[7:]
            for obj in selected_awail:
                if obj in awail_map and obj not in used:
                    surah, ayah, token_index, token = awail_map[obj]
                    add(page, slot, obj, "AWAIL_AL_SUWAR", "SPECIAL_AWAIL", (surah, ayah, token_index, 0, token), "Awailus suwar tanpa pengulangan")
                    slot += 1
        while slot <= 24:
            if page <= 12:
                obj, metadata = disconnected_items[disconnected_index]
                disconnected_index += 1
                competency = "C0005"
            elif page <= 19:
                obj, metadata = connected_items[connected_index]
                connected_index += 1
                competency = "C0006"
            elif (slot + page) % 2 == 0:
                obj, metadata = disconnected_items[disconnected_index]
                disconnected_index += 1
                competency = "C0005"
            else:
                obj, metadata = connected_items[connected_index]
                connected_index += 1
                competency = "C0006"
            if obj in used:
                continue
            add(page, slot, obj, "WORD_FRAGMENT", competency, metadata, "Review kompetensi dengan objek baru" if page >= 21 else "Fragmen dua huruf dari kata Al-Quran")
            slot += 1

    output.mkdir(parents=True, exist_ok=True)
    fields = list(pages[0].keys())
    with (output / "JILID-1-READING-OBJECTS-V1.csv").open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(pages)

    audit: list[dict[str, object]] = []
    for page in range(1, 37):
        page_rows = [row for row in pages if row["Page"] == page]
        type_counts = Counter(row["ObjectType"] for row in page_rows)
        competency_counts = Counter(row["PrimaryCompetency"] for row in page_rows)
        audit.append({
            "Page": page,
            "ObjectCount": len(page_rows),
            "ObjectTypes": "|".join(f"{key}:{value}" for key, value in type_counts.items()),
            "Competencies": "|".join(f"{key}:{value}" for key, value in competency_counts.items()),
            "DuplicateObjects": len(page_rows) - len({row["ArabicObject"] for row in page_rows}),
        })
    with (output / "JILID-1-PAGE-AUDIT-SUMMARY-V1.csv").open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=list(audit[0].keys()))
        writer.writeheader()
        writer.writerows(audit)

    if len(pages) != 864 or len(used) != 864:
        raise ValueError(f"Unexpected output: rows={len(pages)}, unique={len(used)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("corpus", type=Path)
    parser.add_argument("output", type=Path)
    arguments = parser.parse_args()
    build(arguments.corpus, arguments.output)
