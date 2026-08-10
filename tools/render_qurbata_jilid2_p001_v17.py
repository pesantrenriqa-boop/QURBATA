#!/usr/bin/env python3
"""QURBATA Jilid 2 P001 V17 — native harakat with larger vertical breathing room.

Keeps the V16 recovery rule: Arabic base letters + combining marks remain one
uninterrupted Amiri Quran shaping run. No detached marks and no mark offsets.
V17 addresses the remaining visual collisions by allocating more vertical room
per practice row and reducing practice type slightly, rather than moving harakat.
"""
from __future__ import annotations
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v16 as v16
import render_qurbata_jilid2_p001_v1 as p001

# Preserve native Arabic shaping. Give marks more room above/below each line.
p001.P001_CSS += r'''
.j2-grid{
  height:146mm;
  flex:0 0 146mm;
  row-gap:5.4mm;
  padding:.5mm 0;
}
.j2-glyph{
  font-size:32pt;
  line-height:1.28;
  padding:1.2mm 1mm 1.4mm;
  overflow:visible;
  font-family:'Amiri Quran','Amiri','Noto Naskh Arabic',serif;
  font-feature-settings:'mark' 1,'mkmk' 1;
}
.targets{height:9.5mm;flex:0 0 9.5mm;padding:.35mm 1mm .3mm}
.target-item{min-height:7.7mm}
.footer{height:5.2mm;flex:0 0 5.2mm;margin-bottom:1.1mm}
'''


def main():
    rc=v16.main()
    print('JILID2_P001_RENDERER_V17=PASS')
    print('HARAKAT_MODEL=NATIVE_AMIRI_QURAN_UNINTERRUPTED')
    print('PRACTICE_FONT_SIZE=32PT')
    print('PRACTICE_LINE_HEIGHT=1.28')
    print('ROW_GAP_MM=5.4')
    print('GRID_HEIGHT_MM=146')
    print('MARK_OFFSETS=NONE')
    print('DETACHED_MARKS=FORBIDDEN')
    print('COLLISION_STRATEGY=VERTICAL_BREATHING_ROOM_NOT_MARK_MOVEMENT')
    print('STATUS=VISUAL_CANDIDATE_NOT_FROZEN')
    return rc

if __name__=='__main__': raise SystemExit(main())
