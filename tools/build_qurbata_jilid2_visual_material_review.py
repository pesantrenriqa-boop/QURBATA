#!/usr/bin/env python3
"""Build a review PDF from actual QURBATA Jilid 2 visual renderers.

This intentionally does NOT turn planning Markdown into book pages.
It renders only participant-facing visual material that has a real renderer/dataset.
Current verified visual coverage:
- P001-P020: foundation renderer v3 (actual 24-object practice pages)
- P021-P040: reported as NOT YET VISUAL-RENDERED by this audit builder

The output PDF therefore contains only real material pages; missing visual pages are
listed in a manifest, never replaced with documentation text.
"""
from __future__ import annotations
import argparse, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DEFAULT_OUT=ROOT/'dist/jilid-2-visual-material-review'
FOUNDATION_SCRIPT=ROOT/'tools/render_qurbata_jilid2_foundation_v3.py'
FOUNDATION_OUT=DEFAULT_OUT/'p001-p020'
FOUNDATION_PDF=FOUNDATION_OUT/'QURBATA-JILID-2-P001-P020-FOUNDATION-CANDIDATE-V1.pdf'


def run(cmd):
    p=subprocess.run(cmd,cwd=ROOT,text=True,encoding='utf-8',errors='replace')
    if p.returncode!=0: raise SystemExit(p.returncode)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output-dir',default=str(DEFAULT_OUT.relative_to(ROOT)));a=ap.parse_args()
    out=Path(a.output_dir);out=out if out.is_absolute() else ROOT/out;out.mkdir(parents=True,exist_ok=True)
    foundation_out=out/'p001-p020'
    run([sys.executable,str(FOUNDATION_SCRIPT),'--output-dir',str(foundation_out.relative_to(ROOT))])
    pdf=foundation_out/'QURBATA-JILID-2-P001-P020-FOUNDATION-CANDIDATE-V1.pdf'
    if not pdf.exists(): raise FileNotFoundError(pdf)
    manifest=out/'JILID-2-VISUAL-MATERIAL-COVERAGE.tsv'
    lines=['page\tvisual_status\tsource']
    for n in range(1,21): lines.append(f'P{n:03d}\tRENDERED_REAL_MATERIAL\trender_qurbata_jilid2_foundation_v3.py')
    for n in range(21,41): lines.append(f'P{n:03d}\tNO_VERIFIED_VISUAL_RENDERER_IN_CURRENT_PIPELINE\t')
    manifest.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print('JILID2_VISUAL_MATERIAL_REVIEW=PASS')
    print('REAL_VISUAL_PAGES=20')
    print('REAL_VISUAL_RANGE=P001-P020')
    print('NOT_SUBSTITUTED_WITH_MARKDOWN=P021-P040')
    print(f'MANIFEST={manifest.relative_to(ROOT)}')
    print(f'PDF={pdf.relative_to(ROOT)}')
    return 0
if __name__=='__main__':raise SystemExit(main())
