#!/usr/bin/env python3
"""Render QURBATA Jilid 2 P001-P020 joined-form foundation.

Visual inheritance:
- A5 page + header/footer hierarchy from Jilid 1 V22/V25 baseline;
- same 36pt practice baseline and optical ink-bound fitting philosophy;
- Jilid 2 uses 24 joined L3 objects, arranged 3 columns x 8 rows;
- Arabic shaping remains native: each 3-letter object is one intact joined string.

This renderer is a production-layout candidate for P001-P020 only. Footer auxiliary
content is deliberately marked nonfinal until Jilid 2 Tahfidz/Arabic/NIDOM registries
are bound to the composer.
"""
from __future__ import annotations
import argparse,asyncio,csv,html,json
from pathlib import Path
from playwright.async_api import async_playwright

ROOT=Path(__file__).resolve().parents[1]
DEFAULT_DATA=ROOT/'content/qwo/composer/output/jilid-2-v1-joined-foundation'
DEFAULT_OUT=ROOT/'dist/jilid-2-foundation-candidate-v1'
FONT_FAMILY='Amiri'


def read_csv(path:Path):
    with path.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))

def esc(s):return html.escape(str(s or ''))

def page_html(page:int, rows:list[dict], meta:dict, debug:bool)->str:
    objs=''.join(
        f'<div class="j2-object" data-slot="{int(r["Slot"])}"><span class="j2-glyph">{esc(r["ArabicObject"])}</span></div>'
        for r in rows
    )
    debug_attr=' data-layout-debug="true"' if debug else ''
    return f'''<!doctype html><html{debug_attr}><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<main class="page">
  <header class="header">
    <div class="brand">QURBATA <span>• JILID 2</span></div>
    <div class="page-no">{page}</div>
  </header>
  <section class="title-row"><strong>{esc(meta['Focus'])}</strong></section>
  <section class="j2-grid">{objs}</section>
  <section class="targets">
    <div class="target-item"><span>KOMPETENSI</span><strong>{esc(meta['Focus'])}</strong></div>
    <div class="target-item"><span>HAFALAN</span><strong>Registry Jilid 2 belum diikat</strong></div>
    <div class="target-item"><span>BAHASA ARAB</span><strong>Registry Jilid 2 belum diikat</strong></div>
    <div class="target-item"><span>NIDOM</span><strong>Registry Jilid 2 belum diikat</strong></div>
  </section>
  <footer class="footer"><span>QURBATA • JILID 2</span><span>Guru: __________  Nilai: ____  Tanggal: ________</span></footer>
</main></body></html>'''

CSS=r'''
@page{size:A5;margin:0}*{box-sizing:border-box}html,body{margin:0;padding:0;background:#fff}body{font-family:Arial,sans-serif;color:#171717}.page{width:148mm;height:210mm;padding:5mm 8mm 2.5mm;display:flex;flex-direction:column;overflow:hidden;page-break-after:always}.header{height:14mm;flex:0 0 14mm;display:flex;align-items:center;justify-content:space-between;border-bottom:.22mm solid rgba(185,138,47,.55)}.brand{font-family:Georgia,'Times New Roman',serif;font-size:10pt;font-weight:700;letter-spacing:.055em;color:#064d37}.brand span{font-size:7.3pt;font-weight:600;letter-spacing:.08em}.page-no{width:8mm;height:8mm;border:.25mm solid rgba(185,138,47,.65);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:7.5pt;font-weight:700;color:#064d37}.title-row{height:11mm;flex:0 0 11mm;display:flex;align-items:center;justify-content:center;color:#064d37;font-size:8.2pt;letter-spacing:.01em;text-align:center}.j2-grid{height:153mm;flex:0 0 153mm;display:grid;grid-template-columns:repeat(3,36mm);grid-template-rows:repeat(8,minmax(0,1fr));justify-content:space-between;row-gap:1.5mm;padding:1mm 0 1.5mm;direction:rtl;overflow:visible}.j2-object{position:relative;width:36mm;height:100%;min-height:0;display:flex;align-items:center;justify-content:center;overflow:visible}.j2-glyph{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);transform-origin:center;white-space:nowrap;direction:rtl;unicode-bidi:isolate;font-family:'Amiri','Noto Naskh Arabic',serif;font-size:36pt;line-height:1;color:#000}.targets{height:14mm;flex:0 0 14mm;margin-top:auto;margin-bottom:1mm;padding:.8mm 1mm .6mm;display:grid;grid-template-columns:1.2fr 1fr 1fr 1.35fr;gap:1.4mm;background:linear-gradient(to bottom,rgba(247,248,245,.92),rgba(255,255,255,.98));border-top:.22mm solid rgba(185,138,47,.58);border-radius:1.8mm 1.8mm 0 0;overflow:hidden}.target-item{min-width:0;padding:.2mm .9mm 0}.target-item+.target-item{border-left:.18mm solid rgba(185,138,47,.45)}.target-item span{display:block;color:#064d37;font-size:5.8pt;font-weight:800;line-height:1.1}.target-item strong{display:block;margin-top:.45mm;font-size:5.05pt;line-height:1.18;font-weight:600;overflow:hidden}.footer{height:5.5mm;flex:0 0 5.5mm;margin-bottom:.8mm;padding:.5mm 2mm;display:flex;align-items:center;justify-content:space-between;background:rgba(247,248,245,.74);border-radius:1.4mm;color:#555;font-size:5.2pt}html[data-layout-debug="true"] .j2-object{outline:.15mm dashed rgba(0,0,0,.14)}
'''

async def fit_joined(page):
    return await page.evaluate('''()=>{const canvas=document.createElement('canvas'),ctx=canvas.getContext('2d');let count=0,fit=0,damma=0,kasra=0;const mm=v=>v*96/25.4,safe=mm(.7);for(const slot of document.querySelectorAll('.j2-object')){const g=slot.querySelector('.j2-glyph');if(!g)continue;const cs=getComputedStyle(g),text=g.textContent||'';ctx.font=`${cs.fontStyle} ${cs.fontVariant} ${cs.fontWeight} ${cs.fontSize} ${cs.fontFamily}`;ctx.direction='rtl';ctx.textAlign='left';const m=ctx.measureText(text),left=-m.actualBoundingBoxLeft,right=m.actualBoundingBoxRight,raw=Math.max(.01,right-left),w=slot.getBoundingClientRect().width,avail=Math.max(1,w-2*safe),scale=Math.min(1,avail/raw);let y=0;if(text.includes('ُ')){y=mm(.38);damma++;}else if(text.includes('ِ')){y=-mm(.20);kasra++;}g.style.transform=`translate(-50%,-50%) scaleX(${scale})`;g.style.top=`calc(50% + ${y}px)`;g.dataset.scale=String(scale);g.dataset.fit=scale<.999?'1':'0';if(scale<.999)fit++;count++;}return {count,fit,damma,kasra}}''')

async def inspect(page,n):
    return await page.evaluate('''(n)=>{const issues=[],t=2;const add=(kind,el,extra={})=>{const r=el.getBoundingClientRect();issues.push({kind,page:n,className:el.className,x:r.x,y:r.y,width:r.width,height:r.height,...extra})};for(const el of document.querySelectorAll('.page,.header,.j2-grid,.targets,.footer')){if(el.scrollWidth>el.clientWidth+t||el.scrollHeight>el.clientHeight+t)add('STRUCTURAL_SCROLL_OVERFLOW',el,{scrollWidth:el.scrollWidth,clientWidth:el.clientWidth,scrollHeight:el.scrollHeight,clientHeight:el.clientHeight})}for(const slot of document.querySelectorAll('.j2-object')){const s=slot.getBoundingClientRect(),g=slot.querySelector('.j2-glyph').getBoundingClientRect();if(g.left<s.left-t||g.right>s.right+t)add('JOINED_GLYPH_OUTSIDE_SLOT',slot,{slot:slot.dataset.slot,glyphLeft:g.left,glyphRight:g.right,slotLeft:s.left,slotRight:s.right,scale:slot.querySelector('.j2-glyph').dataset.scale})}const grid=document.querySelector('.j2-grid'),targets=document.querySelector('.targets');if(grid&&targets){const g=grid.getBoundingClientRect(),b=targets.getBoundingClientRect();if(g.bottom>b.top+t)add('GRID_FOOTER_OVERLAP',grid,{gridBottom:g.bottom,targetsTop:b.top})}return issues}''',n)

async def render(html_paths:list[Path],out:Path,debug:bool):
    png=out/'png';png.mkdir(parents=True,exist_ok=True);report=out/'LAYOUT-OVERFLOW-REPORT-J2-V1.json';issues=[];sections=[];tot={'count':0,'fit':0,'damma':0,'kasra':0}
    async with async_playwright() as p:
        browser=await p.chromium.launch();page=await browser.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2)
        for n,h in enumerate(html_paths,1):
            await page.goto(h.resolve().as_uri(),wait_until='networkidle');await page.evaluate('document.fonts.ready')
            if await page.locator('.j2-object').count()!=24:raise RuntimeError(f'J2_OBJECT_COUNT_INVALID page={n}')
            m=await fit_joined(page)
            for k in tot:tot[k]+=m[k]
            found=await inspect(page,n);issues.extend(found)
            await page.screenshot(path=str(png/f'page-{n:03d}.png'),full_page=True)
            sections.append(await page.locator('main.page').evaluate('el=>el.outerHTML'))
        report.write_text(json.dumps(issues,ensure_ascii=False,indent=2),encoding='utf-8')
        if issues:
            kinds={}
            for x in issues:kinds[x['kind']]=kinds.get(x['kind'],0)+1
            raise RuntimeError('J2_LAYOUT_ISSUES='+str(len(issues))+' TYPES='+','.join(f'{k}:{v}' for k,v in sorted(kinds.items()))+f' REPORT={report}')
        combined="<!doctype html><html><head><meta charset='utf-8'><style>"+CSS+"</style></head><body>"+''.join(sections)+"</body></html>"
        await page.set_content(combined,wait_until='networkidle');await page.evaluate('document.fonts.ready')
        pdf=out/'QURBATA-JILID-2-P001-P020-FOUNDATION-CANDIDATE-V1.pdf';await page.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await browser.close()
    return tot,report,pdf

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--data-dir',default=str(DEFAULT_DATA.relative_to(ROOT)));ap.add_argument('--output-dir',default=str(DEFAULT_OUT.relative_to(ROOT)));ap.add_argument('--debug',action='store_true');a=ap.parse_args();data=Path(a.data_dir);data=data if data.is_absolute() else ROOT/data;out=Path(a.output_dir);out=out if out.is_absolute() else ROOT/out;out.mkdir(parents=True,exist_ok=True)
    rows=read_csv(data/'JILID-2-READING-OBJECTS-V1.csv');meta_rows=read_csv(data/'JILID-2-PAGE-METADATA-V1.csv');meta={int(r['Page']):r for r in meta_rows}
    if len(rows)!=480 or len(meta)!=20:raise ValueError(f'J2_DATASET_INVALID rows={len(rows)} pages={len(meta)}')
    html_dir=out/'html';html_dir.mkdir(parents=True,exist_ok=True);paths=[]
    for p in range(1,21):
        pr=[r for r in rows if int(r['Page'])==p]
        if len(pr)!=24:raise ValueError(f'J2_PAGE_OBJECT_COUNT page={p} actual={len(pr)}')
        h=html_dir/f'page-{p:03d}.html';h.write_text(page_html(p,pr,meta[p],a.debug),encoding='utf-8');paths.append(h)
    totals,report,pdf=asyncio.run(render(paths,out,a.debug))
    print('JILID2_FOUNDATION_RENDERER_V1=PASS');print('PAGES_RENDERED=20');print('READING_OBJECTS_RENDERED=480');print('PAGE_GRID=3_COLUMNS_X_8_ROWS');print('JOIN_POLICY=ARABIC_NATIVE_JOINING');print('LAYOUT_BASELINE=JILID1_V22_FROZEN');print('PRACTICE_FONT_SIZE=36pt');print(f'OPTICAL_JOINED_OBJECTS_FITTED={totals["count"]}');print(f'COLLISION_FIT_OBJECTS={totals["fit"]}');print(f'DAMMAH_MICRO_OFFSET_OBJECTS={totals["damma"]}');print(f'KASRAH_MICRO_OFFSET_OBJECTS={totals["kasra"]}');print('FOOTER_AUXILIARY_CONTENT=PLACEHOLDER_NONFINAL');print('LAYOUT_OVERFLOW=0');print(f'OVERFLOW_REPORT={report.relative_to(ROOT)}');print(f'PDF={pdf.relative_to(ROOT)}');return 0
if __name__=='__main__':raise SystemExit(main())
