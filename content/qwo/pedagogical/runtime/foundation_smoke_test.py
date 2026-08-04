#!/usr/bin/env python3
"""Executable smoke tests for the QURBATA pedagogical foundation.

This suite intentionally depends only on the Python standard library so it can
run in GitHub Actions without installing packages.
"""

from __future__ import annotations

import argparse
import csv
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DEPENDENCY_MAP = ROOT / "content/qwo/competency/QURBATA-COMPETENCY-DEPENDENCY-MAP-V1.csv"

HAMZAH_FORMS = set("ءأإؤئآ")
TANWIN = set("ًٌٍ")
SUKUN = "ْ"
SHADDA = "ّ"
FATHA = "َ"
DAMMA = "ُ"
KASRA = "ِ"
ARABIC_MARKS = set("ًٌٍَُِّْٰٓۥۦۭ۟ۢ")


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


def validate_dependency_map() -> None:
    rows = load_rows(DEPENDENCY_MAP)
    ids = [row["CompetencyID"].strip() for row in rows]
    if len(ids) != len(set(ids)):
        fail("Duplicate CompetencyID found")
    if ids != [f"C{i:04d}" for i in range(1, len(ids) + 1)]:
        fail("Competency IDs must be contiguous and ordered")

    known: set[str] = set()
    graph: dict[str, set[str]] = {}
    for row in rows:
        cid = row["CompetencyID"].strip()
        deps = {x for x in row.get("PrerequisiteIDs", "").split("|") if x}
        missing = deps - set(ids)
        if missing:
            fail(f"{cid} references missing prerequisites: {sorted(missing)}")
        graph[cid] = deps
        known.add(cid)

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

    required_names = {
        "Lafzul Jalalah bentuk dasar",
        "Lafzul Jalalah berharakat",
        "Lafzul Jalalah dengan awalan",
        "Ayat utuh panjang",
        "Integrasi multi-kompetensi",
    }
    names = {row["CompetencyName"].strip() for row in rows}
    missing_names = required_names - names
    if missing_names:
        fail(f"Required competencies missing: {sorted(missing_names)}")


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


def run_regressions() -> None:
    rejected = ["ؤُ", "إِ", "دَءُ", "مِنْ", "إِنَّ", "عَلِيمٌ", "قُولُوا"]
    for sample in rejected:
        if early_stage_allowed(sample):
            fail(f"Early-stage gate incorrectly accepted: {sample}")

    accepted = ["بَ", "تِ", "ثُ", "بَتَ", "دَرَ", "هُوَ"]
    for sample in accepted:
        if not early_stage_allowed(sample):
            fail(f"Early-stage gate incorrectly rejected: {sample}")

    if has_true_mad_waw("هُوَ"):
        fail("هُوَ must not be classified as mad waw")
    if not has_true_mad_waw("قُولُوا"):
        fail("قُولُوا must be classified as containing mad waw")

    if len(base_letters("بَتَ")) != 2:
        fail("Base-letter counting failed for بَتَ")
    if len(base_letters("إِنَّ")) != 2:
        fail("Base-letter counting failed for إِنَّ")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("dependency", "regression", "all"), default="all")
    args = parser.parse_args()

    if args.mode in ("dependency", "all"):
        validate_dependency_map()
        print("PASS dependency map")
    if args.mode in ("regression", "all"):
        run_regressions()
        print("PASS regression suite")
    print("QURBATA pedagogical foundation: VERIFIED_PASS")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
