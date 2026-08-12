#!/usr/bin/env python3
"""QURBATA Jilid 1 P001 - print anchor using the shared P017 visual system.

Content source is recovered QJ1-P001. Visual rules:
- A5 portrait
- KFGQPC Uthman Taha only for final Arabic
- large participant-facing Arabic (46pt presentation / 42pt practice reference)
- no visible practice boxes/borders/background cards
- 4 objects/row for 2-letter steps, 3 objects/row for 3-letter steps
- no silent substitution with legacy Amiri

Recovery source policy:
- prefer the active recovered source when present;
- otherwise materialize the exact P001 source from the official recovery commit;
- never invent replacement exercises when the worktree source is absent.
"""
from __future__ import annotations
import argparse, asyncio, html, re, subprocess, sys
from pathlib import Path
from playwright.async_api import async_playwright

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v19_kfgqpc as kfgloader

SRC=ROOT/'books/jilid-1/recovery/pages/QJ1-P001.md'
RECOVERY_COMMIT='4c8960a1173b60fa8941ca293ac0ca23f9e0b899'
RECOVERY_PATH='books/jilid-1/recovery/pages/QJ1-P001.md'
LOGO=ROOT/'books/shared/assets/qurbata-logo.svg'
DEFAULT_OUT=ROOT/'dist/qurbata-print-ready/jilid-1/pages/P001'
FONT_FAMILY='QURBATA KFGQPC Uthman Taha'

ROW_RE=re.compile(r'^\|\s*(\d+)\s*\|\s*QJ1-P001-L\d+\s*\|\s*(.*?)\s*\|\s*$')

def load_source_text():
    if SRC.exists():
        return SRC.read_text(encoding='utf-8'),'WORKTREE_RECOVERY_SOURCE'
    p=subprocess.run(
        ['git','show',f'{RECOVERY_COMMIT}:{RECOVERY_PATH}'],
        cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.PIPE
    )
    if p.returncode!=0:
        err=p.stderr.decode('utf-8','replace').strip()
        raise FileNotFoundError(
            f'QJ1_P001_RECOVERY_SOURCE_UNAVAILABLE worktree={SRC} '
            f'git={RECOVERY_COMMIT}:{RECOVERY_PATH} error={err}'
        )
    return p.stdout.decode('utf-8','replace'),'GIT_HISTORY_RECOVERY_SOURCE'

def load_objects():
    text,source_mode=load_source_text()
    items=[]
    for line in text.splitlines():
        m=ROW_RE.match(line.strip())
        if m: items.append((int(m.group(1)),m.group(2).strip()))
    if len(items)!=24: raise RuntimeError(f'QJ1_P001_OBJECT_COUNT={len(items)} expected=24 source={source_mode}')
    return [x for _,x in sorted(items)],source_mode

def base_count(s:str)->int:
    return sum(1 for c in s if '\u0621'<=c<='\u064a')

def build(font_uri:str,objects:list[str]):
    cells=[]
    for idx,obj in enumerate(objects,1):
        cls='l2' if base_count(obj)==2 else 'l3'
        cells.append(f'<div class="practice {cls}" data-slot="{idx}" lang="ar" dir="rtl">{html.escape(obj)}</div>')
    css=f'''@page{{size:A5;margin:0}}*{{box-sizing:border-box}}@font-face{{font-family:"{FONT_FAMILY}";src:url("{font_uri}") format("truetype");font-display:block}}html,body{{margin:0;padding:0;background:#fff}}.page{{width:148mm;height:210mm;padding:5mm 8mm 3.5mm;position:relative;display:flex;flex-direction:column;overflow:hidden;font-family:Arial,sans-serif}}.header{{height:17mm;display:grid;grid-template-columns:25mm 1fr 12mm;align-items:center;gap:3mm}}.brand-logo{{width:23mm;height:16.5mm;object-fit:contain}}.title{{text-align:center;color:#064d37;font-size:8.4pt;font-weight:700;letter-spacing:.11em}}.page-number{{background:#064d37;color:#fff;border-bottom:1.1mm solid #b98a2f;text-align:center;font-weight:700;padding:2.6mm 1mm 3.4mm;border-radius:0 0 3mm 3mm;font-size:12pt}}.presentation{{height:24mm;display:flex;align-items:center;justify-content:center;gap:9mm;font-family:"{FONT_FAMILY}",serif;font-size:46pt;line-height:1.05;direction:rtl;font-feature-settings:'mark' 1,'mkmk' 1}}.grid{{height:145mm;display:grid;grid-template-columns:repeat(12,1fr);grid-auto-rows:minmax(0,1fr);column-gap:4mm;row-gap:4.3mm;align-items:center;direction:rtl;overflow:visible}}.practice{{display:flex;align-items:center;justify-content:center;min-width:0;min-height:0;font-family:"{FONT_FAMILY}",serif;font-size:42pt;line-height:1.04;white-space:nowrap;border:0!important;background:transparent!important;box-shadow:none!important;font-feature-settings:'mark' 1,'mkmk' 1;text-rendering:optimizeLegibility;overflow:visible}}.l2{{grid-column:span 3}}.l3{{grid-column:span 4}}.meta{{height:12mm;margin-top:auto;border-top:.22mm solid rgba(185,138,47,.58);display:grid;grid-template-columns:1.2fr 1.2fr 1fr;gap:2mm;align-items:center;font-size:5.5pt;color:#064d37}}.meta strong{{display:block;font-size:6pt}}.bottom{{position:absolute;left:0;bottom:0;width:100%;height:1.8mm;background:#064d37}}'''
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body><main class="page"><header class="header"><img class="brand-logo" src="{LOGO.resolve().as_uri()}"><div class="title">QURBATA • JILID 1 • FATHAH</div><div class="page-number">01</div></header><section class="presentation" lang="ar" dir="rtl"><span>بَ</span><span>تَ</span><span>ثَ</span></section><section class="grid">{''.join(cells)}</section><section class="meta"><div><strong>Kompetensi</strong>Keluarga Ba berfathah</div><div><strong>Tangga</strong>2 huruf → 3 huruf</div><div><strong>Visual</strong>P017 anchor system</div></section><div class="bottom"></div></main></body></html>'''

async def render(html_path:Path,out:Path):
    pdf=out/'QURBATA-JILID-1-P001-PRINT-ANCHOR-V1.pdf'; png=out/'QURBATA-JILID-1-P001-PRINT-ANCHOR-V1.png'
    async with async_playwright() as pw:
        b=await pw.chromium.launch();p=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2)
        await p.goto(html_path.resolve().as_uri(),wait_until='networkidle');await p.evaluate('document.fonts.ready')
        ok=await p.evaluate(f"()=>document.fonts.check('42pt \\\"{FONT_FAMILY}\\\"','بَ تَ ثَ')")
        if not ok: raise RuntimeError('QJ1_P001_KFGQPC_FONT_BINDING_FAIL')
        count=await p.locator('.practice').count()
        if count!=24: raise RuntimeError(f'QJ1_P001_RENDERED_OBJECT_COUNT={count}')
        boxed=await p.evaluate("()=>[...document.querySelectorAll('.practice')].filter(e=>{const s=getComputedStyle(e);return s.borderTopWidth!=='0px'||s.boxShadow!=='none'||s.backgroundColor!=='rgba(0, 0, 0, 0)'&&s.backgroundColor!=='transparent'}).length")
        if boxed: raise RuntimeError(f'QJ1_P001_VISIBLE_BOX_REGRESSION={boxed}')
        await p.screenshot(path=str(png),full_page=True)
        await p.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'})
        await b.close()
    return pdf,png

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output-dir',default=str(DEFAULT_OUT.relative_to(ROOT)));ap.add_argument('--font-file');ap.add_argument('--font-zip');a=ap.parse_args()
    out=Path(a.output_dir);out=out if out.is_absolute() else ROOT/out;out.mkdir(parents=True,exist_ok=True)
    font,src=kfgloader.discover_font(a.font_file,a.font_zip,out)
    objs,source_mode=load_objects();h=out/'QURBATA-JILID-1-P001-PRINT-ANCHOR-V1.html';h.write_text(build(font.resolve().as_uri(),objs),encoding='utf-8')
    pdf,png=asyncio.run(render(h,out))
    print('QJ1_P001_PRINT_ANCHOR=PASS');print('PAGE=P001');print('BASE_FONT=KFGQPC_UTHMAN_TAHA');print('PRESENTATION_FONT_PT=46');print('PRACTICE_FONT_PT=42');print('VISIBLE_BOXES=0');print('LAYOUT=4_OBJECTS_L2|3_OBJECTS_L3');print('OBJECTS=24');print(f'CONTENT_SOURCE_MODE={source_mode}');print(f'CONTENT_SOURCE_COMMIT={RECOVERY_COMMIT if source_mode=="GIT_HISTORY_RECOVERY_SOURCE" else "WORKTREE"}');print(f'FONT_SOURCE={src}');print(f'PDF={pdf.relative_to(ROOT)}');print(f'PNG={png.relative_to(ROOT)}');return 0
if __name__=='__main__':raise SystemExit(main())
