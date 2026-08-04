#!/usr/bin/env python3
"""QURBATA launch-focused QWO pipeline V1.

Input: JSONL Quran token occurrences.
Output: token occurrence CSV, lexeme CSV, and up to N unique QWO candidates.

This implementation intentionally stays narrow for launch:
- imports verified Quran tokens;
- preserves Uthmani text;
- derives reproducible search/canonical forms;
- detects core reading competencies;
- emits non-repeating candidate objects;
- never promotes candidates beyond CANDIDATE.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable

ARABIC_MARKS = {
    "\u064b", "\u064c", "\u064d", "\u064e", "\u064f", "\u0650",
    "\u0651", "\u0652", "\u0653", "\u0654", "\u0655", "\u0670",
}
QURAN_ANNOTATION_RANGES = ((0x06D6, 0x06ED), (0x08D4, 0x08FF))
NON_CONNECTORS = set("ا د ذ ر ز و أ إ آ ٱ ؤ ء ى".replace(" ", ""))

FATHA = "\u064e"
DAMMA = "\u064f"
KASRA = "\u0650"
SUKUN = "\u0652"
SHADDA = "\u0651"
TANWIN_FATH = "\u064b"
TANWIN_DAMM = "\u064c"
TANWIN_KASR = "\u064d"
DAGGER_ALIF = "\u0670"


class PipelineError(ValueError):
    pass


@dataclass(frozen=True)
class Occurrence:
    occurrence_id: str
    surah_number: int
    ayah_number: int
    token_index: int
    uthmani_token: str
    search_token: str
    canonical_key: str
    source_edition: str
    source_checksum: str
    verification_status: str


@dataclass(frozen=True)
class Candidate:
    qwo_id: str
    arabic_word: str
    canonical_key: str
    source_ref: str
    occurrence_id: str
    target_competency: str
    secondary_competencies: str
    rule_trace: str
    status: str


def is_quran_annotation(ch: str) -> bool:
    code = ord(ch)
    return any(start <= code <= end for start, end in QURAN_ANNOTATION_RANGES)


def nfc(text: str) -> str:
    return unicodedata.normalize("NFC", text.strip())


def make_search_token(uthmani: str) -> str:
    text = nfc(uthmani)
    return "".join(
        ch for ch in text
        if not is_quran_annotation(ch)
        and unicodedata.category(ch) not in {"Cf", "Cc"}
    )


def make_canonical_key(search_token: str) -> str:
    decomposed = unicodedata.normalize("NFD", search_token)
    letters_only = "".join(
        ch for ch in decomposed
        if unicodedata.category(ch) != "Mn" and not is_quran_annotation(ch)
    )
    return unicodedata.normalize("NFC", letters_only)


def checksum_record(record: dict) -> str:
    payload = json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def stable_id(prefix: str, payload: str, length: int = 16) -> str:
    digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()[:length].upper()
    return f"{prefix}-{digest}"


def validate_record(record: dict, line_no: int) -> None:
    required = {"surah_number", "ayah_number", "token_index", "uthmani_token", "source_edition"}
    missing = sorted(required - set(record))
    if missing:
        raise PipelineError(f"line {line_no}: missing fields: {', '.join(missing)}")
    for name in ("surah_number", "ayah_number", "token_index"):
        if not isinstance(record[name], int) or record[name] < 1:
            raise PipelineError(f"line {line_no}: {name} must be a positive integer")
    if not isinstance(record["uthmani_token"], str) or not record["uthmani_token"].strip():
        raise PipelineError(f"line {line_no}: uthmani_token must be non-empty")
    if not isinstance(record["source_edition"], str) or not record["source_edition"].strip():
        raise PipelineError(f"line {line_no}: source_edition must be non-empty")


def load_occurrences(path: Path) -> list[Occurrence]:
    occurrences: list[Occurrence] = []
    seen_positions: set[tuple[int, int, int]] = set()

    with path.open("r", encoding="utf-8") as handle:
        for line_no, raw in enumerate(handle, start=1):
            if not raw.strip():
                continue
            try:
                record = json.loads(raw)
            except json.JSONDecodeError as exc:
                raise PipelineError(f"line {line_no}: invalid JSON: {exc.msg}") from exc
            validate_record(record, line_no)

            position = (record["surah_number"], record["ayah_number"], record["token_index"])
            if position in seen_positions:
                raise PipelineError(f"line {line_no}: duplicate token position {position}")
            seen_positions.add(position)

            uthmani = nfc(record["uthmani_token"])
            search = make_search_token(uthmani)
            canonical = make_canonical_key(search)
            if not canonical:
                raise PipelineError(f"line {line_no}: canonical token is empty")

            source_payload = {
                "surah_number": record["surah_number"],
                "ayah_number": record["ayah_number"],
                "token_index": record["token_index"],
                "uthmani_token": uthmani,
                "source_edition": record["source_edition"],
            }
            position_key = f"{position[0]}:{position[1]}:{position[2]}:{uthmani}"
            occurrences.append(Occurrence(
                occurrence_id=stable_id("OCC", position_key),
                surah_number=position[0],
                ayah_number=position[1],
                token_index=position[2],
                uthmani_token=uthmani,
                search_token=search,
                canonical_key=canonical,
                source_edition=record["source_edition"].strip(),
                source_checksum=checksum_record(source_payload),
                verification_status=record.get("verification_status", "IMPORTED"),
            ))
    if not occurrences:
        raise PipelineError("input corpus contains no token occurrences")
    return occurrences


def pairs(text: str) -> Iterable[tuple[str, str]]:
    chars = list(text)
    return zip(chars, chars[1:])


def detect_competencies(token: str, canonical: str) -> tuple[list[str], list[str]]:
    found: list[str] = []
    trace: list[str] = []

    checks = [
        ("TANWIN_FATH", TANWIN_FATH in token, "contains U+064B"),
        ("TANWIN_DAMM", TANWIN_DAMM in token, "contains U+064C"),
        ("TANWIN_KASR", TANWIN_KASR in token, "contains U+064D"),
        ("SUKUN", SUKUN in token, "contains U+0652"),
        ("TASYDID", SHADDA in token, "contains U+0651"),
        ("DAGGER_ALIF", DAGGER_ALIF in token, "contains U+0670"),
        ("ALIF_LAM", canonical.startswith("ال"), "canonical starts with ال"),
        ("TA_MARBUTHAH", "ة" in canonical, "canonical contains ة"),
        ("HAMZAH", any(ch in canonical for ch in "ءأإؤئآ"), "canonical contains hamzah form"),
        ("ALIF_MAQSHURAH", "ى" in canonical, "canonical contains ى"),
    ]
    for name, matched, reason in checks:
        if matched:
            found.append(name)
            trace.append(f"{name}:{reason}")

    # Sequence-based mad detection on the vocalized token.
    for left, right in pairs(token):
        if left == FATHA and right in {"ا", "آ"}:
            found.append("MAD_ALIF")
            trace.append("MAD_ALIF:fatha followed by alif")
        elif left == KASRA and right == "ي":
            found.append("MAD_YA")
            trace.append("MAD_YA:kasra followed by ya")
        elif left == DAMMA and right == "و":
            found.append("MAD_WAW")
            trace.append("MAD_WAW:damma followed by waw")

    letters = list(canonical)
    if len(letters) == 1:
        found.append("SINGLE_LETTER")
        trace.append("SINGLE_LETTER:one canonical letter")
    elif len(letters) == 2:
        found.append("TWO_LETTER_FORM")
        trace.append("TWO_LETTER_FORM:two canonical letters")
    elif len(letters) == 3:
        found.append("THREE_LETTER_FORM")
        trace.append("THREE_LETTER_FORM:three canonical letters")
    elif len(letters) >= 4:
        found.append("FOUR_PLUS_LETTER_FORM")
        trace.append("FOUR_PLUS_LETTER_FORM:four or more canonical letters")

    if any(ch in NON_CONNECTORS for ch in letters[:-1]):
        found.append("NON_CONNECTOR_TRANSITION")
        trace.append("NON_CONNECTOR_TRANSITION:non-connector before final position")
    else:
        found.append("CONNECTED_FORM")
        trace.append("CONNECTED_FORM:no internal non-connector detected")

    # Preserve order and remove duplicates.
    unique = list(dict.fromkeys(found))
    return unique, trace


def choose_target(competencies: list[str]) -> str:
    priority = [
        "SINGLE_LETTER", "TWO_LETTER_FORM", "THREE_LETTER_FORM",
        "MAD_ALIF", "MAD_YA", "MAD_WAW",
        "TANWIN_FATH", "TANWIN_KASR", "TANWIN_DAMM",
        "SUKUN", "TASYDID", "ALIF_LAM", "HAMZAH",
        "TA_MARBUTHAH", "ALIF_MAQSHURAH",
        "NON_CONNECTOR_TRANSITION", "FOUR_PLUS_LETTER_FORM", "CONNECTED_FORM",
    ]
    return next((name for name in priority if name in competencies), competencies[0])


def build_candidates(occurrences: list[Occurrence], limit: int) -> list[Candidate]:
    # One object per canonical form. Repetition of competencies is allowed;
    # repetition of the same object is not.
    first_by_canonical: dict[str, Occurrence] = {}
    for occurrence in occurrences:
        first_by_canonical.setdefault(occurrence.canonical_key, occurrence)

    ranked: list[tuple[int, int, str, Occurrence, list[str], list[str]]] = []
    frequencies = Counter(o.canonical_key for o in occurrences)
    for canonical, occurrence in first_by_canonical.items():
        competencies, trace = detect_competencies(occurrence.search_token, canonical)
        if not competencies:
            continue
        # Prefer compact, frequent Quran objects while retaining deterministic order.
        ranked.append((-frequencies[canonical], len(canonical), canonical, occurrence, competencies, trace))
    ranked.sort(key=lambda row: (row[0], row[1], row[2]))

    candidates: list[Candidate] = []
    for _, _, canonical, occurrence, competencies, trace in ranked[:limit]:
        target = choose_target(competencies)
        secondary = [item for item in competencies if item != target]
        identity = f"{canonical}|{target}|{occurrence.occurrence_id}"
        candidates.append(Candidate(
            qwo_id=stable_id("QWO", identity),
            arabic_word=occurrence.uthmani_token,
            canonical_key=canonical,
            source_ref=f"{occurrence.surah_number}:{occurrence.ayah_number}:{occurrence.token_index}",
            occurrence_id=occurrence.occurrence_id,
            target_competency=target,
            secondary_competencies="|".join(secondary),
            rule_trace="|".join(trace),
            status="CANDIDATE",
        ))
    return candidates


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        raise PipelineError(f"cannot write empty CSV: {path}")
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_report(path: Path, occurrences: list[Occurrence], candidates: list[Candidate]) -> None:
    competency_counts = Counter(c.target_competency for c in candidates)
    report = {
        "pipeline_version": "1.0.0",
        "occurrence_count": len(occurrences),
        "unique_canonical_count": len({o.canonical_key for o in occurrences}),
        "candidate_count": len(candidates),
        "duplicate_objects_emitted": 0,
        "candidate_status": "CANDIDATE",
        "target_competency_distribution": dict(sorted(competency_counts.items())),
        "corpus_checksum": hashlib.sha256(
            "\n".join(o.source_checksum for o in occurrences).encode("utf-8")
        ).hexdigest(),
    }
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate unique QURBATA QWO candidates from Quran JSONL tokens")
    parser.add_argument("--input", required=True, type=Path, help="JSONL token corpus")
    parser.add_argument("--output-dir", required=True, type=Path, help="output directory")
    parser.add_argument("--limit", type=int, default=2500, help="maximum unique candidates (default: 2500)")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.limit < 1:
        print("error: --limit must be positive", file=sys.stderr)
        return 2
    try:
        occurrences = load_occurrences(args.input)
        candidates = build_candidates(occurrences, args.limit)
        if not candidates:
            raise PipelineError("no candidates generated")

        args.output_dir.mkdir(parents=True, exist_ok=True)
        write_csv(args.output_dir / "TOKEN_OCCURRENCE.csv", [asdict(row) for row in occurrences])
        write_csv(args.output_dir / "MASTER_QWO_CANDIDATES.csv", [asdict(row) for row in candidates])

        grouped: dict[str, list[Occurrence]] = defaultdict(list)
        for occurrence in occurrences:
            grouped[occurrence.canonical_key].append(occurrence)
        lexemes = []
        for canonical, items in sorted(grouped.items()):
            lexemes.append({
                "lexeme_id": stable_id("LEX", canonical),
                "canonical_key": canonical,
                "primary_uthmani_form": items[0].uthmani_token,
                "uthmani_variants": "|".join(sorted({item.uthmani_token for item in items})),
                "search_form": items[0].search_token,
                "occurrence_count": len(items),
                "source_refs": "|".join(f"{item.surah_number}:{item.ayah_number}:{item.token_index}" for item in items),
                "mapper_status": "MAPPED",
                "review_priority": "NORMAL",
            })
        write_csv(args.output_dir / "LEXEME_ENTRY.csv", lexemes)
        write_report(args.output_dir / "PIPELINE_REPORT.json", occurrences, candidates)
    except (OSError, PipelineError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(f"generated {len(candidates)} unique QWO candidates in {args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
