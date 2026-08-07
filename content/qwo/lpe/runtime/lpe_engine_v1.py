#!/usr/bin/env python3
"""QURBATA Learning Progression Engine v1.

This runtime makes the Jilid 1 progression contract executable.  It validates
page-blueprint rules before any composer is allowed to select Quran objects.
"""
from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

EXPECTED_PAGES = tuple(range(1, 41))
ALLOWED_LENGTHS = {1, 2, 3}
FORBIDDEN_JILID1_OBJECT_TYPES = {"AWAIL_AL_SUWAR"}
REQUIRED_INJECTIONS = {20: "LETTER_NAMES", 40: "LETTER_NAMES"}


@dataclass(frozen=True)
class PageRule:
    page: int
    page_role: str
    allowed_unit_lengths: frozenset[int]
    special_injection: str
    awailus_suwar_allowed: bool
    competency_display_required: bool
    memorization_description_required: bool
    arabic_description_required: bool
    status: str


def _yes(value: str) -> bool:
    normalized = (value or "").strip().upper()
    if normalized not in {"YES", "NO"}:
        raise ValueError(f"BOOLEAN_FIELD_INVALID: {value!r}")
    return normalized == "YES"


def _lengths(value: str) -> frozenset[int]:
    try:
        values = frozenset(int(part) for part in (value or "").split("|") if part)
    except ValueError as exc:
        raise ValueError(f"UNIT_LENGTHS_INVALID: {value!r}") from exc
    if not values or not values <= ALLOWED_LENGTHS:
        raise ValueError(f"UNIT_LENGTHS_OUT_OF_RANGE: {value!r}")
    return values


def load_progression(path: str | Path) -> dict[int, PageRule]:
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(path)
    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))

    rules: dict[int, PageRule] = {}
    for row in rows:
        page = int(row["Page"])
        if page in rules:
            raise ValueError(f"DUPLICATE_PAGE_RULE: {page}")
        rules[page] = PageRule(
            page=page,
            page_role=row["PageRole"].strip(),
            allowed_unit_lengths=_lengths(row["AllowedUnitLengths"]),
            special_injection=row["SpecialInjection"].strip().upper(),
            awailus_suwar_allowed=_yes(row["AwailusSuwarAllowed"]),
            competency_display_required=_yes(row["CompetencyDisplayRequired"]),
            memorization_description_required=_yes(row["MemorizationDescriptionRequired"]),
            arabic_description_required=_yes(row["ArabicDescriptionRequired"]),
            status=row["Status"].strip(),
        )
    return rules


def validate_blueprint(rules: dict[int, PageRule]) -> list[str]:
    issues: list[str] = []
    pages = tuple(sorted(rules))
    if pages != EXPECTED_PAGES:
        issues.append(f"PAGE_SEQUENCE_INVALID actual={pages} expected=1..40")

    for page, rule in sorted(rules.items()):
        if rule.awailus_suwar_allowed:
            issues.append(f"AWAILUS_SUWAR_MUST_BE_FORBIDDEN page={page}")
        if not rule.competency_display_required:
            issues.append(f"COMPETENCY_DESCRIPTION_NOT_REQUIRED page={page}")
        if not rule.memorization_description_required:
            issues.append(f"MEMORIZATION_DESCRIPTION_NOT_REQUIRED page={page}")
        if not rule.arabic_description_required:
            issues.append(f"ARABIC_DESCRIPTION_NOT_REQUIRED page={page}")

        required = REQUIRED_INJECTIONS.get(page)
        if required and rule.special_injection != required:
            issues.append(
                f"REQUIRED_INJECTION_MISSING page={page} expected={required} actual={rule.special_injection}"
            )
        if not required and rule.special_injection == "LETTER_NAMES":
            issues.append(f"LETTER_NAMES_UNEXPECTED page={page}")

    # Hard learning-ladder regression checks.
    for page in range(1, 5):
        if page in rules and rules[page].allowed_unit_lengths != frozenset({1}):
            issues.append(f"FOUNDATION_MUST_BE_SINGLE_ONLY page={page}")
    for page in range(5, 13):
        if page in rules and not rules[page].allowed_unit_lengths <= frozenset({1, 2}):
            issues.append(f"TRIPLE_INTRODUCED_TOO_EARLY page={page}")
    for page in range(13, 41):
        if page in rules and 3 not in rules[page].allowed_unit_lengths:
            issues.append(f"TRIPLE_STAGE_MISSING page={page}")

    return issues


def validate_page_object(
    *,
    page: int,
    object_type: str,
    unit_length: int | None,
    rules: dict[int, PageRule],
) -> list[str]:
    issues: list[str] = []
    rule = rules.get(page)
    if rule is None:
        return [f"PAGE_NOT_DEFINED: {page}"]

    object_type = (object_type or "").strip().upper()
    if object_type in FORBIDDEN_JILID1_OBJECT_TYPES:
        issues.append(f"FORBIDDEN_OBJECT_TYPE page={page} type={object_type}")

    if unit_length is not None and unit_length not in rule.allowed_unit_lengths:
        allowed = "|".join(str(value) for value in sorted(rule.allowed_unit_lengths))
        issues.append(
            f"UNIT_LENGTH_NOT_ALLOWED page={page} actual={unit_length} allowed={allowed}"
        )
    return issues


def validate_metadata(
    *,
    page: int,
    competency_code: str,
    competency_description: str,
    memorization_code: str = "",
    memorization_description: str = "",
    arabic_code: str = "",
    arabic_description: str = "",
    rules: dict[int, PageRule],
) -> list[str]:
    issues: list[str] = []
    rule = rules.get(page)
    if rule is None:
        return [f"PAGE_NOT_DEFINED: {page}"]

    if rule.competency_display_required:
        if not competency_code.strip():
            issues.append(f"COMPETENCY_CODE_MISSING page={page}")
        if not competency_description.strip():
            issues.append(f"COMPETENCY_DESCRIPTION_MISSING page={page}")

    if memorization_code.strip() and rule.memorization_description_required and not memorization_description.strip():
        issues.append(f"MEMORIZATION_DESCRIPTION_MISSING page={page}")

    if arabic_code.strip() and rule.arabic_description_required and not arabic_description.strip():
        issues.append(f"ARABIC_DESCRIPTION_MISSING page={page}")

    return issues


def summarize_rules(rules: dict[int, PageRule]) -> Iterable[str]:
    for page in sorted(rules):
        rule = rules[page]
        lengths = "|".join(str(value) for value in sorted(rule.allowed_unit_lengths))
        yield f"{page:02d} {rule.page_role} lengths={lengths} injection={rule.special_injection}"
