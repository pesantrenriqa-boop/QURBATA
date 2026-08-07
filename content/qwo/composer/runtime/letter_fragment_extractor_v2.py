#!/usr/bin/env python3
"""Extract QURBATA Jilid 1 LETTER and WORD_FRAGMENT candidates."""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import unicodedata
from pathlib import Path

ARABIC_BASE = re.compile(r"[\u0621-\u063A\u0641-\u064A\u0671]")
SHORT_MARKS = {"\u064e", "\u064f", "\u0650"}  # fathah, dhammah, kasrah
ANNOTATION_RANGES = ((0x06D6, 0x06ED), (0x08D4, 0x08FF))


def is_annotation(ch: str) -> bool:
    cp = ord(ch)
    return any(start <= cp <= end for start, end in ANNOTATION_RANGES)


def graphemes(word: str) -> list[str]:
    result: list[str] = []

    for ch in unicodedata.normalize("NFC", word):
        if is_annotation(ch):
            continue

        if unicodedata.combining(ch):
            if result:
                result[-1] += ch
        elif ARABIC_BASE.fullmatch(ch):
            result.append(ch)

    return result


def base_letter(grapheme: str) -> str:
    return "".join(
        ch for ch in grapheme
        if not unicodedata.combining(ch)
    )


def marks(grapheme: str) -> set[str]:
    return {
        ch for ch in grapheme
        if unicodedata.combining(ch)
    }


def j1_letter_safe(grapheme: str) -> bool:
    found = marks(grapheme)
    return len(base_letter(grapheme)) == 1 and len(found) == 1 and found <= SHORT_MARKS


def j1_fragment_safe(fragment: str) -> bool:
    return all(
        not unicodedata.combining(ch) or ch in SHORT_MARKS
        for ch in fragment
    )


def canonical_key(object_type: str, text: str) -> str:
    raw = f"{object_type}|{text}".encode("utf-8")
    return hashlib.sha256(raw).hexdigest()[:20]


def parse(path: Path):
    with path.open(encoding="utf-8-sig") as handle:
        for raw in handle:
            line = raw.rstrip("\r\n")

            if not line or line.startswith("#"):
                continue

            parts = line.split("|", 2)

            if len(parts) == 3 and parts[0].isdigit() and parts[1].isdigit():
                yield int(parts[0]), int(parts[1]), parts[2]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("--output", required=True)
    parser.add_argument("--fragment-limit", type=int, default=5000)
    args = parser.parse_args()

    first_letters: dict[str, tuple[int, int]] = {}
    first_fragments: dict[str, tuple[int, int]] = {}
    fragment_counts: dict[str, int] = {}

    for surah, ayah, text in parse(Path(args.input)):
        for word in text.split():
            gs = graphemes(word)

            for grapheme in gs:
                if j1_letter_safe(grapheme):
                    first_letters.setdefault(grapheme, (surah, ayah))

            for index in range(len(gs) - 1):
                fragment = unicodedata.normalize(
                    "NFC",
                    "".join(gs[index:index + 2]),
                )

                if not j1_fragment_safe(fragment):
                    continue

                fragment_counts[fragment] = fragment_counts.get(fragment, 0) + 1
                first_fragments.setdefault(fragment, (surah, ayah))

    ranked_fragments = sorted(
        first_fragments,
        key=lambda value: (-fragment_counts[value], value),
    )[:args.fragment_limit]

    rows: list[dict[str, str]] = []

    for text, (surah, ayah) in sorted(first_letters.items()):
        rows.append({
            "CanonicalKey": canonical_key("LETTER", text),
            "ObjectType": "LETTER",
            "Text": text,
            "SourceRef": f"{surah}:{ayah}",
            "WordCount": "1",
        })

    for text in ranked_fragments:
        surah, ayah = first_fragments[text]

        rows.append({
            "CanonicalKey": canonical_key("WORD_FRAGMENT", text),
            "ObjectType": "WORD_FRAGMENT",
            "Text": text,
            "SourceRef": f"{surah}:{ayah}",
            "WordCount": "1",
        })

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

    print(f"LETTER_OBJECTS={letter_count}")
    print(f"WORD_FRAGMENT_OBJECTS={fragment_count}")
    print(f"TOTAL_OBJECTS={len(rows)}")
    print(f"OUTPUT={output}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
