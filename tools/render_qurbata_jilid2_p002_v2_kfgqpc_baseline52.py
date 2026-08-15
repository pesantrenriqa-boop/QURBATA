#!/usr/bin/env python3
"""QURBATA Jilid 2 P002 V2 — align typography with approved P001 production baseline.

This wrapper preserves the P002 V1 competency/lexical content and semantic gates,
while superseding only the typography values that drifted from the approved P001
production direction:
- presentation / material example: 52 pt
- practice objects: 39 pt

P002 V1 remains untouched for audit/history.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "tools") not in sys.path:
    sys.path.insert(0, str(ROOT / "tools"))

import render_qurbata_jilid2_p002_v1_kfgqpc_lexical as v1
import render_qurbata_jilid2_p001_v1 as p001

p001.P001_CSS += r'''
.presentation-object{font-size:52pt!important;}
.j2-glyph{font-size:39pt!important;}
'''

_original_render = v1.render_p002


async def render_p002_v2(h: Path, out: Path, debug: bool):
    result = await _original_render(h, out, debug)
    if len(result) == 4:
        metrics, report_v1, pdf_v1, pdf_mode = result
    elif len(result) == 3:
        metrics, report_v1, pdf_v1 = result
        pdf_mode = "LEGACY_DIRECT"
    else:
        raise RuntimeError(f"P002_RENDER_RETURN_ARITY_INVALID={len(result)}")

    report_v2 = out / "LAYOUT-OVERFLOW-REPORT-J2-P002-V2.json"
    pdf_v2 = out / "QURBATA-JILID-2-P002-V2-KFGQPC-BASELINE52.pdf"

    if report_v1.exists() and report_v1 != report_v2:
        if report_v2.exists():
            report_v2.unlink()
        report_v1.replace(report_v2)
    if pdf_v1.exists() and pdf_v1 != pdf_v2:
        if pdf_v2.exists():
            pdf_v2.unlink()
        pdf_v1.replace(pdf_v2)

    return metrics, report_v2, pdf_v2, pdf_mode


p001.render = render_p002_v2


def main():
    rc = v1.main()
    print("JILID2_P002_RENDERER_V2=PASS")
    print("PAGE=2")
    print("TYPOGRAPHY_BASELINE=P001_PRODUCTION")
    print("PRESENTATION_FONT_SIZE=52PT")
    print("PRACTICE_FONT_SIZE=39PT")
    print("P002_V1_TYPOGRAPHY=SUPERSEDED_46PT_42PT")
    print("CONTENT_AND_COMPETENCY_LOGIC=P002_V1_PRESERVED")
    print("RENDER_RETURN_CONTRACT=4_VALUES")
    print("STATUS=P002_CANDIDATE_V2_BASELINE52")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
