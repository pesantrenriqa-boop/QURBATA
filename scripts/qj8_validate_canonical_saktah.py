#!/usr/bin/env python3
"""Cross-check canonical Saktah register, source gate and legacy context manifest.
Structural audit only: never asserts Quranic text or print readiness.
"""
import csv
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]/"books/jilid-8"
CASES=ROOT/"QJ8-REGISTER-KASUS-KANONIK-SAKTAH-2026-10-29.csv"
GATE=ROOT/"QJ8-SAKTAH-CONTEXT-GATE.json"
MANIFEST=ROOT/"QJ8-MANIFEST-KONTEKS-AYAT-2026-10-29.csv"
EXPECTED={
 "GH-SAK-01":("N/A",("18:1","18:2"),"18:3"),
 "GH-SAK-02":("36:51",("36:52",),"36:53"),
 "GH-SAK-03":("75:26",("75:27",),"75:28"),
 "GH-SAK-04":("83:13",("83:14",),"83:15"),
}

def check(cases,gate,manifest):
    assert len(cases)==len(EXPECTED)==4, "exactly four canonical occurrences"
    assert {x["case_id"] for x in cases}==set(EXPECTED), "case IDs changed"
    required=set()
    for row in cases:
        before,targets,after=EXPECTED[row["case_id"]]
        assert row["before_ref"]==before
        assert tuple(row["target_refs"].split(";"))==targets
        assert row["after_ref"]==after
        assert row["source_text_status"]=="HOLD_NO_SOURCE"
        assert row["print_status"]=="HOLD"
        required.update(targets)
        if before!="N/A":required.add(before)
        if after!="N/A":required.add(after)
    assert len(required)==12
    assert gate["required_verse_count"]==12
    assert len(gate["required_verse_refs"])==12
    assert set(gate["required_verse_refs"])==required
    assert gate["text_validation"]=="HOLD_NO_SOURCE"
    assert gate["status"]=="HOLD_PENDING_AUTHENTIC_UTHMANI_TEXT"
    target_intervals={tuple(row["target_verse_references"].split(";")) for row in manifest}
    for _,targets,_ in EXPECTED.values():
        assert targets in target_intervals, f"missing legacy target {targets}"
    return True

def main():
    with CASES.open(encoding="utf-8",newline="") as f: cases=list(csv.DictReader(f))
    with MANIFEST.open(encoding="utf-8",newline="") as f: manifest=list(csv.DictReader(f))
    gate=json.loads(GATE.read_text(encoding="utf-8"))
    check(cases,gate,manifest)
    print("PASS: 4 canonical Saktah occurrences; 12 unique verse refs; legacy cross-check")
    print("HOLD: authentic Uthmani text and recitation not verified")

if __name__=="__main__":main()
