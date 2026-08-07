#!/usr/bin/env python3
"""Extract pedagogically valid Jilid 1 LETTER and WORD_FRAGMENT candidates.

This extractor delegates unit validation to the frozen QURBATA Pedagogical
Unit Engine. It preserves Quran source references and writes the standard
foundation candidate schema.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import sys
import unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
UNIT_ENGINE_PATH = ROOT / "content/qwo/pedagogy/runtime/pedagogical_unit_engine.py"


def load_unit_engine():
    spec = importlib.util.spec_from_file_location("qurbata_pedagogical_unit_engine", UNIT_ENGINE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("UNIT_ENGINE_IMPORT_FAILED")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


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

    try:
        unit_engine = load_unit_engine()
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    first_letters: dict[str, tuple[int, int]] = {}
    first_fragments: dict[str, tuple[int, int]] = {}
    fragment_counts: Counter[str] = Counter()
    rejected_reasons: Counter[str] = Counter()

    for surah, ayah, text in parse(Path(args.input)):
        for word in text.split():
            units = unit_engine.grapheme_units(word)

            for unit in units:
                decision = unit_engine.validate_short_vowel_unit(unit)
                if decision.passed:
                    normalized = unicodedata.normalize("NFC", unit)
                    first_letters.setdefault(normalized, (surah, ayah))
                else:
                    rejected_reasons.update(decision.reasons)

            for index in range(len(units) - 1):
                pair = unicodedata.normalize("NFC", "".join(units[index:index + 2]))
                passed, reasons = unit_engine.validate_short_vowel_fragment(pair)
                if not passed:
                    rejected_reasons.update(f"FRAGMENT_{reason}" for reason in reasons)
                    continue
                fragment_counts[pair] += 1
                first_fragments.setdefault(pair, (surah, ayah))

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
            fieldnames=["CanonicalKey", "ObjectType", "Text", "SourceRef", "WordCount"],
        )
        writer.writeheader()
        writer.writerows(rows)

    letter_count = sum(row["ObjectType"] == "LETTER" for row in rows)
    fragment_count = sum(row["ObjectType"] == "WORD_FRAGMENT" for row in rows)

    print("PEDAGOGICAL_UNIT_ENGINE=V1")
    print("PEDAGOGICAL_UNIT_MODEL=SHORT_VOWEL_EXACTLY_ONE")
    print(f"LETTER_OBJECTS={letter_count}")
    print(f"WORD_FRAGMENT_OBJECTS={fragment_count}")
    print(f"TOTAL_OBJECTS={len(rows)}")
    for reason, count in sorted(rejected_reasons.items()):
        print(f"REJECTED_{reason}={count}")
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
