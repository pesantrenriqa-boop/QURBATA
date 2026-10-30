#!/usr/bin/env python3
"""Import locally downloaded Tanzil Uthmani TXT (surah|ayah|text) into QJ8 context JSON.
Offline and fail-closed: NEVER change Quran text or silently drop source verses.
Download yourself from https://tanzil.net/pub/download/index.php, selecting
Uthmani, TXT with verse references and pause marks; retain source license.
"""
import argparse
import csv
import hashlib
import json
import re
from pathlib import Path

from qj8_validate_context_manifest import LENGTHS

LINE = re.compile(r"^(\d{1,3})\|(\d{1,3})\|(.+)$")
REF = re.compile(r"^\d{1,3}:\d+$")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tanzil", required=True, help="Local official Tanzil TXT file")
    ap.add_argument("--manifest", default="books/jilid-8/QJ8-MANIFEST-KONTEKS-AYAT-2026-10-29.csv")
    ap.add_argument("--output", required=True, help="Write selected verses JSON; never overwrite Quran source")
    args = ap.parse_args()
    raw = Path(args.tanzil).read_bytes()
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError as e:
        raise SystemExit(f"Invalid UTF-8: {e}")
    verses = {}
    for n, line in enumerate(text.splitlines(), 1):
        if not line or line.startswith("#"):
            continue
        match = LINE.fullmatch(line)
        if not match:
            raise SystemExit(f"Unknown source format on line {n}; stop rather than modify: {line[:70]}")
        if match[1] != str(int(match[1])) or match[2] != str(int(match[2])):
            raise SystemExit(f"Noncanonical source numbering on line {n}")
        key = f"{int(match[1])}:{int(match[2])}"
        if key in verses:
            raise SystemExit(f"Duplicate source verse {key}")
        if not re.search(r"[\u0621-\u064a\u0671]", match[3]):
            raise SystemExit(f"Source verse {key} has no Arabic letters; stop import")
        verses[key] = match[3]  # verbatim; no normalization or diacritic removal
    if len(verses) != 6236:
        raise SystemExit(f"Expected 6236 verses; found {len(verses)}. Wrong edition/format?")
    expected = {f"{s}:{a}" for s, count in enumerate(LENGTHS, 1) for a in range(1, count + 1)}
    if set(verses) != expected:
        missing = sorted(expected - set(verses))
        extra = sorted(set(verses) - expected)
        raise SystemExit(f"Noncanonical source reference coverage: missing={missing[:8]}, extra={extra[:8]}")
    if any(not verse or verse != verse.strip() or "\\r" in verse or "\\n" in verse for verse in verses.values()):
        raise SystemExit("Whitespace anomaly in source verse; stop rather than silently modify")
    with Path(args.manifest).open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    required = {"before_reference", "target_verse_references", "after_reference"}
    if not rows or not required.issubset(rows[0]):
        raise SystemExit("Manifest missing required columns")
    refs = set()
    for row in rows:
        for ref in [row["before_reference"], *row["target_verse_references"].split(";"), row["after_reference"]]:
            if ref == "N/A":
                continue
            if not REF.fullmatch(ref):
                raise SystemExit(f"Bad reference: {ref}")
            refs.add(ref)
    missing = sorted(refs - verses.keys())
    if missing:
        raise SystemExit(f"Missing source verses: {missing}")
    out = {
        "source_id": "TANZIL-UTHMANI-LOCAL-" + hashlib.sha256(raw).hexdigest()[:16],
        "source_url": "https://tanzil.net/pub/download/index.php",
        "source_sha256": hashlib.sha256(raw).hexdigest(),
        "license": "Tanzil Quran Text CC BY 3.0; source attribution and unchanged verse text required",
        "status": "SOURCE_IMPORTED_NOT_TASHIH",
        "verses": {ref: verses[ref] for ref in sorted(refs, key=lambda k:tuple(map(int,k.split(":"))))}
    }
    target = Path(args.output)
    if target.exists():
        raise SystemExit(f"Output exists; refusing overwrite: {target}")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Imported {len(out['verses'])} distinct source verses for {len(rows)} manifest cases.")
    print("All texts are unmodified. HOLD until Gharib target and recitation review.")

if __name__ == "__main__":
    main()
