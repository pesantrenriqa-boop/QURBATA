#!/usr/bin/env python3
"""QURBATA: index a user-supplied, authorized full Quran corpus.
Input: UTF-8 TSV with columns surah, ayah, token_index, uthmani.
Never reconstruct printed Uthmani text from normalized search strings.
No network calls; no external dependencies. Output is CANDIDATE only.
"""
import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ARABIC_MARKS = re.compile(r"[\u064b-\u065f\u0670\u06d6-\u06ed]")
FATHATAN, DAMMATAN, KASRATAN = "\u064b", "\u064c", "\u064d"
FATHA, DAMMA, KASRA = "\u064e", "\u064f", "\u0650"

def features(word):
    # Heuristic search hints, NOT a tajwid ruling or mushaf verification.
    out = set()
    for mark, tag in [(FATHATAN, "tanwin_fath"), (KASRATAN, "tanwin_kasr"), (DAMMATAN, "tanwin_damm")]:
        if mark in word: out.add(tag)
    if re.search(FATHA + r"ا", word): out.add("mad_alif_candidate")
    if re.search(KASRA + r"ي", word): out.add("mad_ya_candidate")
    if re.search(DAMMA + r"و", word): out.add("mad_waw_candidate")
    if "\u0651" in word: out.add("shadda")
    if "\u0652" in word: out.add("sukun")
    return sorted(out)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input_tsv", type=Path)
    ap.add_argument("output_dir", type=Path)
    args = ap.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    seen = set()
    with args.input_tsv.open(encoding="utf-8-sig", newline="") as f:
        rd = csv.DictReader(f, delimiter="\t")
        required = {"surah", "ayah", "token_index", "uthmani"}
        if not required.issubset(rd.fieldnames or []):
            raise SystemExit("TSV requires surah, ayah, token_index, uthmani")
        for line, row in enumerate(rd, start=2):
            try:
                surah, ayah, token = (int(row[k]) for k in ("surah", "ayah", "token_index"))
            except (ValueError, TypeError):
                raise SystemExit(f"Invalid location on line {line}")
            word = row["uthmani"].strip()
            if not (1 <= surah <= 114 and ayah >= 1 and token >= 1 and word):
                raise SystemExit(f"Invalid token on line {line}")
            key = (surah, ayah, token)
            if key in seen: raise SystemExit(f"Duplicate location {key}")
            seen.add(key)
            rows.append({"surah": surah, "ayah": ayah, "token_index": token,
                         "exact_uthmani": word, "features": features(word),
                         "verification_status": "AUTO-CANDIDATE"})
    by_feature = defaultdict(list)
    for row in rows:
        for feature in row["features"]:
            by_feature[feature].append(row)
    for feature, matches in by_feature.items():
        with (args.output_dir / f"{feature}.jsonl").open("w", encoding="utf-8") as out:
            for item in matches:
                out.write(json.dumps(item, ensure_ascii=False) + "\n")
    report = {
        "status": "AUTO-CANDIDATE / NOT FOR PRINT",
        "surahs_seen": len({r["surah"] for r in rows}),
        "surah_coverage_complete": len({r["surah"] for r in rows}) == 114,
        "token_occurrences": len(rows),
        "distinct_exact_forms": len({r["exact_uthmani"] for r in rows}),
        "candidate_counts": dict(sorted((k, len(v)) for k, v in by_feature.items())),
        "warning": "Feature detection is heuristic; all entries require expert tashih."
    }
    (args.output_dir / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
