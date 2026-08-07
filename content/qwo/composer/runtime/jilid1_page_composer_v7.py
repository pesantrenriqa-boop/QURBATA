#!/usr/bin/env python3
"""QURBATA Jilid 1 Composer v7 — micro progression + 50:50 competency review."""
from __future__ import annotations
import argparse,csv,importlib.util,sys
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[4]
PGE_PATH=ROOT/"content/qwo/composer/runtime/practice_generation_engine_v1.py"
PROGRESSION=ROOT/"content/qwo/lpe/JILID-1-PEDAGOGICAL-PROGRESSION-V4.csv"
CRE_PAGE_REGISTRY=ROOT/"content/qwo/registry/JILID-1-PAGE-CONTENT-REGISTRY-V2.csv"
LETTER_NAMES=ROOT/"content/qwo/lpe/JILID-1-LETTER-NAME-REGISTRY-V1.csv"
DEFAULT_OUTPUT=ROOT/"content/qwo/composer/output/jilid-1-v7-micro-progression"
SPECIAL_PAGES={20,40}
def load_module(path,name):
 spec=importlib.util.spec_from_file_location(name,path); module=importlib.util.module_from_spec(spec); sys.modules[name]=module; spec.loader.exec_module(module); return module
PGE=load_module(PGE_PATH,"qurbata_pge_v1_for_j1v7")
def read_csv(path):
 if not path.is_file(): raise FileNotFoundError(path)
 with path.open(encoding="utf-8-sig",newline="") as h:return list(csv.DictReader(h))
def write_csv(path,rows):
 if not rows: raise ValueError(f"EMPTY_OUTPUT: {path}")
 path.parent.mkdir(parents=True,exist_ok=True)
 with path.open("w",encoding="utf-8",newline="") as h:
  w=csv.DictWriter(h,fieldnames=list(rows[0].keys()));w.writeheader();w.writerows(rows)
def load_progression():
 rows=read_csv(PROGRESSION); result={int(r['Page']):r for r in rows}
 if len(rows)!=40 or set(result)!=set(range(1,41)):raise ValueError("PROGRESSION_PAGE_SET_INVALID")
 return result
def competency(stage,length):
 label={"FATHAH":"fathah","KASRAH":"kasrah","DHAMMAH":"dhammah","MIXED":"campuran fathah-kasrah-dhammah"}[stage]
 return f"J1-PRACTICE-L{length}-{stage}",f"Membaca latihan {length} satuan huruf {label}; setiap huruf tetap berbentuk tunggal dan tidak tersambung."
def main():
 parser=argparse.ArgumentParser();parser.add_argument('--output-dir',default=str(DEFAULT_OUTPUT.relative_to(ROOT)));args=parser.parse_args();out=Path(args.output_dir);out=out if out.is_absolute() else ROOT/out;out.mkdir(parents=True,exist_ok=True)
 progression=load_progression();cre={int(r['Page']):r for r in read_csv(CRE_PAGE_REGISTRY)};reading=[];metadata=[]
 for page in range(1,41):
  plan=progression[page];c=cre[page]
  if page in SPECIAL_PAGES:
   metadata.append({'Page':page,'HarakatStage':'SPECIAL','NewLetters':'','ActiveLetters':plan['ActiveLetters'],'CompetencyCodes':'LETTER_NAMES','CompetencyDescriptions':'Mengenal dan menyebut nama huruf hijaiyah.','MemorizationCode':c['MemorizationCode'],'MemorizationDescription':c['MemorizationDescription'],'MemorizationStage':c['MemorizationStage'],'ArabicCode':c['ArabicCode'],'ArabicDescription':c['ArabicDescription'],'AkhlaqCode':c['AkhlaqCode'],'AkhlaqDescription':c['AkhlaqDescription'],'AssessmentCode':c['AssessmentCode'],'AssessmentDescription':c['AssessmentDescription'],'FooterProfile':c['FooterProfile'],'SpecialInjection':'LETTER_NAMES','Status':'MICRO_PROGRESSION_REVIEW_CANDIDATE_V7'});continue
  stage=plan['HarakatStage'];comps=[]
  for length in (1,2,3):
   generated=PGE.generate(plan['ActiveLetters'],plan['NewLetters'],stage,length,8,page);code,desc=competency(stage,length);comps.append((code,desc))
   for offset,obj in enumerate(generated):
    issues=PGE.validate_object(obj,plan['ActiveLetters'])
    if issues:raise ValueError(f"PGE_OBJECT_INVALID page={page} length={length} issues={'|'.join(issues)}")
    slot=(length-1)*8+offset+1
    reading.append({'Jilid':1,'Page':page,'Slot':slot,'RowBand':'ROWS_1_2_L1' if length==1 else ('ROWS_3_4_L2' if length==2 else 'ROWS_5_6_L3'),'ObjectID':f'J1V7-P{page:02d}-S{slot:02d}','ObjectOrigin':'PRACTICE_GENERATED','LearningState':obj.learning_state,'ArabicObject':obj.display_text,'Unit1':obj.units[0],'Unit2':obj.units[1] if length>=2 else '','Unit3':obj.units[2] if length>=3 else '','Base1':obj.bases[0],'Base2':obj.bases[1] if length>=2 else '','Base3':obj.bases[2] if length>=3 else '','UnitLength':length,'HarakatStage':stage,'DisplayJoinPolicy':'DISCONNECTED_NO_SPACE','CompetencyCode':code,'CompetencyDescription':desc,'SourceRef':'PGE:JILID1','QuranQuotation':'NO','SpecialInjection':'NONE','Status':'MICRO_PROGRESSION_REVIEW_CANDIDATE_V7'})
  metadata.append({'Page':page,'HarakatStage':stage,'NewLetters':plan['NewLetters'],'ActiveLetters':plan['ActiveLetters'],'CompetencyCodes':' | '.join(x[0] for x in comps),'CompetencyDescriptions':' | '.join(x[1] for x in comps),'MemorizationCode':c['MemorizationCode'],'MemorizationDescription':c['MemorizationDescription'],'MemorizationStage':c['MemorizationStage'],'ArabicCode':c['ArabicCode'],'ArabicDescription':c['ArabicDescription'],'AkhlaqCode':c['AkhlaqCode'],'AkhlaqDescription':c['AkhlaqDescription'],'AssessmentCode':c['AssessmentCode'],'AssessmentDescription':c['AssessmentDescription'],'FooterProfile':c['FooterProfile'],'SpecialInjection':'NONE','Status':'MICRO_PROGRESSION_REVIEW_CANDIDATE_V7'})
 names=read_csv(LETTER_NAMES);injections=[{'Page':int(r['TargetPage']),'Sequence':int(r['Sequence']),'ContentType':'LETTER_NAME','Letter':r['Letter'],'LetterNameArabic':r['LetterNameArabic'],'Status':r.get('Status','REVIEW_CANDIDATE')} for r in names]
 write_csv(out/'JILID-1-READING-OBJECTS-V7.csv',reading);write_csv(out/'JILID-1-PAGE-METADATA-V7.csv',metadata);write_csv(out/'JILID-1-INJECTION-CONTENT-V7.csv',injections)
 print('JILID1_COMPOSER_V7=PASS');print(f'READING_ROWS={len(reading)}');print('REVIEW_POLICY=50_NEW|50_REVIEW_AFTER_FOUNDATION');print('DISPLAY_JOIN_POLICY=DISCONNECTED_NO_SPACE');return 0
if __name__=='__main__':raise SystemExit(main())
