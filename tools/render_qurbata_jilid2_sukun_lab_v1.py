#!/usr/bin/env python3
"""Isolated sukun glyph lab for QURBATA Jilid 2.
Does not modify P024. Generates a one-page comparison PDF/PNG using native font shaping only.
"""
from __future__ import annotations
import argparse, asyncio
from pathlib import Path
from playwright.async_api import async_playwright

HTML='''<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><style>
@page{size:A5;margin:0}*{box-sizing:border-box}body{margin:0;background:white;color:#111;font-family:Arial,sans-serif}
.page{width:148mm;height:210mm;padding:12mm;direction:ltr}
h1{font:700 14pt Arial;text-align:center;margin:0 0 8mm}.row{border-bottom:1px solid #ddd;padding:5mm 0;display:grid;grid-template-columns:35mm 1fr;align-items:center}
.label{font:9pt Arial;direction:ltr}.arab{direction:rtl;text-align:center;font-size:48pt;line-height:1.45;font-feature-settings:'mark' 1,'mkmk' 1;text-rendering:optimizeLegibility}
.kfg{font-family:"QURBATA KFGQPC Uthman Taha Naskh","KFGQPC Uthman Taha Naskh",serif}.amq{font-family:"Amiri Quran","Amiri",serif}.ami{font-family:"Amiri",serif}
.note{font:8pt Arial;direction:ltr;margin-top:5mm}
</style></head><body><div class="page"><h1>SUKUN LAB — native shaping only</h1>
<div class="row"><div class="label">A · KFGQPC + U+0652</div><div class="arab kfg">دِيْنُ &nbsp; دِيْ &nbsp; بَيْتُ</div></div>
<div class="row"><div class="label">B · KFGQPC + U+06E1</div><div class="arab kfg">دِيۡنُ &nbsp; دِيۡ &nbsp; بَيۡتُ</div></div>
<div class="row"><div class="label">C · Amiri Quran + U+06E1</div><div class="arab amq">دِيۡنُ &nbsp; دِيۡ &nbsp; بَيۡتُ</div></div>
<div class="row"><div class="label">D · Amiri + U+06E1</div><div class="arab ami">دِيۡنُ &nbsp; دِيۡ &nbsp; بَيۡتُ</div></div>
<div class="note">No SVG, no overlay, no clipping, no manual positioning. Choose the row whose sukun shape is correct; P024 remains untouched.</div>
</div></body></html>'''

async def run(out:Path):
    out.mkdir(parents=True,exist_ok=True); h=out/'sukun-lab.html'; h.write_text(HTML,encoding='utf-8')
    async with async_playwright() as pw:
        b=await pw.chromium.launch(); p=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2)
        await p.goto(h.resolve().as_uri(),wait_until='networkidle'); await p.evaluate('document.fonts.ready')
        await p.screenshot(path=str(out/'SUKUN-LAB-V1.png'),full_page=True)
        await p.pdf(path=str(out/'SUKUN-LAB-V1.pdf'),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'})
        fam=await p.evaluate("()=>[...document.querySelectorAll('.arab')].map(e=>getComputedStyle(e).fontFamily)")
        await b.close()
    print('SUKUN_LAB_V1=PASS'); print('ROWS=A_KFG_U0652|B_KFG_U06E1|C_AMIRI_QURAN_U06E1|D_AMIRI_U06E1'); print('NATIVE_SHAPING_ONLY=YES'); print('P024_MODIFIED=NO'); print('FONT_STACKS='+repr(fam))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',default='dist/jilid-2-sukun-lab-v1'); a=ap.parse_args(); asyncio.run(run(Path(a.output_dir)))
if __name__=='__main__': main()
