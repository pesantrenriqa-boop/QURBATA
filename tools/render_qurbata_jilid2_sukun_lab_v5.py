#!/usr/bin/env python3
"""QURBATA Jilid 2 — SUKUN LAB V5.1.
Keep U+0652 native positioning, but obtain the visually approved open-sukun outline
robustly even when U+06E1 is not directly encoded in the selected KFGQPC cmap.
No book page is modified.
"""
from __future__ import annotations
import argparse,asyncio,copy,json,sys
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v19_kfgqpc as kfgloader

def _bounds(font,gname):
    try:
        from fontTools.pens.boundsPen import BoundsPen
        gs=font.getGlyphSet(); pen=BoundsPen(gs); gs[gname].draw(pen); return pen.bounds
    except Exception:return None

def patch_font(src:Path,dst:Path):
    try: from fontTools.ttLib import TTFont
    except ImportError as e: raise RuntimeError('FONTTOOLS_REQUIRED. Run: python -m pip install fonttools') from e
    font=TTFont(str(src)); cmap={}
    for table in font['cmap'].tables:
        if table.isUnicode(): cmap.update(table.cmap)
    g_round=cmap.get(0x0652)
    if not g_round: raise RuntimeError('NORMAL_SUKUN_U0652_NOT_FOUND')
    # Some KFGQPC builds render U+06E1 through GSUB/alternate glyphs and do not expose
    # a direct cmap entry. Prefer direct cmap; otherwise find a small mark glyph whose
    # outline differs from the round U+0652 and whose glyph name hints at 06E1/sukun.
    g_open=cmap.get(0x06E1); source='cmap_U+06E1'
    if not g_open:
        names=font.getGlyphOrder(); hinted=[n for n in names if any(k in n.lower() for k in ('06e1','sukun','jazm','head')) and n!=g_round]
        if hinted: g_open=hinted[0];source='glyph_name_hint'
    if not g_open:
        # Last-resort diagnostic selection: marks with zero advance and compact bounds.
        hmtx=font['hmtx'].metrics; rb=_bounds(font,g_round); candidates=[]
        for n in font.getGlyphOrder():
            if n==g_round or hmtx.get(n,(1,0))[0]!=0: continue
            b=_bounds(font,n)
            if not b: continue
            w=b[2]-b[0];hh=b[3]-b[1]
            if 20<=w<=500 and 20<=hh<=500: candidates.append((abs(w-hh),w*hh,n,b))
        candidates.sort()
        # Do not silently patch an arbitrary glyph. Emit candidates so next step is deterministic.
        raise RuntimeError('OPEN_SUKUN_NOT_DIRECTLY_MAPPED; round='+str(g_round)+' round_bounds='+repr(rb)+' candidate_marks='+repr(candidates[:24]))
    if 'glyf' not in font: raise RuntimeError('KFGQPC_FONT_NOT_TRUETYPE_GLYF')
    font['glyf'][g_round]=copy.deepcopy(font['glyf'][g_open]);dst.parent.mkdir(parents=True,exist_ok=True);font.save(str(dst))
    return {'round_glyph':g_round,'open_source_glyph':g_open,'open_source_resolution':source,'strategy':'outline_only_U0652_anchor_preserved'}

TEMPLATE='''<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><style>@page{{size:A5;margin:0}}*{{box-sizing:border-box}}body{{margin:0;background:#fff;color:#111;font-family:Arial,sans-serif}}.page{{width:148mm;height:210mm;padding:10mm;direction:ltr}}h1{{font:700 12pt Arial;text-align:center;margin:0 0 6mm}}.row{{border-bottom:1px solid #ddd;padding:5mm 0}}.label{{font:8pt Arial;direction:ltr;margin-bottom:2mm}}.arab{{direction:rtl;text-align:center;font-size:38pt;line-height:1.5;font-family:"QURBATA KFGQPC Uthman Taha Patched",serif!important;font-feature-settings:'mark' 1,'mkmk' 1;text-rendering:optimizeLegibility}}@font-face{{font-family:"QURBATA KFGQPC Uthman Taha Patched";src:url("{font_uri}") format("truetype");font-style:normal;font-weight:400;font-display:block}}</style></head><body><div class="page"><h1>SUKUN LAB V5.1 — OPEN SHAPE + U+0652 NATIVE ANCHORS</h1><div class="row"><div class="label">A · medial consonant</div><div class="arab">يَكْتُبُ &nbsp; يَفْتَحُ &nbsp; يَسْجُدُ</div></div><div class="row"><div class="label">B · final consonant</div><div class="arab">قُلْ &nbsp; مِنْ &nbsp; لَمْ &nbsp; هَلْ</div></div><div class="row"><div class="label">C · mixed positions</div><div class="arab">أَنْعَمْتَ &nbsp; يَعْلَمْ &nbsp; نَعْبُدُ</div></div><div class="row"><div class="label">D · isolated pairs</div><div class="arab">كْ &nbsp; فْ &nbsp; سْ &nbsp; لْ &nbsp; نْ &nbsp; مْ &nbsp; عْ &nbsp; بْ</div></div></div></body></html>'''
async def run(out,font_path,font_source):
    patched=out/'_runtime_font'/'KFGQPC-Uthman-Taha-QURBATA-OPEN-SUKUN.ttf';meta=patch_font(font_path,patched);h=out/'sukun-lab-v5.html';h.write_text(TEMPLATE.format(font_uri=patched.resolve().as_uri()),encoding='utf-8')
    async with async_playwright() as pw:
        b=await pw.chromium.launch();p=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);await p.goto(h.resolve().as_uri(),wait_until='networkidle');await p.evaluate('document.fonts.ready');loaded=await p.evaluate("()=>document.fonts.check('38pt \\\"QURBATA KFGQPC Uthman Taha Patched\\\"','يَكْتُبُ')")
        if not loaded:raise RuntimeError('PATCHED_KFGQPC_BINDING_FAIL')
        await p.screenshot(path=str(out/'SUKUN-LAB-V5.png'),full_page=True);await p.pdf(path=str(out/'SUKUN-LAB-V5.pdf'),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await b.close()
    (out/'SUKUN-LAB-V5.json').write_text(json.dumps({'source_font':font_path.name,'font_source':font_source,'patch':meta,'render_codepoint':'U+0652','gpos_preserved':True},ensure_ascii=False,indent=2),encoding='utf-8');print('SUKUN_LAB_V5_1=PASS');print('BASE_FONT=ACTUAL_KFGQPC_UTHMAN_TAHA');print('RENDER_CODEPOINT=U+0652');print('OPEN_SOURCE='+meta['open_source_glyph']);print('GPOS_ANCHORS=U+0652_ORIGINAL_PRESERVED')
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output-dir',default='dist/jilid-2-sukun-lab-v5');ap.add_argument('--font-file');ap.add_argument('--font-zip');a=ap.parse_args();out=Path(a.output_dir);out=out if out.is_absolute() else ROOT/out;out.mkdir(parents=True,exist_ok=True);fp,src=kfgloader.discover_font(a.font_file,a.font_zip,out);asyncio.run(run(out,fp,src))
if __name__=='__main__':main()
