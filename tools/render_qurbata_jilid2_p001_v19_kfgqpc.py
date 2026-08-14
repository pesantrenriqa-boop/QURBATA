#!/usr/bin/env python3
"""QURBATA Jilid 2 P001 — Jilid-1-compatible production renderer.

Keeps the frozen V7.6 sukun system while replacing the legacy Jilid 2 page
presentation with the current Jilid 1 visual language: large Arabic practice
text, clean lower area, no competency-description boxes, no teacher/date/score
form, while preserving the small Arabic Uthman Taha slogan footer.
"""
from __future__ import annotations
import argparse
import os
import sys
import urllib.request
import zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))

import render_qurbata_jilid2_p001_v18 as v18
import render_qurbata_jilid2_p001_v1 as p001

FONT_FAMILY='QURBATA KFGQPC Uthman Taha Naskh Frozen Sukun'
TTF_BASENAME='KFGQPC Uthman Taha Naskh Regular.ttf'
ZIP_BASENAME='kfgqpc-uthman-taha-naskh-regular.zip'
AMIRI_URL='https://github.com/aliftype/amiri/raw/refs/heads/main/fonts/Amiri-Regular.ttf'
SUKUN_BASELINE_VERSION='V7.6'
SUKUN_Y_SHIFT=-1700
DEFAULT_OUTPUT='dist/qurbata-print-ready/jilid-2/pages/P001'


def discover_font(explicit_font:str|None, explicit_zip:str|None, out_dir:Path)->tuple[Path,str]:
    candidates=[]
    if explicit_font:candidates.append(Path(explicit_font).expanduser())
    env=os.environ.get('QURBATA_KFGQPC_FONT')
    if env:candidates.append(Path(env).expanduser())
    home=Path.home()
    candidates += [ROOT/'_local/fonts'/TTF_BASENAME,home/'Downloads'/TTF_BASENAME,home/'Downloads'/'KFGQPC Uthman Taha Naskh Regular'/TTF_BASENAME]
    for p in candidates:
        if p.is_file():return p.resolve(),'TTF'
    zips=[]
    if explicit_zip:zips.append(Path(explicit_zip).expanduser())
    zips += [home/'Downloads'/ZIP_BASENAME,ROOT/'_local/fonts'/ZIP_BASENAME]
    for zp in zips:
        if not zp.is_file():continue
        target=out_dir/'_runtime_font'/TTF_BASENAME;target.parent.mkdir(parents=True,exist_ok=True)
        with zipfile.ZipFile(zp) as z:
            match=next((n for n in z.namelist() if n.lower().endswith(TTF_BASENAME.lower())),None)
            if not match:raise RuntimeError(f'KFGQPC_TTF_NOT_FOUND_IN_ZIP={zp}')
            target.write_bytes(z.read(match))
        return target.resolve(),'ZIP_EXTRACTED_RUNTIME'
    raise FileNotFoundError('KFGQPC_FONT_NOT_FOUND. Use --font-file or --font-zip.')


def discover_amiri(explicit:str|None,out_dir:Path)->tuple[Path,str]:
    c=[]
    if explicit:c.append(Path(explicit).expanduser())
    env=os.environ.get('QURBATA_AMIRI_FONT')
    if env:c.append(Path(env).expanduser())
    home=Path.home();c += [ROOT/'_local/fonts'/'Amiri-Regular.ttf',home/'Downloads'/'Amiri-Regular.ttf',Path(r'C:\Windows\Fonts\Amiri-Regular.ttf'),home/'AppData/Local/Microsoft/Windows/Fonts/Amiri-Regular.ttf']
    for p in c:
        if p.is_file():return p.resolve(),'LOCAL'
    dst=out_dir/'_runtime_font'/'Amiri-Regular.ttf';dst.parent.mkdir(parents=True,exist_ok=True)
    req=urllib.request.Request(AMIRI_URL,headers={'User-Agent':'QURBATA-renderer/1.0'})
    dst.write_bytes(urllib.request.urlopen(req,timeout=30).read())
    if dst.stat().st_size<50000:raise RuntimeError('AMIRI_AUTO_DOWNLOAD_INVALID')
    return dst.resolve(),'AUTO_DOWNLOADED_RUNTIME'


def build_frozen_sukun_font(kfg_path:Path,amiri_path:Path,out_dir:Path)->Path:
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
    kgs=k.getGlyphSet();ags=a.getGlyphSet();scale=k['head'].unitsPerEm/a['head'].unitsPerEm
    pen=TTGlyphPen(kgs);tp=TransformPen(pen,(scale,0,0,scale,0,SUKUN_Y_SHIFT));ags[source].draw(tp)
    k['glyf'][target]=pen.glyph()
    dst=out_dir/'_runtime_font'/'KFGQPC-QURBATA-FROZEN-SUKUN-V7-6.ttf';dst.parent.mkdir(parents=True,exist_ok=True);k.save(str(dst))
    return dst.resolve()


async def jilid1_style_fit_and_inspect(page):
    metrics=await p001.base.base.fit_joined(page)
    issues=await page.evaluate('''()=>{const out=[];const rows={};const grid=document.querySelector('.j2-grid');const footer=document.querySelector('.footer');for(const el of document.querySelectorAll('.j2-object')){const r=Number(el.dataset.row),x=el.querySelector('.j2-glyph').getBoundingClientRect();(rows[r]??=[]).push({slot:el.dataset.slot,box:x})}for(let r=1;r<=8;r++){const cur=rows[r]||[];for(const it of cur){const s=document.querySelector(`.j2-object[data-slot="${it.slot}"]`).getBoundingClientRect();const pad=r<=2?10:12;if(it.box.left<s.left-pad||it.box.right>s.right+pad)out.push({kind:'JOINED_INK_HORIZONTAL_ESCAPE',slot:it.slot,row:r})}if(r<8&&rows[r+1]){const lowerTop=Math.min(...rows[r+1].map(x=>x.box.top));const upperBottom=Math.max(...cur.map(x=>x.box.bottom));const gap=lowerTop-upperBottom;if(gap<6)out.push({kind:'INTER_ROW_CLEARANCE_TOO_SMALL',row:r,nextRow:r+1,gap,requiredGap:6})}}if(grid&&footer&&grid.getBoundingClientRect().bottom>footer.getBoundingClientRect().top-2)out.push({kind:'GRID_FOOTER_OVERLAP'});return out}''')
    return metrics,issues


def main():
    ap=argparse.ArgumentParser(add_help=False)
    ap.add_argument('--font-file');ap.add_argument('--font-zip');ap.add_argument('--amiri-font')
    known,remaining=ap.parse_known_args(sys.argv[1:])
    out_arg=DEFAULT_OUTPUT
    for i,a in enumerate(remaining):
        if a=='--output-dir' and i+1<len(remaining):out_arg=remaining[i+1]
    out=Path(out_arg);out=out if out.is_absolute() else ROOT/out;out.mkdir(parents=True,exist_ok=True)
    if '--output-dir' not in remaining:remaining=[*remaining,'--output-dir',DEFAULT_OUTPUT]

    kfg_path,font_source=discover_font(known.font_file,known.font_zip,out)
    amiri_path,amiri_source=discover_amiri(known.amiri_font,out)
    frozen_font=build_frozen_sukun_font(kfg_path,amiri_path,out)
    font_uri=frozen_font.as_uri()

    p001.P001_CSS += f'''\n@font-face{{font-family:"{FONT_FAMILY}";src:url("{font_uri}") format("truetype");font-style:normal;font-weight:400;font-display:block;}}
.page{{padding:3.6mm 8mm 2.5mm!important;}}
.header{{height:17mm!important;flex:0 0 17mm!important;grid-template-columns:32mm minmax(0,1fr) 12mm!important;}}
.brand-logo{{width:32mm!important;height:17mm!important;}}
.learning-header-title{{font-size:6.2pt!important;letter-spacing:.16em!important;}}
.presentation{{height:18mm!important;flex:0 0 18mm!important;margin:0!important;}}
.presentation-object{{font-family:"{FONT_FAMILY}",serif!important;font-size:45pt!important;line-height:1.25!important;gap:4mm!important;}}
.presentation-object .arabic-part{{font-family:"{FONT_FAMILY}",serif!important;}}
.presentation-object .arrow{{font-size:22pt!important;}}
.j2-grid{{height:149mm!important;flex:0 0 149mm!important;row-gap:4.8mm!important;padding:2mm 0 1.5mm!important;}}
.j2-glyph{{font-family:"{FONT_FAMILY}",serif!important;font-size:39pt!important;line-height:1.16!important;padding:.2mm 1mm .3mm!important;font-feature-settings:'mark' 1,'mkmk' 1;font-kerning:normal;text-rendering:optimizeLegibility;}}
.targets{{display:none!important;height:0!important;min-height:0!important;margin:0!important;padding:0!important;border:0!important;}}
.footer{{height:12mm!important;flex:0 0 12mm!important;margin:0!important;padding:0 1mm 1mm!important;display:flex!important;align-items:center!important;justify-content:space-between!important;background:transparent!important;border-radius:0!important;color:#173a2d!important;overflow:visible!important;font-family:"{FONT_FAMILY}",serif!important;direction:rtl!important;}}
.footer .field{{display:none!important;}}
.footer::before{{content:"قُرْآنٌ · لُغَةٌ · أَدَبٌ";font-family:"{FONT_FAMILY}",serif!important;font-size:10.3pt!important;line-height:1.2!important;direction:rtl!important;}}
.footer::after{{content:"تَعَلَّمْ · اِعْمَلْ · عَلِّمْ";font-family:"{FONT_FAMILY}",serif!important;font-size:10.3pt!important;line-height:1.2!important;direction:rtl!important;}}
.bottom-band{{display:none!important;}}
'''
    p001.fit_and_inspect=jilid1_style_fit_and_inspect

    sys.argv=[sys.argv[0],*remaining]
    rc=v18.main()
    print('JILID2_P001_PRODUCTION_FROZEN_SUKUN=PASS')
    print('VISUAL_BASELINE=JILID1_CURRENT')
    print('PRACTICE_FONT_PT=39')
    print('PRESENTATION_FONT_PT=45')
    print('LEGACY_BOTTOM_DESCRIPTIONS=REMOVED')
    print('LEGACY_TEACHER_DATE_SCORE_FORM=REMOVED')
    print('ARABIC_SLOGAN_FOOTER=RESTORED')
    print('FOOTER_LEFT=قُرْآنٌ · لُغَةٌ · أَدَبٌ')
    print('FOOTER_RIGHT=تَعَلَّمْ · اِعْمَلْ · عَلِّمْ')
    print('FOOTER_FONT=KFGQPC_UTHMAN_TAHA')
    print('FOOTER_FONT_PT=10.3')
    print('ARABIC_FONT_PRIMARY=KFGQPC UTHMAN TAHA')
    print(f'KFGQPC_SOURCE={font_source}')
    print(f'AMIRI_SOURCE={amiri_source}')
    print('SUKUN_BASELINE_VERSION=V7.6')
    print('SUKUN_BASELINE_STATUS=FROZEN')
    print(f'SUKUN_Y_SHIFT={SUKUN_Y_SHIFT}')
    print(f'PRINT_READY_OUTPUT={DEFAULT_OUTPUT}')
    print('STATUS=JILID1_STYLE_CANDIDATE')
    return rc

if __name__=='__main__':raise SystemExit(main())
