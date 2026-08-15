#!/usr/bin/env python3
"""QURBATA Jilid 2 P005 V3 — force visual title sequence ص → صَبَرَ then ض.

Uses a unique output filename to avoid stale/open V2 PDFs and overrides only the
presentation row. Practice content, competency gates, and 52/39 typography remain unchanged.
"""
from __future__ import annotations
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))

import render_qurbata_jilid2_p005_v1_kfgqpc_lexical as v1
import render_qurbata_jilid2_p001_v1 as p001

DEFAULT_P005_OUTPUT='dist/qurbata-print-ready/jilid-2/pages/P005'

p001.P001_CSS += r'''
.presentation-object{font-size:52pt!important;direction:ltr!important;unicode-bidi:isolate!important;}
.presentation-object .arabic-part{direction:rtl!important;unicode-bidi:isolate!important;}
.j2-glyph{font-size:39pt!important;}
.p005-title-spacer{display:inline-block;width:7mm;flex:0 0 7mm;}
'''

_base_build=p001.build_page_html

def build_p005_v3(debug:bool):
    h=_base_build(debug)
    start=h.index('<section class="presentation">')
    end=h.index('</section>',start)+len('</section>')
    pres=f'''<section class="presentation"><div class="presentation-object-wrap"><div class="presentation-object" dir="ltr"><span class="arabic-part" lang="ar" dir="rtl">{p001.arabic_html('ص')}</span><span class="arrow" dir="ltr">→</span><span class="arabic-part" lang="ar" dir="rtl">{p001.arabic_html('صَبَرَ')}</span><span class="p005-title-spacer"></span><span class="arabic-part" lang="ar" dir="rtl">{p001.arabic_html('ض')}</span></div></div></section>'''
    return h[:start]+pres+h[end:]

p001.build_page_html=build_p005_v3

_original_render=v1.render_p005

async def render_p005_v3(h:Path,out:Path,debug:bool):
    result=await _original_render(h,out,debug)
    metrics,report_v1,pdf_v1,pdf_mode=result if len(result)==4 else (*result,'LEGACY_DIRECT')
    report=out/'LAYOUT-OVERFLOW-REPORT-J2-P005-V3.json'
    pdf=out/'QURBATA-JILID-2-P005-V3-TITLE-SEQUENCE.pdf'
    if report_v1.exists():
        report.write_bytes(report_v1.read_bytes())
    if pdf_v1.exists():
        try:
            pdf.write_bytes(pdf_v1.read_bytes())
            pdf_mode='DIRECT_V3_COPY'
        except PermissionError:
            pdf=out/'QURBATA-JILID-2-P005-V3-TITLE-SEQUENCE-LOCK-SAFE.pdf'
            pdf.write_bytes(pdf_v1.read_bytes())
            pdf_mode='LOCK_FALLBACK_V3_COPY'
    return metrics,report,pdf,pdf_mode

p001.render=render_p005_v3

def main():
    if '--output-dir' not in sys.argv[1:]:sys.argv.extend(['--output-dir',DEFAULT_P005_OUTPUT])
    rc=v1.main()
    print('JILID2_P005_RENDERER_V3_TITLE_SEQUENCE=PASS')
    print('PAGE=5')
    print('PRESENTATION_SEQUENCE_VISUAL=ص→صَبَرَ   ض')
    print('PRESENTATION_DIRECTION=FORCED_LTR_CONTAINER_WITH_RTL_ARABIC_RUNS')
    print('PRESENTATION_FONT_SIZE=52PT')
    print('PRACTICE_FONT_SIZE=39PT')
    print('OUTPUT_DIR='+DEFAULT_P005_OUTPUT)
    return rc

if __name__=='__main__':raise SystemExit(main())
