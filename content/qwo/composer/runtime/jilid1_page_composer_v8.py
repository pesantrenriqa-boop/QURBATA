#!/usr/bin/env python3
"""QURBATA Jilid 1 Composer v8 — revised 1+4+12 page composition.

Reading-page contract:
- Row 1 is metadata/current-material focus (not counted as a reading object).
- Row 2: 4 x L2, CURRENT material only.
- Rows 3-6: 12 x L3, with page 2+ distribution 4 CURRENT + 8 REVIEW.
- Page 1 is FOUNDATION because no prior competency exists.
- All units are independent and rendered with DISCONNECTED_NO_SPACE.
"""
from __future__ import annotations
import argparse, csv
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[4]
PROGRESSION = ROOT / "content/qwo/lpe/JILID-1-PEDAGOGICAL-PROGRESSION-V4.csv"
CRE = ROOT / "content/qwo/registry/JILID-1-PAGE-CONTENT-REGISTRY-V2.csv"
LETTER_NAMES = ROOT / "content/qwo/lpe/JILID-1-LETTER-NAME-REGISTRY-V1.csv"
DEFAULT_OUTPUT = ROOT / "content/qwo/composer/output/jilid-1-v8-composition-v5"
SPECIAL = {20, 40}
MARKS = {"FATHAH":"َ", "KASRAH":"ِ", "DHAMMAH":"ُ"}
STAGE_ID = {"FATHAH":0, "KASRAH":1, "DHAMMAH":2, "MIXED":3}


def read_csv(path: Path) -> list[dict[str,str]]:
    with path.open(encoding="utf-8-sig", newline="") as h: return list(csv.DictReader(h))

def write_csv(path: Path, rows: list[dict[str,Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as h:
        w=csv.DictWriter(h, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

def uniq(text: str) -> tuple[str,...]: return tuple(dict.fromkeys(text))

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
    # controlled offsets keep examples readable while changing surface combinations page-to-page
    patterns = [(0,1)] if length==2 else [(0,1,2),(0,2,1),(0,1,3),(0,2,3),(0,3,1)]
    for round_no in range(max(3,n)):
        for start in range(n):
            p=patterns[(round_no+seed+start)%len(patterns)]
            combo=tuple(pool[(start+d+round_no)%n] for d in p)
            if not allow_adjacent_repeat and any(combo[i]==combo[i+1] for i in range(len(combo)-1)): continue
            if combo in seen: continue
            seen.add(combo); out.append(combo)
            if len(out)>=limit: return out
    # Dedicated Row 2 may intentionally repeat one newly introduced letter when it is the only new base.
    if allow_adjacent_repeat and len(pool)==1:
        return [tuple(pool[0] for _ in range(length)) for _ in range(limit)]
    if not out: raise ValueError(f"SEQUENCE_POOL_EMPTY length={length} pool={''.join(pool)}")
    while len(out)<limit: out.append(out[len(out)%len(out)])
    return out[:limit]

def units_for(combo: tuple[str,...], stage: str, page: int, seq: int) -> tuple[str,...]:
    return tuple(base+mark_for(stage,page,seq,i) for i,base in enumerate(combo))

def material_focus(active: tuple[str,...], new: tuple[str,...], stage: str, page: int) -> tuple[str,list[str]]:
    if new:
        tokens=[base+mark_for(stage,page,i,0) for i,base in enumerate(new)]
        return "Huruf baru", tokens
    start=(page*2)%len(active)
    reps=[active[(start+i)%len(active)] for i in range(3)]
    tokens=[base+mark_for(stage,page,i,0) for i,base in enumerate(reps)]
    labels={"KASRAH":"Kasrah","DHAMMAH":"Dhammah","MIXED":"Campuran fathah-kasrah-dhammah","FATHAH":"Fathah"}
    return labels[stage], tokens

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
        if page in SPECIAL:
            metadata.append({"Page":page,"HarakatStage":"SPECIAL","NewLetters":"","ActiveLetters":p["ActiveLetters"],"NewMaterialLabel":"Nama huruf hijaiyah","NewMaterialTokens":"","CompetencyCodes":"LETTER_NAMES","CompetencyDescriptions":"Mengenal dan menyebut nama huruf hijaiyah.","MemorizationCode":c["MemorizationCode"],"MemorizationDescription":c["MemorizationDescription"],"MemorizationStage":c["MemorizationStage"],"ArabicCode":c["ArabicCode"],"ArabicDescription":c["ArabicDescription"],"AkhlaqCode":c["AkhlaqCode"],"AkhlaqDescription":c["AkhlaqDescription"],"AssessmentCode":c["AssessmentCode"],"AssessmentDescription":c["AssessmentDescription"],"FooterProfile":c["FooterProfile"],"SpecialInjection":"LETTER_NAMES","Status":"COMPOSITION_V5_REVIEW_CANDIDATE_V8"}); continue
        label, focus_tokens=material_focus(active,new,stage,page)
        pair_code=f"J1-PAIR-CURRENT-{stage}"; pair_desc="Pembiasaan dua satuan huruf pada materi halaman; setiap unit tetap tunggal dan tidak tersambung."
        triple_code=f"J1-TRIPLE-{stage}"; triple_desc="Membaca tiga satuan huruf dengan komposisi materi halaman dan murojaah kumulatif."
        # Row 2: four CURRENT pairs. With new letters, use only those letters; otherwise current harakat on active letters.
        pair_pool=new if new else active
        pairs=structural(pair_pool,2,4,seed=page,allow_adjacent_repeat=True)
        for i,combo in enumerate(pairs):
            units=units_for(combo,stage,page,i); reading.append(row_from(combo,units,page=page,slot=i+1,band="ROW_2_L2_CURRENT",state="FOUNDATION" if page==1 else "CURRENT",stage=stage,code=pair_code,desc=pair_desc))
        # Rows 3-6: 12 triples. Page 1 foundation; later 4 CURRENT + 8 REVIEW = total page 8:8 with Row 2.
        if page==1:
            triples=structural(active,3,12,seed=page)
            for i,combo in enumerate(triples):
                units=units_for(combo,stage,page,i); reading.append(row_from(combo,units,page=page,slot=5+i,band="ROWS_3_6_L3",state="FOUNDATION",stage=stage,code=triple_code,desc=triple_desc))
        else:
            if new:
                current_candidates=[x for x in structural(active,3,max(24,len(active)*3),seed=page) if any(ch in set(new) for ch in x)]
                review_pool=tuple(ch for ch in active if ch not in set(new))
                review_candidates=structural(review_pool,3,8,seed=page+7)
                if len(current_candidates)<4: raise ValueError(f"CURRENT_TRIPLE_POOL_SHORT page={page}")
                current=current_candidates[:4]
                review=review_candidates[:8]
                for i,combo in enumerate(current):
                    units=units_for(combo,stage,page,i); reading.append(row_from(combo,units,page=page,slot=5+i,band="ROWS_3_6_L3",state="CURRENT",stage=stage,code=triple_code,desc=triple_desc))
                for j,combo in enumerate(review):
                    units=units_for(combo,stage,page,4+j); reading.append(row_from(combo,units,page=page,slot=9+j,band="ROWS_3_6_L3",state="REVIEW",stage=stage,code=triple_code,desc=triple_desc))
            else:
                current=structural(active,3,4,seed=page)
                review=structural(active,3,8,seed=page+11)
                for i,combo in enumerate(current):
                    units=units_for(combo,stage,page,i); reading.append(row_from(combo,units,page=page,slot=5+i,band="ROWS_3_6_L3",state="CURRENT",stage=stage,code=triple_code,desc=triple_desc))
                for j,combo in enumerate(review):
                    rs=review_stage_for(stage,j); units=units_for(combo,rs,page,4+j); reading.append(row_from(combo,units,page=page,slot=9+j,band="ROWS_3_6_L3",state="REVIEW",stage=rs,code=triple_code,desc=triple_desc))
        metadata.append({"Page":page,"HarakatStage":stage,"NewLetters":p["NewLetters"],"ActiveLetters":p["ActiveLetters"],"NewMaterialLabel":label,"NewMaterialTokens":"|".join(focus_tokens),"CompetencyCodes":f"{pair_code} | {triple_code}","CompetencyDescriptions":f"{pair_desc} | {triple_desc}","MemorizationCode":c["MemorizationCode"],"MemorizationDescription":c["MemorizationDescription"],"MemorizationStage":c["MemorizationStage"],"ArabicCode":c["ArabicCode"],"ArabicDescription":c["ArabicDescription"],"AkhlaqCode":c["AkhlaqCode"],"AkhlaqDescription":c["AkhlaqDescription"],"AssessmentCode":c["AssessmentCode"],"AssessmentDescription":c["AssessmentDescription"],"FooterProfile":c["FooterProfile"],"SpecialInjection":"NONE","Status":"COMPOSITION_V5_REVIEW_CANDIDATE_V8"})
    names=read_csv(LETTER_NAMES); injections=[{"Page":int(r["TargetPage"]),"Sequence":int(r["Sequence"]),"ContentType":"LETTER_NAME","Letter":r["Letter"],"LetterNameArabic":r["LetterNameArabic"],"Status":r.get("Status","REVIEW_CANDIDATE")} for r in names]
    write_csv(out/"JILID-1-READING-OBJECTS-V8.csv",reading); write_csv(out/"JILID-1-PAGE-METADATA-V8.csv",metadata); write_csv(out/"JILID-1-INJECTION-CONTENT-V8.csv",injections)
    print("JILID1_COMPOSER_V8=PASS"); print(f"READING_ROWS={len(reading)}"); print("READING_PAGE_PATTERN=ROW1_FOCUS|ROW2_4xL2|ROWS3_6_12xL3"); print("PRACTICE_FONT_POLICY=ONE_COMMON_SIZE"); print("REVIEW_POLICY=8_CURRENT|8_REVIEW_AFTER_FOUNDATION"); return 0
if __name__=="__main__": raise SystemExit(main())
