#!/usr/bin/env python3
"""Guard QURBATA Jilid 2 PDF production against silent regression."""
from __future__ import annotations
import csv, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
FREEZE=ROOT/'books/jilid-2/pdf-freeze'
BASELINE=FREEZE/'QJ2-PDF-VISUAL-BASELINE.json'
REGISTER=FREEZE/'QJ2-PDF-ARTIFACT-REGISTER.csv'

def fail(msg):
    raise SystemExit('QJ2_PDF_FREEZE_GUARD=FAIL\nREASON='+msg)

def main():
    if not BASELINE.is_file(): fail('BASELINE_MISSING')
    if not REGISTER.is_file(): fail('REGISTER_MISSING')
    b=json.loads(BASELINE.read_text(encoding='utf-8'))
    rules=b.get('rules',{})
    font=rules.get('arabic_practice_font',{})
    layout=rules.get('practice_layout',{})
    sukun=rules.get('sukun',{})
    presentation=rules.get('new_material_presentation',{})
    checks={
        'BASELINE_STATUS': b.get('status')=='FROZEN_BASELINE',
        'FONT_KFGQPC': 'KFGQPC' in font.get('family','').upper(),
        'LEGACY_AMIRI_BASE_FORBIDDEN': font.get('legacy_amiri_as_base_font')=='FORBIDDEN',
        'FINAL_FALLBACK_FORBIDDEN': font.get('fallback_font_for_final_pdf')=='FORBIDDEN',
        'PRESENTATION_ARROW_FROZEN': presentation.get('status')=='FROZEN' and presentation.get('must_not_be_removed') is True,
        'LAYOUT_4_OBJECTS': layout.get('two_letter_or_short_step')=='4 objects per row',
        'LAYOUT_3_OBJECTS': layout.get('three_letter_or_longer_step')=='3 objects per row',
        'VISIBLE_CELL_BORDER_FORBIDDEN': layout.get('visible_cell_border')=='FORBIDDEN',
        'VISIBLE_BOX_BACKGROUND_FORBIDDEN': layout.get('visible_box_background')=='FORBIDDEN',
        'SUKUN_V76': sukun.get('baseline_version')=='V7.6',
        'SUKUN_SHIFT': sukun.get('vertical_shift_font_units')==-1700,
        'SUKUN_CODEPOINT': sukun.get('render_codepoint')=='U+0652',
    }
    bad=[k for k,v in checks.items() if not v]
    if bad: fail('BASELINE_REGRESSION='+','.join(bad))
    with REGISTER.open(encoding='utf-8-sig',newline='') as f: rows=list(csv.DictReader(f))
    pages=[r.get('Page') for r in rows];expected=[f'P{n:03d}' for n in range(1,41)]
    if pages!=expected: fail('REGISTER_PAGE_SEQUENCE_INVALID')
    frozen=[r for r in rows if r.get('PDFStatus')=='FROZEN']
    for r in frozen:
        required=['SourcePath','RendererPath','RendererCommit','PDFFileName','PDF_SHA256','ApprovedDate']
        missing=[x for x in required if not (r.get(x) or '').strip()]
        if missing: fail(f'FROZEN_PAGE_METADATA_INCOMPLETE={r["Page"]}:'+','.join(missing))
    print('QJ2_PDF_FREEZE_GUARD=PASS')
    print('GLOBAL_VISUAL_BASELINE=FROZEN_V2')
    print('BASE_FONT=KFGQPC_UTHMAN_TAHA')
    print('FINAL_FONT_FALLBACK=FORBIDDEN')
    print('PRESENTATION_ARROW=FROZEN')
    print('LAYOUT=4_OBJECTS_L2|3_OBJECTS_L3')
    print('VISIBLE_BOXES=FORBIDDEN')
    print('SUKUN=V7.6|-1700')
    print(f'PAGE_REGISTER_ROWS={len(rows)}')
    print(f'FULLY_FROZEN_PDF_PAGES={len(frozen)}')
    print(f'RECOVERY_OR_REVIEW_PAGES={40-len(frozen)}')
    return 0

if __name__=='__main__': raise SystemExit(main())
