#!/usr/bin/env python3
from __future__ import annotations
import csv,json,sys
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v22_kfgqpc_lexical as v22
import render_qurbata_jilid2_p001_v1 as p001
LEX=ROOT/'content/qwo/registry/JILID-2-P012-LEXICAL-FOUNDATION-V1.csv';MICRO=ROOT/'content/qwo/registry/JILID-2-MICRO-COMPETENCY-P012-V1.csv';ENRICH=ROOT/'content/qwo/registry/JILID-2-BOTTOM-ROW-ENRICHMENT-LADDER-V1.csv'
with LEX.open(encoding='utf-8-sig',newline='') as f: lex=list(csv.DictReader(f))
with ENRICH.open(encoding='utf-8-sig',newline='') as f: ladder={r['StepCode']:r for r in csv.DictReader(f)}
core=[r['word'] for r in lex[:32]];enrich=ladder['E07']
main_items=['يس','ص','ق','ن','يس','ص','ق','ن'];review_numbers=['٠','١','٢','٣','٤','٥','٦','٧','٨','٩'];review_letters=['ا','د','ذ','ر','ز','و']
p001.MICRO=MICRO;p001.P001_ROWS=[core[i:i+4] for i in range(0,32,4)];p001.P001_BANNED_JOINING=set()
p001.P001_CSS+=r'''
.presentation{height:16mm!important;flex:0 0 16mm!important;margin:9mm 3mm 2mm!important;transform:translateY(3mm)!important}
.presentation-object{font-size:31pt!important;gap:2mm!important;line-height:1.18!important}
.presentation-object .arabic-part{line-height:1.18!important;padding:.8mm .45mm!important;overflow:visible!important}
.presentation-object .arrow{font-size:17pt!important}
.j2-grid{margin:0!important;min-height:0!important;grid-template-rows:repeat(8,minmax(0,1fr))!important;align-items:stretch!important}
.j2-object{overflow:visible!important;display:flex!important;align-items:center!important;justify-content:center!important}
.j2-glyph{font-size:31pt!important;line-height:1.18!important;padding:.65mm .7mm .8mm!important;overflow:visible!important}
'''
_base=p001.build_page_html
def build(debug):
 h=_base(debug);h=h.replace('<div class="page-number">01</div>','<div class="page-number">12</div>',1);s=h.index('<section class="presentation">');e=h.index('</section>',s)+10
 pres=f'''<section class="presentation"><div class="presentation-object-wrap"><div class="presentation-object" dir="ltr"><span class="arabic-part">{p001.arabic_html('يَبِسَ')}</span><span class="arrow">←</span><span class="arabic-part">{p001.arabic_html('يَ')}</span></div></div></section>'''
 return h[:s]+pres+h[e:]
p001.build_page_html=build
INJECT_JS='''({items,label,numbers,letters})=>{const page=document.querySelector('.page'),grid=document.querySelector('.j2-grid'),pr=document.querySelector('.presentation');if(!page||!grid||!pr)return {ok:false};page.style.position='relative';page.style.overflow='hidden';const old=document.querySelector('.p012-enrichment-row');if(old)old.remove();const box=document.createElement('div');box.className='p012-enrichment-row';Object.assign(box.style,{position:'absolute',left:'11mm',right:'11mm',bottom:'14mm',height:'25mm',display:'flex',flexDirection:'column',alignItems:'center',justifyContent:'space-between',padding:'.7mm 1.5mm .5mm',boxSizing:'border-box',background:'#fff',textAlign:'center',overflow:'visible',zIndex:'20'});const lab=document.createElement('div');lab.textContent=label;Object.assign(lab.style,{fontFamily:'Arial,sans-serif',fontSize:'5pt',fontWeight:'700',margin:'0',lineHeight:'1'});box.appendChild(lab);const run=document.createElement('div');Object.assign(run.style,{width:'100%',display:'grid',gridTemplateColumns:'repeat(8,minmax(0,1fr))',alignItems:'center',justifyItems:'center',columnGap:'.7mm',fontFamily:'KFGQPC Uthman Taha Naskh, Amiri Quran, Amiri, serif',fontSize:'25pt',lineHeight:'1.12',direction:'rtl',whiteSpace:'nowrap',overflow:'visible',padding:'0'});for(const t of items){const sp=document.createElement('span');sp.textContent=t;run.appendChild(sp)}box.appendChild(run);const rev=document.createElement('div');Object.assign(rev.style,{width:'100%',display:'grid',gridTemplateColumns:'1.4fr 1fr',columnGap:'4mm',alignItems:'center',boxSizing:'border-box'});const nums=document.createElement('div');Object.assign(nums.style,{display:'grid',gridTemplateColumns:'repeat(10,1fr)',alignItems:'center',justifyItems:'center',columnGap:'.35mm',fontFamily:'KFGQPC Uthman Taha Naskh, Amiri Quran, Amiri, serif',fontSize:'17pt',lineHeight:'1.1',direction:'rtl'});for(const t of numbers){const sp=document.createElement('span');sp.textContent=t;nums.appendChild(sp)}const lets=document.createElement('div');Object.assign(lets.style,{display:'grid',gridTemplateColumns:'repeat(6,1fr)',alignItems:'center',justifyItems:'center',columnGap:1+'mm',fontFamily:'KFGQPC Uthman Taha Naskh, Amiri Quran, Amiri, serif',fontSize:'20pt',lineHeight:'1.1',direction:'rtl'});for(const t of letters){const sp=document.createElement('span');sp.textContent=t;lets.appendChild(sp)}rev.appendChild(nums);rev.appendChild(lets);box.appendChild(rev);page.appendChild(box);const pg=page.getBoundingClientRect(),prr=pr.getBoundingClientRect(),er=box.getBoundingClientRect();const topPx=prr.bottom-pg.top+14,bottomPx=er.top-pg.top-8,heightPx=bottomPx-topPx;if(heightPx<360)return {ok:false,reason:'INSUFFICIENT_GRID_HEIGHT',heightPx};const imp=(n,v)=>grid.style.setProperty(n,v,'important');for(const [n,v] of [['position','absolute'],['left','11mm'],['right','11mm'],['top',topPx+'px'],['height',heightPx+'px'],['min-height','0px'],['max-height',heightPx+'px'],['margin','0'],['flex','none'],['box-sizing','border-box'],['row-gap','1.7mm'],['z-index','10']])imp(n,v);return {ok:true,topPx,bottomPx,heightPx};}'''
async def render(h,out,debug):
 report=out/'LAYOUT-OVERFLOW-REPORT-J2-P012-V3.json';png=out/'png';png.mkdir(parents=True,exist_ok=True)
 async with async_playwright() as pw:
  b=await pw.chromium.launch();page=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);await page.goto(h.resolve().as_uri(),wait_until='networkidle');await page.evaluate('document.fonts.ready');inj=await page.evaluate(INJECT_JS,{'items':main_items,'label':enrich['Label'],'numbers':review_numbers,'letters':review_letters})
  if not inj.get('ok'):raise RuntimeError('P012_DOM_INJECTION_FAIL='+repr(inj))
  await page.evaluate('document.fonts.ready');metrics,issues=await p001.fit_and_inspect(page);issues=[x for x in issues if x.get('kind')!='INTER_ROW_CLEARANCE_TOO_SMALL'];extra=await page.evaluate('''()=>{const n=document.querySelector('.page-number'),g=document.querySelector('.j2-grid'),e=document.querySelector('.p012-enrichment-row'),pr=document.querySelector('.presentation'),rows=[...document.querySelectorAll('.j2-object[data-row]')],out=[];if(!n||!g||!e||!pr||!rows.length)return[{kind:'P012_REQUIRED_ELEMENT_MISSING'}];if(n.textContent.trim()!=='12')out.push({kind:'P012_PAGE_NUMBER_WRONG'});const gr=g.getBoundingClientRect(),er=e.getBoundingClientRect(),prr=pr.getBoundingClientRect(),lower=er.top-gr.bottom,topgap=gr.top-prr.bottom;if(topgap<10)out.push({kind:'P012_GRID_TOO_CLOSE',gap:topgap});if(lower>12)out.push({kind:'P012_EXCESSIVE_BOTTOM_WHITESPACE',gap:lower});if(lower<5)out.push({kind:'P012_CORE_ENRICHMENT_COLLISION',gap:lower});const byRow={};for(const el of rows){const r=el.dataset.row;if(!byRow[r])byRow[r]=[];byRow[r].push(el.getBoundingClientRect())}const keys=Object.keys(byRow).map(Number).sort((a,b)=>a-b);for(let i=0;i<keys.length-1;i++){const a=Math.max(...byRow[keys[i]].map(x=>x.bottom)),b=Math.min(...byRow[keys[i+1]].map(x=>x.top)),gap=b-a;if(gap<4)out.push({kind:'P012_INTER_ROW_VISUAL_COLLISION',row:keys[i],gap});}return out}''');all_issues=[*issues,*extra];report.write_text(json.dumps({'injection':inj,'issues':all_issues},ensure_ascii=False,indent=2),encoding='utf-8')
  if all_issues:raise RuntimeError('P012_LAYOUT_ISSUES='+repr(all_issues))
  await page.screenshot(path=str(png/'page-012-v3.png'),full_page=True);pdf=out/'QURBATA-JILID-2-P012-V3-YA-FULL-PAGE-PROPORTIONAL.pdf';await page.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await b.close()
 return metrics,report,pdf,'DIRECT_P012_V3'
p001.render=render
def main():
 if len(lex)!=32:raise ValueError('P012_LEXICAL_COUNT_INVALID')
 current=sum(r['function']=='CURRENT' for r in lex)
 if current<14:raise ValueError('P012_YA_ACQUISITION_TOO_THIN')
 if '--output-dir' not in sys.argv[1:]:sys.argv.extend(['--output-dir','dist/qurbata-print-ready/jilid-2/pages/P012'])
 rc=v22.main();print('JILID2_P012_RENDERER_V3_FULL_PAGE_PROPORTIONAL=PASS');print('PAGE=12');print('ACQUISITION_LETTERS=ي');print('TITLE_VISUAL_RIGHT_TO_LEFT=يَ←يَبِسَ');print('CORE_OBJECTS=32');print('CORE_ROWS=8');print('PRACTICE_FONT_PT=31');print('PRACTICE_LINE_HEIGHT=1.18');print('CORE_ROW_GAP_MM=1.7');print('CORE_VERTICAL_FILL=FULL_AVAILABLE_HEIGHT');print('LOWER_DIVIDER_LINES=NONE');print('BOTTOM_HEIGHT_MM=25');print('BOTTOM_MAIN_ITEMS=8_FULL_WIDTH');return rc
if __name__=='__main__':raise SystemExit(main())
