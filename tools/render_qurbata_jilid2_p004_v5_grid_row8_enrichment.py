#!/usr/bin/env python3
"""QURBATA Jilid 2 P004 V5 — native grid-row-8 cumulative enrichment.

Clean redesign: P004 keeps seven practice rows (28 on-page lexical objects), while
micro-enrichment is inserted as a direct child of .j2-grid at grid-row:8. Nothing
is appended below the grid and nothing overlays the footer. Core typography stays
52pt presentation / 39pt practice.
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

# Seven practice rows; the lexical registry remains untouched at 32 entries.
words=[r['word'] for r in v1.lex[:28]]
p001.P001_ROWS=[words[i:i+4] for i in range(0,28,4)]

# Keep the production geometry. Row 8 is a normal grid row, not extra page flow.
p001.P001_CSS += r'''
.presentation-object{font-size:52pt!important;}
.j2-glyph{font-size:39pt!important;}
.j2-grid{grid-template-rows:repeat(8,minmax(0,1fr))!important;}
.cumulative-grid-row{
  grid-column:1 / -1!important;
  grid-row:8!important;
  min-width:0!important;min-height:0!important;
  align-self:stretch!important;justify-self:stretch!important;
  display:grid!important;grid-template-columns:1.45fr .8fr .75fr!important;
  gap:1.2mm!important;direction:ltr!important;
  border-top:.28mm solid #111!important;
  padding:.55mm .8mm 0!important;box-sizing:border-box!important;
  overflow:hidden!important;background:#fff!important;
}
.cumulative-grid-row .micro{min-width:0!important;min-height:0!important;display:flex!important;flex-direction:column!important;align-items:center!important;justify-content:center!important;text-align:center!important;overflow:hidden!important;line-height:1!important;}
.cumulative-grid-row .micro-label{font-family:Arial,sans-serif!important;font-size:5.7pt!important;font-weight:700!important;line-height:1!important;margin:0 0 .45mm!important;white-space:nowrap!important;}
.cumulative-grid-row .micro-ar{font-family:'KFGQPC Uthman Taha Naskh','Amiri Quran','Amiri',serif!important;font-size:13.2pt!important;line-height:1!important;direction:rtl!important;white-space:nowrap!important;}
.cumulative-grid-row .micro-num{font-family:'KFGQPC Uthman Taha Naskh','Amiri Quran','Amiri',serif!important;font-size:16pt!important;line-height:1!important;direction:rtl!important;white-space:nowrap!important;}
'''

_original_build=p001.build_page_html

def build_p004_v5(debug:bool):
    h=_original_build(debug)
    row='''<div class="cumulative-grid-row" data-enrichment-row="8" aria-label="Kapsul Murojaah">
      <div class="micro"><div class="micro-label">NAMA HURUF</div><div class="micro-ar" lang="ar">بَاءٌ · تَاءٌ · ثَاءٌ · جِيمٌ · حَاءٌ · خَاءٌ · سِينٌ · شِينٌ</div></div>
      <div class="micro"><div class="micro-label">ANGKA ARAB</div><div class="micro-num" lang="ar">٠ · ١ · ٢ · ٣ · ٤ · ٥ · ٦ · ٧ · ٨ · ٩</div></div>
      <div class="micro"><div class="micro-label">PEMUTUS SAMBUNGAN</div><div class="micro-ar" lang="ar">ا · د · ذ · ر · ز · و</div></div>
    </div>'''
    start=h.find('<section class="j2-grid">')
    if start<0: raise RuntimeError('P004_V5_GRID_START_NOT_FOUND')
    end=h.find('</section>',start)
    if end<0: raise RuntimeError('P004_V5_GRID_END_NOT_FOUND')
    return h[:end]+row+h[end:]

p001.build_page_html=build_p004_v5

async def render_p004_v5(h:Path,out:Path,debug:bool):
    report=out/'LAYOUT-OVERFLOW-REPORT-J2-P004-V5.json'
    png=out/'png';png.mkdir(parents=True,exist_ok=True)
    async with async_playwright() as pw:
        browser=await pw.chromium.launch()
        page=await browser.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2)
        await page.goto(h.resolve().as_uri(),wait_until='networkidle')
        await page.evaluate('document.fonts.ready')
        count=await page.locator('.j2-object').count()
        if count!=28: raise RuntimeError(f'P004_V5_OBJECT_COUNT_INVALID actual={count} expected=28')
        if await page.locator('.cumulative-grid-row .micro').count()!=3:
            raise RuntimeError('P004_V5_ENRICHMENT_COUNT_INVALID')
        metrics,layout_issues=await p001.fit_and_inspect(page)
        extra=await page.evaluate('''()=>{
          const g=document.querySelector('.j2-grid'),e=document.querySelector('.cumulative-grid-row');
          const objs=[...document.querySelectorAll('.j2-object')],out=[];
          if(!g||!e)return [{kind:'ENRICHMENT_GRID_ROW_MISSING'}];
          const gr=g.getBoundingClientRect(),er=e.getBoundingClientRect();
          if(er.left<gr.left-1||er.right>gr.right+1||er.top<gr.top-1||er.bottom>gr.bottom+1)out.push({kind:'ENRICHMENT_OUTSIDE_GRID',grid:{top:gr.top,bottom:gr.bottom},enrichment:{top:er.top,bottom:er.bottom}});
          if(objs.length){const lastBottom=Math.max(...objs.map(x=>x.getBoundingClientRect().bottom));if(lastBottom>er.top-4)out.push({kind:'ROW7_ROW8_CLEARANCE_TOO_SMALL',lastPracticeBottom:lastBottom,enrichmentTop:er.top,clearance:er.top-lastBottom,required:4});}
          const f=document.querySelector('.footer');if(f){const fr=f.getBoundingClientRect();if(er.bottom>fr.top-2)out.push({kind:'ENRICHMENT_FOOTER_COLLISION',enrichmentBottom:er.bottom,footerTop:fr.top});}
          return out;
        }''')
        all_issues=[*layout_issues,*extra]
        report.write_text(json.dumps(all_issues,ensure_ascii=False,indent=2),encoding='utf-8')
        if all_issues:
            kinds={}
            for x in all_issues:kinds[x['kind']]=kinds.get(x['kind'],0)+1
            raise RuntimeError('P004_V5_LAYOUT_ISSUES='+str(len(all_issues))+' TYPES='+','.join(f'{k}:{v}' for k,v in sorted(kinds.items()))+f' REPORT={report}')
        await page.screenshot(path=str(png/'page-004-v5.png'),full_page=True)
        primary=out/'QURBATA-JILID-2-P004-V5-GRID-ROW8-ENRICHMENT.pdf'
        try:
            await page.pdf(path=str(primary),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});pdf=primary;pdf_mode='DIRECT_V5'
        except PermissionError:
            pdf=out/'QURBATA-JILID-2-P004-V5-GRID-ROW8-ENRICHMENT-LOCK-SAFE.pdf'
            await page.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});pdf_mode='LOCK_FALLBACK_V5'
        await browser.close()
    return metrics,report,pdf,pdf_mode

p001.render=render_p004_v5

def main():
    if '--output-dir' not in sys.argv[1:]:sys.argv.extend(['--output-dir',DEFAULT_P004_OUTPUT])
    rc=v1.main()
    print('JILID2_P004_RENDERER_V5_GRID_ROW8_ENRICHMENT=PASS')
    print('PAGE=4')
    print('CORE_PRACTICE_ROWS=7')
    print('CORE_PRACTICE_OBJECTS=28')
    print('ENRICHMENT_GRID_ROW=8_NATIVE')
    print('ENRICHMENT_CATEGORY=E01|E02|E06')
    print('REGISTRY_OBJECTS=32_PRESERVED')
    print('PRESENTATION_FONT_SIZE=52PT')
    print('PRACTICE_FONT_SIZE=39PT')
    print('LAYOUT_MODEL=ENRICHMENT_INSIDE_J2_GRID')
    print('OUTPUT_DIR='+DEFAULT_P004_OUTPUT)
    print('STATUS=P004_V5_GRID_ROW8_CANDIDATE')
    return rc

if __name__=='__main__':raise SystemExit(main())
