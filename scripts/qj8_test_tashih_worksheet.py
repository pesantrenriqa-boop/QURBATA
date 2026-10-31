#!/usr/bin/env python3
"""Regression tests: a reviewer cannot approve incomplete Saktah tashih."""
import csv
import sys
import tempfile
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
import qj8_validate_tashih_worksheet as gate

def expect_failure(rows):
    with tempfile.TemporaryDirectory() as temp:
        target=Path(temp)/"worksheet.csv"
        with target.open("w",encoding="utf-8",newline="") as f:
            writer=csv.DictWriter(f,fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
        original=gate.FILE
        try:
            gate.FILE=target
            try:
                gate.main()
            except AssertionError:
                return
            raise RuntimeError("INVALID worksheet was accepted")
        finally:
            gate.FILE=original

def main():
    with gate.FILE.open(encoding="utf-8-sig",newline="") as f:
        rows=list(csv.DictReader(f))
    assert len(rows)==4
    gate.main()
    for change in (
        {"decision":"APPROVED"},
        {"decision":"APPROVED","rasm_uthmani_verified":"YES","waqf_saktah_verified":"YES",
         "hafs_recitation_verified":"YES","source_sha256_checked":"YES"},
        {"target_refs":"18:1"},
        {"context_refs":"18:2;18:3"},
        {"case_id":"GH-SAK-02"},
    ):
        altered=[dict(x) for x in rows]
        altered[0].update(change)
        expect_failure(altered)
    print("PASS: incomplete approvals, incorrect target/context, duplicate ID rejected")
    print("HOLD: tests use worksheet data, not authenticated Quran text")

if __name__=="__main__":main()
