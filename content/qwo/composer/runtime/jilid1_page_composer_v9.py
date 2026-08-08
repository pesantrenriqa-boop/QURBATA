#!/usr/bin/env python3
"""QURBATA Jilid 1 Composer v9.

Contract:
- visual-family/difficulty progression is primary; standard alphabet order is NOT the engine order;
- opening ا ب ت ث is deliberately split across pages 1-2;
- ن and ي are deliberately deferred to the end of the fathah introduction pass;
- row 1 focus; row 2 = 4 L2 from row-1 material only; rows 3-7 = 15 L3;
- kasrah triples mix 2 fathah + 1 kasrah; dhammah triples mix prior marks + 1 dhammah;
- 50:50 is cumulative/near-even: odd 19-slot pages alternate 9:10 and 10:9 current/review.
"""
from __future__ import annotations
import argparse
from pathlib import Path
from jilid1_page_composer_v8 import (ROOT,PROGRESSION,CRE,LETTER_NAMES,SPECIAL,MARKS,read_csv,write_csv,uniq,display_base,structural,current_triples,material_focus,row_from)

DEFAULT_OUTPUT=ROOT/'content/qwo/composer/output/jilid-1-v9-composition-v6'
PEDAGOGICAL_ORDER=tuple('ابتثجحخدذرزسشصضطظعغفقكلمهوني')
EXPECTED_NEW={1:'اب',2:'تث',3:'جحخ',4:'دذ',5:'رز',6:'سش',7:'صض',8:'طظ',9:'عغ',10:'فق',11:'ك',12:'ل',13:'م',14:'ه',15:'و',16:'ني'}

def marks_for_triple(stage:str,page:int,seq:int)->tuple[str,str,str]:
    if stage=='FATHAH': return ('َ','َ','َ')
    if stage=='KASRAH':
        patterns=(('َ','َ','ِ'),('َ','ِ','َ'),('ِ','َ','َ'))
        return patterns[(page+seq)%3]
    if stage=='DHAMMAH':
        patterns=(('َ','ِ','ُ'),('ِ','َ','ُ'),('َ','ُ','ِ'),('ُ','َ','ِ'))
        return patterns[(page+seq)%4]
    if stage=='MIXED':
        patterns=(('َ','ِ','ُ'),('ُ','َ','ِ'),('ِ','ُ','َ'))
        return patterns[(page+seq)%3]
    raise ValueError(stage)

def triple_units(combo,stage,page,seq):
    marks=marks_for_triple(stage,page,seq)
    return tuple(display_base(b)+marks[i] for i,b in enumerate(combo))

def pair_units(combo,stage,page=0,seq=0):
    if stage=='MIXED':
        patterns=(('َ','ِ'),('ِ','ُ'),('ُ','َ'))
        marks=patterns[(page+seq)%3]
        return tuple(display_base(b)+marks[i] for i,b in enumerate(combo))
    mark=MARKS[stage] if stage in MARKS else 'َ'
    return tuple(display_base(b)+mark for b in combo)

def stage_focus(active,stage,page):
    if stage=='MIXED':
        # Mixed-stage focus teaches the mark combination, not nine new letters at once.
        # Keep row-1 to three representative bases so the 44pt focus remains readable.
        starts={37:0,38:9,39:18}
        start=starts[page] % len(active)
        return tuple(active[(start+i)%len(active)] for i in range(3))
    if stage=='KASRAH': pages=(17,18,19,21,22,23,24,25)
    elif stage=='DHAMMAH': pages=tuple(range(26,37))
    else: raise ValueError(f'UNSUPPORTED_STAGE_FOCUS stage={stage} page={page}')
    idx=pages.index(page); q,r=divmod(len(active),len(pages)); sizes=[q+(i<r) for i in range(len(pages))]
    start=sum(sizes[:idx]); size=sizes[idx]
    return tuple(active[start:start+size]) if size else tuple(active[:2])

def focus_tokens_for(focus_bases,stage,page):
    if stage=='MIXED':
        marks=('َ','ِ','ُ')
        return [display_base(b)+marks[i%3] for i,b in enumerate(focus_bases)]
    return [display_base(b)+MARKS[stage] for b in focus_bases]

def main()->int:
    ap=argparse.ArgumentParser();ap.add_argument('--output-dir',default=str(DEFAULT_OUTPUT.relative_to(ROOT)));a=ap.parse_args()
    out=Path(a.output_dir);out=out if out.is_absolute() else ROOT/out
    prog={int(r['Page']):r for r in read_csv(PROGRESSION)};cre={int(r['Page']):r for r in read_csv(CRE)}
    reading=[];metadata=[]
    for page in range(1,41):
        p=prog[page];c=cre[page];active=uniq(p['ActiveLetters']);new=uniq(p['NewLetters']);stage=p['HarakatStage']
        if page<=16 and ''.join(new)!=EXPECTED_NEW[page]: raise ValueError(f'FAMILY_PROGRESS_MISMATCH page={page} new={"".join(new)}')
        expected_active=tuple(ch for ch in PEDAGOGICAL_ORDER if ch in set(active))
        if expected_active!=active: raise ValueError(f'ACTIVE_ORDER_NOT_PEDAGOGICAL page={page} active={"".join(active)}')
        if page in SPECIAL:
            metadata.append({'Page':page,'HarakatStage':'SPECIAL','NewLetters':'','ActiveLetters':p['ActiveLetters'],'NewMaterialLabel':'Nama huruf hijaiyah','NewMaterialBases':'','NewMaterialTokens':'','CompetencyCodes':'LETTER_NAMES','CompetencyDescriptions':'Mengenal dan menyebut nama huruf hijaiyah.','MemorizationCode':c['MemorizationCode'],'MemorizationDescription':c['MemorizationDescription'],'MemorizationStage':c['MemorizationStage'],'ArabicCode':c['ArabicCode'],'ArabicDescription':c['ArabicDescription'],'AkhlaqCode':c['AkhlaqCode'],'AkhlaqDescription':c['AkhlaqDescription'],'AssessmentCode':c['AssessmentCode'],'AssessmentDescription':c['AssessmentDescription'],'FooterProfile':c['FooterProfile'],'SpecialInjection':'LETTER_NAMES','Status':'COMPOSITION_V6_REVIEW_CANDIDATE_V9'});continue
        if new:
            focus_bases=new;label='Huruf baru';focus_tokens=[display_base(b)+MARKS['FATHAH'] for b in focus_bases]
        else:
            focus_bases=stage_focus(active,stage,page);label={'KASRAH':'Kasrah','DHAMMAH':'Dhammah','MIXED':'Campuran fathah-kasrah-dhammah'}[stage];focus_tokens=focus_tokens_for(focus_bases,stage,page)
        pair_code=f'J1-PAIR-CURRENT-{stage}';pair_desc='Empat latihan dua satuan huruf hanya dari materi fokus baris pertama.'
        triple_code=f'J1-TRIPLE-{stage}';triple_desc='Latihan tiga satuan huruf: materi saat ini dan murojaah kumulatif dengan kombinasi baru.'
        pairs=structural(focus_bases,2,4,seed=page,allow_adjacent_repeat=True)
        for i,combo in enumerate(pairs): reading.append(row_from(combo,pair_units(combo,stage,page,i),page=page,slot=i+1,band='ROW_2_L2_CURRENT',state='FOUNDATION' if page==1 else 'CURRENT',stage=stage,code=pair_code,desc=pair_desc))
        if page==1:
            triples=structural(active,3,15,seed=page,allow_adjacent_repeat=True)
            for i,combo in enumerate(triples): reading.append(row_from(combo,triple_units(combo,stage,page,i),page=page,slot=5+i,band='ROWS_3_7_L3',state='FOUNDATION',stage=stage,code=triple_code,desc=triple_desc))
        else:
            current_triple_count=5 if page%2 else 6
            review_count=15-current_triple_count
            current=current_triples(active,focus_bases,current_triple_count,seed=page)
            prior=tuple(ch for ch in active if ch not in set(new)) if new else active
            if not prior: prior=active
            review=structural(prior,3,review_count,seed=page+13,allow_adjacent_repeat=True)
            for i,combo in enumerate(current): reading.append(row_from(combo,triple_units(combo,stage,page,i),page=page,slot=5+i,band='ROWS_3_7_L3',state='CURRENT',stage=stage,code=triple_code,desc=triple_desc))
            for j,combo in enumerate(review): reading.append(row_from(combo,triple_units(combo,stage,page,current_triple_count+j),page=page,slot=5+current_triple_count+j,band='ROWS_3_7_L3',state='REVIEW',stage=stage,code=triple_code,desc=triple_desc))
        metadata.append({'Page':page,'HarakatStage':stage,'NewLetters':p['NewLetters'],'ActiveLetters':p['ActiveLetters'],'NewMaterialLabel':label,'NewMaterialBases':''.join(focus_bases),'NewMaterialTokens':'|'.join(focus_tokens),'CompetencyCodes':f'{pair_code} | {triple_code}','CompetencyDescriptions':f'{pair_desc} | {triple_desc}','MemorizationCode':c['MemorizationCode'],'MemorizationDescription':c['MemorizationDescription'],'MemorizationStage':c['MemorizationStage'],'ArabicCode':c['ArabicCode'],'ArabicDescription':c['ArabicDescription'],'AkhlaqCode':c['AkhlaqCode'],'AkhlaqDescription':c['AkhlaqDescription'],'AssessmentCode':c['AssessmentCode'],'AssessmentDescription':c['AssessmentDescription'],'FooterProfile':c['FooterProfile'],'SpecialInjection':'NONE','Status':'COMPOSITION_V6_REVIEW_CANDIDATE_V9'})
    names=read_csv(LETTER_NAMES);inj=[{'Page':int(r['TargetPage']),'Sequence':int(r['Sequence']),'ContentType':'LETTER_NAME','Letter':r['Letter'],'LetterNameArabic':r['LetterNameArabic'],'Status':r.get('Status','REVIEW_CANDIDATE')} for r in names]
    write_csv(out/'JILID-1-READING-OBJECTS-V9.csv',reading);write_csv(out/'JILID-1-PAGE-METADATA-V9.csv',metadata);write_csv(out/'JILID-1-INJECTION-CONTENT-V9.csv',inj)
    print('JILID1_COMPOSER_V9=PASS');print(f'READING_ROWS={len(reading)}');print('PAGE_PATTERN=ROW1_FOCUS|ROW2_4xL2|ROWS3_7_15xL3');print('ORDER_POLICY=VISUAL_FAMILY_DIFFICULTY_WITH_NUN_YA_DEFERRED');print('KASRAH_TRIPLE_PATTERN=2_FATHAH|1_KASRAH');print('DHAMMAH_TRIPLE_PATTERN=MIX_PRIOR|1_DHAMMAH');print('MIXED_FOCUS=3_BASES_WITH_FATHAH_KASRAH_DHAMMAH');print('REVIEW_POLICY=NEAR_50_50_ALTERNATING');return 0
if __name__=='__main__':raise SystemExit(main())
