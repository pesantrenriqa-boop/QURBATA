#!/usr/bin/env python3
"""Executable validation for the QURBATA pedagogical foundation.

The suite uses only Python's standard library. It fails closed: incomplete
coverage, missing files, dependency errors, or known pedagogical regressions
must block page generation.
"""

from __future__ import annotations

import argparse
import csv
import importlib.util
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DEPENDENCY_MAP = ROOT / "content/qwo/competency/QURBATA-COMPETENCY-DEPENDENCY-MAP-V1.csv"
POLICY_MATRIX = ROOT / "content/qwo/pedagogy/PEDAGOGICAL-POLICY-MATRIX-V2.csv"
RULE_MATRIX = ROOT / "content/qwo/pedagogy/PEDAGOGICAL-RULE-MATRIX-V1.csv"
ENGINE_FILE = ROOT / "content/qwo/pedagogy/runtime/pedagogical_engine.py"

HAMZAH_FORMS = set("ءأإؤئآ")
TANWIN = set("ًٌٍ")
SUKUN = "ْ"
SHADDA = "ّ"
FATHA = "َ"
DAMMA = "ُ"
KASRA = "ِ"


def fail(message: str) -> None:
    raise AssertionError(message)


def load_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        fail(f"Required file missing: {path}")
    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        fail(f"CSV has no data rows: {path}")
    return rows


def ordered_ids(rows: list[dict[str, str]]) -> list[str]:
    return [row["CompetencyID"].strip() for row in rows]


def validate_dependency_map() -> list[str]:
    rows = load_rows(DEPENDENCY_MAP)
    ids = ordered_ids(rows)
    if len(ids) != len(set(ids)):
        fail("Duplicate CompetencyID found")
    expected = [f"C{i:04d}" for i in range(1, 42)]
    if ids != expected:
        fail("Dependency map must contain ordered C0001-C0041")

    graph: dict[str, set[str]] = {}
    for row in rows:
        cid = row["CompetencyID"].strip()
        deps = {x.strip() for x in row.get("PrerequisiteIDs", "").split("|") if x.strip()}
        missing = deps - set(ids)
        if missing:
            fail(f"{cid} references missing prerequisites: {sorted(missing)}")
        graph[cid] = deps

    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> None:
        if node in visiting:
            fail(f"Dependency cycle detected at {node}")
        if node in visited:
            return
        visiting.add(node)
        for dep in graph[node]:
            visit(dep)
        visiting.remove(node)
        visited.add(node)

    for cid in ids:
        visit(cid)

    names = {row["CompetencyName"].strip() for row in rows}
    required_names = {
        "Lafzul Jalalah bentuk dasar",
        "Lafzul Jalalah berharakat",
        "Lafzul Jalalah dengan awalan",
        "Ayat utuh panjang",
        "Integrasi multi-kompetensi",
    }
    missing_names = required_names - names
    if missing_names:
        fail(f"Required competencies missing: {sorted(missing_names)}")
    return ids


def validate_policy_coverage(expected_ids: list[str]) -> None:
    policy_rows = load_rows(POLICY_MATRIX)
    policy_ids = ordered_ids(policy_rows)
    if policy_ids != expected_ids:
        fail("Policy matrix must cover ordered C0001-C0041 exactly once")

    allowed_types = {"LETTER", "WORD_FRAGMENT", "WORD", "PHRASE", "AYAH_FRAGMENT", "FULL_AYAH"}
    for row in policy_rows:
        cid = row["CompetencyID"].strip()
        object_types = {x for x in row["ObjectType"].split("|") if x}
        unknown = object_types - allowed_types
        if unknown:
            fail(f"{cid} has unknown ObjectType values: {sorted(unknown)}")
        minimum = int(row["MinUnits"])
        maximum = int(row["MaxUnits"])
        if minimum < 1 or maximum < minimum:
            fail(f"{cid} has invalid unit range {minimum}-{maximum}")


def import_engine():
    if not ENGINE_FILE.exists():
        fail(f"Pedagogical engine missing: {ENGINE_FILE}")
    spec = importlib.util.spec_from_file_location("qurbata_pedagogical_engine", ENGINE_FILE)
    if spec is None or spec.loader is None:
        fail("Unable to load pedagogical engine module")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    for name in ("load_rules", "validate", "has_madd", "base_letters"):
        if not hasattr(module, name):
            fail(f"Pedagogical engine missing callable: {name}")
    return module


def validate_executable_rules(module, expected_ids: list[str]) -> None:
    rules = module.load_rules(RULE_MATRIX)
    rule_ids = sorted(rules)
    missing = sorted(set(expected_ids) - set(rule_ids))
    extra = sorted(set(rule_ids) - set(expected_ids))
    if missing or extra:
        fail(
            "Executable rule coverage incomplete; "
            f"missing={missing}, extra={extra}. "
            "Page generation must remain blocked until C0001-C0041 are executable."
        )


def base_letters(text: str) -> list[str]:
    normalized = unicodedata.normalize("NFC", text)
    return [ch for ch in normalized if unicodedata.category(ch).startswith("L")]


def has_true_mad_waw(text: str) -> bool:
    chars = list(unicodedata.normalize("NFC", text))
    for index, ch in enumerate(chars):
        if ch != "و":
            continue
        following = chars[index + 1:index + 4]
        if any(mark in following for mark in (FATHA, DAMMA, KASRA, SUKUN, SHADDA)):
            continue
        previous = chars[max(0, index - 3):index]
        if DAMMA in previous:
            return True
    return False


def early_stage_allowed(text: str) -> bool:
    if any(ch in text for ch in HAMZAH_FORMS):
        return False
    if any(ch in text for ch in TANWIN):
        return False
    if SUKUN in text or SHADDA in text:
        return False
    if "ٰ" in text or "ٓ" in text:
        return False
    if has_true_mad_waw(text):
        return False
    return True


def run_regressions(module) -> None:
    rejected = ["ؤُ", "إِ", "دَءُ", "مِنْ", "إِنَّ", "عَلِيمٌ", "قُولُوا"]
    for sample in rejected:
        if early_stage_allowed(sample):
            fail(f"Early-stage gate incorrectly accepted: {sample}")

    accepted = ["بَ", "تِ", "ثُ", "بَتَ", "دَرَ", "هُوَ"]
    for sample in accepted:
        if not early_stage_allowed(sample):
            fail(f"Early-stage gate incorrectly rejected: {sample}")

    if has_true_mad_waw("هُوَ") or module.has_madd("هُوَ"):
        fail("هُوَ must not be classified as mad waw")
    if not has_true_mad_waw("قُولُوا") or not module.has_madd("قُولُوا"):
        fail("قُولُوا must be classified as containing mad waw")
    if len(base_letters("بَتَ")) != 2 or len(module.base_letters("بَتَ")) != 2:
        fail("Base-letter counting failed for بَتَ")
    if len(base_letters("إِنَّ")) != 2 or len(module.base_letters("إِنَّ")) != 2:
        fail("Base-letter counting failed for إِنَّ")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=("dependency", "coverage", "regression", "all"),
        default="all",
    )
    args = parser.parse_args()

    ids = validate_dependency_map()
    if args.mode in ("dependency", "all"):
        print("PASS dependency map C0001-C0041")

    module = import_engine()
    if args.mode in ("coverage", "all"):
        validate_policy_coverage(ids)
        validate_executable_rules(module, ids)
        print("PASS policy and executable rule coverage")

    if args.mode in ("regression", "all"):
        run_regressions(module)
        print("PASS regression suite")

    print("QURBATA pedagogical foundation: VERIFIED_PASS")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
