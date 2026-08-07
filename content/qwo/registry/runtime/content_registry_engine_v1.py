#!/usr/bin/env python3
"""QURBATA Content Registry Engine v1.

Validates page-level instructional registries independently of the Composer.
This runtime intentionally allows UNASSIGNED targets in review-candidate mode,
but final-production validation rejects them.
"""
from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path

EXPECTED_PAGES = tuple(range(1, 41))
KNOWN_FOOTER_PROFILES = {"J1_STANDARD_V1"}
ALLOWED_INJECTIONS = {"LETTER_NAMES"}
FORBIDDEN_INJECTIONS = {"AWAIL_AL_SUWAR"}
REQUIRED_INJECTIONS = {20: "LETTER_NAMES", 40: "LETTER_NAMES"}


@dataclass(frozen=True)
class PageContent:
    page: int
    memorization_code: str
    memorization_description: str
    arabic_code: str
    arabic_description: str
    akhlaq_code: str
    akhlaq_description: str
    assessment_code: str
    assessment_description: str
    footer_profile: str
    status: str


@dataclass(frozen=True)
class Injection:
    page: int
    code: str
    injection_type: str
    source_registry: str
    required: bool
    description: str
    status: str


def _yes(value: str) -> bool:
    normalized = (value or "").strip().upper()
    if normalized not in {"YES", "NO"}:
        raise ValueError(f"BOOLEAN_FIELD_INVALID: {value!r}")
    return normalized == "YES"


def _rows(path: str | Path) -> list[dict[str, str]]:
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(path)
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def load_page_content(path: str | Path) -> dict[int, PageContent]:
    result: dict[int, PageContent] = {}
    for row in _rows(path):
        page = int(row["Page"])
        if page in result:
            raise ValueError(f"DUPLICATE_PAGE_CONTENT page={page}")
        result[page] = PageContent(
            page=page,
            memorization_code=row["MemorizationCode"].strip(),
            memorization_description=row["MemorizationDescription"].strip(),
            arabic_code=row["ArabicCode"].strip(),
            arabic_description=row["ArabicDescription"].strip(),
            akhlaq_code=row["AkhlaqCode"].strip(),
            akhlaq_description=row["AkhlaqDescription"].strip(),
            assessment_code=row["AssessmentCode"].strip(),
            assessment_description=row["AssessmentDescription"].strip(),
            footer_profile=row["FooterProfile"].strip(),
            status=row["Status"].strip(),
        )
    return result


def load_injections(path: str | Path) -> dict[int, Injection]:
    result: dict[int, Injection] = {}
    for row in _rows(path):
        page = int(row["Page"])
        if page in result:
            raise ValueError(f"DUPLICATE_INJECTION page={page}")
        result[page] = Injection(
            page=page,
            code=row["InjectionCode"].strip(),
            injection_type=row["InjectionType"].strip().upper(),
            source_registry=row["SourceRegistry"].strip(),
            required=_yes(row["Required"]),
            description=row["Description"].strip(),
            status=row["Status"].strip(),
        )
    return result


def validate_page_content(content: dict[int, PageContent], *, final: bool = False) -> list[str]:
    issues: list[str] = []
    pages = tuple(sorted(content))
    if pages != EXPECTED_PAGES:
        issues.append(f"PAGE_SEQUENCE_INVALID actual={pages} expected=1..40")

    target_fields = (
        ("MEMORIZATION", "memorization_code", "memorization_description"),
        ("ARABIC_LANGUAGE", "arabic_code", "arabic_description"),
        ("AKHLAQ", "akhlaq_code", "akhlaq_description"),
        ("ASSESSMENT", "assessment_code", "assessment_description"),
    )

    for page, row in sorted(content.items()):
        if row.footer_profile not in KNOWN_FOOTER_PROFILES:
            issues.append(f"UNKNOWN_FOOTER_PROFILE page={page} value={row.footer_profile}")
        for label, code_field, desc_field in target_fields:
            code = getattr(row, code_field).strip()
            desc = getattr(row, desc_field).strip()
            if not code:
                issues.append(f"{label}_CODE_MISSING page={page}")
                continue
            if not desc:
                issues.append(f"{label}_DESCRIPTION_MISSING page={page}")
            if final and code.upper() == "UNASSIGNED":
                issues.append(f"{label}_UNASSIGNED_FINAL page={page}")
            if code.upper() == "UNASSIGNED" and "belum ditetapkan" not in desc.lower():
                issues.append(f"{label}_UNASSIGNED_DESCRIPTION_NOT_EXPLICIT page={page}")
    return issues


def validate_injections(injections: dict[int, Injection]) -> list[str]:
    issues: list[str] = []
    for page, injection in sorted(injections.items()):
        if injection.injection_type in FORBIDDEN_INJECTIONS:
            issues.append(f"FORBIDDEN_INJECTION page={page} type={injection.injection_type}")
        if injection.injection_type not in ALLOWED_INJECTIONS:
            issues.append(f"UNKNOWN_INJECTION_TYPE page={page} type={injection.injection_type}")
        if not injection.code:
            issues.append(f"INJECTION_CODE_MISSING page={page}")
        if not injection.source_registry:
            issues.append(f"INJECTION_SOURCE_MISSING page={page}")
        if not injection.description:
            issues.append(f"INJECTION_DESCRIPTION_MISSING page={page}")

    for page, required_type in REQUIRED_INJECTIONS.items():
        injection = injections.get(page)
        if injection is None:
            issues.append(f"REQUIRED_INJECTION_MISSING page={page} expected={required_type}")
        elif injection.injection_type != required_type:
            issues.append(
                f"REQUIRED_INJECTION_MISMATCH page={page} expected={required_type} actual={injection.injection_type}"
            )

    unexpected_letter_name_pages = [
        page for page, injection in injections.items()
        if injection.injection_type == "LETTER_NAMES" and page not in REQUIRED_INJECTIONS
    ]
    for page in unexpected_letter_name_pages:
        issues.append(f"LETTER_NAMES_UNEXPECTED page={page}")
    return issues


def validate_letter_names(path: str | Path) -> list[str]:
    rows = _rows(path)
    issues: list[str] = []
    if len(rows) != 28:
        issues.append(f"LETTER_NAME_COUNT expected=28 actual={len(rows)}")
    sequences = [int(row["Sequence"]) for row in rows]
    if sequences != list(range(1, 29)):
        issues.append("LETTER_NAME_SEQUENCE_INVALID")
    canonical = [row["Letter"].strip() for row in rows]
    if len(canonical) != len(set(canonical)):
        issues.append("LETTER_NAME_DUPLICATE_LETTER")
    page20 = sum(row["TargetPage"].strip() == "20" for row in rows)
    page40 = sum(row["TargetPage"].strip() == "40" for row in rows)
    if page20 != 14:
        issues.append(f"PAGE20_LETTER_NAMES expected=14 actual={page20}")
    if page40 != 14:
        issues.append(f"PAGE40_LETTER_NAMES expected=14 actual={page40}")
    for row in rows:
        if not row["LetterNameArabic"].strip():
            issues.append(f"LETTER_NAME_ARABIC_MISSING sequence={row['Sequence']}")
    return issues
