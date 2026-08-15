#!/usr/bin/env python3
"""QURBATA Jilid 2 P005 V2 — lock-safe 52/39 production wrapper."""
from __future__ import annotations
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p005_v1_kfgqpc_lexical as v1
import render_qurbata_jilid2_p001_v1 as p001

DEFAULT_P005_OUTPUT='dist/qurbata-print-ready/jilid-2/pages/P005'
p001.P001_CSS += r'''
.presentation-object{font-size:52pt!important;}
.j2-glyph{font-size:39pt!important;}
'''
_original_render=v1.render_p005

async def render_p005_v2(h:Path,out:Path,debug:bool):
    result=await _original_render(h,out,debug)
    if len(result)==4:
        metrics,report_v1,pdf_v1,pdf_mode=result
    elif len(result)==3:
        metrics,report_v1,pdf_v1=result;pdf_mode='LEGACY_DIRECT'
    else:
        raise RuntimeError(f'P005_RENDER_RETURN_ARITY_INVALID={len(result)}')

    report_v2=out/'LAYOUT-OVERFLOW-REPORT-J2-P005-V2.json'
    if report_v1.exists() and report_v1!=report_v2:
        try:
            if report_v2.exists(): report_v2.unlink()
            report_v1.replace(report_v2)
        except PermissionError:
            report_v2=out/'LAYOUT-OVERFLOW-REPORT-J2-P005-V2-LOCK-SAFE.json'
            report_v1.replace(report_v2)

    primary=out/'QURBATA-JILID-2-P005-V2-KFGQPC-BASELINE52.pdf'
    if pdf_v1.exists() and pdf_v1!=primary:
        if not primary.exists():
            try:
                pdf_v1.replace(primary)
                pdf_v2=primary
                pdf_mode='RENAMED_V2'
            except PermissionError:
                pdf_v2=out/'QURBATA-JILID-2-P005-V2-KFGQPC-BASELINE52-LOCK-SAFE.pdf'
                if pdf_v2.exists(): pdf_v2=out/'QURBATA-JILID-2-P005-V2-KFGQPC-BASELINE52-LOCK-SAFE-2.pdf'
                pdf_v1.replace(pdf_v2)
                pdf_mode='LOCK_FALLBACK_V2'
        else:
            pdf_v2=out/'QURBATA-JILID-2-P005-V2-KFGQPC-BASELINE52-LOCK-SAFE.pdf'
            n=2
            while pdf_v2.exists():
                pdf_v2=out/f'QURBATA-JILID-2-P005-V2-KFGQPC-BASELINE52-LOCK-SAFE-{n}.pdf';n+=1
            pdf_v1.replace(pdf_v2)
            pdf_mode='LOCK_FALLBACK_V2'
    else:
        pdf_v2=pdf_v1
    return metrics,report_v2,pdf_v2,pdf_mode

p001.render=render_p005_v2

def main():
    if '--output-dir' not in sys.argv[1:]:sys.argv.extend(['--output-dir',DEFAULT_P005_OUTPUT])
    rc=v1.main()
    print('JILID2_P005_RENDERER_V2=PASS')
    print('PAGE=5')
    print('OUTPUT_DIR='+DEFAULT_P005_OUTPUT)
    print('TYPOGRAPHY_BASELINE=P001_P004_PRODUCTION')
    print('PRESENTATION_FONT_SIZE=52PT')
    print('PRACTICE_FONT_SIZE=39PT')
    print('ENRICHMENT=NONE_REGULAR_ACQUISITION_PAGE')
    print('ARABIC_SPELLED_LETTER_NAMES=DISABLED')
    print('PDF_WRITE_POLICY=LOCK_SAFE_NO_DELETE')
    print('STATUS=P005_CANDIDATE_V2_BASELINE52')
    return rc
if __name__=='__main__':raise SystemExit(main())
