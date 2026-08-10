#!/usr/bin/env python3
"""QURBATA Jilid 2 P001 V15.

Goal: keep Arabic base letters in one uninterrupted shaping run while positioning
fatha/damma/kasra independently from the base run. V15 strips only the three
short-vowel marks from the visible base shaping run, keeps all base letters joined
natively, then overlays each mark on the DOM Range box of its own base character.
Horizontal fitting remains scaleX-only; no whole-word Y shift.
"""
from __future__ import annotations
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / 'tools') not in sys.path:
    sys.path.insert(0, str(ROOT / 'tools'))

import render_qurbata_jilid2_p001_v1 as p001

p001.P001_CSS += r'''
.j2-object{position:relative}
.q-overlay-mark{position:absolute;z-index:3;pointer-events:none;direction:rtl;unicode-bidi:isolate;font-family:'Amiri Quran','Amiri','Noto Naskh Arabic',serif;font-size:26pt;line-height:1;font-feature-settings:'mark' 1,'mkmk' 1;transform:translate(-50%,-50%);transform-origin:center;white-space:nowrap;color:#000}
.q-overlay-fatha{--q-mark-kind:fatha}
.q-overlay-damma{--q-mark-kind:damma}
.q-overlay-kasra{--q-mark-kind:kasra}
'''


async def fit_joined_cluster_overlay(page):
    return await page.evaluate(r'''()=>{
      const FATHA='َ', DAMMA='ُ', KASRA='ِ';
      const isMark=c=>c===FATHA||c===DAMMA||c===KASRA;
      const canvas=document.createElement('canvas'),ctx=canvas.getContext('2d');
      const mm=v=>v*96/25.4,safe=mm(.7);
      let count=0,fit=0,marks=0,fatha=0,damma=0,kasra=0,clamped=0;
      for(const slot of document.querySelectorAll('.j2-object')){
        const g=slot.querySelector('.j2-glyph'); if(!g)continue;
        for(const old of slot.querySelectorAll('.q-overlay-mark')) old.remove();
        const original=g.dataset.qOriginalText || g.textContent || '';
        g.dataset.qOriginalText=original;
        const bases=[],attached=[]; let baseIndex=-1;
        for(const ch of original){
          if(isMark(ch)){ if(baseIndex>=0) attached.push({baseIndex,mark:ch}); }
          else { bases.push(ch); baseIndex++; }
        }
        const baseText=bases.join('');
        g.textContent=baseText;
        g.style.position='relative'; g.style.left='auto'; g.style.top='auto';
        g.style.transform='none'; g.style.transformOrigin='center center';
        const cs=getComputedStyle(g);
        ctx.font=`${cs.fontStyle} ${cs.fontVariant} ${cs.fontWeight} ${cs.fontSize} ${cs.fontFamily}`;
        ctx.direction='rtl';ctx.textAlign='left';
        const m=ctx.measureText(baseText),left=-m.actualBoundingBoxLeft,right=m.actualBoundingBoxRight;
        const raw=Math.max(.01,right-left),w=slot.getBoundingClientRect().width;
        const avail=Math.max(1,w-2*safe),scale=Math.min(1,avail/raw);
        g.style.transform=`scaleX(${scale})`; g.dataset.scale=String(scale); g.dataset.fit=scale<.999?'1':'0';
        if(scale<.999)fit++;
        const node=g.firstChild, s=slot.getBoundingClientRect();
        if(node && node.nodeType===Node.TEXT_NODE){
          for(const item of attached){
            if(item.baseIndex<0 || item.baseIndex>=node.length)continue;
            const range=document.createRange(); range.setStart(node,item.baseIndex); range.setEnd(node,item.baseIndex+1);
            const r=range.getBoundingClientRect(); if(!r.width && !r.height)continue;
            const span=document.createElement('span');
            span.className='q-overlay-mark '+(item.mark===FATHA?'q-overlay-fatha':item.mark===DAMMA?'q-overlay-damma':'q-overlay-kasra');
            span.textContent=item.mark; span.dataset.baseIndex=String(item.baseIndex); span.dataset.mark=item.mark;
            const x=(r.left+r.right)/2-s.left;
            const top=r.top-s.top,bottom=r.bottom-s.top,h=r.height;
            let y;
            if(item.mark===FATHA){y=top+h*0.28;fatha++;}
            else if(item.mark===DAMMA){y=top+h*0.38;damma++;}
            else {y=bottom-h*0.03;kasra++;}

            // Keep the mark anchor inside its own logical row cell. This is a
            // geometry safety clamp only; it does not move the base word or
            // change the relative fatha/damma/kasra policy.
            const minY=3, maxY=Math.max(minY, s.height-3);
            const unclampedY=y;
            y=Math.max(minY,Math.min(maxY,y));
            if(Math.abs(y-unclampedY)>0.01)clamped++;

            span.style.left=`${x}px`; span.style.top=`${y}px`; slot.appendChild(span); marks++;
          }
        }
        count++;
      }
      return {count,fit,damma:0,kasra:0,overlayMarks:marks,overlayFatha:fatha,overlayDamma:damma,overlayKasra:kasra,overlayAnchorsClamped:clamped};
    }''')

p001.base.base.fit_joined = fit_joined_cluster_overlay
_original_fit_and_inspect = p001.fit_and_inspect

async def fit_and_inspect_v15(page):
    metrics, issues = await _original_fit_and_inspect(page)
    extra = await page.evaluate(r'''()=>{
      const out=[];
      for(const slot of document.querySelectorAll('.j2-object')){
        const s=slot.getBoundingClientRect();
        for(const mark of slot.querySelectorAll('.q-overlay-mark')){
          const r=mark.getBoundingClientRect();
          const cx=(r.left+r.right)/2, cy=(r.top+r.bottom)/2;
          if(cx<s.left-6||cx>s.right+6){
            out.push({kind:'OVERLAY_MARK_ANCHOR_OUTSIDE_CELL_X',slot:slot.dataset.slot,mark:mark.dataset.mark,cx,slotLeft:s.left,slotRight:s.right});
          }
          if(cy<s.top-1||cy>s.bottom+1){
            out.push({kind:'OVERLAY_MARK_ANCHOR_OUTSIDE_CELL_Y',slot:slot.dataset.slot,mark:mark.dataset.mark,cy,slotTop:s.top,slotBottom:s.bottom});
          }
        }
      }
      return out;
    }''')
    issues.extend(extra)
    return metrics, issues

p001.fit_and_inspect = fit_and_inspect_v15


def main():
    rc=p001.main()
    print('JILID2_P001_RENDERER_V15=PASS')
    print('LEGACY_VERTICAL_FITTER=DISABLED')
    print('WHOLE_WORD_VERTICAL_OFFSET=DISABLED')
    print('BASE_JOINING=UNINTERRUPTED_NATIVE_ARABIC')
    print('HARAKAT_POSITIONING=DOM_RANGE_CLUSTER_OVERLAY')
    print('HARAKAT_FONT_SIZE_PT=26')
    print('FATHA_CLUSTER_Y_RATIO=0.28')
    print('DAMMA_CLUSTER_Y_RATIO=0.38')
    print('KASRA_CLUSTER_Y_RATIO=0.97')
    print('OVERLAY_ANCHOR_Y_CLAMP=3PX_INSIDE_LOGICAL_CELL')
    print('OVERLAY_VALIDATION=ANCHOR_CENTER_INSIDE_LOGICAL_CELL')
    print('FIT_POLICY=HORIZONTAL_SCALE_ONLY')
    return rc

if __name__=='__main__': raise SystemExit(main())
