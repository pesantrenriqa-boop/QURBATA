#!/usr/bin/env python3
"""QURBATA Jilid 2 P005 V4 — compact vocalized presentation + clean centered enrichment.

Visual title is forced from the RIGHT edge as:
    صَ ← صَبَرَ    ضَ ← ضَرَبَ
Row 8 keeps the active enrichment block from P004. Each numeral and non-joining
letter is rendered as an individual fixed-width glyph so spacing is even,
centered, and independent from RTL text reordering. No dot separators are used.
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
.presentation-object{font-size:34pt!important;direction:ltr!important;flex-direction:row-reverse!important;unicode-bidi:isolate!important;gap:1.7mm!important;}
.presentation-object .arabic-part{direction:rtl!important;unicode-bidi:isolate!important;line-height:1.15!important;padding:.35mm .3mm!important;}
.presentation-object .arrow{direction:ltr!important;unicode-bidi:isolate!important;font-size:15pt!important;}
.j2-glyph{font-size:39pt!important;}
.p005-title-spacer{display:inline-block;width:6mm;flex:0 0 6mm;}
.j2-grid{grid-template-rows:repeat(8,minmax(0,1fr))!important;}
.p005-enrichment-row{
  grid-column:1 / -1!important;grid-row:8!important;
  min-width:0!important;min-height:0!important;
  align-self:stretch!important;justify-self:stretch!important;
  display:grid!important;grid-template-columns:1fr 1fr!important;
  column-gap:10mm!important;direction:ltr!important;
  border-top:.28mm solid #111!important;
  padding:.7mm 7mm .5mm!important;box-sizing:border-box!important;
  overflow:visible!important;background:#fff!important;
}
.p005-enrichment-row .micro{
  min-width:0!important;min-height:0!important;width:100%!important;
  margin:0 auto!important;display:flex!important;flex-direction:column!important;
  align-items:center!important;justify-content:center!important;text-align:center!important;
  overflow:visible!important;line-height:1!important;padding:0!important;box-sizing:border-box!important;
}
.p005-enrichment-row .micro-label{
  font-family:Arial,sans-serif!important;font-size:6.4pt!important;font-weight:700!important;
  line-height:1!important;margin:0 0 1mm!important;white-space:nowrap!important;text-align:center!important;
}
.p005-enrichment-row .glyph-row{
  width:100%!important;display:flex!important;align-items:center!important;justify-content:center!important;
  direction:ltr!important;unicode-bidi:isolate!important;white-space:nowrap!important;
  box-sizing:border-box!important;overflow:visible!important;
}
.p005-enrichment-row .glyph-row.numbers{gap:2.7mm!important;}
.p005-enrichment-row .glyph-row.nonjoiners{gap:4.2mm!important;}
.p005-enrichment-row .glyph{
  font-family:'KFGQPC Uthman Taha Naskh','Amiri Quran','Amiri',serif!important;
  display:inline-flex!important;align-items:center!important;justify-content:center!important;
  flex:0 0 auto!important;line-height:1!important;text-align:center!important;direction:rtl!important;
  unicode-bidi:isolate!important;padding:.2mm!important;box-sizing:border-box!important;overflow:visible!important;
}
.p005-enrichment-row .numbers .glyph{font-size:20pt!important;min-width:5mm!important;}
.p005-enrichment-row .nonjoiners .glyph{font-size:21pt!important;min-width:6mm!important;}
'''

_base_build=p001.build_page_html

def _glyphs(items:str,kind:str)->str:
    return '<div class="glyph-row '+kind+'">'+''.join(f'<span class="glyph" lang="ar">{x}</span>' for x in items.split())+'</div>'

def build_p005_v4(debug:bool):
    h=_base_build(debug)
    start=h.index('<section class="presentation">')
    end=h.index('</section>',start)+len('</section>')
    pres=f'''<section class="presentation"><div class="presentation-object-wrap"><div class="presentation-object" dir="ltr">
      <span class="arabic-part" lang="ar" dir="rtl">{p001.arabic_html('صَ')}</span>
      <span class="arrow" dir="ltr">←</span>
      <span class="arabic-part" lang="ar" dir="rtl">{p001.arabic_html('صَبَرَ')}</span>
      <span class="p005-title-spacer"></span>
      <span class="arabic-part" lang="ar" dir="rtl">{p001.arabic_html('ضَ')}</span>
      <span class="arrow" dir="ltr">←</span>
      <span class="arabic-part" lang="ar" dir="rtl">{p001.arabic_html('ضَرَبَ')}</span>
    </div></div></section>'''
    h=h[:start]+pres+h[end:]

    enrichment=f'''<div class="p005-enrichment-row" data-enrichment-row="8" aria-label="Lanjutan materi mikro">
      <div class="micro"><div class="micro-label">ANGKA ARAB</div>{_glyphs('٠ ١ ٢ ٣ ٤ ٥ ٦ ٧ ٨ ٩','numbers')}</div>
      <div class="micro"><div class="micro-label">PEMUTUS SAMBUNGAN</div>{_glyphs('ا د ذ ر ز و','nonjoiners')}</div>
    </div>'''
    gs=h.find('<section class="j2-grid">')
    if gs<0: raise RuntimeError('P005_V4_GRID_START_NOT_FOUND')
    ge=h.find('</section>',gs)
    if ge<0: raise RuntimeError('P005_V4_GRID_END_NOT_FOUND')
    return h[:ge]+enrichment+h[ge:]

p001.build_page_html=build_p005_v4

async def _write_pdf_incremental(page,out:Path):
    names=[out/'QURBATA-JILID-2-P005-V4-RIGHT-TITLE-BOTTOMROW.pdf']
    names.extend(out/f'QURBATA-JILID-2-P005-V4-RIGHT-TITLE-BOTTOMROW-LOCK-SAFE-{i:02d}.pdf' for i in range(1,100))
    last_error=None
    for idx,pdf in enumerate(names):
        try:
            await page.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'})
            return pdf,('DIRECT_V4' if idx==0 else f'LOCK_FALLBACK_V4_{idx:02d}')
        except PermissionError as e:
            last_error=e
    raise RuntimeError('P005_V4_NO_AVAILABLE_PDF_NAME') from last_error

async def render_p005_v4(h:Path,out:Path,debug:bool):
    report=out/'LAYOUT-OVERFLOW-REPORT-J2-P005-V4.json'
    png=out/'png';png.mkdir(parents=True,exist_ok=True)
    async with async_playwright() as pw:
        browser=await pw.chromium.launch();page=await browser.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2)
        await page.goto(h.resolve().as_uri(),wait_until='networkidle');await page.evaluate('document.fonts.ready')
        count=await page.locator('.j2-object').count()
        if count!=28: raise RuntimeError(f'P005_V4_OBJECT_COUNT_INVALID actual={count} expected=28')
        if await page.locator('.p005-enrichment-row .micro').count()!=2: raise RuntimeError('P005_V4_ENRICHMENT_COUNT_INVALID')
        if await page.locator('.glyph-row.numbers .glyph').count()!=10: raise RuntimeError('P005_V4_NUMERAL_COUNT_INVALID')
        if await page.locator('.glyph-row.nonjoiners .glyph').count()!=6: raise RuntimeError('P005_V4_NONJOINER_COUNT_INVALID')
        metrics,layout_issues=await p001.fit_and_inspect(page)
        extra=await page.evaluate('''()=>{
          const g=document.querySelector('.j2-grid'),e=document.querySelector('.p005-enrichment-row'),f=document.querySelector('.footer');
          const out=[];if(!g||!e)return [{kind:'P005_ENRICHMENT_MISSING'}];
          const gr=g.getBoundingClientRect(),er=e.getBoundingClientRect();
          if(er.left<gr.left-1||er.right>gr.right+1||er.top<gr.top-1||er.bottom>gr.bottom+1)out.push({kind:'P005_ENRICHMENT_OUTSIDE_GRID'});
          const objs=[...document.querySelectorAll('.j2-object')];if(objs.length){const lastBottom=Math.max(...objs.map(x=>x.getBoundingClientRect().bottom));if(lastBottom>er.top-4)out.push({kind:'P005_ROW7_ROW8_CLEARANCE_TOO_SMALL',clearance:er.top-lastBottom,required:4});}
          if(f){const fr=f.getBoundingClientRect();if(er.bottom>fr.top-2)out.push({kind:'P005_ENRICHMENT_FOOTER_COLLISION'});}
          for(const row of document.querySelectorAll('.glyph-row')){const r=row.getBoundingClientRect(),p=row.parentElement.getBoundingClientRect();if(r.left<p.left-1||r.right>p.right+1)out.push({kind:'P005_ENRICHMENT_TEXT_HORIZONTAL_CLIP',row:row.className});}
          return out;
        }''')
        all_issues=[*layout_issues,*extra];report.write_text(json.dumps(all_issues,ensure_ascii=False,indent=2),encoding='utf-8')
        if all_issues:
            kinds={}
            for x in all_issues:kinds[x['kind']]=kinds.get(x['kind'],0)+1
            raise RuntimeError('P005_V4_LAYOUT_ISSUES='+str(len(all_issues))+' TYPES='+','.join(f'{k}:{v}' for k,v in sorted(kinds.items()))+f' REPORT={report}')
        await page.screenshot(path=str(png/'page-005-v4.png'),full_page=True)
        pdf,pdf_mode=await _write_pdf_incremental(page,out)
        await browser.close()
    return metrics,report,pdf,pdf_mode

p001.render=render_p005_v4

def main():
    if '--output-dir' not in sys.argv[1:]:sys.argv.extend(['--output-dir',DEFAULT_P005_OUTPUT])
    rc=v1.main()
    print('JILID2_P005_RENDERER_V4_RIGHT_TITLE_BOTTOMROW=PASS');print('PAGE=5')
    print('TITLE_VISUAL_RIGHT_TO_LEFT=صَ←صَبَرَ|ضَ←ضَرَبَ');print('RIGHTMOST_TITLE_OBJECT=صَ')
    print('CORE_PRACTICE_ROWS=7');print('CORE_PRACTICE_OBJECTS=28');print('ENRICHMENT_GRID_ROW=8_NATIVE')
    print('ENRICHMENT_BLOCK_POLICY=CONTINUE_UNTIL_MASTERY');print('ENRICHMENT_CATEGORY=E02|E06')
    print('ENRICHMENT_ITEM=ARABIC_INDIC_NUMERALS_0_9|NON_JOINERS');print('ARABIC_SPELLED_LETTER_NAMES=DISABLED')
    print('REGISTRY_OBJECTS=32_PRESERVED');print('PRESENTATION_FONT_SIZE=34PT');print('PRACTICE_FONT_SIZE=39PT')
    print('PRESENTATION_VOWELING=FATHA_ON_ISOLATED_ACQUISITION_LETTERS');print('ENRICHMENT_SEPARATOR=NONE')
    print('ENRICHMENT_ALIGNMENT=CENTERED_SYMMETRIC');print('ENRICHMENT_LAYOUT=INDIVIDUAL_FIXED_WIDTH_GLYPHS')
    print('ENRICHMENT_NUMERAL_ORDER=٠_١_٢_٣_٤_٥_٦_٧_٨_٩');print('ENRICHMENT_TEXT_SIZE=NUMBERS_20PT_NONJOINERS_21PT')
    print('ENRICHMENT_TEXT_CLIP_GUARD=ENABLED');print('PDF_WRITE_POLICY=INCREMENTAL_LOCK_SAFE_01_99')
    print('OUTPUT_DIR='+DEFAULT_P005_OUTPUT);return rc

if __name__=='__main__':raise SystemExit(main())
