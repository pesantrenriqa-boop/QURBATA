#!/usr/bin/env python3
"""Regression gate for Jilid 1 40-page v5 layout YAML adapter."""
from __future__ import annotations

import argparse
from pathlib import Path
from collections import Counter
import yaml

ROOT = Path(__file__).resolve().parents[1]
SPECIAL_PAGES = {20, 40}


def load(path: Path):
    with path.open(encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"YAML_ROOT_INVALID {path}")
    return data


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", default="books/jilid-1/data-generated-v5-native")
    args = parser.parse_args()
    data_dir = Path(args.data_dir)
    data_dir = data_dir if data_dir.is_absolute() else ROOT / data_dir
    paths = sorted(data_dir.glob("page-*.yaml"))
    issues: list[str] = []
    if len(paths) != 40:
        issues.append(f"PAGE_COUNT expected=40 actual={len(paths)}")
    total_reading = 0
    total_names = 0
    page_kind_counts = Counter()
    for expected_page, path in enumerate(paths, 1):
        data = load(path)
        page = int(data.get("page", -1))
        if page != expected_page:
            issues.append(f"PAGE_SEQUENCE expected={expected_page} actual={page}")
        targets = data.get("targets", {})
        for key in ("competency_codes","competency_descriptions","memorization_code","memorization","arabic_code","arabic_language"):
            if not str(targets.get(key, "")).strip():
                issues.append(f"TARGET_MISSING page={page} field={key}")
        kind = data.get("page_kind")
        page_kind_counts[kind] += 1
        objects = data.get("objects", [])
        names = data.get("letter_names", [])
        if page in SPECIAL_PAGES:
            if kind != "LETTER_NAMES": issues.append(f"SPECIAL_KIND page={page}")
            if objects: issues.append(f"SPECIAL_READING_NOT_ZERO page={page}")
            if len(names) != 14: issues.append(f"SPECIAL_NAME_COUNT page={page} actual={len(names)}")
            total_names += len(names)
        else:
            if kind != "READING": issues.append(f"READING_KIND page={page}")
            if len(objects) != 24: issues.append(f"READING_COUNT page={page} actual={len(objects)}")
            if names: issues.append(f"READING_PAGE_HAS_NAMES page={page}")
            for item in objects:
                if item.get("render_mode") != "qae-native-short-vowel":
                    issues.append(f"RENDER_MODE page={page} slot={item.get('slot')}")
                if len(item.get("tokens", [])) != int(item.get("unit_length", 0)):
                    issues.append(f"TOKEN_UNIT_MISMATCH page={page} slot={item.get('slot')}")
            total_reading += len(objects)
    if total_reading != 912: issues.append(f"READING_TOTAL expected=912 actual={total_reading}")
    if total_names != 28: issues.append(f"LETTER_NAME_TOTAL expected=28 actual={total_names}")
    print(f"YAML_PAGES={len(paths)}")
    print(f"YAML_READING_OBJECTS={total_reading}")
    print(f"YAML_LETTER_NAMES={total_names}")
    print(f"YAML_READING_PAGES={page_kind_counts['READING']}")
    print(f"YAML_SPECIAL_PAGES={page_kind_counts['LETTER_NAMES']}")
    print(f"YAML_V2_ISSUES={len(issues)}")
    if issues:
        for issue in issues[:50]: print("ISSUE=" + issue)
        print("LAYOUT_YAML_V2_GATE=FAIL")
        return 1
    print("LAYOUT_YAML_V2_GATE=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
