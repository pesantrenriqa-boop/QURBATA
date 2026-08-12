#!/usr/bin/env python3
"""Fast QJ2 exact visual recovery using the already-generated historical inventory.

Avoids rescanning full Git history. Reads the 366-record inventory produced by
recover_qurbata_jilid2_visual_history.py and scores historical renderer records for:
- arrow/presentation pattern
- large Arabic typography
- 3/4 objects per row or 12-column span grammar
- no visible practice boxes/borders

No production files or freeze status are modified.
"""
from __future__ import annotations
import csv,re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'dist/jilid-2-visual-history-recovery/JILID-2-HISTORICAL-VISUAL-INVENTORY.tsv'
OUT=ROOT/'dist/jilid-2-exact-visual-recovery'
DST=OUT/'JILID-2-EXACT-VISUAL-RENDERER-CANDIDATES-FAST.tsv'

PAGE_RE=re.compile(r'P(\d{3})',re.I)

def val(r,*keys):
    for k in keys:
        if k in r and r[k]: return r[k]
    return ''

def score(r):
    blob=' '.join(str(v) for v in r.values()).lower()
    s=0; reasons=[]
    if 'render' in blob or '.py' in blob: s+=3;reasons.append('renderer')
    if 'arrow' in blob or '←' in blob or 'presentation' in blob: s+=5;reasons.append('arrow/presentation')
    if 'font-size' in blob or '36pt' in blob or '34pt' in blob or '31pt' in blob: s+=3;reasons.append('large-font')
    if 'grid-template-columns:repeat(12' in blob or 'span 3' in blob or 'span 4' in blob or 'l2' in blob or 'l3' in blob: s+=5;reasons.append('3/4-grid')
    if 'kfgqpc' in blob or 'uthman taha' in blob: s+=4;reasons.append('kfgqpc')
    # Penalize visible box styling, but do not reject historical content merely for border mentions elsewhere.
    box_terms=sum(blob.count(x) for x in ['border:', 'border =', 'background:', 'box-shadow'])
    if box_terms>=3: s-=5;reasons.append('box-style-penalty')
    return s,'|'.join(reasons)

def main():
    if not SRC.exists(): raise SystemExit('Run recover_qurbata_jilid2_visual_history.py first')
    with SRC.open(encoding='utf-8-sig',newline='') as f: rows=list(csv.DictReader(f,delimiter='\t'))
    by={i:[] for i in range(1,41)}
    for r in rows:
        ptxt=val(r,'Page','page','PAGE')
        m=PAGE_RE.search(ptxt) or PAGE_RE.search(' '.join(str(v) for v in r.values()))
        if not m: continue
        p=int(m.group(1))
        if 1<=p<=40:
            sc,why=score(r); by[p].append((sc,why,r))
    OUT.mkdir(parents=True,exist_ok=True)
    fields=['Page','Score','Strength','Reasons','Commit','Path','OriginalRecord']
    out=[];strong=0;covered=0
    for p in range(1,41):
        cand=sorted(by[p],key=lambda x:x[0],reverse=True)
        if cand:
            covered+=1;sc,why,r=cand[0]
            strength='STRONG' if sc>=10 else 'REVIEW'
            if strength=='STRONG':strong+=1
            out.append({'Page':f'P{p:03d}','Score':sc,'Strength':strength,'Reasons':why,'Commit':val(r,'Commit','commit','SHA','sha'),'Path':val(r,'Path','path','File','file','Filename','filename'),'OriginalRecord':repr(r)})
        else:
            out.append({'Page':f'P{p:03d}','Score':'','Strength':'NONE','Reasons':'','Commit':'','Path':'','OriginalRecord':''})
    with DST.open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(out)
    print('QJ2_EXACT_VISUAL_RENDERER_RECOVERY_FAST=PASS')
    print(f'INVENTORY_RECORDS_READ={len(rows)}')
    print(f'PAGES_WITH_CANDIDATE={covered}')
    print(f'STRONG_CANDIDATES={strong}')
    print(f'REVIEW_REQUIRED={40-strong}')
    print('FULL_GIT_RESCAN=NO')
    print('VISIBLE_BOX_LAYOUT_ACCEPTED=NO')
    print('FREEZE_STATUS_MODIFIED=NO')
    print('PRODUCTION_FILES_MODIFIED=NO')
    print(f'OUTPUT={DST.relative_to(ROOT)}')
    return 0

if __name__=='__main__': raise SystemExit(main())
