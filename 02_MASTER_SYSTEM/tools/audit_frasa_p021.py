#!/usr/bin/env python3
"""Cari kandidat frasa Qurani P021 dari korpus Tanzil, tanpa mengubah teks mushaf.

Usage:
 python audit_frasa_p021.py path/to/quran-uthmani.txt --output kandidat-p021.tsv
Input: Tanzil plain text: surah|ayah|text; OR dotquran/corpus JSON (surahs[].ayahs[].text).
Status otomatis selalu CANDIDATE; tidak menggantikan tashih ahli.
"""
import argparse
import csv
import json
import re
from pathlib import Path

# Tanda tajwid Utsmani: gunakan larangan konservatif, bukan normalisasi diam-diam.
TASHDID = "\u0651"
MAD_MARKS = set("\u0653\u0654\u0655\u0670\u06e4\u06e5\u06e6")
LONG_LETTERS = set("اىآٱ")  # waw/ya checked contextually: allow layyin (ـَوْ / ـَيْ)
SUN = set("تثدذرزسشصضطظلن")
QALQALAH = set("قطبجد")
VOWELS = set("\u064e\u064f\u0650")
SUKUN = "\u0652"
ARABIC = re.compile(r"[\u0621-\u064a]")
STRIP = re.compile(r"[\u06d6-\u06ed\u06dd\u06de\u06e9\u0640]")
def words(text):
    return [x for x in STRIP.sub("", text).split() if ARABIC.search(x)]
def fail_reasons(ws):
    s=" ".join(ws)
    errors=[]
    if TASHDID in s: errors.append("tasydid")
    if any(x in s for x in MAD_MARKS): errors.append("tanda_mad")
    # Tolak seluruh huruf pemanjang (sangat konservatif; false rejection disengaja).
    if any(x in s for x in LONG_LETTERS): errors.append("potensi_mad_atau_alif_wasl")
    # Waw/ya sukun after fathah = layyin; other waw/ya remain conservative rejects.
    if re.search(r"(?<![َ])وْ|(?<![َ])يْ|[وي][َُِ]?", s) and not re.search(r"[َ][وي]ْ", s):
        errors.append("waw_ya_perlu_audit_mad")
    for w in ws:
        if re.search(r"ال["+ "".join(SUN) +r"]", re.sub(r"[\u064b-\u065f]","",w)):
            errors.append("potensi_al_syamsiyah")
        if any(q+SUKUN in w for q in QALQALAH): errors.append("sukun_qalqalah")
        # Semua tanda khusus yang belum didefinisikan dalam silabus perlu reviewer.
        if "\u0656" in w or "\u0657" in w or "\u0658" in w: errors.append("tanda_khusus")
    # Nun sukun/tanwin di batas kata memerlukan pemeriksaan hukum bacaan tersendiri.
    for a,b in zip(ws,ws[1:]):
        if a.endswith(("ن"+SUKUN,"\u064b","\u064c","\u064d")):
            errors.append("nun_sukun_tanwin_sambung")
        if a.endswith("م"+SUKUN): errors.append("mim_sukun_sambung")
    return sorted(set(errors))
def verses(path):
    if path.suffix.lower()==".json":
        obj=json.loads(path.read_text(encoding="utf-8-sig"))
        for s in obj["surahs"]:
            for a in s["ayahs"]:
                if int(a["number"])>0:
                    yield int(s["number"]),int(a["number"]),a["text"]
    else:
        for line in path.read_text(encoding="utf-8-sig").splitlines():
            p=line.split("|",2)
            if len(p)==3 and p[0].isdigit() and p[1].isdigit():
                yield int(p[0]),int(p[1]),p[2]
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("corpus",type=Path)
    ap.add_argument("--output",default="kandidat-p021.tsv")
    ap.add_argument("--limit",type=int,default=500)
    args=ap.parse_args()
    found=[]; seen=set(); checked=0; verse_count=0
    for surah,ayah,text in verses(args.corpus):
        verse_count+=1; ws=words(text)
        for n in (3,4,5):
            for i in range(len(ws)-n+1):
                checked+=1; seg=ws[i:i+n]
                reasons=fail_reasons(seg)
                if reasons: continue
                key=" ".join(seg)
                if key in seen: continue
                seen.add(key)
                found.append((surah,ayah,i+1,n,key,"CANDIDATE_NEEDS_MANUAL_TASHIH"))
                if len(found)>=args.limit: break
            if len(found)>=args.limit: break
        if len(found)>=args.limit: break
    with open(args.output,"w",encoding="utf-8",newline="") as f:
        w=csv.writer(f,delimiter="\t")
        w.writerow(["surah","ayah","start_word","word_count","exact_uthmani_text","status"])
        w.writerows(found)
    print(f"verses_checked={verse_count} windows_checked={checked} candidates={len(found)} output={args.output}")
    if verse_count != 6236:
        print(f"WARNING: corpus has {verse_count} verses; expected 6236. Inspect basmalah/format and coverage.")
    print("WARNING: conservative automatic filter; verify every phrase with qualified Quran reviewer before print.")
if __name__=="__main__": main()
