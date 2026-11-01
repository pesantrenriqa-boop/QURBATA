#!/usr/bin/env python3
"""Read-only audit of the 360-slot QURBATA Jilid 8 draft.
No automatic replacement or print approval; duplicate text is a review flag.
"""
import argparse
import collections
import csv
import io
import json
import re
from pathlib import Path

DEFAULT=Path(__file__).resolve().parents[1]/"books/jilid-8/QJ8-MATRIKS-SINKRON-360-SLOT-2026-10-29.md"
PATTERN=re.compile(r"^\| (QJ8-P(\d{3})-K(\d{2})) \| (.*?) \| (.*?) \| (.*?) \| (.*?) \|$")
def audit(source):
    rows=[]
    for line in source.splitlines():
        m=PATTERN.fullmatch(line)
        if m:
            slot,page,k,text,ref,status,origin=m.groups()
            rows.append(dict(slot=slot,page=int(page),position=int(k),text=text,ref=ref,status=status,origin=origin))
    expected={f"QJ8-P{p:03d}-K{k:02d}" for p in range(1,41) for k in range(1,10)}
    ids=[r["slot"] for r in rows]
    assert len(rows)==360 and len(set(ids))==360 and set(ids)==expected, "Slot coverage invalid"
    assert all(r["text"] and r["ref"] and r["origin"] for r in rows), "Missing source metadata"
    by_text=collections.defaultdict(list)
    for row in rows:by_text[row["text"]].append(row["slot"])
    repeats={text:ids for text,ids in by_text.items() if len(ids)>1}
    report={
        "source":str(DEFAULT.relative_to(DEFAULT.parents[2])),
        "status":"DRAFT_AUDIT_NOT_TASHIH",
        "slots":len(rows),"pages":40,"slots_per_page":9,
        "unique_texts":len(by_text),"repeat_occurrences":sum(len(ids)-1 for ids in repeats.values()),
        "repeated_text_groups":len(repeats),
        "repeats":[{"text":text,"count":len(ids),"slots":ids} for text,ids in sorted(repeats.items(),key=lambda pair:(-len(pair[1]),pair[0]))],
        "note":"Repeated text may be pedagogically intentional; inspect before editing. Source texts not verified against Uthmani mushaf."
    }
    return report

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--source",type=Path,default=DEFAULT)
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    report=audit(args.source.read_text(encoding="utf-8"))
    serialized=json.dumps(report,ensure_ascii=False,indent=2)+"\n"
    if args.output:
        with args.output.open("x",encoding="utf-8") as f:f.write(serialized)
    else:print(serialized)
if __name__=="__main__":main()
