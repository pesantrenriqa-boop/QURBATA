#!/usr/bin/env python3
"""QURBATA Jilid 2 P004 V3 — cumulative page with bottom-row micro-enrichment.

Adds a compact Kapsul Murojaah to P004 without changing the 32 core lexical
objects or the 52/39 pt production typography. P004 is the first cumulative
transfer page, so enrichment is limited to already-safe symbolic/writing recall:
E01 letter names, E02 Arabic-Indic numerals, and E06 non-joining letters.
"""
from __future__ import annotations
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p004_v2_kfgqpc_baseline52 as v2
import render_qurbata_jilid2_p001_v1 as p001

DEFAULT_P004_OUTPUT='dist/qurbata-print-ready/jilid-2/pages/P004'

# Compact bottom-row capsule. Core typography remains untouched.
p001.P001_CSS += r'''
.cumulative-enrichment{margin-top:1.2mm;border-top:.35mm solid #111;padding-top:1.4mm;display:grid;grid-template-columns:1fr 1fr 1fr;gap:1.4mm;direction:ltr}
.cumulative-enrichment .micro{min-height:10mm;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;line-height:1.05}
.cumulative-enrichment .micro-label{font-family:Arial,sans-serif;font-size:6.5pt;font-weight:700;letter-spacing:.15pt;margin-bottom:.8mm}
.cumulative-enrichment .micro-ar{font-family:'KFGQPC Uthman Taha Naskh','Amiri Quran','Amiri',serif;font-size:17pt;direction:rtl;white-space:nowrap}
.cumulative-enrichment .micro-num{font-family:'KFGQPC Uthman Taha Naskh','Amiri Quran','Amiri',serif;font-size:18pt;direction:rtl;white-space:nowrap}
'''

_original_build=p001.build_page_html

def build_p004_v3(debug:bool):
    h=_original_build(debug)
    capsule='''<section class="cumulative-enrichment" aria-label="Kapsul Murojaah">
      <div class="micro"><div class="micro-label">NAMA HURUF</div><div class="micro-ar" lang="ar">بَاءٌ · تَاءٌ · ثَاءٌ · جِيمٌ · حَاءٌ · خَاءٌ · سِينٌ · شِينٌ</div></div>
      <div class="micro"><div class="micro-label">ANGKA ARAB</div><div class="micro-num" lang="ar">٠ · ١ · ٢ · ٣ · ٤ · ٥ · ٦ · ٧ · ٨ · ٩</div></div>
      <div class="micro"><div class="micro-label">PEMUTUS SAMBUNGAN</div><div class="micro-ar" lang="ar">ا · د · ذ · ر · ز · و</div></div>
    </section>'''
    # Insert immediately before the existing footer so it becomes the lowest
    # instructional row while the absolute footer/slogan remains preserved.
    candidates=['<footer', '<div class="footer', '<section class="footer']
    positions=[h.find(x) for x in candidates if h.find(x)>=0]
    if not positions:
        raise RuntimeError('P004_V3_FOOTER_ANCHOR_NOT_FOUND')
    pos=min(positions)
    return h[:pos]+capsule+h[pos:]

p001.build_page_html=build_p004_v3

def main():
    if '--output-dir' not in sys.argv[1:]:
        sys.argv.extend(['--output-dir',DEFAULT_P004_OUTPUT])
    rc=v2.main()
    print('JILID2_P004_RENDERER_V3_CUMULATIVE_ENRICHMENT=PASS')
    print('PAGE=4')
    print('CUMULATIVE_ENRICHMENT=TRUE')
    print('ENRICHMENT_CATEGORY=E01|E02|E06')
    print('ENRICHMENT_ITEM=LETTER_NAMES|ARABIC_INDIC_NUMERALS_0_9|NON_JOINERS')
    print('ENRICHMENT_PREREQUISITE=P001_P003_ACQUIRED_SYMBOL_SET')
    print('ENRICHMENT_STATUS=ACTIVE_CANDIDATE')
    print('CORE_PRACTICE_OBJECTS=32_UNCHANGED')
    print('PRESENTATION_FONT_SIZE=52PT')
    print('PRACTICE_FONT_SIZE=39PT')
    print('OUTPUT_DIR='+DEFAULT_P004_OUTPUT)
    print('STATUS=P004_CUMULATIVE_ENRICHMENT_CANDIDATE')
    return rc

if __name__=='__main__': raise SystemExit(main())
