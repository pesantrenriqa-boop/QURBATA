#!/usr/bin/env python3
"""QURBATA Jilid 2 P001 — production KFGQPC renderer with frozen V7.6 sukun.

Arabic base letters and native mark positioning stay KFGQPC Uthman Taha Naskh.
Only the U+0652 sukun outline is replaced at runtime with Amiri U+06E1 and shifted
vertically by the approved frozen offset -1700 KFGQPC font units. Font binaries are
runtime-only and are never committed to the repository.
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


def discover_font(explicit_font:str|None, explicit_zip:str|None, out_dir:Path)->tuple[Path,str]:
    candidates=[]
    if explicit_font: candidates.append(Path(explicit_font).expanduser())
    env=os.environ.get('QURBATA_KFGQPC_FONT')
    if env: candidates.append(Path(env).expanduser())
    home=Path.home()
    candidates += [ROOT/'_local/fonts'/TTF_BASENAME,home/'Downloads'/TTF_BASENAME,home/'Downloads'/'KFGQPC Uthman Taha Naskh Regular'/TTF_BASENAME]
    for p in candidates:
        if p.is_file(): return p.resolve(),'TTF'
    zips=[]
    if explicit_zip: zips.append(Path(explicit_zip).expanduser())
    zips += [home/'Downloads'/ZIP_BASENAME,ROOT/'_local/fonts'/ZIP_BASENAME]
    for zp in zips:
        if not zp.is_file(): continue
        target=out_dir/'_runtime_font'/TTF_BASENAME;target.parent.mkdir(parents=True,exist_ok=True)
        with zipfile.ZipFile(zp) as z:
            match=next((n for n in z.namelist() if n.lower().endswith(TTF_BASENAME.lower())),None)
            if not match: raise RuntimeError(f'KFGQPC_TTF_NOT_FOUND_IN_ZIP={zp}')
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


def main():
    ap=argparse.ArgumentParser(add_help=False)
    ap.add_argument('--font-file');ap.add_argument('--font-zip');ap.add_argument('--amiri-font')
    known,remaining=ap.parse_known_args(sys.argv[1:])
    out_arg='dist/jilid-2-p001-production-frozen-sukun'
    for i,a in enumerate(remaining):
        if a=='--output-dir' and i+1<len(remaining):out_arg=remaining[i+1]
    out=Path(out_arg);out=out if out.is_absolute() else ROOT/out;out.mkdir(parents=True,exist_ok=True)

    kfg_path,font_source=discover_font(known.font_file,known.font_zip,out)
    amiri_path,amiri_source=discover_amiri(known.amiri_font,out)
    frozen_font=build_frozen_sukun_font(kfg_path,amiri_path,out)
    font_uri=frozen_font.as_uri()

    p001.P001_CSS += f'''\n@font-face{{font-family:"{FONT_FAMILY}";src:url("{font_uri}") format("truetype");font-style:normal;font-weight:400;font-display:block;}}\n.j2-glyph,.presentation-object,.presentation-object .arabic-part{{font-family:"{FONT_FAMILY}",serif!important;font-feature-settings:'mark' 1,'mkmk' 1;font-kerning:normal;text-rendering:optimizeLegibility;}}\n'''

    sys.argv=[sys.argv[0],*remaining]
    rc=v18.main()
    print('JILID2_P001_PRODUCTION_FROZEN_SUKUN=PASS')
    print('ARABIC_FONT_PRIMARY=KFGQPC UTHMAN TAHA')
    print(f'KFGQPC_SOURCE={font_source}')
    print(f'AMIRI_SOURCE={amiri_source}')
    print('SUKUN_BASELINE_VERSION=V7.6')
    print('SUKUN_BASELINE_STATUS=FROZEN')
    print('SUKUN_RENDER_CODEPOINT=U+0652')
    print('SUKUN_VISUAL_OUTLINE=AMIRI_U+06E1')
    print(f'SUKUN_Y_SHIFT={SUKUN_Y_SHIFT}')
    print('POSITIONING=KFGQPC_U+0652_GPOS_PRESERVED')
    print('FONT_BINARY_REPOSITORY_STORAGE=NO')
    print('V18_GEOMETRY=PRESERVED')
    print('STATUS=PRODUCTION_INTEGRATION_CANDIDATE')
    return rc

if __name__=='__main__':raise SystemExit(main())
