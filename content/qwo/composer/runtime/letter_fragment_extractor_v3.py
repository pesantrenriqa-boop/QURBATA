#!/usr/bin/env python3
"""Extract pedagogically valid Jilid 1 LETTER and WORD_FRAGMENT candidates.

This v3 extractor treats a QURBATA reading unit as a base Arabic letter carrying
exactly one short vowel (fathah, kasrah, or dhammah). It rejects units with:
- no short vowel,
- more than one combining mark,
- sukun, shadda, tanwin, dagger alif, madd marks, or Quran annotations.

Input format: surah|ayah|text
Output schema matches the frozen foundation candidate pool.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import unicodedata
from collections import Counter
from pathlib import Path

ARABIC_BASE = re.compile(r"[\u0621-\u063A\u0641-\u064A\u0671]")
SHORT_MARKS = {"\u064e", "\u064f", "\u0650"}  # fathah, dhammah, kasrah
ANNOTATION_RANGES = ((0x06D6, 0x06ED), (0x08D4, 0x08FF))


def is_annotation(ch: str) -> bool:
    codepoint = ord(ch)
    return any(start <= codepoint <= end for start, end in ANNOTATION_RANGES)


def grapheme_units(word: str) -> list[str]:
    units: list[str] = []

    for ch in unicodedata.normalize("NFC", word):
        if is_annotation(ch):
            continue

        if ARABIC_BASE.fullmatch(ch):
            units.append(ch)
            continue

        if unicodedata.combining(ch) and units:
            units[-1] += ch

    return units


def unit_base(unit: str) -> str:
    return next((ch for ch in unit if ARABIC_BASE.fullmatch(ch)), "")


def unit_marks(unit: str) -> list[str]:
    return [ch for ch in unit if unicodedata.combining(ch)]


def is_pedagogical_short_unit(unit: str) -> bool:
    base = unit_base(unit)
    marks = unit_marks(unit)
    return bool(base) and len(marks) == 1 and marks[0] in SHORT_MARKS


def is_valid_fragment(units: list[str]) -> bool:
    return len(units) == 2 and all(is_pedagogical_short_unit(unit) for unit in units)


def canonical_key(object_type: str, text: str) -> str:
    raw = f"{object_type}|{unicodedata.normalize('NFC', text)}".encode("utf-8")
    return hashlib.sha256(raw).hexdigest()[:20]


def parse(path: Path):
    with path.open(encoding="utf-8-sig") as handle:
        for raw in handle:
            line = raw.rstrip("\r\n")

            if not line or line.startswith("#"):
                continue

            parts = line.split("|", 2)
            if len(parts) != 3 or not parts[0].isdigit() or not parts[1].isdigit():
                continue

            yield int(parts[0]), int(parts[1]), parts[2]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("--output", required=True)
    parser.add_argument("--fragment-limit", type=int, default=5000)
    args = parser.parse_args()

    first_letters: dict[str, tuple[int, int]] = {}
    first_fragments: dict[str, tuple[int, int]] = {}
    fragment_counts: Counter[str] = Counter()

    rejected_units_no_mark = 0
    rejected_units_multi_mark = 0
    rejected_units_non_short = 0
    rejected_fragments = 0

    for surah, ayah, text in parse(Path(args.input)):
        for word in text.split():
            units = grapheme_units(word)

            for unit in units:
                marks = unit_marks(unit)
                if is_pedagogical_short_unit(unit):
                    normalized = unicodedata.normalize("NFC", unit)
                    first_letters.setdefault(normalized, (surah, ayah))
                elif not marks:
                    rejected_units_no_mark += 1
                elif len(marks) > 1:
                    rejected_units_multi_mark += 1
                else:
                    rejected_units_non_short += 1

            for index in range(len(units) - 1):
                pair_units = units[index:index + 2]
                if not is_valid_fragment(pair_units):
                    rejected_fragments += 1
                    continue

                fragment = unicodedata.normalize("NFC", "".join(pair_units))
                fragment_counts[fragment] += 1
                first_fragments.setdefault(fragment, (surah, ayah))

    ranked_fragments = sorted(
        first_fragments,
        key=lambda value: (-fragment_counts[value], value),
    )[: args.fragment_limit]

    rows: list[dict[str, str]] = []

    for text, (surah, ayah) in sorted(first_letters.items()):
        rows.append(
            {
                "CanonicalKey": canonical_key("LETTER", text),
                "ObjectType": "LETTER",
                "Text": text,
                "SourceRef": f"{surah}:{ayah}",
                "WordCount": "1",
            }
        )

    for text in ranked_fragments:
        surah, ayah = first_fragments[text]
        rows.append(
            {
                "CanonicalKey": canonical_key("WORD_FRAGMENT", text),
                "ObjectType": "WORD_FRAGMENT",
                "Text": text,
                "SourceRef": f"{surah}:{ayah}",
                "WordCount": "1",
            }
        )

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)

    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "CanonicalKey",
                "ObjectType",
                "Text",
                "SourceRef",
                "WordCount",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    letter_count = sum(row["ObjectType"] == "LETTER" for row in rows)
    fragment_count = sum(row["ObjectType"] == "WORD_FRAGMENT" for row in rows)

    print("PEDAGOGICAL_UNIT_MODEL=SHORT_VOWEL_EXACTLY_ONE")
    print(f"LETTER_OBJECTS={letter_count}")
    print(f"WORD_FRAGMENT_OBJECTS={fragment_count}")
    print(f"TOTAL_OBJECTS={len(rows)}")
    print(f"REJECTED_UNITS_NO_MARK={rejected_units_no_mark}")
    print(f"REJECTED_UNITS_MULTI_MARK={rejected_units_multi_mark}")
    print(f"REJECTED_UNITS_NON_SHORT={rejected_units_non_short}")
    print(f"REJECTED_FRAGMENTS={rejected_fragments}")
    print(f"OUTPUT={output}")

    if letter_count < 81:
        print("FOUNDATION_STATUS=LETTER_SHORTAGE")
        return 3
    if fragment_count < 500:
        print("FOUNDATION_STATUS=FRAGMENT_SHORTAGE")
        return 4

    print("FOUNDATION_STATUS=PEDAGOGICALLY_VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
