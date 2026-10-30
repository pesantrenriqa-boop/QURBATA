#!/usr/bin/env python3
"""Offline regression: validate downloader against synthetic, NEVER Quran, content."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from qj8_download_official_tanzil import validate_download
from qj8_validate_context_manifest import LENGTHS

def rejected(payload):
    try:
        validate_download(payload)
    except (SystemExit, ValueError, UnicodeError):
        return True
    return False

def main():
    lines=[f"{s}|{a}|تجربة_{s}_{a}" for s,n in enumerate(LENGTHS,1) for a in range(1,n+1)]
    assert len(lines)==6236
    assert validate_download(("\n".join(lines)+"\n").encode())==6236
    corrupted=lines.copy()
    corrupted[0]="1|8|تجربة_BAD"
    assert rejected(("\n".join(corrupted)+"\n").encode())
    duplicate=lines.copy()
    duplicate[0]=duplicate[1]
    assert rejected(("\n".join(duplicate)+"\n").encode())
    assert rejected(b"<html>not Quran</html>")
    no_arabic=lines.copy()
    no_arabic[0]="1|1|NOT_ARABIC"
    assert rejected(("\\n".join(no_arabic)+"\\n").encode())
    print("PASS: 6236 canonical synthetic refs accepted; wrong ref, duplicate and HTML rejected")
    print("HOLD: no authentic Quran text downloaded or validated")

if __name__=="__main__":
    main()
