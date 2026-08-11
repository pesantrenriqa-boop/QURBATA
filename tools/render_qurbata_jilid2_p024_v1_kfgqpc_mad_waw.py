#!/usr/bin/env python3
"""QURBATA Jilid 2 P024 — K2 U02 mad ya: KFGQPC base glyphs with Amiri open-sukun mark anchored to ya glyph."""
from __future__ import annotations
import csv,json,sys,unicodedata
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v22_kfgqpc_lexical as v22
import render_qurbata_jilid2_p001_v1 as p001
MAP=ROOT/'content/qwo/registry/JILID-2-P024-COMPETENCY-MAP-V1.csv'; MICRO=ROOT/'content/qwo/registry/JILID-2-MICRO-COMPETENCY-P024-V1.csv'; LEX=ROOT/'content/qwo/registry/JILID-2-P024-LEXICAL-FOUNDATION-V1.csv'
with MAP.open(encoding='utf-8-sig',newline='') as f: meta=next(csv.DictReader(f))
with MICRO.open(encoding='utf-8-sig',newline='') as f: stairs=list(csv.DictReader(f))
with LEX.open(encoding='utf-8-sig',newline='') as f: lex=list(csv.DictReader(f))
if len(stairs)!=10 or len(lex)!=32: raise ValueError('P024_REGISTRY_INVALID')
OPEN_SUKUN='ۡ'; ROUND_SUKUN='ْ'; FORBIDDEN_MARKS=set('ًٌٍّ')
MARKS=set(chr(c) for c in range(0x064B,0x0660))|{OPEN_SUKUN,'ـ'}
def bases(s): return ''.join(ch for ch in unicodedata.normalize('NFC',s) if ch not in MARKS and unicodedata.category(ch)!='Mn')
def has_mad_ya(text):
    chars=list(text); return any(ch=='ي' and i>=1 and chars[i-1]=='ِ' for i,ch in enumerate(chars))
lengths={2:0,3:0}
for r in lex:
    n=len(bases(r['word']))
    if n not in lengths: raise ValueError('P024_LENGTH_GATE_FAIL='+repr(r))
    lengths[n]+=1
    if r['function']!='CURRENT' or r['lexical_status']!='CURATED' or r['competency_status']!='ALLOWED': raise ValueError('P024_STATUS_GATE_FAIL='+repr(r))
    if ROUND_SUKUN in r['word'] or OPEN_SUKUN in r['word']: raise ValueError('P024_REGISTRY_MUST_REMAIN_MARK_FREE='+repr(r))
    if not has_mad_ya(r['word']): raise ValueError('P024_MAD_YA_REQUIRED='+repr(r))
    if n==3 and (not r['meaning_id'].strip() or not r['word'].endswith('ُ')): raise ValueError('P024_THREE_LETTER_SEMANTIC_OR_FINAL_DAMMA_FAIL='+repr(r))
    if any(m in r['word'] for m in FORBIDDEN_MARKS): raise ValueError('P024_UPPER_COMPETENCY_MARK_LEAKAGE='+repr(r))
if lengths!={2:16,3:16}: raise ValueError('P024_LADDER_DISTRIBUTION_FAIL='+repr(lengths))
# Keep ALL words mark-free so KFGQPC shapes them exactly as earlier pages.
p001.MICRO=MICRO; p001.P001_BANNED_JOINING=set(); words=[r['word'] for r in lex]; p001.P001_ROWS=[words[i:i+4] for i in range(0,32,4)]
p001.P001_CSS += r'''
.presentation-object{font-size:48pt}.j2-glyph{font-size:44pt}
.j2-glyph,.presentation-object,.presentation-object .arabic-part,.mad-unit{font-family:"QURBATA KFGQPC Uthman Taha Naskh","KFGQPC Uthman Taha Naskh",serif!important;font-feature-settings:'mark' 1,'mkmk' 1;font-kerning:normal;text-rendering:optimizeLegibility}
.mad-unit{display:inline-block;direction:rtl;unicode-bidi:isolate}
.page{position:relative}
.sukun-mark-layer{position:absolute;inset:0;pointer-events:none;z-index:80;overflow:visible}
.sukun-native-amiri{position:absolute;display:block;font-family:'Amiri Quran','Amiri',serif!important;font-weight:400;line-height:1;color:#000;transform:translate(-50%,-50%);transform-origin:center;white-space:nowrap}
'''
orig=p001.build_page_html
def build(debug):
    h=orig(debug).replace('<div class="page-number">01</div>','<div class="page-number">24</div>',1)
    s=h.index('<section class="presentation">'); e=h.index('</section>',s)+len('</section>')
    pres='''<section class="presentation"><div class="presentation-object-wrap"><div class="presentation-object"><span class="arabic-part mad-unit" lang="ar">دِينُ</span><span class="arrow">←</span><span class="arabic-part mad-unit" lang="ar">دِي</span><span class="arrow">←</span><span class="arabic-part" lang="ar">دِ</span></div></div></section>'''
    h=h[:s]+pres+h[e:]
    ts=h.index('<section class="targets">'); te=h.index('</section>',ts)+len('</section>')
    t=f'''<section class="targets"><div class="target-item"><span>Kompetensi</span><strong>{meta['CompetencyCode']} — {meta['Competency']}</strong></div><div class="target-item"><span>Unit Kompetensi</span><strong>{meta['UnitCompetencyCode']} — {meta['UnitCompetency']}</strong></div><div class="target-item"><span>Unit Murojaah</span><strong>{meta['UnitMurojaahCode']} — {meta['UnitMurojaah']}</strong></div><div class="target-item"><span>Tangga</span><strong>{stairs[0]['StairCode']}–{stairs[-1]['StairCode']}</strong></div></section>'''
    return h[:ts]+t+h[te:]
p001.build_page_html=build

# Hybrid strategy: KFGQPC remains the only font shaping each Arabic word. After
# shaping is complete, locate the actual rendered ya glyph via a DOM Range and draw
# ONLY U+06E1 in Amiri Quran on a page-level layer using viewport coordinates.
# Appending to the page (not the word) avoids RTL local-coordinate drift seen in V7-V9.
SUKUN_LAYER_JS=r'''() => {
  const page=document.querySelector('.page'); if(!page) return {count:0,placed:[]};
  let layer=page.querySelector('.sukun-mark-layer'); if(layer) layer.remove();
  layer=document.createElement('div'); layer.className='sukun-mark-layer'; page.appendChild(layer);
  const pr=page.getBoundingClientRect(); const placed=[];
  const targets=[...document.querySelectorAll('.j2-glyph,.presentation-object .mad-unit')];
  for(const el of targets){
    const walker=document.createTreeWalker(el,NodeFilter.SHOW_TEXT); let node,hit=null,idx=-1;
    while((node=walker.nextNode())){
      const t=node.nodeValue||'';
      for(let i=1;i<t.length;i++){ if(t[i]==='ي'&&t[i-1]==='ِ'){hit=node;idx=i;break;} }
      if(hit) break;
    }
    if(!hit) continue;
    const range=document.createRange(); range.setStart(hit,idx); range.setEnd(hit,idx+1);
    const rects=[...range.getClientRects()].filter(r=>r.width>0&&r.height>0); if(!rects.length) continue;
    const rr=rects[0], fs=parseFloat(getComputedStyle(el).fontSize)||58;
    const mark=document.createElement('span'); mark.className='sukun-native-amiri'; mark.setAttribute('aria-hidden','true'); mark.textContent='\u06E1';
    mark.style.fontSize=(fs*0.34)+'px';
    mark.style.left=(rr.left-pr.left+rr.width*0.52)+'px';
    mark.style.top=(rr.top-pr.top-fs*0.11)+'px';
    layer.appendChild(mark); placed.push({x:rr.left-pr.left+rr.width*0.52,y:rr.top-pr.top-fs*0.11,w:rr.width,h:rr.height});
  }
  return {count:placed.length,placed};
}'''
async def render(h,out,debug):
    report=out/'LAYOUT-OVERFLOW-REPORT-J2-P024-V12.json';png=out/'png';png.mkdir(parents=True,exist_ok=True)
    async with async_playwright() as pw:
        browser=await pw.chromium.launch();page=await browser.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2)
        await page.goto(h.resolve().as_uri(),wait_until='networkidle');await page.evaluate('document.fonts.ready')
        if await page.locator('.j2-object').count()!=32: raise RuntimeError('P024_OBJECT_COUNT_INVALID')
        if (await page.locator('.page-number').inner_text()).strip()!='24': raise RuntimeError('P024_PAGE_IDENTITY_FAIL')
        body=await page.locator('body').inner_text()
        if OPEN_SUKUN in body or ROUND_SUKUN in body: raise RuntimeError('P024_INLINE_SUKUN_FORBIDDEN')
        families=await page.evaluate("""()=>[...document.querySelectorAll('.j2-glyph,.presentation-object .arabic-part')].map(e=>getComputedStyle(e).fontFamily)""")
        if not families or any('QURBATA KFGQPC Uthman Taha Naskh' not in f for f in families): raise RuntimeError('P024_BASE_FONT_REGRESSION='+repr(families[:4]))
        placed=await page.evaluate(SUKUN_LAYER_JS)
        if placed['count']!=34: raise RuntimeError(f"P024_SUKUN_MARK_COUNT_FAIL actual={placed['count']} expected=34")
        visible=await page.evaluate("""()=>[...document.querySelectorAll('.sukun-native-amiri')].every(e=>{const r=e.getBoundingClientRect();return r.width>0&&r.height>0&&getComputedStyle(e).visibility!=='hidden'})""")
        if not visible: raise RuntimeError('P024_SUKUN_VISIBILITY_FAIL')
        metrics,issues=await p001.fit_and_inspect(page);report.write_text(json.dumps({'layout_issues':issues,'sukun_positions':placed['placed']},ensure_ascii=False,indent=2),encoding='utf-8')
        if issues: raise RuntimeError('P024_LAYOUT_ISSUES='+str(len(issues))+' REPORT='+str(report))
        await page.screenshot(path=str(png/'page-024.png'),full_page=True)
        pdf=out/'QURBATA-JILID-2-P024-V12-KFGQPC-WORDS-AMIRI-OPEN-SUKUN.pdf';await page.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await browser.close()
    return metrics,report,pdf
p001.render=render
def main():
    rc=v22.main();print('JILID2_P024_RENDERER_V12=PASS');print('PAGE=24');print('HEADER_SEQUENCE=دِ|دِي|دِينُ');print('P024_STAGE=TWO_TO_THREE_LETTER_LADDER');print('TWO_LETTER_OBJECTS=16');print('THREE_LETTER_OBJECTS=16');print('BASE_ARABIC_FONT=KFGQPC_UTHMAN_TAHA');print('SUKUN_CODEPOINT=U+06E1');print('SUKUN_MARK_FONT=AMIRI_QURAN_ONLY');print('SUKUN_RENDER_MODE=PAGE_LAYER_RANGE_ANCHORED');print('INLINE_SUKUN=DISABLED');print('WORD_FONT_FALLBACK=DISABLED');print('SUKUN_MARK_COUNT=34');print('STATUS=P024_HYBRID_SUKUN_CANDIDATE_NOT_FROZEN');return rc
if __name__=='__main__': raise SystemExit(main())
