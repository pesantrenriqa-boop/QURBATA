#!/usr/bin/env python3
"""Regression gate for QURBATA Jilid 1 Learning Progression Engine v1."""
from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
ENGINE_PATH = ROOT / "content/qwo/lpe/runtime/lpe_engine_v1.py"
DEFAULT_BLUEPRINT = ROOT / "content/qwo/lpe/JILID-1-40-PAGE-PROGRESSION-V2.csv"


def load_engine():
    spec = importlib.util.spec_from_file_location("qurbata_lpe_engine_v1", ENGINE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("LPE_ENGINE_IMPORT_FAILED")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--blueprint", default=str(DEFAULT_BLUEPRINT.relative_to(ROOT)))
    args = parser.parse_args()

    path = Path(args.blueprint)
    path = path if path.is_absolute() else ROOT / path
    engine = load_engine()

    try:
        rules = engine.load_progression(path)
    except (FileNotFoundError, ValueError) as exc:
        print(f"LPE_LOAD_FAIL={exc}")
        return 2

    issues = engine.validate_blueprint(rules)

    # Positive acceptance checks.
    checks: list[tuple[str, list[str]]] = [
        ("PAGE1_SINGLE", engine.validate_page_object(page=1, object_type="LETTER", unit_length=1, rules=rules)),
        ("PAGE5_DOUBLE", engine.validate_page_object(page=5, object_type="WORD_FRAGMENT", unit_length=2, rules=rules)),
        ("PAGE13_TRIPLE", engine.validate_page_object(page=13, object_type="WORD_FRAGMENT", unit_length=3, rules=rules)),
        ("META_COMPLETE", engine.validate_metadata(
            page=1,
            competency_code="C0002",
            competency_description="Membaca huruf tunggal berharakat fathah",
            memorization_code="HIFZ-J1-001",
            memorization_description="Target hafalan terdaftar",
            arabic_code="ARB-J1-001",
            arabic_description="Target Bahasa Arab terdaftar",
            rules=rules,
        )),
    ]
    for name, result in checks:
        if result:
            issues.append(f"POSITIVE_CHECK_FAILED {name} reasons={result}")

    # Negative regression checks must be rejected by the engine.
    negative_checks = {
        "TRIPLE_TOO_EARLY": engine.validate_page_object(page=5, object_type="WORD_FRAGMENT", unit_length=3, rules=rules),
        "AWAIL_FORBIDDEN": engine.validate_page_object(page=20, object_type="AWAIL_AL_SUWAR", unit_length=None, rules=rules),
        "MISSING_COMPETENCY_DESCRIPTION": engine.validate_metadata(
            page=1,
            competency_code="C0002",
            competency_description="",
            rules=rules,
        ),
        "MISSING_MEMORIZATION_DESCRIPTION": engine.validate_metadata(
            page=1,
            competency_code="C0002",
            competency_description="Valid",
            memorization_code="HIFZ-J1-001",
            memorization_description="",
            rules=rules,
        ),
        "MISSING_ARABIC_DESCRIPTION": engine.validate_metadata(
            page=1,
            competency_code="C0002",
            competency_description="Valid",
            arabic_code="ARB-J1-001",
            arabic_description="",
            rules=rules,
        ),
    }
    for name, result in negative_checks.items():
        if not result:
            issues.append(f"NEGATIVE_CHECK_NOT_REJECTED {name}")

    print(f"LPE_PAGES={len(rules)}")
    print(f"LPE_BLUEPRINT_ISSUES={len(issues)}")
    print("PAGE20_INJECTION=" + rules[20].special_injection)
    print("PAGE40_INJECTION=" + rules[40].special_injection)
    print("AWAILUS_SUWAR_ALLOWED=" + ("YES" if any(r.awailus_suwar_allowed for r in rules.values()) else "NO"))

    if issues:
        for issue in issues:
            print("FAIL:", issue)
        print("LPE_REGRESSION_GATE_V1=FAIL")
        return 3

    print("LPE_REGRESSION_GATE_V1=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
