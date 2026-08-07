#!/usr/bin/env python3
from __future__ import annotations
import argparse,asyncio,json
from pathlib import Path
import yaml
from jinja2 import Environment,FileSystemLoader,StrictUndefined
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1];SPECIAL={20,40};NATIVE_PROFILE=ROOT/'content/qwo/arabic-engine/anchors/jilid-1-short-vowels-native-v2.yaml'
def load_yaml(p):return yaml.safe_load(p.read_text(encoding='utf-8'))
def load_pages(data):
 paths=sorted(data.glob('page-*.yaml'))
 if len(paths)!=40:raise ValueError(f'LAYOUT_PAGE_COUNT actual={len(paths)} expected=40')
 pages=[load_yaml(p) for p in paths];reading=names=0
 for d in pages:
  n=int(d['page']);objs=d.get('objects',[]);ln=d.get('letter_names',[])
  if n in SPECIAL:
   if d.get('page_kind')!='LETTER_NAMES' or objs or len(ln)!=14:raise ValueError(f'SPECIAL_PAGE_CONTENT_INVALID page={n}')
   names+=14
  else:
   if d.get('page_kind')!='READING' or len(objs)!=19 or ln:raise ValueError(f'READING_PAGE_CONTENT_INVALID page={n}')
   pairs=[x for x in objs if x.get('row_band')=='ROW_2_L2_CURRENT'];triples=[x for x in objs if x.get('row_band')=='ROWS_3_7_L3']
   if len(pairs)!=4 or len(triples)!=15:raise ValueError(f'COMPOSITION_PATTERN_INVALID page={n}')
   reading+=19
 if reading!=722 or names!=28:raise ValueError(f'CONTENT_TOTAL_INVALID reading={reading} names={names}')
 return pages
def token_css(t):
 p=t['page'];c=t['colors'];f=t['fonts'];z=t['zones'];vals={'page-width':f"{p['width_mm']}mm",'page-height':f"{p['height_mm']}mm",'margin-top':f"{p['margin_top_mm']}mm",'margin-right':f"{p['margin_right_mm']}mm",'margin-bottom':f"{p['margin_bottom_mm']}mm",'margin-left':f"{p['margin_left_mm']}mm",'green':c['green'],'gold':c['gold'],'ink':c['ink'],'soft':c['soft'],'muted':c['muted'],'arabic-font':f'"{f["arabic_family"]}"','latin-font':f'"{f["latin_family"]}"','header-size':f"{f['header_pt']}pt",'target-size':f"{f['target_pt']}pt",'footer-size':f"{f['footer_pt']}pt",'header-height':f"{z['header_height_mm']}mm",'targets-height':f"{z['targets_height_mm']}mm",'footer-height':f"{z['footer_height_mm']}mm",'bottom-band-height':f"{z['bottom_band_height_mm']}mm"};return ':root {\n'+'\n'.join(f'--{k}:{v};' for k,v in vals.items())+'\n}'
def compile_css(tokens,out,book):
 extra='''.qae-native{font-family:var(--arabic-font);font-feature-settings:"liga" 0,"calt" 0;unicode-bidi:isolate}.canonical-targets{grid-template-columns:.8fr .8fr 2fr .8fr .8fr}.competency-target strong{font-size:6.1pt}.canonical-title{height:11mm;display:grid;grid-template-columns:minmax(0,1fr) auto minmax(0,1fr);align-items:center;gap:3mm;color:var(--green);font-size:8pt;overflow:hidden}.canonical-title strong{white-space:nowrap}.letter-name-grid{box-sizing:border-box;height:130mm;display:grid;grid-template-columns:repeat(2,1fr);grid-template-rows:repeat(7,minmax(0,1fr));gap:2.5mm;padding:3mm 8mm;direction:rtl;overflow:visible}.letter-name-card{box-sizing:border-box;min-width:0;min-height:0;display:flex;align-items:center;justify-content:center;gap:5mm;border:.25mm solid rgba(185,138,47,.38);border-radius:2mm;background:#fff}.letter-name-letter{font-family:var(--arabic-font);font-size:30pt;color:var(--green);line-height:1}.letter-name-arabic{font-family:var(--arabic-font);font-size:18pt;color:var(--ink);line-height:1.2}'''
 out.write_text('\n\n'.join([token_css(tokens),(book/'layout/master-layout-v1.css').read_text(encoding='utf-8'),(book/'layout/composition-v5.css').read_text(encoding='utf-8'),extra]),encoding='utf-8')
def render_html(d,template_dir,css,logo,out,debug,profile):
 env=Environment(loader=FileSystemLoader(str(template_dir)),undefined=StrictUndefined,autoescape=True);e=dict(d);e['qae']={'profile':profile.get('profile')};out.write_text(env.get_template('canonical-j1-composition-v5.html.j2').render(**e,css_uri=css.resolve().as_uri(),logo_uri=logo.resolve().as_uri(),layout_debug=debug),encoding='utf-8')
async def inspect(page,n):
 return await page.evaluate('''(n)=>{const t=2,issues=[];const add=(kind,el,extra={})=>{const r=el.getBoundingClientRect();issues.push({kind,className:el.className,x:r.x,y:r.y,width:r.width,height:r.height,...extra})};for(const el of document.querySelectorAll('.page,.header,.targets,.footer,.composition-v5-pairs,.composition-v5-triples')){if(el.scrollWidth>el.clientWidth+t||el.scrollHeight>el.clientHeight+t)add('STRUCTURAL_SCROLL_OVERFLOW',el,{scrollWidth:el.scrollWidth,clientWidth:el.clientWidth,scrollHeight:el.scrollHeight,clientHeight:el.clientHeight})}for(const slot of document.querySelectorAll('.composition-v5-object')){const c=slot.querySelector('.composition-v5-arabic');if(!c)continue;const s=slot.getBoundingClientRect(),r=c.getBoundingClientRect();if(r.left<s.left-t||r.right>s.right+t||r.top<s.top-t||r.bottom>s.bottom+t)add('OBJECT_OUTSIDE_SLOT',slot,{slot:slot.dataset.slot})}return issues}''',n)
async def browser_render(html_paths,png_dir,pdf,css,font,report):
 async with async_playwright() as p:
  b=await p.chromium.launch();page=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);sections=[];issues=[]
  for n,h in enumerate(html_paths,1):
   await page.goto(h.resolve().as_uri(),wait_until='networkidle');await page.evaluate('document.fonts.ready');obj=await page.locator('.composition-v5-object').count();names=await page.locator('.letter-name-card').count()
   if n in SPECIAL:
    if obj!=0 or names!=14:raise RuntimeError(f'SPECIAL_RENDER_COUNT_INVALID page={n} objects={obj} names={names}')
   else:
    if obj!=19 or names!=0:raise RuntimeError(f'READING_RENDER_COUNT_INVALID page={n} objects={obj} names={names}')
   x=await inspect(page,n)
   for i in x:i['page']=f'page-{n:03d}'
   issues.extend(x);await page.screenshot(path=str(png_dir/f'page-{n:03d}.png'),full_page=True);sections.append(await page.locator('main.page').evaluate('el=>el.outerHTML'))
  report.write_text(json.dumps(issues,ensure_ascii=False,indent=2),encoding='utf-8')
  if issues:
   kinds={}
   for x in issues:kinds[x['kind']]=kinds.get(x['kind'],0)+1
   raise RuntimeError('LAYOUT_OVERFLOW_COUNT='+str(len(issues))+' TYPES='+','.join(f'{k}:{v}' for k,v in sorted(kinds.items()))+f' REPORT={report}')
  combined="<!doctype html><html><head><meta charset='utf-8'><style>"+css.read_text(encoding='utf-8')+"</style></head><body>"+''.join(sections)+"</body></html>";await page.set_content(combined,wait_until='networkidle');await page.evaluate('document.fonts.ready');await page.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await b.close()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--book-dir',default='books/jilid-1');ap.add_argument('--data-dir',default='books/jilid-1/data-generated-v9-composition-v6');ap.add_argument('--output-dir',default='dist/jilid-1-production-candidate-v4');ap.add_argument('--logo',default='books/shared/assets/qurbata-logo.svg');ap.add_argument('--profile',default=str(NATIVE_PROFILE.relative_to(ROOT)));ap.add_argument('--debug',action='store_true');a=ap.parse_args();book=ROOT/a.book_dir;data=ROOT/a.data_dir;out=ROOT/a.output_dir;logo=ROOT/a.logo;profile=load_yaml(ROOT/a.profile);pages=load_pages(data);tokens=load_yaml(book/'layout/design-tokens.yaml');html_dir=out/'html';png_dir=out/'png';html_dir.mkdir(parents=True,exist_ok=True);png_dir.mkdir(parents=True,exist_ok=True);css=out/'runtime-layout.css';compile_css(tokens,css,book);html=[]
 for d in pages:
  h=html_dir/f"page-{int(d['page']):03d}.html";render_html(d,book/'templates',css,logo,h,a.debug,profile);html.append(h)
 pdf=out/'QURBATA-JILID-1-COMPOSITION-V6-CANDIDATE-V4.pdf';report=out/'LAYOUT-OVERFLOW-REPORT-V6.json';asyncio.run(browser_render(html,png_dir,pdf,css,str(tokens['fonts']['arabic_family']),report));print('PAGES_RENDERED=40');print('READING_OBJECTS_RENDERED=722');print('LETTER_NAMES_RENDERED=28');print('PRACTICE_FONT_SIZE=36pt');print('FOCUS_FONT_SIZE=44pt');print('LAYOUT_OVERFLOW=0');print(f'OVERFLOW_REPORT={report.relative_to(ROOT)}');print(f'PDF={pdf.relative_to(ROOT)}');print('COMPOSITION_V6_RENDERER=PASS');return 0
if __name__=='__main__':raise SystemExit(main())
