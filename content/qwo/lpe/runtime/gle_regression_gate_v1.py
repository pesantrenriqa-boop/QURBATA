#!/usr/bin/env python3
"""Regression gate for QURBATA Graphical Learning Engine v1."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
ENGINE_PATH = ROOT / "content/qwo/lpe/runtime/grapheme_learning_engine_v1.py"


def load_engine():
    spec = importlib.util.spec_from_file_location("qurbata_gle_v1", ENGINE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("GLE_IMPORT_FAILED")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    engine = load_engine()
    families = engine.load_registry()
    issues = engine.validate_registry(families)
    rank = engine.build_letter_rank(families)

    print(f"GLE_FAMILIES={len(families)}")
    print(f"GLE_CANONICAL_LETTERS={len(rank)}")
    print(f"GLE_REGISTRY_ISSUES={len(issues)}")
    print("GLE_ORDER=" + " ".join(letter for family in families for letter in family.letters))

    if issues:
        for issue in issues:
            print("ISSUE=" + issue)
        print("GLE_REGRESSION_GATE_V1=FAIL")
        return 1

    print("GLE_REGRESSION_GATE_V1=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
