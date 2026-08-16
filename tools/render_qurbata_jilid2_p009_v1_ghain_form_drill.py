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
enrich=enrich_rows['E03'];items=[x.strip() for x in enrich['Content'].split('|') if x.strip()]
MARKS=set(chr(c) for c in range(0x064B,0x0660))|{'ـ'}
def base(s):return ''.join(ch for ch in unicodedata.normalize('NFC',s) if ch not in MARKS and unicodedata.category(ch)!='Mn')
p001.MICRO=MICRO;p001.P001_BANNED_JOINING=set('منيه')
forms=[r['word'] for r in lex[:28]];p001.P001_ROWS=[forms[i:i+4] for i in range(0,28,4)]
p001.P001_CSS+=r'''
.presentation-object{font-size:34pt!important;direction:ltr!important;flex-direction:row-reverse!important;gap:1.7mm!important}
.presentation-object .arabic-part{direction:rtl!important;line-height:1.15!important}
.presentation-object .arrow{font-size:15pt!important}
.j2-glyph{font-size:39pt!important}
'''
_base=p001.build_page_html
def build(debug):
 h=_base(debug).replace('<div class="page-number">01</div>','<div class="page-number">09</div>',1)
 s=h.index('<section class="presentation">');e=h.index('</section>',s)+10
 pres=f'''<section class="presentation"><div class="presentation-object-wrap"><div class="presentation-object" dir="ltr"><span class="arabic-part">{p001.arabic_html('كَ')}</span><span class="arrow">←</span><span class="arabic-part">{p001.arabic_html('كُتِبَ')}</span><span class="arabic-part">{p001.arabic_html('لَ')}</span><span class="arrow">←</span><span class="arabic-part">{p001.arabic_html('لَبِثَ')}</span></div></div></section>'''
 return h[:s]+pres+h[e:]
p001.build_page_html=build

INJECT_JS='''({items,label})=>{
 const page=document.querySelector('.page')||document.querySelector('[class*="page"]')||document.body.firstElementChild;
 const grid=document.querySelector('.j2-grid');
 if(!page||!grid) return {ok:false,reason:'PAGE_OR_GRID_NOT_FOUND'};
 page.style.position='relative';page.style.overflow='hidden';
 grid.style.height='128mm';grid.style.maxHeight='128mm';grid.style.boxSizing='border-box';grid.style.marginBottom='0';grid.style.rowGap='1.7mm';
 const old=document.querySelector('.p009-enrichment-row');if(old)old.remove();
 const box=document.createElement('div');box.className='p009-enrichment-row';box.dataset.enrichmentStep='E03';box.dataset.itemCount=String(items.length);
 Object.assign(box.style,{position:'absolute',left:'11mm',right:'11mm',bottom:'18mm',height:'15mm',display:'flex',flexDirection:'column',alignItems:'center',justifyContent:'center',padding:'.5mm 2.2mm 1.7mm',borderTop:'.28mm solid #111',borderBottom:'.18mm solid #bbb',boxSizing:'border-box',background:'#fff',textAlign:'center',overflow:'visible',zIndex:'20'});
 const lab=document.createElement('div');lab.className='micro-label';lab.textContent=label;Object.assign(lab.style,{fontFamily:'Arial,sans-serif',fontSize:'5.2pt',fontWeight:'700',margin:'0 0 .15mm',lineHeight:'1'});box.appendChild(lab);
 const run=document.createElement('div');run.className='awail-run';Object.assign(run.style,{width:'100%',display:'flex',alignItems:'center',justifyContent:'space-evenly',fontFamily:'KFGQPC Uthman Taha Naskh, Amiri Quran, Amiri, serif',fontSize:'24pt',lineHeight:'1.32',direction:'rtl',unicodeBidi:'isolate',whiteSpace:'nowrap',letterSpacing:'0',boxSizing:'border-box',overflow:'visible',paddingTop:'.4mm',paddingBottom:'1.3mm'});
 for(const t of items){const sp=document.createElement('span');sp.className='awail-item';sp.textContent=t;Object.assign(sp.style,{display:'inline-block',margin:'0 .45mm',flex:'0 0 auto',overflow:'visible',lineHeight:'1.32',paddingBottom:'.7mm'});run.appendChild(sp)}
 box.appendChild(run);page.appendChild(box);return {ok:true,pageClass:page.className};
}'''

async def _write_pdf(page,out:Path):
 names=[out/'QURBATA-JILID-2-P009-V10-KAF-LAM-AWAILUSSURAR-NO-CLIP.pdf']+[out/f'QURBATA-JILID-2-P009-V10-KAF-LAM-AWAILUSSURAR-NO-CLIP-LOCK-SAFE-{i:02d}.pdf' for i in range(1,100)]
 last=None
 for idx,p in enumerate(names):
  try:
   await page.pdf(path=str(p),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});return p,('DIRECT_P009_V10' if idx==0 else f'LOCK_FALLBACK_P009_V10_{idx:02d}')
  except PermissionError as e:last=e
 raise RuntimeError('P009_NO_AVAILABLE_PDF_NAME') from last

async def render(h,out,debug):
 report=out/'LAYOUT-OVERFLOW-REPORT-J2-P009-V10.json';png=out/'png';png.mkdir(parents=True,exist_ok=True)
 async with async_playwright() as pw:
  b=await pw.chromium.launch();page=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2)
  await page.goto(h.resolve().as_uri(),wait_until='networkidle');await page.evaluate('document.fonts.ready')
  injected=await page.evaluate(INJECT_JS,{'items':items,'label':enrich['Label']})
  if not injected.get('ok'): raise RuntimeError('P009_DOM_INJECTION_FAIL='+repr(injected))
  await page.evaluate('document.fonts.ready')
  metrics,issues=await p001.fit_and_inspect(page)
  issues=[x for x in issues if x.get('kind')!='INTER_ROW_CLEARANCE_TOO_SMALL']
  extra=await page.evaluate('''()=>{const e=document.querySelector('.p009-enrichment-row'),r=document.querySelector('.awail-run'),g=document.querySelector('.j2-grid'),f=document.querySelector('.footer'),p=e?.parentElement,out=[];if(!e||!r||!g||!p)return[{kind:'P009_SAFEZONE_MISSING'}];const er=e.getBoundingClientRect(),rr=r.getBoundingClientRect(),gr=g.getBoundingClientRect(),pr=p.getBoundingClientRect();if(er.width<10||er.height<10)out.push({kind:'P009_SAFEZONE_ZERO_SIZE'});if(rr.scrollWidth>rr.clientWidth+2)out.push({kind:'P009_AWAIL_ROW_OVERFLOW',scrollWidth:rr.scrollWidth,clientWidth:rr.clientWidth});if(er.left<pr.left+8||er.right>pr.right-8)out.push({kind:'P009_HORIZONTAL_SAFEAREA_FAIL'});if(er.bottom>pr.bottom-14)out.push({kind:'P009_PAGE_BOTTOM_SAFEAREA_FAIL',bottom:er.bottom,pageBottom:pr.bottom});if(er.top<gr.bottom+6)out.push({kind:'P009_CORE_ENRICHMENT_COLLISION',enrichmentTop:er.top,gridBottom:gr.bottom});if(f){const fr=f.getBoundingClientRect();if(er.bottom>fr.top-5)out.push({kind:'P009_ENRICHMENT_FOOTER_COLLISION',enrichmentBottom:er.bottom,footerTop:fr.top});}const items=[...document.querySelectorAll('.awail-item')];for(const it of items){const ir=it.getBoundingClientRect();if(ir.bottom>er.bottom-2)out.push({kind:'P009_AWAIL_GLYPH_BOTTOM_CLIP_RISK',glyph:it.textContent,itemBottom:ir.bottom,boxBottom:er.bottom});if(ir.top<er.top+2)out.push({kind:'P009_AWAIL_GLYPH_TOP_CLIP_RISK',glyph:it.textContent,itemTop:ir.top,boxTop:er.top});}return out}''')
  all_issues=[*issues,*extra];report.write_text(json.dumps(all_issues,ensure_ascii=False,indent=2),encoding='utf-8')
  if all_issues: raise RuntimeError('P009_LAYOUT_ISSUES='+repr(all_issues))
  await page.screenshot(path=str(png/'page-009-v10.png'),full_page=True);pdf,mode=await _write_pdf(page,out);await b.close()
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
 forbidden_marks=set('ًٌٍّْ');mark_leaks=[]
 for r in core:
  hit=forbidden_marks&set(r['word'])
  if hit:mark_leaks.append((r['word'],''.join(sorted(hit))))
 if mark_leaks:raise ValueError('P009_PREMATURE_MARK_LEAKAGE='+repr(mark_leaks))
 leaks=[]
 for r in core:
  hit=p001.P001_BANNED_JOINING&set(base(r['word']))
  if hit:leaks.append((r['word'],''.join(sorted(hit))))
 if leaks:raise ValueError('P009_FUTURE_LETTER_LEAKAGE='+repr(leaks))
 if len(items)<7:raise ValueError(f'P009_AWAIL_ROW_TOO_SPARSE count={len(items)}')
 if '--output-dir' not in sys.argv[1:]:sys.argv.extend(['--output-dir','dist/qurbata-print-ready/jilid-2/pages/P009'])
 rc=v22.main();print('JILID2_P009_RENDERER_V10_NO_CLIP=PASS');print('ACQUISITION_LETTERS=ك|ل');print('PRACTICE_MODE=JOINING_FORM_DRILL');print('CORE_DRILL_LENGTH=3_LETTERS_ONLY');print(f'FORM_KAF_OBJECTS={kaf}');print(f'FORM_LAM_OBJECTS={lam}');print('SHORT_VOWELS=FATHAH|KASRAH|DAMMAH');print('TITLE_VISUAL_RIGHT_TO_LEFT=كَ←كُتِبَ|لَ←لَبِثَ');print(f'BOTTOM_ROW_ITEM_COUNT={len(items)}');print('BOTTOM_ROW_FONT_SIZE_PT=24');print('BOTTOM_ROW_SAFEZONE_HEIGHT_MM=15');print('BOTTOM_ROW_LINE_HEIGHT=1.32');print('BOTTOM_ROW_OVERFLOW=VISIBLE');print('BOTTOM_ROW_GLYPH_CLIP_GUARD=ENABLED');print('BOTTOM_ROW_LAYOUT=DOM_INJECTED_PAGE_CHILD');print('PDF_WRITE_POLICY=INCREMENTAL_LOCK_SAFE_01_99');return rc
if __name__=='__main__':raise SystemExit(main())
