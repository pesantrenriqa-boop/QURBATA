#!/usr/bin/env python3
"""Render a standalone QURBATA header/footer ornament prototype.

This does NOT modify P001 or any production page. It implements the approved
QURBATA Ornament System v1 direction as a review artifact only.
"""
from pathlib import Path
import asyncio
from playwright.async_api import async_playwright

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'dist/qurbata-brand-prototypes/header-footer-v1'
LOGO=ROOT/'books/shared/assets/qurbata-logo.svg'

HTML='''<!doctype html><html><head><meta charset="utf-8"><style>
@page{size:A5;margin:0}*{box-sizing:border-box}html,body{margin:0;background:#fff;font-family:Arial,sans-serif}.page{width:148mm;height:210mm;padding:8mm 10mm;display:flex;flex-direction:column;justify-content:space-between;background:#fff}.header-wrap{height:28mm;position:relative}.header-row{height:17mm;display:grid;grid-template-columns:31mm 1fr 13mm;align-items:center}.logo{width:29mm;height:16mm;object-fit:contain}.book-id{text-align:center;color:#064d37;font-family:Georgia,"Times New Roman",serif;font-size:7pt;font-weight:700;letter-spacing:.18em;white-space:nowrap}.page-no{justify-self:end;width:12mm;background:#064d37;color:#fff;border-bottom:1mm solid #b98a2f;border-radius:0 0 3mm 3mm;text-align:center;font-size:12pt;font-weight:700;padding:2.2mm 1mm 3mm}.orn-line{height:7mm;display:flex;align-items:center;gap:2.2mm}.seg{height:.28mm;background:#064d37;flex:1}.seg.short{flex:.34}.gold{height:.45mm;width:6mm;background:#b98a2f}.kufi{width:8mm;height:5mm;position:relative;flex:0 0 8mm}.kufi:before,.kufi:after{content:"";position:absolute;border-color:#064d37}.kufi:before{left:0;top:2mm;width:3mm;height:2.5mm;border-left:.45mm solid #064d37;border-top:.45mm solid #064d37}.kufi:after{right:0;top:.5mm;width:3mm;height:4mm;border-right:.45mm solid #064d37;border-bottom:.45mm solid #064d37}.tauhid{width:1.8mm;height:1.8mm;border-radius:50%;background:#b98a2f;flex:0 0 1.8mm}.spacer{flex:1;display:flex;align-items:center;justify-content:center;color:#ddd;font-size:8pt}.footer-wrap{height:20mm;position:relative;display:flex;flex-direction:column;justify-content:flex-end}.footer-orn{height:7mm;display:flex;align-items:center;gap:2mm}.roof{width:9mm;height:5mm;position:relative;flex:0 0 9mm}.roof:before{content:"";position:absolute;left:1mm;right:1mm;top:1.8mm;height:.45mm;background:#064d37}.roof:after{content:"";position:absolute;left:3.3mm;top:.2mm;width:2.4mm;height:2.4mm;border-left:.45mm solid #b98a2f;border-top:.45mm solid #b98a2f;transform:rotate(45deg)}.footer-text{display:flex;align-items:center;justify-content:space-between;color:#064d37;font-family:Georgia,"Times New Roman",serif;font-size:7.2pt;font-weight:700;letter-spacing:.04em;direction:ltr;padding-top:.5mm}.footer-text .ar{font-family:"Amiri","Noto Naskh Arabic",serif;font-size:10.5pt;letter-spacing:0;direction:rtl}.note{font-size:5.2pt;color:#777;text-align:center;margin-top:1mm}
</style></head><body><main class="page">
<section class="header-wrap"><div class="header-row"><img class="logo" src="LOGO_URI"><div class="book-id">QURBATA · JILID 1</div><div class="page-no">01</div></div><div class="orn-line"><span class="seg"></span><span class="gold"></span><span class="seg short"></span><span class="kufi"></span><span class="tauhid"></span><span class="kufi"></span><span class="seg short"></span><span class="gold"></span><span class="seg"></span></div></section>
<div class="spacer">AREA MATERI UTAMA — prototype tidak mengubah halaman produksi</div>
<section class="footer-wrap"><div class="footer-orn"><span class="seg"></span><span class="gold"></span><span class="kufi"></span><span class="roof"></span><span class="tauhid"></span><span class="roof"></span><span class="kufi"></span><span class="gold"></span><span class="seg"></span></div><div class="footer-text"><span class="ar">قُرْآنٌ · لُغَةٌ · أَدَبٌ</span><span class="ar">تَعَلَّمْ · اِعْمَلْ · عَلِّمْ</span></div><div class="note">QURBATA Ornament Prototype v1 · RIOS secondary/micro geometry · LIGHT density</div></section>
</main></body></html>'''

async def render():
    OUT.mkdir(parents=True,exist_ok=True)
    h=OUT/'QURBATA-HEADER-FOOTER-ORNAMENT-PROTOTYPE-V1.html'
    h.write_text(HTML.replace('LOGO_URI',LOGO.resolve().as_uri()),encoding='utf-8')
    pdf=OUT/'QURBATA-HEADER-FOOTER-ORNAMENT-PROTOTYPE-V1.pdf'
    png=OUT/'QURBATA-HEADER-FOOTER-ORNAMENT-PROTOTYPE-V1.png'
    async with async_playwright() as pw:
        b=await pw.chromium.launch();p=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2)
        await p.goto(h.resolve().as_uri(),wait_until='networkidle')
        await p.screenshot(path=str(png),full_page=True)
        await p.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'})
        await b.close()
    print('QURBATA_ORNAMENT_PROTOTYPE_V1=PASS')
    print('PRODUCTION_PAGES_MODIFIED=NO')
    print('HEADER=LOGO_LARGER|BOOK_ID_SMALL|PAGE_NO_PRESERVED|RIOS_LIGHT_LINE')
    print('FOOTER=RIOS_LIGHT_ORNAMENT|NO_LITERAL_Q_MEDALLION')
    print('FOOTER_LEFT=قُرْآنٌ · لُغَةٌ · أَدَبٌ')
    print('FOOTER_RIGHT=تَعَلَّمْ · اِعْمَلْ · عَلِّمْ')
    print(f'PDF={pdf.relative_to(ROOT)}')
    print(f'PNG={png.relative_to(ROOT)}')

if __name__=='__main__':asyncio.run(render())
