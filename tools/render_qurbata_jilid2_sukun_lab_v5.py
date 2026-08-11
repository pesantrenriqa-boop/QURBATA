#!/usr/bin/env python3
"""QURBATA Jilid 2 — SUKUN LAB V7.1.
Keeps KFGQPC Arabic letters and U+0652 positioning, replacing only the sukun outline
with Amiri U+06E1. Amiri is auto-fetched into dist when absent; no font is committed.
"""
from __future__ import annotations
import argparse,asyncio,json,sys,os,urllib.request
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path:sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v19_kfgqpc as kfgloader
AMIRI_URL='https://github.com/aliftype/amiri/raw/refs/heads/main/fonts/Amiri-Regular.ttf'

def discover_amiri(explicit:str|None,out:Path)->Path:
    c=[]
    if explicit:c.append(Path(explicit).expanduser())
    env=os.environ.get('QURBATA_AMIRI_FONT')
    if env:c.append(Path(env).expanduser())
    home=Path.home();c += [ROOT/'_local/fonts'/'Amiri-Regular.ttf',home/'Downloads'/'Amiri-Regular.ttf',Path(r'C:\Windows\Fonts\Amiri-Regular.ttf'),home/'AppData/Local/Microsoft/Windows/Fonts/Amiri-Regular.ttf']
    for p in c:
        if p.is_file():return p.resolve()
    dst=out/'_runtime_font'/'Amiri-Regular.ttf';dst.parent.mkdir(parents=True,exist_ok=True)
    try:
        req=urllib.request.Request(AMIRI_URL,headers={'User-Agent':'QURBATA-renderer/1.0'});dst.write_bytes(urllib.request.urlopen(req,timeout=30).read())
        if dst.stat().st_size<50000:raise RuntimeError('downloaded file too small')
        return dst.resolve()
    except Exception as e:
        raise FileNotFoundError('AMIRI_FONT_NOT_FOUND_AND_AUTO_DOWNLOAD_FAILED='+repr(e)+'; manually download Amiri-Regular.ttf and pass --amiri-font "C:\\path\\Amiri-Regular.ttf"') from e

def patch_font(kfg_path:Path,amiri_path:Path,dst:Path):
    from fontTools.ttLib import TTFont
    from fontTools.pens.ttGlyphPen import TTGlyphPen
    from fontTools.pens.transformPen import TransformPen
    k=TTFont(str(kfg_path));a=TTFont(str(amiri_path));kc={};ac={}
    for t in k['cmap'].tables:
        if t.isUnicode():kc.update(t.cmap)
    for t in a['cmap'].tables:
        if t.isUnicode():ac.update(t.cmap)
    target=kc.get(0x0652);source=ac.get(0x06E1)
    if not target:raise RuntimeError('KFGQPC_U0652_NOT_FOUND')
    if not source:raise RuntimeError('AMIRI_U06E1_NOT_FOUND')
    if 'glyf' not in k:raise RuntimeError('KFGQPC_NOT_TRUETYPE_GLYF')
    kgs=k.getGlyphSet();ags=a.getGlyphSet();upm_k=k['head'].unitsPerEm;upm_a=a['head'].unitsPerEm;scale=upm_k/upm_a
    pen=TTGlyphPen(kgs);tp=TransformPen(pen,(scale,0,0,scale,0,0));ags[source].draw(tp);k['glyf'][target]=pen.glyph();dst.parent.mkdir(parents=True,exist_ok=True);k.save(str(dst))
    return {'target':target,'source':source,'scale':scale,'strategy':'AMIRI_U06E1_OUTLINE_IN_KFG_U0652_SLOT'}
TEMPLATE='''<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><style>@page{{size:A5;margin:0}}*{{box-sizing:border-box}}body{{margin:0;background:#fff;color:#111;font-family:Arial}}.page{{width:148mm;height:210mm;padding:10mm;direction:ltr}}h1{{font:700 12pt Arial;text-align:center;margin-bottom:5mm}}.row{{border-bottom:1px solid #ddd;padding:4mm 0}}.label{{font:8pt Arial;direction:ltr;margin-bottom:1mm}}.arab{{direction:rtl;text-align:center;font-size:38pt;line-height:1.45;font-family:"QURBATA KFGQPC Hybrid",serif!important;font-feature-settings:'mark' 1,'mkmk' 1;text-rendering:optimizeLegibility}}@font-face{{font-family:"QURBATA KFGQPC Hybrid";src:url("{font_uri}") format("truetype");font-display:block}}</style></head><body><div class="page"><h1>SUKUN LAB V7.1 — KFGQPC + OPEN SUKUN</h1><div class="row"><div class="label">medial</div><div class="arab">يَكْتُبُ &nbsp; يَفْتَحُ &nbsp; يَسْجُدُ</div></div><div class="row"><div class="label">final</div><div class="arab">قُلْ &nbsp; مِنْ &nbsp; لَمْ &nbsp; هَلْ</div></div><div class="row"><div class="label">mixed</div><div class="arab">أَنْعَمْتَ &nbsp; يَعْلَمْ &nbsp; نَعْبُدُ</div></div><div class="row"><div class="label">isolated</div><div class="arab">كْ &nbsp; فْ &nbsp; سْ &nbsp; لْ &nbsp; نْ &nbsp; مْ &nbsp; عْ &nbsp; بْ</div></div></div></body></html>'''
async def run(out,kfg,amiri,kfgsrc):
    patched=out/'_runtime_font'/'KFGQPC-QURBATA-HYBRID-OPEN-SUKUN.ttf';meta=patch_font(kfg,amiri,patched);h=out/'sukun-lab-v7.html';h.write_text(TEMPLATE.format(font_uri=patched.resolve().as_uri()),encoding='utf-8')
    async with async_playwright() as pw:
        b=await pw.chromium.launch();p=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);await p.goto(h.resolve().as_uri(),wait_until='networkidle');await p.evaluate('document.fonts.ready');ok=await p.evaluate("()=>document.fonts.check('38pt \\\"QURBATA KFGQPC Hybrid\\\"','يَكْتُبُ')")
        if not ok:raise RuntimeError('HYBRID_FONT_BINDING_FAIL')
        await p.screenshot(path=str(out/'SUKUN-LAB-V7.png'),full_page=True);await p.pdf(path=str(out/'SUKUN-LAB-V7.pdf'),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await b.close()
    (out/'SUKUN-LAB-V7.json').write_text(json.dumps({'kfg_source':kfgsrc,'kfg_font':kfg.name,'amiri_font':amiri.name,'patch':meta,'book_pages_modified':False},ensure_ascii=False,indent=2),encoding='utf-8');print('SUKUN_LAB_V7_1=PASS');print('BASE_LETTERS=KFGQPC_UTHMAN_TAHA');print('RENDER_CODEPOINT=U+0652');print('VISUAL_OUTLINE=AMIRI_U+06E1');print('POSITIONING=KFGQPC_U+0652_GPOS_PRESERVED')
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output-dir',default='dist/jilid-2-sukun-lab-v7');ap.add_argument('--font-file');ap.add_argument('--font-zip');ap.add_argument('--amiri-font');a=ap.parse_args();out=Path(a.output_dir);out=out if out.is_absolute() else ROOT/out;out.mkdir(parents=True,exist_ok=True);kfg,src=kfgloader.discover_font(a.font_file,a.font_zip,out);amiri=discover_amiri(a.amiri_font,out);asyncio.run(run(out,kfg,amiri,src))
if __name__=='__main__':main()
