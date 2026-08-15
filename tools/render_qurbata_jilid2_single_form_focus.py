#!/usr/bin/env python3
from __future__ import annotations
import csv,json,sys,unicodedata
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v22_kfgqpc_lexical as v22
import render_qurbata_jilid2_p001_v1 as p001
MARKS=set(chr(c) for c in range(0x064B,0x0660))|{'ـ'}
def base(s): return ''.join(ch for ch in unicodedata.normalize('NFC',s) if ch not in MARKS and unicodedata.category(ch)!='Mn')

def run(page_no:int,letter:str,example:str,banned:str,tag:str):
    p=f'{page_no:03d}'; MAP=ROOT/f'content/qwo/registry/JILID-2-P{p}-COMPETENCY-MAP-V1.csv'; MICRO=ROOT/f'content/qwo/registry/JILID-2-MICRO-COMPETENCY-P{p}-V1.csv'; LEX=ROOT/f'content/qwo/registry/JILID-2-P{p}-LEXICAL-FOUNDATION-V1.csv'
    with MAP.open(encoding='utf-8-sig',newline='') as f: meta=next(csv.DictReader(f))
    with MICRO.open(encoding='utf-8-sig',newline='') as f: stairs=list(csv.DictReader(f))
    with LEX.open(encoding='utf-8-sig',newline='') as f: lex=list(csv.DictReader(f))
    if len(lex)!=32: raise ValueError(f'P{p}_LEXICAL_COUNT_INVALID')
    p001.MICRO=MICRO; p001.P001_BANNED_JOINING=set(banned)
    core=lex[:28]; forms=[r['word'] for r in core]; p001.P001_ROWS=[forms[i:i+4] for i in range(0,28,4)]
    p001.P001_CSS+=r'''.presentation-object{font-size:34pt!important;direction:ltr!important;flex-direction:row-reverse!important;gap:1.7mm!important}.presentation-object .arabic-part{direction:rtl!important;line-height:1.15!important}.presentation-object .arrow{font-size:15pt!important}.j2-glyph{font-size:39pt!important}.j2-grid{grid-template-rows:repeat(8,minmax(0,1fr))!important}.single-enrichment-row{grid-column:1/-1!important;grid-row:8!important;display:grid!important;grid-template-columns:1fr 1fr!important;gap:10mm!important;padding:.55mm 6mm .35mm!important;border-top:.28mm solid #111!important;box-sizing:border-box!important;background:#fff!important}.single-enrichment-row .micro{display:flex!important;flex-direction:column!important;align-items:center!important;justify-content:center!important}.single-enrichment-row .micro-label{font-family:Arial,sans-serif!important;font-size:6.2pt!important;font-weight:700!important;margin:0 0 .7mm!important}.glyph-run{display:flex!important;justify-content:center!important;gap:1.45mm!important;direction:ltr!important}.glyph-run.num .eg{font-size:20pt!important;width:4mm!important;text-align:center!important}.glyph-run.nonjoin .eg{font-size:21pt!important;width:5mm!important;text-align:center!important}'''
    base_build=p001.build_page_html
    def build(debug):
        h=base_build(debug).replace('<div class="page-number">01</div>',f'<div class="page-number">{page_no:02d}</div>',1)
        s=h.index('<section class="presentation">');e=h.index('</section>',s)+10
        pres=f'''<section class="presentation"><div class="presentation-object-wrap"><div class="presentation-object" dir="ltr"><span class="arabic-part">{p001.arabic_html(letter+'َ')}</span><span class="arrow">←</span><span class="arabic-part">{p001.arabic_html(example)}</span></div></div></section>''';h=h[:s]+pres+h[e:]
        nums=''.join(f'<span class="eg">{x}</span>' for x in '٠١٢٣٤٥٦٧٨٩');njs=''.join(f'<span class="eg">{x}</span>' for x in 'ادذرزو');en=f'''<div class="single-enrichment-row"><div class="micro"><div class="micro-label">ANGKA ARAB</div><div class="glyph-run num">{nums}</div></div><div class="micro"><div class="micro-label">PEMUTUS SAMBUNGAN</div><div class="glyph-run nonjoin">{njs}</div></div></div>''';g=h.find('<section class="j2-grid">');ge=h.find('</section>',g);return h[:ge]+en+h[ge:]
    p001.build_page_html=build
    async def render(h,out,debug):
        report=out/f'LAYOUT-OVERFLOW-REPORT-J2-P{p}-SINGLE.json';png=out/'png';png.mkdir(parents=True,exist_ok=True)
        async with async_playwright() as pw:
            b=await pw.chromium.launch();page=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);await page.goto(h.resolve().as_uri(),wait_until='networkidle');await page.evaluate('document.fonts.ready');metrics,issues=await p001.fit_and_inspect(page);report.write_text(json.dumps(issues,ensure_ascii=False,indent=2),encoding='utf-8')
            if issues: raise RuntimeError(f'P{p}_LAYOUT_ISSUES='+repr(issues))
            await page.screenshot(path=str(png/f'page-{p}-single.png'),full_page=True)
            names=[out/f'QURBATA-JILID-2-P{p}-{tag}.pdf']+[out/f'QURBATA-JILID-2-P{p}-{tag}-LOCK-SAFE-{i:02d}.pdf' for i in range(1,100)]
            pdf=None;mode=None
            for i,name in enumerate(names):
                try: await page.pdf(path=str(name),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});pdf=name;mode='DIRECT_SINGLE' if i==0 else f'LOCK_FALLBACK_SINGLE_{i:02d}';break
                except PermissionError: pass
            await b.close()
        if pdf is None: raise RuntimeError(f'P{p}_NO_AVAILABLE_PDF_NAME')
        return metrics,report,pdf,mode
    p001.render=render
    focus=sum(letter in base(r['word']) for r in core)
    if focus<28: raise ValueError(f'P{p}_SINGLE_FOCUS_FAIL letter={letter} count={focus} required=28')
    premature=[]
    for r in core:
        hit=set(base(r['word']))&set('اأإآءؤئى')
        if hit: premature.append((r['word'],''.join(sorted(hit))))
    if premature: raise ValueError(f'P{p}_PREMATURE_MADD_OR_HAMZAH='+repr(premature))
    leaks=[]
    for r in core:
        hit=set(banned)&set(base(r['word']))
        if hit: leaks.append((r['word'],''.join(sorted(hit))))
    if leaks: raise ValueError(f'P{p}_FUTURE_LETTER_LEAKAGE='+repr(leaks))
    if '--output-dir' not in sys.argv[1:]: sys.argv.extend(['--output-dir',f'dist/qurbata-print-ready/jilid-2/pages/P{p}'])
    rc=v22.main();print(f'JILID2_P{p}_SINGLE_FORM_FOCUS=PASS');print(f'PAGE={page_no}');print(f'ACQUISITION_LETTERS={letter}');print('PRACTICE_MODE=JOINING_FORM_DRILL');print(f'FORM_FOCUS_OBJECTS={focus}');print(f'TITLE_VISUAL_RIGHT_TO_LEFT={letter}َ←{example}');print('PREMATURE_MADD_OR_HAMZAH=0');print('FUTURE_LETTER_LEAKAGE=0');return rc
