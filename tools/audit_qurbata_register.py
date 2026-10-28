#!/usr/bin/env python3
"""Read-only QURBATA register audit. No auto-correction or Quran authentication."""
import argparse
import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

ROW = re.compile(r"^\| P(\d{3}) \|")
REF = re.compile(r"QS\s*\d+\s*:\s*\d+")
ARABIC_MARKS = re.compile(r"[\u064b-\u065f\u0670\u06d6-\u06ed]")
KNOWN_MISQUOTES = {
    ("P008", "QS 85:14", "إِنَّهُ هُوَ الْغَفُورُ الْوَدُودُ"),
    ("P007", "QS 22:16", "آيَاتِنَا بَيِّنَاتٍ"),
}
def normalize(text):
    return ARABIC_MARKS.sub("", unicodedata.normalize("NFC", text)).replace("ـ", "").strip()

def audit(path):
    warnings, counts = [], {"filled": 0, "empty": 0, "pages": 0}
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        match = ROW.match(line)
        if not match:
            continue
        page = "P" + match.group(1)
        page_no = int(match.group(1))
        fields = line.split(" | ")
        expected = 16 if page_no <= 20 else 8
        cells = fields[2:2 + expected]
        counts["pages"] += 1
        if len(cells) != expected:
            warnings.append({"page": page, "line": line_no, "type": "STRUCTURE", "detail": f"{len(cells)} of {expected} slots"})
        seen = defaultdict(list)
        for slot, cell in enumerate(cells, 1):
            if cell == "—":
                counts["empty"] += 1
                continue
            counts["filled"] += 1
            excerpt = cell.split(" [", 1)[0].strip()
            refs = REF.findall(cell)
            if not refs and page_no != 28 and page_no != 38:
                warnings.append({"page": page, "slot": slot, "type": "NO_QS_REFERENCE"})
            key = normalize(excerpt)
            seen[key].append(slot)
            for bad_page, bad_ref, bad_text in KNOWN_MISQUOTES:
                if page == bad_page and bad_ref in cell and normalize(bad_text) == key:
                    warnings.append({"page": page, "slot": slot, "type": "KNOWN_MISQUOTE"})
        for key, slots in seen.items():
            if len(slots) > 1:
                warnings.append({"page": page, "slots": slots, "type": "DUPLICATE_EXCERPT", "detail": key})
    counts["total"] = counts["filled"] + counts["empty"]
    return {"file": str(path), "counts": counts, "warnings": warnings, "note": "Heuristic warnings only. Verify Quran text against authoritative Uthmani mushaf and review tajwid manually."}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--fail-on-warnings", action="store_true")
    args = parser.parse_args()
    reports = [audit(p) for p in args.files]
    print(json.dumps(reports, ensure_ascii=False, indent=2))
    if args.fail_on_warnings and any(x["warnings"] for x in reports):
        raise SystemExit(1)

if __name__ == "__main__":
    main()
