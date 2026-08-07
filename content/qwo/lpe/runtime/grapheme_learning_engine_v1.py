#!/usr/bin/env python3
"""QURBATA Graphical Learning Engine (GLE) v1.

Loads the Jilid 1 grapheme-family registry and provides deterministic family
ranking for early-letter progression. This engine does not compose pages; it
provides ordering metadata that the Composer must respect.
"""
from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DEFAULT_REGISTRY = ROOT / "content/qwo/lpe/JILID-1-GRAPHEME-FAMILY-REGISTRY-V1.csv"
EXPECTED_CANONICAL_LETTERS = set("ابتثجحخدذرزسشصضطظعغفقكلمنهوي")


@dataclass(frozen=True)
class GraphemeFamily:
    family_id: str
    family_order: int
    family_name: str
    letters: tuple[str, ...]
    notes: str
    status: str


def load_registry(path: str | Path = DEFAULT_REGISTRY) -> list[GraphemeFamily]:
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(path)
    result: list[GraphemeFamily] = []
    with path.open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            letters = tuple(row["Letters"].strip())
            result.append(GraphemeFamily(
                family_id=row["FamilyID"].strip(),
                family_order=int(row["FamilyOrder"]),
                family_name=row["FamilyName"].strip(),
                letters=letters,
                notes=row["Notes"].strip(),
                status=row["Status"].strip(),
            ))
    return sorted(result, key=lambda item: item.family_order)


def validate_registry(families: list[GraphemeFamily]) -> list[str]:
    issues: list[str] = []
    orders = [item.family_order for item in families]
    if orders != list(range(1, len(families) + 1)):
        issues.append(f"FAMILY_ORDER_INVALID actual={orders}")

    seen: list[str] = []
    for family in families:
        if not family.family_id or not family.family_name or not family.letters:
            issues.append(f"FAMILY_METADATA_MISSING id={family.family_id or 'UNKNOWN'}")
        seen.extend(family.letters)

    duplicates = sorted({letter for letter in seen if seen.count(letter) > 1})
    if duplicates:
        issues.append("DUPLICATE_LETTERS=" + "|".join(duplicates))

    actual = set(seen)
    missing = sorted(EXPECTED_CANONICAL_LETTERS - actual)
    extra = sorted(actual - EXPECTED_CANONICAL_LETTERS)
    if missing:
        issues.append("CANONICAL_LETTERS_MISSING=" + "|".join(missing))
    if extra:
        issues.append("NON_CANONICAL_LETTERS_PRESENT=" + "|".join(extra))
    return issues


def build_letter_rank(families: list[GraphemeFamily]) -> dict[str, tuple[int, int]]:
    rank: dict[str, tuple[int, int]] = {}
    for family in families:
        for within_family_order, letter in enumerate(family.letters, start=1):
            rank[letter] = (family.family_order, within_family_order)
    return rank


def sort_letters(letters: list[str], families: list[GraphemeFamily]) -> list[str]:
    rank = build_letter_rank(families)
    return sorted(letters, key=lambda letter: rank.get(letter, (999, 999)))
