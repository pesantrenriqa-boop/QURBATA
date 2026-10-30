#!/usr/bin/env python3
"""Download an UNMODIFIED Tanzil Uthmani source for manual QJ8 import.
No source file is committed automatically. Requires internet and explicit license acceptance.
"""
import argparse
import hashlib
import re
import urllib.parse
import urllib.request
from pathlib import Path
from qj8_validate_context_manifest import LENGTHS

URL = "https://tanzil.net/pub/download/index.php"


def validate_download(data):
    text = data.decode("utf-8-sig")
    lines = [line for line in text.splitlines() if line and not line.startswith("#")]
    if len(lines) != 6236:
        raise SystemExit(f"Unexpected verse count ({len(lines)}); nothing saved")
    expected = {f"{surah}|{ayah}" for surah, count in enumerate(LENGTHS, 1) for ayah in range(1, count + 1)}
    found = set()
    for line in lines:
        parts = line.split("|", 2)
        if len(parts) != 3 or not parts[2] or parts[2] != parts[2].strip():
            raise SystemExit("Malformed or whitespace-altered verse; nothing saved")
        if not re.search(r"[\u0621-\u064a\u0671]", parts[2]):
            raise SystemExit("Verse contains no Arabic letters; nothing saved")
        ref = parts[0] + "|" + parts[1]
        if ref in found:
            raise SystemExit(f"Duplicate source verse {ref}; nothing saved")
        found.add(ref)
    if found != expected:
        raise SystemExit("Source has noncanonical or missing Quran references; nothing saved")
    return len(lines)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True, help="New local source file; refuses overwrite")
    ap.add_argument("--accept-tanzil-terms", action="store_true")
    args = ap.parse_args()
    if not args.accept_tanzil_terms:
        ap.error("Read https://tanzil.net/pub/download/index.php and pass --accept-tanzil-terms")
    output = Path(args.output)
    if output.exists():
        ap.error("Refusing to overwrite existing Quran source")
    fields = {"quranType":"uthmani", "outType":"txt-2", "marks":"true",
              "sajdah":"true", "tatweel":"true", "agree":"true"}
    request = urllib.request.Request(URL, data=urllib.parse.urlencode(fields).encode(),
                                     headers={"User-Agent":"QURBATA-source-acquisition/1.0",
                                              "Content-Type":"application/x-www-form-urlencoded"})
    with urllib.request.urlopen(request, timeout=45) as response:
        if "text/html" in response.headers.get("Content-Type","").lower():
            raise SystemExit("Received HTML, not Quran text; nothing saved")
        data = response.read(4_000_001)
    if len(data) > 4_000_000:
        raise SystemExit("Unexpected oversized response; nothing saved")
    count = validate_download(data)
    output.parent.mkdir(parents=True,exist_ok=True)
    with output.open("xb") as destination:
        destination.write(data)
    if hashlib.sha256(output.read_bytes()).digest() != hashlib.sha256(data).digest():
        raise SystemExit("CRITICAL: saved source differs from downloaded bytes; stop")
    print(f"Downloaded {count} verses without modification: {output}")
    print(f"SHA256: {hashlib.sha256(data).hexdigest()}")
    print("HOLD: run qj8_import_tanzil_context.py and manual tashih before use.")

if __name__ == "__main__":
    main()
