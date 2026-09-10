# Stress Test K21–K23 v0.1

**Status:** WORKING RESEARCH — PRE-FREEZE  
**Parent:** `EVIDENCE-K21-K22-HEADTOHEAD-K23-K24-v0.1.md`  
**Rule:** cumulative-only, occurrence-specific morphology/syntax, minimal valid Qur'anic unit.

## Sequence Under Test

- K21-CAND — dhamir muttashil sebagai maf'ul bih
- K22-CAND — recognition isim isyarah
- K23-CAND — recognition isim maushul

## K21 Stress Test — Attached Pronoun as Direct Object

Dependencies:
- K14 maf'ul bih isim zhahir gives object relation;
- K15 attached-pronoun recognition gives segmentation;
- K6/K7/K10 provide verbal foundation.

Pass condition:
- suffix attached to a verb;
- occurrence parser confirms object function;
- no need to introduce two-object construction, object clause, or higher verbal government.

Reject/premature:
- suffix on noun = possible mudhaf ilaih (already K18 but not K21 target);
- suffix on preposition = K20 relation;
- subject suffix/person marker must not be confused with object suffix;
- verb with two pronominal objects or complex complement remains later.

Result: **PASS / READY FOR DRAFT-FREEZE** with occurrence-specific annotation.

## K22 Stress Test — Isim Isyarah Recognition

Target: identify demonstrative forms as a category/token before teaching demonstrative phrase or syntactic function.

Core forms may include occurrence-validated examples of:
- هذا
- هذه
- ذلك
- تلك
- هؤلاء
- أولئك

Pass condition:
- only recognition;
- do not require analysis of badal, 'athaf bayan, mubtada', khabar, or demonstrative phrase.

Result: **PASS / VERY STRONG**.

## K23 Stress Test — Isim Maushul Recognition

Target: identify relative-pronoun forms without yet analyzing silah al-maushul.

Core forms may include:
- الذي
- التي
- الذين
- اللاتي/اللائي where corpus occurrence supports form inventory.

Pass condition:
- token recognition only;
- relative clause boundary and syntactic role are withheld.

Risk:
- students may assume recognizing `الذي` means they already understand the following clause. Curriculum metadata must explicitly set `silah_analysis = locked`.

Result: **PASS / READY FOR DRAFT-FREEZE**.

## Dependency Reversal Check

No hard dependency requires:
- demonstrative recognition after verbal PP attachment;
- relative-pronoun recognition after verbal PP attachment;
- K21 object suffix after demonstrative/relative recognition.

Thus K21→K22→K23 is pedagogically valid. K22 and K23 are recognition nodes and could be parallel in the graph; sequence order is retained for linear teaching.

## Next Frontier Re-scan

Existing:
- verbal + jar–majrur attachment;
- fa'il mustatir.

New integration candidates now unlocked by K22/K23:
- demonstrative as mubtada' + simple nominal khabar;
- simple demonstrative phrase (`اسم إشارة + اسم معرف`), with exact syntactic label to be evidence-driven;
- relative pronoun + minimal silah verbal/nominal, but this is structurally heavier;
- attached pronoun object already K21.

### Preliminary comparison

**Demonstrative as mubtada'** combines K22 + K8 and may be lighter than verbal PP attachment.

**Simple demonstrative phrase** may involve apposition/badal/'athaf bayan analyses and therefore cannot be treated as one relation until occurrence-specific grammar is audited.

**Silah al-maushul** is clearly heavier than mere recognition and should not immediately follow K23 without evidence.

## Revised Frontier Hypothesis

- K24-CAND — isim isyarah sebagai mubtada' dengan khabar nominal sederhana
- K25-CAND — jar–majrur sebagai pelengkap/attachment fi'il sederhana
- K26-CAND — fa'il mustatir dasar
- K27+ — demonstrative phrase relation, silah maushul, and further nominal/verbal expansions subject to evidence.

This revises the earlier assumption that verbal PP attachment must immediately be K24.

## Decision

K21, K22, K23 pass structural stress test and are eligible for research-layer draft freeze.

Next action:
1. issue final gate K21–K23;
2. head-to-head K24 demonstrative-mubtada' vs verbal PP attachment;
3. keep fa'il mustatir behind both until its inference burden is justified by evidence.