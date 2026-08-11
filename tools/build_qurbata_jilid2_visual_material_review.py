#!/usr/bin/env python3
"""QURBATA Jilid 2 visual-material audit gate.

IMPORTANT: the old P001-P020 foundation renderer is Amiri/Amiri Quran and is LEGACY.
It must not be presented as the current QURBATA visual review after the project moved
to KFGQPC Uthman Taha. This gate deliberately refuses to render that legacy PDF.

Current visual baseline:
- Arabic base letters: KFGQPC Uthman Taha
- sukun: frozen V7.6, U+0652 positioning with Amiri U+06E1 outline, Y=-1700
- legacy Amiri foundation PDF: rejected

Use this audit before building a full current-edition visual PDF. A new KFGQPC renderer
must be bound to the current page/material dataset first.
"""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'dist/jilid-2-visual-material-review'

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    manifest=OUT/'JILID-2-CURRENT-VISUAL-BASELINE.txt'
    manifest.write_text(
        'STATUS=BLOCK_LEGACY_VISUAL_REVIEW\n'
        'LEGACY_RENDERER=tools/render_qurbata_jilid2_foundation_v3.py\n'
        'LEGACY_FONT=AMIRI_QURAN\n'
        'CURRENT_BASE_FONT=KFGQPC_UTHMAN_TAHA\n'
        'SUKUN_BASELINE=V7.6_FROZEN\n'
        'SUKUN_Y_SHIFT=-1700\n'
        'ACTION=BUILD_NEW_KFGQPC_CURRENT_EDITION_RENDERER\n',encoding='utf-8')
    print('JILID2_VISUAL_MATERIAL_REVIEW=BLOCKED_LEGACY')
    print('REASON=FOUNDATION_V3_USES_AMIRI_QURAN_NOT_CURRENT_KFGQPC_UTHMAN_TAHA')
    print('CURRENT_BASE_FONT=KFGQPC_UTHMAN_TAHA')
    print('SUKUN_BASELINE=V7.6_FROZEN')
    print('SUKUN_Y_SHIFT=-1700')
    print('NEXT=RENDER_CURRENT_EDITION_FROM_KFGQPC_PIPELINE')
    print(f'MANIFEST={manifest.relative_to(ROOT)}')
    return 2
if __name__=='__main__':raise SystemExit(main())
