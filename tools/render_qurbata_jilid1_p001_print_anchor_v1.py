#!/usr/bin/env python3
"""QURBATA Jilid 1 P001 — V8 explicit proportional groups: letters close, groups wide."""
from __future__ import annotations
import argparse, asyncio, html, re, subprocess, sys
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path:sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v19_kfgqpc as kfgloader
SRC=ROOT/'books/jilid-1/recovery/pages/QJ1-P001.md';RECOVERY_COMMIT='4c8960a1173b60fa8941ca293ac0ca23f9e0b899';RECOVERY_PATH='books/jilid-1/recovery/pages/QJ1-P001.md';LOGO=ROOT/'books/shared/assets/qurbata-logo.svg';DEFAULT_OUT=ROOT/'dist/qurbata-print-ready/jilid-1/pages/P001';FONT_FAMILY='QURBATA KFGQPC Uthman Taha';ROW_RE=re.compile(r'^\|\s*(\d+)\s*\|\s*QJ1-P001-L\d+\s*\|\s*(.*?)\s*\|\s*$')
def load_source_text():
    if SRC.exists():return SRC.read_text(encoding='utf-8'),'WORKTREE_RECOVERY_SOURCE'
    p=subprocess.run(['git','show',f'{RECOVERY_COMMIT}:{RECOVERY_PATH}'],cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if p.returncode:raise FileNotFoundError('QJ1_P001_RECOVERY_SOURCE_UNAVAILABLE '+p.stderr.decode('utf-8','replace'))
    return p.stdout.decode('utf-8','replace'),'GIT_HISTORY_RECOVERY_SOURCE'
def load_objects():
    text,mode=load_source_text();items=[]
    for line in text.splitlines():
        m=ROW_RE.match(line.strip())
        if m:items.append((int(m.group(1)),m.group(2).strip()))
    if len(items)!=24:raise RuntimeError(f'QJ1_P001_OBJECT_COUNT={len(items)} expected=24')
    ordered=[x for _,x in sorted(items)];return ordered[:-1],mode,ordered[-1]
def tokens(s):return [x for x in s.split() if x]
def obj_html(obj):return '<span class="token-run">'+''.join(f'<span class="letter-token">{html.escape(t)}</span>' for t in tokens(obj))+'</span>'
def build_rows(objects):
    l2=[o for o in objects if len(tokens(o))==2];l3=[o for o in objects if len(tokens(o))==3];rows=[]
    for i in range(0,len(l2),4):rows.append('<div class="practice-row row-l2">'+''.join(f'<div class="practice l2">{obj_html(o)}</div>' for o in l2[i:i+4])+'</div>')
    for i in range(0,len(l3),3):rows.append('<div class="practice-row row-l3">'+''.join(f'<div class="practice l3">{obj_html(o)}</div>' for o in l3[i:i+3])+'</div>')
    return ''.join(rows)
def build(font_uri,objects):
    rows=build_rows(objects)
    css=f'''@page{{size:A5;margin:0}}*{{box-sizing:border-box}}@font-face{{font-family:"{FONT_FAMILY}";src:url("{font_uri}") format("truetype");font-display:block}}html,body{{margin:0;padding:0;background:#fff}}.page{{width:148mm;height:210mm;padding:3.6mm 8mm 0;display:flex;flex-direction:column;overflow:hidden;font-family:Arial,sans-serif}}.header{{height:15mm;flex:0 0 15mm;position:relative;display:flex;align-items:center;justify-content:center}}.brand-logo{{position:absolute;left:0;top:.2mm;width:21mm;height:14mm;object-fit:contain}}.title{{position:absolute;left:50%;transform:translateX(-50%);width:82mm;text-align:center;color:#064d37;font-family:Georgia,"Times New Roman",serif;font-size:9.2pt;font-weight:700;letter-spacing:.16em;font-variant:small-caps;line-height:1;white-space:nowrap}}.title:before,.title:after{{content:'◆';color:#b98a2f;font-size:5.5pt;vertical-align:1pt;margin:0 2.2mm}}.page-number{{position:absolute;right:0;top:0;background:#064d37;color:#fff;border-bottom:1mm solid #b98a2f;text-align:center;font-weight:700;padding:2.2mm 1mm 3mm;border-radius:0 0 3mm 3mm;font-size:12pt;width:12mm}}.presentation{{height:20mm;flex:0 0 20mm;display:flex;align-items:center;justify-content:center;gap:13mm;font-family:"{FONT_FAMILY}",serif;font-size:46pt;line-height:1.05;direction:rtl;font-feature-settings:'mark' 1,'mkmk' 1}}.practice-grid{{height:164mm;flex:0 0 164mm;display:grid;grid-template-rows:repeat(7,minmax(0,1fr));row-gap:3.2mm;padding:.8mm 0 1mm;overflow:visible}}.practice-row{{display:flex;direction:rtl;align-items:center;justify-content:center;min-height:0;width:100%;overflow:visible}}.row-l2{{gap:10mm}}.row-l3{{gap:11mm}}.practice{{display:flex;align-items:center;justify-content:center;flex:0 0 auto;font-family:"{FONT_FAMILY}",serif;font-size:40pt;line-height:1.02;white-space:nowrap;border:0!important;background:transparent!important;box-shadow:none!important;font-feature-settings:'mark' 1,'mkmk' 1;text-rendering:optimizeLegibility;overflow:visible}}.l2{{width:23mm}}.l3{{width:35mm}}.token-run{{display:inline-flex;direction:rtl;align-items:center;justify-content:center}}.l2 .token-run{{gap:2.8mm}}.l3 .token-run{{gap:2.4mm}}.letter-token{{display:inline-block;direction:rtl;unicode-bidi:isolate}}.decor-footer{{height:7mm;flex:0 0 7mm;margin:0 -8mm;position:relative;border-top:.32mm solid #b98a2f;background:linear-gradient(to bottom,#fff 0,#fff 1.3mm,#064d37 1.3mm,#064d37 100%);overflow:visible}}.decor-footer:before{{content:'';position:absolute;left:7mm;right:7mm;top:2.4mm;height:2.4mm;opacity:.24;background:repeating-linear-gradient(45deg,transparent 0 2.2mm,#b98a2f 2.2mm 2.5mm,transparent 2.5mm 4.7mm)}}.decor-footer:after{{content:'Q';position:absolute;left:50%;top:-2.7mm;transform:translateX(-50%);width:8mm;height:8mm;border-radius:50%;display:flex;align-items:center;justify-content:center;background:#064d37;border:.6mm solid #b98a2f;color:#fff;font-family:Georgia,serif;font-size:7pt;font-weight:700;box-shadow:0 0 0 .6mm #fff}}.footer-left,.footer-right{{position:absolute;bottom:1.05mm;color:#fff;font-family:Georgia,"Times New Roman",serif;font-size:4.3pt;font-weight:700;letter-spacing:.13em;z-index:2}}.footer-left{{left:4mm}}.footer-right{{right:4mm}}'''
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body><main class="page"><header class="header"><img class="brand-logo" src="{LOGO.resolve().as_uri()}"><div class="title">QURBATA · JILID 1 · FATHAH</div><div class="page-number">01</div></header><section class="presentation" lang="ar" dir="rtl"><span>بَ</span><span>تَ</span><span>ثَ</span></section><section class="practice-grid">{rows}</section><footer class="decor-footer"><span class="footer-left">QURBATA</span><span class="footer-right">BACA · PAHAMI · AMALKAN</span></footer></main></body></html>'''
async def render(h,out):
    pdf=out/'QURBATA-JILID-1-P001-PRINT-ANCHOR-V8-GROUPED-SPACING.pdf';png=out/'QURBATA-JILID-1-P001-PRINT-ANCHOR-V8-GROUPED-SPACING.png'
    async with async_playwright() as pw:
        b=await pw.chromium.launch();p=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);await p.goto(h.resolve().as_uri(),wait_until='networkidle');await p.evaluate('document.fonts.ready')
        if not await p.evaluate(f"()=>document.fonts.check('40pt \\\"{FONT_FAMILY}\\\"','بَ تَ ثَ')"):raise RuntimeError('QJ1_P001_KFGQPC_FONT_BINDING_FAIL')
        if await p.locator('.practice').count()!=23:raise RuntimeError('QJ1_P001_OBJECT_COUNT_FAIL')
        if await p.locator('.row-l2').count()!=2 or await p.locator('.row-l3').count()!=5:raise RuntimeError('QJ1_P001_GROUP_ROW_COUNT_FAIL')
        # Each three-letter row must contain exactly 3 visually separate groups.
        counts=await p.locator('.row-l3').evaluate_all('(rows)=>rows.map(r=>r.querySelectorAll(":scope > .practice").length)')
        if counts!=[3,3,3,3,3]:raise RuntimeError(f'QJ1_P001_THREE_LETTER_GROUPING_FAIL={counts}')
        await p.screenshot(path=str(png),full_page=True);await p.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await b.close()
    return pdf,png
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output-dir',default=str(DEFAULT_OUT.relative_to(ROOT)));ap.add_argument('--font-file');ap.add_argument('--font-zip');a=ap.parse_args();out=Path(a.output_dir);out=out if out.is_absolute() else ROOT/out;out.mkdir(parents=True,exist_ok=True);font,src=kfgloader.discover_font(a.font_file,a.font_zip,out);objs,mode,removed=load_objects();h=out/'QURBATA-JILID-1-P001-PRINT-ANCHOR-V8-GROUPED-SPACING.html';h.write_text(build(font.resolve().as_uri(),objs),encoding='utf-8');pdf,png=asyncio.run(render(h,out));print('QJ1_P001_PRINT_ANCHOR_V8=PASS');print('BASE_FONT=KFGQPC_UTHMAN_TAHA');print('PRACTICE_FONT_PT=40');print('TWO_LETTER=LETTERS_CLOSE_2.8MM|GROUP_GAP_10MM');print('THREE_LETTER=LETTERS_CLOSE_2.4MM|GROUP_GAP_11MM|GROUPS_PER_ROW=3');print('GROUPING=3_LETTERS_THEN_WIDE_SPACE_THEN_3_LETTERS');print('REMOVED_ORPHAN_OBJECT='+removed);print(f'CONTENT_SOURCE_MODE={mode}');print(f'FONT_SOURCE={src}');print(f'PDF={pdf.relative_to(ROOT)}');print(f'PNG={png.relative_to(ROOT)}');return 0
if __name__=='__main__':raise SystemExit(main())
