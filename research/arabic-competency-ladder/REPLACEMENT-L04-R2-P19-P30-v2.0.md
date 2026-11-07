# L04 R2 Replacement — P19–P30 v2.0

**Status:** DRAFT-REPLACEMENT — NOT PRODUCTION ENABLED  
**Checkpoint:** L04  
**Ceiling:** K01–K12  
**Recovery class:** R2 SUMMARY-ONLY → VERSIONED REPLACEMENT  
**Rule:** these are new replacement records, not reconstructions of lost historical wording.

## P19 — K01 transfer: definite noun recognition
- Canonical ID: `ARB-PL-L04-P019-v2.0`
- Target: K01
- Reference: QS 1:2
- Span: `الْحَمْدُ`
- Prompt: identifikasi apakah bentuk target merupakan isim ma'rifah pada ceiling L04 dan sebutkan bukti bentuk yang tampak.
- Expected: isim dengan `الـ`; recognition only.
- Response class: transfer
- Ambiguity: LOW
- production_enabled: false

## P20 — K02 transfer: indefinite noun with tanwin
- Canonical ID: `ARB-PL-L04-P020-v2.0`
- Target: K02
- Reference: QS 2:2
- Span: `هُدًى`
- Prompt: identifikasi status nakirah/tanwin pada bentuk target tanpa menganalisis keseluruhan kalimat.
- Expected: nakirah dengan tanwin; ceiling-safe recognition.
- Response class: transfer
- Ambiguity: LOW
- production_enabled: false

## P21 — K03 contrast: preposition versus conjunction
- Canonical ID: `ARB-PL-L04-P021-v2.0`
- Target: K03
- Reference: QS 1:2
- Span: `لِلَّهِ`
- Prompt: tunjukkan unsur preposisional pada bentuk target dan bedakan dari `و` sebagai conjunction.
- Expected: `لـ` = prepositional element; not conjunction.
- Response class: contrast
- Ambiguity: LOW
- production_enabled: false

## P22 — K04 pronoun recognition transfer
- Canonical ID: `ARB-PL-L04-P022-v2.0`
- Target: K04
- Reference: QS 112:1
- Span: `هُوَ`
- Prompt: klasifikasikan bentuk target pada ceiling K04.
- Expected: dhamir munfashil.
- Response class: transfer
- Ambiguity: LOW
- production_enabled: false

## P23 — K05 past-verb recognition transfer
- Canonical ID: `ARB-PL-L04-P023-v2.0`
- Target: K05
- Reference: QS 17:81
- Span: `جَاءَ`
- Prompt: tentukan kelas verba target pada ceiling K05.
- Expected: fi'il madhi.
- Response class: transfer
- Ambiguity: LOW
- production_enabled: false

## P24 — K06 present-verb recognition transfer
- Canonical ID: `ARB-PL-L04-P024-v2.0`
- Target: K06
- Reference: QS 2:3
- Span: `يُؤْمِنُونَ`
- Prompt: tentukan kelas verba target tanpa meminta analisis infleksi lanjut.
- Expected: fi'il mudhari'.
- Response class: transfer
- Ambiguity: LOW
- production_enabled: false

## P25 — K07 command recognition transfer
- Canonical ID: `ARB-PL-L04-P025-v2.0`
- Target: K07
- Reference: QS 112:1
- Span: `قُلْ`
- Prompt: identifikasi kelas verba target.
- Expected: fi'il amr.
- Response class: transfer
- Ambiguity: LOW
- production_enabled: false

## P26 — K08 nominal-pair boundary
- Canonical ID: `ARB-PL-L04-P026-v2.0`
- Target: K08
- Reference: QS 112:2
- Span: `اللَّهُ الصَّمَدُ`
- Prompt: apakah span memuat dua unsur nominal yang dapat dikenali pada ceiling K08? Jangan lakukan i'rab penuh.
- Expected: ya; dua unsur nominal dikenali, full predication analysis excluded.
- Response class: boundary
- Ambiguity: MEDIUM
- ceiling_note: score category recognition only.
- production_enabled: false

## P27 — K09 prepositional phrase transfer
- Canonical ID: `ARB-PL-L04-P027-v2.0`
- Target: K09
- Reference: QS 114:1
- Span: `بِرَبِّ النَّاسِ`
- Prompt: identifikasi prepositional unit dan isim yang langsung mengikuti marker.
- Expected: `بـ` + `رب`; extended idafah analysis excluded.
- Response class: transfer/boundary
- Ambiguity: LOW
- production_enabled: false

## P28 — K10 verb + visible noun relation-lite
- Canonical ID: `ARB-PL-L04-P028-v2.0`
- Target: K10
- Reference: QS 54:1
- Span: `اقْتَرَبَتِ السَّاعَةُ`
- Prompt: tunjukkan verba dan isim zhahir yang terkait langsung; jangan meminta terminology di atas ceiling.
- Expected: `اقتربت` = verba; `الساعة` = isim zhahir terkait sebagai participant utama pada relation-lite.
- Response class: relation-lite transfer
- Ambiguity: LOW
- production_enabled: false

## P29 — K11 pronoun + nominal relation-lite
- Canonical ID: `ARB-PL-L04-P029-v2.0`
- Target: K11
- Reference: QS 112:1
- Span: `هُوَ اللَّهُ`
- Prompt: identifikasi pronoun dan unsur nominal sesudahnya; jangan menetapkan satu full i'rab sebagai satu-satunya jawaban.
- Expected: `هو` = dhamir; `الله` = unsur nominal terkait pada ceiling K11.
- Response class: boundary/alternate-analysis safe
- Ambiguity: MEDIUM
- alternate_analysis_policy: full syntactic labeling is outside scored target.
- production_enabled: false

## P30 — K12 integration-lite final replacement
- Canonical ID: `ARB-PL-L04-P030-v2.0`
- Target: K12 with sampled K01–K11 prerequisites
- References: QS 112:1–2
- Spans: `قُلْ هُوَ اللَّهُ أَحَدٌ` / `اللَّهُ الصَّمَدُ`
- Prompt: lakukan tiga operasi ceiling-safe: identifikasi satu fi'il amr, satu dhamir, dan dua unsur nominal; jangan melakukan tafsir atau i'rab penuh.
- Expected: `قل` = amr; `هو` = dhamir; valid nominal examples identified from selected spans.
- Response class: integration-lite
- Ambiguity: MEDIUM
- scoring: segmented; each operation independently scored.
- production_enabled: false

## Completion audit

R2 L04 historical missing range P01–P30 now has explicit versioned replacement coverage:
- P01–P06: replacement batch 01
- P07–P18: replacement batch 02
- P19–P30: this batch

**Replacement coverage: 30/30 = 100%.**

This does not mean production approval. Next gates: duplicate-function audit against surviving L04 P31–P36, Arabic-content review, quality disposition, registry normalization, pilot evidence, and production enablement.