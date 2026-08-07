#!/usr/bin/env python3
"""QURBATA Pedagogical Unit Engine v1.

Defines the smallest teachable reading units used by the early QURBATA levels.
The engine is Unicode-aware but pedagogically stricter than raw grapheme
segmentation.

Foundation model:
- SHORT_VOWEL_UNIT: exactly one Arabic base letter carrying exactly one of
  fathah, kasrah, or dhammah.
- SHORT_VOWEL_FRAGMENT: exactly two SHORT_VOWEL_UNIT values.
- Quranic annotation marks are ignored before validation.
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass

ARABIC_BASE = re.compile(r"[\u0621-\u063A\u0641-\u064A\u0671]")
SHORT_MARKS = {"\u064e", "\u064f", "\u0650"}
ANNOTATION_RANGES = ((0x06D6, 0x06ED), (0x08D4, 0x08FF))
NON_CONNECTORS = set("ادذرزوأإآٱؤءى")


@dataclass(frozen=True)
class UnitDecision:
    passed: bool
    base: str
    marks: tuple[str, ...]
    reasons: tuple[str, ...]


def normalize(text: str) -> str:
    return unicodedata.normalize("NFC", text)


def is_annotation(ch: str) -> bool:
    codepoint = ord(ch)
    return any(start <= codepoint <= end for start, end in ANNOTATION_RANGES)


def grapheme_units(text: str) -> list[str]:
    """Return Arabic base-letter units with attached non-annotation marks."""
    units: list[str] = []
    for ch in normalize(text):
        if is_annotation(ch):
            continue
        if ARABIC_BASE.fullmatch(ch):
            units.append(ch)
        elif unicodedata.combining(ch) and units:
            units[-1] += ch
    return units


def unit_base(unit: str) -> str:
    return next((ch for ch in normalize(unit) if ARABIC_BASE.fullmatch(ch)), "")


def unit_marks(unit: str) -> tuple[str, ...]:
    return tuple(
        ch
        for ch in normalize(unit)
        if unicodedata.combining(ch) and not is_annotation(ch)
    )


def validate_short_vowel_unit(unit: str) -> UnitDecision:
    base = unit_base(unit)
    marks = unit_marks(unit)
    reasons: list[str] = []

    if not base:
        reasons.append("NO_BASE_LETTER")
    if len(marks) == 0:
        reasons.append("NO_MARK")
    elif len(marks) > 1:
        reasons.append("MULTIPLE_MARKS")
    elif marks[0] not in SHORT_MARKS:
        reasons.append("MARK_NOT_SHORT_VOWEL")

    return UnitDecision(not reasons, base, marks, tuple(reasons))


def is_short_vowel_unit(unit: str) -> bool:
    return validate_short_vowel_unit(unit).passed


def validate_short_vowel_fragment(text: str) -> tuple[bool, tuple[str, ...]]:
    units = grapheme_units(text)
    reasons: list[str] = []

    if len(units) != 2:
        reasons.append(f"UNIT_COUNT_{len(units)}")
        return False, tuple(reasons)

    for index, unit in enumerate(units, start=1):
        decision = validate_short_vowel_unit(unit)
        reasons.extend(f"UNIT_{index}_{reason}" for reason in decision.reasons)

    return not reasons, tuple(reasons)


def is_short_vowel_fragment(text: str) -> bool:
    passed, _ = validate_short_vowel_fragment(text)
    return passed


def first_base(text: str) -> str:
    units = grapheme_units(text)
    return unit_base(units[0]) if units else ""


def has_nonconnector_transition(text: str) -> bool:
    return first_base(text) in NON_CONNECTORS


def has_connector_transition(text: str) -> bool:
    base = first_base(text)
    return bool(base) and base not in NON_CONNECTORS
