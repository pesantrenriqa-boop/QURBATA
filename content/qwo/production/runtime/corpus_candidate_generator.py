#!/usr/bin/env python3
"""Generate QURBATA candidate objects from a verified Quran corpus.

Accepted corpus CSV columns (aliases supported):
- surah | sura | chapter
- ayah | aya | verse
- text | uthmani | arabic

Outputs a canonical CSV containing QWO, QPO, AYAH_FRAGMENT and FULL_AYAH
objects. The script never fabricates source text. If no readable corpus exists it
exits with CORPUS_NOT_FOUND.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DEFAULT_CORPUS_CANDIDATES = (
    ROOT / "content/qwo/corpus/QURAN-CORPUS-VERIFIED.csv",
    ROOT / "content/qwo/corpus/quran-uthmani.csv",
    ROOT / "data/quran-uthmani.csv",
    ROOT / "corpus/quran-uthmani.csv",
)
ARABIC_RE = re.compile(r"[\u0600-\u06ff]")


def pick(row: dict[str, str], names: tuple[str, ...]) -> str:
    normalized = {k.strip().lower(): (v or "").strip() for k, v in row.items()}
    for name in names:
        if normalized.get(name):
            return normalized[name]
    return ""


def find_corpus(explicit: str | None) -> Path:
    candidates = [Path(explicit)] if explicit else list(DEFAULT_CORPUS_CANDIDATES)
    for path in candidates:
        path = path if path.is_absolute() else ROOT / path
        if path.is_file() and path.stat().st_size > 0:
            return path
    searched = ", ".join(str(p) for p in candidates)
    raise FileNotFoundError(f"CORPUS_NOT_FOUND searched={searched}")


def read_ayahs(path: Path) -> list[tuple[str, str, str]]:
    rows: list[tuple[str, str, str]] = []
    with path.open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            surah = pick(row, ("surah", "sura", "chapter"))
            ayah = pick(row, ("ayah", "aya", "verse"))
            text = pick(row, ("text", "uthmani", "arabic"))
            if not surah or not ayah or not text or not ARABIC_RE.search(text):
                continue
            rows.append((surah, ayah, " ".join(text.split())))
    if len(rows) < 6000:
        raise ValueError(f"CORPUS_INCOMPLETE valid_ayah_rows={len(rows)} expected_at_least=6000")
    return rows


def canonical_key(object_type: str, text: str) -> str:
    raw = f"{object_type}|{' '.join(text.split())}".encode("utf-8")
    return hashlib.sha256(raw).hexdigest()[:20]


def add(out: dict[str, dict[str, str]], object_type: str, text: str, source: str) -> None:
    text = " ".join(text.split())
    if not text or not ARABIC_RE.search(text):
        return
    key = canonical_key(object_type, text)
    out.setdefault(key, {
        "CanonicalKey": key,
        "ObjectType": object_type,
        "Text": text,
        "SourceRef": source,
        "WordCount": str(len(text.split())),
    })


def generate(ayahs: list[tuple[str, str, str]]) -> list[dict[str, str]]:
    objects: dict[str, dict[str, str]] = {}
    for surah, ayah, text in ayahs:
        source = f"{surah}:{ayah}"
        words = text.split()
        for word in words:
            add(objects, "QWO", word, source)
        for size in (2, 3, 4):
            for i in range(0, max(0, len(words) - size + 1)):
                add(objects, "QPO", " ".join(words[i:i + size]), source)
        for size in range(4, min(15, len(words)) + 1):
            for i in range(0, len(words) - size + 1):
                add(objects, "AYAH_FRAGMENT", " ".join(words[i:i + size]), source)
        add(objects, "FULL_AYAH", text, source)
    return sorted(objects.values(), key=lambda row: (row["ObjectType"], row["CanonicalKey"]))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--corpus")
    parser.add_argument("--output", default="content/qwo/production/generated/MASTER-QURAN-OBJECTS-V1.csv")
    args = parser.parse_args()
    try:
        corpus = find_corpus(args.corpus)
        ayahs = read_ayahs(corpus)
    except (FileNotFoundError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 2

    objects = generate(ayahs)
    output = Path(args.output)
    output = output if output.is_absolute() else ROOT / output
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["CanonicalKey", "ObjectType", "Text", "SourceRef", "WordCount"])
        writer.writeheader()
        writer.writerows(objects)
    print(f"CORPUS={corpus}")
    print(f"AYAH_ROWS={len(ayahs)}")
    print(f"OBJECTS={len(objects)}")
    print(f"OUTPUT={output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
