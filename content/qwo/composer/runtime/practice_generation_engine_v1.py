#!/usr/bin/env python3
"""QURBATA Practice Generation Engine v1.

Generates deterministic practice sequences from ACTIVE letters only.
Each unit is independent; the engine never creates Arabic connected words.
"""
from __future__ import annotations

import itertools
from dataclasses import dataclass

MARKS = {"FATHAH": "َ", "KASRAH": "ِ", "DHAMMAH": "ُ"}
MIXED_MARKS = ("َ", "ِ", "ُ")


@dataclass(frozen=True)
class PracticeObject:
    units: tuple[str, ...]
    bases: tuple[str, ...]
    length: int
    stage: str

    @property
    def display_text(self) -> str:
        # Human-readable export only. Renderer MUST use `units` independently.
        return " ".join(self.units)


def _mark_for(stage: str, page: int, sequence_index: int, unit_index: int) -> str:
    if stage in MARKS:
        return MARKS[stage]
    if stage == "MIXED":
        return MIXED_MARKS[(page + sequence_index + unit_index) % len(MIXED_MARKS)]
    raise ValueError(f"UNSUPPORTED_HARAKAT_STAGE: {stage}")


def generate(active_letters: str, new_letters: str, stage: str, length: int, count: int, page: int) -> list[PracticeObject]:
    letters = tuple(dict.fromkeys(active_letters))
    new_set = set(new_letters)
    if not letters:
        raise ValueError("ACTIVE_LETTERS_EMPTY")
    if length not in {1, 2, 3}:
        raise ValueError(f"UNSUPPORTED_PRACTICE_LENGTH: {length}")
    if count < 1:
        return []

    combos = list(itertools.product(letters, repeat=length))
    # Prefer sequences containing newly introduced letters, then preserve active-letter order.
    rank = {letter: index for index, letter in enumerate(letters)}
    combos.sort(key=lambda combo: (-sum(letter in new_set for letter in combo), tuple(rank[x] for x in combo)))

    selected: list[tuple[str, ...]] = []
    cursor = ((page - 1) * 3 + length) % len(combos)
    ordered = combos[cursor:] + combos[:cursor]
    while len(selected) < count:
        selected.extend(ordered[: count - len(selected)])

    result: list[PracticeObject] = []
    for sequence_index, combo in enumerate(selected):
        units = tuple(
            base + _mark_for(stage, page, sequence_index, unit_index)
            for unit_index, base in enumerate(combo)
        )
        result.append(PracticeObject(units=units, bases=combo, length=length, stage=stage))
    return result


def validate_object(obj: PracticeObject, active_letters: str) -> list[str]:
    active = set(active_letters)
    issues: list[str] = []
    if obj.length != len(obj.units) or obj.length != len(obj.bases):
        issues.append("UNIT_LENGTH_MISMATCH")
    if any(base not in active for base in obj.bases):
        issues.append("FUTURE_LETTER_LEAKAGE")
    if any(" " in unit for unit in obj.units):
        issues.append("SPACE_INSIDE_UNIT")
    return issues
