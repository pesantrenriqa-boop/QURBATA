#!/usr/bin/env python3
"""Audit QURBATA J4: never turn fragments or unreviewed ayat into approved exercises.
Usage: python J4_GATE_REGISTER_960.py REGISTER_24_KELOMPOK_JILID_4.md
"""
import re, sys, pathlib
PAGES=40
SLOTS=24
def audit(path):
    txt=pathlib.Path(path).read_text(encoding="utf-8")
    lines=[x for x in txt.splitlines() if re.match(r"^\| P\d{3} \|",x) and x.rstrip().endswith("| 0/24 |")]
    assert len(lines)==PAGES, f"Expected 40 canonical register rows, got {len(lines)}"
    seen={}
    filled=0
    for i,line in enumerate(lines,1):
        cells=[x.strip() for x in line.split("|")[1:-1]]
        assert cells[0]==f"P{i:03}",f"Missing page P{i:03}"
        assert len(cells)==27,f"{cells[0]}: expected page, competency, 24 slots, status; got {len(cells)}"
        for j,cell in enumerate(cells[2:26],1):
            if cell=="—": continue
            filled+=1
            ref=re.search(r"\[QS\s+(\d+):(\d+);",cell)
            assert ref, f"{cells[0]}/K{j:02}: missing explicit surah:ayah source"
            key=ref.group(1)+":"+ref.group(2)
            assert key not in seen,f"Duplicate verse {key} in {cells[0]}/K{j:02} and {seen[key]}"
            seen[key]=f"{cells[0]}/K{j:02}"
            assert "SAH CETAK" not in cell, "Automated script cannot certify Quran text"
    print(f"Pages: {PAGES}; total slots: {PAGES*SLOTS}; candidate slots: {filled}; empty: {PAGES*SLOTS-filled}; independently certified: 0")
    print("WARNING: This structural audit cannot validate full verse boundaries, rasm, waqf, or pedagogical tajwid gates.")
if __name__=="__main__":
    if len(sys.argv)!=2: raise SystemExit("Usage: python J4_GATE_REGISTER_960.py REGISTER.md")
    audit(sys.argv[1])
