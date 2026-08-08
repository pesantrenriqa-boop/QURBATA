#!/usr/bin/env python3
"""QURBATA Jilid 2 foundation renderer v3.

Adds the explicit new-material presentation block before practice while preserving
Jilid 1/V22-derived grid philosophy, Amiri Quran, 36pt practice text, footer, and
post-fit collision gates.

Page order on new-material pages:
TITLE -> PRESENTATION -> PRACTICE -> FOOTER.
Reinforcement/evaluation pages do not repeat an old presentation.
"""
from __future__ import annotations

import csv
import html
from pathlib import Path

import render_qurbata_jilid2_foundation_v1 as base

ROOT = Path(__file__).resolve().parents[1]
PRESENTATION_REG = ROOT / 'content/qwo/registry/JILID-2-NEW-MATERIAL-PRESENTATION-V1.csv'


def load_presentations() -> dict[int, dict]:
    with PRESENTATION_REG.open(encoding='utf-8-sig', newline='') as f:
        rows = list(csv.DictReader(f))
    return {int(r['Page']): r for r in rows}


PRESENTATIONS = load_presentations()

# Font policy: Amiri Quran first. Geometry remains derived from the stable v1 layout.
base.FONT_FAMILY = 'Amiri Quran'
base.CSS = base.CSS.replace(
    "font-family:'Amiri','Noto Naskh Arabic',serif",
    "font-family:'Amiri Quran','Amiri','Noto Naskh Arabic',serif",
)

# Dynamic page geometry: reserve a compact teaching band only when material is genuinely new.
base.CSS += r'''
.title-row{height:9mm;flex:0 0 9mm}
.page.with-presentation .j2-grid{height:138mm;flex:0 0 138mm;row-gap:1.25mm;padding:.7mm 0 1mm}
.page.without-presentation .j2-grid{height:151mm;flex:0 0 151mm}
.presentation{height:13mm;flex:0 0 13mm;display:flex;align-items:center;justify-content:center;gap:3mm;margin:0 3mm .4mm;padding:.7mm 2.5mm;border-top:.18mm solid rgba(185,138,47,.42);border-bottom:.18mm solid rgba(185,138,47,.42);background:linear-gradient(90deg,rgba(247,248,245,.35),rgba(255,255,255,.9),rgba(247,248,245,.35));overflow:visible}
.presentation-copy{display:flex;flex-direction:column;align-items:flex-start;justify-content:center;min-width:28mm;max-width:45mm}
.presentation-kicker{font-size:5.2pt;line-height:1;color:#777;letter-spacing:.08em;text-transform:uppercase}
.presentation-title{margin-top:.4mm;font-family:Georgia,'Times New Roman',serif;font-size:7.3pt;line-height:1.1;font-weight:700;color:#064d37}
.presentation-object{flex:1;min-width:0;text-align:center;direction:rtl;unicode-bidi:isolate;font-family:'Amiri Quran','Amiri','Noto Naskh Arabic',serif;font-size:24pt;line-height:1.05;color:#000;white-space:nowrap;overflow:visible}
html[data-layout-debug="true"] .presentation{outline:.15mm dashed rgba(6,77,55,.18)}
'''


def esc(value: str) -> str:
    return html.escape(str(value or ''))


def page_html(page: int, rows: list[dict], meta: dict, debug: bool) -> str:
    pres = PRESENTATIONS.get(page, {})
    required = str(pres.get('PresentationRequired', '')).strip().upper() == 'YES'
    page_class = 'page with-presentation' if required else 'page without-presentation'
    objs = ''.join(
        f'<div class="j2-object" data-slot="{int(r["Slot"])}"><span class="j2-glyph">{esc(r["ArabicObject"])}</span></div>'
        for r in rows
    )
    debug_attr = ' data-layout-debug="true"' if debug else ''
    presentation_html = ''
    if required:
        presentation_html = f'''
  <section class="presentation" data-presentation="new-material">
    <div class="presentation-copy">
      <span class="presentation-kicker">MATERI BARU</span>
      <strong class="presentation-title">{esc(pres.get('PresentationTitle',''))}</strong>
    </div>
    <div class="presentation-object">{esc(pres.get('PresentationObject',''))}</div>
  </section>'''
    return f'''<!doctype html><html{debug_attr}><head><meta charset="utf-8"><style>{base.CSS}</style></head><body>
<main class="{page_class}">
  <header class="header">
    <div class="brand">QURBATA <span>• JILID 2</span></div>
    <div class="page-no">{page}</div>
  </header>
  <section class="title-row"><strong>{esc(meta['Focus'])}</strong></section>{presentation_html}
  <section class="j2-grid">{objs}</section>
  <section class="targets">
    <div class="target-item"><span>KOMPETENSI</span><strong>{esc(pres.get('Competency') or meta['Focus'])}</strong></div>
    <div class="target-item"><span>SUBKOMPETENSI</span><strong>{esc(pres.get('SubCompetency',''))}</strong></div>
    <div class="target-item"><span>TANGGA</span><strong>{esc(pres.get('Stair',''))}</strong></div>
    <div class="target-item"><span>NIDOM</span><strong>Registry Jilid 2 belum diikat</strong></div>
  </section>
  <footer class="footer"><span>QURBATA • JILID 2</span><span>Guru: __________  Nilai: ____  Tanggal: ________</span></footer>
</main></body></html>'''


base.page_html = page_html
_original_inspect = base.inspect


async def inspect_with_presentation(page, n):
    issues = await _original_inspect(page, n)
    extra = await page.evaluate('''(n)=>{const out=[],t=2;const p=document.querySelector('.presentation');if(!p)return out;const r=p.getBoundingClientRect();if(p.scrollWidth>p.clientWidth+t||p.scrollHeight>p.clientHeight+t)out.push({kind:'PRESENTATION_SCROLL_OVERFLOW',page:n,className:p.className,scrollWidth:p.scrollWidth,clientWidth:p.clientWidth,scrollHeight:p.scrollHeight,clientHeight:p.clientHeight});const obj=p.querySelector('.presentation-object');if(obj){const o=obj.getBoundingClientRect();if(o.left<r.left-t||o.right>r.right+t||o.top<r.top-t||o.bottom>r.bottom+t)out.push({kind:'PRESENTATION_OBJECT_OUTSIDE_BAND',page:n,className:obj.className,presentationLeft:r.left,presentationRight:r.right,objectLeft:o.left,objectRight:o.right,objectTop:o.top,objectBottom:o.bottom});}return out}''', n)
    issues.extend(extra)
    return issues


base.inspect = inspect_with_presentation


def main() -> int:
    rc = base.main()
    required = sum(1 for p in range(1, 21) if str(PRESENTATIONS[p]['PresentationRequired']).strip().upper() == 'YES')
    suppressed = 20 - required
    print('ARABIC_FONT_PRIMARY=Amiri Quran')
    print('GRID_SCROLL_VALIDATION=POST_FIT_GLYPH_BOUNDS')
    print('NEW_MATERIAL_PRESENTATION=INTEGRATED')
    print(f'P001_P020_PRESENTATION_REQUIRED={required}')
    print(f'P001_P020_PRESENTATION_SUPPRESSED={suppressed}')
    print('PAGE_ORDER=TITLE|PRESENTATION_IF_NEW|PRACTICE|FOOTER')
    print('PRACTICE_OBJECTS_PER_PAGE=24')
    print('PRACTICE_FONT_SIZE=36pt')
    print('JILID2_FOUNDATION_RENDERER_V3=PASS' if rc == 0 else 'JILID2_FOUNDATION_RENDERER_V3=FAIL')
    return rc


if __name__ == '__main__':
    raise SystemExit(main())
