#!/usr/bin/env python3
"""Jilid 2 foundation renderer v2.

Thin controlled wrapper over v1. The successful Jilid 1/Jilid 2 layout geometry is
left unchanged; only the Arabic font policy is promoted to Amiri Quran first,
with Amiri and Noto Naskh Arabic as fallbacks when the local system does not
provide the requested family.
"""
from __future__ import annotations

import render_qurbata_jilid2_foundation_v1 as base

# Do not change grid geometry here. Font-only refinement.
base.FONT_FAMILY = 'Amiri Quran'
base.CSS = base.CSS.replace(
    "font-family:'Amiri','Noto Naskh Arabic',serif",
    "font-family:'Amiri Quran','Amiri','Noto Naskh Arabic',serif",
)


def main() -> int:
    rc = base.main()
    print('ARABIC_FONT_PRIMARY=Amiri Quran')
    print('ARABIC_FONT_FALLBACK=Amiri|Noto Naskh Arabic|serif')
    print('JILID2_FOUNDATION_RENDERER_V2=PASS' if rc == 0 else 'JILID2_FOUNDATION_RENDERER_V2=FAIL')
    return rc


if __name__ == '__main__':
    raise SystemExit(main())
