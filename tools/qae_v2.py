#!/usr/bin/env python3
"""QURBATA Arabic Engine v2: render fathah, kasrah, and dhammah independently."""
from __future__ import annotations

import importlib.util
import sys
from copy import deepcopy
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
PUE_PATH = ROOT / "content/qwo/pedagogy/runtime/pedagogical_unit_engine.py"
MARK_NAMES = {"َ": "fathah", "ِ": "kasrah", "ُ": "dhammah"}


def load_pue():
    spec = importlib.util.spec_from_file_location("qurbata_pue", PUE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("PUE_IMPORT_FAILED")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


PUE = load_pue()


def load_qae_profile(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise FileNotFoundError(f"QAE_PROFILE_NOT_FOUND: {path}")
    with path.open(encoding="utf-8") as handle:
        profile = yaml.safe_load(handle)
    if not isinstance(profile, dict) or profile.get("engine") != "QAE":
        raise ValueError("QAE_PROFILE_INVALID")
    marks = profile.get("marks")
    anchors = profile.get("anchors")
    if not isinstance(marks, dict) or not isinstance(anchors, dict):
        raise ValueError("QAE_MULTI_MARK_PROFILE_REQUIRED")
    for name in MARK_NAMES.values():
        mark = marks.get(name)
        if not isinstance(mark, dict) or mark.get("renderer") != "inline-svg-path":
            raise ValueError(f"QAE_MARK_PROFILE_INVALID: {name}")
        for key in ("unicode", "view_box", "path_d", "stroke_width", "width_em", "height_em", "color"):
            if key not in mark:
                raise ValueError(f"QAE_MARK_FIELD_MISSING: {name}.{key}")
    return profile


def split_token(token: str) -> tuple[str, str]:
    units = PUE.grapheme_units(token)
    if len(units) != 1:
        raise ValueError(f"QAE_TOKEN_MUST_HAVE_ONE_UNIT: {token!r}")
    decision = PUE.validate_short_vowel_unit(units[0])
    if not decision.passed:
        raise ValueError(
            f"QAE_EXACTLY_ONE_SHORT_VOWEL_REQUIRED: {token!r} reasons={decision.reasons}"
        )
    return decision.base, decision.marks[0]


def render_token(token: str, profile: dict[str, Any]) -> dict[str, Any]:
    base, mark_char = split_token(token)
    mark_name = MARK_NAMES[mark_char]
    mark = profile["marks"][mark_name]
    base_anchors = profile["anchors"].get(base, {})
    default_anchors = profile["anchors"].get("default", {})
    anchor = base_anchors.get(mark_name, default_anchors.get(mark_name))
    if not isinstance(anchor, dict):
        raise ValueError(f"QAE_ANCHOR_MISSING base={base!r} mark={mark_name}")
    for key in ("x_em", "y_em", "scale"):
        if key not in anchor:
            raise ValueError(f"QAE_ANCHOR_INCOMPLETE base={base!r} mark={mark_name} key={key}")
    return {
        "source": token,
        "base": base,
        "mark": mark_name,
        "svg": {
            "view_box": str(mark["view_box"]),
            "path_d": str(mark["path_d"]),
            "stroke_width": float(mark["stroke_width"]),
            "color": str(mark["color"]),
        },
        "style": (
            f"--qae-x:{float(anchor['x_em'])}em;"
            f"--qae-y:{float(anchor['y_em'])}em;"
            f"--qae-scale:{float(anchor['scale'])};"
            f"--qae-mark-width:{float(mark['width_em'])}em;"
            f"--qae-mark-height:{float(mark['height_em'])}em;"
            f"--qae-mark-rotation:{float(mark.get('rotation_deg', 0))}deg;"
        ),
    }


def enrich_page(page: dict[str, Any], profile: dict[str, Any]) -> dict[str, Any]:
    enriched = deepcopy(page)
    rendered_objects: list[dict[str, Any]] = []
    for item in page.get("objects", []):
        rendered = deepcopy(item)
        if item.get("render_mode") == "qae-short-vowel":
            rendered["qae_tokens"] = [render_token(token, profile) for token in item["tokens"]]
        elif item.get("render_mode") == "raw-quran":
            rendered["qae_tokens"] = []
        else:
            raise ValueError(f"QAE_UNKNOWN_RENDER_MODE: {item.get('render_mode')}")
        rendered_objects.append(rendered)
    enriched["objects"] = rendered_objects
    enriched["qae"] = {"profile": profile.get("profile")}
    return enriched
