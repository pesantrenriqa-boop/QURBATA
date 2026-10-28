#!/usr/bin/env python3
"""QURBATA Jilid 6: deterministic register builder and pre-audit (stdlib only)."""
import argparse,csv,json,re,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parent
FIELDS=["slot_id","page_id","competency","kind","text_uthmani","surah","ayah_start","ayah_end","source_id","source_verified","competency_verified","reviewer","review_status","notes"]
SPECIAL={18:"hafalan",28:"bahasa-arab",36:"hafalan",38:"akhlak-hadis"}
def load_master(path):
    text=path.read_text(encoding="utf-8")
    rows=[]
    for line in text.splitlines():
        m=re.match(r"^\|\s*(\d+)\s*\|\s*(QJ6-P\d{3})\s*\|\s*([^|]+)\|\s*([^|]+)\|",line)
        if m: rows.append((int(m[1]),m[2],m[3].strip(),m[4].strip()))
    if len(rows)!=40 or [x[0] for x in rows]!=list(range(1,41)): raise ValueError("Master must contain ordered P001-P040")
    return rows
def init(master,out):
    if out.exists(): raise FileExistsError(f"Refusing to overwrite {out}")
    with out.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=FIELDS);w.writeheader()
        for num,pid,focus,detail in master:
            for s in range(1,10):
                w.writerow(dict(slot_id=f"{pid}-S{s:02d}",page_id=pid,competency=focus+" — "+detail,kind=SPECIAL.get(num,"tartil"),review_status="EMPTY"))
def audit(master,inp,report):
    with inp.open(encoding="utf-8",newline="") as f: rows=list(csv.DictReader(f))
    problems=[];ids=set(); expected={f"{pid}-S{s:02d}" for _,pid,_,_ in master for s in range(1,10)}
    for i,r in enumerate(rows,2):
        sid=r.get("slot_id","");status=r.get("review_status","")
        if sid in ids:problems.append([sid,"DUPLICATE_ID"])
        ids.add(sid)
        if sid not in expected:problems.append([sid,"UNKNOWN_ID"])
        if r.get("page_id")!=sid[:8]:problems.append([sid,"PAGE_MISMATCH"])
        filled=bool(r.get("text_uthmani","").strip())
        if filled:
            if status=="APPROVED" and "PENDING-DEDUP" in r.get("notes",""):
                problems.append([sid,"DEDUP_NOT_CLEARED"])
            try:
                sn=int(r.get("surah",""))
                if sn==1 or 78<=sn<=114:problems.append([sid,"FORBIDDEN_SURAH_J6"])
            except (ValueError,TypeError):pass
            for k in ("source_id","surah","ayah_start","ayah_end"):
                if not r.get(k,"").strip():problems.append([sid,"MISSING_"+k.upper()])
            if r.get("source_verified")!="yes":problems.append([sid,"SOURCE_UNVERIFIED"])
            if r.get("competency_verified")!="yes":problems.append([sid,"COMPETENCY_UNVERIFIED"])
            if r.get("review_status")=="APPROVED" and not r.get("reviewer"):problems.append([sid,"NO_REVIEWER"])
        elif status=="APPROVED":problems.append([sid,"EMPTY_APPROVED"])
        if status=="APPROVED" and (not filled or r.get("source_verified")!="yes" or r.get("competency_verified")!="yes" or not r.get("reviewer","").strip()):
            problems.append([sid,"INVALID_APPROVAL"])
    for sid in sorted(expected-ids):problems.append([sid,"MISSING_SLOT"])
    filled=sum(bool(r.get("text_uthmani","").strip()) for r in rows)
    approved=sum(r.get("review_status")=="APPROVED" for r in rows)
    result={"expected":360,"actual":len(rows),"filled":filled,"approved":approved,"issues":len(problems),"findings":problems,"sha256":hashlib.sha256(inp.read_bytes()).hexdigest(),"warning":"Automated audit cannot authenticate Quranic text or tajwid; human tashih mandatory."}
    report.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps({k:v for k,v in result.items() if k!="findings"},ensure_ascii=False))
    return 1 if problems else 0
def main():
    p=argparse.ArgumentParser();p.add_argument("action",choices=["init","audit"]);p.add_argument("--master",type=Path,required=True);p.add_argument("--csv",type=Path,default=ROOT/"QJ6-slots.csv");p.add_argument("--report",type=Path,default=ROOT/"QJ6-audit.json");a=p.parse_args()
    master=load_master(a.master)
    if a.action=="init":init(master,a.csv);print("Initialized 360 slots")
    else:raise SystemExit(audit(master,a.csv,a.report))
if __name__=="__main__":main()
