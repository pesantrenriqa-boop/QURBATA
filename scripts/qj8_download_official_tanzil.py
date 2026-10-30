#!/usr/bin/env python3
"""Download an UNMODIFIED Tanzil Uthmani source for manual QJ8 import.
No source file is committed automatically. Requires internet and explicit license acceptance.
"""
import argparse
import hashlib
import urllib.parse
import urllib.request
from pathlib import Path

URL = "https://tanzil.net/pub/download/index.php"

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
    text = data.decode("utf-8-sig")
    lines = [line for line in text.splitlines() if line and not line.startswith("#")]
    if len(lines) != 6236 or not all(line.count("|") >= 2 for line in lines):
        raise SystemExit(f"Unexpected download format/count ({len(lines)}); nothing saved")
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_bytes(data)
    print(f"Downloaded {len(lines)} verses without modification: {output}")
    print(f"SHA256: {hashlib.sha256(data).hexdigest()}")
    print("HOLD: run qj8_import_tanzil_context.py and manual tashih before use.")

if __name__ == "__main__":
    main()
