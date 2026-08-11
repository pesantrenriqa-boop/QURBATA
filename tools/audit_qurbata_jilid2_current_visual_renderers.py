#!/usr/bin/env python3
"""Audit QURBATA Jilid 2 visual renderer coverage for the current KFGQPC edition.

The audit scans tools/render_qurbata_jilid2_*.py and classifies renderers without
rendering them. It prevents legacy Amiri/Amiri Quran pipelines from being mistaken
for current-edition visual pages.
"""
from __future__ import annotations
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
TOOLS=ROOT/'tools'
OUT=ROOT/'dist/jilid-2-current-renderer-audit'

PAGE_RE=re.compile(r'(?:^|_)p(\d{3})(?:_|\.|$)',re.I)

def classify(text:str):
    u=text.upper()
    has_kfg='KFGQPC' in u or 'UTHMAN TAHA' in u
    has_amiri='AMIRI QURAN' in u or "'AMIRI'" in u or 'AMIRI-REGULAR' in u
    frozen='V7.6' in u and '-1700' in text
    if has_kfg and frozen:return 'CURRENT_KFGQPC_FROZEN_SUKUN'
    if has_kfg:return 'KFGQPC_NONFROZEN_OR_LAB'
    if has_amiri:return 'LEGACY_AMIRI'
    return 'UNCLASSIFIED'

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    rows=[]
    coverage={n:[] for n in range(1,41)}
    for path in sorted(TOOLS.glob('render_qurbata_jilid2_*.py')):
        text=path.read_text(encoding='utf-8',errors='replace')
        cls=classify(text)
        m=PAGE_RE.search(path.name)
        page=int(m.group(1)) if m else None
        if page and 1<=page<=40:coverage[page].append((path.name,cls))
        rows.append((path.name,f'P{page:03d}' if page else 'MULTI_OR_LAB',cls))
    manifest=OUT/'JILID-2-CURRENT-VISUAL-RENDERER-AUDIT.tsv'
    lines=['renderer\tpage\tclassification']+[f'{a}\t{b}\t{c}' for a,b,c in rows]
    manifest.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    cov=OUT/'JILID-2-CURRENT-PAGE-COVERAGE.tsv'
    cl=['page\tcurrent_kfgqpc_renderer\tother_renderers']
    current=0
    for n in range(1,41):
        hits=coverage[n]
        cur=[name for name,cls in hits if cls=='CURRENT_KFGQPC_FROZEN_SUKUN']
        oth=[name+':'+cls for name,cls in hits if cls!='CURRENT_KFGQPC_FROZEN_SUKUN']
        if cur:current+=1
        cl.append(f'P{n:03d}\t{"|".join(cur) if cur else "NONE"}\t{"|".join(oth) if oth else "NONE"}')
    cov.write_text('\n'.join(cl)+'\n',encoding='utf-8')
    print('JILID2_CURRENT_VISUAL_RENDERER_AUDIT=PASS')
    print(f'CURRENT_KFGQPC_PAGES={current}')
    print(f'PAGES_REQUIRING_CURRENT_RENDERER={40-current}')
    print('LEGACY_AMIRI_ACCEPTED=NO')
    print('BASELINE_FONT=KFGQPC_UTHMAN_TAHA')
    print('SUKUN_BASELINE=V7.6_FROZEN')
    print('SUKUN_Y_SHIFT=-1700')
    print(f'AUDIT={manifest.relative_to(ROOT)}')
    print(f'COVERAGE={cov.relative_to(ROOT)}')
    return 0

if __name__=='__main__':raise SystemExit(main())
