#!/usr/bin/env python3
"""Build QURBATA Word Objects (QWO) from a verified whole-Quran text file.

Input format:
- one ayah per line, in canonical mushaf order (6236 lines), or
- `surah|ayah|text` per line.

The script never edits Quran text. It emits derived metadata records while
preserving the exact source token in `ArabicTextUthmani`.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
import unicodedata
from collections import Counter
from dataclasses import dataclass, asdict
from pathlib import Path

SURAH_AYAH_COUNTS = [
    7,286,200,176,120,165,206,75,129,109,123,111,43,52,99,128,111,110,
    98,135,112,78,118,64,77,227,93,88,69,60,34,30,73,54,45,83,182,88,
    75,85,54,53,89,59,37,35,38,29,18,45,60,49,62,55,78,96,29,22,24,
    13,14,11,11,18,12,12,30,52,52,44,28,28,20,56,40,31,50,40,46,42,
    29,19,36,25,22,17,19,26,30,20,15,21,11,8,8,19,5,8,8,11,11,8,3,
    9,5,4,7,3,6,3,5,4,5,6
]

ARABIC_LETTER_RE = re.compile(r"[\u0621-\u064A\u066E-\u06D3\u06FA-\u06FF]")
TOKEN_CLEAN_RE = re.compile(r"^[^\u0600-\u06FF]+|[^\u0600-\u06FF]+$")

FATHA = "\u064e"
DAMMA = "\u064f"
KASRA = "\u0650"
SUKUNS = {"\u0652", "\u06e1"}
SHADDA = "\u0651"
TANWIN = {"\u064b", "\u064c", "\u064d", "\u08f0", "\u08f1", "\u08f2"}
HAMZA_CHARS = set("ءأإؤئٱ")
ALIF_CHARS = set("اٱآىٰ")
YA_CHARS = set("ييىۦ")
WAW_CHARS = set("ووۥ")
PAUSE_AND_ORNAMENT = set("۞۩ۖۗۘۙۚۛۜ۝")


def strip_marks(text: str) -> str:
    return "".join(ch for ch in unicodedata.normalize("NFD", text)
                   if unicodedata.category(ch) != "Mn" and ch not in PAUSE_AND_ORNAMENT)


def arabic_letter_count(text: str) -> int:
    return sum(1 for ch in strip_marks(text) if ARABIC_LETTER_RE.match(ch))


def contains_mad_alif(text: str) -> bool:
    chars = list(text)
    return any(chars[i] == FATHA and chars[i + 1] in ALIF_CHARS for i in range(len(chars) - 1))


def contains_mad_ya(text: str) -> bool:
    chars = list(text)
    return any(chars[i] == KASRA and chars[i + 1] in YA_CHARS for i in range(len(chars) - 1))


def contains_mad_waw(text: str) -> bool:
    chars = list(text)
    return any(chars[i] == DAMMA and chars[i + 1] in WAW_CHARS for i in range(len(chars) - 1))


def bool01(value: bool) -> int:
    return 1 if value else 0


def feature_tags(text: str) -> list[str]:
    tags: list[str] = []
    if contains_mad_alif(text): tags.append("MAD_ALIF")
    if contains_mad_ya(text): tags.append("MAD_YA")
    if contains_mad_waw(text): tags.append("MAD_WAW")
    if any(ch in SUKUNS for ch in text): tags.append("SUKUN")
    if any(ch in TANWIN for ch in text): tags.append("TANWIN")
    if SHADDA in text: tags.append("SHADDA")
    if any(ch in HAMZA_CHARS for ch in text): tags.append("HAMZA")
    if strip_marks(text).startswith(("ال", "ٱل")): tags.append("ALIF_LAM")
    return tags or ["SHORT_VOWELS"]


def difficulty_score(text: str, frequency: int) -> int:
    length = arabic_letter_count(text)
    tags = set(feature_tags(text))
    score = 8 + max(0, length - 2) * 5
    weights = {
        "MAD_ALIF": 5, "MAD_YA": 6, "MAD_WAW": 6, "SUKUN": 8,
        "TANWIN": 8, "HAMZA": 10, "ALIF_LAM": 10, "SHADDA": 14,
    }
    score += sum(weights.get(tag, 0) for tag in tags)
    if frequency >= 100: score -= 8
    elif frequency >= 30: score -= 5
    elif frequency >= 10: score -= 2
    return max(1, min(100, score))


def pedagogical_score(text: str, frequency: int, difficulty: int) -> int:
    length = arabic_letter_count(text)
    score = 100 - difficulty
    if 3 <= length <= 5: score += 12
    elif length <= 7: score += 5
    if frequency >= 100: score += 12
    elif frequency >= 30: score += 8
    elif frequency >= 10: score += 4
    return max(1, min(100, score))


def inferred_min_volume(tags: set[str], length: int) -> int:
    volume = 1
    if length >= 3: volume = max(volume, 2)
    if {"MAD_ALIF", "MAD_YA", "MAD_WAW"} & tags: volume = max(volume, 3)
    if "SUKUN" in tags: volume = max(volume, 3)
    if "TANWIN" in tags: volume = max(volume, 3)
    if "ALIF_LAM" in tags: volume = max(volume, 4)
    if "HAMZA" in tags: volume = max(volume, 4)
    if "SHADDA" in tags: volume = max(volume, 5)
    if length >= 8: volume = max(volume, 6)
    return min(8, volume)


def target_competency(tags: set[str]) -> str:
    priority = [
        ("SHADDA", "QT-U-021"), ("ALIF_LAM", "QT-U-020"),
        ("HAMZA", "QT-U-019"), ("TANWIN", "QT-U-018"),
        ("SUKUN", "QT-U-016"), ("MAD_WAW", "QT-U-014"),
        ("MAD_YA", "QT-U-013"), ("MAD_ALIF", "QT-U-012"),
    ]
    for tag, code in priority:
        if tag in tags:
            return code
    return "QT-U-008"


def cumulative_competencies(target: str) -> str:
    try:
        n = int(target.rsplit("-", 1)[1])
    except (ValueError, IndexError):
        return target
    start = 1
    return ";".join(f"QT-U-{i:03d}" for i in range(start, n + 1))


def position_to_surah_ayah(line_index: int) -> tuple[int, int]:
    remaining = line_index + 1
    for surah, count in enumerate(SURAH_AYAH_COUNTS, start=1):
        if remaining <= count:
            return surah, remaining
        remaining -= count
    raise ValueError(f"Ayah line out of range: {line_index + 1}")


def parse_input(path: Path) -> list[tuple[int, int, str]]:
    records: list[tuple[int, int, str]] = []
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    for idx, raw in enumerate(lines):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split("|", 2)
        if len(parts) == 3 and parts[0].isdigit() and parts[1].isdigit():
            surah, ayah, text = int(parts[0]), int(parts[1]), parts[2]
        else:
            surah, ayah = position_to_surah_ayah(len(records))
            text = line
        records.append((surah, ayah, text))
    if len(records) != 6236:
        raise ValueError(f"Expected 6236 ayat, found {len(records)}")
    return records


def tokenize(text: str) -> list[str]:
    tokens: list[str] = []
    for raw in text.split():
        token = TOKEN_CLEAN_RE.sub("", raw)
        token = "".join(ch for ch in token if ch not in PAUSE_AND_ORNAMENT)
        if token and any(ARABIC_LETTER_RE.match(ch) for ch in strip_marks(token)):
            tokens.append(token)
    return tokens


def build_rows(ayahs: list[tuple[int, int, str]]) -> list[dict[str, object]]:
    normalized_tokens: list[str] = []
    occurrences: list[tuple[int, int, int, str, str]] = []
    for surah, ayah, text in ayahs:
        for pos, token in enumerate(tokenize(text), start=1):
            normalized = strip_marks(token)
            normalized_tokens.append(normalized)
            occurrences.append((surah, ayah, pos, token, normalized))
    frequencies = Counter(normalized_tokens)

    rows: list[dict[str, object]] = []
    for qwo_no, (surah, ayah, pos, token, normalized) in enumerate(occurrences, start=1):
        tags = set(feature_tags(token))
        length = arabic_letter_count(token)
        freq = frequencies[normalized]
        difficulty = difficulty_score(token, freq)
        pedagogy = pedagogical_score(token, freq, difficulty)
        target = target_competency(tags)
        volume = inferred_min_volume(tags, length)
        rows.append({
            "QWO_ID": f"QWO-{qwo_no:06d}",
            "ObjectType": "QWO",
            "ArabicTextUthmani": token,
            "ArabicTextNormalized": normalized,
            "Surah": surah,
            "Ayah": ayah,
            "WordPosition": pos,
            "OccurrenceFrequency": freq,
            "LetterCount": length,
            "FeatureTags": ";".join(sorted(tags)),
            "TargetCompetency": target,
            "RequiredCompetencies": cumulative_competencies(target).rsplit(";", 1)[0] if ";" in cumulative_competencies(target) else "",
            "CumulativeCompetencies": cumulative_competencies(target),
            "DifficultyScore": difficulty,
            "PedagogicalScore": pedagogy,
            "AllowedFromJilid": volume,
            "AllowedFromPage": 1,
            "ReviewWeight": max(1, min(100, pedagogy + min(freq, 20))),
            "SourceType": "TANZIL_DERIVED_QURAN_TEXT",
            "SourceStatus": "QURAN_VERIFIED_SOURCE_PENDING_QURBATA_QA",
            "ReusePolicy": "UNIQUE_BLOCK_10",
            "Status": "CANDIDATE",
        })
    return rows


def write_csv(rows: list[dict[str, object]], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", default=Path("content/qlo/generated/QWO-WHOLE-QURAN-CANDIDATES.csv"), type=Path)
    args = parser.parse_args()
    try:
        ayahs = parse_input(args.input)
        rows = build_rows(ayahs)
        write_csv(rows, args.output)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"Generated {len(rows):,} QWO occurrence records -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
