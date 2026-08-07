#!/usr/bin/env python3
"""QURBATA Practice Generation Engine v1.

Generates deterministic independent-unit practice from ACTIVE letters.
50:50 is defined by competency, not merely by newly introduced letters:
- while new letters are introduced: NEW = current letters, REVIEW = earlier active letters;
- after the alphabet set is established: NEW = current harakat competency,
  REVIEW = cumulative previously mastered harakat competencies;
- review prefers fresh surface combinations and never introduces future material.
"""
from __future__ import annotations
from dataclasses import dataclass

MARKS={"FATHAH":"َ","KASRAH":"ِ","DHAMMAH":"ُ"}
MIXED_MARKS=("َ","ِ","ُ")

@dataclass(frozen=True)
class PracticeObject:
    units:tuple[str,...]
    bases:tuple[str,...]
    length:int
    stage:str
    learning_state:str
    review_from_stage:str=""
    @property
    def display_text(self)->str:return " ".join(self.units)

def _mark_for(stage,page,sequence_index,unit_index):
    if stage in MARKS:return MARKS[stage]
    if stage=="MIXED":return MIXED_MARKS[(page+sequence_index+unit_index)%3]
    raise ValueError(f"UNSUPPORTED_HARAKAT_STAGE: {stage}")

def _structural_sequences(letters,length):
    n=len(letters);out=[];seen=set()
    if length==1:return [(x,) for x in letters]
    if n<2:return []
    if length==2:
        steps=range(1,n)
        for step in steps:
            for start in range(n):
                c=(letters[start],letters[(start+step)%n])
                if c[0]!=c[1] and c not in seen:seen.add(c);out.append(c)
    elif length==3:
        for step1 in range(1,min(n,6)):
            for step2 in range(1,min(n,6)):
                for start in range(n):
                    c=(letters[start],letters[(start+step1)%n],letters[(start+step1+step2)%n])
                    if any(c[i]==c[i+1] for i in range(2)) or c in seen:continue
                    seen.add(c);out.append(c)
    else:raise ValueError(f"UNSUPPORTED_PRACTICE_LENGTH: {length}")
    return out

def _slice_rotated(items,count,seed):
    if not items:return []
    start=seed%len(items);rot=items[start:]+items[:start]
    if len(rot)>=count:return rot[:count]
    return [rot[i%len(rot)] for i in range(count)]

def _make(combo,stage,state,page,seq_index,review_from=""):
    units=tuple(base+_mark_for(stage,page,seq_index,i) for i,base in enumerate(combo))
    return PracticeObject(units,combo,len(combo),stage,state,review_from)

def generate(active_letters:str,new_letters:str,stage:str,length:int,count:int,page:int,review_stages:tuple[str,...]=())->list[PracticeObject]:
    letters=tuple(dict.fromkeys(active_letters));new_set=set(new_letters)
    if not letters:raise ValueError("ACTIVE_LETTERS_EMPTY")
    if count<1:return []
    if count%2 and page!=1:raise ValueError("FIFTY_FIFTY_REQUIRES_EVEN_COUNT")
    candidates=_structural_sequences(letters,length)
    if not candidates:raise ValueError(f"PRACTICE_SEQUENCE_POOL_EMPTY page={page} length={length}")

    # Foundation page: all slots establish the initial competency.
    if page==1:
        chosen=_slice_rotated(candidates,count,0)
        return [_make(c,stage,"FOUNDATION",page,i) for i,c in enumerate(chosen)]

    half=count//2
    result=[]
    if new_set:
        # New-letter phase: current competency vs cumulative previous letters, same harakat.
        new_candidates=[c for c in candidates if any(x in new_set for x in c)]
        review_candidates=[c for c in candidates if all(x not in new_set for x in c)]
        if not new_candidates or not review_candidates:
            raise ValueError(f"LETTER_REVIEW_POOL_UNAVAILABLE page={page} length={length}")
        new_sel=_slice_rotated(new_candidates,half,page*11+length*3)
        rev_sel=_slice_rotated(review_candidates,half,page*17+length*5)
        for i in range(half):
            result.append(_make(new_sel[i],stage,"NEW",page,2*i))
            result.append(_make(rev_sel[i],stage,"REVIEW",page,2*i+1,stage))
        return result

    # Harakat phase: NEW is current harakat; REVIEW comes from all earlier mastered harakat.
    if not review_stages:
        raise ValueError(f"REVIEW_STAGES_REQUIRED page={page} stage={stage}")
    new_sel=_slice_rotated(candidates,half,page*19+length*7)
    rev_sel=_slice_rotated(candidates,half,page*23+length*11)
    for i in range(half):
        review_stage=review_stages[(page+i+length)%len(review_stages)]
        result.append(_make(new_sel[i],stage,"NEW",page,2*i))
        result.append(_make(rev_sel[i],review_stage,"REVIEW",page,2*i+1,review_stage))
    return result

def validate_object(obj,active_letters):
    active=set(active_letters);issues=[]
    if obj.length!=len(obj.units) or obj.length!=len(obj.bases):issues.append("UNIT_LENGTH_MISMATCH")
    if any(b not in active for b in obj.bases):issues.append("FUTURE_LETTER_LEAKAGE")
    if any(" " in u for u in obj.units):issues.append("SPACE_INSIDE_UNIT")
    if obj.length>1 and any(obj.bases[i]==obj.bases[i+1] for i in range(obj.length-1)):issues.append("ADJACENT_DUPLICATE_BASE")
    if obj.learning_state not in {"FOUNDATION","NEW","REVIEW"}:issues.append("LEARNING_STATE_INVALID")
    return issues
