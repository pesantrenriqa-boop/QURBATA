#!/usr/bin/env python3
"""QURBATA Jilid 2 P025 — penguatan mad ya, tangga 3/4/5 huruf, tanpa pindah ke kasrah/sukun baru."""
from __future__ import annotations
import sys,json
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v22_kfgqpc_lexical as v22
import render_qurbata_jilid2_p001_v1 as p001
ROWS=[
['دِينُ','فِيلُ','جِيدُ','عِيدُ'],
['خِيرُ','سِيرُ','بِيرُ','زِيرُ'],
['رَحِيمُ','كَرِيمُ','حَكِيمُ','عَلِيمُ'],
['عَظِيمُ','شَهِيدُ','وَكِيلُ','مَجِيدُ'],
['بَصِيرُ','خَبِيرُ','قَدِيرُ','سَمِيعُ'],
['نَذِيرُ','بَشِيرُ','قَرِيبُ','مُنِيبُ'],
['مِيثَاقُ','مِيزَانُ','قِيلَتْ','زِينَةُ'],
['سَبِيلُ','نَصِيرُ','حَمِيدُ','شَدِيدُ'],
]
p001.P001_BANNED_JOINING=set(); p001.P001_ROWS=ROWS
p001.P001_CSS += r'''
.presentation-object{font-size:48pt}.j2-glyph{font-size:42pt}
.j2-glyph,.presentation-object .arabic-part{direction:rtl;font-family:"QURBATA KFGQPC Uthman Taha Naskh","KFGQPC Uthman Taha Naskh",serif!important;font-feature-settings:'mark' 1,'mkmk' 1;text-rendering:optimizeLegibility}
'''
orig=p001.build_page_html
def build(debug):
 h=orig(debug).replace('<div class="page-number">01</div>','<div class="page-number">25</div>',1)
 s=h.index('<section class="presentation">');e=h.index('</section>',s)+len('</section>')
 pres='''<section class="presentation"><div class="presentation-object-wrap"><div class="presentation-object"><span class="arabic-part" lang="ar">رَحِيمُ</span><span class="arrow">←</span><span class="arabic-part" lang="ar">حِيمُ</span><span class="arrow">←</span><span class="arabic-part" lang="ar">حِي</span></div></div></section>'''
 return h[:s]+pres+h[e:]
p001.build_page_html=build
async def render(h,out,debug):
 report=out/'LAYOUT-OVERFLOW-REPORT-J2-P025-V2.json';png=out/'png';png.mkdir(parents=True,exist_ok=True)
 async with async_playwright() as pw:
  b=await pw.chromium.launch();p=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2)
  await p.goto(h.resolve().as_uri(),wait_until='networkidle');await p.evaluate('document.fonts.ready')
  if (await p.locator('.page-number').inner_text()).strip()!='25':raise RuntimeError('P025_PAGE_IDENTITY_FAIL')
  # Do not scan the entire inherited page: debug/metadata/targets may legitimately contain
  # characters unrelated to the P025 exercise. Gate only the actual Arabic lesson objects.
  lesson_text=await p.evaluate("""()=>[...document.querySelectorAll('.j2-glyph,.presentation-object .arabic-part')].map(e=>e.textContent||'').join('|')""")
  if 'ۡ' in lesson_text or 'ْ' in lesson_text:raise RuntimeError('P025_EXPLICIT_SUKUN_FORBIDDEN_IN_LESSON_OBJECTS='+repr(lesson_text))
  expected=[w for row in ROWS for w in row]
  rendered=await p.evaluate("""()=>[...document.querySelectorAll('.j2-glyph')].map(e=>(e.textContent||'').trim())""")
  if rendered!=expected:raise RuntimeError('P025_LESSON_CONTENT_DRIFT')
  metrics,issues=await p001.fit_and_inspect(p);report.write_text(json.dumps({'layout_issues':issues,'stage':'MAD_YA_REINFORCEMENT_3_4_5','sukun_gate_scope':'lesson_objects_only'},ensure_ascii=False,indent=2),encoding='utf-8')
  if issues:raise RuntimeError('P025_LAYOUT_ISSUES='+str(len(issues))+' REPORT='+str(report))
  await p.screenshot(path=str(png/'page-025.png'),full_page=True)
  pdf=out/'QURBATA-JILID-2-P025-V2-MAD-YA-REINFORCEMENT.pdf';await p.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await b.close()
 return metrics,report,pdf
p001.render=render
def main():
 rc=v22.main();print('JILID2_P025_RENDERER_V2=PASS');print('PAGE=25');print('SEQUENCE=CONTINUE_MAD_YA');print('LADDER=3_4_5_LETTERS');print('EXPLICIT_SUKUN_ON_MAD_YA=NO');print('SUKUN_GATE_SCOPE=LESSON_OBJECTS_ONLY');print('FONT=KFGQPC_UTHMAN_TAHA');print('STATUS=P025_CANDIDATE_NOT_FROZEN');return rc
if __name__=='__main__':raise SystemExit(main())
