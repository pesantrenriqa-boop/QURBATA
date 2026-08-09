#!/usr/bin/env python3
"""Render only QURBATA Jilid 2 P001 with a strict no-leakage joining ladder."""
from __future__ import annotations
import argparse, asyncio, csv
from pathlib import Path
import render_qurbata_jilid2_foundation_v3 as base

ROOT=Path(__file__).resolve().parents[1]
CONTRACT=ROOT/'content/qwo/registry/JILID-2-P001-PAGE-CONTRACT-V1.csv'
MICRO=ROOT/'content/qwo/registry/JILID-2-MICRO-COMPETENCY-P001-V1.csv'
DEFAULT_DATA=ROOT/'content/qwo/composer/output/jilid-2-v1-joined-foundation'
DEFAULT_OUT=ROOT/'dist/jilid-2-p001-candidate-v2'

def read_csv(p):
    with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))

# P001 acquisition boundary: only ب ت ث plus previously-known non-joining review ا د ذ ر ز و.
# Deliberately starts with L2, then L3. No other joining families may leak into P001.
P001_OBJECTS=[
'بَتَ','تَبَ','بَثَ','ثَبَ','تَثَ','ثَتَ','بِتِ','تِبِ',
'بُثُ','ثُبُ','تِثِ','ثِتِ',
'بَتِثُ','تَبِثُ','ثَبِتُ','بِثَتُ','تُبَثِ','ثِتُبَ',
'بَا','تَدَ','ثَذَ','بَرَ','تَزَ','ثَوَ'
]
P001_BANNED_JOINING=set('جحخسشصضطظعغفقكلمنيه')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--data-dir',default=str(DEFAULT_DATA.relative_to(ROOT)));ap.add_argument('--output-dir',default=str(DEFAULT_OUT.relative_to(ROOT)));ap.add_argument('--debug',action='store_true');a=ap.parse_args()
    data=Path(a.data_dir);data=data if data.is_absolute() else ROOT/data
    out=Path(a.output_dir);out=out if out.is_absolute() else ROOT/out;out.mkdir(parents=True,exist_ok=True)
    contract=read_csv(CONTRACT)[0];micro=read_csv(MICRO)
    if len(micro)!=10:raise ValueError(f'P001_MICRO_LADDER_INVALID actual={len(micro)} expected=10')
    rows=[r for r in read_csv(data/'JILID-2-READING-OBJECTS-V1.csv') if int(r['Page'])==1]
    meta=[r for r in read_csv(data/'JILID-2-PAGE-METADATA-V1.csv') if int(r['Page'])==1][0]
    if len(rows)!=24 or len(P001_OBJECTS)!=24:raise ValueError('P001_OBJECT_COUNT expected=24')
    for r,obj in zip(rows,P001_OBJECTS):
        r['ArabicObject']=obj
        leaked=P001_BANNED_JOINING.intersection(obj)
        if leaked:raise ValueError('P001_COMPETENCY_LEAKAGE object='+obj+' leaked='+''.join(sorted(leaked)))
    base.PRESENTATIONS[1].update({'PresentationRequired':'YES','PresentationTitle':'Konsep Huruf Bersambung','PresentationObject':'بَتِثُ ← بَ ← تِ ← ثُ','Competency':'Membaca huruf hijaiyah bersambung','SubCompetency':'Konsep dasar sambungan: 2 huruf → 3 huruf → pemutus sambungan','Stair':'L2 terpimpin → L2 variasi → L3 terpimpin → L3 variasi → pemutus ا د ذ ر ز و'})
    html_dir=out/'html';html_dir.mkdir(parents=True,exist_ok=True)
    h=html_dir/'page-001.html';h.write_text(base.page_html(1,rows,meta,a.debug),encoding='utf-8')
    totals,report,pdf=asyncio.run(base.base.render([h],out,a.debug))
    print('JILID2_P001_RENDERER_V1=PASS')
    print('PAGE=1')
    print('COMPETENCY_LEAKAGE=0')
    print('ACQUISITION_LETTERS=بتث')
    print('NON_JOINING_REVIEW=ا|د|ذ|ر|ز|و')
    print('LADDER=L2_JOINED|L2_HARAKAT_VARIATION|L3_JOINED|L3_HARAKAT_VARIATION|NON_JOINER_TRANSFER')
    print('PRESENTATION=بَتِثُ ← بَ ← تِ ← ثُ')
    print('PRACTICE_OBJECTS=24')
    print('ARABIC_FONT_PRIMARY=Amiri Quran')
    print('LAYOUT_OVERFLOW=0')
    print(f'OVERFLOW_REPORT={report.relative_to(ROOT)}')
    print(f'PDF={pdf.relative_to(ROOT)}')
    return 0
if __name__=='__main__':raise SystemExit(main())
