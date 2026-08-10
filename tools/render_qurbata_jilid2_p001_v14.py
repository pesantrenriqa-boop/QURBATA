#!/usr/bin/env python3
"""QURBATA Jilid 2 P001 V14 font/shaping diagnostic renderer.

Runs the V13 horizontal-only fit policy, then records the *actual* platform font
used by Chromium for the Arabic glyph node through the Chrome DevTools Protocol.
This distinguishes declared CSS family from the font that really renders.
"""
from __future__ import annotations
import argparse, asyncio, json, sys
from pathlib import Path
from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / 'tools') not in sys.path:
    sys.path.insert(0, str(ROOT / 'tools'))

import render_qurbata_jilid2_p001_v1 as p001
import render_qurbata_jilid2_p001_v13 as v13

# Keep V13 fit policy.
p001.base.base.fit_joined = v13.fit_joined_horizontal_only

async def render_with_font_diagnostic(h: Path, out: Path, debug: bool):
    report = out / 'LAYOUT-OVERFLOW-REPORT-J2-P001-V14.json'
    font_report = out / 'FONT-DIAGNOSTIC-J2-P001-V14.json'
    png = out / 'png'; png.mkdir(parents=True, exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width':1120,'height':1584}, device_scale_factor=2)
        await page.goto(h.resolve().as_uri(), wait_until='networkidle')
        await page.evaluate('document.fonts.ready')

        # Actual platform font via Chrome DevTools Protocol.
        cdp = await page.context.new_cdp_session(page)
        await cdp.send('DOM.enable')
        await cdp.send('CSS.enable')
        doc = await cdp.send('DOM.getDocument', {'depth': -1, 'pierce': True})
        node = await cdp.send('DOM.querySelector', {'nodeId': doc['root']['nodeId'], 'selector': '.j2-glyph'})
        platform = await cdp.send('CSS.getPlatformFontsForNode', {'nodeId': node['nodeId']})

        declared = await page.locator('.j2-glyph').first.evaluate("el=>({fontFamily:getComputedStyle(el).fontFamily,fontSize:getComputedStyle(el).fontSize,fontFeatureSettings:getComputedStyle(el).fontFeatureSettings,text:el.textContent})")
        checks = await page.evaluate("()=>({amiriQuran36:document.fonts.check(\"36pt 'Amiri Quran'\",'بَتِثُ'),amiri36:document.fonts.check(\"36pt 'Amiri'\",'بَتِثُ')})")
        fd = {'declared': declared, 'fontChecks': checks, 'platformFonts': platform.get('fonts', [])}
        font_report.write_text(json.dumps(fd, ensure_ascii=False, indent=2), encoding='utf-8')

        count = await page.locator('.j2-object').count()
        if count != 26:
            raise RuntimeError(f'P001_OBJECT_COUNT_INVALID actual={count} expected=26')
        metrics, issues = await p001.fit_and_inspect(page)
        report.write_text(json.dumps(issues, ensure_ascii=False, indent=2), encoding='utf-8')
        if issues:
            kinds={}
            for x in issues:kinds[x['kind']]=kinds.get(x['kind'],0)+1
            raise RuntimeError('P001_LAYOUT_ISSUES='+str(len(issues))+' TYPES='+','.join(f'{k}:{v}' for k,v in sorted(kinds.items()))+f' REPORT={report}')
        await page.screenshot(path=str(png/'page-001.png'), full_page=True)
        pdf = out/'QURBATA-JILID-2-P001-CANDIDATE-V14.pdf'
        await page.pdf(path=str(pdf), format='A5', print_background=True, margin={'top':'0','right':'0','bottom':'0','left':'0'})
        await browser.close()
    return metrics, report, font_report, pdf, fd

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',default='dist/jilid-2-p001-candidate-v20'); ap.add_argument('--debug',action='store_true'); a=ap.parse_args()
    out=Path(a.output_dir); out=out if out.is_absolute() else ROOT/out; out.mkdir(parents=True, exist_ok=True)
    hdir=out/'html'; hdir.mkdir(parents=True, exist_ok=True); h=hdir/'page-001.html'; h.write_text(p001.build_page_html(a.debug), encoding='utf-8')
    metrics,report,font_report,pdf,fd=asyncio.run(render_with_font_diagnostic(h,out,a.debug))
    fonts=fd.get('platformFonts',[])
    names='|'.join(sorted({str(x.get('familyName','')) for x in fonts if x.get('familyName')})) or 'NONE'
    print('JILID2_P001_RENDERER_V14=PASS')
    print('FIT_POLICY=HORIZONTAL_SCALE_ONLY')
    print('LEGACY_VERTICAL_FITTER=DISABLED')
    print('HARAKAT_POSITIONING=NATIVE_UNINTERRUPTED_SHAPING')
    print('DECLARED_FONT_FAMILY='+str(fd['declared'].get('fontFamily','')))
    print('PLATFORM_FONT_FAMILIES='+names)
    print('FONT_CHECK_AMIRI_QURAN='+('PASS' if fd['fontChecks'].get('amiriQuran36') else 'FAIL'))
    print('FONT_CHECK_AMIRI='+('PASS' if fd['fontChecks'].get('amiri36') else 'FAIL'))
    print('LAYOUT_OVERFLOW=0')
    print(f'FONT_REPORT={font_report.relative_to(ROOT)}')
    print(f'OVERFLOW_REPORT={report.relative_to(ROOT)}')
    print(f'PDF={pdf.relative_to(ROOT)}')
    return 0

if __name__=='__main__': raise SystemExit(main())
