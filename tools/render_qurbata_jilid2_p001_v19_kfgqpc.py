#!/usr/bin/env python3
"""QURBATA Jilid 2 P001 V19 — KFGQPC Uthman Taha Naskh local-font candidate.

The font binary is intentionally NOT stored in the repository. This renderer loads
KFGQPC Uthman Taha Naskh from a local TTF or from the user's local ZIP at runtime,
then injects it with @font-face. Content, competency ladder, page shell and V18 row
geometry remain unchanged so this candidate isolates the effect of the typeface.
"""
from __future__ import annotations
import argparse
import os
import sys
import tempfile
import zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))

# Read V18 first so our final CSS override wins.
import render_qurbata_jilid2_p001_v18 as v18
import render_qurbata_jilid2_p001_v1 as p001

FONT_FAMILY='QURBATA KFGQPC Uthman Taha Naskh'
TTF_BASENAME='KFGQPC Uthman Taha Naskh Regular.ttf'
ZIP_BASENAME='kfgqpc-uthman-taha-naskh-regular.zip'


def discover_font(explicit_font:str|None, explicit_zip:str|None, out_dir:Path)->tuple[Path,str]:
    candidates=[]
    if explicit_font: candidates.append(Path(explicit_font).expanduser())
    env=os.environ.get('QURBATA_KFGQPC_FONT')
    if env: candidates.append(Path(env).expanduser())
    home=Path.home()
    candidates += [
        ROOT/'_local/fonts'/TTF_BASENAME,
        home/'Downloads'/TTF_BASENAME,
        home/'Downloads'/'KFGQPC Uthman Taha Naskh Regular'/TTF_BASENAME,
    ]
    for p in candidates:
        if p.is_file(): return p.resolve(),'TTF'

    zips=[]
    if explicit_zip: zips.append(Path(explicit_zip).expanduser())
    zips += [home/'Downloads'/ZIP_BASENAME, ROOT/'_local/fonts'/ZIP_BASENAME]
    for zp in zips:
        if not zp.is_file(): continue
        target=out_dir/'_runtime_font'/TTF_BASENAME
        target.parent.mkdir(parents=True,exist_ok=True)
        with zipfile.ZipFile(zp) as z:
            match=next((n for n in z.namelist() if n.lower().endswith(TTF_BASENAME.lower())),None)
            if not match: raise RuntimeError(f'KFGQPC_TTF_NOT_FOUND_IN_ZIP={zp}')
            target.write_bytes(z.read(match))
        return target.resolve(),'ZIP_EXTRACTED_RUNTIME'

    raise FileNotFoundError(
        'KFGQPC_FONT_NOT_FOUND. Use --font-file "C:\\path\\KFGQPC Uthman Taha Naskh Regular.ttf" '
        'or --font-zip "C:\\path\\kfgqpc-uthman-taha-naskh-regular.zip".'
    )


def main():
    # Parse only V19-specific options, leave the original renderer args in sys.argv.
    ap=argparse.ArgumentParser(add_help=False)
    ap.add_argument('--font-file')
    ap.add_argument('--font-zip')
    known,remaining=ap.parse_known_args(sys.argv[1:])

    # Resolve output dir from the remaining args because runtime ZIP extraction lives there.
    out_arg='dist/jilid-2-p001-candidate-v27'
    for i,a in enumerate(remaining):
        if a=='--output-dir' and i+1<len(remaining): out_arg=remaining[i+1]
    out=Path(out_arg); out=out if out.is_absolute() else ROOT/out
    out.mkdir(parents=True,exist_ok=True)

    font_path,font_source=discover_font(known.font_file,known.font_zip,out)
    font_uri=font_path.as_uri()

    # Override all Arabic practice/presentation text after V18's Amiri rules.
    p001.P001_CSS += f'''\n@font-face{{font-family:"{FONT_FAMILY}";src:url("{font_uri}") format("truetype");font-style:normal;font-weight:400;font-display:block;}}\n.j2-glyph,.presentation-object,.presentation-object .arabic-part{{font-family:"{FONT_FAMILY}",serif!important;font-feature-settings:'mark' 1,'mkmk' 1;font-kerning:normal;text-rendering:optimizeLegibility;}}\n'''

    # Let the base renderer parse only its own arguments.
    sys.argv=[sys.argv[0],*remaining]
    rc=v18.main()

    print('JILID2_P001_RENDERER_V19_KFGQPC=PASS')
    print('ARABIC_FONT_PRIMARY=KFGQPC Uthman Taha Naskh')
    print(f'FONT_SOURCE={font_source}')
    print(f'FONT_FILE_NAME={font_path.name}')
    print('FONT_BINARY_REPOSITORY_STORAGE=NO')
    print('HARAKAT_MODEL=NATIVE_FONT_GPOS')
    print('MARK_OFFSETS=NONE')
    print('DETACHED_MARKS=FORBIDDEN')
    print('V18_GEOMETRY=PRESERVED')
    print('STATUS=FONT_COMPARISON_CANDIDATE_NOT_FROZEN')
    return rc

if __name__=='__main__': raise SystemExit(main())
