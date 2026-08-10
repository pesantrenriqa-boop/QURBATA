#!/usr/bin/env python3
"""QURBATA Jilid 2 P001 V22 — lexical foundation candidate.

Keeps the V21 KFGQPC 42pt 4-column visual baseline, but:
- moves the practice block lower into previously unused lower whitespace;
- enlarges the presentation/title line to at least practice size;
- keeps rows 1-2 as the required two-letter acquisition ladder;
- replaces every 3-letter slot in rows 3-8 with a meaningful Arabic lexeme from
  the P001 lexical foundation registry;
- preserves the existing competency boundary: only ب ت ث as acquisition letters,
  with ا د ذ ر ز و as previously-known non-joiner/review letters.
"""
from __future__ import annotations
import csv
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))

import render_qurbata_jilid2_p001_v21_kfgqpc_4col_large as v21
import render_qurbata_jilid2_p001_v1 as p001

LEX=ROOT/'content/qwo/registry/JILID-2-P001-LEXICAL-FOUNDATION-V1.csv'


def load_lexical_rows():
    with LEX.open(encoding='utf-8-sig',newline='') as f:
        rows=list(csv.DictReader(f))
    if len(rows)!=24:
        raise ValueError(f'P001_LEXICAL_REGISTRY_COUNT_INVALID actual={len(rows)} expected=24')
    if any(r.get('lexical_status')!='VERIFIED' or r.get('competency_status')!='ALLOWED' for r in rows):
        raise ValueError('P001_LEXICAL_REGISTRY_NOT_FULLY_VERIFIED')
    return [r['word'] for r in rows]

lex=load_lexical_rows()

# Rows 1-2 remain the pedagogically required L2 ladder. Rows 3-8 are lexical L3.
p001.P001_ROWS=[
    ['بَتَ','تَبَ','بَثَ','ثَبَ'],
    ['تِثُ','ثُتِ','بِثَ','ثَبُ'],
    lex[0:4],
    lex[4:8],
    lex[8:12],
    lex[12:16],
    lex[16:20],
    lex[20:24],
]

# Use the lower whitespace instead of compressing the child-reading objects further.
# The presentation is now larger than the 42pt practice type.
p001.P001_CSS += r'''
.presentation{
  height:15mm;
  flex:0 0 15mm;
  margin:1.0mm 1.2mm 1.0mm;
}
.presentation-object{font-size:46pt;gap:1.15mm;line-height:.98}
.presentation-object .arrow{font-size:24pt}
.j2-grid{
  margin-top:3.8mm;
  height:149mm;
  flex:0 0 149mm;
  column-gap:.45mm;
  row-gap:2.35mm;
}
.j2-glyph{font-size:42pt;line-height:.96}
'''


def main():
    # Verify no lexical word leaks a joining family not yet acquired.
    banned=p001.P001_BANNED_JOINING
    leaks=[]
    for word in lex:
        hit=banned.intersection(word)
        if hit: leaks.append((word,''.join(sorted(hit))))
    if leaks:
        raise ValueError('P001_LEXICAL_COMPETENCY_LEAKAGE='+repr(leaks))

    rc=v21.main()
    print('JILID2_P001_RENDERER_V22_KFGQPC_LEXICAL=PASS')
    print('PRACTICE_FONT_SIZE=42PT')
    print('PRESENTATION_FONT_SIZE=46PT')
    print('PRACTICE_BLOCK_SHIFT_DOWN_MM=3.8')
    print('ROWS_1_2=L2_ACQUISITION_LADDER_PRESERVED')
    print('ROWS_3_8=LEXICAL_THREE_LETTER_WORDS')
    print('LEXICAL_OBJECTS=24')
    print('LEXICAL_REGISTRY=content/qwo/registry/JILID-2-P001-LEXICAL-FOUNDATION-V1.csv')
    print('LEXICAL_STATUS=VERIFIED')
    print('COMPETENCY_LEAKAGE=0')
    print('ARABIC_FONT_PRIMARY=KFGQPC Uthman Taha Naskh')
    print('STATUS=VISUAL_AND_LEXICAL_CANDIDATE_NOT_FROZEN')
    return rc

if __name__=='__main__': raise SystemExit(main())
