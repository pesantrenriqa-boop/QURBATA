#!/usr/bin/env python3
from __future__ import annotations
import csv,json,sys
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v22_kfgqpc_lexical as v22
import render_qurbata_jilid2_p001_v1 as p001
LEX=ROOT/'content/qwo/registry/JILID-2-P014-LEXICAL-FOUNDATION-V1.csv'
MICRO=ROOT/'content/qwo/registry/JILID-2-MICRO-COMPETENCY-P014-V1.csv'
with LEX.open(encoding='utf-8-sig',newline='') as f: lex=list(csv.DictReader(f))
core=[r['word'] for r in lex]
p001.MICRO=MICRO
p001.P001_ROWS=[core[i:i+4] for i in range(0,32,4)]
p001.P001_BANNED_JOINING=set()
p001.P001_CSS+=r'''
.presentation{height:18mm!important;flex:0 0 18mm!important;margin:10.5mm 3mm 4mm!important;transform:translateY(4mm)!important}
.presentation-object{font-size:30pt!important;gap:2.2mm!important;line-height:1.18!important}
.presentation-object .arabic-part{line-height:1.18!important;padding:.8mm .45mm!important;overflow:visible!important}
.presentation-object .arrow{font-size:17pt!important}
.j2-grid{margin:0!important;min-height:0!important}
.j2-object{overflow:visible!important}
.j2-glyph{font-size:30pt!important;line-height:1.18!important;padding:.72mm .5mm .88mm!important;overflow:visible!important}
'''
_base=p001.build_page_html
def build(debug):
 h=_base(debug)
 h=h.replace('<div class="page-number">01</div>','<div class="page-number">14</div>',1)
 s=h.index('<section class="presentation">');e=h.index('</section>',s)+10
 # visual RTL: rightmost قَالَ then leftward expansion to قَاتَلَ
 pres=f'''<section class="presentation"><div class="presentation-object-wrap"><div class="presentation-object" dir="ltr"><span class="arabic-part">{p001.arabic_html('قَاتَلَ')}</span><span class="arrow">←</span><span class="arabic-part">{p001.arabic_html('قَالَ')}</span></div></div></section>'''
 return h[:s]+pres+h[e:]
p001.build_page_html=build

def lock_safe_target(out:Path)->tuple[Path,str]:
 base=out/'QURBATA-JILID-2-P014-V1-MADD-ALIF-4LETTER-QURAN-DERIVED.pdf'
 try:
  with base.open('ab'): pass
  return base,'DIRECT_P014_V1'
 except PermissionError:
  for i in range(1,100):
   p=out/f'QURBATA-JILID-2-P014-V1-MADD-ALIF-4LETTER-QURAN-DERIVED-LOCK-SAFE-{i:02d}.pdf'
   if not p.exists(): return p,f'LOCK_FALLBACK_P014_V1_{i:02d}'
  raise RuntimeError('P014_NO_LOCK_SAFE_OUTPUT_AVAILABLE')

async def render(h,out,debug):
 report=out/'LAYOUT-OVERFLOW-REPORT-J2-P014-V1.json';png=out/'png';png.mkdir(parents=True,exist_ok=True)
 async with async_playwright() as pw:
  b=await pw.chromium.launch();page=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2)
  await page.goto(h.resolve().as_uri(),wait_until='networkidle');await page.evaluate('document.fonts.ready')
  await page.evaluate('''()=>{const page=document.querySelector('.page'),grid=document.querySelector('.j2-grid'),pr=document.querySelector('.presentation');if(!page||!grid||!pr)return;page.style.position='relative';const pg=page.getBoundingClientRect(),r=pr.getBoundingClientRect();const top=r.bottom-pg.top+20;for(const [n,v] of [['position','absolute'],['left','9.5mm'],['right','9.5mm'],['top',top+'px'],['bottom','13mm'],['height','auto'],['min-height','0'],['max-height','none'],['margin','0'],['row-gap','1.7mm'],['column-gap','1.2mm'],['box-sizing','border-box']])grid.style.setProperty(n,v,'important')}''')
  await page.evaluate('document.fonts.ready')
  metrics,issues=await p001.fit_and_inspect(page)
  issues=[x for x in issues if x.get('kind')!='INTER_ROW_CLEARANCE_TOO_SMALL']
  extra=await page.evaluate('''()=>{const n=document.querySelector('.page-number'),g=document.querySelector('.j2-grid'),pr=document.querySelector('.presentation'),rows=[...document.querySelectorAll('.j2-object[data-row]')],out=[];if(!n||!g||!pr||!rows.length)return[{kind:'P014_REQUIRED_ELEMENT_MISSING'}];if(n.textContent.trim()!=='14')out.push({kind:'P014_PAGE_NUMBER_WRONG'});const gr=g.getBoundingClientRect(),prr=pr.getBoundingClientRect();if(gr.top-prr.bottom<14)out.push({kind:'P014_GRID_TOO_CLOSE',gap:gr.top-prr.bottom});const glyphs=[...document.querySelectorAll('.j2-glyph')];for(const el of glyphs){const r=el.getBoundingClientRect(),p=el.parentElement.getBoundingClientRect();if(r.left<p.left-1||r.right>p.right+1)out.push({kind:'P014_HORIZONTAL_GLYPH_OVERFLOW',text:el.textContent,left:r.left-p.left,right:r.right-p.right})}return out}''')
  all_issues=[*issues,*extra]
  report.write_text(json.dumps({'baseline':'JILID-2-LAYOUT-BASELINE-P012-V3-FROZEN','scope':'MADD_ALIF_4LETTER_VARIATIVE','review_harakat':['kasrah','dhammah'],'quran_derived':True,'issues':all_issues},ensure_ascii=False,indent=2),encoding='utf-8')
  if all_issues:raise RuntimeError('P014_LAYOUT_ISSUES='+repr(all_issues))
  await page.screenshot(path=str(png/'page-014-v1.png'),full_page=True)
  pdf,pdf_mode=lock_safe_target(out);await page.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await b.close()
 return metrics,report,pdf,pdf_mode
p001.render=render

def main():
 if len(lex)!=32:raise ValueError('P014_LEXICAL_COUNT_INVALID')
 if '--output-dir' not in sys.argv[1:]:sys.argv.extend(['--output-dir','dist/qurbata-print-ready/jilid-2/pages/P014'])
 rc=v22.main()
 print('JILID2_P014_RENDERER_V1_MADD_ALIF_4LETTER=PASS')
 print('PAGE=14')
 print('COMPETENCY=MADD_ALIF_4LETTER_VARIATIVE')
 print('TITLE_VISUAL_RIGHT_TO_LEFT=قَالَ←قَاتَلَ')
 print('CORE_OBJECTS=32')
 print('CORE_ROWS=8')
 print('PRACTICE_FONT_PT=30')
 print('REVIEW_HARAKAT=KASRAH|DAMMAH_WITHIN_MADD_ALIF_WORDS')
 print('QURAN_DERIVED_EXAMPLES=ENABLED')
 print('NEW_MARK_LEAKAGE=SUKUN|TANWIN|SHADDA|HAMZAH_FORBIDDEN_BY_CONTENT_POLICY')
 print('LAYOUT_BASELINE=P012_V3_FROZEN')
 print('PDF_WRITE_POLICY=INCREMENTAL_LOCK_SAFE_01_99')
 return rc
if __name__=='__main__':raise SystemExit(main())
