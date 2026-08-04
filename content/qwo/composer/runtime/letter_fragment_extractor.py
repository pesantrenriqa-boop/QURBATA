#!/usr/bin/env python3
"""Extract launch-focused LETTER and WORD_FRAGMENT objects from Tanzil Uthmani text.

Input line: surah|ayah|text
Outputs:
- MASTER_LETTER.csv
- MASTER_WORD_FRAGMENT.csv

Every object preserves a Quran source reference. Exact Arabic objects are unique.
"""
from __future__ import annotations
import argparse, csv, re, unicodedata
from collections import Counter
from pathlib import Path

ARABIC_BASE = re.compile(r"[\u0621-\u063A\u0641-\u064A\u0671]")
ALLOWED_J1_MARKS = {"\u064e", "\u064f", "\u0650"}  # fathah, dhammah, kasrah
ANNOTATION_RANGES = ((0x06D6, 0x06ED), (0x08D4, 0x08FF))


def is_annotation(ch: str) -> bool:
    cp = ord(ch)
    return any(a <= cp <= b for a, b in ANNOTATION_RANGES) or ch in "۞۩۝"


def graphemes(word: str) -> list[str]:
    result: list[str] = []
    for ch in unicodedata.normalize("NFC", word):
        if is_annotation(ch):
            continue
        if unicodedata.combining(ch):
            if result:
                result[-1] += ch
        elif ARABIC_BASE.fullmatch(ch):
            result.append(ch)
    return result


def j1_safe(fragment: str) -> bool:
    return all(not unicodedata.combining(ch) or ch in ALLOWED_J1_MARKS for ch in fragment)


def parse(path: Path):
    for line in path.read_text(encoding="utf-8").splitlines():
        parts = line.split("|", 2)
        if len(parts) == 3 and parts[0].isdigit() and parts[1].isdigit():
            yield int(parts[0]), int(parts[1]), parts[2]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("--out", required=True)
    ap.add_argument("--fragment-limit", type=int, default=1200)
    args = ap.parse_args()
    out = Path(args.out); out.mkdir(parents=True, exist_ok=True)

    first_letter = {}
    first_fragment = {}
    counts = Counter()

    for surah, ayah, text in parse(Path(args.input)):
        for token_index, word in enumerate(text.split(), 1):
            gs = graphemes(word)
            for g in gs:
                base = "".join(ch for ch in g if not unicodedata.combining(ch))
                first_letter.setdefault(base, (surah, ayah, token_index, word))
            for size in (2, 3):
                for i in range(len(gs) - size + 1):
                    frag = unicodedata.normalize("NFC", "".join(gs[i:i+size]))
                    if not j1_safe(frag):
                        continue
                    counts[frag] += 1
                    first_fragment.setdefault(frag, (surah, ayah, token_index, word, size))

    with (out / "MASTER_LETTER.csv").open("w", encoding="utf-8", newline="") as f:
        fields = ["ObjectID","ArabicObject","SourceRef","TokenIndex","SourceWord","CompetencyID","Status"]
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader()
        for i, letter in enumerate(sorted(first_letter), 1):
            s,a,t,word = first_letter[letter]
            w.writerow({"ObjectID":f"QLT-{i:03d}","ArabicObject":letter,"SourceRef":f"{s}:{a}","TokenIndex":t,"SourceWord":word,"CompetencyID":"C0001","Status":"CANDIDATE"})

    ranked = sorted(counts, key=lambda x: (-counts[x], len(graphemes(x)), x))[:args.fragment_limit]
    with (out / "MASTER_WORD_FRAGMENT.csv").open("w", encoding="utf-8", newline="") as f:
        fields = ["ObjectID","ArabicObject","FragmentLength","SourceRef","TokenIndex","SourceWord","OccurrenceCount","PrimaryCompetencyID","Status"]
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader()
        for i, frag in enumerate(ranked, 1):
            s,a,t,word,size = first_fragment[frag]
            competency = "C0005" if size == 2 else "C0007"
            w.writerow({"ObjectID":f"QFR-{i:05d}","ArabicObject":frag,"FragmentLength":size,"SourceRef":f"{s}:{a}","TokenIndex":t,"SourceWord":word,"OccurrenceCount":counts[frag],"PrimaryCompetencyID":competency,"Status":"CANDIDATE"})

if __name__ == "__main__":
    main()
