#!/usr/bin/env python3
"""QURBATA Jilid 2 P004 V3 — cumulative page with lock-safe bottom-row enrichment.

V3 renders directly to its own PDF/report names and never deletes or overwrites
P004 V2. Core content stays at 32 lexical objects; production typography stays
52/39 pt. The cumulative enrichment capsule is absolutely anchored above the
footer so it cannot push document flow into the footer area.
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

# Production baseline. The capsule is fixed immediately above the 7mm footer.
p001.P001_CSS += r'''
.presentation-object{font-size:52pt!important;}
.j2-glyph{font-size:39pt!important;}
.cumulative-enrichment{
  position:absolute!important;
  left:8mm!important;right:8mm!important;bottom:10.2mm!important;
  height:8.2mm!important;box-sizing:border-box!important;
  border-top:.25mm solid #111;padding-top:.55mm!important;
  display:grid!important;grid-template-columns:1.45fr .8fr .75fr!important;
  gap:1.0mm!important;direction:ltr!important;overflow:hidden!important;
  background:#fff!important;z-index:3!important;
}
.cumulative-enrichment .micro{height:7.2mm!important;min-height:0!important;display:flex!important;flex-direction:column!important;align-items:center!important;justify-content:center!important;text-align:center!important;line-height:1!important;overflow:hidden!important}
.cumulative-enrichment .micro-label{font-family:Arial,sans-serif!important;font-size:5.4pt!important;font-weight:700!important;letter-spacing:.08pt!important;margin:0 0 .35mm!important;line-height:1!important}
.cumulative-enrichment .micro-ar{font-family:'KFGQPC Uthman Taha Naskh','Amiri Quran','Amiri',serif!important;font-size:11.8pt!important;line-height:1!important;direction:rtl!important;white-space:nowrap!important}
.cumulative-enrichment .micro-num{font-family:'KFGQPC Uthman Taha Naskh','Amiri Quran','Amiri',serif!important;font-size:14pt!important;line-height:1!important;direction:rtl!important;white-space:nowrap!important}
'''

_original_build=p001.build_page_html

def build_p004_v3(debug:bool):
    h=_original_build(debug)
    capsule='''<section class="cumulative-enrichment" aria-label="Kapsul Murojaah">
      <div class="micro"><div class="micro-label">NAMA HURUF</div><div class="micro-ar" lang="ar">بَاءٌ · تَاءٌ · ثَاءٌ · جِيمٌ · حَاءٌ · خَاءٌ · سِينٌ · شِينٌ</div></div>
      <div class="micro"><div class="micro-label">ANGKA ARAB</div><div class="micro-num" lang="ar">٠ · ١ · ٢ · ٣ · ٤ · ٥ · ٦ · ٧ · ٨ · ٩</div></div>
      <div class="micro"><div class="micro-label">PEMUTUS SAMBUNGAN</div><div class="micro-ar" lang="ar">ا · د · ذ · ر · ز · و</div></div>
    </section>'''
    candidates=['<footer', '<div class="footer', '<section class="footer']
    positions=[h.find(x) for x in candidates if h.find(x)>=0]
    if not positions: raise RuntimeError('P004_V3_FOOTER_ANCHOR_NOT_FOUND')
    pos=min(positions)
    return h[:pos]+capsule+h[pos:]

p001.build_page_html=build_p004_v3

async def render_p004_v3(h:Path,out:Path,debug:bool):
    report=out/'LAYOUT-OVERFLOW-REPORT-J2-P004-V3.json'
    png=out/'png'; png.mkdir(parents=True,exist_ok=True)
    async with async_playwright() as pw:
        browser=await pw.chromium.launch()
        page=await browser.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2)
        await page.goto(h.resolve().as_uri(),wait_until='networkidle')
        await page.evaluate('document.fonts.ready')
        count=await page.locator('.j2-object').count()
        if count!=32: raise RuntimeError(f'P004_V3_OBJECT_COUNT_INVALID actual={count} expected=32')
        enrichment_count=await page.locator('.cumulative-enrichment .micro').count()
        if enrichment_count!=3: raise RuntimeError(f'P004_V3_ENRICHMENT_COUNT_INVALID actual={enrichment_count} expected=3')
        metrics,layout_issues=await p001.fit_and_inspect(page)
        # Validate capsule against page, footer, and the last practice row.
        extra=await page.evaluate('''()=>{
          const e=document.querySelector('.cumulative-enrichment'),f=document.querySelector('.footer'),p=document.querySelector('.page');
          if(!e||!p)return [{kind:'ENRICHMENT_MISSING'}];
          const er=e.getBoundingClientRect(),pr=p.getBoundingClientRect(),out=[];
          if(er.left<pr.left||er.right>pr.right||er.bottom>pr.bottom)out.push({kind:'ENRICHMENT_PAGE_OVERFLOW'});
          if(f){const fr=f.getBoundingClientRect();if(er.bottom>fr.top-2)out.push({kind:'ENRICHMENT_FOOTER_COLLISION',enrichmentBottom:er.bottom,footerTop:fr.top});}
          const objs=[...document.querySelectorAll('.j2-object')];
          if(objs.length){const lastBottom=Math.max(...objs.map(x=>x.getBoundingClientRect().bottom));if(lastBottom>er.top-4)out.push({kind:'ENRICHMENT_CORE_COLLISION',lastPracticeBottom:lastBottom,enrichmentTop:er.top});}
          return out;
        }''')
        all_issues=[*layout_issues,*extra]
        report.write_text(json.dumps(all_issues,ensure_ascii=False,indent=2),encoding='utf-8')
        if all_issues:
            kinds={}
            for x in all_issues:kinds[x['kind']]=kinds.get(x['kind'],0)+1
            raise RuntimeError('P004_V3_LAYOUT_ISSUES='+str(len(all_issues))+' TYPES='+','.join(f'{k}:{v}' for k,v in sorted(kinds.items()))+f' REPORT={report}')
        await page.screenshot(path=str(png/'page-004-v3.png'),full_page=True)
        pdf=out/'QURBATA-JILID-2-P004-V3-CUMULATIVE-ENRICHMENT.pdf'
        try:
            await page.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'})
            pdf_mode='DIRECT_V3'
        except PermissionError:
            pdf=out/'QURBATA-JILID-2-P004-V3-CUMULATIVE-ENRICHMENT-LOCK-SAFE.pdf'
            await page.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'})
            pdf_mode='LOCK_FALLBACK_V3'
        await browser.close()
    return metrics,report,pdf,pdf_mode

p001.render=render_p004_v3

def main():
    if '--output-dir' not in sys.argv[1:]: sys.argv.extend(['--output-dir',DEFAULT_P004_OUTPUT])
    rc=v1.main()
    print('JILID2_P004_RENDERER_V3_CUMULATIVE_ENRICHMENT=PASS')
    print('PAGE=4')
    print('CUMULATIVE_ENRICHMENT=TRUE')
    print('ENRICHMENT_CATEGORY=E01|E02|E06')
    print('ENRICHMENT_ITEM=LETTER_NAMES|ARABIC_INDIC_NUMERALS_0_9|NON_JOINERS')
    print('ENRICHMENT_POSITION=ABSOLUTE_ABOVE_FOOTER')
    print('ENRICHMENT_PREREQUISITE=P001_P003_ACQUIRED_SYMBOL_SET')
    print('ENRICHMENT_STATUS=ACTIVE_CANDIDATE')
    print('CORE_PRACTICE_OBJECTS=32_UNCHANGED')
    print('PRESENTATION_FONT_SIZE=52PT')
    print('PRACTICE_FONT_SIZE=39PT')
    print('V2_FILE_TOUCH=FORBIDDEN')
    print('OUTPUT_DIR='+DEFAULT_P004_OUTPUT)
    print('STATUS=P004_CUMULATIVE_ENRICHMENT_CANDIDATE')
    return rc

if __name__=='__main__': raise SystemExit(main())
