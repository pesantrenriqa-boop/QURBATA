#!/usr/bin/env python3
"""Acceptance tests for QURBATA Pedagogical Unit Engine v1."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
ENGINE_PATH = ROOT / "content/qwo/pedagogy/runtime/pedagogical_unit_engine.py"


def load_engine():
    spec = importlib.util.spec_from_file_location("qurbata_pedagogical_unit_engine", ENGINE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("UNIT_ENGINE_IMPORT_FAILED")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    engine = load_engine()

    pass_units = ["بَ", "تِ", "نُ", "ءَ", "إِ", "ؤُ"]
    fail_units = ["ب", "بْ", "بّ", "بٌ", "آ", "ا", "بَٰ"]
    pass_fragments = ["بَتَ", "دَرَ", "تَنَ", "مِثُ"]
    fail_fragments = ["بَت", "بتَ", "بْتَ", "بَّتَ", "قَالَ", "آءَ"]

    failures: list[str] = []

    for text in pass_units:
        if not engine.is_short_vowel_unit(text):
            failures.append(f"EXPECTED_UNIT_PASS text={text}")

    for text in fail_units:
        if engine.is_short_vowel_unit(text):
            failures.append(f"EXPECTED_UNIT_FAIL text={text}")

    for text in pass_fragments:
        if not engine.is_short_vowel_fragment(text):
            failures.append(f"EXPECTED_FRAGMENT_PASS text={text}")

    for text in fail_fragments:
        if engine.is_short_vowel_fragment(text):
            failures.append(f"EXPECTED_FRAGMENT_FAIL text={text}")

    if not engine.has_nonconnector_transition("دَرَ"):
        failures.append("EXPECTED_NONCONNECTOR_PASS text=دَرَ")
    if engine.has_nonconnector_transition("بَتَ"):
        failures.append("EXPECTED_NONCONNECTOR_FAIL text=بَتَ")
    if not engine.has_connector_transition("بَتَ"):
        failures.append("EXPECTED_CONNECTOR_PASS text=بَتَ")

    print(f"PEDAGOGICAL_UNIT_TESTS={len(pass_units) + len(fail_units) + len(pass_fragments) + len(fail_fragments) + 3}")
    print(f"FAILURES={len(failures)}")
    for failure in failures:
        print(f"FAIL {failure}")

    if failures:
        print("PEDAGOGICAL_UNIT_ENGINE_V1=FAIL")
        return 1

    print("PEDAGOGICAL_UNIT_ENGINE_V1=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
