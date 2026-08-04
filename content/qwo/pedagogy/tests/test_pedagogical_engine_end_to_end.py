#!/usr/bin/env python3
"""Regression tests for QURBATA pedagogical foundation V1."""
from content.qwo.pedagogy.runtime.jilid_series_validator import validate_jilid, validate_series

PREREQUISITES = {
    "C0001": set(),
    "C0002": {"C0001"},
    "C0005": {"C0002"},
    "C0028": {"C0012"},
}
SCOPES = {
    "C0001": {"LETTER"},
    "C0002": {"LETTER"},
    "C0005": {"WORD_FRAGMENT"},
    "C0028": {"WORD"},
}


def valid_pages():
    return [
        {"page": 1, "primary_competencies": ["C0001"], "review_competencies": [], "objects": [
            {"object_id": "L-BA-F", "object_type": "LETTER", "source_ref": "1:1:1", "competencies": ["C0001"]}
        ]},
        {"page": 2, "primary_competencies": ["C0002"], "review_competencies": ["C0001"], "objects": [
            {"object_id": "L-TA-F", "object_type": "LETTER", "source_ref": "2:2:1", "competencies": ["C0001", "C0002"]}
        ]},
        {"page": 3, "primary_competencies": ["C0005"], "review_competencies": ["C0001", "C0002"], "objects": [
            {"object_id": "F-BT-01", "object_type": "WORD_FRAGMENT", "source_ref": "2:3:1", "competencies": ["C0005"]}
        ]},
    ]


def test_valid_jilid_passes():
    assert validate_jilid(1, valid_pages(), PREREQUISITES, SCOPES) == []


def test_hamzah_leap_is_rejected():
    pages = valid_pages()
    pages[2]["objects"][0] = {"object_id": "BAD-HAMZAH", "object_type": "WORD", "source_ref": "2:4:1", "competencies": ["C0028"]}
    codes = {issue.code for issue in validate_jilid(1, pages, PREREQUISITES, SCOPES)}
    assert "COMPETENCY_LEAP" in codes


def test_missing_source_is_rejected():
    pages = valid_pages()
    pages[2]["objects"][0]["source_ref"] = ""
    codes = {issue.code for issue in validate_jilid(1, pages, PREREQUISITES, SCOPES)}
    assert "MISSING_QURAN_SOURCE" in codes


def test_duplicate_object_in_series_is_rejected():
    j1 = valid_pages()
    j2 = [{"page": 1, "primary_competencies": ["C0001"], "review_competencies": [], "objects": [
        {"object_id": "L-BA-F", "object_type": "LETTER", "source_ref": "3:1:1", "competencies": ["C0001"]}
    ]}]
    codes = {issue.code for issue in validate_series({1: j1, 2: j2}, PREREQUISITES, SCOPES)}
    assert "DUPLICATE_OBJECT_IN_SERIES" in codes


def test_scope_mismatch_is_rejected():
    pages = valid_pages()
    pages[0]["objects"][0]["object_type"] = "WORD"
    codes = {issue.code for issue in validate_jilid(1, pages, PREREQUISITES, SCOPES)}
    assert "OBJECT_SCOPE_MISMATCH" in codes
