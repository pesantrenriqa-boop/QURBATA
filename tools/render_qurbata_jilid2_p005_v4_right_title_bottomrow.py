#!/usr/bin/env python3
"""QURBATA Jilid 2 P005 V4 — right-anchored title + continued enrichment block.

Visual title is forced from the RIGHT edge as:
    ص ← صَبَرَ    ض ← ضَرَبَ
Presentation typography is aligned to the 39 pt practice baseline. Row 8 continues
the active enrichment block from P004; Arabic-Indic numerals are given safe
horizontal/vertical breathing room so edge glyphs are never clipped.
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

words=[r['word'] for r in v1.lex[:28]]
p001.P001_ROWS=[words[i:i+4] for i in range(0,28,4)]

p001.P001_CSS += r'''
.presentation-object{font-size:39pt!important;direction:ltr!important;flex-direction:row-reverse!important;unicode-bidi:isolate!important;}
.presentation-object .arabic-part{direction:rtl!important;unicode-bidi:isolate!important;line-height:1.12!important;padding:.35mm .25mm!important;}
.presentation-object .arrow{direction:ltr!important;unicode-bidi:isolate!important;font-size:18pt!important;}
.j2-glyph{font-size:39pt!important;}
.p005-title-spacer{display:inline-block;width:7mm;flex:0 0 7mm;}
.j2-grid{grid-template-rows:repeat(8,minmax(0,1fr))!important;}
.p005-enrichment-row{grid-column:1 / -1!important;grid-row:8!important;min-width:0!important;min-height:0!important;align-self:stretch!important;justify-self:stretch!important;display:grid!important;grid-template-columns:1fr 1fr!important;gap:3mm!important;direction:ltr!important;border-top:.28mm solid #111!important;padding:.55mm 2.2mm .35mm!important;box-sizing:border-box!important;overflow:visible!important;background:#fff!important;}
.p005-enrichment-row .micro{min-width:0!important;min-height:0!important;width:100%!important;display:flex!important;flex-direction:column!important;align-items:center!important;justify-content:center!important;text-align:center!important;overflow:visible!important;line-height:1.12!important;padding:0 .8mm!important;box-sizing:border-box!important;}
.p005-enrichment-row .micro-label{font-family:Arial,sans-serif!important;font-size:5.7pt!important;font-weight:700!important;line-height:1!important;margin:0 0 .6mm!important;white-space:nowrap!important;}
.p005-enrichment-row .micro-ar{font-family:'KFGQPC Uthman Taha Naskh','Amiri Quran','Amiri',serif!important;font-size:15.5pt!important;line-height:1.18!important;direction:rtl!important;white-space:nowrap!important;display:block!important;width:100%!important;text-align:center!important;padding:.35mm 1mm!important;box-sizing:border-box!important;overflow:visible!important;}
.p005-enrichment-row .micro-num{font-family:'KFGQPC Uthman Taha Naskh','Amiri Quran','Amiri',serif!important;font-size:15.5pt!important;line-height:1.22!important;direction:rtl!important;white-space:nowrap!important;display:block!important;width:100%!important;text-align:center!important;padding:.45mm 1.6mm!important;box-sizing:border-box!important;overflow:visible!important;letter-spacing:.05em!important;}
'''

_base_build=p001.build_page_html

def build_p005_v4(debug:bool):
    h=_base_build(debug)
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

    enrichment='''<div class="p005-enrichment-row" data-enrichment-row="8" aria-label="Lanjutan materi mikro">
      <div class="micro"><div class="micro-label">ANGKA ARAB</div><div class="micro-num" lang="ar">٠ · ١ · ٢ · ٣ · ٤ · ٥ · ٦ · ٧ · ٨ · ٩</div></div>
      <div class="micro"><div class="micro-label">PEMUTUS SAMBUNGAN</div><div class="micro-ar" lang="ar">ا · د · ذ · ر · ز · و</div></div>
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
        browser=await pw.chromium.launch();page=await browser.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2)
        await page.goto(h.resolve().as_uri(),wait_until='networkidle');await page.evaluate('document.fonts.ready')
        count=await page.locator('.j2-object').count()
        if count!=28: raise RuntimeError(f'P005_V4_OBJECT_COUNT_INVALID actual={count} expected=28')
        if await page.locator('.p005-enrichment-row .micro').count()!=2: raise RuntimeError('P005_V4_ENRICHMENT_COUNT_INVALID')
        metrics,layout_issues=await p001.fit_and_inspect(page)
        extra=await page.evaluate('''()=>{
          const g=document.querySelector('.j2-grid'),e=document.querySelector('.p005-enrichment-row'),f=document.querySelector('.footer');
          const out=[];if(!g||!e)return [{kind:'P005_ENRICHMENT_MISSING'}];
          const gr=g.getBoundingClientRect(),er=e.getBoundingClientRect();
          if(er.left<gr.left-1||er.right>gr.right+1||er.top<gr.top-1||er.bottom>gr.bottom+1)out.push({kind:'P005_ENRICHMENT_OUTSIDE_GRID'});
          const objs=[...document.querySelectorAll('.j2-object')];if(objs.length){const lastBottom=Math.max(...objs.map(x=>x.getBoundingClientRect().bottom));if(lastBottom>er.top-4)out.push({kind:'P005_ROW7_ROW8_CLEARANCE_TOO_SMALL',clearance:er.top-lastBottom,required:4});}
          if(f){const fr=f.getBoundingClientRect();if(er.bottom>fr.top-2)out.push({kind:'P005_ENRICHMENT_FOOTER_COLLISION'});}
          for(const sel of ['.micro-num','.micro-ar']){const el=document.querySelector(sel);if(el){const r=el.getBoundingClientRect(),p=el.parentElement.getBoundingClientRect();if(r.left<p.left-1||r.right>p.right+1)out.push({kind:'P005_ENRICHMENT_TEXT_HORIZONTAL_CLIP',selector:sel,textLeft:r.left,textRight:r.right,parentLeft:p.left,parentRight:p.right});}}
          return out;
        }''')
        all_issues=[*layout_issues,*extra];report.write_text(json.dumps(all_issues,ensure_ascii=False,indent=2),encoding='utf-8')
        if all_issues:
            kinds={}
            for x in all_issues:kinds[x['kind']]=kinds.get(x['kind'],0)+1
            raise RuntimeError('P005_V4_LAYOUT_ISSUES='+str(len(all_issues))+' TYPES='+','.join(f'{k}:{v}' for k,v in sorted(kinds.items()))+f' REPORT={report}')
        await page.screenshot(path=str(png/'page-005-v4.png'),full_page=True)
        primary=out/'QURBATA-JILID-2-P005-V4-RIGHT-TITLE-BOTTOMROW.pdf'
        try:
            await page.pdf(path=str(primary),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});pdf=primary;pdf_mode='DIRECT_V4'
        except PermissionError:
            pdf=out/'QURBATA-JILID-2-P005-V4-RIGHT-TITLE-BOTTOMROW-LOCK-SAFE.pdf';await page.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});pdf_mode='LOCK_FALLBACK_V4'
        await browser.close()
    return metrics,report,pdf,pdf_mode

p001.render=render_p005_v4

def main():
    if '--output-dir' not in sys.argv[1:]:sys.argv.extend(['--output-dir',DEFAULT_P005_OUTPUT])
    rc=v1.main()
    print('JILID2_P005_RENDERER_V4_RIGHT_TITLE_BOTTOMROW=PASS');print('PAGE=5')
    print('TITLE_VISUAL_RIGHT_TO_LEFT=ص←صَبَرَ|ض←ضَرَبَ');print('RIGHTMOST_TITLE_OBJECT=ص')
    print('CORE_PRACTICE_ROWS=7');print('CORE_PRACTICE_OBJECTS=28');print('ENRICHMENT_GRID_ROW=8_NATIVE')
    print('ENRICHMENT_BLOCK_POLICY=CONTINUE_UNTIL_MASTERY');print('ENRICHMENT_CATEGORY=E02|E06')
    print('ENRICHMENT_ITEM=ARABIC_INDIC_NUMERALS_0_9|NON_JOINERS');print('ARABIC_SPELLED_LETTER_NAMES=DISABLED')
    print('REGISTRY_OBJECTS=32_PRESERVED');print('PRESENTATION_FONT_SIZE=39PT');print('PRACTICE_FONT_SIZE=39PT')
    print('PRESENTATION_SIZE_POLICY=MATCH_PRACTICE');print('ENRICHMENT_TEXT_CLIP_GUARD=ENABLED')
    print('OUTPUT_DIR='+DEFAULT_P005_OUTPUT);return rc

if __name__=='__main__':raise SystemExit(main())
