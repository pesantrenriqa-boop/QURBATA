#!/usr/bin/env python3
"""P001 visual reopen candidate: larger Arabic practice type, content unchanged."""
from pathlib import Path
import importlib.util, argparse, asyncio
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'tools/render_qurbata_jilid1_p001_print_anchor_v1.py'
spec=importlib.util.spec_from_file_location('p001base',BASE);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
OUT=ROOT/'dist/qurbata-print-ready/jilid-1/pages/P001-LARGE-TYPE-REVIEW'

def build(font_uri,objects):
    s=m.build(font_uri,objects)
    # Keep large type. V4 removes the transform that caused overlap with presentation,
    # and instead shortens the grid so it fits naturally between presentation and footer.
    s=s.replace('font-size:46pt;line-height:1.05','font-size:52pt;line-height:1.0')
    s=s.replace('height:158mm;flex:0 0 158mm','height:140mm;flex:0 0 140mm')
    s=s.replace('row-gap:3.2mm;padding:.8mm 0 1mm','row-gap:0.9mm;padding:1.5mm 0 0')
    s=s.replace('font-size:40pt;line-height:1.02','font-size:48pt;line-height:1.0')
    s=s.replace('.l2{width:23mm}', '.l2{width:25mm}')
    s=s.replace('.l3{width:35mm}', '.l3{width:38mm}')
    s=s.replace('.row-l2{gap:10mm}', '.row-l2{gap:6mm}')
    s=s.replace('.row-l3{gap:11mm}', '.row-l3{gap:5mm}')
    return s

def free(base):
    if not base.exists():return base
    try:open(base,'ab').close();return base
    except PermissionError:pass
    for n in range(1,100):
        p=base.with_name(base.stem+f'-R{n}'+base.suffix)
        if not p.exists():return p
    raise RuntimeError('NO_FREE_OUTPUT')

async def render(h):
    pdf=free(OUT/'QURBATA-JILID-1-P001-LARGE-TYPE-CANDIDATE-V4.pdf');png=free(OUT/'QURBATA-JILID-1-P001-LARGE-TYPE-CANDIDATE-V4.png')
    async with async_playwright() as pw:
        b=await pw.chromium.launch();p=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);await p.goto(h.resolve().as_uri(),wait_until='networkidle');await p.evaluate('document.fonts.ready')
        if not await p.evaluate(f"()=>document.fonts.check('48pt \\\"{m.FONT_FAMILY}\\\"','بَ تَ ثَ')"):raise RuntimeError('P001_LARGE_FONT_BINDING_FAIL')
        geom=await p.evaluate("""()=>{const page=document.querySelector('.page').getBoundingClientRect(),footer=document.querySelector('.footer').getBoundingClientRect(),pres=document.querySelector('.presentation').getBoundingClientRect(),ps=[...document.querySelectorAll('.practice')].map(e=>e.getBoundingClientRect());const maxBottom=Math.max(...ps.map(x=>x.bottom)),minTop=Math.min(...ps.map(x=>x.top)),maxRight=Math.max(...ps.map(x=>x.right)),minLeft=Math.min(...ps.map(x=>x.left));return {ok:maxBottom<=footer.top-12&&minTop>=pres.bottom+4&&maxRight<=page.right-8&&minLeft>=page.left+8,clearance:footer.top-maxBottom,topClearance:minTop-pres.bottom,maxBottom,footerTop:footer.top,minTop,presBottom:pres.bottom,minLeft,maxRight,pageLeft:page.left,pageRight:page.right}}""")
        if not geom['ok']:raise RuntimeError(f'P001_LARGE_SAFEAREA_FAIL {geom}')
        await p.screenshot(path=str(png),full_page=True);await p.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await b.close()
    return pdf,geom

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--font-file');ap.add_argument('--font-zip');a=ap.parse_args();OUT.mkdir(parents=True,exist_ok=True);font,src=m.kfgloader.discover_font(a.font_file,a.font_zip,OUT);objs,mode,removed=m.load_objects();h=OUT/'QURBATA-JILID-1-P001-LARGE-TYPE-CANDIDATE-V4.html';h.write_text(build(font.resolve().as_uri(),objs),encoding='utf-8');pdf,g=asyncio.run(render(h));print('QJ1_P001_LARGE_TYPE_CANDIDATE_V4=PASS');print('CONTENT_CHANGED=NO');print('PRESENTATION_FONT_PT=52');print('PRACTICE_FONT_PT=48');print('GRID_HEIGHT_MM=140');print('GRID_SHIFT_UP_MM=0');print('ROW_GAP_MM=0.9');print('SAFEAREA=PASS');print('SAFE_CLEARANCE_PX='+str(round(g['clearance'],2)));print('TOP_CLEARANCE_PX='+str(round(g['topClearance'],2)));print('PDF='+str(pdf.relative_to(ROOT)));return 0
if __name__=='__main__':raise SystemExit(main())
