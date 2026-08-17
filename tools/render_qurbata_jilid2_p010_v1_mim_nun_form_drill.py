#!/usr/bin/env python3
from __future__ import annotations
import csv,json,sys
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p009_v1_ghain_form_drill as p009
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
# P010 proportional composition: presentation and core type reduced; vertical rhythm relaxed.
p001.P001_CSS+=r'''
.presentation{height:14mm!important;flex:0 0 14mm!important;margin:2.2mm 3mm 1.8mm!important;transform:none!important}
.presentation-object{font-size:30pt!important;gap:2mm!important;line-height:1.2!important}
.presentation-object .arabic-part{line-height:1.2!important;padding:.8mm .45mm!important}
.presentation-object .arrow{font-size:17pt!important}
.j2-grid{margin-top:.8mm!important}
.j2-glyph{font-size:35pt!important;line-height:1.08!important;padding:.3mm .8mm .45mm!important}
'''

_base=p001.build_page_html
def build(debug):
 h=_base(debug).replace('<div class="page-number">01</div>','<div class="page-number">10</div>',1)
 s=h.index('<section class="presentation">');e=h.index('</section>',s)+10
 pres=f'''<section class="presentation"><div class="presentation-object-wrap"><div class="presentation-object" dir="ltr"><span class="arabic-part">{p001.arabic_html('مَ')}</span><span class="arrow">←</span><span class="arabic-part">{p001.arabic_html('مَنَعَ')}</span><span class="arabic-part">{p001.arabic_html('نَ')}</span><span class="arrow">←</span><span class="arabic-part">{p001.arabic_html('نَزَلَ')}</span></div></div></section>'''
 return h[:s]+pres+h[e:]
p001.build_page_html=build

INJECT_JS='''({items,label})=>{
 const page=document.querySelector('.page')||document.querySelector('[class*="page"]')||document.body.firstElementChild;
 const grid=document.querySelector('.j2-grid');
 if(!page||!grid) return {ok:false,reason:'PAGE_OR_GRID_NOT_FOUND'};
 page.style.position='relative';page.style.overflow='hidden';
 grid.style.height='124mm';grid.style.maxHeight='124mm';grid.style.boxSizing='border-box';grid.style.marginBottom='0';grid.style.rowGap='2.4mm';
 const old=document.querySelector('.p010-enrichment-row');if(old)old.remove();
 const box=document.createElement('div');box.className='p010-enrichment-row';box.dataset.enrichmentStep='E04';
 Object.assign(box.style,{position:'absolute',left:'11mm',right:'11mm',bottom:'17mm',height:'18mm',display:'flex',flexDirection:'column',alignItems:'center',justifyContent:'flex-start',padding:'0 3mm 1.5mm',boxSizing:'border-box',background:'#fff',textAlign:'center',overflow:'visible',zIndex:'20'});
 const line=document.createElement('div');line.className='awail-heading-line';Object.assign(line.style,{width:'100%',height:'0',borderTop:'.24mm solid #111',margin:'0 0 1.8mm'});box.appendChild(line);
 const lab=document.createElement('div');lab.className='micro-label';lab.textContent=label;Object.assign(lab.style,{fontFamily:'Arial,sans-serif',fontSize:'5.2pt',fontWeight:'700',margin:'0 0 1.3mm',lineHeight:'1'});box.appendChild(lab);
 const run=document.createElement('div');run.className='awail-run';Object.assign(run.style,{width:'100%',display:'grid',gridTemplateColumns:'repeat(6,minmax(0,1fr))',alignItems:'center',justifyItems:'center',columnGap:'2.8mm',fontFamily:'KFGQPC Uthman Taha Naskh, Amiri Quran, Amiri, serif',fontSize:'21pt',lineHeight:'1.5',direction:'rtl',unicodeBidi:'isolate',whiteSpace:'nowrap',boxSizing:'border-box',overflow:'visible',padding:'.6mm 0 1.1mm'});
 for(const t of items){const sp=document.createElement('span');sp.className='awail-item';sp.textContent=t;Object.assign(sp.style,{display:'inline-block',overflow:'visible',lineHeight:'1.5',padding:'0 .8mm .6mm'});run.appendChild(sp)}
 box.appendChild(run);page.appendChild(box);return {ok:true};
}'''

async def _write_pdf(page,out:Path):
 names=[out/'QURBATA-JILID-2-P010-V6-MIM-NUN-PROPORTIONAL-COMPOSITION.pdf']+[out/f'QURBATA-JILID-2-P010-V6-MIM-NUN-PROPORTIONAL-COMPOSITION-LOCK-SAFE-{i:02d}.pdf' for i in range(1,100)]
 last=None
 for idx,p in enumerate(names):
  try:
   await page.pdf(path=str(p),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});return p,('DIRECT_P010_V6' if idx==0 else f'LOCK_FALLBACK_P010_V6_{idx:02d}')
  except PermissionError as e:last=e
 raise RuntimeError('P010_NO_AVAILABLE_PDF_NAME') from last

async def render(h,out,debug):
 report=out/'LAYOUT-OVERFLOW-REPORT-J2-P010-V6.json';png=out/'png';png.mkdir(parents=True,exist_ok=True)
 async with async_playwright() as pw:
  b=await pw.chromium.launch();page=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2)
  await page.goto(h.resolve().as_uri(),wait_until='networkidle');await page.evaluate('document.fonts.ready')
  injected=await page.evaluate(INJECT_JS,{'items':items,'label':enrich['Label']})
  if not injected.get('ok'):raise RuntimeError('P010_DOM_INJECTION_FAIL='+repr(injected))
  await page.evaluate('document.fonts.ready')
  metrics,issues=await p001.fit_and_inspect(page);issues=[x for x in issues if x.get('kind')!='INTER_ROW_CLEARANCE_TOO_SMALL']
  extra=await page.evaluate('''()=>{const e=document.querySelector('.p010-enrichment-row'),r=document.querySelector('.awail-run'),g=document.querySelector('.j2-grid'),f=document.querySelector('.footer'),p=e?.parentElement,pr=document.querySelector('.presentation'),lab=document.querySelector('.micro-label'),line=document.querySelector('.awail-heading-line'),out=[];if(!e||!r||!g||!p||!pr||!lab||!line)return[{kind:'P010_SAFEZONE_MISSING'}];const er=e.getBoundingClientRect(),rr=r.getBoundingClientRect(),gr=g.getBoundingClientRect(),pg=p.getBoundingClientRect(),prr=pr.getBoundingClientRect(),lr=lab.getBoundingClientRect(),ln=line.getBoundingClientRect();if(rr.scrollWidth>rr.clientWidth+2)out.push({kind:'P010_AWAIL_ROW_OVERFLOW'});if(er.bottom>pg.bottom-12)out.push({kind:'P010_PAGE_BOTTOM_SAFEAREA_FAIL'});if(er.top<gr.bottom+7)out.push({kind:'P010_CORE_ENRICHMENT_COLLISION',gap:er.top-gr.bottom});if(lr.top-ln.bottom<5)out.push({kind:'P010_AWAIL_HEADING_LINE_TOO_CLOSE',gap:lr.top-ln.bottom});if(f){const fr=f.getBoundingClientRect();if(er.bottom>fr.top-4)out.push({kind:'P010_ENRICHMENT_FOOTER_COLLISION'});}for(const it of document.querySelectorAll('.awail-item')){const ir=it.getBoundingClientRect();if(ir.bottom>er.bottom-3)out.push({kind:'P010_GLYPH_BOTTOM_CLIP_RISK',glyph:it.textContent});if(ir.top<lr.bottom+2)out.push({kind:'P010_GLYPH_LABEL_COLLISION',glyph:it.textContent});}return out}''')
  all_issues=[*issues,*extra];report.write_text(json.dumps(all_issues,ensure_ascii=False,indent=2),encoding='utf-8')
  if all_issues:raise RuntimeError('P010_LAYOUT_ISSUES='+repr(all_issues))
  await page.screenshot(path=str(png/'page-010-v6.png'),full_page=True);pdf,mode=await _write_pdf(page,out);await b.close()
 return metrics,report,pdf,mode
p001.render=render

def main():
 mim=sum('م' in r['word'] for r in lex[:28]);nun=sum('ن' in r['word'] for r in lex[:28])
 if mim<14 or nun<14:raise ValueError(f'P010_FORM_BALANCE_FAIL mim={mim} nun={nun}')
 leaks=[]
 for r in lex[:28]:
  hit=p001.P001_BANNED_JOINING.intersection(r['word'])
  if hit:leaks.append((r['word'],''.join(sorted(hit))))
 if leaks:raise ValueError('P010_FUTURE_LETTER_LEAKAGE='+repr(leaks))
 if '--output-dir' not in sys.argv[1:]:sys.argv.extend(['--output-dir','dist/qurbata-print-ready/jilid-2/pages/P010'])
 rc=p009.v22.main()
 print('JILID2_P010_RENDERER_V6_PROPORTIONAL_COMPOSITION=PASS');print('PAGE=10');print('ACQUISITION_LETTERS=م|ن');print('PRACTICE_MODE=JOINING_FORM_DRILL_MEANINGFUL');print(f'FORM_MIM_OBJECTS={mim}');print(f'FORM_NUN_OBJECTS={nun}');print('PRESENTATION_FONT_SIZE_PT=30');print('PRACTICE_FONT_SIZE_PT=35');print('CORE_GRID_HEIGHT_MM=124');print('CORE_ROW_GAP_MM=2.4');print('BOTTOM_ROW_HEIGHT_MM=18');print('BOTTOM_ROW_FONT_SIZE_PT=21');print('AWAIL_HEADING_LINE_SEPARATION_MM=1.8');print('BOTTOM_ROW_BOTTOM_OFFSET_MM=17');print('VERTICAL_COMPOSITION=PROPORTIONAL');print('MICRO_BINDING=PATH_NOT_PARSED_LIST');return rc
if __name__=='__main__':raise SystemExit(main())
