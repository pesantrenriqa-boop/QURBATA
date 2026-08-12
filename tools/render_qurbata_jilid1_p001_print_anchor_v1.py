#!/usr/bin/env python3
"""QURBATA Jilid 1 P001 — V6 refined spacing, aligned decorative header, QURBATA footer."""
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
    ordered=[x for _,x in sorted(items)]
    return ordered[:-1],mode,ordered[-1]
def tokens(s):return [x for x in s.split() if x]
def spaced_object(obj):return ''.join(f'<span class="letter-token">{html.escape(t)}</span>' for t in tokens(obj))
def build(font_uri,objects):
    cells=[]
    for idx,obj in enumerate(objects,1):
        cls='l2' if len(tokens(obj))==2 else 'l3';cells.append(f'<div class="practice {cls}" data-slot="{idx}" lang="ar" dir="rtl"><span class="token-run">{spaced_object(obj)}</span></div>')
    css=f'''@page{{size:A5;margin:0}}*{{box-sizing:border-box}}@font-face{{font-family:"{FONT_FAMILY}";src:url("{font_uri}") format("truetype");font-display:block}}html,body{{margin:0;padding:0;background:#fff}}.page{{width:148mm;height:210mm;padding:3.6mm 8mm 0;position:relative;display:flex;flex-direction:column;overflow:hidden;font-family:Arial,sans-serif}}.header{{height:15mm;flex:0 0 15mm;position:relative;display:flex;align-items:center;justify-content:center}}.brand-logo{{position:absolute;left:0;top:.2mm;width:21mm;height:14mm;object-fit:contain}}.title{{position:absolute;left:50%;transform:translateX(-50%);width:82mm;text-align:center;color:#064d37;font-family:Georgia,"Times New Roman",serif;font-size:9.2pt;font-weight:700;letter-spacing:.16em;font-variant:small-caps;line-height:1;white-space:nowrap}}.title:before,.title:after{{content:'◆';color:#b98a2f;font-size:5.5pt;vertical-align:1pt;margin:0 2.2mm}}.page-number{{position:absolute;right:0;top:0;background:#064d37;color:#fff;border-bottom:1mm solid #b98a2f;text-align:center;font-weight:700;padding:2.2mm 1mm 3mm;border-radius:0 0 3mm 3mm;font-size:12pt;width:12mm}}.presentation{{height:20mm;flex:0 0 20mm;display:flex;align-items:center;justify-content:center;gap:13mm;font-family:"{FONT_FAMILY}",serif;font-size:46pt;line-height:1.05;direction:rtl;font-feature-settings:'mark' 1,'mkmk' 1;overflow:visible}}.presentation span{{display:inline-block}}.grid{{height:164mm;flex:0 0 164mm;display:grid;grid-template-columns:repeat(12,1fr);grid-template-rows:repeat(7,minmax(0,1fr));column-gap:5mm;row-gap:3.2mm;align-items:center;direction:rtl;overflow:visible;padding:.8mm 0 1mm}}.practice{{display:flex;align-items:center;justify-content:center;min-width:0;min-height:0;font-family:"{FONT_FAMILY}",serif;font-size:46pt;line-height:1.02;white-space:nowrap;border:0!important;background:transparent!important;box-shadow:none!important;font-feature-settings:'mark' 1,'mkmk' 1;text-rendering:optimizeLegibility;overflow:visible}}.l2{{grid-column:span 3}}.l3{{grid-column:span 4}}.token-run{{display:inline-flex;direction:rtl;align-items:center;justify-content:center}}.l2 .token-run{{gap:8mm}}.l3 .token-run{{gap:6mm}}.letter-token{{display:inline-block;direction:rtl;unicode-bidi:isolate}}.decor-footer{{height:7mm;flex:0 0 7mm;margin:0 -8mm;position:relative;border-top:.32mm solid #b98a2f;background:linear-gradient(to bottom,#fff 0,#fff 1.3mm,#064d37 1.3mm,#064d37 100%);overflow:visible}}.decor-footer:before{{content:'';position:absolute;left:7mm;right:7mm;top:2.4mm;height:2.4mm;opacity:.24;background:repeating-linear-gradient(45deg,transparent 0 2.2mm,#b98a2f 2.2mm 2.5mm,transparent 2.5mm 4.7mm)}}.decor-footer:after{{content:'Q';position:absolute;left:50%;top:-2.7mm;transform:translateX(-50%);width:8mm;height:8mm;border-radius:50%;display:flex;align-items:center;justify-content:center;background:#064d37;border:.6mm solid #b98a2f;color:#fff;font-family:Georgia,serif;font-size:7pt;font-weight:700;box-shadow:0 0 0 .6mm #fff}}.footer-left,.footer-right{{position:absolute;bottom:1.05mm;color:#fff;font-family:Georgia,"Times New Roman",serif;font-size:4.3pt;font-weight:700;letter-spacing:.13em;z-index:2}}.footer-left{{left:4mm}}.footer-right{{right:4mm}}'''
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body><main class="page"><header class="header"><img class="brand-logo" src="{LOGO.resolve().as_uri()}"><div class="title">QURBATA · JILID 1 · FATHAH</div><div class="page-number">01</div></header><section class="presentation" lang="ar" dir="rtl"><span>بَ</span><span>تَ</span><span>ثَ</span></section><section class="grid">{''.join(cells)}</section><footer class="decor-footer"><span class="footer-left">QURBATA</span><span class="footer-right">BACA · PAHAMI · AMALKAN</span></footer></main></body></html>'''
async def render(h,out):
    pdf=out/'QURBATA-JILID-1-P001-PRINT-ANCHOR-V6-REFINED.pdf';png=out/'QURBATA-JILID-1-P001-PRINT-ANCHOR-V6-REFINED.png'
    async with async_playwright() as pw:
        b=await pw.chromium.launch();p=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);await p.goto(h.resolve().as_uri(),wait_until='networkidle');await p.evaluate('document.fonts.ready')
        if not await p.evaluate(f"()=>document.fonts.check('46pt \\\"{FONT_FAMILY}\\\"','بَ تَ ثَ')"):raise RuntimeError('QJ1_P001_KFGQPC_FONT_BINDING_FAIL')
        count=await p.locator('.practice').count()
        if count!=23:raise RuntimeError(f'QJ1_P001_RENDERED_OBJECT_COUNT={count} expected=23')
        if await p.locator('.presentation').count()!=1:raise RuntimeError('QJ1_P001_PRESENTATION_REQUIRED')
        if await p.locator('.decor-footer').count()!=1:raise RuntimeError('QJ1_P001_DECOR_FOOTER_REQUIRED')
        l2=await p.locator('.practice.l2').count();l3=await p.locator('.practice.l3').count()
        if (l2,l3)!=(8,15):raise RuntimeError(f'QJ1_P001_ROW_DISTRIBUTION_INVALID l2={l2} l3={l3}')
        await p.screenshot(path=str(png),full_page=True);await p.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await b.close()
    return pdf,png
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output-dir',default=str(DEFAULT_OUT.relative_to(ROOT)));ap.add_argument('--font-file');ap.add_argument('--font-zip');a=ap.parse_args();out=Path(a.output_dir);out=out if out.is_absolute() else ROOT/out;out.mkdir(parents=True,exist_ok=True);font,src=kfgloader.discover_font(a.font_file,a.font_zip,out);objs,mode,removed=load_objects();h=out/'QURBATA-JILID-1-P001-PRINT-ANCHOR-V6-REFINED.html';h.write_text(build(font.resolve().as_uri(),objs),encoding='utf-8');pdf,png=asyncio.run(render(h,out));print('QJ1_P001_PRINT_ANCHOR_V6=PASS');print('BASE_FONT=KFGQPC_UTHMAN_TAHA');print('PRESENTATION_BLOCK=PRESERVED');print('PRACTICE_FONT_PT=46');print('VISIBLE_BOXES=0');print('OBJECTS_RENDERED=23');print('REMOVED_ORPHAN_OBJECT='+removed);print('ROW_1_2=2_LETTER|4_OBJECTS_PER_ROW|LETTER_GAP_8MM');print('ROW_3_7=3_LETTER|3_OBJECTS_PER_ROW|LETTER_GAP_6MM');print('HEADER=DECORATIVE_CENTERED_ALIGNED_WITH_PRESENTATION');print('DECORATIVE_FOOTER=QURBATA_GREEN_GOLD_PATTERN_MEDALLION');print(f'CONTENT_SOURCE_MODE={mode}');print(f'FONT_SOURCE={src}');print(f'PDF={pdf.relative_to(ROOT)}');print(f'PNG={png.relative_to(ROOT)}');return 0
if __name__=='__main__':raise SystemExit(main())
