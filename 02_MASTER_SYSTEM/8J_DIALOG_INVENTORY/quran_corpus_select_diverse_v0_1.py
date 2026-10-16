#!/usr/bin/env python3
"""Select diverse *candidates* from a QURBATA feature JSONL, not print-ready text.
Usage: python quran_corpus_select_diverse_v0_1.py candidates.jsonl out.json --limit 20
"""
import argparse
import json
from collections import Counter
from pathlib import Path

def select_diverse(rows, limit):
    """Greedy coverage of distinct surface forms and surahs; deterministic."""
    remaining = sorted(rows, key=lambda r: (int(r["surah"]), int(r["ayah"]), int(r["token_index"])))
    chosen, forms, surahs = [], set(), set()
    while remaining and len(chosen) < limit:
        def score(r):
            return (int(r["exact_uthmani"] not in forms) * 10 +
                    int(r["surah"] not in surahs) * 4 -
                    sum(c["exact_uthmani"] == r["exact_uthmani"] for c in chosen) * 20)
        best = max(range(len(remaining)), key=lambda i: score(remaining[i]))
        row = remaining.pop(best)
        if row["exact_uthmani"] in forms:
            continue  # no duplicate surface forms in initial candidate set
        chosen.append(row)
        forms.add(row["exact_uthmani"])
        surahs.add(row["surah"])
    return chosen

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input_jsonl", type=Path)
    ap.add_argument("output_json", type=Path)
    ap.add_argument("--limit", type=int, default=20)
    args = ap.parse_args()
    if args.limit < 1:
        ap.error("--limit must be positive")
    rows = [json.loads(line) for line in args.input_jsonl.read_text(encoding="utf-8").splitlines() if line.strip()]
    selected = select_diverse(rows, args.limit)
    result = {
        "status": "AUTO-CANDIDATE / NOT FOR PRINT",
        "input_candidates": len(rows),
        "selected_candidates": len(selected),
        "distinct_surahs": len({r["surah"] for r in selected}),
        "selection": selected,
        "warning": "Diversity does not prove rasm correctness or pedagogical suitability."
    }
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Selected {len(selected)} of {len(rows)} candidates")

if __name__ == "__main__":
    main()
