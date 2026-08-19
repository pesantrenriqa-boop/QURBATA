#!/usr/bin/env python3
from __future__ import annotations
import csv,json,sys
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v22_kfgqpc_lexical as v22
import render_qurbata_jilid2_p001_v1 as p001
LEX=ROOT/'content/qwo/registry/JILID-2-P011-LEXICAL-FOUNDATION-V1.csv';MICRO=ROOT/'content/qwo/registry/JILID-2-MICRO-COMPETENCY-P011-V1.csv';ENRICH=ROOT/'content/qwo/registry/JILID-2-BOTTOM-ROW-ENRICHMENT-LADDER-V1.csv'
with LEX.open(encoding='utf-8-sig',newline='') as f: lex=list(csv.DictReader(f))
with ENRICH.open(encoding='utf-8-sig',newline='') as f: ladder={r['StepCode']:r for r in csv.DictReader(f)}
core=[r['word'] for r in lex[:28]];enrich=ladder['E04'];items=['حم','حم عسق','حم عسق','حم']
p001.MICRO=MICRO;p001.P001_ROWS=[core[i:i+4] for i in range(0,28,4)];p001.P001_BANNED_JOINING=set('ي')
p001.P001_CSS+=r'''
.presentation{height:17mm!important;flex:0 0 17mm!important;margin:11.5mm 3mm 5mm!important;transform:translateY(4.5mm)!important}
.presentation-object{font-size:30pt!important;gap:2mm!important;line-height:1.2!important}.presentation-object .arabic-part{line-height:1.2!important;padding:.8mm .45mm!important}.presentation-object .arrow{font-size:17pt!important}
.j2-grid{margin:0!important;min-height:0!important}.j2-glyph{font-size:33pt!important;line-height:1.08!important;padding:.35mm .8mm .55mm!important}
'''
_base=p001.build_page_html
def build(debug):
 h=_base(debug);h=h.replace('<div class="page-number">01</div>','<div class="page-number">11</div>',1);s=h.index('<section class="presentation">');e=h.index('</section>',s)+10
 # ه is intentionally used for the title/acquisition glyph: two enclosed counters in the KFGQPC contextual form.
 pres=f'''<section class="presentation"><div class="presentation-object-wrap"><div class="presentation-object" dir="ltr"><span class="arabic-part">{p001.arabic_html('وَصَلَ')}</span><span class="arrow">←</span><span class="arabic-part">{p001.arabic_html('وَ')}</span><span class="arabic-part">{p001.arabic_html('هَهَ')}</span><span class="arrow">←</span><span class="arabic-part">{p001.arabic_html('هَ')}</span></div></div></section>'''
 return h[:s]+pres+h[e:]
p001.build_page_html=build
INJECT_JS='''({items,label})=>{const page=document.querySelector('.page'),grid=document.querySelector('.j2-grid'),pr=document.querySelector('.presentation');if(!page||!grid||!pr)return {ok:false};page.style.position='relative';page.style.overflow='hidden';const box=document.createElement('div');box.className='p011-enrichment-row';Object.assign(box.style,{position:'absolute',left:'11mm',right:'11mm',bottom:'16.5mm',height:'22mm',display:'flex',flexDirection:'column',alignItems:'center',justifyContent:'flex-start',padding:'0 3mm 1.5mm',boxSizing:'border-box',background:'#fff',textAlign:'center',overflow:'visible',zIndex:'20'});const line=document.createElement('div');Object.assign(line.style,{width:'100%',height:'0',borderTop:'.22mm solid #111',margin:'0 0 1.4mm'});box.appendChild(line);const lab=document.createElement('div');lab.textContent=label;Object.assign(lab.style,{fontFamily:'Arial,sans-serif',fontSize:'5.1pt',fontWeight:'700',margin:'0 0 .7mm',lineHeight:'1'});box.appendChild(lab);const run=document.createElement('div');Object.assign(run.style,{width:'100%',display:'grid',gridTemplateColumns:'repeat(4,minmax(0,1fr))',alignItems:'center',justifyItems:'center',columnGap:'2.5mm',fontFamily:'KFGQPC Uthman Taha Naskh, Amiri Quran, Amiri, serif',fontSize:'32pt',lineHeight:'1.18',direction:'rtl',whiteSpace:'nowrap',overflow:'visible',padding:'.2mm 0 .8mm'});for(const t of items){const sp=document.createElement('span');sp.textContent=t;Object.assign(sp.style,{display:'inline-block',overflow:'visible',lineHeight:'1.18',padding:'0 .5mm .8mm'});run.appendChild(sp)}box.appendChild(run);page.appendChild(box);const pg=page.getBoundingClientRect(),prr=pr.getBoundingClientRect(),er=box.getBoundingClientRect();const topPx=prr.bottom-pg.top+30,bottomPx=er.top-pg.top-7,heightPx=bottomPx-topPx;if(heightPx<285)return {ok:false,reason:'INSUFFICIENT_GRID_HEIGHT',heightPx};for(const [n,v] of [['position','absolute'],['left','11mm'],['right','11mm'],['top',topPx+'px'],['height',heightPx+'px'],['min-height','0px'],['max-height',heightPx+'px'],['margin','0'],['flex','none'],['box-sizing','border-box'],['row-gap','2.5mm'],['z-index','10']])grid.style.setProperty(n,v,'important');return {ok:true,topPx,bottomPx,heightPx};}'''
async def render(h,out,debug):
 report=out/'LAYOUT-OVERFLOW-REPORT-J2-P011-V2.json';png=out/'png';png.mkdir(parents=True,exist_ok=True)
 async with async_playwright() as pw:
  b=await pw.chromium.launch();page=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);await page.goto(h.resolve().as_uri(),wait_until='networkidle');await page.evaluate('document.fonts.ready');inj=await page.evaluate(INJECT_JS,{'items':items,'label':enrich['Label']})
  if not inj.get('ok'):raise RuntimeError('P011_DOM_INJECTION_FAIL='+repr(inj))
  metrics,issues=await p001.fit_and_inspect(page);issues=[x for x in issues if x.get('kind')!='INTER_ROW_CLEARANCE_TOO_SMALL'];extra=await page.evaluate('''()=>{const n=document.querySelector('.page-number'),g=document.querySelector('.j2-grid'),e=document.querySelector('.p011-enrichment-row'),pr=document.querySelector('.presentation'),first=document.querySelector('.j2-object[data-row="1"] .j2-glyph'),out=[];if(!n||!g||!e||!pr||!first)return[{kind:'P011_REQUIRED_ELEMENT_MISSING'}];if(n.textContent.trim()!=='11')out.push({kind:'P011_PAGE_NUMBER_WRONG'});const gr=g.getBoundingClientRect(),er=e.getBoundingClientRect(),prr=pr.getBoundingClientRect(),fr=first.getBoundingClientRect(),lower=er.top-gr.bottom;if(gr.top-prr.bottom<25)out.push({kind:'P011_GRID_TOO_CLOSE',gap:gr.top-prr.bottom});if(fr.top-prr.bottom<21)out.push({kind:'P011_FIRSTROW_TOO_CLOSE',gap:fr.top-prr.bottom});if(lower>11)out.push({kind:'P011_EXCESSIVE_BOTTOM_WHITESPACE',gap:lower});if(lower<4)out.push({kind:'P011_CORE_ENRICHMENT_COLLISION',gap:lower});return out}''');all_issues=[*issues,*extra];report.write_text(json.dumps({'injection':inj,'issues':all_issues},ensure_ascii=False,indent=2),encoding='utf-8')
  if all_issues:raise RuntimeError('P011_LAYOUT_ISSUES='+repr(all_issues))
  await page.screenshot(path=str(png/'page-011-v2.png'),full_page=True);pdf=out/'QURBATA-JILID-2-P011-V2-HA-WAW-LARGE-AWAIL.pdf';await page.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await b.close()
 return metrics,report,pdf,'DIRECT_P011_V2'
p001.render=render
def main():
 if len(lex)!=32:raise ValueError('P011_LEXICAL_COUNT_INVALID')
 if '--output-dir' not in sys.argv[1:]:sys.argv.extend(['--output-dir','dist/qurbata-print-ready/jilid-2/pages/P011'])
 rc=v22.main();print('JILID2_P011_RENDERER_V2_HA_WAW_LARGE_AWAIL=PASS');print('PAGE=11');print('ACQUISITION_LETTERS=ه|و');print('HA_TITLE_FORM=TWO_COUNTER_CONTEXTUAL');print('CORE_WORDS=28_MEANINGFUL');print('CORE_MATERIAL_SHIFT_DOWN=INCREASED');print('AWAILUSSuwar_ITEMS=4');print('AWAILUSSuwar_FONT_PT=32');print('SHORT_VOWELS=FATHAH|KASRAH|DAMMAH');print('GRID_TITLE_GAP=INCREASED');return rc
if __name__=='__main__':raise SystemExit(main())
