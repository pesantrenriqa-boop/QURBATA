#!/usr/bin/env python3
"""QURBATA Jilid 2 P024 — K2 U02 mad ya: 2→3-letter ladder; open naskhi sukun overlay."""
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
ROUND_SUKUN='ْ'; UTHMANI_HEAD='ۡ'; FORBIDDEN_MARKS=set('ًٌٍّ')
MARKS=set(chr(c) for c in range(0x064B,0x0660))|{UTHMANI_HEAD,'ـ'}
def bases(s): return ''.join(ch for ch in unicodedata.normalize('NFC',s) if ch not in MARKS and unicodedata.category(ch)!='Mn')
def has_mad_ya(text):
    chars=list(text); return any(ch=='ي' and i>=1 and chars[i-1]=='ِ' for i,ch in enumerate(chars))
lengths={2:0,3:0}
for r in lex:
    n=len(bases(r['word']))
    if n not in lengths: raise ValueError('P024_LENGTH_GATE_FAIL='+repr(r))
    lengths[n]+=1
    if r['function']!='CURRENT' or r['lexical_status']!='CURATED' or r['competency_status']!='ALLOWED': raise ValueError('P024_STATUS_GATE_FAIL='+repr(r))
    if ROUND_SUKUN in r['word'] or UTHMANI_HEAD in r['word']: raise ValueError('P024_INLINE_SUKUN_FORBIDDEN='+repr(r))
    if not has_mad_ya(r['word']): raise ValueError('P024_MAD_YA_REQUIRED='+repr(r))
    if n==3 and (not r['meaning_id'].strip() or not r['word'].endswith('ُ')): raise ValueError('P024_THREE_LETTER_SEMANTIC_OR_FINAL_DAMMA_FAIL='+repr(r))
    if any(m in r['word'] for m in FORBIDDEN_MARKS): raise ValueError('P024_UPPER_COMPETENCY_MARK_LEAKAGE='+repr(r))
if lengths!={2:16,3:16}: raise ValueError('P024_LADDER_DISTRIBUTION_FAIL='+repr(lengths))
p001.MICRO=MICRO; p001.P001_BANNED_JOINING=set(); words=[r['word'] for r in lex]; p001.P001_ROWS=[words[i:i+4] for i in range(0,32,4)]
p001.P001_CSS += r'''
.presentation-object{font-size:48pt}.j2-glyph{font-size:44pt}
.mad-unit{display:inline-block;direction:rtl;unicode-bidi:isolate;font-family:"QURBATA KFGQPC Uthman Taha Naskh",serif!important;font-feature-settings:"mark" 1,"mkmk" 1}
.j2-object,.presentation-object .arabic-part{position:relative;overflow:visible!important}
.sukun-open-naskhi{position:absolute!important;z-index:30!important;pointer-events:none!important;overflow:visible!important;display:block!important;color:#000!important}
.sukun-open-naskhi path{fill:#000!important;stroke:none!important}
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

# SVG is intentionally independent from Arabic shaping. The path is an open
# ras-al-kha silhouette (not a circle and not a Unicode combining character).
# Explicit SVG width/height attributes plus CSS pixels avoid Chromium reporting
# zero geometry, which caused V6's false visibility failure.
SUKUN_OVERLAY_JS=r'''() => {
  const targets=[...document.querySelectorAll('.j2-object,.presentation-object .mad-unit')];
  let count=0;
  for(const el of targets){
    if(el.dataset.sukunDone==='1') continue;
    const walker=document.createTreeWalker(el,NodeFilter.SHOW_TEXT);
    let node,hit=null,idx=-1;
    while((node=walker.nextNode())){
      const t=node.nodeValue||'';
      for(let i=1;i<t.length;i++){ if(t[i]==='ي'&&t[i-1]==='ِ'){hit=node;idx=i;break;} }
      if(hit) break;
    }
    if(!hit) continue;
    const range=document.createRange(); range.setStart(hit,idx); range.setEnd(hit,idx+1);
    const rr=range.getBoundingClientRect(), er=el.getBoundingClientRect();
    const fs=parseFloat(getComputedStyle(el).fontSize)||58;
    const w=Math.max(12,fs*0.24), h=Math.max(9,fs*0.18);
    const svg=document.createElementNS('http://www.w3.org/2000/svg','svg');
    svg.classList.add('sukun-open-naskhi'); svg.setAttribute('aria-hidden','true');
    svg.setAttribute('viewBox','0 0 28 20'); svg.setAttribute('width',String(w)); svg.setAttribute('height',String(h));
    svg.style.width=w+'px'; svg.style.height=h+'px';
    svg.style.left=(rr.left-er.left+rr.width*0.50-w*0.50)+'px';
    svg.style.top=(rr.top-er.top-fs*0.16-h*0.50)+'px';
    const path=document.createElementNS('http://www.w3.org/2000/svg','path');
    // Compact open head: thick right horn, shallow crown, tapered left return;
    // deliberately no lower closing stroke, therefore it cannot read as round sukun.
    path.setAttribute('d','M25 3.2 C20.7 1.1 14.6 1.0 9.8 2.9 C5.8 4.5 3.4 7.4 3.9 10.4 C4.3 13.0 6.8 15.0 10.6 15.4 L11.7 12.2 C9.2 11.9 7.8 10.8 7.6 9.4 C7.4 7.9 8.8 6.5 11.2 5.6 C14.7 4.3 19.2 4.6 23.0 6.4 Z');
    svg.appendChild(path); el.appendChild(svg); el.dataset.sukunDone='1'; count++;
  }
  return count;
}'''
async def render(h,out,debug):
    report=out/'LAYOUT-OVERFLOW-REPORT-J2-P024-V7.json'; png=out/'png'; png.mkdir(parents=True,exist_ok=True)
    async with async_playwright() as pw:
        browser=await pw.chromium.launch(); page=await browser.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2)
        await page.goto(h.resolve().as_uri(),wait_until='networkidle'); await page.evaluate('document.fonts.ready')
        if await page.locator('.j2-object').count()!=32: raise RuntimeError('P024_OBJECT_COUNT_INVALID')
        if (await page.locator('.page-number').inner_text()).strip()!='24': raise RuntimeError('P024_PAGE_IDENTITY_FAIL')
        family=await page.locator('.mad-unit').first.evaluate("e=>getComputedStyle(e).fontFamily")
        if 'QURBATA KFGQPC Uthman Taha Naskh' not in family: raise RuntimeError('P024_FONT_BINDING_FAIL='+repr(family))
        raw=await page.locator('body').inner_text()
        if ROUND_SUKUN in raw or UTHMANI_HEAD in raw: raise RuntimeError('P024_INLINE_SUKUN_RENDERED')
        overlay_count=await page.evaluate(SUKUN_OVERLAY_JS)
        if overlay_count!=34: raise RuntimeError(f'P024_SUKUN_OVERLAY_COUNT_FAIL actual={overlay_count} expected=34')
        visible=await page.evaluate("""()=>[...document.querySelectorAll('.sukun-open-naskhi')].every(e=>{const r=e.getBoundingClientRect(),p=e.querySelector('path');return !!p && r.width>=10 && r.height>=7 && p.getAttribute('d').length>20})""")
        if not visible: raise RuntimeError('P024_SUKUN_VISIBILITY_GATE_FAIL')
        metrics,issues=await p001.fit_and_inspect(page); report.write_text(json.dumps(issues,ensure_ascii=False,indent=2),encoding='utf-8')
        if issues: raise RuntimeError('P024_LAYOUT_ISSUES='+str(len(issues))+' REPORT='+str(report))
        await page.screenshot(path=str(png/'page-024.png'),full_page=True)
        pdf=out/'QURBATA-JILID-2-P024-V7-KFGQPC-MAD-YA-2TO3-OPEN-NASKHI-SUKUN.pdf'; await page.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'}); await browser.close()
    return metrics,report,pdf
p001.render=render
def main():
    rc=v22.main(); print('JILID2_P024_RENDERER_V7=PASS'); print('PAGE=24'); print('K_SEQUENCE=K2'); print('UK_SEQUENCE=J2.K2.U02'); print('SEQUENCE_BEFORE=P021-P023:MAD_ALIF'); print('HEADER_SEQUENCE=دِ|دِي|دِينُ'); print('NEW_COMPETENCY=MAD_YA'); print('P024_STAGE=TWO_TO_THREE_LETTER_LADDER'); print('TWO_LETTER_OBJECTS=16'); print('THREE_LETTER_OBJECTS=16'); print('MAD_PATTERN=KASRA_PLUS_YA'); print('MAD_LENGTH=2_HARAKAT'); print('SUKUN_STYLE=OPEN_NASKHI_RAS_AL_KHA'); print('SUKUN_RENDER_MODE=EXPLICIT_SIZED_SVG_OVERLAY'); print('SUKUN_VISIBILITY_GATE=PASS'); print('INLINE_SUKUN_CODEPOINTS=FORBIDDEN'); print('SUKUN_OVERLAY_COUNT=34'); print('FINAL_HARAKAT_FOR_3_LETTER=DAMMA'); print('ARABIC_FONT_PRIMARY=QURBATA KFGQPC Uthman Taha Naskh'); print('STATUS=P024_2TO3_OPEN_NASKHI_SUKUN_CANDIDATE_NOT_FROZEN'); return rc
if __name__=='__main__': raise SystemExit(main())
