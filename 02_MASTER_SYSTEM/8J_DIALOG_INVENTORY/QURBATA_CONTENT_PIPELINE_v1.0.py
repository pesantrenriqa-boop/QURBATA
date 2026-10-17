#!/usr/bin/env python3
"""Read-only QURBATA 8-volume content audit. Standard library only."""
import argparse, csv, json, re
from pathlib import Path

PATTERN = re.compile(r"QJ(\d+)_P(\d{3})_PAKET_KONTEN_TERPADU_SIAP_REVIEW_v\d+\.\d+\.md$")
HADITH = {"H03":(1,4),"H04":(5,8),"H05":(9,12),"H08":(13,16),"H07":(17,20),"H09":(21,24),"H11":(25,27),"H12":(28,30)}
GATES = ("G1","G2","G3","G4","G5")
def inspect(root):
    rows=[]
    for jilid in range(1,9):
        for page in range(1,41):
            matches=list(root.rglob(f"QJ{jilid}_P{page:03d}_PAKET_KONTEN_TERPADU_SIAP_REVIEW_v*.md"))
            row={"jilid":jilid,"page":page,"status":"MISSING" if not matches else "REVIEW","file":str(matches[0]) if matches else "", "issues":[]}
            if matches:
                body=matches[0].read_text(encoding="utf-8")
                if not re.search(r"Tartil",body,re.I):row["issues"].append("NO_TARTIL")
                if not re.search(r"Arabiyah|Bi.ah",body,re.I):row["issues"].append("NO_DIALOG")
                if not re.search(r"Akhlak",body,re.I):row["issues"].append("NO_AKHLAK")
                if not re.search(r"Tahfidz",body,re.I):row["issues"].append("NO_TAHFIDZ")
                if not re.search(r"FROZEN",body,re.I):row["issues"].append("NO_FROZEN_MARKER")
                if jilid==2:
                    expected=next((k for k,(a,z) in HADITH.items() if a<=page<=z), "H05" if page<=34 else "H07" if page<=38 else "H11")
                    row["hadith_expected"]=expected
                    if not re.search(r"Integrasi hadis Akhlak "+expected+r"\b|Kandidat hadis Akhlak terkait halaman|Hadis Akhlak kandidat "+expected,body,re.I):
                        row["issues"].append("HADITH_NOT_INTEGRATED")
                if "CONTENT-FINAL" in body and re.search(r"CONTENT-FINAL\s*(?:PASS|APPROVED)",body,re.I):
                    row["issues"].append("CLAIMED_FINAL_REQUIRES_MANUAL_EVIDENCE")
            rows.append(row)
    return rows

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--root",default=".")
    ap.add_argument("--out",default="qurbata-audit")
    args=ap.parse_args()
    rows=inspect(Path(args.root))
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    with (out/"audit.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=["jilid","page","status","file","hadith_expected","issues"],extrasaction="ignore")
        w.writeheader()
        for row in rows:w.writerow({**row,"issues":";".join(row["issues"])})
    report={"total":320,"files_present":sum(x["status"]!="MISSING" for x in rows),"missing":sum(x["status"]=="MISSING" for x in rows),"issues":sum(bool(x["issues"]) for x in rows),"final_approved_by_script":0,"warning":"Automated checks never authorize G1–G5 or CONTENT-FINAL"}
    (out/"summary.json").write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding="utf-8")
    print(json.dumps(report,ensure_ascii=False))
if __name__=="__main__":main()
