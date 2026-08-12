#!/usr/bin/env python3
"""QURBATA header/footer prototype v6 — clean header, bottom-edge footer ornament, review only."""
from pathlib import Path
import asyncio,sys
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path:sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v19_kfgqpc as kfgloader
OUT=ROOT/'dist/qurbata-brand-prototypes/header-footer-v6';LOGO=ROOT/'books/shared/assets/qurbata-logo.svg';FONT_FAMILY='QURBATA KFGQPC Uthman Taha'
def html_doc(font_uri):
 return f'''<!doctype html><html><head><meta charset="utf-8"><style>
@page{{size:A5;margin:0}}*{{box-sizing:border-box}}@font-face{{font-family:"{FONT_FAMILY}";src:url("{font_uri}") format("truetype");font-display:block}}html,body{{margin:0;background:#fff;font-family:Arial,sans-serif}}.page{{width:148mm;height:210mm;padding:7mm 10mm 0;display:flex;flex-direction:column;position:relative;overflow:hidden}}.header{{height:18mm;flex:0 0 18mm;display:grid;grid-template-columns:34mm 1fr 13mm;align-items:center}}.logo{{width:32mm;height:17.5mm;object-fit:contain}}.book-id{{text-align:center;color:#064d37;font-family:Georgia,"Times New Roman",serif;font-size:6.2pt;font-weight:700;letter-spacing:.16em}}.page-no{{justify-self:end;width:12mm;background:#064d37;color:#fff;border-bottom:1mm solid #b98a2f;border-radius:0 0 3mm 3mm;text-align:center;font-size:12pt;font-weight:700;padding:2.2mm 1mm 3mm}}.spacer{{flex:1;display:flex;align-items:center;justify-content:center;color:#ddd;font-size:8pt}}.footer-text{{height:10mm;flex:0 0 10mm;display:flex;justify-content:space-between;align-items:center;color:#064d37;padding-bottom:1mm}}.ar{{font-family:"{FONT_FAMILY}",serif;font-size:11pt;line-height:1.1;direction:rtl;font-feature-settings:'mark' 1,'mkmk' 1}}.edge-ornament{{height:7mm;flex:0 0 7mm;margin-left:-10mm;margin-right:-10mm;position:relative;background:#064d37;overflow:hidden}}.edge-ornament:before{{content:'';position:absolute;left:0;right:0;top:0;height:.55mm;background:#b98a2f}}.edge-ornament:after{{content:'';position:absolute;left:0;right:0;top:1.3mm;height:4.8mm;opacity:.34;background:repeating-linear-gradient(135deg,transparent 0 5mm,#b98a2f 5mm 5.45mm,transparent 5.45mm 10mm),repeating-linear-gradient(45deg,transparent 0 5mm,rgba(255,255,255,.65) 5mm 5.3mm,transparent 5.3mm 10mm)}}.edge-center{{position:absolute;left:50%;top:.75mm;transform:translateX(-50%) rotate(45deg);width:5.2mm;height:5.2mm;border:.45mm solid #b98a2f;background:#064d37;z-index:2}}.edge-center:after{{content:'';position:absolute;inset:1.05mm;border:.3mm solid rgba(255,255,255,.8)}}
</style></head><body><main class="page"><header class="header"><img class="logo" src="{LOGO.resolve().as_uri()}"><div class="book-id">QURBATA · JILID 1</div><div class="page-no">01</div></header><div class="spacer">AREA MATERI UTAMA — prototype identitas saja</div><div class="footer-text"><span class="ar">قُرْآنٌ · لُغَةٌ · أَدَبٌ</span><span class="ar">تَعَلَّمْ · اِعْمَلْ · عَلِّمْ</span></div><footer class="edge-ornament"><span class="edge-center"></span></footer></main></body></html>'''
def free_path(base):
 if not base.exists():return base
 for n in range(1,100):
  p=base.with_name(base.stem+f'-R{n}'+base.suffix)
  if not p.exists():return p
 raise RuntimeError('NO_FREE_OUTPUT_FILENAME')
async def render():
 OUT.mkdir(parents=True,exist_ok=True);font,src=kfgloader.discover_font(None,None,OUT);h=OUT/'QURBATA-HEADER-FOOTER-PROTOTYPE-V6-EDGE-ORNAMENT.html';h.write_text(html_doc(font.resolve().as_uri()),encoding='utf-8');pdf=free_path(OUT/'QURBATA-HEADER-FOOTER-PROTOTYPE-V6-EDGE-ORNAMENT.pdf');png=free_path(OUT/'QURBATA-HEADER-FOOTER-PROTOTYPE-V6-EDGE-ORNAMENT.png')
 async with async_playwright() as pw:
  b=await pw.chromium.launch();p=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);await p.goto(h.resolve().as_uri(),wait_until='networkidle');await p.evaluate('document.fonts.ready')
  if not await p.evaluate(f"()=>document.fonts.check('11pt \\\"{FONT_FAMILY}\\\"','قُرْآنٌ تَعَلَّمْ')"):raise RuntimeError('QURBATA_FOOTER_KFGQPC_BINDING_FAIL')
  await p.screenshot(path=str(png),full_page=True);await p.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await b.close()
 print('QURBATA_HEADER_FOOTER_PROTOTYPE_V6=PASS');print('PRODUCTION_PAGES_MODIFIED=NO');print('HEADER_LINES=NONE');print('FOOTER_ORNAMENT=FLUSH_TO_BOTTOM_PAGE_EDGE');print('FOOTER_ORNAMENT_STYLE=THIN_ISLAMIC_GEOMETRIC_EDGE_BAND');print('FOOTER_ARABIC_FONT=KFGQPC_UTHMAN_TAHA');print(f'FONT_SOURCE={src}');print(f'PDF={pdf.relative_to(ROOT)}')
if __name__=='__main__':asyncio.run(render())
