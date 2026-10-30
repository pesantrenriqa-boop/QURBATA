#!/usr/bin/env python3
"""Check that imported QJ8 source contains all 12 Saktah context ayat.
Structural verification ONLY. No Quran text is synthesized or print-approved.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
GATE=ROOT/"books/jilid-8/QJ8-SAKTAH-CONTEXT-GATE.json"

def verify(source_path, gate_path=GATE):
    data=json.loads(Path(source_path).read_text(encoding="utf-8"))
    gate=json.loads(Path(gate_path).read_text(encoding="utf-8"))
    refs=gate["required_verse_refs"]
    assert len(refs)==len(set(refs))==12, "Saktah context must have 12 unique ayat"
    assert gate["text_validation"]=="HOLD_NO_SOURCE", "Review status changed unexpectedly"
    sha=data.get("source_sha256")
    assert isinstance(sha,str) and re.fullmatch("[0-9a-f]{64}",sha), "Missing source checksum"
    assert data.get("source_id")=="TANZIL-UTHMANI-LOCAL-"+sha[:16], "Source ID mismatch"
    assert data.get("source_url")=="https://tanzil.net/pub/download/index.php"
    assert data.get("status")=="SOURCE_IMPORTED_NOT_TASHIH", "Unexpected print approval"
    verses=data.get("verses")
    assert isinstance(verses,dict), "Missing verse map"
    for ref in refs:
        verse=verses.get(ref)
        assert isinstance(verse,str) and verse and verse==verse.strip(), f"Missing/blank ayah {ref}"
        assert re.search(r"[\u0621-\u064a\u0671]",verse), f"Non-Arabic ayah {ref}"
    print("PASS: 12 unique Saktah context refs present in imported source JSON")
    print("HOLD: source metadata and Arabic-script checks do NOT prove Quran authenticity or tashih")

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--source",required=True)
    args=p.parse_args()
    verify(args.source)

if __name__=="__main__": main()
