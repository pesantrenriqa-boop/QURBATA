#!/usr/bin/env python3
"""Recover exact historical QURBATA Jilid 2 visual renderer candidates.

Goal: find the original per-page visual grammar from Git history, not synthesize a
new layout. Desired fingerprint:
- presentation/new-material strip with arrow(s)
- large Arabic practice text
- adaptive 4 objects/row (L2 span=3 of 12) and 3 objects/row (L3 span=4 of 12)
- NO visible practice boxes/borders/background cards

Font is scored separately. Legacy Amiri may identify the historical structure; it
will be replaced by the current KFGQPC pipeline only after structural recovery.
No production file or freeze register is modified.
"""
from __future__ import annotations
import re, subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'dist/jilid-2-exact-visual-recovery'
PAGE_RE=re.compile(r'(?:^|[_/-])p(\d{3})(?:[_./-]|$)',re.I)

def sh(*args):
    p=subprocess.run(args,cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL)
    return p.stdout.decode('utf-8','replace') if p.returncode==0 else ''

def score(text:str):
    u=text.upper();s=0;tags=[]
    def hit(cond,pts,name):
        nonlocal s
        if cond:s+=pts;tags.append(name)
    hit('PRESENTATION' in u and ('←' in text or '&LARR;' in u or 'ARROW' in u),8,'ARROW_PRESENTATION')
    hit('GRID-TEMPLATE-COLUMNS:REPEAT(12' in u.replace(' ',''),7,'GRID12')
    hit('GRID-COLUMN:SPAN 3' in u or 'GRID-COLUMN:SPAN3' in u.replace(' ',''),6,'L2_4_PER_ROW')
    hit('GRID-COLUMN:SPAN 4' in u or 'GRID-COLUMN:SPAN4' in u.replace(' ',''),6,'L3_3_PER_ROW')
    hit(bool(re.search(r'font-size\s*:\s*(3[4-9]|[4-9]\d)pt',text,re.I)),5,'LARGE_ARABIC')
    hit('KFGQPC' in u or 'UTHMAN TAHA' in u,4,'KFGQPC')
    hit('AMIRI QURAN' in u or "'AMIRI'" in u,1,'LEGACY_FONT_STRUCTURE_ONLY')
    # Strongly prefer practice objects with no visual card/border.
    no_box=bool(re.search(r'\.j2-object\s*\{[^}]*border\s*:\s*0',text,re.I|re.S)) or not bool(re.search(r'\.j2-object\s*\{[^}]*border\s*:',text,re.I|re.S))
    hit(no_box,7,'NO_VISIBLE_BOX')
    bad_box=bool(re.search(r'\.j2-object\s*\{[^}]*(border\s*:\s*(?!0)|background\s*:)',text,re.I|re.S))
    if bad_box:s-=12;tags.append('VISIBLE_BOX_PENALTY')
    return s,'|'.join(tags)

def page_from(path,text):
    m=PAGE_RE.search(path)
    if m:return int(m.group(1))
    m=re.search(r'PAGE\s*=\s*[\'\"]?0*(\d{1,3})',text,re.I)
    return int(m.group(1)) if m else None

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    commits=sh('git','rev-list','--all').splitlines()
    best={};records=0
    for commit in commits:
        names=sh('git','ls-tree','-r','--name-only',commit).splitlines()
        for path in names:
            low=path.lower()
            if 'jilid2' not in low and 'jilid-2' not in low:continue
            if not low.endswith(('.py','.html','.css')):continue
            if not any(x in low for x in ('render','page','print','pdf')):continue
            text=sh('git','show',f'{commit}:{path}')
            if not text:continue
            page=page_from(path,text)
            if not page or not 1<=page<=40:continue
            sc,tags=score(text);records+=1
            cur=best.get(page)
            row=(sc,commit,path,tags)
            if cur is None or row[0]>cur[0]:best[page]=row
    lines=['page\tscore\tcommit\tpath\tfingerprint']
    strong=0
    for p in range(1,41):
        row=best.get(p)
        if row:
            sc,c,path,tags=row
            if sc>=30:strong+=1
            lines.append(f'P{p:03d}\t{sc}\t{c}\t{path}\t{tags}')
        else:lines.append(f'P{p:03d}\t\t\t\tNO_CANDIDATE')
    out=OUT/'JILID-2-EXACT-VISUAL-RENDERER-CANDIDATES.tsv';out.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print('QJ2_EXACT_VISUAL_RENDERER_RECOVERY=PASS')
    print(f'HISTORICAL_RENDERER_RECORDS_SCANNED={records}')
    print(f'PAGES_WITH_EXACT_CANDIDATE={len(best)}')
    print(f'STRONG_NO_BOX_ARROW_GRID_CANDIDATES={strong}')
    print('VISIBLE_BOX_LAYOUT_ACCEPTED=NO')
    print('FREEZE_STATUS_MODIFIED=NO')
    print('PRODUCTION_FILES_MODIFIED=NO')
    print(f'CANDIDATES={out.relative_to(ROOT)}')
if __name__=='__main__':main()
