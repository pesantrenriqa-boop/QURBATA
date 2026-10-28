#!/usr/bin/env python3
"""QURBATA Jilid 4 register audit; read-only, stdlib only.
Usage: python tools/qj4_slot_audit.py path/to/register.csv
Expected CSV columns: page,slot,text,surah,ayah,source_id,status
Column aliases: halaman,slot,arab,surat,ayat,source_id,status.
"""
import csv, sys, re, json
from collections import Counter
from pathlib import Path

def check(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        rows=list(csv.DictReader(f))
    def field(row,*keys):
        return next((str(row[k]).strip() for k in keys if k in row and row[k] is not None),"")
    errors=[]; seen={}; pages=Counter()
    for i,row in enumerate(rows,2):
        p=field(row,"page","halaman").upper()
        if p.isdigit(): p=f"QJ4-P{int(p):03d}"
        slot=field(row,"slot","slot_id")
        arab=field(row,"text","arab","teks_arab")
        surah=field(row,"surah","surat")
        ayah=field(row,"ayah","ayat")
        source=field(row,"source_id","Source-ID")
        if not re.fullmatch(r"QJ4-P0(?:[0-3][0-9]|40)",p) or p.endswith("000"):
            errors.append([i,"INVALID_PAGE",p])
        else: pages[p]+=1
        for name,value in [("slot",slot),("text",arab),("surah",surah),("ayah",ayah),("source_id",source)]:
            if not value: errors.append([i,"MISSING_"+name.upper(),p])
        if arab and not re.search(r"[\u0621-\u064a]",arab):
            errors.append([i,"NOT_ARABIC",p])
        key=(surah.casefold(),ayah,arab)
        if all(key):
            if key in seen: errors.append([i,"DUPLICATE_TEXT_REFERENCE",f"first row {seen[key]}"])
            else: seen[key]=i
        if source:
            if source in seen: errors.append([i,"DUPLICATE_SOURCE_ID",f"first row {seen[source]}"])
            else: seen[source]=i
        # Never certify tajwid or a Quran quotation using orthography alone.
    return {"rows":len(rows),"pages_with_rows":len(pages),"counts_by_page":dict(sorted(pages.items())),"issues":errors,"issue_count":len(errors),"tajwid_review":"REQUIRED","quran_text_verification":"REQUIRED","competency_whitelist_review":"REQUIRED"}
if __name__=="__main__":
    if len(sys.argv)!=2: sys.exit(__doc__)
    print(json.dumps(check(Path(sys.argv[1])),ensure_ascii=False,indent=2))
