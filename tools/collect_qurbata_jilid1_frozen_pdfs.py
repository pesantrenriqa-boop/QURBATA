#!/usr/bin/env python3
from pathlib import Path
import shutil
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'dist/qurbata-print-ready/jilid-1/pages'
OUT=ROOT/'dist/qurbata-print-ready/jilid-1/FROZEN'
FROZEN={
 'P001':['QURBATA-JILID-1-P001-PRODUCTION-CLEAN-V10*.pdf'],
 'P003':['QURBATA-JILID-1-P003-CANDIDATE-V1*.pdf'],
 'P004':['QURBATA-JILID-1-P004-DAL-DHAL-CANDIDATE-V3*.pdf'],
 'P005':['QURBATA-JILID-1-P005-RA-ZAY-CANDIDATE-V2*.pdf'],
}
def latest(folder,patterns):
 cand=[]
 for pat in patterns:cand.extend(folder.glob(pat))
 return max(cand,key=lambda p:p.stat().st_mtime) if cand else None
def main():
 OUT.mkdir(parents=True,exist_ok=True);copied=0;missing=[]
 for page,pats in FROZEN.items():
  src=latest(BASE/page,pats)
  if not src:
   missing.append(page);continue
  dst=OUT/f'QURBATA-JILID-1-{page}-FROZEN.pdf';shutil.copy2(src,dst);copied+=1;print(f'{page}=COPIED|SOURCE={src.name}|DEST={dst.relative_to(ROOT)}')
 print(f'FROZEN_PDF_COLLECTOR=PASS');print(f'COPIED={copied}');print('MISSING=' + ('NONE' if not missing else '|'.join(missing)));print(f'FOLDER={OUT.relative_to(ROOT)}')
 return 0
if __name__=='__main__':raise SystemExit(main())
