# Placement Pilot L04 — Batch 01 v1.0

**Status:** WORKING RESEARCH — QUALITY-REVIEW READY, NON-AUTHORITATIVE  
**Branch:** `agent/quranic-arabic-competency-ladder`  
**Scope:** adaptive placement checkpoint L04  
**Guardrail:** item hanya boleh menuntut operasi yang telah tersedia sampai checkpoint L04; struktur lebih tinggi boleh muncul hanya bila tidak diperlukan untuk menjawab target atau item harus ditandai REVIEW/PREMATURE.

## 1. Tujuan

Membangun verse-level pilot bank checkpoint L04 sebagai implementasi awal adaptive placement architecture. Pool minimum 36 item kini lengkap untuk menguji recognition, classification, prerequisite integrity, contrast/negative control, transfer, dan integrative discrimination sebelum pilot operasional.

## 2. Item record schema

Setiap item wajib menyimpan: Item ID; checkpoint/level; target competency; prerequisite; referensi Qur'an; target span; response class; prompt; expected response; scoring key; critical misconception; error code; feature ceiling; ambiguity flag; review status.

## 3. Pilot pool P01–P30

P01–P30 dipertahankan dari batch sebelumnya. Coverage yang telah dibangun mencakup K01–K12 dengan direct recognition, negative controls, prerequisite probes, transfer, dan integrative items. Anchor penting termasuk QS 112:2 `اللَّهُ الصَّمَدُ`, QS 17:81 `جَاءَ الْحَقُّ`, QS 57:3 `هُوَ الْأَوَّلُ`, QS 39:3 `لِلَّهِ الدِّينُ`, dan QS 45:36 `لِلَّهِ الْحَمْدُ`.

## 4. Final balancing items P31–P36

### L04-P31 — Prerequisite integrity K08
- Target: K08 simple nominal predication
- Prerequisite: K01/K02
- Reference: QS 85:12
- Target span: `بَطْشَ رَبِّكَ شَدِيدٌ`
- Response class: prerequisite/boundary
- Prompt: jangan analisis seluruh struktur; tentukan apakah span ini aman sebagai contoh inti mubtada' + khabar dua-token sederhana.
- Expected: tidak; struktur permukaan lebih kompleks daripada pola inti K08.
- Critical misconception: menyamakan semua predikasi nominal dengan template dua-token sederhana.
- Error: E04/E07
- Feature ceiling: negative/boundary judgment only.
- Ambiguity: MEDIUM
- Status: PILOT BOUNDARY CONTROL

### L04-P32 — Integrative K09 + K02
- Target: K09 + K02
- Prerequisite: K01/K04
- Reference: QS 2:2
- Target span: `فِيهِ هُدًى`
- Response class: integration/boundary
- Prompt: identifikasi marker preposisional pada target dan tentukan apakah unsur sesudahnya memenuhi pola isim zhahir langsung setelah huruf jar.
- Expected: `في` dikenali sebagai preposisi; pola target bukan huruf jar + isim zhahir langsung karena pronomina terikat hadir pada `فيه`.
- Critical misconception: menganggap semua konstruksi yang mengandung preposisi otomatis sama dengan K09.
- Error: E03/E05/E07
- Feature ceiling: tidak meminta analisis pronomina terikat penuh.
- Ambiguity: MEDIUM
- Status: PILOT INTEGRATIVE BOUNDARY

### L04-P33 — Integrative K06 + K10
- Target: K06/K10
- Prerequisite: K01
- Reference: QS 54:1
- Target span: `اقْتَرَبَتِ السَّاعَةُ`
- Response class: integration/relation
- Prompt: klasifikasikan fi'il dan identifikasi fa'il zhahir pada span.
- Expected: `اقتربت` = fi'il madhi; `الساعة` = fa'il zhahir.
- Critical misconception: menganggap ta' pada fi'il sebagai bukti bahwa subjek tidak mungkin berupa isim zhahir sesudahnya.
- Error: E03/E04/E05
- Ambiguity: LOW
- Status: PILOT INTEGRATIVE

### L04-P34 — Integrative K05 + K08/K11
- Target: K05/K08/K11
- Prerequisite: K01
- Reference: QS 59:22
- Target span: `هُوَ اللَّهُ`
- Response class: integration/transfer
- Prompt: identifikasi jenis `هو` dan hubungan predikatif dasar pada span tanpa memasuki struktur lanjutan ayat.
- Expected: `هو` = dhamir munfashil sebagai unsur awal/mubtada' sederhana; `الله` = unsur predikat nominal pada ceiling L04.
- Critical misconception: mengenali pronoun tetapi gagal mengintegrasikannya ke predikasi nominal dasar.
- Error: E04/E06
- Ambiguity: LOW
- Status: PILOT INTEGRATIVE TRANSFER

### L04-P35 — Integrative K04 + K09 + K12
- Target: K04/K09/K12
- Prerequisite: K01/K08
- Reference: QS 30:4
- Target span: `لِلَّهِ الْأَمْرُ`
- Response class: integration/transfer
- Prompt: segmentasikan huruf jar + isim dan tentukan fungsi predikatif depan pada span minimal.
- Expected: `لِـ` = huruf jar; `الله` = isim majrur secara bentuk; `لله` = jar-majrur predikatif depan; `الأمر` = unsur nominal sesudahnya.
- Critical misconception: mampu mengenali huruf jar tetapi gagal mengintegrasikan konstruksi ke predikasi depan.
- Error: E04/E05/E06
- Ambiguity: LOW
- Status: PILOT INTEGRATIVE TRANSFER

### L04-P36 — Final integrative discriminator
- Target: K01–K12 sampled integration
- Prerequisite: K01/K04/K05/K06/K08/K10/K11/K12
- Reference: QS 112:1–2
- Target spans: `هُوَ اللَّهُ أَحَدٌ` / `اللَّهُ الصَّمَدُ`
- Response class: integration/discrimination
- Prompt: pada dua span pendek, tunjukkan (a) dhamir munfashil, (b) unsur nominal, dan (c) satu predikasi nominal sederhana; jangan memakai terjemahan sebagai bukti.
- Expected: `هو` dikenali sebagai dhamir munfashil; `الله/أحد/الصمد` dikenali sebagai unsur nominal sesuai target; peserta dapat menunjukkan predikasi nominal dasar pada span yang dipilih tanpa membutuhkan analisis di atas L04.
- Critical misconception: jawaban berbasis hafalan arti tanpa operasi linguistik atau mencampur seluruh ayat menjadi analisis tingkat lanjut.
- Error: E01/E04/E05/E06
- Feature ceiling: scoring hanya pada operasi K01–K12.
- Ambiguity: MEDIUM; item wajib memakai rubric tersegmentasi.
- Status: PILOT FINAL DISCRIMINATOR WITH CEILING NOTE

## 5. Final distribution audit — 36 items

Pool size: **36/36 = 100% target minimum**.

Functional coverage (multi-tag allowed):
- direct/recognition/classification: >=12 exposures across P01–P13 and supporting items;
- negative/contrast/boundary: >=6 (P03, P15, P19, P20, P21, P31/P32 plus earlier controls);
- prerequisite-integrity/relation: >=6 (P04, P14, P16, P17, P24 and P31/P33 supporting probes);
- transfer: >=6 (P05, P18, P22, P23 and additional transfer records through P30/P34/P35);
- integrative: >=6 (P06, P17 and P33–P36 plus earlier integrative records).

Because tags overlap, counts are not intended to sum to 36. The gate is minimum functional exposure, not mutually exclusive buckets.

Competency coverage: **K01–K12 all represented**, with higher emphasis on K08–K12 in the second half of the pool.

## 6. PREMATURE / feature-ceiling audit

### PASS — usable at L04 ceiling
Items whose answer can be obtained using only the intended L04 operation remain PILOT.

### PASS WITH CEILING NOTE
Items containing surface structures above L04 may remain only when:
1. higher structure is explicitly outside the target span/scoring;
2. correct response does not require naming that higher structure;
3. rubric states exactly what is ignored.

This applies especially to P06, P21, P31, P32, and P36.

### HOLD / REWRITE trigger
Any content reviewer who finds that an item cannot be answered correctly without a K13+ operation must mark it **PREMATURE** and remove it from automated routing until rewritten. No item is promoted to production merely because the verse is authentic.

## 7. Provisional routing rule

Checkpoint L04 tidak dinyatakan mastered hanya dari total skor mentah.

Working core gate:
- minimum 5/6 selected core items benar;
- prerequisite-integrity item benar;
- transfer item benar;
- tidak ada critical misconception fondasional;
- selected six must sample at least four distinct competencies and include one contrast/boundary item.

Jika 4/6 atau prerequisite/transfer gagal, sistem membuka 3–5 diagnostic probes lokal dari pool 36 sebelum menentukan placement.

## 8. Quality-review decision

**Decision: L04 POOL COMPLETE — READY FOR CONTENT QUALITY REVIEW, NOT YET PRODUCTION-FROZEN.**

Before operational use:
1. Arabic-content reviewer validates target spans and expected linguistic labels;
2. item-quality reviewer checks prompt clarity, distractor logic, and ceiling leakage;
3. ambiguous/medium items receive explicit scoring rubrics;
4. a six-item assembly simulation verifies adaptive routing balance;
5. pilot data is required before final cut-score freeze.

## 9. Next work package

1. Freeze a reviewed L04 subset only after corrections from quality review.
2. Open **L10 placement pilot** using the same 36-item minimum architecture but targeting K13–K30.
3. Keep L04 items immutable by ID after pilot data collection begins; revisions then require a new item version.

## 10. Governance note

Dokumen ini berada di research layer PR #4 dan tidak mengubah registry produksi QURBATA. Promotion ke assessment production membutuhkan freeze terpisah setelah content review, pilot/psychometric review, dan mapping RIQA OS.