#!/usr/bin/env python3
"""Regression gate for QURBATA Content Registry Engine v1."""
from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
ENGINE_PATH = ROOT / "content/qwo/registry/runtime/content_registry_engine_v1.py"
DEFAULT_PAGE_CONTENT = ROOT / "content/qwo/registry/JILID-1-PAGE-CONTENT-REGISTRY-V1.csv"
DEFAULT_INJECTIONS = ROOT / "content/qwo/registry/JILID-1-INJECTION-REGISTRY-V1.csv"
DEFAULT_LETTER_NAMES = ROOT / "content/qwo/lpe/JILID-1-LETTER-NAME-REGISTRY-V1.csv"


def load_engine():
    spec = importlib.util.spec_from_file_location("qurbata_cre_v1", ENGINE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("CRE_IMPORT_FAILED")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def resolve(value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else ROOT / path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--page-content", default=str(DEFAULT_PAGE_CONTENT.relative_to(ROOT)))
    parser.add_argument("--injections", default=str(DEFAULT_INJECTIONS.relative_to(ROOT)))
    parser.add_argument("--letter-names", default=str(DEFAULT_LETTER_NAMES.relative_to(ROOT)))
    parser.add_argument("--final", action="store_true", help="Reject every UNASSIGNED instructional target")
    args = parser.parse_args()

    engine = load_engine()
    page_content = engine.load_page_content(resolve(args.page_content))
    injections = engine.load_injections(resolve(args.injections))

    issues: list[str] = []
    issues.extend(engine.validate_page_content(page_content, final=args.final))
    issues.extend(engine.validate_injections(injections))
    issues.extend(engine.validate_letter_names(resolve(args.letter_names)))

    unassigned = 0
    for row in page_content.values():
        unassigned += sum(
            value.upper() == "UNASSIGNED"
            for value in (
                row.memorization_code,
                row.arabic_code,
                row.akhlaq_code,
                row.assessment_code,
            )
        )

    print(f"CRE_PAGES={len(page_content)}")
    print(f"CRE_INJECTIONS={len(injections)}")
    print(f"CRE_UNASSIGNED_TARGETS={unassigned}")
    print("PAGE20_INJECTION=" + (injections.get(20).injection_type if 20 in injections else "MISSING"))
    print("PAGE40_INJECTION=" + (injections.get(40).injection_type if 40 in injections else "MISSING"))
    print(f"CRE_REGISTRY_ISSUES={len(issues)}")

    if issues:
        for issue in issues[:50]:
            print("ISSUE=" + issue)
        print("CRE_REGRESSION_GATE_V1=FAIL")
        return 1

    print("CRE_MODE=" + ("FINAL" if args.final else "REVIEW_CANDIDATE"))
    print("CRE_REGRESSION_GATE_V1=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
