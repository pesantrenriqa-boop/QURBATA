#!/usr/bin/env python3
"""Regression gate for QURBATA short-vowel typography profile v2."""
from __future__ import annotations

from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[4]
PROFILE = ROOT / "content/qwo/arabic-engine/anchors/jilid-1-short-vowels-native-v2.yaml"
EXPECTED = {"fathah": "َ", "kasrah": "ِ", "dhammah": "ُ"}


def main() -> int:
    if not PROFILE.is_file():
        print(f"QAE_PROFILE_MISSING={PROFILE}")
        print("QAE_TYPOGRAPHY_GATE_V2=FAIL")
        return 1

    data = yaml.safe_load(PROFILE.read_text(encoding="utf-8"))
    issues: list[str] = []

    if data.get("engine") != "QAE":
        issues.append("ENGINE_NOT_QAE")
    if data.get("strategy", {}).get("primary_renderer") != "font-combining-mark":
        issues.append("PRIMARY_RENDERER_NOT_NATIVE")

    marks = data.get("marks", {})
    for name, char in EXPECTED.items():
        mark = marks.get(name)
        if not isinstance(mark, dict):
            issues.append(f"MARK_MISSING={name}")
            continue
        if mark.get("unicode") != char:
            issues.append(f"UNICODE_MISMATCH={name}")
        if mark.get("renderer") != "font-combining-mark":
            issues.append(f"RENDERER_MISMATCH={name}")
        if float(mark.get("scale", 0)) <= 0:
            issues.append(f"INVALID_SCALE={name}")

    fallback = data.get("fallback_svg", {})
    for name in EXPECTED:
        mark = fallback.get(name, {})
        stroke = float(mark.get("stroke_width", 999))
        if stroke > 3.0:
            issues.append(f"FALLBACK_STROKE_TOO_HEAVY={name}:{stroke}")

    qa = data.get("visual_qa", {})
    required_qa = (
        "require_distinct_fathah_kasrah",
        "require_non_dot_like_short_vowels",
        "require_dhammah_loop_identity",
        "require_no_base_collision",
        "require_font_ready",
    )
    for field in required_qa:
        if qa.get(field) is not True:
            issues.append(f"VISUAL_QA_REQUIREMENT_MISSING={field}")

    print(f"QAE_PROFILE={data.get('profile', '')}")
    print(f"QAE_PRIMARY_RENDERER={data.get('strategy', {}).get('primary_renderer', '')}")
    print(f"QAE_MARKS={len(marks)}")
    print(f"QAE_TYPOGRAPHY_ISSUES={len(issues)}")
    if issues:
        for issue in issues:
            print("ISSUE=" + issue)
        print("QAE_TYPOGRAPHY_GATE_V2=FAIL")
        return 1
    print("QAE_TYPOGRAPHY_GATE_V2=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
