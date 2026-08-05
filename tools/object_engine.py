#!/usr/bin/env python3
"""Canonical learning-object and competency validation for QURBATA pages."""
from __future__ import annotations

import unicodedata
from copy import deepcopy
from pathlib import Path
from typing import Any

import yaml

FATHA = "َ"
MARK_NAMES = {
    "َ": "fathah",
    "ِ": "kasrah",
    "ُ": "dhammah",
    "ْ": "sukun",
    "ّ": "shaddah",
    "ً": "fathatan",
    "ٍ": "kasratan",
    "ٌ": "dhammatan",
    "ٰ": "dagger_alif",
}


def load_competency(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise FileNotFoundError(f"COMPETENCY_FILE_NOT_FOUND: {path}")
    with path.open(encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError("COMPETENCY_ROOT_MUST_BE_MAPPING")
    for key in ("id", "allowed", "distribution", "material_title"):
        if key not in data:
            raise ValueError(f"COMPETENCY_FIELD_MISSING: {key}")
    return data


def split_token(token: str) -> tuple[str, list[str]]:
    normalized = unicodedata.normalize("NFD", token)
    bases = [char for char in normalized if unicodedata.category(char).startswith("L")]
    marks = [char for char in normalized if unicodedata.category(char).startswith("M")]
    if len(bases) != 1:
        raise ValueError(f"TOKEN_MUST_HAVE_ONE_BASE_LETTER: {token!r}")
    return bases[0], marks


def canonicalize_objects(page: dict[str, Any]) -> dict[str, Any]:
    """Create stable object IDs while preserving grouped data for the renderer."""
    canonical: list[dict[str, Any]] = []
    groups = page.get("objects")
    if not isinstance(groups, dict):
        raise ValueError("PAGE_OBJECTS_MUST_BE_MAPPING")

    definitions = (("single", "singles", 1), ("pair", "pairs", 2), ("triple", "triples", 3))
    for kind, group_key, expected_count in definitions:
        items = groups.get(group_key)
        if not isinstance(items, list):
            raise ValueError(f"OBJECT_GROUP_MUST_BE_LIST: {group_key}")
        for index, raw in enumerate(items, start=1):
            tokens = [raw] if kind == "single" else raw
            if not isinstance(tokens, list) or len(tokens) != expected_count:
                raise ValueError(f"OBJECT_TOKEN_COUNT_INVALID kind={kind} index={index}")
            if any(not isinstance(token, str) or not token for token in tokens):
                raise ValueError(f"OBJECT_TOKEN_INVALID kind={kind} index={index}")
            canonical.append({
                "id": f"P{int(page['page']):03d}-{kind.upper()}-{index:02d}",
                "type": kind,
                "tokens": tokens,
                "token_count": len(tokens),
                "connected": False,
            })

    enriched = deepcopy(page)
    enriched["learning_objects"] = canonical
    return enriched


def validate_competency(page: dict[str, Any], competency: dict[str, Any]) -> None:
    allowed = competency["allowed"]
    allowed_letters = set(allowed.get("base_letters", []))
    allowed_marks = set(allowed.get("marks", []))
    expected_counts = allowed.get("token_count_per_object", {})
    expected_distribution = competency["distribution"]

    if page.get("material_title") != competency["material_title"].get("tokens"):
        raise ValueError("MATERIAL_TITLE_DOES_NOT_MATCH_COMPETENCY")

    objects = page.get("learning_objects", [])
    ids = [obj.get("id") for obj in objects]
    if len(ids) != len(set(ids)):
        raise ValueError("LEARNING_OBJECT_IDS_NOT_UNIQUE")

    actual_distribution = {"single": 0, "pair": 0, "triple": 0}
    for obj in objects:
        kind = obj.get("type")
        if kind not in actual_distribution:
            raise ValueError(f"LEARNING_OBJECT_TYPE_INVALID: {kind}")
        actual_distribution[kind] += 1
        tokens = obj.get("tokens", [])
        if len(tokens) != int(expected_counts[kind]):
            raise ValueError(f"LEARNING_OBJECT_TOKEN_COUNT_OUT_OF_SCOPE id={obj.get('id')}")
        if obj.get("connected") is not False:
            raise ValueError(f"CONNECTED_OBJECT_FORBIDDEN id={obj.get('id')}")

        for token in tokens:
            base, marks = split_token(token)
            if base not in allowed_letters:
                raise ValueError(f"BASE_LETTER_OUT_OF_COMPETENCY token={token!r}")
            mark_names = {MARK_NAMES.get(mark, f"unicode-{ord(mark):04X}") for mark in marks}
            if not mark_names or not mark_names.issubset(allowed_marks):
                raise ValueError(f"MARK_OUT_OF_COMPETENCY token={token!r} marks={sorted(mark_names)}")
            if "fathah" in allowed_marks and marks != [FATHA]:
                raise ValueError(f"TOKEN_MUST_HAVE_EXACTLY_ONE_FATHAH token={token!r}")

    for kind, expected in expected_distribution.items():
        if actual_distribution.get(kind) != int(expected):
            raise ValueError(
                f"OBJECT_DISTRIBUTION_DOES_NOT_MATCH_COMPETENCY kind={kind} "
                f"actual={actual_distribution.get(kind)} expected={expected}"
            )


def prepare_page(page: dict[str, Any], competency: dict[str, Any]) -> dict[str, Any]:
    enriched = canonicalize_objects(page)
    validate_competency(enriched, competency)
    enriched["competency"] = {
        "id": competency["id"],
        "status": competency.get("status"),
    }
    return enriched
