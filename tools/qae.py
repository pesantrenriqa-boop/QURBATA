#!/usr/bin/env python3
"""QURBATA Arabic Engine v1: independent educational harakat rendering."""
from __future__ import annotations

import unicodedata
from copy import deepcopy
from pathlib import Path
from typing import Any

import yaml

FATHA = "َ"


def load_qae_profile(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise FileNotFoundError(f"QAE_PROFILE_NOT_FOUND: {path}")
    with path.open(encoding="utf-8") as handle:
        profile = yaml.safe_load(handle)
    if not isinstance(profile, dict):
        raise ValueError("QAE_PROFILE_ROOT_MUST_BE_MAPPING")
    if profile.get("engine") != "QAE":
        raise ValueError("QAE_PROFILE_ENGINE_INVALID")
    if not isinstance(profile.get("anchors"), dict):
        raise ValueError("QAE_ANCHORS_MISSING")
    return profile


def split_token(token: str) -> tuple[str, list[str]]:
    normalized = unicodedata.normalize("NFD", token)
    bases = [char for char in normalized if unicodedata.category(char).startswith("L")]
    marks = [char for char in normalized if unicodedata.category(char).startswith("M")]
    if len(bases) != 1:
        raise ValueError(f"QAE_TOKEN_MUST_HAVE_ONE_BASE: {token!r}")
    return bases[0], marks


def render_token(token: str, profile: dict[str, Any]) -> dict[str, Any]:
    base, marks = split_token(token)
    unsupported = [mark for mark in marks if mark != FATHA]
    if unsupported:
        raise ValueError(f"QAE_UNSUPPORTED_MARKS token={token!r} marks={unsupported}")
    if FATHA not in marks:
        raise ValueError(f"QAE_FATHA_REQUIRED token={token!r}")

    anchor = profile["anchors"].get(base, profile.get("default_anchor", {}))
    mark = profile.get("mark", {})
    required_anchor = ("x_em", "y_em", "scale")
    if any(key not in anchor for key in required_anchor):
        raise ValueError(f"QAE_ANCHOR_INCOMPLETE base={base!r}")

    return {
        "source": token,
        "base": base,
        "mark": "fathah",
        "style": (
            f"--qae-x:{float(anchor['x_em'])}em;"
            f"--qae-y:{float(anchor['y_em'])}em;"
            f"--qae-scale:{float(anchor['scale'])};"
            f"--qae-mark-width:{float(mark.get('width_em', 0.42))}em;"
            f"--qae-mark-height:{float(mark.get('height_em', 0.075))}em;"
            f"--qae-mark-rotation:{float(mark.get('rotation_deg', -12))}deg;"
            f"--qae-mark-color:{mark.get('color', '#000000')};"
        ),
    }


def enrich_page(page: dict[str, Any], profile: dict[str, Any]) -> dict[str, Any]:
    enriched = deepcopy(page)
    enriched["qae"] = {
        "profile": profile.get("profile"),
        "material_title": [render_token(token, profile) for token in page["material_title"]],
        "singles": [render_token(token, profile) for token in page["objects"]["singles"]],
        "pairs": [
            [render_token(token, profile) for token in item]
            for item in page["objects"]["pairs"]
        ],
        "triples": [
            [render_token(token, profile) for token in item]
            for item in page["objects"]["triples"]
        ],
    }
    return enriched
