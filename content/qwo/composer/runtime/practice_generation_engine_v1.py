#!/usr/bin/env python3
"""QURBATA Practice Generation Engine v1.

Generates deterministic practice sequences from ACTIVE letters only.
Each unit is independent; the engine never creates Arabic connected words.

Pedagogical ordering policy:
- preserve explicit ActiveLetters order;
- page 1 establishes the foundation set in canonical order;
- L2/L3 avoid adjacent duplicate bases;
- after page 1, target 50% NEW competency exposure and 50% cumulative REVIEW;
- REVIEW means prior competency with a fresh surface combination where possible;
- multi-unit practice is never an Arabic connected word.
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
    learning_state: str

    @property
    def display_text(self) -> str:
        return " ".join(self.units)

def _mark_for(stage: str, page: int, sequence_index: int, unit_index: int) -> str:
    if stage in MARKS: return MARKS[stage]
    if stage == "MIXED": return MIXED_MARKS[(page + sequence_index + unit_index) % 3]
    raise ValueError(f"UNSUPPORTED_HARAKAT_STAGE: {stage}")

def _cycle_fill(items, count):
    if not items: return []
    return [items[i % len(items)] for i in range(count)]

def _structural_sequences(letters: tuple[str, ...], length: int):
    n=len(letters); out=[]; seen=set()
    if n < 2: return []
    if length == 2:
        for step in (1,2,3):
            if step >= n: continue
            for start in range(n):
                c=(letters[start],letters[(start+step)%n])
                if c[0]!=c[1] and c not in seen: seen.add(c); out.append(c)
    elif length == 3:
        for pattern in ((0,1,2),(0,2,1),(0,1,3),(0,2,3)):
            if max(pattern)>=n: continue
            for start in range(n):
                c=tuple(letters[(start+d)%n] for d in pattern)
                if any(c[i]==c[i+1] for i in range(2)) or c in seen: continue
                seen.add(c); out.append(c)
    else: raise ValueError(f"UNSUPPORTED_STRUCTURAL_LENGTH: {length}")
    return out

def _tagged_select(candidates, new_letters: str, count: int, page: int):
    """Return (sequence,state). Page 1 is FOUNDATION; later pages target 50:50."""
    if page == 1:
        return [(x,"FOUNDATION") for x in _cycle_fill(candidates,count)]
    ns=set(new_letters)
    if not ns:
        return [(x,"REVIEW") for x in _cycle_fill(candidates,count)]
    new=[x for x in candidates if any(ch in ns for ch in x)]
    review=[x for x in candidates if all(ch not in ns for ch in x)]
    if not new or not review:
        raise ValueError(f"FIFTY_FIFTY_POOL_UNAVAILABLE page={page} new={len(new)} review={len(review)}")
    half=count//2
    selected=[]
    for i in range(half):
        selected.append((new[i%len(new)],"NEW"))
        selected.append((review[i%len(review)],"REVIEW"))
    if count%2: selected.append((new[half%len(new)],"NEW"))
    return selected

def generate(active_letters: str, new_letters: str, stage: str, length: int, count: int, page: int):
    letters=tuple(dict.fromkeys(active_letters))
    if not letters: raise ValueError("ACTIVE_LETTERS_EMPTY")
    if length not in {1,2,3}: raise ValueError(f"UNSUPPORTED_PRACTICE_LENGTH: {length}")
    if count<1: return []
    if length==1:
        candidates=[(x,) for x in letters]
    else:
        candidates=_structural_sequences(letters,length)
    if not candidates: raise ValueError(f"PRACTICE_SEQUENCE_POOL_EMPTY page={page} length={length}")
    tagged=_tagged_select(candidates,new_letters,count,page)
    result=[]
    for si,(combo,state) in enumerate(tagged):
        units=tuple(base+_mark_for(stage,page,si,ui) for ui,base in enumerate(combo))
        result.append(PracticeObject(units,combo,length,stage,state))
    return result

def validate_object(obj: PracticeObject, active_letters: str):
    active=set(active_letters); issues=[]
    if obj.length!=len(obj.units) or obj.length!=len(obj.bases): issues.append("UNIT_LENGTH_MISMATCH")
    if any(b not in active for b in obj.bases): issues.append("FUTURE_LETTER_LEAKAGE")
    if any(" " in u for u in obj.units): issues.append("SPACE_INSIDE_UNIT")
    if obj.length>1 and any(obj.bases[i]==obj.bases[i+1] for i in range(obj.length-1)): issues.append("ADJACENT_DUPLICATE_BASE")
    if obj.learning_state not in {"FOUNDATION","NEW","REVIEW"}: issues.append("LEARNING_STATE_INVALID")
    return issues
