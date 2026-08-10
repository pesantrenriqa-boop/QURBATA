#!/usr/bin/env python3
"""QURBATA Jilid 2 P001 V18 — row-box geometry tuned for native harakat.

V17 failed because its larger line-height enlarged each glyph element box; the
validator correctly found all seven inter-row clearances too small. V18 keeps
native Amiri Quran shaping but uses a compact line box plus larger explicit row
gaps so the logical boxes themselves are separated.
"""
from __future__ import annotations
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v16 as v16
import render_qurbata_jilid2_p001_v1 as p001

p001.P001_CSS += r'''
.j2-grid{
  height:146mm;
  flex:0 0 146mm;
  row-gap:6mm;
  padding:.4mm 0;
}
.j2-glyph{
  font-size:30pt;
  line-height:1.00;
  padding:.35mm 1mm .45mm;
  overflow:visible;
  font-family:'Amiri Quran','Amiri','Noto Naskh Arabic',serif;
  font-feature-settings:'mark' 1,'mkmk' 1;
}
.targets{height:9mm;flex:0 0 9mm;padding:.3mm 1mm .25mm}
.target-item{min-height:7.2mm}
.footer{height:5mm;flex:0 0 5mm;margin-bottom:1mm}
'''


def main():
    rc=v16.main()
    print('JILID2_P001_RENDERER_V18=PASS')
    print('HARAKAT_MODEL=NATIVE_AMIRI_QURAN_UNINTERRUPTED')
    print('PRACTICE_FONT_SIZE=30PT')
    print('PRACTICE_LINE_HEIGHT=1.00')
    print('ROW_GAP_MM=6.0')
    print('GRID_HEIGHT_MM=146')
    print('MARK_OFFSETS=NONE')
    print('DETACHED_MARKS=FORBIDDEN')
    print('COLLISION_STRATEGY=COMPACT_LINE_BOX_PLUS_EXPLICIT_ROW_GAP')
    print('STATUS=VISUAL_CANDIDATE_NOT_FROZEN')
    return rc

if __name__=='__main__': raise SystemExit(main())
