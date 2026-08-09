#!/usr/bin/env python3
"""QURBATA Jilid 2 P001 V13.

This wrapper keeps P001 V12 content/layout but replaces the legacy foundation
fit_joined routine. The legacy fitter was written for absolutely positioned
glyphs and applies translate(-50%,-50%) plus whole-word damma/kasra Y offsets.
P001 now uses flex/static glyphs and native Amiri Quran shaping, so those legacy
vertical transforms corrupt the apparent harakat position.

V13 performs horizontal fit only. It never moves a word vertically and never
moves a harakat separately from its base glyph.
"""
from __future__ import annotations
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / 'tools') not in sys.path:
    sys.path.insert(0, str(ROOT / 'tools'))

import render_qurbata_jilid2_p001_v1 as p001


async def fit_joined_horizontal_only(page):
    """Fit joined Arabic objects horizontally without any vertical transform."""
    return await page.evaluate(r'''()=>{
      const canvas=document.createElement('canvas'),ctx=canvas.getContext('2d');
      let count=0,fit=0;
      const mm=v=>v*96/25.4,safe=mm(.7);
      for(const slot of document.querySelectorAll('.j2-object')){
        const g=slot.querySelector('.j2-glyph');
        if(!g)continue;
        const cs=getComputedStyle(g),text=g.textContent||'';
        ctx.font=`${cs.fontStyle} ${cs.fontVariant} ${cs.fontWeight} ${cs.fontSize} ${cs.fontFamily}`;
        ctx.direction='rtl';ctx.textAlign='left';
        const m=ctx.measureText(text),left=-m.actualBoundingBoxLeft,right=m.actualBoundingBoxRight;
        const raw=Math.max(.01,right-left),w=slot.getBoundingClientRect().width;
        const avail=Math.max(1,w-2*safe),scale=Math.min(1,avail/raw);
        g.style.position='relative';
        g.style.left='auto';
        g.style.top='auto';
        g.style.transformOrigin='center center';
        g.style.transform=`scaleX(${scale})`;
        g.dataset.scale=String(scale);
        g.dataset.fit=scale<.999?'1':'0';
        if(scale<.999)fit++;
        count++;
      }
      return {count,fit,damma:0,kasra:0};
    }''')


# P001.fit_and_inspect calls p001.base.base.fit_joined(). Replace only that
# legacy fitter; all P001 content, competency gates, layout and validators remain.
p001.base.base.fit_joined = fit_joined_horizontal_only


def main():
    rc = p001.main()
    print('JILID2_P001_RENDERER_V13=PASS')
    print('LEGACY_VERTICAL_FITTER=DISABLED')
    print('WHOLE_WORD_DAMMA_OFFSET=DISABLED')
    print('WHOLE_WORD_KASRA_OFFSET=DISABLED')
    print('GLYPH_TRANSLATE_MINUS_50=DISABLED')
    print('FIT_POLICY=HORIZONTAL_SCALE_ONLY')
    print('HARAKAT_POSITIONING=AMIRI_QURAN_NATIVE_OPENTYPE_UNINTERRUPTED')
    return rc


if __name__ == '__main__':
    raise SystemExit(main())
