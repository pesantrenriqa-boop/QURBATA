#!/usr/bin/env python3
from __future__ import annotations
import csv,json,sys,unicodedata
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v22_kfgqpc_lexical as v22
import render_qurbata_jilid2_p001_v1 as p001
MAP=ROOT/'content/qwo/registry/JILID-2-P006-COMPETENCY-MAP-V1.csv';MICRO=ROOT/'content/qwo/registry/JILID-2-MICRO-COMPETENCY-P006-V1.csv';LEX=ROOT/'content/qwo/registry/JILID-2-P006-LEXICAL-FOUNDATION-V1.csv'
with MAP.open(encoding='utf-8-sig',newline='') as f:meta=next(csv.DictReader(f))
with MICRO.open(encoding='utf-8-sig',newline='') as f:stairs=list(csv.DictReader(f))
with LEX.open(encoding='utf-8-sig',newline='') as f:lex=list(csv.DictReader(f))
MARKS=set(chr(c) for c in range(0x064B,0x0660))|{'ـ'}
def base(s):return ''.join(ch for ch in unicodedata.normalize('NFC',s) if ch not in MARKS and unicodedata.category(ch)!='Mn')
p001.MICRO=MICRO;p001.P001_BANNED_JOINING=set('عغفقكلمنيه')
forms=[r['word'] for r in lex[:28]];p001.P001_ROWS=[forms[i:i+4] for i in range(0,28,4)]
p001.P001_CSS+=r'''.presentation-object{font-size:34pt!important;direction:ltr!important;flex-direction:row-reverse!important;gap:1.7mm!important}.presentation-object .arabic-part{direction:rtl!important;line-height:1.15!important}.presentation-object .arrow{font-size:15pt!important}.j2-glyph{font-size:39pt!important}.j2-grid{grid-template-rows:repeat(8,minmax(0,1fr))!important}.p006-enrichment-row{grid-column:1/-1!important;grid-row:8!important;display:grid!important;grid-template-columns:1fr 1fr!important;gap:10mm!important;padding:.55mm 6mm .35mm!important;border-top:.28mm solid #111!important;box-sizing:border-box!important;background:#fff!important}.p006-enrichment-row .micro{display:flex!important;flex-direction:column!important;align-items:center!important;justify-content:center!important}.p006-enrichment-row .micro-label{font-family:Arial,sans-serif!important;font-size:6.2pt!important;font-weight:700!important;margin:0 0 .7mm!important}.glyph-run{display:flex!important;justify-content:center!important;gap:1.45mm!important;direction:ltr!important}.glyph-run.num .eg{font-size:20pt!important;width:4mm!important;text-align:center!important}.glyph-run.nonjoin .eg{font-size:21pt!important;width:5mm!important;text-align:center!important}'''
_base=p001.build_page_html
def build(debug):
 h=_base(debug).replace('<div class="page-number">01</div>','<div class="page-number">06</div>',1);s=h.index('<section class="presentation">');e=h.index('</section>',s)+10
 pres=f'''<section class="presentation"><div class="presentation-object-wrap"><div class="presentation-object" dir="ltr"><span class="arabic-part">{p001.arabic_html('طَ')}</span><span class="arrow">←</span><span class="arabic-part">{p001.arabic_html('طَرَبَ')}</span><span class="arabic-part">{p001.arabic_html('ظَ')}</span><span class="arrow">←</span><span class="arabic-part">{p001.arabic_html('حَظَرَ')}</span></div></div></section>''';h=h[:s]+pres+h[e:]
 nums=''.join(f'<span class="eg">{x}</span>' for x in '٠١٢٣٤٥٦٧٨٩');njs=''.join(f'<span class="eg">{x}</span>' for x in 'ادذرزو');en=f'''<div class="p006-enrichment-row"><div class="micro"><div class="micro-label">ANGKA ARAB</div><div class="glyph-run num">{nums}</div></div><div class="micro"><div class="micro-label">PEMUTUS SAMBUNGAN</div><div class="glyph-run nonjoin">{njs}</div></div></div>''';g=h.find('<section class="j2-grid">');ge=h.find('</section>',g);return h[:ge]+en+h[ge:]
p001.build_page_html=build
async def _write_pdf(page,out:Path):
 names=[out/'QURBATA-JILID-2-P006-V7-TA-ZA-THREE-LETTER-FORM-DRILL.pdf']+[out/f'QURBATA-JILID-2-P006-V7-TA-ZA-THREE-LETTER-FORM-DRILL-LOCK-SAFE-{i:02d}.pdf' for i in range(1,100)]
 last=None
 for idx,p in enumerate(names):
  try:
   await page.pdf(path=str(p),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'})
   return p,('DIRECT_P006_V7' if idx==0 else f'LOCK_FALLBACK_P006_V7_{idx:02d}')
  except PermissionError as e:last=e
 raise RuntimeError('P006_NO_AVAILABLE_PDF_NAME') from last
async def render(h,out,debug):
 report=out/'LAYOUT-OVERFLOW-REPORT-J2-P006-V7.json';png=out/'png';png.mkdir(parents=True,exist_ok=True)
 async with async_playwright() as pw:
  b=await pw.chromium.launch();page=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);await page.goto(h.resolve().as_uri(),wait_until='networkidle');await page.evaluate('document.fonts.ready');metrics,issues=await p001.fit_and_inspect(page);report.write_text(json.dumps(issues,ensure_ascii=False,indent=2),encoding='utf-8')
  if issues:raise RuntimeError('P006_LAYOUT_ISSUES='+repr(issues))
  await page.screenshot(path=str(png/'page-006-v7.png'),full_page=True);pdf,mode=await _write_pdf(page,out);await b.close()
 return metrics,report,pdf,mode
p001.render=render
def main():
 core=lex[:28]
 invalid_len=[r['word'] for r in core if len(base(r['word']))!=3]
 if invalid_len:raise ValueError('P006_NON_THREE_LETTER_DRILL='+repr(invalid_len))
 ta=sum('ط' in base(r['word']) for r in core);za=sum('ظ' in base(r['word']) for r in core)
 if ta<14 or za<14:raise ValueError(f'P006_FORM_BALANCE_FAIL ta={ta} za={za}')
 premature=[]
 for r in core:
  hit=set(base(r['word']))&set('اأإآءؤئى')
  if hit:premature.append((r['word'],''.join(sorted(hit))))
 if premature:raise ValueError('P006_PREMATURE_MADD_OR_HAMZAH='+repr(premature))
 leaks=[]
 for r in core:
  hit=p001.P001_BANNED_JOINING&set(base(r['word']))
  if hit:leaks.append((r['word'],''.join(sorted(hit))))
 if leaks:raise ValueError('P006_FUTURE_LETTER_LEAKAGE='+repr(leaks))
 if '--output-dir' not in sys.argv[1:]:sys.argv.extend(['--output-dir','dist/qurbata-print-ready/jilid-2/pages/P006'])
 rc=v22.main();print('JILID2_P006_RENDERER_V7_THREE_LETTER=PASS');print('ACQUISITION_LETTERS=ط|ظ');print('PRACTICE_MODE=JOINING_FORM_DRILL');print('CORE_DRILL_LENGTH=3_LETTERS_ONLY');print(f'FORM_TA_OBJECTS={ta}');print(f'FORM_ZA_OBJECTS={za}');print('TITLE_VISUAL_RIGHT_TO_LEFT=طَ←طَرَبَ|ظَ←حَظَرَ');print('PREMATURE_MADD_OR_HAMZAH=0');print('FUTURE_LETTER_LEAKAGE=0');print('PDF_WRITE_POLICY=INCREMENTAL_LOCK_SAFE_01_99');return rc
if __name__=='__main__':raise SystemExit(main())
