#!/usr/bin/env python3
"""Materialize only STRONG QJ2 historical visual candidates from fast recovery TSV.
No production or freeze files are modified.
"""
from __future__ import annotations
import csv, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'dist/jilid-2-exact-visual-recovery/JILID-2-EXACT-VISUAL-RENDERER-CANDIDATES-FAST.tsv'
OUT=ROOT/'dist/jilid-2-exact-visual-recovery/strong-candidates'

def git_show(commit,path):
    p=subprocess.run(['git','show',f'{commit}:{path}'],cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if p.returncode!=0:return None,p.stderr.decode('utf-8','replace')
    return p.stdout,p.stderr.decode('utf-8','replace')

def main():
    if not SRC.exists():raise SystemExit('FAST_CANDIDATE_TSV_NOT_FOUND')
    with SRC.open(encoding='utf-8-sig',newline='') as f:rows=list(csv.DictReader(f,delimiter='\t'))
    strong=[r for r in rows if (r.get('Strength') or '').upper()=='STRONG']
    OUT.mkdir(parents=True,exist_ok=True)
    print('QJ2_STRONG_VISUAL_CANDIDATES=MATERIALIZE')
    print(f'STRONG_COUNT={len(strong)}')
    ok=0
    for i,r in enumerate(strong,1):
        page=r.get('Page','');commit=r.get('Commit','');path=r.get('Path','');score=r.get('Score','');why=r.get('Reasons','')
        print(f'--- CANDIDATE_{i} ---')
        print(f'PAGE={page}');print(f'SCORE={score}');print(f'COMMIT={commit}');print(f'PATH={path}');print(f'REASONS={why}')
        data,err=git_show(commit,path)
        if data is None:
            print('MATERIALIZED=NO');print('ERROR='+err.replace('\n',' ')[:300]);continue
        suffix=Path(path).suffix or '.txt';dst=OUT/f'{page}-{commit[:12]}{suffix}';dst.write_bytes(data);ok+=1
        print('MATERIALIZED=YES');print(f'SOURCE_COPY={dst.relative_to(ROOT)}')
    print(f'MATERIALIZED_COUNT={ok}')
    print('FREEZE_STATUS_MODIFIED=NO');print('PRODUCTION_FILES_MODIFIED=NO')
    return 0
if __name__=='__main__':raise SystemExit(main())
