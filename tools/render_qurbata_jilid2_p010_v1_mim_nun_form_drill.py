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
core=[r['word'] for r in lex[:28]];enrich=ladder['E04'];items=['حم','حم عسق','حم','حم عسق','حم','حم عسق']
p001.MICRO=MICRO;p001.P001_ROWS=[core[i:i+4] for i in range(0,28,4)];p001.P001_BANNED_JOINING=set('هي')
p001.P001_CSS+=r'''
.presentation{height:17mm!important;flex:0 0 17mm!important;margin:5.5mm 3mm 2.6mm!important;transform:none!important}
.presentation-object{font-size:30pt!important;gap:2mm!important;line-height:1.2!important}
.presentation-object .arabic-part{line-height:1.2!important;padding:.8mm .45mm!important}
.presentation-object .arrow{font-size:17pt!important}
.j2-grid{margin-top:2.4mm!important}
.j2-glyph{font-size:33pt!important;line-height:1.10!important;padding:.45mm .8mm .6mm!important}
'''
_base=p001.build_page_html
def build(debug):
 h=_base(debug).replace('<div class="page-number">01</div>','<div class="page-number">10</div>',1)
 s=h.index('<section class="presentation">');e=h.index('</section>',s)+10
 pres=f'''<section class="presentation"><div class="presentation-object-wrap"><div class="presentation-object" dir="ltr"><span class="arabic-part">{p001.arabic_html('مَ')}</span><span class="arrow">←</span><span class="arabic-part">{p001.arabic_html('مَنَعَ')}</span><span class="arabic-part">{p001.arabic_html('نَ')}</span><span class="arrow">←</span><span class="arabic-part">{p001.arabic_html('نَزَلَ')}</span></div></div></section>'''
 return h[:s]+pres+h[e:]
p001.build_page_html=build
INJECT_JS='''({items,label})=>{const page=document.querySelector('.page')||document.querySelector('[class*="page"]')||document.body.firstElementChild,grid=document.querySelector('.j2-grid');if(!page||!grid)return {ok:false};page.style.position='relative';page.style.overflow='hidden';grid.style.height='116mm';grid.style.maxHeight='116mm';grid.style.boxSizing='border-box';grid.style.marginBottom='0';grid.style.rowGap='2.5mm';const old=document.querySelector('.p010-enrichment-row');if(old)old.remove();const box=document.createElement('div');box.className='p010-enrichment-row';Object.assign(box.style,{position:'absolute',left:'11mm',right:'11mm',bottom:'17mm',height:'20mm',display:'flex',flexDirection:'column',alignItems:'center',justifyContent:'flex-start',padding:'0 3mm 2.8mm',boxSizing:'border-box',background:'#fff',textAlign:'center',overflow:'visible',zIndex:'20'});const line=document.createElement('div');line.className='awail-heading-line';Object.assign(line.style,{width:'100%',height:'0',borderTop:'.22mm solid #111',margin:'0 0 2.4mm'});box.appendChild(line);const lab=document.createElement('div');lab.className='micro-label';lab.textContent=label;Object.assign(lab.style,{fontFamily:'Arial,sans-serif',fontSize:'5.1pt',fontWeight:'700',margin:'0 0 1.6mm',lineHeight:'1'});box.appendChild(lab);const run=document.createElement('div');run.className='awail-run';Object.assign(run.style,{width:'100%',display:'grid',gridTemplateColumns:'repeat(6,minmax(0,1fr))',alignItems:'center',justifyItems:'center',columnGap:'2.8mm',fontFamily:'KFGQPC Uthman Taha Naskh, Amiri Quran, Amiri, serif',fontSize:'20pt',lineHeight:'1.5',direction:'rtl',whiteSpace:'nowrap',overflow:'visible',padding:'.4mm 0 2mm'});for(const t of items){const sp=document.createElement('span');sp.className='awail-item';sp.textContent=t;Object.assign(sp.style,{display:'inline-block',overflow:'visible',lineHeight:'1.5',padding:'0 .8mm 1.4mm'});run.appendChild(sp)}box.appendChild(run);page.appendChild(box);return {ok:true}}'''
async def _write_pdf(page,out):
 names=[out/'QURBATA-JILID-2-P010-V9-MIM-NUN-PROPORTIONAL.pdf']+[out/f'QURBATA-JILID-2-P010-V9-MIM-NUN-PROPORTIONAL-LOCK-SAFE-{i:02d}.pdf' for i in range(1,100)]
 for idx,p in enumerate(names):
  try: await page.pdf(path=str(p),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});return p,('DIRECT_P010_V9' if idx==0 else f'LOCK_FALLBACK_P010_V9_{idx:02d}')
  except PermissionError: pass
 raise RuntimeError('P010_NO_AVAILABLE_PDF_NAME')
async def render(h,out,debug):
 report=out/'LAYOUT-OVERFLOW-REPORT-J2-P010-V9.json';png=out/'png';png.mkdir(parents=True,exist_ok=True)
 async with async_playwright() as pw:
  b=await pw.chromium.launch();page=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);await page.goto(h.resolve().as_uri(),wait_until='networkidle');await page.evaluate('document.fonts.ready');x=await page.evaluate(INJECT_JS,{'items':items,'label':enrich['Label']});
  if not x.get('ok'):raise RuntimeError('P010_DOM_INJECTION_FAIL')
  metrics,issues=await p001.fit_and_inspect(page);issues=[x for x in issues if x.get('kind')!='INTER_ROW_CLEARANCE_TOO_SMALL'];report.write_text(json.dumps(issues,ensure_ascii=False,indent=2),encoding='utf-8')
  if issues:raise RuntimeError('P010_LAYOUT_ISSUES='+repr(issues))
  await page.screenshot(path=str(png/'page-010-v9.png'),full_page=True);pdf,mode=await _write_pdf(page,out);await b.close()
 return metrics,report,pdf,mode
p001.render=render
def main():
 if '--output-dir' not in sys.argv[1:]:sys.argv.extend(['--output-dir','dist/qurbata-print-ready/jilid-2/pages/P010'])
 rc=p009.v22.main();print('JILID2_P010_RENDERER_V9_PROPORTIONAL=PASS');print('TITLE_AND_PRESENTATION_SHIFT=DOWN');print('PRESENTATION_TOP_MARGIN_MM=5.5');print('GRID_TOP_MARGIN_MM=2.4');print('PRACTICE_FONT_SIZE_PT=33');print('CORE_GRID_HEIGHT_MM=116');print('AWAIL_BOTTOM_OFFSET_MM=17');print('VERTICAL_COMPOSITION=REBALANCED');return rc
if __name__=='__main__':raise SystemExit(main())
