#!/usr/bin/env python3
"""Non-destructive Naskhi/Uthmani sukun overlay for QURBATA.

Purpose:
- Keep the Arabic word in ONE uninterrupted shaping run.
- Never insert U+0652 or U+06E1 into the lexical string.
- Place a visual head-of-khah sukun above the target mad letter after shaping.

This avoids the P023 failure where combining U+06E1 directly into KFGQPC broke GPOS.
"""
from __future__ import annotations

NASKHI_SUKUN_GLYPH = "ۡ"  # U+06E1, visual overlay only; never inserted into source word.

CSS = r'''
.qrb-sukun-host{position:relative;display:inline-block;direction:rtl;unicode-bidi:isolate}
.qrb-sukun-overlay{position:fixed;z-index:20;pointer-events:none;font-family:"QURBATA KFGQPC Uthman Taha Naskh",serif;font-weight:400;line-height:1;transform:translate(-50%,-100%);transform-origin:center bottom}
'''

JS = r'''
async function qurbataApplyNaskhiSukunOverlays(){
  await document.fonts.ready;
  document.querySelectorAll('.qrb-sukun-overlay').forEach(x=>x.remove());
  const hosts=[...document.querySelectorAll('.qrb-sukun-host[data-sukun-char]')];
  const out=[];
  for(const host of hosts){
    const target=host.dataset.sukunChar;
    const occurrence=parseInt(host.dataset.sukunOccurrence||'1',10);
    const textNode=[...host.childNodes].find(n=>n.nodeType===Node.TEXT_NODE && n.textContent.includes(target));
    if(!textNode){out.push({ok:false,reason:'TEXT_NODE_NOT_FOUND',text:host.textContent});continue;}
    let seen=0,index=-1;
    for(let i=0;i<textNode.textContent.length;i++){
      if(textNode.textContent[i]===target){seen++;if(seen===occurrence){index=i;break;}}
    }
    if(index<0){out.push({ok:false,reason:'TARGET_NOT_FOUND',text:host.textContent,target});continue;}
    const range=document.createRange(); range.setStart(textNode,index); range.setEnd(textNode,index+1);
    const r=range.getBoundingClientRect();
    const mark=document.createElement('span'); mark.className='qrb-sukun-overlay'; mark.textContent='ۡ';
    const fs=parseFloat(getComputedStyle(host).fontSize)||40;
    mark.style.fontSize=(fs*0.42)+'px';
    mark.style.left=(r.left+r.width/2)+'px';
    mark.style.top=(r.top+Math.max(1,fs*0.08))+'px';
    document.body.appendChild(mark);
    out.push({ok:true,target,left:r.left,top:r.top,width:r.width,height:r.height});
  }
  return out;
}
'''

def host_html(word: str, target_char: str, occurrence: int = 1, cls: str = "") -> str:
    """Return an uninterrupted word span tagged for post-shaping sukun overlay."""
    safe_cls=("qrb-sukun-host "+cls).strip()
    return f'<span class="{safe_cls}" lang="ar" data-sukun-char="{target_char}" data-sukun-occurrence="{occurrence}">{word}</span>'

async def apply(page):
    """Apply overlays after document/font load and return geometry diagnostics."""
    await page.add_style_tag(content=CSS)
    await page.add_script_tag(content=JS)
    result=await page.evaluate('qurbataApplyNaskhiSukunOverlays()')
    bad=[x for x in result if not x.get('ok')]
    if bad:
        raise RuntimeError('QURBATA_NASKHI_SUKUN_OVERLAY_FAIL='+repr(bad))
    return result
