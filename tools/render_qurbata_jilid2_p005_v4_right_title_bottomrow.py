#!/usr/bin/env python3
"""QURBATA Jilid 2 P005 V4 — right-anchored acquisition title + native row-8 enrichment.

Visual title is forced from the RIGHT edge as:
    ص ← صَبَرَ    ض ← ضَرَبَ
Row 8 is reserved for E04 letter-form awareness (initial–medial–final) for ص ض,
following the staged Iqro-style recognition of connected shapes. No Arabic
spelled-out letter names are used. Registry remains 32 items; 28 appear as core
practice on this page, with 4 review items reserved for subsequent cumulative use.
"""
from __future__ import annotations
import json,sys
from pathlib import Path
from playwright.async_api import async_playwright

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))

import render_qurbata_jilid2_p005_v1_kfgqpc_lexical as v1
import render_qurbata_jilid2_p001_v1 as p001

DEFAULT_P005_OUTPUT='dist/qurbata-print-ready/jilid-2/pages/P005'

# 7 rows core practice; row 8 becomes a native enrichment row.
words=[r['word'] for r in v1.lex[:28]]
p001.P001_ROWS=[words[i:i+4] for i in range(0,28,4)]

p001.P001_CSS += r'''
.presentation-object{
  font-size:52pt!important;
  direction:ltr!important;
  flex-direction:row-reverse!important;
  unicode-bidi:isolate!important;
}
.presentation-object .arabic-part{direction:rtl!important;unicode-bidi:isolate!important;}
.presentation-object .arrow{direction:ltr!important;unicode-bidi:isolate!important;}
.j2-glyph{font-size:39pt!important;}
.p005-title-spacer{display:inline-block;width:8mm;flex:0 0 8mm;}
.j2-grid{grid-template-rows:repeat(8,minmax(0,1fr))!important;}
.p005-enrichment-row{
  grid-column:1 / -1!important;grid-row:8!important;
  min-width:0!important;min-height:0!important;
  align-self:stretch!important;justify-self:stretch!important;
  display:grid!important;grid-template-columns:1fr 1fr!important;
  gap:3mm!important;direction:rtl!important;
  border-top:.28mm solid #111!important;
  padding:.45mm 1.2mm 0!important;box-sizing:border-box!important;
  overflow:hidden!important;background:#fff!important;
}
.p005-enrichment-row .form-group{display:flex!important;align-items:center!important;justify-content:center!important;gap:2mm!important;min-width:0!important;overflow:hidden!important;}
.p005-enrichment-row .form-label{font-family:Arial,sans-serif!important;font-size:5.5pt!important;font-weight:700!important;white-space:nowrap!important;direction:ltr!important;}
.p005-enrichment-row .forms{font-family:'KFGQPC Uthman Taha Naskh','Amiri Quran','Amiri',serif!important;font-size:21pt!important;line-height:1!important;direction:rtl!important;white-space:nowrap!important;}
'''

_base_build=p001.build_page_html

def build_p005_v4(debug:bool):
    h=_base_build(debug)
    # Force title source order; row-reverse makes first item visually rightmost.
    start=h.index('<section class="presentation">')
    end=h.index('</section>',start)+len('</section>')
    pres=f'''<section class="presentation"><div class="presentation-object-wrap"><div class="presentation-object" dir="ltr">
      <span class="arabic-part" lang="ar" dir="rtl">{p001.arabic_html('ص')}</span>
      <span class="arrow" dir="ltr">←</span>
      <span class="arabic-part" lang="ar" dir="rtl">{p001.arabic_html('صَبَرَ')}</span>
      <span class="p005-title-spacer"></span>
      <span class="arabic-part" lang="ar" dir="rtl">{p001.arabic_html('ض')}</span>
      <span class="arrow" dir="ltr">←</span>
      <span class="arabic-part" lang="ar" dir="rtl">{p001.arabic_html('ضَرَبَ')}</span>
    </div></div></section>'''
    h=h[:start]+pres+h[end:]

    enrichment='''<div class="p005-enrichment-row" data-enrichment-row="8" aria-label="Bentuk huruf awal tengah akhir">
      <div class="form-group"><span class="form-label">BENTUK ص</span><span class="forms" lang="ar">صـ · ـصـ · ـص</span></div>
      <div class="form-group"><span class="form-label">BENTUK ض</span><span class="forms" lang="ar">ضـ · ـضـ · ـض</span></div>
    </div>'''
    gs=h.find('<section class="j2-grid">')
    if gs<0: raise RuntimeError('P005_V4_GRID_START_NOT_FOUND')
    ge=h.find('</section>',gs)
    if ge<0: raise RuntimeError('P005_V4_GRID_END_NOT_FOUND')
    return h[:ge]+enrichment+h[ge:]

p001.build_page_html=build_p005_v4

async def render_p005_v4(h:Path,out:Path,debug:bool):
    report=out/'LAYOUT-OVERFLOW-REPORT-J2-P005-V4.json'
    png=out/'png';png.mkdir(parents=True,exist_ok=True)
    async with async_playwright() as pw:
        browser=await pw.chromium.launch()
        page=await browser.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2)
        await page.goto(h.resolve().as_uri(),wait_until='networkidle')
        await page.evaluate('document.fonts.ready')
        count=await page.locator('.j2-object').count()
        if count!=28: raise RuntimeError(f'P005_V4_OBJECT_COUNT_INVALID actual={count} expected=28')
        if await page.locator('.p005-enrichment-row .form-group').count()!=2:
            raise RuntimeError('P005_V4_ENRICHMENT_COUNT_INVALID')
        metrics,layout_issues=await p001.fit_and_inspect(page)
        extra=await page.evaluate('''()=>{
          const g=document.querySelector('.j2-grid'),e=document.querySelector('.p005-enrichment-row'),f=document.querySelector('.footer');
          const out=[];if(!g||!e)return [{kind:'P005_ENRICHMENT_MISSING'}];
          const gr=g.getBoundingClientRect(),er=e.getBoundingClientRect();
          if(er.left<gr.left-1||er.right>gr.right+1||er.top<gr.top-1||er.bottom>gr.bottom+1)out.push({kind:'P005_ENRICHMENT_OUTSIDE_GRID'});
          const objs=[...document.querySelectorAll('.j2-object')];if(objs.length){const lastBottom=Math.max(...objs.map(x=>x.getBoundingClientRect().bottom));if(lastBottom>er.top-4)out.push({kind:'P005_ROW7_ROW8_CLEARANCE_TOO_SMALL',clearance:er.top-lastBottom,required:4});}
          if(f){const fr=f.getBoundingClientRect();if(er.bottom>fr.top-2)out.push({kind:'P005_ENRICHMENT_FOOTER_COLLISION'});}
          return out;
        }''')
        all_issues=[*layout_issues,*extra]
        report.write_text(json.dumps(all_issues,ensure_ascii=False,indent=2),encoding='utf-8')
        if all_issues:
            kinds={}
            for x in all_issues:kinds[x['kind']]=kinds.get(x['kind'],0)+1
            raise RuntimeError('P005_V4_LAYOUT_ISSUES='+str(len(all_issues))+' TYPES='+','.join(f'{k}:{v}' for k,v in sorted(kinds.items()))+f' REPORT={report}')
        await page.screenshot(path=str(png/'page-005-v4.png'),full_page=True)
        primary=out/'QURBATA-JILID-2-P005-V4-RIGHT-TITLE-BOTTOMROW.pdf'
        try:
            await page.pdf(path=str(primary),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});pdf=primary;pdf_mode='DIRECT_V4'
        except PermissionError:
            pdf=out/'QURBATA-JILID-2-P005-V4-RIGHT-TITLE-BOTTOMROW-LOCK-SAFE.pdf'
            await page.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});pdf_mode='LOCK_FALLBACK_V4'
        await browser.close()
    return metrics,report,pdf,pdf_mode

p001.render=render_p005_v4

def main():
    if '--output-dir' not in sys.argv[1:]:sys.argv.extend(['--output-dir',DEFAULT_P005_OUTPUT])
    rc=v1.main()
    print('JILID2_P005_RENDERER_V4_RIGHT_TITLE_BOTTOMROW=PASS')
    print('PAGE=5')
    print('TITLE_VISUAL_RIGHT_TO_LEFT=ص←صَبَرَ|ض←ضَرَبَ')
    print('RIGHTMOST_TITLE_OBJECT=ص')
    print('CORE_PRACTICE_ROWS=7')
    print('CORE_PRACTICE_OBJECTS=28')
    print('ENRICHMENT_GRID_ROW=8_NATIVE')
    print('ENRICHMENT_CATEGORY=E04')
    print('ENRICHMENT_ITEM=CONNECTED_FORMS_INITIAL_MEDIAL_FINAL_ص_ض')
    print('ARABIC_SPELLED_LETTER_NAMES=DISABLED')
    print('REGISTRY_OBJECTS=32_PRESERVED')
    print('PRESENTATION_FONT_SIZE=52PT')
    print('PRACTICE_FONT_SIZE=39PT')
    print('OUTPUT_DIR='+DEFAULT_P005_OUTPUT)
    return rc

if __name__=='__main__':raise SystemExit(main())
