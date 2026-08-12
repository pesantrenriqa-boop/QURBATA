#!/usr/bin/env python3
from __future__ import annotations
import argparse, asyncio, html, sys
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v19_kfgqpc as kfgloader
LOGO=ROOT/'books/shared/assets/qurbata-logo.svg'; OUT0=ROOT/'dist/qurbata-print-ready/jilid-1/pages/P003'; FONT='QURBATA KFGQPC Uthman Taha'
SOURCE='books/jilid-1/recovery/pages/QJ1-P003-DEC-CUR-007-CANDIDATE.md'
EXERCISES=['جَ حَ','ءَ أَ','خَ جَ','بَ تَ','حَ خَ','ثَ ءَ','جَ خَ','أَ بَ','جَ حَ خَ','ءَ أَ بَ','حَ خَ جَ','تَ ثَ ءَ','خَ جَ حَ','أَ تَ بَ','جَ خَ حَ','ثَ أَ تَ','حَ جَ خَ','بَ ءَ ثَ','خَ حَ جَ','تَ بَ أَ','جَ جَ حَ','ءَ ثَ بَ','خَ خَ حَ','أَ ءَ تَ']
FOCUS={'جَ','حَ','خَ'}; REVIEW={'ءَ','أَ','بَ','تَ','ثَ'}
def toks(s): return s.split()
def obj(s): return '<span class="run">'+''.join(f'<span>{html.escape(x)}</span>' for x in toks(s))+'</span>'
def audit_source():
    ts=[x for e in EXERCISES for x in toks(e)]
    f=sum(x in FOCUS for x in ts); r=sum(x in REVIEW for x in ts)
    if len(EXERCISES)!=24 or len(ts)!=64 or f!=32 or r!=32: raise RuntimeError(f'P003_DEC_CUR_007_DISTRIBUTION_FAIL total={len(ts)} focus={f} review={r}')
    if any(x not in FOCUS|REVIEW for x in ts): raise RuntimeError('P003_WHITELIST_FAIL')
def rows():
    items=EXERCISES[:-1]
    l2=items[:8]; l3=items[8:]
    out=[]
    for i in range(0,8,4): out.append('<div class="row r2">'+''.join(f'<div class="practice l2">{obj(x)}</div>' for x in l2[i:i+4])+'</div>')
    for i in range(0,15,3): out.append('<div class="row r3">'+''.join(f'<div class="practice l3">{obj(x)}</div>' for x in l3[i:i+3])+'</div>')
    return ''.join(out)
def doc(font_uri):
    css=f'''@page{{size:A5;margin:0}}*{{box-sizing:border-box}}@font-face{{font-family:"{FONT}";src:url("{font_uri}") format("truetype");font-display:block}}html,body{{margin:0;background:#fff}}.page{{width:148mm;height:210mm;padding:3.6mm 8mm 2.5mm;display:flex;flex-direction:column;overflow:hidden;font-family:Arial,sans-serif}}.header{{height:17mm;flex:0 0 17mm;position:relative;display:flex;align-items:center;justify-content:center}}.logo{{position:absolute;left:0;width:32mm;height:17mm;object-fit:contain}}.title{{position:absolute;left:50%;transform:translateX(-50%);color:#064d37;font:700 6.2pt Georgia,"Times New Roman",serif;letter-spacing:.16em;white-space:nowrap}}.pageno{{position:absolute;right:0;top:0;width:12mm;background:#064d37;color:#fff;border-bottom:1mm solid #b98a2f;text-align:center;font-weight:700;padding:2.2mm 1mm 3mm;border-radius:0 0 3mm 3mm;font-size:12pt}}.presentation{{height:20mm;flex:0 0 20mm;display:flex;align-items:center;justify-content:center;gap:13mm;font-family:"{FONT}",serif;font-size:46pt;line-height:1;direction:rtl;font-feature-settings:'mark' 1,'mkmk' 1}}.grid{{height:158mm;flex:0 0 158mm;display:grid;grid-template-rows:repeat(7,minmax(0,1fr));row-gap:3.2mm;padding:.8mm 0 1mm}}.row{{display:flex;direction:rtl;align-items:center;justify-content:center;min-height:0}}.r2{{gap:10mm}}.r3{{gap:11mm}}.practice{{display:flex;align-items:center;justify-content:center;flex:0 0 auto;font-family:"{FONT}",serif;font-size:40pt;line-height:1.02;white-space:nowrap;font-feature-settings:'mark' 1,'mkmk' 1}}.l2{{width:23mm}}.l3{{width:35mm}}.run{{display:inline-flex;direction:rtl;align-items:center;justify-content:center}}.l2 .run{{gap:2.8mm}}.l3 .run{{gap:2.4mm}}.footer{{height:12mm;flex:0 0 12mm;display:flex;justify-content:space-between;align-items:center;padding-bottom:2.2mm;color:#173a2d}}.ar{{font-family:"{FONT}",serif;font-size:10.3pt;direction:rtl;font-feature-settings:'mark' 1,'mkmk' 1}}'''
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body><main class="page"><header class="header"><img class="logo" src="{LOGO.resolve().as_uri()}"><div class="title">QURBATA · JILID 1</div><div class="pageno">03</div></header><section class="presentation" lang="ar" dir="rtl"><span>جَ</span><span>حَ</span><span>خَ</span></section><section class="grid">{rows()}</section><footer class="footer"><span class="ar">قُرْآنٌ · لُغَةٌ · أَدَبٌ</span><span class="ar">تَعَلَّمْ · اِعْمَلْ · عَلِّمْ</span></footer></main></body></html>'''
def free(base):
    if not base.exists(): return base
    try:
        with open(base,'ab'): pass
        return base
    except PermissionError: pass
    for n in range(1,100):
        p=base.with_name(base.stem+f'-R{n}'+base.suffix)
        if not p.exists(): return p
    raise RuntimeError('NO_FREE_OUTPUT')
async def render(h,out):
    pdf=free(out/'QURBATA-JILID-1-P003-CANDIDATE-V1.pdf'); png=free(out/'QURBATA-JILID-1-P003-CANDIDATE-V1.png')
    async with async_playwright() as pw:
        b=await pw.chromium.launch(); p=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2); await p.goto(h.resolve().as_uri(),wait_until='networkidle'); await p.evaluate('document.fonts.ready')
        if not await p.evaluate(f"()=>document.fonts.check('40pt \\\"{FONT}\\\"','جَ حَ خَ')"): raise RuntimeError('P003_FONT_BINDING_FAIL')
        if await p.locator('.practice').count()!=23: raise RuntimeError('P003_OBJECT_COUNT_FAIL')
        if await p.locator('.r2').count()!=2 or await p.locator('.r3').count()!=5: raise RuntimeError('P003_ROW_COUNT_FAIL')
        await p.screenshot(path=str(png),full_page=True); await p.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'}); await b.close()
    return pdf,png
def main():
    audit_source(); ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',default=str(OUT0.relative_to(ROOT))); ap.add_argument('--font-file'); ap.add_argument('--font-zip'); a=ap.parse_args(); out=Path(a.output_dir); out=out if out.is_absolute() else ROOT/out; out.mkdir(parents=True,exist_ok=True); font,src=kfgloader.discover_font(a.font_file,a.font_zip,out); h=out/'QURBATA-JILID-1-P003-CANDIDATE-V1.html'; h.write_text(doc(font.resolve().as_uri()),encoding='utf-8'); pdf,png=asyncio.run(render(h,out)); print('QJ1_P003_CANDIDATE_V1=PASS'); print('POLICY=DEC_CUR_007_50_50_CUMULATIVE'); print('SOURCE_TOKENS=64'); print('FOCUS_TOKENS=32'); print('REVIEW_TOKENS=32'); print('MATERIAL_NEW=جَ|حَ|خَ'); print('REVIEW=ءَ|أَ|بَ|تَ|ثَ'); print('SOURCE_EXERCISES=24'); print('RENDERED_EXERCISES=23'); print('REMOVED_ORPHAN_SOURCE=L24'); print('GLOBAL_SHELL=P001_FROZEN_CLEAN_V10'); print('BASE_FONT=KFGQPC_UTHMAN_TAHA'); print(f'FONT_SOURCE={src}'); print(f'PDF={pdf.relative_to(ROOT)}'); return 0
if __name__=='__main__': raise SystemExit(main())
