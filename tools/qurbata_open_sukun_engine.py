#!/usr/bin/env python3
"""Validated QURBATA open-sukun font engine.

Visual model approved in SUKUN LAB V7.1:
- all Arabic base glyphs: KFGQPC Uthman Taha
- semantic/render codepoint: U+0652
- visual outline for U+0652: Amiri U+06E1 open ras-al-kha
- KFGQPC U+0652 positioning/GPOS is preserved

This module creates only a runtime derivative font under dist. It never commits a
font binary and does not alter source fonts.
"""
from __future__ import annotations
import os,urllib.request
from pathlib import Path
AMIRI_URL='https://github.com/aliftype/amiri/raw/refs/heads/main/fonts/Amiri-Regular.ttf'

def discover_amiri(root:Path,out:Path,explicit:str|None=None)->Path:
    candidates=[]
    if explicit:candidates.append(Path(explicit).expanduser())
    env=os.environ.get('QURBATA_AMIRI_FONT')
    if env:candidates.append(Path(env).expanduser())
    home=Path.home();candidates += [root/'_local/fonts'/'Amiri-Regular.ttf',home/'Downloads'/'Amiri-Regular.ttf',Path(r'C:\Windows\Fonts\Amiri-Regular.ttf'),home/'AppData/Local/Microsoft/Windows/Fonts/Amiri-Regular.ttf']
    for p in candidates:
        if p.is_file():return p.resolve()
    dst=out/'_runtime_font'/'Amiri-Regular.ttf';dst.parent.mkdir(parents=True,exist_ok=True)
    req=urllib.request.Request(AMIRI_URL,headers={'User-Agent':'QURBATA-renderer/1.0'});dst.write_bytes(urllib.request.urlopen(req,timeout=30).read())
    if dst.stat().st_size<50000:raise RuntimeError('AMIRI_DOWNLOAD_INVALID')
    return dst.resolve()

def build_open_sukun_font(kfg_path:Path,out:Path,root:Path,amiri_font:str|None=None)->Path:
    from fontTools.ttLib import TTFont
    from fontTools.pens.ttGlyphPen import TTGlyphPen
    from fontTools.pens.transformPen import TransformPen
    amiri=discover_amiri(root,out,amiri_font);k=TTFont(str(kfg_path));a=TTFont(str(amiri));kc={};ac={}
    for t in k['cmap'].tables:
        if t.isUnicode():kc.update(t.cmap)
    for t in a['cmap'].tables:
        if t.isUnicode():ac.update(t.cmap)
    target=kc.get(0x0652);source=ac.get(0x06E1)
    if not target:raise RuntimeError('KFGQPC_U0652_NOT_FOUND')
    if not source:raise RuntimeError('AMIRI_U06E1_NOT_FOUND')
    if 'glyf' not in k:raise RuntimeError('KFGQPC_NOT_TRUETYPE_GLYF')
    scale=k['head'].unitsPerEm/a['head'].unitsPerEm;pen=TTGlyphPen(k.getGlyphSet());tp=TransformPen(pen,(scale,0,0,scale,0,0));a.getGlyphSet()[source].draw(tp);k['glyf'][target]=pen.glyph()
    dst=out/'_runtime_font'/'KFGQPC-QURBATA-OPEN-SUKUN.ttf';dst.parent.mkdir(parents=True,exist_ok=True);k.save(str(dst));return dst

def font_face_css(font_path:Path,family:str='QURBATA KFGQPC Open Sukun')->str:
    return '@font-face{font-family:"'+family+'";src:url("'+font_path.resolve().as_uri()+'") format("truetype");font-display:block}'
