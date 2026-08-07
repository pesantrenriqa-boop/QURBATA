#!/usr/bin/env python3
"""QURBATA Practice Generation Engine v1.

Generates deterministic practice sequences from ACTIVE letters only.
Each unit is independent; the engine never creates Arabic connected words.

Pedagogical ordering policy:
- preserve the explicit ActiveLetters order supplied by LPE/GLE;
- L1 starts from the canonical active-letter order (page 1 therefore starts ا ب ت ث);
- L2/L3 avoid adjacent duplicate bases;
- when NewLetters exist after page 1, balance sequences containing new letters with
  cumulative review sequences so one page does not collapse into only the newest letters;
- multi-unit practice remains a sequence of independent units, never an Arabic word.
"""
from __future__ import annotations

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
        # Human-readable audit export only. Renderer MUST render `units` independently.
        return " ".join(self.units)


def _mark_for(stage: str, page: int, sequence_index: int, unit_index: int) -> str:
    if stage in MARKS:
        return MARKS[stage]
    if stage == "MIXED":
        return MIXED_MARKS[(page + sequence_index + unit_index) % len(MIXED_MARKS)]
    raise ValueError(f"UNSUPPORTED_HARAKAT_STAGE: {stage}")


def _cycle_fill(items: list[tuple[str, ...]], count: int) -> list[tuple[str, ...]]:
    if not items:
        return []
    result: list[tuple[str, ...]] = []
    cursor = 0
    while len(result) < count:
        result.append(items[cursor % len(items)])
        cursor += 1
    return result


def _l1_sequences(letters: tuple[str, ...], new_letters: str, count: int, page: int) -> list[tuple[str, ...]]:
    # Page 1 must visibly establish the canonical order beginning with alif.
    if page == 1:
        return _cycle_fill([(letter,) for letter in letters], count)

    new_set = set(new_letters)
    new_part = [(letter,) for letter in letters if letter in new_set]
    review_part = [(letter,) for letter in letters if letter not in new_set]
    ordered = new_part + review_part if new_part else list(review_part)
    return _cycle_fill(ordered, count)


def _structural_sequences(letters: tuple[str, ...], length: int) -> list[tuple[str, ...]]:
    """Build easy-to-scan sequences in canonical order, without adjacent repetition."""
    n = len(letters)
    if n < 2:
        return []

    sequences: list[tuple[str, ...]] = []
    seen: set[tuple[str, ...]] = set()

    if length == 2:
        # First: nearest-neighbour reading flow. Second: one-letter skip.
        for step in (1, 2, 3):
            if step >= n:
                continue
            for start in range(n):
                combo = (letters[start], letters[(start + step) % n])
                if combo[0] == combo[1] or combo in seen:
                    continue
                seen.add(combo); sequences.append(combo)
    elif length == 3:
        # First: three consecutive units. Then controlled permutations, never aa/aaa-like drills.
        patterns = ((0, 1, 2), (0, 2, 1), (0, 1, 3), (0, 2, 3))
        for pattern in patterns:
            if max(pattern) >= n:
                continue
            for start in range(n):
                combo = tuple(letters[(start + delta) % n] for delta in pattern)
                if any(combo[i] == combo[i + 1] for i in range(len(combo) - 1)):
                    continue
                if combo in seen:
                    continue
                seen.add(combo); sequences.append(combo)
    else:
        raise ValueError(f"UNSUPPORTED_STRUCTURAL_LENGTH: {length}")

    return sequences


def _balanced_select(candidates: list[tuple[str, ...]], new_letters: str, count: int, page: int) -> list[tuple[str, ...]]:
    if not candidates:
        return []
    new_set = set(new_letters)
    if page == 1 or not new_set:
        return _cycle_fill(candidates, count)

    new_candidates = [combo for combo in candidates if any(letter in new_set for letter in combo)]
    review_candidates = [combo for combo in candidates if all(letter not in new_set for letter in combo)]

    # Target roughly half new-letter exposure and half cumulative review when both pools exist.
    if new_candidates and review_candidates:
        selected: list[tuple[str, ...]] = []
        ni = ri = 0
        while len(selected) < count:
            if len(selected) % 2 == 0:
                selected.append(new_candidates[ni % len(new_candidates)]); ni += 1
            else:
                selected.append(review_candidates[ri % len(review_candidates)]); ri += 1
        return selected

    return _cycle_fill(new_candidates or review_candidates or candidates, count)


def generate(active_letters: str, new_letters: str, stage: str, length: int, count: int, page: int) -> list[PracticeObject]:
    letters = tuple(dict.fromkeys(active_letters))
    if not letters:
        raise ValueError("ACTIVE_LETTERS_EMPTY")
    if length not in {1, 2, 3}:
        raise ValueError(f"UNSUPPORTED_PRACTICE_LENGTH: {length}")
    if count < 1:
        return []

    if length == 1:
        selected = _l1_sequences(letters, new_letters, count, page)
    else:
        candidates = _structural_sequences(letters, length)
        if not candidates:
            raise ValueError(f"PRACTICE_SEQUENCE_POOL_EMPTY page={page} length={length} active={''.join(letters)}")
        selected = _balanced_select(candidates, new_letters, count, page)

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
    if obj.length > 1 and any(obj.bases[i] == obj.bases[i + 1] for i in range(obj.length - 1)):
        issues.append("ADJACENT_DUPLICATE_BASE")
    return issues
