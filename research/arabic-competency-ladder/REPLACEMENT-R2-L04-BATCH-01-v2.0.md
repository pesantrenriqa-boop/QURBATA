# R2 Replacement — L04 Batch 01 v2.0

**Status:** DRAFT-REPLACEMENT — NON-PRODUCTION  
**Checkpoint:** L04  
**Recovery source class:** R2 SUMMARY-ONLY  
**Historical slots covered:** L04-P01–L04-P06  
**Rule:** these are newly authored replacements. They are **not** reconstructions of lost historical wording.

## 1. Replacement policy

Each replacement receives a new major version because original full wording is unavailable. Historical slot identity is preserved for traceability, but the new item must pass quality and Arabic-content review from zero.

All rows: `production_enabled=false`.

## 2. Replacement items

### ARB-PL-L04-P001-v2.0 — Basic definite noun recognition
- Historical slot: L04-P01
- Target competency: K01/K02
- Reference: QS 112:2
- Target span: `اللَّهُ الصَّمَدُ`
- Response class: direct recognition
- Prompt: tunjukkan satu isim ma‘rifah dengan `الـ` pada span.
- Expected: `الصمد` recognized as definite noun with `الـ`; `الله` accepted as proper-name noun but is not the target `الـ` example.
- Critical misconception: every Arabic token treated as same word class.
- Feature ceiling: word-class + definiteness recognition only; no full i‘rab.
- Ambiguity: LOW
- Quality status: DRAFT-REPLACEMENT

### ARB-PL-L04-P002-v2.0 — Nakirah/tanwin recognition
- Historical slot: L04-P02
- Target competency: K03
- Reference: QS 2:2
- Target span: `هُدًى`
- Response class: direct recognition
- Prompt: apakah target menunjukkan bentuk nakirah dengan tanwin pada bentuk tertulis/terbaca yang relevan?
- Expected: yes; target is treated as the intended indefinite/tanwin recognition example at this ceiling.
- Critical misconception: confusing definiteness with semantic familiarity.
- Feature ceiling: no sentence-relation scoring.
- Ambiguity: MEDIUM; Arabic-content review required for pedagogical phrasing.
- Quality status: DRAFT-REPLACEMENT

### ARB-PL-L04-P003-v2.0 — Harf jarr recognition
- Historical slot: L04-P03
- Target competency: K04
- Reference: QS 1:2
- Target span: `لِلَّهِ`
- Response class: direct recognition
- Prompt: segmentasikan marker preposisional dari isim pada target.
- Expected: `لِـ` = harf jarr; `الله` = isim after the preposition.
- Critical misconception: treating `لله` as an unanalyzed lexical whole.
- Feature ceiling: no predicate-fronting claim.
- Ambiguity: LOW
- Quality status: DRAFT-REPLACEMENT

### ARB-PL-L04-P004-v2.0 — Independent pronoun recognition
- Historical slot: L04-P04
- Target competency: K05
- Reference: QS 112:1
- Target span: `هُوَ`
- Response class: prerequisite/direct
- Prompt: klasifikasikan `هو` pada tingkat bentuk dasar.
- Expected: dhamir munfashil / independent pronoun.
- Critical misconception: treating the pronoun as an ordinary lexical noun.
- Feature ceiling: no full nominal predication analysis.
- Ambiguity: LOW
- Quality status: DRAFT-REPLACEMENT

### ARB-PL-L04-P005-v2.0 — Past-tense verb recognition
- Historical slot: L04-P05
- Target competency: K06
- Reference: QS 17:81
- Target span: `جَاءَ`
- Response class: direct/transfer
- Prompt: klasifikasikan bentuk verba pada target sebagai madhi atau mudhari‘.
- Expected: fi‘il madhi.
- Critical misconception: classifying by translation rather than form.
- Feature ceiling: no subject relation required.
- Ambiguity: LOW
- Quality status: DRAFT-REPLACEMENT

### ARB-PL-L04-P006-v2.0 — Present/imperfect verb recognition
- Historical slot: L04-P06
- Target competency: K07
- Reference: QS 107:1
- Target span: `يُكَذِّبُ`
- Response class: direct/transfer
- Prompt: klasifikasikan target sebagai fi‘il mudhari‘ atau madhi.
- Expected: fi‘il mudhari‘.
- Critical misconception: relying only on lexical meaning.
- Feature ceiling: no relative-clause analysis.
- Ambiguity: LOW
- Quality status: DRAFT-REPLACEMENT

## 3. Duplicate controls

These replacements deliberately use familiar anchors because the operation is low-level recognition. Production assembly must prevent same verse family from being repeated with near-identical function signatures in the same test form.

## 4. Review gate

Before any promotion:
1. Arabic-content review validates linguistic wording and pedagogical simplification.
2. Quality review checks feature ceiling and prompt objectivity.
3. Function signatures are compared against surviving L04 P31–P36 and other checkpoint anchors.
4. Pilot evidence is required.

## 5. Progress

R2 L04 replacement drafting: **6/30 = 20%**.

No replacement in this file is production-enabled.