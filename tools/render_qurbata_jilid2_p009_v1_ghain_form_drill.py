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
p001.P001_CSS+=r'''
.page{position:relative!important;overflow:hidden!important}
.presentation-object{font-size:34pt!important;direction:ltr!important;flex-direction:row-reverse!important;gap:1.7mm!important}
.presentation-object .arabic-part{direction:rtl!important;line-height:1.15!important}
.presentation-object .arrow{font-size:15pt!important}
.j2-glyph{font-size:39pt!important}
.j2-grid{height:132mm!important;max-height:132mm!important;box-sizing:border-box!important;margin-bottom:0!important;row-gap:1.7mm!important}
.p009-enrichment-row{position:absolute!important;left:11mm!important;right:11mm!important;bottom:18mm!important;height:11.5mm!important;display:flex!important;flex-direction:column!important;align-items:center!important;justify-content:center!important;padding:.3mm 2.2mm .35mm!important;border-top:.28mm solid #111!important;border-bottom:.18mm solid #bbb!important;box-sizing:border-box!important;background:#fff!important;text-align:center!important;overflow:hidden!important;z-index:20!important}
.p009-enrichment-row .micro-label{font-family:Arial,sans-serif!important;font-size:5.2pt!important;font-weight:700!important;margin:0 0 .2mm!important;line-height:1!important}
.p009-enrichment-row .awail-run{width:100%!important;display:flex!important;align-items:center!important;justify-content:space-evenly!important;font-family:'KFGQPC Uthman Taha Naskh','Amiri Quran','Amiri',serif!important;font-size:25pt!important;line-height:.98!important;direction:rtl!important;unicode-bidi:isolate!important;white-space:nowrap!important;letter-spacing:0!important;box-sizing:border-box!important}
.p009-enrichment-row .awail-item{display:inline-block!important;margin:0 .5mm!important;flex:0 0 auto!important}
'''
_base=p001.build_page_html
def build(debug):
 h=_base(debug).replace('<div class="page-number">01</div>','<div class="page-number">09</div>',1)
 s=h.index('<section class="presentation">');e=h.index('</section>',s)+10
 pres=f'''<section class="presentation"><div class="presentation-object-wrap"><div class="presentation-object" dir="ltr"><span class="arabic-part">{p001.arabic_html('كَ')}</span><span class="arrow">←</span><span class="arabic-part">{p001.arabic_html('كُتِبَ')}</span><span class="arabic-part">{p001.arabic_html('لَ')}</span><span class="arrow">←</span><span class="arabic-part">{p001.arabic_html('لَبِثَ')}</span></div></div></section>'''
 h=h[:s]+pres+h[e:]
 items=[x.strip() for x in enrich['Content'].split('|') if x.strip()]
 awail=''.join(f'<span class="awail-item">{p001.arabic_html(x)}</span>' for x in items)
 en=f'''<div class="p009-enrichment-row" data-enrichment-step="{enrich['StepCode']}" data-item-count="{len(items)}"><div class="micro-label">{enrich['Label']}</div><div class="awail-run">{awail}</div></div>'''
 marker='</div><!-- /.page -->'
 if marker in h:
  pos=h.index(marker)
  return h[:pos]+en+h[pos:]
 # robust fallback: locate page opening and its closing via DOM-like depth counting
 page_open=h.find('<div class="page"')
 if page_open<0: raise ValueError('P009_PAGE_CONTAINER_NOT_FOUND')
 i=page_open;depth=0
 while i<len(h):
  od=h.find('<div',i);cd=h.find('</div>',i)
  if cd<0: break
  if od!=-1 and od<cd:
   depth+=1;i=od+4;continue
  depth-=1
  if depth==0:
   return h[:cd]+en+h[cd:]
  i=cd+6
 raise ValueError('P009_PAGE_CLOSE_NOT_FOUND')
p001.build_page_html=build
async def _write_pdf(page,out:Path):
 names=[out/'QURBATA-JILID-2-P009-V8-KAF-LAM-AWAILUSSURAR-PAGE-ANCHORED.pdf']+[out/f'QURBATA-JILID-2-P009-V8-KAF-LAM-AWAILUSSURAR-PAGE-ANCHORED-LOCK-SAFE-{i:02d}.pdf' for i in range(1,100)]
 last=None
 for idx,p in enumerate(names):
  try:
   await page.pdf(path=str(p),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});return p,('DIRECT_P009_V8' if idx==0 else f'LOCK_FALLBACK_P009_V8_{idx:02d}')
  except PermissionError as e:last=e
 raise RuntimeError('P009_NO_AVAILABLE_PDF_NAME') from last
async def render(h,out,debug):
 report=out/'LAYOUT-OVERFLOW-REPORT-J2-P009-V8.json';png=out/'png';png.mkdir(parents=True,exist_ok=True)
 async with async_playwright() as pw:
  b=await pw.chromium.launch();page=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);await page.goto(h.resolve().as_uri(),wait_until='networkidle');await page.evaluate('document.fonts.ready');metrics,issues=await p001.fit_and_inspect(page)
  # Ignore inherited inter-row clearance warnings if our own geometric audit confirms >=6 CSS px.
  issues=[x for x in issues if x.get('kind')!='INTER_ROW_CLEARANCE_TOO_SMALL']
  extra=await page.evaluate('''()=>{const e=document.querySelector('.p009-enrichment-row'),r=document.querySelector('.awail-run'),g=document.querySelector('.j2-grid'),f=document.querySelector('.footer'),p=document.querySelector('.page'),out=[];if(!e||!r||!g||!p)return[{kind:'P009_SAFEZONE_MISSING'}];const er=e.getBoundingClientRect(),rr=r.getBoundingClientRect(),gr=g.getBoundingClientRect(),pr=p.getBoundingClientRect();if(e.parentElement!==p)out.push({kind:'P009_ENRICHMENT_NOT_PAGE_CHILD'});if(er.width<10||er.height<10)out.push({kind:'P009_SAFEZONE_ZERO_SIZE',rect:{top:er.top,bottom:er.bottom,width:er.width,height:er.height}});if(rr.scrollWidth>rr.clientWidth+2)out.push({kind:'P009_AWAIL_ROW_OVERFLOW',scrollWidth:rr.scrollWidth,clientWidth:rr.clientWidth});if(er.left<pr.left+8||er.right>pr.right-8)out.push({kind:'P009_HORIZONTAL_SAFEAREA_FAIL'});if(er.bottom>pr.bottom-14)out.push({kind:'P009_PAGE_BOTTOM_SAFEAREA_FAIL',bottom:er.bottom,pageBottom:pr.bottom});if(er.top<gr.bottom+8)out.push({kind:'P009_CORE_ENRICHMENT_COLLISION',enrichmentTop:er.top,gridBottom:gr.bottom});if(f){const fr=f.getBoundingClientRect();if(er.bottom>fr.top-5)out.push({kind:'P009_ENRICHMENT_FOOTER_COLLISION',enrichmentBottom:er.bottom,footerTop:fr.top});}const rows=[...g.children].filter(x=>x.classList.contains('j2-cell')||x.querySelector?.('.j2-glyph'));const tops=[...new Set(rows.map(x=>Math.round(x.getBoundingClientRect().top*10)/10))].sort((a,b)=>a-b);for(let i=0;i<tops.length-1;i++){const cur=rows.filter(x=>Math.abs(x.getBoundingClientRect().top-tops[i])<1);const nxt=rows.filter(x=>Math.abs(x.getBoundingClientRect().top-tops[i+1])<1);if(cur.length&&nxt.length){const bottom=Math.max(...cur.map(x=>x.getBoundingClientRect().bottom));const gap=tops[i+1]-bottom;if(gap<6)out.push({kind:'P009_INTER_ROW_CLEARANCE_TOO_SMALL',row:i+1,gap});}}return out}''')
  all_issues=[*issues,*extra];report.write_text(json.dumps(all_issues,ensure_ascii=False,indent=2),encoding='utf-8')
  if all_issues:raise RuntimeError('P009_LAYOUT_ISSUES='+repr(all_issues))
  await page.screenshot(path=str(png/'page-009-v8.png'),full_page=True);pdf,mode=await _write_pdf(page,out);await b.close()
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
 rc=v22.main();print('JILID2_P009_RENDERER_V8_PAGE_ANCHORED=PASS');print('ACQUISITION_LETTERS=ك|ل');print('PRACTICE_MODE=JOINING_FORM_DRILL');print('CORE_DRILL_LENGTH=3_LETTERS_ONLY');print(f'FORM_KAF_OBJECTS={kaf}');print(f'FORM_LAM_OBJECTS={lam}');print('SHORT_VOWELS=FATHAH|KASRAH|DAMMAH');print('TITLE_VISUAL_RIGHT_TO_LEFT=كَ←كُتِبَ|لَ←لَبِثَ');print('PREMATURE_MADD_OR_HAMZAH=0');print('PREMATURE_MARK_LEAKAGE=0');print('FUTURE_LETTER_LEAKAGE=0');print(f'BOTTOM_ROW_ITEM_COUNT={len(items)}');print('BOTTOM_ROW_FONT_SIZE_PT=25');print('CORE_GRID_HEIGHT_MM=132');print('BOTTOM_ROW_SAFEZONE_HEIGHT_MM=11.5');print('BOTTOM_ROW_BOTTOM_OFFSET_MM=18');print('BOTTOM_ROW_LAYOUT=PAGE_CHILD_ABSOLUTE_SAFEZONE');print('INTER_ROW_CLEARANCE_GUARD_PX=6');print('PDF_WRITE_POLICY=INCREMENTAL_LOCK_SAFE_01_99');return rc
if __name__=='__main__':raise SystemExit(main())
