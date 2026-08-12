#!/usr/bin/env python3
"""Build a visual recovery contact-sheet PDF from QJ2 historical candidate records.

This is a REVIEW artifact, not a freeze operation. It materializes the selected
historical source at its exact commit where possible, extracts Arabic/presentation
content, and renders one A5 review page per QJ2 page using the frozen visual grammar.
No production source or freeze register is modified.
"""
from __future__ import annotations
import csv, html, re, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
REC=ROOT/'dist/jilid-2-visual-history-recovery'
CAND=REC/'JILID-2-HISTORICAL-VISUAL-CANDIDATES.tsv'
OUT=REC/'visual-pdf-review'
HTML=OUT/'QURBATA-JILID-2-HISTORICAL-VISUAL-RECOVERY.html'
PDF=OUT/'QURBATA-JILID-2-HISTORICAL-VISUAL-RECOVERY-P001-P040.pdf'

ARABIC_RE=re.compile(r'[\u0600-\u06ff][\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff\u064b-\u065f\u0670\u06d6-\u06ed\s]{0,40}')

def git_show(commit,path):
    if not commit or not path:return ''
    p=subprocess.run(['git','show',f'{commit}:{path}'],cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL)
    return p.stdout.decode('utf-8','replace') if p.returncode==0 else ''

def read_candidates():
    if not CAND.exists():raise SystemExit('Run select_qurbata_jilid2_historical_visual_candidates.py first')
    with CAND.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f,delimiter='\t'))

def pick(row,*names):
    for n in names:
        if n in row and row[n]:return row[n]
    return ''

def arabic_objects(text):
    vals=[]
    # Prefer quoted/list Arabic fragments from renderer/source history.
    for m in ARABIC_RE.finditer(text):
        s=' '.join(m.group(0).split()).strip(' ,;|[](){}\"\'')
        if s and any('\u0600'<=c<='\u06ff' for c in s) and s not in vals:
            vals.append(s)
    return vals[:28]

def page_html(page,commit,path,text,status):
    objs=arabic_objects(text)
    presentation=objs[:4]
    practice=objs[4:28] if len(objs)>4 else objs
    pres=' <span class="arr">←</span> '.join(f'<span>{html.escape(x)}</span>' for x in presentation) if presentation else '<span class="warn">presentation recovery needed</span>'
    cells=[]
    for x in practice:
        base=sum(1 for c in x if '\u0621'<=c<='\u064a')
        cls='l2' if base<=2 else 'l3'
        cells.append(f'<div class="cell {cls}" lang="ar">{html.escape(x)}</div>')
    if not cells:cells=['<div class="warn">No Arabic objects extracted automatically; inspect historical source.</div>']
    return f'''<section class="sheet"><header><b>QURBATA JILID 2 — P{page:03d}</b><span>{html.escape(status)}</span></header><div class="presentation" dir="rtl">{pres}</div><div class="grid" dir="rtl">{''.join(cells)}</div><footer><code>{html.escape(commit[:12])}</code> · {html.escape(path)}</footer></section>'''

def main():
    rows=read_candidates();OUT.mkdir(parents=True,exist_ok=True)
    pages=[];resolved=0
    for i,row in enumerate(rows,1):
        ptxt=pick(row,'Page','page','PAGE') or f'P{i:03d}'
        m=re.search(r'(\d{1,3})',ptxt);page=int(m.group(1)) if m else i
        commit=pick(row,'Commit','commit','CandidateCommit','candidate_commit','SelectedCommit','selected_commit')
        path=pick(row,'Path','path','CandidatePath','candidate_path','SelectedPath','selected_path','File','file')
        status=pick(row,'Status','status','CandidateStrength','candidate_strength','SelectionStatus','selection_status') or 'REVIEW'
        text=git_show(commit,path)
        if text:resolved+=1
        pages.append(page_html(page,commit,path,text,status))
    css='''@page{size:A5;margin:0}*{box-sizing:border-box}body{margin:0;background:#ddd}.sheet{width:148mm;height:210mm;background:#fff;padding:8mm;page-break-after:always;position:relative;overflow:hidden;font-family:Arial,sans-serif}header{height:12mm;border-bottom:.4mm solid #b98a2f;color:#064d37;display:flex;justify-content:space-between;align-items:center;font-size:8pt}header span{font-size:5.5pt;color:#777}.presentation{height:38mm;display:flex;align-items:center;justify-content:center;gap:4mm;font-family:"KFGQPC Uthman Taha Naskh","KFGQPC Uthmanic Script HAFS","Amiri Quran",serif;font-size:31pt}.arr{font-family:Arial;font-size:18pt;color:#b98a2f}.grid{display:grid;grid-template-columns:repeat(12,1fr);gap:4mm 3mm;align-items:center}.cell{min-height:24mm;border:.25mm solid #d7c59b;border-radius:2mm;display:flex;align-items:center;justify-content:center;font-family:"KFGQPC Uthman Taha Naskh","KFGQPC Uthmanic Script HAFS","Amiri Quran",serif;font-size:34pt;line-height:1.1}.l2{grid-column:span 3}.l3{grid-column:span 4}.warn{grid-column:1/-1;text-align:center;color:#a33;font:8pt Arial}footer{position:absolute;left:8mm;right:8mm;bottom:5mm;border-top:.2mm solid #ddd;padding-top:1mm;font-size:5pt;color:#777;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}'''
    doc='<!doctype html><html><head><meta charset="utf-8"><style>'+css+'</style></head><body>'+''.join(pages)+'</body></html>'
    HTML.write_text(doc,encoding='utf-8')
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as pw:
            b=pw.chromium.launch();pg=b.new_page(viewport={'width':1120,'height':1584});pg.goto(HTML.resolve().as_uri(),wait_until='networkidle');pg.evaluate('document.fonts.ready');pg.pdf(path=str(PDF),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});b.close()
        print('QJ2_HISTORICAL_VISUAL_RECOVERY_PDF=PASS')
    except Exception as e:
        print('QJ2_HISTORICAL_VISUAL_RECOVERY_PDF=HTML_ONLY')
        print('PDF_ERROR='+str(e).replace('\n',' '))
    print(f'CANDIDATE_ROWS={len(rows)}');print(f'HISTORICAL_SOURCES_RESOLVED={resolved}');print('FREEZE_STATUS_MODIFIED=NO');print('PRODUCTION_FILES_MODIFIED=NO');print(f'HTML={HTML.relative_to(ROOT)}');print(f'PDF={PDF.relative_to(ROOT)}')
if __name__=='__main__':main()
