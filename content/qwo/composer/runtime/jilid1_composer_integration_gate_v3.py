#!/usr/bin/env python3
"""Regression gate for Jilid 1 Composer v5 GLE + CRE integration."""
from __future__ import annotations

import argparse
import csv
import importlib.util
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
GLE_PATH = ROOT / "content/qwo/lpe/runtime/grapheme_learning_engine_v1.py"
GLE_REGISTRY = ROOT / "content/qwo/lpe/JILID-1-GRAPHEME-FAMILY-REGISTRY-V1.csv"
DEFAULT_DIR = ROOT / "content/qwo/composer/output/jilid-1-v5-integrated"
CRE_PAGE_REGISTRY = ROOT / "content/qwo/registry/JILID-1-PAGE-CONTENT-REGISTRY-V2.csv"
SPECIAL_PAGES = {20, 40}


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"MODULE_IMPORT_FAILED: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


GLE = load_module(GLE_PATH, "qurbata_gle_v1_gate_v3")


def rows(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        raise FileNotFoundError(path)
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def first_base(text: str) -> str:
    # Enough for the v5 canonical early-letter surface: first Arabic base codepoint.
    for ch in text:
        if "\u0621" <= ch <= "\u064a" or ch == "\u0671":
            return ch
    return ""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default=str(DEFAULT_DIR.relative_to(ROOT)))
    args = parser.parse_args()
    output_dir = Path(args.output_dir)
    output_dir = output_dir if output_dir.is_absolute() else ROOT / output_dir

    reading = rows(output_dir / "JILID-1-READING-OBJECTS-V5.csv")
    metadata = rows(output_dir / "JILID-1-PAGE-METADATA-V5.csv")
    injections = rows(output_dir / "JILID-1-INJECTION-CONTENT-V5.csv")
    cre = rows(CRE_PAGE_REGISTRY)
    cre_by_page = {int(row["Page"]): row for row in cre}
    issues: list[str] = []

    grouped: dict[int, list[dict[str, str]]] = defaultdict(list)
    for row in reading:
        grouped[int(row["Page"])].append(row)

    if len(reading) != 912:
        issues.append(f"READING_ROWS expected=912 actual={len(reading)}")
    if sorted(grouped) != [page for page in range(1, 41) if page not in SPECIAL_PAGES]:
        issues.append("READING_PAGE_SET_INVALID")
    for page, page_rows in grouped.items():
        if len(page_rows) != 24:
            issues.append(f"PAGE_OBJECT_COUNT page={page} actual={len(page_rows)}")
        if len({row["ArabicObject"] for row in page_rows}) != len(page_rows):
            issues.append(f"DUPLICATE_WITHIN_PAGE page={page}")

    if len(metadata) != 40:
        issues.append(f"METADATA_COUNT expected=40 actual={len(metadata)}")
    meta_by_page = {int(row["Page"]): row for row in metadata}
    if set(meta_by_page) != set(range(1, 41)):
        issues.append("METADATA_PAGE_SET_INVALID")

    for page in range(1, 41):
        meta = meta_by_page.get(page)
        cre_row = cre_by_page.get(page)
        if not meta or not cre_row:
            continue
        for field in (
            "MemorizationCode", "MemorizationDescription", "MemorizationStage",
            "ArabicCode", "ArabicDescription", "AkhlaqCode", "AkhlaqDescription",
            "AssessmentCode", "AssessmentDescription", "FooterProfile",
        ):
            if meta.get(field, "").strip() != cre_row.get(field, "").strip():
                issues.append(f"CRE_METADATA_MISMATCH page={page} field={field}")
        if page in SPECIAL_PAGES:
            if meta.get("SpecialInjection") != "LETTER_NAMES":
                issues.append(f"SPECIAL_INJECTION_MISSING page={page}")
            if meta.get("CompetencyCodes") != "LETTER_NAMES":
                issues.append(f"LETTER_NAME_COMPETENCY_MISSING page={page}")
        else:
            if not meta.get("CompetencyCodes", "").strip() or not meta.get("CompetencyDescriptions", "").strip():
                issues.append(f"COMPETENCY_METADATA_MISSING page={page}")

    page_counts = Counter(int(row["Page"]) for row in injections)
    if page_counts != Counter({20: 14, 40: 14}):
        issues.append(f"LETTER_NAME_DISTRIBUTION actual={dict(page_counts)}")

    # GLE gate: first introduction of each available L1 base must follow family order.
    families = GLE.load_registry(GLE_REGISTRY)
    gle_issues = GLE.validate_registry(families)
    issues.extend("GLE_" + issue for issue in gle_issues)
    rank = GLE.build_letter_rank(families)
    first_seen_bases: list[str] = []
    seen_bases: set[str] = set()
    for row in sorted(reading, key=lambda r: (int(r["Page"]), int(r["Slot"]))):
        if row["UnitLength"] != "1" or row["LearningState"].upper() != "NEW":
            continue
        base = first_base(row["ArabicObject"])
        if base and base not in seen_bases:
            seen_bases.add(base); first_seen_bases.append(base)
    expected_bases = sorted(first_seen_bases, key=lambda letter: rank.get(letter, (999, 999)))
    if first_seen_bases != expected_bases:
        issues.append("GLE_INTRODUCTION_ORDER_INVALID actual=" + "".join(first_seen_bases))

    print(f"V5_READING_ROWS={len(reading)}")
    print(f"V5_READING_PAGES={len(grouped)}")
    print(f"V5_METADATA_PAGES={len(metadata)}")
    print(f"V5_LETTER_NAME_ROWS={len(injections)}")
    print("V5_GLE_FIRST_BASE_ORDER=" + "".join(first_seen_bases))
    print(f"V5_INTEGRATION_ISSUES={len(issues)}")
    if issues:
        for issue in issues[:50]:
            print("ISSUE=" + issue)
        print("JILID1_COMPOSER_INTEGRATION_GATE_V3=FAIL")
        return 1
    print("PAGE20_READING_OBJECTS=0")
    print("PAGE40_READING_OBJECTS=0")
    print("AWAILUS_SUWAR=0")
    print("JILID1_COMPOSER_INTEGRATION_GATE_V3=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
