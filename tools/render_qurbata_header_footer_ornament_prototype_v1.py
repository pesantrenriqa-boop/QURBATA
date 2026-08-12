#!/usr/bin/env python3
"""QURBATA header/footer prototype v7 — slogans inside grayscale-safe bottom edge ornament."""
from pathlib import Path
import asyncio,sys
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path:sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v19_kfgqpc as kfgloader
OUT=ROOT/'dist/qurbata-brand-prototypes/header-footer-v7';LOGO=ROOT/'books/shared/assets/qurbata-logo.svg';FONT_FAMILY='QURBATA KFGQPC Uthman Taha'
def html_doc(font_uri):
 return f'''<!doctype html><html><head><meta charset="utf-8"><style>
@page{{size:A5;margin:0}}*{{box-sizing:border-box}}@font-face{{font-family:"{FONT_FAMILY}";src:url("{font_uri}") format("truetype");font-display:block}}html,body{{margin:0;background:#fff;font-family:Arial,sans-serif}}.page{{width:148mm;height:210mm;padding:7mm 10mm 0;display:flex;flex-direction:column;overflow:hidden}}.header{{height:18mm;flex:0 0 18mm;display:grid;grid-template-columns:34mm 1fr 13mm;align-items:center}}.logo{{width:32mm;height:17.5mm;object-fit:contain}}.book-id{{text-align:center;color:#064d37;font-family:Georgia,"Times New Roman",serif;font-size:6.2pt;font-weight:700;letter-spacing:.16em}}.page-no{{justify-self:end;width:12mm;background:#064d37;color:#fff;border-bottom:1mm solid #b98a2f;border-radius:0 0 3mm 3mm;text-align:center;font-size:12pt;font-weight:700;padding:2.2mm 1mm 3mm}}.spacer{{flex:1;display:flex;align-items:center;justify-content:center;color:#ddd;font-size:8pt}}.edge-ornament{{height:10mm;flex:0 0 10mm;margin-left:-10mm;margin-right:-10mm;position:relative;overflow:hidden;background:linear-gradient(90deg,#f5f5f2 0%,#d9dfda 17%,#8da398 50%,#d9dfda 83%,#f5f5f2 100%);border-top:.28mm solid #6b7d73}}.edge-ornament:before{{content:'';position:absolute;inset:0;opacity:.36;background:repeating-linear-gradient(135deg,transparent 0 6mm,rgba(0,0,0,.22) 6mm 6.35mm,transparent 6.35mm 12mm),repeating-linear-gradient(45deg,transparent 0 6mm,rgba(255,255,255,.8) 6mm 6.25mm,transparent 6.25mm 12mm)}}.edge-ornament:after{{content:'';position:absolute;left:0;right:0;bottom:0;height:.7mm;background:linear-gradient(90deg,#b9b9b9,#5f6b64,#b9b9b9)}}.edge-center{{position:absolute;left:50%;top:1.6mm;transform:translateX(-50%) rotate(45deg);width:5.4mm;height:5.4mm;border:.34mm solid rgba(50,60,54,.75);background:rgba(255,255,255,.45);z-index:2}}.edge-center:after{{content:'';position:absolute;inset:1.1mm;border:.26mm solid rgba(255,255,255,.85)}}.slogan{{position:absolute;top:50%;transform:translateY(-50%);z-index:3;font-family:"{FONT_FAMILY}",serif;font-size:10.3pt;line-height:1;color:#173a2d;direction:rtl;font-feature-settings:'mark' 1,'mkmk' 1;text-shadow:0 .1mm .1mm rgba(255,255,255,.65)}}.slogan.left{{left:8mm}}.slogan.right{{right:8mm}}
@media print{{.edge-ornament{{background:linear-gradient(90deg,#f3f3f3 0%,#d6d6d6 17%,#8f8f8f 50%,#d6d6d6 83%,#f3f3f3 100%);border-top-color:#777}}.slogan{{color:#222;text-shadow:none}}.edge-center{{border-color:#555}}}}
</style></head><body><main class="page"><header class="header"><img class="logo" src="{LOGO.resolve().as_uri()}"><div class="book-id">QURBATA · JILID 1</div><div class="page-no">01</div></header><div class="spacer">AREA MATERI UTAMA — prototype identitas saja</div><footer class="edge-ornament"><span class="slogan left">قُرْآنٌ · لُغَةٌ · أَدَبٌ</span><span class="edge-center"></span><span class="slogan right">تَعَلَّمْ · اِعْمَلْ · عَلِّمْ</span></footer></main></body></html>'''
def free_path(base):
 if not base.exists():return base
 for n in range(1,100):
  p=base.with_name(base.stem+f'-R{n}'+base.suffix)
  if not p.exists():return p
 raise RuntimeError('NO_FREE_OUTPUT_FILENAME')
async def render():
 OUT.mkdir(parents=True,exist_ok=True);font,src=kfgloader.discover_font(None,None,OUT);h=OUT/'QURBATA-HEADER-FOOTER-PROTOTYPE-V7-GRAYSCALE-SAFE.html';h.write_text(html_doc(font.resolve().as_uri()),encoding='utf-8');pdf=free_path(OUT/'QURBATA-HEADER-FOOTER-PROTOTYPE-V7-GRAYSCALE-SAFE.pdf');png=free_path(OUT/'QURBATA-HEADER-FOOTER-PROTOTYPE-V7-GRAYSCALE-SAFE.png')
 async with async_playwright() as pw:
  b=await pw.chromium.launch();p=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);await p.goto(h.resolve().as_uri(),wait_until='networkidle');await p.evaluate('document.fonts.ready')
  if not await p.evaluate(f"()=>document.fonts.check('10.3pt \\\"{FONT_FAMILY}\\\"','قُرْآنٌ تَعَلَّمْ')"):raise RuntimeError('QURBATA_FOOTER_KFGQPC_BINDING_FAIL')
  await p.screenshot(path=str(png),full_page=True);await p.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await b.close()
 print('QURBATA_HEADER_FOOTER_PROTOTYPE_V7=PASS');print('PRODUCTION_PAGES_MODIFIED=NO');print('FOOTER_ORNAMENT=FLUSH_TO_BOTTOM_PAGE_EDGE');print('SLOGANS=INSIDE_ORNAMENT');print('FOOTER_ARABIC_FONT=KFGQPC_UTHMAN_TAHA');print('COLOR_MODEL=TONAL_GRADIENT_GRAYSCALE_SAFE');print(f'FONT_SOURCE={src}');print(f'PDF={pdf.relative_to(ROOT)}')
if __name__=='__main__':asyncio.run(render())
