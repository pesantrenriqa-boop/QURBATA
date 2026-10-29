#!/usr/bin/env python3
"""Offline regression tests for the QJ8 Saktah 4-case / 12-verse gate.
Runs without Quran text; does NOT certify the recitation or Uthmani spelling.
"""
import csv
import io
import json
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
GATE=ROOT/"books/jilid-8/QJ8-SAKTAH-CONTEXT-GATE.json"
CASES=[
 ("GH-SAK-01",("18:1","18:2"),None,"18:3"),
 ("GH-SAK-02",("36:52",),"36:51","36:53"),
 ("GH-SAK-03",("75:27",),"75:26","75:28"),
 ("GH-SAK-04",("83:14",),"83:13","83:15"),
]
def validate(data):
    assert data.get("status")=="HOLD_PENDING_AUTHENTIC_UTHMANI_TEXT"
    assert data.get("case_count")==4
    refs=set()
    for ident,target,before,after in CASES:
        refs.update(target)
        if before: refs.add(before)
        if after: refs.add(after)
    assert len(refs)==12
    assert set(data["required_verse_refs"])==refs
    assert len(data["required_verse_refs"])==len(refs)
    assert data["text_validation"]=="HOLD_NO_SOURCE"
    return True

def main():
    data=json.loads(GATE.read_text(encoding="utf-8"))
    validate(data)
    for name,mutate in [
        ("missing verse",lambda d:d["required_verse_refs"].remove("36:51")),
        ("duplicate verse",lambda d:d["required_verse_refs"].append("18:1")),
        ("false approved status",lambda d:d.update(text_validation="PASS")),
        ("false source status",lambda d:d.update(status="SOURCE_IMPORTED")),
    ]:
        copy=json.loads(json.dumps(data))
        mutate(copy)
        try:validate(copy)
        except AssertionError:pass
        else:raise AssertionError(f"negative test failed: {name}")
    print("PASS: four positive/negative structural checks; 4 cases, 12 references")
    print("HOLD: no Uthmani text has been imported or reviewed")
if __name__=="__main__":main()
