#!/usr/bin/env python3
"""QURBATA Jilid 1 Composer v10 — unit-level letter+harakat review.

Jilid-1 specific policy:
- the atomic review unit is one learned letter+harakat, NOT a previously generated L2/L3 block;
- each page is dominated by the current page's letter+harakat material;
- cumulative review samples previously introduced letter+harakat units;
- row 2 remains four L2 boxes from current focus only, but avoids repeating the same pair surface when the focus has >=2 units;
- rows 3-7 contain fifteen L3 boxes assembled afresh from unit pools;
- no L3 surface block is copied as the review unit;
- practice target after foundation: 32 CURRENT units + 21 REVIEW units = 53 total units (~60/40).
"""
from __future__ import annotations
import argparse
from pathlib import Path
from jilid1_page_composer_v8 import ROOT,PROGRESSION,CRE,LETTER_NAMES,SPECIAL,MARKS,read_csv,write_csv,uniq,display_base
from jilid1_page_composer_v9 import PEDAGOGICAL_ORDER,EXPECTED_NEW,stage_focus

DEFAULT_OUTPUT=ROOT/'content/qwo/composer/output/jilid-1-v10-unit-review'
MARK_TO_NAME={'َ':'FATHAH','ِ':'KASRAH','ُ':'DHAMMAH'}

def unit(base:str, mark:str, state:str)->dict:
    return {'base':base,'mark':mark,'token':display_base(base)+mark,'state':state}

def current_mark(stage:str,page:int,index:int)->str:
    if stage=='FATHAH': return 'َ'
    if stage=='KASRAH': return 'ِ'
    if stage=='DHAMMAH': return 'ُ'
    return ('َ','ِ','ُ')[(page+index)%3]

def focus_for(active, new, stage, page):
    if new:return tuple(new)
    return stage_focus(active,stage,page)

def prior_unit_pool(prog:dict[int,dict], page:int):
    """All letter+harakat units explicitly introduced before this page."""
    pool=[];seen=set()
    for pno in range(1,page):
        if pno in SPECIAL:continue
        p=prog[pno];active=uniq(p['ActiveLetters']);new=uniq(p['NewLetters']);stage=p['HarakatStage']
        focus=focus_for(active,new,stage,pno)
        for i,b in enumerate(focus):
            mark=current_mark(stage,pno,i)
            key=(b,mark)
            if key not in seen:
                seen.add(key);pool.append(unit(b,mark,'REVIEW'))
    return pool

def cycle_select(pool:list[dict], count:int, seed:int)->list[dict]:
    if not pool:raise ValueError('EMPTY_UNIT_POOL')
    start=seed%len(pool);ordered=pool[start:]+pool[:start]
    return [dict(ordered[i%len(ordered)]) for i in range(count)]

def make_pairs(focus_bases,stage,page):
    """Four L2 boxes from focus units only, with surface variation when possible."""
    cur=[unit(b,current_mark(stage,page,i),'CURRENT') for i,b in enumerate(focus_bases)]
    if not cur:raise ValueError(f'FOCUS_EMPTY page={page}')
    n=len(cur)
    if n==1:
        patterns=((0,0),(0,0),(0,0),(0,0))
    elif n==2:
        # AB, BA, AA, BB: four distinct pedagogical exposures instead of AB x4.
        patterns=((0,1),(1,0),(0,0),(1,1))
    else:
        # Rotate across the focus set while keeping every unit CURRENT.
        patterns=((0,1),(1,2),(2,0),(0,2))
    return [[dict(cur[a%n]),dict(cur[b%n])] for a,b in patterns]

def _replacement_same_state(pool:list[dict], forbidden_token:str, seed:int)->dict|None:
    if not pool:return None
    for off in range(len(pool)):
        cand=pool[(seed+off)%len(pool)]
        if cand['token']!=forbidden_token:
            return dict(cand)
    return None

def make_triples(current_pool,review_pool,page):
    cur=cycle_select(current_pool,24,page*3)
    rev=cycle_select(review_pool,21,page*5+1)
    units=[];ci=ri=0
    motif=('C','R','C','R','C','C','R','R')
    for i in range(45):
        want=motif[(i+page)%len(motif)]
        if want=='C' and ci<len(cur):units.append(cur[ci]);ci+=1
        elif want=='R' and ri<len(rev):units.append(rev[ri]);ri+=1
        elif ci<len(cur):units.append(cur[ci]);ci+=1
        else:units.append(rev[ri]);ri+=1
    triples=[]
    for i in range(0,45,3):
        block=[dict(x) for x in units[i:i+3]]
        if len(block)==3 and block[0]['token']==block[1]['token']:
            pool=current_pool if block[1]['state']=='CURRENT' else review_pool
            repl=_replacement_same_state(pool,block[0]['token'],page+i+1)
            if repl is not None:
                repl['state']=block[1]['state'];block[1]=repl
        if len(block)==3 and block[1]['token']==block[2]['token']:
            pool=current_pool if block[2]['state']=='CURRENT' else review_pool
            repl=_replacement_same_state(pool,block[1]['token'],page+i+2)
            if repl is not None:
                repl['state']=block[2]['state'];block[2]=repl
        triples.append(block)
    cc=sum(u['state']=='CURRENT' for b in triples for u in b)
    rr=sum(u['state']=='REVIEW' for b in triples for u in b)
    if (cc,rr)!=(24,21):
        raise ValueError(f'UNIT_RATIO_DRIFT page={page} current={cc} review={rr}')
    return triples

def row(page,slot,band,units,stage,code,desc):
    states=[u['state'] for u in units];cur=states.count('CURRENT');rev=states.count('REVIEW')
    d={'Jilid':1,'Page':page,'Slot':slot,'RowBand':band,'ObjectID':f'J1V10-P{page:02d}-S{slot:02d}','ObjectOrigin':'UNIT_LEVEL_PRACTICE','LearningState':'FOUNDATION' if page==1 else ('MIXED_CURRENT_REVIEW' if cur and rev else states[0]),'ArabicObject':' '.join(u['token'] for u in units),'UnitLength':len(units),'HarakatStage':stage,'DisplayJoinPolicy':'DISCONNECTED_NO_SPACE','CompetencyCode':code,'CompetencyDescription':desc,'SourceRef':'UNIT-REVIEW:JILID1','QuranQuotation':'NO','SpecialInjection':'NONE','CurrentUnitCount':cur,'ReviewUnitCount':rev,'Status':'UNIT_REVIEW_CANDIDATE_V10'}
    for i in range(1,4):
        u=units[i-1] if i<=len(units) else None
        d[f'Unit{i}']=u['token'] if u else '';d[f'Base{i}']=u['base'] if u else '';d[f'Mark{i}']=MARK_TO_NAME.get(u['mark'],'') if u else '';d[f'Unit{i}State']=u['state'] if u else ''
    return d

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output-dir',default=str(DEFAULT_OUTPUT.relative_to(ROOT)));a=ap.parse_args();out=Path(a.output_dir);out=out if out.is_absolute() else ROOT/out
    prog={int(r['Page']):r for r in read_csv(PROGRESSION)};cre={int(r['Page']):r for r in read_csv(CRE)};reading=[];metadata=[]
    for page in range(1,41):
        p=prog[page];c=cre[page];active=uniq(p['ActiveLetters']);new=uniq(p['NewLetters']);stage=p['HarakatStage']
        if page<=16 and ''.join(new)!=EXPECTED_NEW[page]:raise ValueError(f'FAMILY_PROGRESS_MISMATCH page={page}')
        expected=tuple(ch for ch in PEDAGOGICAL_ORDER if ch in set(active))
        if expected!=active:raise ValueError(f'ACTIVE_ORDER_NOT_PEDAGOGICAL page={page}')
        if page in SPECIAL:
            metadata.append({'Page':page,'HarakatStage':'SPECIAL','NewLetters':'','ActiveLetters':p['ActiveLetters'],'NewMaterialLabel':'Nama huruf hijaiyah','NewMaterialBases':'','NewMaterialTokens':'','CompetencyCodes':'LETTER_NAMES','CompetencyDescriptions':'Mengenal dan menyebut nama huruf hijaiyah.','MemorizationCode':c['MemorizationCode'],'MemorizationDescription':c['MemorizationDescription'],'MemorizationStage':c['MemorizationStage'],'ArabicCode':c['ArabicCode'],'ArabicDescription':c['ArabicDescription'],'AkhlaqCode':c['AkhlaqCode'],'AkhlaqDescription':c['AkhlaqDescription'],'AssessmentCode':c['AssessmentCode'],'AssessmentDescription':c['AssessmentDescription'],'FooterProfile':c['FooterProfile'],'SpecialInjection':'LETTER_NAMES','Status':'UNIT_REVIEW_CANDIDATE_V10'});continue
        focus=focus_for(active,new,stage,page)
        focus_units=[unit(b,current_mark(stage,page,i),'CURRENT') for i,b in enumerate(focus)]
        label='Huruf baru' if new else {'KASRAH':'Kasrah baru','DHAMMAH':'Dhammah baru','MIXED':'Latihan campuran'}[stage]
        pairs=make_pairs(focus,stage,page)
        code=f'J1-LETTER-HARAKAT-{stage}';desc='Membaca huruf berharakat dengan dominasi materi halaman dan murojaah kumulatif pada tingkat satuan huruf.'
        for i,b in enumerate(pairs):reading.append(row(page,i+1,'ROW_2_L2_CURRENT',b,stage,code,desc))
        if page==1:
            basepool=[unit(b,'َ','CURRENT') for b in focus]
            flat=cycle_select(basepool,45,1);triples=[flat[i:i+3] for i in range(0,45,3)]
        else:
            review_pool=prior_unit_pool(prog,page)
            current_pool=[unit(b,current_mark(stage,page,i),'CURRENT') for i,b in enumerate(focus)]
            triples=make_triples(current_pool,review_pool,page)
        for i,b in enumerate(triples):reading.append(row(page,5+i,'ROWS_3_7_L3',b,stage,code,desc))
        metadata.append({'Page':page,'HarakatStage':stage,'NewLetters':p['NewLetters'],'ActiveLetters':p['ActiveLetters'],'NewMaterialLabel':label,'NewMaterialBases':''.join(focus),'NewMaterialTokens':'|'.join(u['token'] for u in focus_units),'CompetencyCodes':code,'CompetencyDescriptions':desc,'MemorizationCode':c['MemorizationCode'],'MemorizationDescription':c['MemorizationDescription'],'MemorizationStage':c['MemorizationStage'],'ArabicCode':c['ArabicCode'],'ArabicDescription':c['ArabicDescription'],'AkhlaqCode':c['AkhlaqCode'],'AkhlaqDescription':c['AkhlaqDescription'],'AssessmentCode':c['AssessmentCode'],'AssessmentDescription':c['AssessmentDescription'],'FooterProfile':c['FooterProfile'],'SpecialInjection':'NONE','Status':'UNIT_REVIEW_CANDIDATE_V10'})
    names=read_csv(LETTER_NAMES);inj=[{'Page':int(r['TargetPage']),'Sequence':int(r['Sequence']),'ContentType':'LETTER_NAME','Letter':r['Letter'],'LetterNameArabic':r['LetterNameArabic'],'Status':r.get('Status','REVIEW_CANDIDATE')} for r in names]
    write_csv(out/'JILID-1-READING-OBJECTS-V10.csv',reading);write_csv(out/'JILID-1-PAGE-METADATA-V10.csv',metadata);write_csv(out/'JILID-1-INJECTION-CONTENT-V10.csv',inj)
    print('JILID1_COMPOSER_V10=PASS');print(f'READING_ROWS={len(reading)}');print('REVIEW_ATOM=LETTER_PLUS_HARAKAT');print('BLOCK_REUSE_AS_REVIEW=FORBIDDEN');print('PAGE_UNIT_TARGET=32_CURRENT|21_REVIEW');print('ROW2_SOURCE=FOCUS_UNITS_ONLY');print('ROW2_VARIATION=UNIQUE_WHEN_FOCUS_GE_2');print('ROWS3_7=FRESH_UNIT_ASSEMBLY');return 0
if __name__=='__main__':raise SystemExit(main())
