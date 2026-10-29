#!/usr/bin/env python3
"""Fail-closed QJ8 manifest validator. No Quran text generated."""
import argparse
import csv
import re
from collections import Counter
from pathlib import Path

# Canonical surah lengths (Hafs / Kufan ayah numbering).
LENGTHS = [7,286,200,176,120,165,206,75,129,109,123,111,43,52,99,128,111,110,98,135,112,78,118,64,77,227,93,88,69,60,34,30,73,54,45,83,182,88,75,85,54,53,89,59,37,35,38,29,18,45,60,49,62,55,78,96,29,22,24,13,14,11,11,18,12,12,30,52,52,44,28,28,20,56,40,31,50,40,46,42,29,19,36,25,22,17,19,26,30,20,15,21,11,8,8,19,5,8,8,11,11,8,3,9,5,4,7,3,6,3,5,4,5,6]
assert len(LENGTHS)==114 and sum(LENGTHS)==6236

def parse(ref):
    if not isinstance(ref,str) or not re.fullmatch(r"[1-9][0-9]*:[1-9][0-9]*",ref):
        raise ValueError(f"malformed Quran verse reference: {ref!r}")
    a,b = ref.split(":")
    s,n=int(a),int(b)
    if not (1<=s<=114 and 1<=n<=LENGTHS[s-1]):
        raise ValueError(f"invalid Quran verse reference: {ref}")
    return s,n

def validate(path):
    with open(path,encoding="utf-8-sig",newline="") as f:
        rows=list(csv.DictReader(f))
    required={"case_id","target_reference","before_reference","target_verse_references","after_reference"}
    if not rows or not required.issubset(rows[0]):
        raise ValueError("missing required columns")
    if any(not row["case_id"] or not row["target_verse_references"] for row in rows):
        raise ValueError("blank case ID or target references")
    ids=Counter(x["case_id"] for x in rows)
    duplicates=[k for k,n in ids.items() if n>1]
    if duplicates: raise ValueError(f"duplicate case IDs: {duplicates}")
    errors=[]
    signatures=Counter()
    for row in rows:
        ident=row["case_id"]
        try:
            target=[parse(v) for v in row["target_verse_references"].split(";")]
            if not target:
                raise ValueError("empty target interval")
            if any(target[i+1] != (target[i][0],target[i][1]+1) for i in range(len(target)-1)):
                raise ValueError("target verses not consecutive within one surah")
            s,start=target[0]
            end=target[-1][1]
            expected_before=f"{s}:{start-1}" if start>1 else "N/A"
            expected_after=f"{s}:{end+1}" if end<LENGTHS[s-1] else "N/A"
            if row["before_reference"]!=expected_before:
                raise ValueError(f"before={row['before_reference']} expected={expected_before}")
            if row["after_reference"]!=expected_after:
                raise ValueError(f"after={row['after_reference']} expected={expected_after}")
            signatures[(s,start,end)]+=1
        except Exception as e: errors.append(f"{ident}: {e}")
    if errors: raise ValueError("\n".join(errors))
    print(f"PASS structural references: {len(rows)} rows; {len(signatures)} distinct target intervals")
    print("NOTE: this is not Gharib authentication, text tashih, or permission to print.")
    return True

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--manifest",default="books/jilid-8/QJ8-MANIFEST-KONTEKS-AYAT-2026-10-29.csv")
    args=ap.parse_args()
    validate(Path(args.manifest))
