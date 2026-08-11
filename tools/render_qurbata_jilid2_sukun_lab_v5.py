#!/usr/bin/env python3
"""QURBATA Jilid 2 — SUKUN LAB V5.
Runtime font patch experiment:
- keep U+0652's native KFGQPC GPOS/anchor behaviour (which positions correctly),
- replace ONLY its glyph outline with the open-head shape from U+06E1,
- preserve all Arabic base glyphs and all original positioning tables.
This avoids U+06E1 triggering the mark-collision behaviour seen in V3/V4.
No font binary is committed; patched TTF exists only under dist/ at runtime.
"""
from __future__ import annotations
import argparse,asyncio,copy,json,sys
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v19_kfgqpc as kfgloader

def patch_font(src:Path,dst:Path):
    try:
        from fontTools.ttLib import TTFont
    except ImportError as e:
        raise RuntimeError('FONTTOOLS_REQUIRED. Run: python -m pip install fonttools') from e
    font=TTFont(str(src))
    cmap={}
    for table in font['cmap'].tables:
        if table.isUnicode(): cmap.update(table.cmap)
    g_round=cmap.get(0x0652); g_open=cmap.get(0x06E1)
    if not g_round or not g_open: raise RuntimeError(f'SUKUN_GLYPHS_NOT_FOUND round={g_round} open={g_open}')
    if 'glyf' not in font: raise RuntimeError('KFGQPC_FONT_NOT_TRUETYPE_GLYF')
    # Copy only the open-sukun outline into the normal sukun glyph slot.
    # Do NOT touch cmap, GPOS, GDEF, GSUB, anchors, or Arabic base glyphs.
    font['glyf'][g_round]=copy.deepcopy(font['glyf'][g_open])
    # Keep U+0652's original zero-advance metrics so its existing mark positioning survives.
    dst.parent.mkdir(parents=True,exist_ok=True); font.save(str(dst))
    return {'round_glyph':g_round,'open_source_glyph':g_open,'strategy':'outline_only'}

TEMPLATE='''<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><style>
@page{{size:A5;margin:0}}*{{box-sizing:border-box}}body{{margin:0;background:#fff;color:#111;font-family:Arial,sans-serif}}.page{{width:148mm;height:210mm;padding:10mm;direction:ltr}}h1{{font:700 12pt Arial;text-align:center;margin:0 0 6mm}}.row{{border-bottom:1px solid #ddd;padding:5mm 0}}.label{{font:8pt Arial;direction:ltr;margin-bottom:2mm}}.arab{{direction:rtl;text-align:center;font-size:38pt;line-height:1.5;font-family:"QURBATA KFGQPC Uthman Taha Patched",serif!important;font-feature-settings:'mark' 1,'mkmk' 1;text-rendering:optimizeLegibility}}
@font-face{{font-family:"QURBATA KFGQPC Uthman Taha Patched";src:url("{font_uri}") format("truetype");font-style:normal;font-weight:400;font-display:block}}</style></head><body><div class="page"><h1>SUKUN LAB V5 — OPEN SHAPE + U+0652 NATIVE ANCHORS</h1>
<div class="row"><div class="label">A · medial consonant</div><div class="arab">يَكْتُبُ &nbsp; يَفْتَحُ &nbsp; يَسْجُدُ</div></div>
<div class="row"><div class="label">B · final consonant</div><div class="arab">قُلْ &nbsp; مِنْ &nbsp; لَمْ &nbsp; هَلْ</div></div>
<div class="row"><div class="label">C · mixed positions</div><div class="arab">أَنْعَمْتَ &nbsp; يَعْلَمْ &nbsp; نَعْبُدُ</div></div>
<div class="row"><div class="label">D · isolated pairs</div><div class="arab">كْ &nbsp; فْ &nbsp; سْ &nbsp; لْ &nbsp; نْ &nbsp; مْ &nbsp; عْ &nbsp; بْ</div></div>
<div class="label" style="margin-top:6mm">Expected: Uthman Taha letters stay clean; sukun looks open; no harakat collision.</div></div></body></html>'''

async def run(out:Path,font_path:Path,font_source:str):
    patched=out/'_runtime_font'/'KFGQPC-Uthman-Taha-QURBATA-OPEN-SUKUN.ttf'; meta=patch_font(font_path,patched)
    h=out/'sukun-lab-v5.html'; h.write_text(TEMPLATE.format(font_uri=patched.resolve().as_uri()),encoding='utf-8')
    async with async_playwright() as pw:
        b=await pw.chromium.launch(); p=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2)
        await p.goto(h.resolve().as_uri(),wait_until='networkidle'); await p.evaluate('document.fonts.ready')
        loaded=await p.evaluate("()=>document.fonts.check('38pt \\\"QURBATA KFGQPC Uthman Taha Patched\\\"','يَكْتُبُ')")
        if not loaded: raise RuntimeError('PATCHED_KFGQPC_BINDING_FAIL')
        await p.screenshot(path=str(out/'SUKUN-LAB-V5.png'),full_page=True)
        await p.pdf(path=str(out/'SUKUN-LAB-V5.pdf'),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'})
        await b.close()
    (out/'SUKUN-LAB-V5.json').write_text(json.dumps({'source_font':font_path.name,'font_source':font_source,'patch':meta,'render_codepoint':'U+0652','visual_shape_source':'U+06E1','gpos_preserved':True,'book_pages_modified':False},ensure_ascii=False,indent=2),encoding='utf-8')
    print('SUKUN_LAB_V5=PASS');print('BASE_FONT=ACTUAL_KFGQPC_UTHMAN_TAHA');print('RENDER_CODEPOINT=U+0652');print('VISUAL_OUTLINE_SOURCE=U+06E1');print('GPOS_ANCHORS=U+0652_ORIGINAL_PRESERVED');print('ARABIC_BASE_GLYPHS=UNCHANGED');print('BOOK_PAGES_MODIFIED=NO')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output-dir',default='dist/jilid-2-sukun-lab-v5');ap.add_argument('--font-file');ap.add_argument('--font-zip');a=ap.parse_args();out=Path(a.output_dir);out=out if out.is_absolute() else ROOT/out;out.mkdir(parents=True,exist_ok=True);fp,src=kfgloader.discover_font(a.font_file,a.font_zip,out);asyncio.run(run(out,fp,src))
if __name__=='__main__':main()
