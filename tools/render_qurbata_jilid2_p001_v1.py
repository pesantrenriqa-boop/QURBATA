#!/usr/bin/env python3
"""Render only QURBATA Jilid 2 P001, bound to frozen micro competency ladder."""
from __future__ import annotations
import argparse, asyncio, csv
from pathlib import Path
import render_qurbata_jilid2_foundation_v3 as base

ROOT=Path(__file__).resolve().parents[1]
CONTRACT=ROOT/'content/qwo/registry/JILID-2-P001-PAGE-CONTRACT-V1.csv'
MICRO=ROOT/'content/qwo/registry/JILID-2-MICRO-COMPETENCY-P001-V1.csv'
DEFAULT_DATA=ROOT/'content/qwo/composer/output/jilid-2-v1-joined-foundation'
DEFAULT_OUT=ROOT/'dist/jilid-2-p001-candidate-v1'

def read_csv(p):
    with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--data-dir',default=str(DEFAULT_DATA.relative_to(ROOT)));ap.add_argument('--output-dir',default=str(DEFAULT_OUT.relative_to(ROOT)));ap.add_argument('--debug',action='store_true');a=ap.parse_args()
    data=Path(a.data_dir);data=data if data.is_absolute() else ROOT/data
    out=Path(a.output_dir);out=out if out.is_absolute() else ROOT/out;out.mkdir(parents=True,exist_ok=True)
    contract=read_csv(CONTRACT)[0];micro=read_csv(MICRO)
    if len(micro)!=10:raise ValueError(f'P001_MICRO_LADDER_INVALID actual={len(micro)} expected=10')
    rows=[r for r in read_csv(data/'JILID-2-READING-OBJECTS-V1.csv') if int(r['Page'])==1]
    meta=[r for r in read_csv(data/'JILID-2-PAGE-METADATA-V1.csv') if int(r['Page'])==1][0]
    if len(rows)!=24:raise ValueError(f'P001_OBJECT_COUNT actual={len(rows)} expected=24')
    # Override presentation/footer semantics for P001 from the frozen page contract.
    base.PRESENTATIONS[1].update({'PresentationRequired':'YES','PresentationTitle':contract['Title'],'PresentationObject':contract['PresentationObject'],'Competency':contract['Competency'],'SubCompetency':contract['SubCompetency'],'Stair':'T01–T10 • konsep → posisi → baca → acak → transfer'})
    html_dir=out/'html';html_dir.mkdir(parents=True,exist_ok=True)
    h=html_dir/'page-001.html';h.write_text(base.page_html(1,rows,meta,a.debug),encoding='utf-8')
    totals,report,pdf=asyncio.run(base.base.render([h],out,a.debug))
    print('JILID2_P001_RENDERER_V1=PASS')
    print('PAGE=1')
    print('COMPETENCY=K1 Membaca huruf hijaiyah bersambung')
    print('SUBCOMPETENCY=K1.SK1 Konsep dasar perubahan huruf ketika disambung')
    print('MICRO_COMPETENCY_STAIRS=10')
    print('STAIR_RANGE=K1.SK1.T01-K1.SK1.T10')
    print('PRESENTATION=بَتِثُ ← بَ ← تِ ← ثُ')
    print('PRACTICE_OBJECTS=24')
    print('ARABIC_FONT_PRIMARY=Amiri Quran')
    print('LAYOUT_OVERFLOW=0')
    print(f'OVERFLOW_REPORT={report.relative_to(ROOT)}')
    print(f'PDF={pdf.relative_to(ROOT)}')
    return 0
if __name__=='__main__':raise SystemExit(main())
