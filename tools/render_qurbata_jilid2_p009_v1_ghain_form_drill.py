#!/usr/bin/env python3
from __future__ import annotations
import csv,json,sys,unicodedata
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v22_kfgqpc_lexical as v22
import render_qurbata_jilid2_p001_v1 as p001
MAP=ROOT/'content/qwo/registry/JILID-2-P009-COMPETENCY-MAP-V1.csv';MICRO=ROOT/'content/qwo/registry/JILID-2-MICRO-COMPETENCY-P009-V1.csv';LEX=ROOT/'content/qwo/registry/JILID-2-P009-LEXICAL-FOUNDATION-V1.csv';ENRICH=ROOT/'content/qwo/registry/JILID-2-BOTTOM-ROW-ENRICHMENT-LADDER-V1.csv'
with MAP.open(encoding='utf-8-sig',newline='') as f:meta=next(csv.DictReader(f))
with MICRO.open(encoding='utf-8-sig',newline='') as f:stairs=list(csv.DictReader(f))
with LEX.open(encoding='utf-8-sig',newline='') as f:lex=list(csv.DictReader(f))
with ENRICH.open(encoding='utf-8-sig',newline='') as f:enrich_rows={r['StepCode']:r for r in csv.DictReader(f)}
enrich=enrich_rows['E03']
MARKS=set(chr(c) for c in range(0x064B,0x0660))|{'ـ'}
def base(s):return ''.join(ch for ch in unicodedata.normalize('NFC',s) if ch not in MARKS and unicodedata.category(ch)!='Mn')
p001.MICRO=MICRO;p001.P001_BANNED_JOINING=set('منيه')
forms=[r['word'] for r in lex[:28]];p001.P001_ROWS=[forms[i:i+4] for i in range(0,28,4)]
p001.P001_CSS+=r'''.presentation-object{font-size:34pt!important;direction:ltr!important;flex-direction:row-reverse!important;gap:1.7mm!important}.presentation-object .arabic-part{direction:rtl!important;line-height:1.15!important}.presentation-object .arrow{font-size:15pt!important}.j2-glyph{font-size:39pt!important}.j2-grid{grid-template-rows:repeat(7,minmax(0,1fr)) minmax(0,.86fr)!important;padding-bottom:2.4mm!important;box-sizing:border-box!important}.p009-enrichment-row{grid-column:1/-1!important;grid-row:8!important;display:flex!important;flex-direction:column!important;align-items:center!important;justify-content:center!important;padding:.15mm 3mm .1mm!important;border-top:.28mm solid #111!important;box-sizing:border-box!important;background:#fff!important;text-align:center!important;overflow:hidden!important;transform:translateY(-1.2mm)!important}.p009-enrichment-row .micro-label{font-family:Arial,sans-serif!important;font-size:5.5pt!important;font-weight:700!important;margin:0 0 .2mm!important;line-height:1!important}.p009-enrichment-row .awail-run{width:100%!important;display:flex!important;align-items:center!important;justify-content:space-evenly!important;font-family:'KFGQPC Uthman Taha Naskh','Amiri Quran','Amiri',serif!important;font-size:27pt!important;line-height:.92!important;direction:rtl!important;unicode-bidi:isolate!important;white-space:nowrap!important;letter-spacing:0!important}.p009-enrichment-row .awail-item{display:inline-block!important;margin:0 .8mm!important;flex:0 0 auto!important}'''
_base=p001.build_page_html
def build(debug):
 h=_base(debug).replace('<div class="page-number">01</div>','<div class="page-number">09</div>',1);s=h.index('<section class="presentation">');e=h.index('</section>',s)+10
 pres=f'''<section class="presentation"><div class="presentation-object-wrap"><div class="presentation-object" dir="ltr"><span class="arabic-part">{p001.arabic_html('كَ')}</span><span class="arrow">←</span><span class="arabic-part">{p001.arabic_html('كُتِبَ')}</span><span class="arabic-part">{p001.arabic_html('لَ')}</span><span class="arrow">←</span><span class="arabic-part">{p001.arabic_html('لَبِثَ')}</span></div></div></section>''';h=h[:s]+pres+h[e:]
 items=[x.strip() for x in enrich['Content'].split('|') if x.strip()]
 awail=''.join(f'<span class="awail-item">{p001.arabic_html(x)}</span>' for x in items)
 en=f'''<div class="p009-enrichment-row" data-enrichment-step="{enrich['StepCode']}" data-item-count="{len(items)}"><div class="micro-label">{enrich['Label']}</div><div class="awail-run">{awail}</div></div>''';g=h.find('<section class="j2-grid">');ge=h.find('</section>',g);return h[:ge]+en+h[ge:]
p001.build_page_html=build
async def _write_pdf(page,out:Path):
 names=[out/'QURBATA-JILID-2-P009-V5-KAF-LAM-MIXED-VOWELS-AWAILUSSURAR-SAFE-BOTTOM.pdf']+[out/f'QURBATA-JILID-2-P009-V5-KAF-LAM-MIXED-VOWELS-AWAILUSSURAR-SAFE-BOTTOM-LOCK-SAFE-{i:02d}.pdf' for i in range(1,100)]
 last=None
 for idx,p in enumerate(names):
  try:
   await page.pdf(path=str(p),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});return p,('DIRECT_P009_V5' if idx==0 else f'LOCK_FALLBACK_P009_V5_{idx:02d}')
  except PermissionError as e:last=e
 raise RuntimeError('P009_NO_AVAILABLE_PDF_NAME') from last
async def render(h,out,debug):
 report=out/'LAYOUT-OVERFLOW-REPORT-J2-P009-V5.json';png=out/'png';png.mkdir(parents=True,exist_ok=True)
 async with async_playwright() as pw:
  b=await pw.chromium.launch();page=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);await page.goto(h.resolve().as_uri(),wait_until='networkidle');await page.evaluate('document.fonts.ready');metrics,issues=await p001.fit_and_inspect(page);extra=await page.evaluate('''()=>{const e=document.querySelector('.p009-enrichment-row'),r=document.querySelector('.awail-run'),g=document.querySelector('.j2-grid'),out=[];if(!e||!r||!g)return[{kind:'P009_ENRICHMENT_MISSING'}];const er=e.getBoundingClientRect(),rr=r.getBoundingClientRect(),gr=g.getBoundingClientRect();if(er.left<gr.left-1||er.right>gr.right+1||er.bottom>gr.bottom+1)out.push({kind:'P009_ENRICHMENT_OUTSIDE_GRID'});if(rr.scrollWidth>rr.clientWidth+2)out.push({kind:'P009_AWAIL_ROW_OVERFLOW',scrollWidth:rr.scrollWidth,clientWidth:rr.clientWidth});const safeBottom=window.innerHeight-18;if(er.bottom>safeBottom)out.push({kind:'P009_PAGE_BOTTOM_SAFEAREA_FAIL',bottom:er.bottom,safeBottom});return out}''');all_issues=[*issues,*extra];report.write_text(json.dumps(all_issues,ensure_ascii=False,indent=2),encoding='utf-8')
  if all_issues:raise RuntimeError('P009_LAYOUT_ISSUES='+repr(all_issues))
  await page.screenshot(path=str(png/'page-009-v5.png'),full_page=True);pdf,mode=await _write_pdf(page,out);await b.close()
 return metrics,report,pdf,mode
p001.render=render
def main():
 core=lex[:28];kaf=sum('ك' in base(r['word']) for r in core);lam=sum('ل' in base(r['word']) for r in core)
 if kaf<14 or lam<14:raise ValueError(f'P009_FORM_BALANCE_FAIL kaf={kaf} lam={lam}')
 badlen=[r['word'] for r in core if len(base(r['word']))!=3]
 if badlen:raise ValueError('P009_CORE_NOT_THREE_LETTERS='+repr(badlen))
 premature=[]
 for r in core:
  hit=set(base(r['word']))&set('اأإآءؤئى')
  if hit:premature.append((r['word'],''.join(sorted(hit))))
 if premature:raise ValueError('P009_PREMATURE_MADD_OR_HAMZAH='+repr(premature))
 forbidden_marks=set('ًٌٍّْ')
 mark_leaks=[]
 for r in core:
  hit=forbidden_marks&set(r['word'])
  if hit:mark_leaks.append((r['word'],''.join(sorted(hit))))
 if mark_leaks:raise ValueError('P009_PREMATURE_MARK_LEAKAGE='+repr(mark_leaks))
 leaks=[]
 for r in core:
  hit=p001.P001_BANNED_JOINING&set(base(r['word']))
  if hit:leaks.append((r['word'],''.join(sorted(hit))))
 if leaks:raise ValueError('P009_FUTURE_LETTER_LEAKAGE='+repr(leaks))
 items=[x.strip() for x in enrich['Content'].split('|') if x.strip()]
 if len(items)<7:raise ValueError(f'P009_AWAIL_ROW_TOO_SPARSE count={len(items)}')
 if '--output-dir' not in sys.argv[1:]:sys.argv.extend(['--output-dir','dist/qurbata-print-ready/jilid-2/pages/P009'])
 rc=v22.main();print('JILID2_P009_RENDERER_V5_SAFE_BOTTOM=PASS');print('ACQUISITION_LETTERS=ك|ل');print('PRACTICE_MODE=JOINING_FORM_DRILL');print('CORE_DRILL_LENGTH=3_LETTERS_ONLY');print(f'FORM_KAF_OBJECTS={kaf}');print(f'FORM_LAM_OBJECTS={lam}');print('SHORT_VOWELS=FATHAH|KASRAH|DAMMAH');print('TITLE_VISUAL_RIGHT_TO_LEFT=كَ←كُتِبَ|لَ←لَبِثَ');print('PREMATURE_MADD_OR_HAMZAH=0');print('PREMATURE_MARK_LEAKAGE=0');print('FUTURE_LETTER_LEAKAGE=0');print(f'BOTTOM_ROW_ENRICHMENT_STEP={enrich["StepCode"]}');print(f'BOTTOM_ROW_ITEM_COUNT={len(items)}');print('BOTTOM_ROW_FONT_SIZE_PT=27');print('BOTTOM_ROW_SAFE_MARGIN_MM=2.4');print('BOTTOM_ROW_PAGE_SAFEAREA_GUARD=ENABLED');print('PDF_WRITE_POLICY=INCREMENTAL_LOCK_SAFE_01_99');return rc
if __name__=='__main__':raise SystemExit(main())
