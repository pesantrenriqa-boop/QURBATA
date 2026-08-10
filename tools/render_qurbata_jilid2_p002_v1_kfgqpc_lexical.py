#!/usr/bin/env python3
"""QURBATA Jilid 2 P002 — competency-led lexical page.

P002 continues K1 with the new joining family ج ح خ.  The page explicitly carries
Competency, Unit Competency, Unit Murojaah and Stair metadata.  It preserves the
approved P001/V22 KFGQPC visual direction: 42pt practice, 46pt presentation,
4 columns x 8 rows, native GPOS harakat, compact spacing and lexical examples.
"""
from __future__ import annotations
import asyncio,csv,json,sys
from pathlib import Path
from playwright.async_api import async_playwright

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))

import render_qurbata_jilid2_p001_v22_kfgqpc_lexical as v22
import render_qurbata_jilid2_p001_v1 as p001

MAP=ROOT/'content/qwo/registry/JILID-2-P002-COMPETENCY-MAP-V1.csv'
MICRO=ROOT/'content/qwo/registry/JILID-2-MICRO-COMPETENCY-P002-V1.csv'
LEX=ROOT/'content/qwo/registry/JILID-2-P002-LEXICAL-FOUNDATION-V1.csv'

with MAP.open(encoding='utf-8-sig',newline='') as f: meta=next(csv.DictReader(f))
with MICRO.open(encoding='utf-8-sig',newline='') as f: stairs=list(csv.DictReader(f))
with LEX.open(encoding='utf-8-sig',newline='') as f: lex=list(csv.DictReader(f))
if len(stairs)!=10: raise ValueError('P002_MICRO_STAIRS_INVALID')
if len(lex)!=32: raise ValueError('P002_LEXICAL_COUNT_INVALID')
if any(r['competency_status']!='ALLOWED' for r in lex): raise ValueError('P002_LEXICAL_COMPETENCY_NOT_ALLOWED')

# Bind base renderer validation to P002 registry.
p001.MICRO=MICRO
# New acquisition family is allowed; later joining families remain forbidden.
p001.P001_BANNED_JOINING=set('سشصضطظعغفقكلمنيه')

# 8 rows x 4 objects. Rows 1-6 current lexical acquisition, rows 7-8 cumulative review.
words=[r['word'] for r in lex]
p001.P001_ROWS=[words[i:i+4] for i in range(0,32,4)]

# Preserve approved V22 geometry, only page-specific presentation metadata changes.
p001.P001_CSS += r'''
.presentation-object{font-size:46pt}
.j2-glyph{font-size:42pt}
'''

_original_build=p001.build_page_html

def build_p002(debug:bool):
    h=_original_build(debug)
    h=h.replace('<div class="page-number">01</div>','<div class="page-number">02</div>',1)
    start=h.index('<section class="presentation">')
    end=h.index('</section>',start)+len('</section>')
    pres=f'''<section class="presentation"><div class="presentation-object-wrap"><div class="presentation-object"><span class="arabic-part" lang="ar">{p001.arabic_html('جَحِخُ')}</span><span class="arrow">←</span><span class="arabic-part" lang="ar">{p001.arabic_html('خُ')}</span><span class="arrow">←</span><span class="arabic-part" lang="ar">{p001.arabic_html('حِ')}</span><span class="arrow">←</span><span class="arabic-part" lang="ar">{p001.arabic_html('جَ')}</span></div></div></section>'''
    h=h[:start]+pres+h[end:]
    ts=h.index('<section class="targets">')
    te=h.index('</section>',ts)+len('</section>')
    targets=f'''<section class="targets"><div class="target-item"><span>Kompetensi</span><strong>{meta['CompetencyCode']} — {meta['Competency']}</strong></div><div class="target-item"><span>Unit Kompetensi</span><strong>{meta['UnitCompetencyCode']} — {meta['UnitCompetency']}</strong></div><div class="target-item"><span>Unit Murojaah</span><strong>{meta['UnitMurojaahCode']} — {meta['UnitMurojaah']}</strong></div><div class="target-item"><span>Tangga</span><strong>{stairs[0]['StairCode']}–{stairs[-1]['StairCode']}</strong></div></section>'''
    return h[:ts]+targets+h[te:]

p001.build_page_html=build_p002

async def render_p002(h:Path,out:Path,debug:bool):
    report=out/'LAYOUT-OVERFLOW-REPORT-J2-P002-V1.json'
    png=out/'png';png.mkdir(parents=True,exist_ok=True)
    async with async_playwright() as pw:
        browser=await pw.chromium.launch()
        page=await browser.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2)
        await page.goto(h.resolve().as_uri(),wait_until='networkidle');await page.evaluate('document.fonts.ready')
        count=await page.locator('.j2-object').count()
        if count!=32: raise RuntimeError(f'P002_OBJECT_COUNT_INVALID actual={count} expected=32')
        metrics,issues=await p001.fit_and_inspect(page)
        report.write_text(json.dumps(issues,ensure_ascii=False,indent=2),encoding='utf-8')
        if issues:
            kinds={}
            for x in issues:kinds[x['kind']]=kinds.get(x['kind'],0)+1
            raise RuntimeError('P002_LAYOUT_ISSUES='+str(len(issues))+' TYPES='+','.join(f'{k}:{v}' for k,v in sorted(kinds.items()))+f' REPORT={report}')
        await page.screenshot(path=str(png/'page-002.png'),full_page=True)
        pdf=out/'QURBATA-JILID-2-P002-V1-KFGQPC-LEXICAL.pdf'
        await page.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'})
        await browser.close()
    return metrics,report,pdf

p001.render=render_p002

def main():
    # Explicit competency leakage check before render.
    leaks=[]
    for r in lex:
        hit=p001.P001_BANNED_JOINING.intersection(r['word'])
        if hit: leaks.append((r['word'],''.join(sorted(hit))))
    if leaks: raise ValueError('P002_COMPETENCY_LEAKAGE='+repr(leaks))
    rc=v22.main()
    print('JILID2_P002_RENDERER_V1=PASS')
    print(f"PAGE=2")
    print(f"COMPETENCY={meta['CompetencyCode']}|{meta['Competency']}")
    print(f"UNIT_COMPETENCY={meta['UnitCompetencyCode']}|{meta['UnitCompetency']}")
    print(f"SUBCOMPETENCY={meta['SubCompetencyCode']}|{meta['SubCompetency']}")
    print(f"UNIT_MUROJAAH={meta['UnitMurojaahCode']}|{meta['UnitMurojaah']}")
    print('MICRO_COMPETENCY_STAIRS=10')
    print(f"STAIR_RANGE={stairs[0]['StairCode']}-{stairs[-1]['StairCode']}")
    print('ACQUISITION_LETTERS=ج|ح|خ')
    print('REVIEW_LETTERS=ب|ت|ث|ا|د|ذ|ر|ز|و')
    print('PRACTICE_OBJECTS=32')
    print('CURRENT_LEXICAL_OBJECTS=24')
    print('MUROJAAH_LEXICAL_OBJECTS=8')
    print('ARABIC_FONT_PRIMARY=KFGQPC Uthman Taha Naskh')
    print('PRACTICE_FONT_SIZE=42PT')
    print('PRESENTATION_FONT_SIZE=46PT')
    print('COMPETENCY_LEAKAGE=0')
    print('LEXICAL_STATUS=CURATED_PENDING_FINAL_VALIDATION')
    print('STATUS=P002_CANDIDATE_NOT_FROZEN')
    return rc

if __name__=='__main__': raise SystemExit(main())
