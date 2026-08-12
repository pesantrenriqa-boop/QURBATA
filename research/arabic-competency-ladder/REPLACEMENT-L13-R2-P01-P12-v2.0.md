# L13 R2 Replacement — P01–P12 v2.0

**Status:** DRAFT-REPLACEMENT — NOT PRODUCTION ENABLED  
**Checkpoint:** L13  
**Recovery class:** R2 SUMMARY-ONLY → VERSIONED REPLACEMENT  
**Stage:** S3 — Sentence Relations  
**Guardrail:** item harus menilai relasi antarkomponen kalimat sampai ceiling K31–K39; Complex Clause Integration K40+ tidak boleh menjadi syarat full credit.

## P01 — nominal predication anchor
- Canonical ID: `ARB-PL-L13-P001-v2.0`
- Target: nominal predication relation
- Reference: QS 112:2
- Span: `اللَّهُ الصَّمَدُ`
- Prompt: tunjukkan dua unsur utama dalam predikasi nominal dasar.
- Expected: `الله` dan `الصمد` dipetakan sebagai dua unsur predikatif pada ceiling L13.
- Response class: relation
- Ambiguity: LOW
- production_enabled: false

## P02 — nominal pattern contrast
- Canonical ID: `ARB-PL-L13-P002-v2.0`
- Target: contrast of nominal relation types
- Reference: QS 2:2
- Span: `فِيهِ هُدًى`
- Prompt: jelaskan mengapa span ini tidak identik dengan pola dua isim berdampingan seperti `الله الصمد`.
- Expected: adanya prepositional unit membuat surface relation berbeda.
- Response class: contrast/boundary
- Ambiguity: MEDIUM
- production_enabled: false

## P03 — verb–subject relation
- Canonical ID: `ARB-PL-L13-P003-v2.0`
- Target: verbal subject relation
- Reference: QS 17:81
- Span: `جَاءَ الْحَقُّ`
- Prompt: petakan relasi antara verba dan isim sesudahnya.
- Expected: `جاء` ↔ `الحق` as verb–subject/fa'il relation.
- Response class: relation
- Ambiguity: LOW
- production_enabled: false

## P04 — verb–object relation
- Canonical ID: `ARB-PL-L13-P004-v2.0`
- Target: object relation
- Reference: QS 1:5
- Span: `إِيَّاكَ نَعْبُدُ`
- Prompt: petakan fungsi `إياك` terhadap `نعبد` tanpa membahas balaghah taqdim.
- Expected: fronted direct-object relation.
- Response class: relation
- Ambiguity: LOW
- production_enabled: false

## P05 — coordination relation
- Canonical ID: `ARB-PL-L13-P005-v2.0`
- Target: coordination relation
- Reference: QS 112:3
- Span: `لَمْ يَلِدْ وَلَمْ يُولَدْ`
- Prompt: tunjukkan dua unit verbal yang dikoordinasikan dan marker penghubungnya.
- Expected: two verbal units coordinated by `و`.
- Response class: relation
- Ambiguity: LOW
- production_enabled: false

## P06 — demonstrative local relation
- Canonical ID: `ARB-PL-L13-P006-v2.0`
- Target: demonstrative relation
- Reference: QS 2:2
- Span: `ذَٰلِكَ الْكِتَابُ`
- Prompt: identifikasi demonstratif dan unsur nominal terkait pada konstruksi lokal.
- Expected: `ذلك` + `الكتاب` relation recognized; no wider clause analysis.
- Response class: relation/boundary
- Ambiguity: MEDIUM
- production_enabled: false

## P07 — relative head–silah relation
- Canonical ID: `ARB-PL-L13-P007-v2.0`
- Target: relative relation
- Reference: QS 107:1
- Span: `الَّذِي يُكَذِّبُ`
- Prompt: petakan hubungan isim maushul dengan unit verbal sesudahnya.
- Expected: `الذي` opens relative unit; `يكذب` belongs to its silah.
- Response class: relation
- Ambiguity: LOW
- production_enabled: false

## P08 — fronted prepositional predication
- Canonical ID: `ARB-PL-L13-P008-v2.0`
- Target: fronted predicate relation
- Reference: QS 45:36
- Span: `لِلَّهِ الْحَمْدُ`
- Prompt: petakan hubungan jar-majrur depan dengan unsur nominal sesudahnya pada ceiling L13.
- Expected: fronted prepositional predication recognized.
- Response class: transfer/relation
- Ambiguity: LOW
- production_enabled: false

## P09 — two local relations in coordinated frame
- Canonical ID: `ARB-PL-L13-P009-v2.0`
- Target: local relation retention under coordination
- Reference: QS 1:5
- Span: `إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ`
- Prompt: petakan dua object–verb pairs dan marker koordinasi di antaranya.
- Expected: `إياك↔نعبد`; `إياك↔نستعين`; `و` coordinates the units.
- Response class: prerequisite/integration
- Ambiguity: LOW
- production_enabled: false

## P10 — conditional-domain boundary
- Canonical ID: `ARB-PL-L13-P010-v2.0`
- Target: condition-marker local domain
- Reference: QS 110:1
- Span: `إِذَا جَاءَ نَصْرُ اللَّهِ`
- Prompt: identifikasi marker pembuka dan unit lokal dalam domain awalnya; jangan analisis response/result.
- Expected: `إذا` opens domain containing `جاء نصر الله`; result relation excluded.
- Response class: boundary
- Ambiguity: MEDIUM
- production_enabled: false

## P11 — subject versus object contrast
- Canonical ID: `ARB-PL-L13-P011-v2.0`
- Target: relation discrimination
- Reference: QS 54:1
- Span: `اقْتَرَبَتِ السَّاعَةُ`
- Prompt: tentukan apakah `الساعة` berfungsi sebagai subject/fa'il atau object pada relation lokal.
- Expected: subject/fa'il relation.
- Response class: transfer/contrast
- Ambiguity: LOW
- production_enabled: false

## P12 — first sentence-relations integrative discriminator
- Canonical ID: `ARB-PL-L13-P012-v2.0`
- Target: sampled sentence relations
- References: QS 112:2; QS 17:81; QS 1:5
- Prompt: lakukan tiga operasi terpisah: nominal predication, verb–subject relation, dan fronted object–verb relation. Jangan masuk ke Complex Clause Integration.
- Expected: three local relation maps correctly produced.
- Response class: integrative relation
- Ambiguity: LOW
- scoring: segmented 3-part rubric.
- production_enabled: false

## Batch audit

L13 R2 replacement coverage opened: **12/24 = 50%**.

All records are new v2.0 replacements and remain disabled until canonical K-ID alignment, Arabic-content review, duplicate-function audit, and quality screening.