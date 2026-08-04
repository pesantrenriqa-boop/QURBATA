#!/usr/bin/env python3
"""QURBATA jilid/series validator V1.

Validates page order, competency dependencies, object scope, Quran source trace,
and global no-repeat policy before any page can be promoted.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Mapping, Sequence

VALID_OBJECT_TYPES = {"LETTER", "WORD_FRAGMENT", "WORD", "PHRASE", "AYAH_FRAGMENT", "FULL_AYAH", "EVALUATION", "HAFALAN", "ARABIC"}

@dataclass(frozen=True)
class ValidationIssue:
    code: str
    message: str
    jilid: int | None = None
    page: int | None = None
    object_id: str | None = None


def validate_jilid(
    jilid_number: int,
    pages: Sequence[Mapping[str, object]],
    competency_prerequisites: Mapping[str, set[str]],
    object_type_by_competency: Mapping[str, set[str]],
) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    introduced: set[str] = set()
    seen_pages: set[int] = set()
    seen_objects: set[str] = set()

    for page in pages:
        page_no = int(page["page"])
        if page_no in seen_pages:
            issues.append(ValidationIssue("DUPLICATE_PAGE", "Nomor halaman terulang", jilid_number, page_no))
        seen_pages.add(page_no)

        primary = set(page.get("primary_competencies", []))
        review = set(page.get("review_competencies", []))
        allowed = introduced | primary | review

        for competency in primary:
            missing = competency_prerequisites.get(competency, set()) - introduced
            if missing:
                issues.append(ValidationIssue("MISSING_PREREQUISITE", f"{competency} belum memenuhi {sorted(missing)}", jilid_number, page_no))

        for obj in page.get("objects", []):
            object_id = str(obj.get("object_id", ""))
            object_type = str(obj.get("object_type", ""))
            source_ref = str(obj.get("source_ref", ""))
            competencies = set(obj.get("competencies", []))

            if not object_id:
                issues.append(ValidationIssue("MISSING_OBJECT_ID", "ObjectID kosong", jilid_number, page_no))
            elif object_id in seen_objects:
                issues.append(ValidationIssue("DUPLICATE_OBJECT_IN_JILID", "Objek utama terulang dalam jilid", jilid_number, page_no, object_id))
            seen_objects.add(object_id)

            if object_type not in VALID_OBJECT_TYPES:
                issues.append(ValidationIssue("INVALID_OBJECT_TYPE", object_type, jilid_number, page_no, object_id))
            if object_type not in {"EVALUATION", "HAFALAN", "ARABIC"} and not source_ref:
                issues.append(ValidationIssue("MISSING_QURAN_SOURCE", "Objek baca tanpa SourceRef", jilid_number, page_no, object_id))
            if competencies - allowed:
                issues.append(ValidationIssue("COMPETENCY_LEAP", f"Kompetensi melompat: {sorted(competencies - allowed)}", jilid_number, page_no, object_id))

            for competency in competencies:
                expected_types = object_type_by_competency.get(competency, set())
                if expected_types and object_type not in expected_types:
                    issues.append(ValidationIssue("OBJECT_SCOPE_MISMATCH", f"{competency} tidak menerima {object_type}", jilid_number, page_no, object_id))

        introduced |= primary

    return issues


def validate_series(
    jilids: Mapping[int, Sequence[Mapping[str, object]]],
    competency_prerequisites: Mapping[str, set[str]],
    object_type_by_competency: Mapping[str, set[str]],
) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    global_seen: dict[str, tuple[int, int]] = {}

    for jilid_number in sorted(jilids):
        pages = jilids[jilid_number]
        issues.extend(validate_jilid(jilid_number, pages, competency_prerequisites, object_type_by_competency))
        for page in pages:
            page_no = int(page["page"])
            for obj in page.get("objects", []):
                object_id = str(obj.get("object_id", ""))
                if not object_id:
                    continue
                if object_id in global_seen:
                    first_jilid, first_page = global_seen[object_id]
                    issues.append(ValidationIssue("DUPLICATE_OBJECT_IN_SERIES", f"Pertama dipakai J{first_jilid} H{first_page}", jilid_number, page_no, object_id))
                else:
                    global_seen[object_id] = (jilid_number, page_no)

    return issues


def can_promote(issues: Iterable[ValidationIssue]) -> bool:
    return not any(True for _ in issues)
