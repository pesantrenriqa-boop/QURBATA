# Registry Normalization — L21 v1.0

**Status:** REGISTRY-NORMALIZED — NON-PRODUCTION  
**Checkpoint:** L21 / S5 Capstone  
**Recovery class:** R0 FULL  
**Source:** L21 Batch 01–03

## 1. Result

All historical slots L21-P01 through L21-P36 are present as complete records across the three source batches and are therefore classified **R0 FULL**. No wording recovery or speculative reconstruction is required.

Canonical IDs are reserved as:

`ARB-PL-L21-P001-v1.0` through `ARB-PL-L21-P036-v1.0`.

All rows remain `production_enabled=false` pending review and pilot validation.

## 2. Registry status map

P01–P04: normalized candidate, review pending.  
P05: normalized **HOLD-REVIEW/HIGH-AMBIGUITY**.  
P06–P07: normalized candidate, review pending.  
P08: normalized **HOLD-REVIEW/HIGH-AMBIGUITY**.  
P09–P12: normalized candidate, review pending; P12 requires segmented rubric.  
P13–P17: normalized candidate, review pending.  
P18: normalized **HOLD-REVIEW/HIGH-AMBIGUITY**.  
P19: normalized **HOLD-REVIEW/HIGH-AMBIGUITY**.  
P20–P24: normalized candidate, review pending.  
P25–P26: **PASS-CANDIDATE** from quality screen.  
P27–P28: **PASS-WITH-NOTE**.  
P29–P30: **PASS-CANDIDATE**.  
P31: **HOLD-AMBIGUOUS**; replacement/versioning required before automated learner scoring.  
P32: **PASS-CANDIDATE**.  
P33: **PASS-WITH-NOTE**.  
P34: **PASS-CANDIDATE**.  
P35–P36: **PASS-WITH-NOTE**.

## 3. Mandatory normalized fields

Every L21 row is required to carry:
- canonical_item_id
- historical_slot_id
- version
- checkpoint = L21
- stage = S5
- target_competency_ids
- prerequisite_ids
- quran_reference
- target_span
- response_class
- prompt
- expected_response
- critical_misconception
- error_codes
- ambiguity
- recovery_class = R0
- quality_status
- verse_family_id
- function_signature
- alternate_analysis_policy
- production_enabled = false

## 4. Capstone controls

1. Translation-only answers never satisfy mastery.
2. Tafsir/asbab al-nuzul knowledge never substitutes for linguistic evidence.
3. High-ambiguity items require alternate-analysis rubrics.
4. Meta-evaluative items must not be automatically learner-scored unless converted to an objective response format.
5. Critical prerequisite failure can block capstone mastery despite aggregate score.

## 5. Completion

**L21 registry normalization: 36/36 = 100%.**

This is registry completeness, not production readiness.