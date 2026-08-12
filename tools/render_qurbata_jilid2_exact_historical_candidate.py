#!/usr/bin/env python3
"""Render an exact historical QURBATA Jilid 2 candidate from its original commit.

No visual reconstruction is performed. The script creates a temporary detached Git
worktree at the historical commit, executes the original renderer there, then copies
all generated PDFs/PNGs back into the current repository under dist for review.
Production files and freeze registry are not modified.
"""
from __future__ import annotations
import argparse, shutil, subprocess, sys, tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CANDIDATES={
    'P017':('cee937e853550c63bb508e23edfebce0d8f583f7','tools/render_qurbata_jilid2_p017_v1_kfgqpc_ha.py'),
    'P018':('604399dabec78c9168a3f050efa97c8b5ea0f40e','tools/render_qurbata_jilid2_p018_v1_kfgqpc_ya.py'),
}

def run(cmd,cwd,check=True):
    p=subprocess.run(cmd,cwd=cwd,text=True,encoding='utf-8',errors='replace')
    if check and p.returncode!=0: raise RuntimeError(f'COMMAND_FAILED={cmd!r} RC={p.returncode}')
    return p.returncode

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--page',choices=sorted(CANDIDATES),default='P017');a=ap.parse_args()
    page=a.page;commit,renderer=CANDIDATES[page]
    out=ROOT/'dist/jilid-2-exact-historical-preview'/page.lower();out.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=f'qurbata-{page.lower()}-') as td:
        wt=Path(td)/'repo'
        run(['git','worktree','add','--detach',str(wt),commit],ROOT)
        try:
            before={p.resolve() for p in wt.rglob('*.pdf')}|{p.resolve() for p in wt.rglob('*.png')}
            rc=run([sys.executable,renderer],wt,check=False)
            after=[p for p in wt.rglob('*') if p.is_file() and p.suffix.lower() in {'.pdf','.png'} and p.resolve() not in before]
            copied=[]
            for src in after:
                dst=out/src.name
                shutil.copy2(src,dst);copied.append(dst)
            print('QJ2_EXACT_HISTORICAL_CANDIDATE=PASS' if rc==0 else 'QJ2_EXACT_HISTORICAL_CANDIDATE=RENDERER_FAILED')
            print(f'PAGE={page}')
            print(f'HISTORICAL_COMMIT={commit}')
            print(f'HISTORICAL_RENDERER={renderer}')
            print(f'RENDERER_RC={rc}')
            print(f'ARTIFACTS_COPIED={len(copied)}')
            for p in copied: print('ARTIFACT='+str(p.relative_to(ROOT)))
            print('VISUAL_RECONSTRUCTION=NO')
            print('FREEZE_STATUS_MODIFIED=NO')
            print('PRODUCTION_FILES_MODIFIED=NO')
            return rc
        finally:
            run(['git','worktree','remove','--force',str(wt)],ROOT,check=False)

if __name__=='__main__':raise SystemExit(main())
