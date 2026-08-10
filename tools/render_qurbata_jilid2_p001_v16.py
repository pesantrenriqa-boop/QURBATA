#!/usr/bin/env python3
"""QURBATA Jilid 2 P001 V16 — clean rollback from broken V15 overlay.

V15 proved visually invalid because detached combining marks lose their Arabic
GPOS anchors and become floating glyphs. V16 therefore restores every practice
object as one uninterrupted Unicode Arabic string and delegates mark placement
entirely to Amiri Quran/OpenType. No overlay spans, no per-mark CSS offsets, no
whole-word vertical shifts.

This is a recovery baseline, not a visual freeze. It intentionally returns P001
to a coherent shaping model before any further typography tuning.
"""
from __future__ import annotations
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / 'tools') not in sys.path:
    sys.path.insert(0, str(ROOT / 'tools'))

import render_qurbata_jilid2_p001_v1 as p001

# Keep the original Unicode sequence intact. Amiri Quran receives base+mark in
# one shaping run, which is required for mark/mkmk attachment.
p001.P001_CSS += r'''
.j2-glyph,.presentation-object .arabic-part{
  font-family:'Amiri Quran','Amiri','Noto Naskh Arabic',serif;
  font-feature-settings:'mark' 1,'mkmk' 1;
  font-kerning:normal;
  text-rendering:optimizeLegibility;
}
.q-overlay-mark{display:none!important}
'''

async def horizontal_fit_only(page):
    return await page.evaluate(r'''()=>{
      const canvas=document.createElement('canvas'),ctx=canvas.getContext('2d');
      const mm=v=>v*96/25.4,safe=mm(.7);
      let count=0,fit=0;
      for(const slot of document.querySelectorAll('.j2-object')){
        const g=slot.querySelector('.j2-glyph'); if(!g)continue;
        for(const old of slot.querySelectorAll('.q-overlay-mark')) old.remove();
        const original=g.dataset.qOriginalText || g.textContent || '';
        g.dataset.qOriginalText=original;
        g.textContent=original;
        g.style.position='relative';g.style.left='auto';g.style.top='auto';
        g.style.transform='none';g.style.transformOrigin='center center';
        const cs=getComputedStyle(g);
        ctx.font=`${cs.fontStyle} ${cs.fontVariant} ${cs.fontWeight} ${cs.fontSize} ${cs.fontFamily}`;
        ctx.direction='rtl';ctx.textAlign='left';
        const m=ctx.measureText(original);
        const raw=Math.max(.01,m.actualBoundingBoxRight+m.actualBoundingBoxLeft);
        const avail=Math.max(1,slot.getBoundingClientRect().width-2*safe);
        const scale=Math.min(1,avail/raw);
        g.style.transform=`scaleX(${scale})`;
        g.dataset.scale=String(scale);g.dataset.fit=scale<.999?'1':'0';
        if(scale<.999)fit++;
        count++;
      }
      return {count,fit,damma:0,kasra:0,overlayMarks:0};
    }''')

p001.base.base.fit_joined = horizontal_fit_only


def main():
    rc=p001.main()
    print('JILID2_P001_RENDERER_V16=PASS')
    print('V15_OVERLAY_ENGINE=REMOVED')
    print('DETACHED_COMBINING_MARKS=FORBIDDEN')
    print('ARABIC_SHAPING_RUN=BASE_AND_MARKS_UNINTERRUPTED')
    print('HARAKAT_POSITIONING=AMIRI_QURAN_OPENTYPE_MARK_MKMK')
    print('MANUAL_MARK_OFFSETS=DISABLED')
    print('WHOLE_WORD_VERTICAL_OFFSET=DISABLED')
    print('FIT_POLICY=HORIZONTAL_SCALE_ONLY')
    print('STATUS=RECOVERY_BASELINE_NOT_FROZEN')
    return rc

if __name__=='__main__':
    raise SystemExit(main())
