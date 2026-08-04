#!/usr/bin/env python3
"""Build and validate QURBATA Word Objects (QWO) from verified Quran text.

Input formats:
- one ayah per line in canonical mushaf order (6236 lines); or
- ``surah|ayah|text`` per line.

The script preserves the exact source token in ``ArabicTextUthmani`` and emits
candidate metadata. It never grants ACTIVE/QURAN_VERIFIED status automatically;
those statuses require QURBATA human QA.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

SURAH_AYAH_COUNTS = [
    7, 286, 200, 176, 120, 165, 206, 75, 129, 109, 123, 111, 43, 52, 99,
    128, 111, 110, 98, 135, 112, 78, 118, 64, 77, 227, 93, 88, 69, 60, 34,
    30, 73, 54, 45, 83, 182, 88, 75, 85, 54, 53, 89, 59, 37, 35, 38, 29,
    18, 45, 60, 49, 62, 55, 78, 96, 29, 22, 24, 13, 14, 11, 11, 18, 12,
    12, 30, 52, 52, 44, 28, 28, 20, 56, 40, 31, 50, 40, 46, 42, 29, 19,
    36, 25, 22, 17, 19, 26, 30, 20, 15, 21, 11, 8, 8, 19, 5, 8, 8, 11,
    11, 8, 3, 9, 5, 4, 7, 3, 6, 3, 5, 4, 5, 6,
]

ARABIC_LETTER_RE = re.compile(r"[\u0621-\u064A\u066E-\u06D3\u06FA-\u06FF]")
TOKEN_CLEAN_RE = re.compile(r"^[^\u0600-\u06FF]+|[^\u0600-\u06FF]+$")
CANONICAL_UNIT_RE = re.compile(r"^QT-UK-\d{3}$")
SOURCE_RE = re.compile(r"^[1-9]\d{0,2}:[1-9]\d{0,2}$")

FATHA = "\u064e"
DAMMA = "\u064f"
KASRA = "\u0650"
SUKUNS = {"\u0652", "\u06e1"}
SHADDA = "\u0651"
TANWIN_FATH = {"\u064b", "\u08f0"}
TANWIN_DAMM = {"\u064c", "\u08f1"}
TANWIN_KASR = {"\u064d", "\u08f2"}
TANWIN = TANWIN_FATH | TANWIN_DAMM | TANWIN_KASR
HAMZA_CHARS = set("ءأإؤئٱ")
ALIF_CHARS = set("اٱآ")
ALIF_MAQSURAH_CHARS = set("ىٰ")
YA_CHARS = set("يىۦ")
WAW_CHARS = set("وۥ")
PAUSE_AND_ORNAMENT = set("۞۩ۖۗۘۙۚۛۜ۝")
VALID_OBJECT_STATUS = {"ACTIVE", "REVIEW", "HOLD", "DEPRECATED"}
VALID_SOURCE_STATUS = {"QURAN_VERIFIED", "QURAN_CANDIDATE", "HOLD"}

# Canonical competency units from QCF-001.
UNIT_MIN_VOLUME = {
    "QT-UK-001": 1, "QT-UK-002": 1, "QT-UK-003": 1, "QT-UK-004": 1,
    "QT-UK-005": 1, "QT-UK-006": 1, "QT-UK-007": 1, "QT-UK-008": 1,
    "QT-UK-009": 2, "QT-UK-010": 2, "QT-UK-011": 2, "QT-UK-012": 2,
    "QT-UK-013": 2, "QT-UK-014": 3, "QT-UK-015": 3, "QT-UK-016": 3,
    "QT-UK-017": 3, "QT-UK-018": 3, "QT-UK-019": 3, "QT-UK-020": 4,
    "QT-UK-021": 4, "QT-UK-022": 4, "QT-UK-023": 5, "QT-UK-024": 4,
    "QT-UK-025": 5, "QT-UK-026": 1, "QT-UK-027": 1, "QT-UK-028": 6,
    "QT-UK-029": 7, "QT-UK-030": 8, "QT-UK-031": 3, "QT-UK-032": 6,
    "QT-UK-033": 5, "QT-UK-034": 5,
}


def strip_marks(text: str) -> str:
    return "".join(
        ch for ch in unicodedata.normalize("NFD", text)
        if unicodedata.category(ch) != "Mn" and ch not in PAUSE_AND_ORNAMENT
    )


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


def feature_tags(text: str) -> list[str]:
    tags: list[str] = []
    if contains_mad_alif(text): tags.append("MAD_ALIF")
    if contains_mad_ya(text): tags.append("MAD_YA")
    if contains_mad_waw(text): tags.append("MAD_WAW")
    if any(ch in SUKUNS for ch in text): tags.append("SUKUN")
    if any(ch in TANWIN_FATH for ch in text): tags.append("TANWIN_FATH")
    if any(ch in TANWIN_DAMM for ch in text): tags.append("TANWIN_DAMM")
    if any(ch in TANWIN_KASR for ch in text): tags.append("TANWIN_KASR")
    if SHADDA in text: tags.append("SHADDA")
    if any(ch in HAMZA_CHARS for ch in text): tags.append("HAMZA")
    if strip_marks(text).startswith(("ال", "ٱل")): tags.append("ALIF_LAM")
    if any(ch in ALIF_MAQSURAH_CHARS for ch in text): tags.append("ALIF_MAQSURAH")
    return tags or ["SHORT_VOWELS"]


def difficulty_score(text: str, frequency: int) -> int:
    length = arabic_letter_count(text)
    tags = set(feature_tags(text))
    score = 8 + max(0, length - 2) * 5
    weights = {
        "MAD_ALIF": 5, "MAD_YA": 6, "MAD_WAW": 6, "SUKUN": 8,
        "TANWIN_FATH": 8, "TANWIN_DAMM": 8, "TANWIN_KASR": 8,
        "HAMZA": 10, "ALIF_LAM": 10, "SHADDA": 14,
        "ALIF_MAQSURAH": 10,
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


def target_competency(tags: set[str], length: int) -> str:
    priority = [
        ("ALIF_MAQSURAH", "QT-UK-032"),
        ("SHADDA", "QT-UK-023"),
        ("ALIF_LAM", "QT-UK-021"),
        ("TANWIN_DAMM", "QT-UK-020"),
        ("TANWIN_KASR", "QT-UK-020"),
        ("TANWIN_FATH", "QT-UK-019"),
        ("SUKUN", "QT-UK-031"),
        ("MAD_WAW", "QT-UK-015"),
        ("MAD_YA", "QT-UK-014"),
        ("MAD_ALIF", "QT-UK-011"),
    ]
    for tag, code in priority:
        if tag in tags:
            return code
    if length >= 3:
        return "QT-UK-009"
    return "QT-UK-008"


def required_competencies(target: str) -> list[str]:
    dependencies = {
        "QT-UK-008": ["QT-UK-001"],
        "QT-UK-009": ["QT-UK-008"],
        "QT-UK-011": ["QT-UK-009"],
        "QT-UK-014": ["QT-UK-012"],
        "QT-UK-015": ["QT-UK-013"],
        "QT-UK-019": ["QT-UK-012", "QT-UK-013", "QT-UK-014", "QT-UK-015"],
        "QT-UK-020": ["QT-UK-019"],
        "QT-UK-021": ["QT-UK-020"],
        "QT-UK-023": ["QT-UK-020", "QT-UK-021", "QT-UK-022"],
        "QT-UK-031": ["QT-UK-009", "QT-UK-012", "QT-UK-013"],
        "QT-UK-032": ["QT-UK-028"],
    }
    return dependencies.get(target, [])


def inferred_min_volume(target: str, length: int) -> int:
    volume = UNIT_MIN_VOLUME[target]
    if length >= 8:
        volume = max(volume, 6)
    return min(8, volume)


def position_to_surah_ayah(line_index: int) -> tuple[int, int]:
    remaining = line_index + 1
    for surah, count in enumerate(SURAH_AYAH_COUNTS, start=1):
        if remaining <= count:
            return surah, remaining
        remaining -= count
    raise ValueError(f"Ayah line out of range: {line_index + 1}")


def validate_surah_ayah(surah: int, ayah: int) -> None:
    if not 1 <= surah <= 114:
        raise ValueError(f"Invalid surah number: {surah}")
    max_ayah = SURAH_AYAH_COUNTS[surah - 1]
    if not 1 <= ayah <= max_ayah:
        raise ValueError(f"Invalid ayah {surah}:{ayah}; maximum is {max_ayah}")


def parse_input(path: Path) -> list[tuple[int, int, str]]:
    records: list[tuple[int, int, str]] = []
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    for raw in lines:
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split("|", 2)
        if len(parts) == 3 and parts[0].isdigit() and parts[1].isdigit():
            surah, ayah, text = int(parts[0]), int(parts[1]), parts[2].strip()
        else:
            surah, ayah = position_to_surah_ayah(len(records))
            text = line
        validate_surah_ayah(surah, ayah)
        if not text:
            raise ValueError(f"Empty Quran text at {surah}:{ayah}")
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


def validate_generated_row(row: dict[str, object]) -> list[str]:
    errors: list[str] = []
    target = str(row["TargetCompetency"])
    required = [x for x in str(row["RequiredCompetencies"]).split(";") if x]
    volume = int(row["AllowedFromJilid"])
    source = f'{row["Surah"]}:{row["Ayah"]}'

    if not CANONICAL_UNIT_RE.fullmatch(target) or target not in UNIT_MIN_VOLUME:
        errors.append(f"unknown target competency {target}")
    for code in required:
        if not CANONICAL_UNIT_RE.fullmatch(code) or code not in UNIT_MIN_VOLUME:
            errors.append(f"unknown required competency {code}")
    if target in required:
        errors.append("target competency cannot also be a prerequisite")
    if target in UNIT_MIN_VOLUME and volume < UNIT_MIN_VOLUME[target]:
        errors.append(
            f"volume {volume} is earlier than {target} minimum {UNIT_MIN_VOLUME[target]}"
        )
    if not SOURCE_RE.fullmatch(source):
        errors.append(f"invalid source {source}")
    if str(row["Status"]) not in VALID_OBJECT_STATUS:
        errors.append(f'invalid object status {row["Status"]}')
    if str(row["SourceStatus"]) not in VALID_SOURCE_STATUS:
        errors.append(f'invalid source status {row["SourceStatus"]}')
    if str(row["Status"]) == "ACTIVE" and str(row["SourceStatus"]) != "QURAN_VERIFIED":
        errors.append("ACTIVE object must have QURAN_VERIFIED source")
    return errors


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
        target = target_competency(tags, length)
        required = required_competencies(target)
        volume = inferred_min_volume(target, length)
        cumulative = required + [target]
        row: dict[str, object] = {
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
            "RequiredCompetencies": ";".join(required),
            "CumulativeCompetencies": ";".join(cumulative),
            "DifficultyScore": difficulty,
            "PedagogicalScore": pedagogy,
            "AllowedFromJilid": volume,
            "AllowedFromPage": 1,
            "ReviewWeight": max(1, min(100, pedagogy + min(freq, 20))),
            "SourceType": "VERIFIED_QURAN_TEXT_IMPORT",
            "SourceStatus": "QURAN_CANDIDATE",
            "ReusePolicy": "UNIQUE_BLOCK_10",
            "Status": "REVIEW",
        }
        errors = validate_generated_row(row)
        if errors:
            raise ValueError(f'{row["QWO_ID"]} ({surah}:{ayah}:{pos}): ' + "; ".join(errors))
        rows.append(row)
    return rows


def validate_csv(path: Path) -> tuple[int, list[str]]:
    errors: list[str] = []
    count = 0
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        required_columns = {
            "TargetCompetency", "RequiredCompetencies", "AllowedFromJilid",
            "Status", "SourceStatus", "Surah", "Ayah",
        }
        missing = required_columns - set(reader.fieldnames or [])
        if missing:
            return 0, [f"missing columns: {', '.join(sorted(missing))}"]
        for line_no, row in enumerate(reader, start=2):
            count += 1
            try:
                row_errors = validate_generated_row(row)
            except (TypeError, ValueError) as exc:
                row_errors = [f"invalid field value: {exc}"]
            errors.extend(f"line {line_no}: {error}" for error in row_errors)
    return count, errors


def write_csv(rows: list[dict[str, object]], output: Path) -> None:
    if not rows:
        raise ValueError("No Quran word objects generated")
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, help="verified 6236-ayah Quran text")
    parser.add_argument(
        "--output",
        default=Path("content/qlo/generated/QWO-WHOLE-QURAN-CANDIDATES.csv"),
        type=Path,
    )
    parser.add_argument("--validate-csv", type=Path, help="validate an existing QWO CSV")
    args = parser.parse_args()

    if bool(args.input) == bool(args.validate_csv):
        parser.error("provide exactly one of --input or --validate-csv")

    try:
        if args.validate_csv:
            count, errors = validate_csv(args.validate_csv)
            if errors:
                for error in errors:
                    print(f"ERROR: {error}", file=sys.stderr)
                print(f"Validation failed: {len(errors)} error(s) in {count} row(s)", file=sys.stderr)
                return 1
            print(f"Validation passed: {count} QWO row(s)")
            return 0

        ayahs = parse_input(args.input)
        rows = build_rows(ayahs)
        write_csv(rows, args.output)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(f"Generated {len(rows):,} REVIEW QWO records -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
