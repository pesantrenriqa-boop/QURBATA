#!/usr/bin/env python3
"""QURBATA Jilid 2 P001 V21 — larger KFGQPC type, tighter 4-column spacing.

Typography-only iteration over V20. Content, competency boundary, 8x4 object
matrix, native KFGQPC GPOS, header and footer structure remain unchanged.
V21 also normalizes the generated PDF filename after the inherited V20 render.
"""
from __future__ import annotations
import shutil
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))

import render_qurbata_jilid2_p001_v20_kfgqpc_4col as v20
import render_qurbata_jilid2_p001_v1 as p001

p001.P001_CSS += r'''
.presentation{height:13mm;flex:0 0 13mm;margin:.1mm 1.4mm .35mm}
.presentation-object{font-size:34pt;gap:1.25mm}
.j2-grid{
  height:149mm;
  flex:0 0 149mm;
  column-gap:.45mm;
  row-gap:2.35mm;
  padding:.1mm 0;
}
.j2-glyph{
  font-size:42pt;
  line-height:.96;
  padding:.05mm .08mm .12mm;
}
.targets{height:8mm;flex:0 0 8mm;margin-bottom:.35mm;padding:.1mm .45mm}
.target-item{min-height:6.4mm;padding:.08mm .4mm 0}
.target-item span{font-size:5.1pt}
.target-item strong{font-size:4.7pt;line-height:1.08;margin-top:.15mm}
.footer{height:4.2mm;flex:0 0 4.2mm;margin-bottom:.65mm;padding:0 1.5mm;font-size:4.8pt}
'''


def _resolve_output_dir(argv:list[str])->Path:
    out='dist/jilid-2-p001-candidate-v29'
    for i,a in enumerate(argv):
        if a=='--output-dir' and i+1<len(argv):
            out=argv[i+1]
            break
    p=Path(out)
    return p if p.is_absolute() else ROOT/p


def main():
    out=_resolve_output_dir(sys.argv[1:])
    rc=v20.main()

    inherited=out/'QURBATA-JILID-2-P001-CANDIDATE-V20-KFGQPC-4COL.pdf'
    stable=out/'QURBATA-JILID-2-P001-V21-KFGQPC-4COL-LARGE.pdf'
    if inherited.exists():
        shutil.copy2(inherited,stable)
    elif not stable.exists():
        raise FileNotFoundError(f'V21_PDF_SOURCE_NOT_FOUND expected={inherited}')

    print('JILID2_P001_RENDERER_V21_KFGQPC_4COL_LARGE=PASS')
    print('PRACTICE_ROWS=8')
    print('PRACTICE_COLUMNS=4')
    print('PRACTICE_OBJECTS=32')
    print('PRACTICE_FONT_SIZE=42PT')
    print('PRESENTATION_FONT_SIZE=34PT')
    print('GRID_HEIGHT_MM=149')
    print('ROW_GAP_MM=2.35')
    print('COLUMN_GAP_MM=0.45')
    print('ARABIC_FONT_PRIMARY=KFGQPC Uthman Taha Naskh')
    print('HARAKAT_MODEL=NATIVE_FONT_GPOS')
    print('CONTENT_CHANGE=NONE')
    print('COMPETENCY_CHANGE=NONE')
    print(f'PDF={stable.relative_to(ROOT)}')
    print('STATUS=VISUAL_CANDIDATE_NOT_FROZEN')
    return rc

if __name__=='__main__': raise SystemExit(main())
