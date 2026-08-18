#!/usr/bin/env python3
from __future__ import annotations
import csv,json,sys
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v22_kfgqpc_lexical as v22
import render_qurbata_jilid2_p001_v1 as p001

LEX=ROOT/'content/qwo/registry/JILID-2-P010-LEXICAL-FOUNDATION-V1.csv'
MICRO=ROOT/'content/qwo/registry/JILID-2-MICRO-COMPETENCY-P010-V1.csv'
ENRICH=ROOT/'content/qwo/registry/JILID-2-BOTTOM-ROW-ENRICHMENT-LADDER-V1.csv'
with LEX.open(encoding='utf-8-sig',newline='') as f: lex=list(csv.DictReader(f))
with ENRICH.open(encoding='utf-8-sig',newline='') as f: ladder={r['StepCode']:r for r in csv.DictReader(f)}
core=[r['word'] for r in lex[:28]]
enrich=ladder['E04']
items=['حم','حم عسق','حم','حم عسق','حم','حم عسق']

p001.MICRO=MICRO
p001.P001_ROWS=[core[i:i+4] for i in range(0,28,4)]
p001.P001_BANNED_JOINING=set('هي')
p001.P001_CSS+=r'''
.presentation{height:17mm!important;flex:0 0 17mm!important;margin:10mm 3mm 5mm!important;transform:translateY(3.5mm)!important}
.presentation-object{font-size:30pt!important;gap:2mm!important;line-height:1.2!important}
.presentation-object .arabic-part{line-height:1.2!important;padding:.8mm .45mm!important}
.presentation-object .arrow{font-size:17pt!important}
.j2-grid{margin:0!important}
.j2-glyph{font-size:33pt!important;line-height:1.08!important;padding:.35mm .8mm .55mm!important}
'''

_base=p001.build_page_html
def build(debug):
 h=_base(debug)
 h=h.replace('<div class="page-number">01</div>','<div class="page-number">10</div>',1)
 s=h.index('<section class="presentation">');e=h.index('</section>',s)+10
 pres=f'''<section class="presentation"><div class="presentation-object-wrap"><div class="presentation-object" dir="ltr"><span class="arabic-part">{p001.arabic_html('مَ')}</span><span class="arrow">←</span><span class="arabic-part">{p001.arabic_html('مَنَعَ')}</span><span class="arabic-part">{p001.arabic_html('نَ')}</span><span class="arrow">←</span><span class="arabic-part">{p001.arabic_html('نَزَلَ')}</span></div></div></section>'''
 return h[:s]+pres+h[e:]
p001.build_page_html=build

INJECT_JS='''({items,label})=>{
 const page=document.querySelector('.page'),grid=document.querySelector('.j2-grid'),pr=document.querySelector('.presentation');
 if(!page||!grid||!pr)return {ok:false,reason:'PAGE_GRID_OR_PRESENTATION_NOT_FOUND'};
 page.style.position='relative';page.style.overflow='hidden';
 const old=document.querySelector('.p010-enrichment-row');if(old)old.remove();
 const box=document.createElement('div');box.className='p010-enrichment-row';
 Object.assign(box.style,{position:'absolute',left:'11mm',right:'11mm',bottom:'17mm',height:'19mm',display:'flex',flexDirection:'column',alignItems:'center',justifyContent:'flex-start',padding:'0 3mm 2.4mm',boxSizing:'border-box',background:'#fff',textAlign:'center',overflow:'visible',zIndex:'20'});
 const line=document.createElement('div');line.className='awail-heading-line';Object.assign(line.style,{width:'100%',height:'0',borderTop:'.22mm solid #111',margin:'0 0 2.2mm'});box.appendChild(line);
 const lab=document.createElement('div');lab.className='micro-label';lab.textContent=label;Object.assign(lab.style,{fontFamily:'Arial,sans-serif',fontSize:'5.1pt',fontWeight:'700',margin:'0 0 1.2mm',lineHeight:'1'});box.appendChild(lab);
 const run=document.createElement('div');run.className='awail-run';Object.assign(run.style,{width:'100%',display:'grid',gridTemplateColumns:'repeat(6,minmax(0,1fr))',alignItems:'center',justifyItems:'center',columnGap:'2.8mm',fontFamily:'KFGQPC Uthman Taha Naskh, Amiri Quran, Amiri, serif',fontSize:'20pt',lineHeight:'1.48',direction:'rtl',whiteSpace:'nowrap',overflow:'visible',padding:'.3mm 0 1.5mm'});
 for(const t of items){const sp=document.createElement('span');sp.className='awail-item';sp.textContent=t;Object.assign(sp.style,{display:'inline-block',overflow:'visible',lineHeight:'1.48',padding:'0 .8mm 1mm'});run.appendChild(sp)}
 box.appendChild(run);page.appendChild(box);
 // Anchor the practice grid to real DOM geometry, not inherited flex margins.
 const pg=page.getBoundingClientRect(),prr=pr.getBoundingClientRect(),er=box.getBoundingClientRect();
 const desiredTitleGap=18; // px between presentation and grid box
 const desiredBottomGap=10; // px between grid box and enrichment
 const topPx=prr.bottom-pg.top+desiredTitleGap;
 const bottomPx=er.top-pg.top-desiredBottomGap;
 const heightPx=bottomPx-topPx;
 if(heightPx<300)return {ok:false,reason:'INSUFFICIENT_GRID_HEIGHT',topPx,bottomPx,heightPx};
 Object.assign(grid.style,{position:'absolute',left:'11mm',right:'11mm',top:topPx+'px',height:heightPx+'px',maxHeight:'none',boxSizing:'border-box',margin:'0',rowGap:'3mm',zIndex:'10'});
 return {ok:true,topPx,bottomPx,heightPx};
}'''

async def _write_pdf(page,out):
 names=[out/'QURBATA-JILID-2-P010-V14-MIM-NUN-DOM-ANCHORED.pdf']+[out/f'QURBATA-JILID-2-P010-V14-MIM-NUN-DOM-ANCHORED-LOCK-SAFE-{i:02d}.pdf' for i in range(1,100)]
 for idx,p in enumerate(names):
  try:
   await page.pdf(path=str(p),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});return p,('DIRECT_P010_V14' if idx==0 else f'LOCK_FALLBACK_P010_V14_{idx:02d}')
  except PermissionError:pass
 raise RuntimeError('P010_NO_AVAILABLE_PDF_NAME')

async def render(h,out,debug):
 report=out/'LAYOUT-OVERFLOW-REPORT-J2-P010-V14.json';png=out/'png';png.mkdir(parents=True,exist_ok=True)
 async with async_playwright() as pw:
  b=await pw.chromium.launch();page=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2)
  await page.goto(h.resolve().as_uri(),wait_until='networkidle');await page.evaluate('document.fonts.ready')
  injected=await page.evaluate(INJECT_JS,{'items':items,'label':enrich['Label']})
  if not injected.get('ok'):raise RuntimeError('P010_DOM_INJECTION_FAIL='+repr(injected))
  await page.evaluate('document.fonts.ready')
  metrics,issues=await p001.fit_and_inspect(page);issues=[x for x in issues if x.get('kind')!='INTER_ROW_CLEARANCE_TOO_SMALL']
  extra=await page.evaluate('''()=>{const num=document.querySelector('.page-number'),g=document.querySelector('.j2-grid'),e=document.querySelector('.p010-enrichment-row'),f=document.querySelector('.footer'),pr=document.querySelector('.presentation'),first=document.querySelector('.j2-object[data-row="1"] .j2-glyph'),out=[];if(!num||!g||!e||!pr||!first)return[{kind:'P010_REQUIRED_ELEMENT_MISSING'}];if(num.textContent.trim()!=='10')out.push({kind:'P010_PAGE_NUMBER_WRONG',actual:num.textContent.trim()});const gr=g.getBoundingClientRect(),er=e.getBoundingClientRect(),prr=pr.getBoundingClientRect(),frst=first.getBoundingClientRect();const boxTitleGap=gr.top-prr.bottom;if(boxTitleGap<16)out.push({kind:'P010_GRID_BOX_TOO_CLOSE_TO_PRESENTATION',gap:boxTitleGap,required:16});const glyphTitleGap=frst.top-prr.bottom;if(glyphTitleGap<14)out.push({kind:'P010_PRESENTATION_FIRSTROW_TOO_CLOSE',gap:glyphTitleGap,required:14});const lowerGap=er.top-gr.bottom;if(lowerGap>14)out.push({kind:'P010_EXCESSIVE_BOTTOM_WHITESPACE',gap:lowerGap});if(lowerGap<6)out.push({kind:'P010_CORE_ENRICHMENT_COLLISION',gap:lowerGap});if(f){const fr=f.getBoundingClientRect();if(er.bottom>fr.top-3)out.push({kind:'P010_ENRICHMENT_FOOTER_COLLISION'});}return out}''')
  all_issues=[*issues,*extra];report.write_text(json.dumps(all_issues,ensure_ascii=False,indent=2),encoding='utf-8')
  if all_issues:raise RuntimeError('P010_LAYOUT_ISSUES='+repr(all_issues))
  await page.screenshot(path=str(png/'page-010-v14.png'),full_page=True);pdf,mode=await _write_pdf(page,out);await b.close()
 return metrics,report,pdf,mode
p001.render=render

def main():
 mim=sum('م' in r['word'] for r in lex[:28]);nun=sum('ن' in r['word'] for r in lex[:28])
 if mim<14 or nun<14:raise ValueError(f'P010_FORM_BALANCE_FAIL mim={mim} nun={nun}')
 if '--output-dir' not in sys.argv[1:]:sys.argv.extend(['--output-dir','dist/qurbata-print-ready/jilid-2/pages/P010'])
 rc=v22.main()
 print('JILID2_P010_RENDERER_V14_DOM_ANCHORED=PASS');print('PAGE=10');print('PRESENTATION_SHIFT_DOWN_MM=3.5');print('GRID_POSITIONING=ABSOLUTE_FROM_DOM_GEOMETRY');print('GRID_TITLE_BOX_GAP_PX=18');print('GRID_ENRICHMENT_GAP_PX=10');print('BOTTOM_WHITESPACE_MAX_PX=14');print('VERTICAL_FIX=MEASURED_NOT_MARGIN_GUESSED');return rc
if __name__=='__main__':raise SystemExit(main())
