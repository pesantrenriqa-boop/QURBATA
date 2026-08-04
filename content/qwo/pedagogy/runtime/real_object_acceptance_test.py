#!/usr/bin/env python3
from __future__ import annotations

import csv
import importlib.util
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
FIXTURES = ROOT / "content/qwo/pedagogy/tests/REAL-OBJECT-ACCEPTANCE-FIXTURES-V1.csv"
RULES = ROOT / "content/qwo/pedagogy/PEDAGOGICAL-RULE-MATRIX-V1.csv"
ENGINE = ROOT / "content/qwo/pedagogy/runtime/pedagogical_engine.py"


def fail(message: str) -> None:
    raise AssertionError(message)


def load_engine():
    spec = importlib.util.spec_from_file_location("qurbata_pedagogical_engine", ENGINE)
    if spec is None or spec.loader is None:
        fail("Cannot import pedagogical engine")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def word_count(text: str) -> int:
    return len([part for part in text.split() if part])


def strip_marks(text: str) -> str:
    return "".join(
        ch for ch in unicodedata.normalize("NFC", text)
        if not unicodedata.category(ch).startswith("M")
    )


def validate_extended(row: dict[str, str], engine, rules) -> tuple[bool, list[str]]:
    cid = row["CompetencyID"]
    object_type = row["ObjectType"]
    text = row["Text"]
    decision = engine.validate(text, object_type, cid, rules)
    reasons = list(decision.reasons)

    words = word_count(text)
    if cid == "C0033" and words != 2:
        reasons.append("PHRASE_WORD_COUNT")
    elif cid == "C0034" and not 3 <= words <= 4:
        reasons.append("PHRASE_WORD_COUNT")
    elif cid == "C0035" and not 4 <= words <= 8:
        reasons.append("FRAGMENT_WORD_COUNT")
    elif cid == "C0036" and not 8 <= words <= 15:
        reasons.append("FRAGMENT_WORD_COUNT")
    elif cid == "C0037" and not 1 <= words <= 7:
        reasons.append("AYAH_WORD_COUNT")
    elif cid == "C0038" and not 8 <= words <= 15:
        reasons.append("AYAH_WORD_COUNT")
    elif cid == "C0039" and words < 16:
        reasons.append("AYAH_WORD_COUNT")

    if cid == "C0040" and not any(mark in text for mark in "ۖۗۚۛۜۙ"):
        reasons.append("WAQF_MARK_REQUIRED")
    if cid == "C0041":
        feature_count = sum([
            "ّ" in text,
            "ْ" in text,
            any(mark in text for mark in "ًٌٍ"),
            any(ch in strip_marks(text) for ch in "ءأإؤئآٱ"),
            any(ch in text for ch in "ٰٓ"),
        ])
        if feature_count < 2:
            reasons.append("MULTI_COMPETENCY_REQUIRED")

    return not reasons, reasons


def main() -> int:
    engine = load_engine()
    rules = engine.load_rules(RULES)
    with FIXTURES.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        fail("No acceptance fixtures")

    failures: list[str] = []
    for row in rows:
        passed, reasons = validate_extended(row, engine, rules)
        expected = row["Expected"] == "PASS"
        if passed != expected:
            failures.append(
                f'{row["FixtureID"]} {row["CompetencyID"]} expected={row["Expected"]} '
                f'actual={"PASS" if passed else "FAIL"} reasons={reasons}'
            )

    if failures:
        fail("\n".join(failures))
    print(f"PASS real-object acceptance fixtures: {len(rows)}")
    print("QURBATA real-object gate: VERIFIED_PASS")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
