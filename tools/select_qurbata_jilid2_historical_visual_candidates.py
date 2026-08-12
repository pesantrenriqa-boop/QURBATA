#!/usr/bin/env python3
"""Select strongest historical visual candidate per QURBATA Jilid 2 page.

Consumes the inventory produced by recover_qurbata_jilid2_visual_history.py and
scores historical records for the visual grammar the user already approved:
- explicit presentation arrows / decomposition-composition cue
- large Arabic practice glyphs
- adaptive 4-box and/or 3-box row grid
- per-page renderer/page artifact rather than generic documentation
- newer records preferred only after visual evidence score

This script does NOT modify production files or freeze status. It writes a candidate
selection report for human verification before any page is marked FROZEN.
"""
from __future__ import annotations
import csv,re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
INVENTORY=ROOT/'dist/jilid-2-visual-history-recovery/JILID-2-HISTORICAL-VISUAL-INVENTORY.tsv'
OUT=ROOT/'dist/jilid-2-visual-history-recovery'

ARROW_PATTERNS=('←','->','arrow','presentation')
GRID_PATTERNS=('grid-template-columns:repeat(4','grid-template-columns: repeat(4','span 3','l2','4_box','4-box','grid-template-columns:repeat(3','span 4','l3','3_box','3-box')
FONT_PATTERNS=('36pt','38pt','39pt','40pt','42pt','font-size:36','font-size:38','font-size:39','font-size:40')
RENDER_PATTERNS=('render_qurbata_jilid2','page-0','QURBATA-JILID-2-P')
LEGACY_NEG=('foundation_v1','foundation_v2','foundation_v3','full_review','markdown_preview')

def load():
    if not INVENTORY.exists():
        raise FileNotFoundError(f'INVENTORY_NOT_FOUND={INVENTORY.relative_to(ROOT)}; run recover_qurbata_jilid2_visual_history.py first')
    with INVENTORY.open(encoding='utf-8-sig',newline='') as f:
        return list(csv.DictReader(f,delimiter='\t'))

def val(row,*names):
    for n in names:
        if n in row and row[n]: return row[n]
    return ''

def score(row):
    text=' '.join(str(v) for v in row.values() if v).lower()
    s=0; reasons=[]
    if any(p.lower() in text for p in ARROW_PATTERNS): s+=35; reasons.append('ARROW')
    grid_hits=sum(1 for p in GRID_PATTERNS if p.lower() in text)
    if grid_hits: s+=min(30,grid_hits*5); reasons.append('GRID')
    if any(p.lower() in text for p in FONT_PATTERNS): s+=20; reasons.append('LARGE_FONT')
    if any(p.lower() in text for p in RENDER_PATTERNS): s+=15; reasons.append('RENDERER')
    if any(p.lower() in text for p in LEGACY_NEG): s-=35; reasons.append('LEGACY_PENALTY')
    path=val(row,'path','file','filename','Path','File')
    if re.search(r'p\d{3}',path,re.I): s+=10; reasons.append('PER_PAGE')
    return s,'|'.join(reasons) if reasons else 'NONE'

def page_of(row):
    combined=' '.join(str(v) for v in row.values() if v)
    m=re.search(r'(?:QJ2[-_/ ]?P|jilid2[_-]?p|page[-_ ]?)(\d{3})',combined,re.I)
    if not m:m=re.search(r'\bP(\d{3})\b',combined,re.I)
    return int(m.group(1)) if m else None

def main():
    rows=load(); grouped={n:[] for n in range(1,41)}
    for r in rows:
        p=page_of(r)
        if p and 1<=p<=40:
            sc,why=score(r); grouped[p].append((sc,why,r))
    out=OUT/'JILID-2-HISTORICAL-VISUAL-CANDIDATES.tsv'
    fields=['page','score','signals','commit','path','record_summary','candidate_status']
    with out.open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader()
        selected=0; strong=0
        for n in range(1,41):
            cand=sorted(grouped[n],key=lambda x:x[0],reverse=True)
            if not cand:
                w.writerow({'page':f'P{n:03d}','score':0,'signals':'NONE','candidate_status':'NO_CANDIDATE'});continue
            sc,why,r=cand[0]; selected+=1
            status='STRONG_VISUAL_CANDIDATE' if sc>=55 else 'REVIEW_REQUIRED'
            if status=='STRONG_VISUAL_CANDIDATE':strong+=1
            commit=val(r,'commit','sha','commit_sha','Commit','SHA')
            path=val(r,'path','file','filename','Path','File')
            summary=' | '.join(f'{k}={v}' for k,v in r.items() if v)[:1200]
            w.writerow({'page':f'P{n:03d}','score':sc,'signals':why,'commit':commit,'path':path,'record_summary':summary,'candidate_status':status})
    print('QJ2_HISTORICAL_VISUAL_CANDIDATE_SELECTION=PASS')
    print(f'PAGES_WITH_CANDIDATE={selected}')
    print(f'STRONG_VISUAL_CANDIDATES={strong}')
    print(f'REVIEW_REQUIRED={40-strong}')
    print('FREEZE_STATUS_MODIFIED=NO')
    print('PRODUCTION_FILES_MODIFIED=NO')
    print(f'CANDIDATES={out.relative_to(ROOT)}')
    return 0
if __name__=='__main__':raise SystemExit(main())
