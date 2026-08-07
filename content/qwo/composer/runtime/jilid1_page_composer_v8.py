#!/usr/bin/env python3
"""QURBATA Jilid 1 Composer v8 — revised 1+4+12 page composition.

Reading-page contract:
- Row 1 is current-material focus.
- Row 2: 4 x L2 using ONLY the exact bases shown in Row 1.
- Rows 3-6: 12 x L3, with page 2+ distribution 4 CURRENT + 8 REVIEW.
- Letter introduction follows standard hijaiyah order ا..ي.
- Visual reading order is authored first-to-last for RTL rendering.
- Canonical ه remains metadata; display uses a two-eye heh presentation glyph.
"""
from __future__ import annotations
import argparse, csv
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[4]
PROGRESSION = ROOT / "content/qwo/lpe/JILID-1-PEDAGOGICAL-PROGRESSION-V5.csv"
CRE = ROOT / "content/qwo/registry/JILID-1-PAGE-CONTENT-REGISTRY-V2.csv"
LETTER_NAMES = ROOT / "content/qwo/lpe/JILID-1-LETTER-NAME-REGISTRY-V1.csv"
DEFAULT_OUTPUT = ROOT / "content/qwo/composer/output/jilid-1-v8-composition-v5"
SPECIAL = {20, 40}
MARKS = {"FATHAH":"َ", "KASRAH":"ِ", "DHAMMAH":"ُ"}
HIJAIYAH = tuple("ابتثجحخدذرزسشصضطظعغفقكلمنهوي")
STAGE_READING_PAGES = {
    "KASRAH": (16,17,18,19,21,22,23,24,25),
    "DHAMMAH": (26,27,28,29,30,31,32,33,34,35,36),
    "MIXED": (37,38,39),
}

def read_csv(path: Path) -> list[dict[str,str]]:
    with path.open(encoding="utf-8-sig", newline="") as h: return list(csv.DictReader(h))

def write_csv(path: Path, rows: list[dict[str,Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as h:
        w=csv.DictWriter(h, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

def uniq(text: str) -> tuple[str,...]: return tuple(dict.fromkeys(text))

def display_base(base: str) -> str:
    # U+FEEB: initial-form presentation of canonical ه; visually the requested two-eye heh.
    return "ﻫ" if base == "ه" else base

def mark_for(stage: str, page: int, seq: int, unit: int) -> str:
    if stage in MARKS: return MARKS[stage]
    if stage == "MIXED": return ("َ","ِ","ُ")[(page+seq+unit)%3]
    raise ValueError(f"UNSUPPORTED_STAGE {stage}")

def review_stage_for(stage: str, index: int) -> str:
    if stage == "FATHAH": return "FATHAH"
    if stage == "KASRAH": return "FATHAH"
    if stage == "DHAMMAH": return ("FATHAH","KASRAH")[index%2]
    if stage == "MIXED": return ("FATHAH","KASRAH","DHAMMAH")[index%3]
    raise ValueError(stage)

def structural(pool: tuple[str,...], length: int, limit: int, seed: int, allow_adjacent_repeat: bool=False) -> list[tuple[str,...]]:
    if not pool: return []
    n=len(pool); seen=set(); out=[]
    patterns = [(0,1)] if length==2 else [(0,1,2),(0,2,1),(0,1,3),(0,2,3),(0,3,1)]
    for round_no in range(max(4,n+1)):
        for start in range(n):
            p=patterns[(round_no+seed+start)%len(patterns)]
            combo=tuple(pool[(start+d+round_no)%n] for d in p)
            if not allow_adjacent_repeat and any(combo[i]==combo[i+1] for i in range(len(combo)-1)): continue
            if combo in seen: continue
            seen.add(combo); out.append(combo)
            if len(out)>=limit: return out
    if allow_adjacent_repeat and len(pool)==1:
        return [tuple(pool[0] for _ in range(length)) for _ in range(limit)]
    if not out: raise ValueError(f"SEQUENCE_POOL_EMPTY length={length} pool={''.join(pool)}")
    while len(out)<limit: out.append(out[len(out)%len(out)])
    return out[:limit]

def current_triples(active: tuple[str,...], focus: tuple[str,...], limit: int, seed: int) -> list[tuple[str,...]]:
    """CURRENT triples must contain at least one focus/current-material base."""
    focus_set=set(focus); candidates=structural(active,3,max(limit*8,len(active)*5),seed=seed)
    out=[c for c in candidates if any(ch in focus_set for ch in c)]
    if len(out)<limit:
        # Deterministic fallback: place a focus base first, then two active review bases.
        seen=set(out)
        for f in focus:
            for a in active:
                for b in active:
                    c=(f,a,b)
                    if a==b or f==a or c in seen: continue
                    seen.add(c); out.append(c)
                    if len(out)>=limit:return out
    if len(out)<limit: raise ValueError(f"CURRENT_TRIPLE_POOL_SHORT focus={''.join(focus)}")
    return out[:limit]

def units_for(combo: tuple[str,...], stage: str, page: int, seq: int) -> tuple[str,...]:
    return tuple(display_base(base)+mark_for(stage,page,seq,i) for i,base in enumerate(combo))

def ordered_stage_focus(active: tuple[str,...], stage: str, page: int) -> tuple[str,...]:
    """Choose a small contiguous focus group in standard hijaiyah order."""
    pages=STAGE_READING_PAGES[stage]
    idx=pages.index(page)
    if stage in {"KASRAH","DHAMMAH"}:
        # Progress sequentially through ا..ي; use 2-4 letters so Row 1 remains spacious.
        q,r=divmod(len(active),len(pages))
        sizes=[q+(1 if i<r else 0) for i in range(len(pages))]
        start=sum(sizes[:idx]); size=sizes[idx]
        return tuple(active[start:start+size])
    # MIXED is review, not a new alphabet pass: use compact sequential windows.
    start=(idx*3)%len(active)
    return tuple(active[(start+i)%len(active)] for i in range(3))

def material_focus(active: tuple[str,...], new: tuple[str,...], stage: str, page: int) -> tuple[str,list[str],tuple[str,...]]:
    focus=new if new else ordered_stage_focus(active,stage,page)
    tokens=[display_base(base)+mark_for(stage,page,i,0) for i,base in enumerate(focus)]
    if new: label="Huruf baru"
    else: label={"KASRAH":"Kasrah","DHAMMAH":"Dhammah","MIXED":"Campuran fathah-kasrah-dhammah","FATHAH":"Fathah"}[stage]
    return label,tokens,focus

def row_from(combo, units, *, page, slot, band, state, stage, code, desc):
    length=len(combo)
    return {
        "Jilid":1,"Page":page,"Slot":slot,"RowBand":band,"ObjectID":f"J1V8-P{page:02d}-S{slot:02d}",
        "ObjectOrigin":"PRACTICE_GENERATED","LearningState":state,"ArabicObject":" ".join(units),
        "Unit1":units[0],"Unit2":units[1] if length>=2 else "","Unit3":units[2] if length>=3 else "",
        "Base1":combo[0],"Base2":combo[1] if length>=2 else "","Base3":combo[2] if length>=3 else "",
        "UnitLength":length,"HarakatStage":stage,"DisplayJoinPolicy":"DISCONNECTED_NO_SPACE",
        "CompetencyCode":code,"CompetencyDescription":desc,"SourceRef":"PGE:JILID1:V8","QuranQuotation":"NO",
        "SpecialInjection":"NONE","Status":"COMPOSITION_V5_REVIEW_CANDIDATE_V8"
    }

def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument("--output-dir", default=str(DEFAULT_OUTPUT.relative_to(ROOT))); args=ap.parse_args()
    out=Path(args.output_dir); out=out if out.is_absolute() else ROOT/out
    prog={int(r["Page"]):r for r in read_csv(PROGRESSION)}; cre={int(r["Page"]):r for r in read_csv(CRE)}
    reading=[]; metadata=[]
    for page in range(1,41):
        p=prog[page]; c=cre[page]; active=uniq(p["ActiveLetters"]); new=uniq(p["NewLetters"]); stage=p["HarakatStage"]
        if tuple(x for x in HIJAIYAH if x in set(active)) != active:
            raise ValueError(f"ACTIVE_ORDER_NOT_HIJAIYAH page={page} active={''.join(active)}")
        if page in SPECIAL:
            metadata.append({"Page":page,"HarakatStage":"SPECIAL","NewLetters":"","ActiveLetters":p["ActiveLetters"],"NewMaterialLabel":"Nama huruf hijaiyah","NewMaterialBases":"","NewMaterialTokens":"","CompetencyCodes":"LETTER_NAMES","CompetencyDescriptions":"Mengenal dan menyebut nama huruf hijaiyah.","MemorizationCode":c["MemorizationCode"],"MemorizationDescription":c["MemorizationDescription"],"MemorizationStage":c["MemorizationStage"],"ArabicCode":c["ArabicCode"],"ArabicDescription":c["ArabicDescription"],"AkhlaqCode":c["AkhlaqCode"],"AkhlaqDescription":c["AkhlaqDescription"],"AssessmentCode":c["AssessmentCode"],"AssessmentDescription":c["AssessmentDescription"],"FooterProfile":c["FooterProfile"],"SpecialInjection":"LETTER_NAMES","Status":"COMPOSITION_V5_REVIEW_CANDIDATE_V8"}); continue
        label, focus_tokens, focus_bases=material_focus(active,new,stage,page)
        pair_code=f"J1-PAIR-CURRENT-{stage}"; pair_desc="Pembiasaan dua satuan huruf yang sama dengan materi fokus baris pertama; setiap unit tetap tunggal dan tidak tersambung."
        triple_code=f"J1-TRIPLE-{stage}"; triple_desc="Membaca tiga satuan huruf dengan komposisi materi halaman dan murojaah kumulatif."
        # Row 2 MUST be generated only from the exact Row-1 focus bases.
        pairs=structural(focus_bases,2,4,seed=page,allow_adjacent_repeat=True)
        for i,combo in enumerate(pairs):
            units=units_for(combo,stage,page,i); reading.append(row_from(combo,units,page=page,slot=i+1,band="ROW_2_L2_CURRENT",state="FOUNDATION" if page==1 else "CURRENT",stage=stage,code=pair_code,desc=pair_desc))
        if page==1:
            triples=structural(active,3,12,seed=page)
            for i,combo in enumerate(triples):
                units=units_for(combo,stage,page,i); reading.append(row_from(combo,units,page=page,slot=5+i,band="ROWS_3_6_L3",state="FOUNDATION",stage=stage,code=triple_code,desc=triple_desc))
        else:
            if new:
                current=current_triples(active,focus_bases,4,seed=page)
                review_pool=tuple(ch for ch in active if ch not in set(new)); review=structural(review_pool,3,8,seed=page+7)
            else:
                current=current_triples(active,focus_bases,4,seed=page)
                review=structural(active,3,8,seed=page+11)
            for i,combo in enumerate(current):
                units=units_for(combo,stage,page,i); reading.append(row_from(combo,units,page=page,slot=5+i,band="ROWS_3_6_L3",state="CURRENT",stage=stage,code=triple_code,desc=triple_desc))
            for j,combo in enumerate(review):
                rs=stage if new else review_stage_for(stage,j); units=units_for(combo,rs,page,4+j); reading.append(row_from(combo,units,page=page,slot=9+j,band="ROWS_3_6_L3",state="REVIEW",stage=rs,code=triple_code,desc=triple_desc))
        metadata.append({"Page":page,"HarakatStage":stage,"NewLetters":p["NewLetters"],"ActiveLetters":p["ActiveLetters"],"NewMaterialLabel":label,"NewMaterialBases":"".join(focus_bases),"NewMaterialTokens":"|".join(focus_tokens),"CompetencyCodes":f"{pair_code} | {triple_code}","CompetencyDescriptions":f"{pair_desc} | {triple_desc}","MemorizationCode":c["MemorizationCode"],"MemorizationDescription":c["MemorizationDescription"],"MemorizationStage":c["MemorizationStage"],"ArabicCode":c["ArabicCode"],"ArabicDescription":c["ArabicDescription"],"AkhlaqCode":c["AkhlaqCode"],"AkhlaqDescription":c["AkhlaqDescription"],"AssessmentCode":c["AssessmentCode"],"AssessmentDescription":c["AssessmentDescription"],"FooterProfile":c["FooterProfile"],"SpecialInjection":"NONE","Status":"COMPOSITION_V5_REVIEW_CANDIDATE_V8"})
    names=read_csv(LETTER_NAMES); injections=[{"Page":int(r["TargetPage"]),"Sequence":int(r["Sequence"]),"ContentType":"LETTER_NAME","Letter":r["Letter"],"LetterNameArabic":r["LetterNameArabic"],"Status":r.get("Status","REVIEW_CANDIDATE")} for r in names]
    write_csv(out/"JILID-1-READING-OBJECTS-V8.csv",reading); write_csv(out/"JILID-1-PAGE-METADATA-V8.csv",metadata); write_csv(out/"JILID-1-INJECTION-CONTENT-V8.csv",injections)
    print("JILID1_COMPOSER_V8=PASS"); print(f"READING_ROWS={len(reading)}"); print("HIJAIYAH_ORDER=ابتثجحخدذرزسشصضطظعغفقكلمنهوي"); print("ROW2_SOURCE=ROW1_FOCUS_ONLY"); print("RTL_AUTHORING_ORDER=FIRST_TOKEN_ON_RIGHT"); print("HEH_DISPLAY=TWO_EYE_PRESENTATION"); print("REVIEW_POLICY=8_CURRENT|8_REVIEW_AFTER_FOUNDATION"); return 0
if __name__=="__main__": raise SystemExit(main())
