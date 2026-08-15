#!/usr/bin/env python3
"""QURBATA Jilid 2 P004 V4 — 7 core rows + 1 dedicated enrichment row.

This redesign replaces the previous overlay capsule approach. P004 is a cumulative
page, so row 8 is reserved for micro-enrichment instead of forcing 32 practice
objects plus an extra block into the same page height.

Core typography remains 52 pt presentation / 39 pt practice. The lexical registry
remains unchanged for audit; this renderer intentionally uses the first 28 objects
(24 TRANSFER + first 4 MUROJAAH) on-page, while the remaining 4 review objects stay
in the registry for later cumulative reuse.
"""
from __future__ import annotations
import json,sys
from pathlib import Path
from playwright.async_api import async_playwright

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))

import render_qurbata_jilid2_p004_v1_kfgqpc_lexical as v1
import render_qurbata_jilid2_p001_v1 as p001

DEFAULT_P004_OUTPUT='dist/qurbata-print-ready/jilid-2/pages/P004'

# Use only seven 4-object rows on cumulative pages. Registry is preserved.
words=[r['word'] for r in v1.lex[:28]]
p001.P001_ROWS=[words[i:i+4] for i in range(0,28,4)]

p001.P001_CSS += r'''
.presentation-object{font-size:52pt!important;}
.j2-glyph{font-size:39pt!important;}
.j2-grid{height:134mm!important;flex:0 0 134mm!important;grid-template-rows:repeat(7,minmax(0,1fr))!important;row-gap:2.8mm!important;}
.cumulative-bottom-row{height:15mm!important;flex:0 0 15mm!important;margin:1.5mm 0 0!important;border-top:.28mm solid #111!important;padding-top:1mm!important;display:grid!important;grid-template-columns:1.45fr .8fr .75fr!important;gap:1.2mm!important;direction:ltr!important;box-sizing:border-box!important;overflow:hidden!important;}
.cumulative-bottom-row .micro{display:flex!important;flex-direction:column!important;align-items:center!important;justify-content:center!important;text-align:center!important;overflow:hidden!important;line-height:1!important;}
.cumulative-bottom-row .micro-label{font-family:Arial,sans-serif!important;font-size:6pt!important;font-weight:700!important;margin-bottom:.7mm!important;}
.cumulative-bottom-row .micro-ar{font-family:'KFGQPC Uthman Taha Naskh','Amiri Quran','Amiri',serif!important;font-size:14.5pt!important;direction:rtl!important;white-space:nowrap!important;}
.cumulative-bottom-row .micro-num{font-family:'KFGQPC Uthman Taha Naskh','Amiri Quran','Amiri',serif!important;font-size:17pt!important;direction:rtl!important;white-space:nowrap!important;}
'''

_original_build=p001.build_page_html

def build_p004_v4(debug:bool):
    h=_original_build(debug)
    row='''<section class="cumulative-bottom-row" aria-label="Kapsul Murojaah">
      <div class="micro"><div class="micro-label">NAMA HURUF</div><div class="micro-ar" lang="ar">بَاءٌ · تَاءٌ · ثَاءٌ · جِيمٌ · حَاءٌ · خَاءٌ · سِينٌ · شِينٌ</div></div>
      <div class="micro"><div class="micro-label">ANGKA ARAB</div><div class="micro-num" lang="ar">٠ · ١ · ٢ · ٣ · ٤ · ٥ · ٦ · ٧ · ٨ · ٩</div></div>
      <div class="micro"><div class="micro-label">PEMUTUS SAMBUNGAN</div><div class="micro-ar" lang="ar">ا · د · ذ · ر · ز · و</div></div>
    </section>'''
    candidates=['<footer', '<div class="footer', '<section class="footer']
    positions=[h.find(x) for x in candidates if h.find(x)>=0]
    if not positions: raise RuntimeError('P004_V4_FOOTER_ANCHOR_NOT_FOUND')
    pos=min(positions)
    return h[:pos]+row+h[pos:]

p001.build_page_html=build_p004_v4

async def render_p004_v4(h:Path,out:Path,debug:bool):
    report=out/'LAYOUT-OVERFLOW-REPORT-J2-P004-V4.json'
    png=out/'png'; png.mkdir(parents=True,exist_ok=True)
    async with async_playwright() as pw:
        browser=await pw.chromium.launch()
        page=await browser.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2)
        await page.goto(h.resolve().as_uri(),wait_until='networkidle')
        await page.evaluate('document.fonts.ready')
        count=await page.locator('.j2-object').count()
        if count!=28: raise RuntimeError(f'P004_V4_OBJECT_COUNT_INVALID actual={count} expected=28')
        if await page.locator('.cumulative-bottom-row .micro').count()!=3:
            raise RuntimeError('P004_V4_ENRICHMENT_COUNT_INVALID')
        metrics,layout_issues=await p001.fit_and_inspect(page)
        extra=await page.evaluate('''()=>{const e=document.querySelector('.cumulative-bottom-row'),f=document.querySelector('.footer'),p=document.querySelector('.page');const out=[];if(!e||!p)return [{kind:'ENRICHMENT_MISSING'}];const er=e.getBoundingClientRect(),pr=p.getBoundingClientRect();if(er.left<pr.left||er.right>pr.right||er.bottom>pr.bottom)out.push({kind:'ENRICHMENT_PAGE_OVERFLOW'});if(f){const fr=f.getBoundingClientRect();if(er.bottom>fr.top-2)out.push({kind:'ENRICHMENT_FOOTER_COLLISION',enrichmentBottom:er.bottom,footerTop:fr.top})}const objs=[...document.querySelectorAll('.j2-object')];if(objs.length){const lastBottom=Math.max(...objs.map(x=>x.getBoundingClientRect().bottom));if(lastBottom>er.top-4)out.push({kind:'ENRICHMENT_CORE_COLLISION',lastPracticeBottom:lastBottom,enrichmentTop:er.top})}return out}''')
        all_issues=[*layout_issues,*extra]
        report.write_text(json.dumps(all_issues,ensure_ascii=False,indent=2),encoding='utf-8')
        if all_issues:
            kinds={}
            for x in all_issues:kinds[x['kind']]=kinds.get(x['kind'],0)+1
            raise RuntimeError('P004_V4_LAYOUT_ISSUES='+str(len(all_issues))+' TYPES='+','.join(f'{k}:{v}' for k,v in sorted(kinds.items()))+f' REPORT={report}')
        await page.screenshot(path=str(png/'page-004-v4.png'),full_page=True)
        pdf=out/'QURBATA-JILID-2-P004-V4-CUMULATIVE-BOTTOMROW.pdf'
        try:
            await page.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'})
            pdf_mode='DIRECT_V4'
        except PermissionError:
            pdf=out/'QURBATA-JILID-2-P004-V4-CUMULATIVE-BOTTOMROW-LOCK-SAFE.pdf'
            await page.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'})
            pdf_mode='LOCK_FALLBACK_V4'
        await browser.close()
    return metrics,report,pdf,pdf_mode

p001.render=render_p004_v4

def main():
    if '--output-dir' not in sys.argv[1:]: sys.argv.extend(['--output-dir',DEFAULT_P004_OUTPUT])
    rc=v1.main()
    print('JILID2_P004_RENDERER_V4_CUMULATIVE_BOTTOMROW=PASS')
    print('PAGE=4')
    print('CORE_PRACTICE_ROWS=7')
    print('CORE_PRACTICE_OBJECTS=28')
    print('BOTTOM_ROW=DEDICATED_CUMULATIVE_ENRICHMENT')
    print('ENRICHMENT_CATEGORY=E01|E02|E06')
    print('ENRICHMENT_ITEM=LETTER_NAMES|ARABIC_INDIC_NUMERALS_0_9|NON_JOINERS')
    print('REGISTRY_OBJECTS=32_PRESERVED')
    print('ONPAGE_UNUSED_REGISTRY_OBJECTS=4_RESERVED_FOR_LATER_REVIEW')
    print('PRESENTATION_FONT_SIZE=52PT')
    print('PRACTICE_FONT_SIZE=39PT')
    print('STATUS=P004_CUMULATIVE_BOTTOMROW_CANDIDATE')
    return rc

if __name__=='__main__': raise SystemExit(main())
