#!/usr/bin/env python3
"""Compose QURBATA Jilid 1 from the frozen foundation candidate pool.

Inputs:
- JILID-1-FOUNDATION-OBJECTS-V2.csv
- Tanzil-style Uthmani corpus (surah|ayah|text)
- JILID-1-40-PAGE-BLUEPRINT-V1.csv

Outputs:
- JILID-1-READING-OBJECTS-V2.csv (pages 1-36, 24 slots/page)
- JILID-1-PAGE-AUDIT-SUMMARY-V2.csv
- JILID-1-COMPOSER-REPORT-V2.txt

The composer is deterministic, preserves Quran source references, never repeats
an Arabic surface object, and reserves pages 37-40 for non-reading content.
"""

from __future__ import annotations

import argparse
import csv
import re
import unicodedata
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from pathlib import Path

BASIC_MARK_TO_COMPETENCY = {
    "َ": "C0002",
    "ِ": "C0003",
    "ُ": "C0004",
}

BASE_RE = re.compile(r"[\u0621-\u063A\u0641-\u064A\u0671]")
NON_CONNECTORS = set("ادذرزوأإآٱؤءى")
LETTER_ORDER = list("ابتثجحخدذرزسشصضطظعغفقكلمنهويءأإؤئٱىة")
VOWEL_ORDER = {"َ": 0, "ِ": 1, "ُ": 2}
AWAIL = [
    "الٓمٓ",
    "الٓمٓصٓ",
    "الٓر",
    "الٓمٓر",
    "كٓهيعٓصٓ",
    "طه",
    "طسٓمٓ",
    "طسٓ",
    "يسٓ",
    "صٓ",
    "حمٓ",
    "عٓسٓقٓ",
    "قٓ",
    "نٓ",
]


@dataclass(frozen=True)
class Candidate:
    key: str
    object_type: str
    text: str
    source_ref: str


def base_letters(text: str) -> list[str]:
    return [ch for ch in unicodedata.normalize("NFC", text) if BASE_RE.fullmatch(ch)]


def combining_marks(text: str) -> list[str]:
    return [ch for ch in unicodedata.normalize("NFC", text) if unicodedata.combining(ch)]


def letter_sort_key(candidate: Candidate) -> tuple[int, int, str]:
    letters = base_letters(candidate.text)
    marks = combining_marks(candidate.text)
    base = letters[0] if letters else ""
    mark = marks[0] if marks else ""
    return (
        LETTER_ORDER.index(base) if base in LETTER_ORDER else 999,
        VOWEL_ORDER.get(mark, 999),
        candidate.text,
    )


def fragment_sort_key(candidate: Candidate) -> tuple[str, str, str]:
    return candidate.text, candidate.source_ref, candidate.key


def load_candidates(path: Path) -> list[Candidate]:
    if not path.is_file():
        raise FileNotFoundError(f"FOUNDATION_POOL_NOT_FOUND {path}")

    result: list[Candidate] = []
    seen_keys: set[str] = set()

    with path.open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            key = row["CanonicalKey"].strip()
            object_type = row["ObjectType"].strip()
            text = unicodedata.normalize("NFC", row["Text"].strip())
            source_ref = row["SourceRef"].strip()

            if not key or key in seen_keys or not text or not source_ref:
                continue
            if object_type not in {"LETTER", "WORD_FRAGMENT"}:
                continue

            seen_keys.add(key)
            result.append(Candidate(key, object_type, text, source_ref))

    return result


def load_blueprint(path: Path) -> dict[int, dict[str, str]]:
    if not path.is_file():
        raise FileNotFoundError(f"BLUEPRINT_NOT_FOUND {path}")

    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))

    blueprint = {int(row["Page"]): row for row in rows}
    if sorted(blueprint) != list(range(1, 41)):
        raise ValueError("BLUEPRINT_MUST_DEFINE_PAGES_1_TO_40")

    for page in range(1, 37):
        expected = int(blueprint[page]["TargetObjectCount"])
        if expected != 24:
            raise ValueError(f"READING_PAGE_TARGET_MUST_BE_24 page={page} actual={expected}")

    return blueprint


def load_awail(corpus: Path) -> dict[str, str]:
    if not corpus.is_file():
        raise FileNotFoundError(f"CORPUS_NOT_FOUND {corpus}")

    found: dict[str, str] = {}
    with corpus.open(encoding="utf-8-sig") as handle:
        for raw in handle:
            line = raw.rstrip("\r\n")
            if not line or line.startswith("#"):
                continue
            parts = line.split("|", 2)
            if len(parts) != 3 or not parts[0].isdigit() or not parts[1].isdigit():
                continue
            surah, ayah, text = parts
            for token in text.split():
                token = unicodedata.normalize("NFC", token)
                if token in AWAIL and token not in found:
                    found[token] = f"{surah}:{ayah}"

    missing = [item for item in AWAIL if item not in found]
    if missing:
        raise ValueError(f"AWAIL_NOT_FOUND missing={'|'.join(missing)}")
    return found


def classify_foundation(candidates: list[Candidate]) -> tuple[list[Candidate], list[Candidate], list[Candidate]]:
    letters: list[Candidate] = []
    disconnected: list[Candidate] = []
    connected: list[Candidate] = []

    for candidate in candidates:
        if candidate.object_type == "LETTER":
            units = base_letters(candidate.text)
            marks = combining_marks(candidate.text)
            if len(units) == 1 and len(marks) == 1 and marks[0] in BASIC_MARK_TO_COMPETENCY:
                letters.append(candidate)
            continue

        units = base_letters(candidate.text)
        marks = combining_marks(candidate.text)
        if len(units) != 2 or any(mark not in BASIC_MARK_TO_COMPETENCY for mark in marks):
            continue

        if units[0] in NON_CONNECTORS:
            disconnected.append(candidate)
        else:
            connected.append(candidate)

    letters.sort(key=letter_sort_key)
    disconnected.sort(key=fragment_sort_key)
    connected.sort(key=fragment_sort_key)
    return letters, disconnected, connected


def compose(
    foundation: Path,
    corpus: Path,
    blueprint_path: Path,
    output_dir: Path,
) -> None:
    blueprint = load_blueprint(blueprint_path)
    candidates = load_candidates(foundation)
    awail_sources = load_awail(corpus)
    letters, disconnected, connected = classify_foundation(candidates)

    if len(letters) < 96:
        raise ValueError(f"LETTER_POOL_SHORTAGE required=96 actual={len(letters)}")
    if len(disconnected) < 192:
        raise ValueError(f"C0005_POOL_SHORTAGE required=192 actual={len(disconnected)}")
    if len(connected) < 168:
        raise ValueError(f"C0006_POOL_SHORTAGE required=168 actual={len(connected)}")

    disconnected_queue = deque(disconnected)
    connected_queue = deque(connected)
    rows: list[dict[str, str | int]] = []
    used_texts: set[str] = set()

    def add_row(
        page: int,
        slot: int,
        candidate: Candidate,
        competency: str,
        object_type: str,
        note: str,
    ) -> None:
        if candidate.text in used_texts:
            raise ValueError(f"DUPLICATE_ARABIC_OBJECT text={candidate.text}")
        used_texts.add(candidate.text)
        rows.append(
            {
                "Jilid": 1,
                "Page": page,
                "PageRole": blueprint[page]["PageRole"],
                "Slot": slot,
                "ObjectID": f"J1-P{page:02d}-S{slot:02d}",
                "CanonicalKey": candidate.key,
                "ObjectType": object_type,
                "ArabicObject": candidate.text,
                "PrimaryCompetency": competency,
                "ReviewCompetencies": blueprint[page]["ReviewCompetencyIDs"],
                "SourceRef": candidate.source_ref,
                "Status": "COMPOSED_CANDIDATE_V2",
                "Notes": note,
            }
        )

    for index, candidate in enumerate(letters[:96]):
        page = index // 24 + 1
        slot = index % 24 + 1
        mark = combining_marks(candidate.text)[0]
        add_row(
            page,
            slot,
            candidate,
            BASIC_MARK_TO_COMPETENCY[mark],
            "LETTER",
            "Huruf tunggal berharakat pendek dari corpus Al-Quran",
        )

    def take_fragment(prefer_disconnected: bool) -> tuple[Candidate, str]:
        primary = disconnected_queue if prefer_disconnected else connected_queue
        secondary = connected_queue if prefer_disconnected else disconnected_queue
        competency = "C0005" if prefer_disconnected else "C0006"

        while primary:
            candidate = primary.popleft()
            if candidate.text not in used_texts:
                return candidate, competency
        while secondary:
            candidate = secondary.popleft()
            if candidate.text not in used_texts:
                fallback = "C0006" if prefer_disconnected else "C0005"
                return candidate, fallback
        raise ValueError("WORD_FRAGMENT_POOL_EXHAUSTED")

    for page in range(5, 37):
        slot = 1

        if page in {20, 30}:
            awail_subset = AWAIL[:7] if page == 20 else AWAIL[7:]
            for awail in awail_subset:
                source_ref = awail_sources[awail]
                candidate = Candidate(
                    key=f"AWAIL-{page:02d}-{slot:02d}",
                    object_type="AWAIL_AL_SUWAR",
                    text=awail,
                    source_ref=source_ref,
                )
                add_row(
                    page,
                    slot,
                    candidate,
                    "SPECIAL_AWAIL",
                    "AWAIL_AL_SUWAR",
                    "Awailus suwar tanpa pengulangan",
                )
                slot += 1

        while slot <= 24:
            if page <= 12:
                prefer_disconnected = True
            elif page <= 19:
                prefer_disconnected = False
            else:
                prefer_disconnected = (page + slot) % 2 == 0

            candidate, competency = take_fragment(prefer_disconnected)
            add_row(
                page,
                slot,
                candidate,
                competency,
                "WORD_FRAGMENT",
                "Fragmen dua huruf dari corpus Al-Quran; objek tidak diulang",
            )
            slot += 1

    expected_rows = 36 * 24
    if len(rows) != expected_rows:
        raise ValueError(f"ROW_COUNT_MISMATCH expected={expected_rows} actual={len(rows)}")
    if len(used_texts) != expected_rows:
        raise ValueError(f"UNIQUE_COUNT_MISMATCH expected={expected_rows} actual={len(used_texts)}")

    output_dir.mkdir(parents=True, exist_ok=True)
    reading_output = output_dir / "JILID-1-READING-OBJECTS-V2.csv"
    fields = [
        "Jilid",
        "Page",
        "PageRole",
        "Slot",
        "ObjectID",
        "CanonicalKey",
        "ObjectType",
        "ArabicObject",
        "PrimaryCompetency",
        "ReviewCompetencies",
        "SourceRef",
        "Status",
        "Notes",
    ]
    with reading_output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    audit_rows: list[dict[str, str | int]] = []
    grouped: dict[int, list[dict[str, str | int]]] = defaultdict(list)
    for row in rows:
        grouped[int(row["Page"])].append(row)

    for page in range(1, 37):
        page_rows = grouped[page]
        type_counts = Counter(str(row["ObjectType"]) for row in page_rows)
        competency_counts = Counter(str(row["PrimaryCompetency"]) for row in page_rows)
        audit_rows.append(
            {
                "Page": page,
                "PageRole": blueprint[page]["PageRole"],
                "ObjectCount": len(page_rows),
                "ObjectTypes": "|".join(f"{key}:{value}" for key, value in sorted(type_counts.items())),
                "Competencies": "|".join(f"{key}:{value}" for key, value in sorted(competency_counts.items())),
                "DuplicateObjects": len(page_rows) - len({str(row["ArabicObject"]) for row in page_rows}),
                "Status": "PASS" if len(page_rows) == 24 else "FAIL",
            }
        )

    audit_output = output_dir / "JILID-1-PAGE-AUDIT-SUMMARY-V2.csv"
    with audit_output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(audit_rows[0].keys()))
        writer.writeheader()
        writer.writerows(audit_rows)

    competency_counts = Counter(str(row["PrimaryCompetency"]) for row in rows)
    report_output = output_dir / "JILID-1-COMPOSER-REPORT-V2.txt"
    report_lines = [
        "QURBATA JILID 1 COMPOSER V2",
        "STATUS=COMPOSED_CANDIDATE_PASS",
        f"READING_PAGES=36",
        f"OBJECTS_PER_PAGE=24",
        f"TOTAL_OBJECTS={len(rows)}",
        f"UNIQUE_ARABIC_OBJECTS={len(used_texts)}",
        f"LETTER_POOL_AVAILABLE={len(letters)}",
        f"C0005_POOL_AVAILABLE={len(disconnected)}",
        f"C0006_POOL_AVAILABLE={len(connected)}",
        "COMPETENCY_COUNTS=" + "|".join(f"{key}:{value}" for key, value in sorted(competency_counts.items())),
        f"READING_OUTPUT={reading_output}",
        f"AUDIT_OUTPUT={audit_output}",
        "NON_READING_PAGES=37:EVALUATION|38:HAFALAN|39:ARABIC_INTEGRATION|40:FINAL_EVALUATION",
    ]
    report_output.write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    print("JILID1_COMPOSER_V2=PASS")
    print(f"TOTAL_OBJECTS={len(rows)}")
    print(f"UNIQUE_OBJECTS={len(used_texts)}")
    print(f"READING_OUTPUT={reading_output}")
    print(f"AUDIT_OUTPUT={audit_output}")
    print(f"REPORT_OUTPUT={report_output}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--foundation",
        default="content/qwo/production/generated/JILID-1-FOUNDATION-OBJECTS-V2.csv",
    )
    parser.add_argument(
        "--corpus",
        default="content/qwo/corpus/quran-uthmani.txt",
    )
    parser.add_argument(
        "--blueprint",
        default="content/qwo/composer/templates/JILID-1-40-PAGE-BLUEPRINT-V1.csv",
    )
    parser.add_argument(
        "--output-dir",
        default="content/qwo/composer/output/jilid-1-v2",
    )
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[4]

    def resolve(value: str) -> Path:
        path = Path(value)
        return path if path.is_absolute() else root / path

    compose(
        resolve(args.foundation),
        resolve(args.corpus),
        resolve(args.blueprint),
        resolve(args.output_dir),
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
