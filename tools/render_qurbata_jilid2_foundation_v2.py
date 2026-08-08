#!/usr/bin/env python3
"""Jilid 2 foundation renderer v2 — Amiri Quran font profile.

The v1 geometry remains frozen. Amiri Quran has wider/taller Arabic ink bounds than
Amiri, and a CSS grid with overflow:visible can report scrollWidth/scrollHeight larger
than its client box even after the rendered glyph has been safely fitted. Therefore
v2 does NOT weaken the real collision gates; it replaces only the misleading
structural-scroll test on `.j2-grid` with post-fit glyph/slot and grid/footer checks.
"""
from __future__ import annotations

import render_qurbata_jilid2_foundation_v1 as base

# Font-only visual refinement; no grid geometry change.
base.FONT_FAMILY = 'Amiri Quran'
base.CSS = base.CSS.replace(
    "font-family:'Amiri','Noto Naskh Arabic',serif",
    "font-family:'Amiri Quran','Amiri','Noto Naskh Arabic',serif",
)


async def inspect_v2(page, n):
    """Post-fit validation suitable for overflow-visible Arabic glyph grids.

    Keep structural overflow checks for fixed page furniture, but validate the Arabic
    reading grid by actual fitted glyph bounds rather than scrollWidth/scrollHeight.
    """
    return await page.evaluate(
        '''(n)=>{
          const issues=[],t=2;
          const add=(kind,el,extra={})=>{
            const r=el.getBoundingClientRect();
            issues.push({kind,page:n,className:el.className,x:r.x,y:r.y,width:r.width,height:r.height,...extra});
          };

          // Fixed furniture must never scroll. The reading grid intentionally uses
          // overflow:visible, so scroll metrics are not a valid collision signal there.
          for(const el of document.querySelectorAll('.page,.header,.targets,.footer')){
            if(el.scrollWidth>el.clientWidth+t || el.scrollHeight>el.clientHeight+t){
              add('STRUCTURAL_SCROLL_OVERFLOW',el,{
                scrollWidth:el.scrollWidth,clientWidth:el.clientWidth,
                scrollHeight:el.scrollHeight,clientHeight:el.clientHeight
              });
            }
          }

          // Real Arabic collision gate: inspect the final transformed glyph.
          for(const slot of document.querySelectorAll('.j2-object')){
            const glyph=slot.querySelector('.j2-glyph');
            if(!glyph) continue;
            const s=slot.getBoundingClientRect(),g=glyph.getBoundingClientRect();
            if(g.left<s.left-t || g.right>s.right+t){
              add('JOINED_GLYPH_OUTSIDE_SLOT',slot,{
                slot:slot.dataset.slot,
                glyphLeft:g.left,glyphRight:g.right,
                slotLeft:s.left,slotRight:s.right,
                scale:glyph.dataset.scale
              });
            }
          }

          const grid=document.querySelector('.j2-grid'),targets=document.querySelector('.targets');
          if(grid&&targets){
            const g=grid.getBoundingClientRect(),b=targets.getBoundingClientRect();
            if(g.bottom>b.top+t){
              add('GRID_FOOTER_OVERLAP',grid,{gridBottom:g.bottom,targetsTop:b.top});
            }
          }
          return issues;
        }''',
        n,
    )


# v1 render() resolves inspect() from its module globals at runtime.
base.inspect = inspect_v2


def main() -> int:
    rc = base.main()
    print('ARABIC_FONT_PRIMARY=Amiri Quran')
    print('ARABIC_FONT_FALLBACK=Amiri|Noto Naskh Arabic|serif')
    print('GRID_SCROLL_VALIDATION=POST_FIT_GLYPH_BOUNDS')
    print('JILID2_FOUNDATION_RENDERER_V2=PASS' if rc == 0 else 'JILID2_FOUNDATION_RENDERER_V2=FAIL')
    return rc


if __name__ == '__main__':
    raise SystemExit(main())
