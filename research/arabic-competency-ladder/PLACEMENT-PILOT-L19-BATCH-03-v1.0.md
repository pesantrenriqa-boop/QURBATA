# Placement Pilot L19 — Batch 03 v1.0

**Status:** POOL COMPLETE — READY FOR CONTENT QUALITY REVIEW, NON-AUTHORITATIVE  
**Branch:** `agent/quranic-arabic-competency-ladder`  
**Scope:** L19 P25–P36 completion + final audit  
**Competency band:** K40–K57  
**Parents:** `PLACEMENT-PILOT-L19-BATCH-01-v1.0.md`, `PLACEMENT-PILOT-L19-BATCH-02-v1.0.md`

## 1. Tujuan

Menutup pool L19 dari 24/36 menjadi **36/36**, memperkuat K45–K50, menambah integrative discriminators dengan ambiguity lebih rendah, lalu menjalankan PREMATURE/K58+ leakage audit dan simulasi assembly enam item.

## 2. Items P25–P36

### L19-P25 — K45 reconstruction with explicit local roles
- Target: K45
- Prerequisite: K31/K37
- Reference: QS 30:4
- Target span: `لِلَّهِ الْأَمْرُ مِن قَبْلُ وَمِن بَعْدُ`
- Response class: reconstruction/relation
- Prompt: identifikasi predikasi inti dan bedakan material adverbial tambahan tanpa mengubah urutan ayat menjadi parafrasa bebas.
- Expected: `لله` dipetakan secara predikatif dengan `الأمر`; `من قبل ومن بعد` dipertahankan sebagai material tambahan lokal, bukan inti predikasi.
- Critical misconception: seluruh span dianggap satu relasi datar atau diterjemahkan sebagai pengganti parsing.
- Error: E01/E05/E08
- Ambiguity: MEDIUM
- Status: PILOT REVIEW

### L19-P26 — K46 modifier-chain lower-ambiguity anchor
- Target: K46
- Prerequisite: K31/K36
- Reference: QS 103:3
- Target span: `الَّذِينَ آمَنُوا وَعَمِلُوا الصَّالِحَاتِ`
- Response class: integration
- Prompt: petakan relative head dan dua predikasi verbal terkoordinasi di dalam silah.
- Expected: `الذين` membuka relative unit; `آمنوا` dan `عملوا الصالحات` berada di dalam silah dan dikoordinasikan dengan `و`.
- Critical misconception: unit kedua dianggap keluar dari relative scope.
- Error: E05/E08
- Ambiguity: LOW
- Status: PILOT INTEGRATIVE

### L19-P27 — K47 embedded object relation transfer
- Target: K47
- Prerequisite: K33/K36
- Reference: QS 107:1–2
- Target span: `الَّذِي يُكَذِّبُ بِالدِّينِ ... الَّذِي يَدُعُّ الْيَتِيمَ`
- Response class: transfer/integration
- Prompt: bedakan relative unit yang hanya memuat complement preposisional dari relative unit yang memuat objek langsung.
- Expected: `يكذب بالدين` dipetakan dengan complement preposisional; `يدع اليتيم` memuat relasi verba–objek langsung.
- Critical misconception: semua complement pascaverba dianggap maf'ul bih langsung.
- Error: E05/E06/E07
- Ambiguity: LOW
- Status: PILOT TRANSFER CONTRAST

### L19-P28 — K48 passive domain transfer
- Target: K48
- Prerequisite: K32/K40
- Reference: QS 81:1
- Target span: `إِذَا الشَّمْسُ كُوِّرَتْ`
- Response class: transfer/integration
- Prompt: pertahankan domain `إذا` dan identifikasi relation lokal nominal–verbal pada passive frame tanpa menjelaskan seluruh rangkaian surah.
- Expected: `إذا` membuka domain; `الشمس` berada pada frame lokal dengan verba pasif `كورت`; analysis stops at local structural relation.
- Critical misconception: domain marker membuat peserta berhenti melakukan local parsing.
- Error: E05/E06/E08
- Ambiguity: MEDIUM
- Status: PILOT TRANSFER REVIEW

### L19-P29 — K49 complexity discriminator
- Target: K49
- Prerequisite: K38/K43
- Reference: QS 17:81
- Target span: `جَاءَ الْحَقُّ وَزَهَقَ الْبَاطِلُ`
- Response class: contrast/discrimination
- Prompt: apakah koordinasi dua klausa sederhana ini sudah cukup untuk dianggap nested complex dependency?
- Expected: tidak; ia menunjukkan coordinated clauses, tetapi bukan nested dependency hanya karena terdiri dari dua klausa.
- Critical misconception: semua multi-clause structures dianggap nested.
- Error: E07/E08
- Ambiguity: LOW
- Status: PILOT NEGATIVE CONTROL

### L19-P30 — K50 prerequisite integrity in nested frame
- Target: K50
- Prerequisite: K32/K33/K36
- Reference: QS 2:3
- Target span: `الَّذِينَ يُؤْمِنُونَ بِالْغَيْبِ وَيُقِيمُونَ الصَّلَاةَ`
- Response class: prerequisite/integration
- Prompt: sebelum memberi kredit integrasi, tunjukkan relative head, scope silah, dan object relation lokal `يقيمون الصلاة`.
- Expected: ketiga prerequisite relation benar; integrasi tidak diberi kredit bila salah satu fondasi gagal.
- Critical misconception: mengenali `الذين` lalu menebak scope tanpa parsing local roles.
- Error: E04/E05/E08
- Ambiguity: LOW
- Status: PILOT PREREQUISITE

### L19-P31 — K51 internal coordination under conditional domain
- Target: K51
- Prerequisite: K34/K40
- Reference: QS 2:286
- Target span: `إِن نَّسِينَا أَوْ أَخْطَأْنَا`
- Response class: integration
- Prompt: petakan conditional domain dan koordinasi internal dengan `أو` tanpa menganggap salah satu unit sebagai result clause.
- Expected: kedua verba berada di dalam domain syarat yang sama dan dikoordinasikan oleh `أو`.
- Critical misconception: coordinator internal diperlakukan sebagai boundary domain.
- Error: E05/E08
- Ambiguity: LOW
- Status: PILOT

### L19-P32 — K52 explicit result transfer
- Target: K52
- Prerequisite: K40/K41
- Reference: QS 4:59
- Target span: `فَإِن تَنَازَعْتُمْ فِي شَيْءٍ فَرُدُّوهُ إِلَى اللَّهِ`
- Response class: transfer/relation
- Prompt: tandai protasis dan result unit, lalu jelaskan fungsi `فـ` pada response boundary.
- Expected: `إن تنازعتم في شيء` = protasis; `فردوه إلى الله` = response/result.
- Critical misconception: prepositional material di tengah dianggap memutus protasis.
- Error: E05/E06/E08
- Ambiguity: LOW
- Status: PILOT TRANSFER

### L19-P33 — K53 relative scope integration
- Target: K53
- Prerequisite: K36/K42
- Reference: QS 103:3
- Target span: `الَّذِينَ آمَنُوا وَعَمِلُوا الصَّالِحَاتِ وَتَوَاصَوْا بِالْحَقِّ`
- Response class: integration
- Prompt: tentukan scope relative head atas rangkaian predikasi verbal terkoordinasi.
- Expected: seluruh rangkaian verbal target tetap berada dalam silah `الذين` pada ceiling L19.
- Critical misconception: predikasi kedua/ketiga dikeluarkan dari scope relative karena adanya `و`.
- Error: E05/E08
- Ambiguity: MEDIUM
- Status: PILOT INTEGRATIVE REVIEW

### L19-P34 — K54 fronted-object scope transfer
- Target: K54
- Prerequisite: K33/K44
- Reference: QS 1:5
- Target span: `إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ`
- Response class: transfer/discrimination
- Prompt: buktikan bahwa setiap fronted object memiliki local scope terhadap verba masing-masing, bukan shared scope.
- Expected: dua pasangan lokal yang berbeda dipetakan secara eksplisit.
- Critical misconception: satu objek depan dianggap menguasai dua verba.
- Error: E05/E08
- Ambiguity: LOW
- Status: PILOT

### L19-P35 — K56 routing discriminator
- Target: K56
- Prerequisite: K43/K46/K50
- Reference: QS 103:3
- Target span: `الَّذِينَ آمَنُوا وَعَمِلُوا الصَّالِحَاتِ وَتَوَاصَوْا بِالْحَقِّ وَتَوَاصَوْا بِالصَّبْرِ`
- Response class: prerequisite/integration
- Prompt: petakan relative scope dan empat predikasi/verbal units terkoordinasi; bila local role parsing gagal, route ke prerequisite band sebelum memberi kredit integrasi.
- Expected: relative scope tetap stabil dan unit-unit lokal dibedakan; koordinasi tidak menghapus scope.
- Critical misconception: benar di awal tetapi scope collapse pada unit terakhir.
- Error: E05/E08
- Ambiguity: MEDIUM
- Status: PILOT ROUTING INTEGRATION

### L19-P36 — Final L19 integrative discriminator
- Target: K40–K57 sampled integration
- Prerequisite: K40/K41/K43/K46/K52/K56
- Reference: QS 3:160
- Target span: `إِن يَنصُرْكُمُ اللَّهُ فَلَا غَالِبَ لَكُمْ وَإِن يَخْذُلْكُمْ فَمَن ذَا الَّذِي يَنصُرُكُم مِّن بَعْدِهِ`
- Response class: integration/discrimination
- Prompt: petakan dua conditional frames, response masing-masing, dan relative unit di dalam response kedua. Jangan memberi tafsir teologis sebagai pengganti relation map.
- Expected: dua protasis dipisahkan; response pertama dan kedua dipetakan; `الذي ينصركم` dikenali sebagai embedded relative unit di dalam response kedua.
- Critical misconception: dua frame condition disatukan atau relative unit dikeluarkan dari scope response.
- Error: E01/E05/E08
- Feature ceiling: no K58+ semantic/discourse interpretation.
- Ambiguity: HIGH; segmented rubric mandatory.
- Status: PILOT FINAL INTEGRATIVE REVIEW

## 3. Final cumulative distribution

Cumulative L19 pool: **36/36 = 100%**.

Coverage:
- K40–K57 all represented;
- condition/result: multiple environments (QS 110, QS 3:160, QS 4:59, QS 2:286 boundaries);
- embedded/relative integration: QS 1:7, QS 2:3, QS 103:3, QS 107:1–3, QS 3:160;
- prerequisite routing: L14–L16 and L17–L18 probes retained;
- negative/contrast: complexity-by-length, coordinated-vs-nested, and K58+ leakage controls;
- transfer: multiple surahs and surface orders.

## 4. PREMATURE / K58+ leakage audit

### PASS
Item remains usable at L19 when all scored operations can be solved from structural evidence up to K57.

### PASS WITH CEILING NOTE
An item may contain semantic/discourse cues only when:
1. they are not required for the correct answer;
2. scoring explicitly ignores interpretation beyond structural relation;
3. rubric is segmented enough to prevent accidental K58+ credit.

### HOLD/PREMATURE
Any item must be removed from automated routing if correct response requires:
- discourse-purpose inference;
- semantic integration beyond the canonical K57 ceiling;
- tafsir knowledge;
- capstone transfer reasoning belonging to S5/K58+.

High-ambiguity items requiring mandatory Arabic-content review include Batch-01 P07/P12, Batch-02 P18/P19/P21, and Batch-03 P36. These are not production-safe until reviewed.

## 5. Six-item assembly simulation

A valid sample assembly can be:
- P23 — prerequisite routing (local subject + coordination)
- P29 — negative control (coordinated ≠ nested)
- P32 — transfer condition-result
- P26 — embedded relative integration
- P35 — complex prerequisite/integration
- P36 — final integrative discriminator

This simulated form satisfies:
- >=4 primary K;
- >=1 prerequisite probe;
- >=1 negative/contrast;
- >=1 transfer;
- >=2 integration items;
- explicit relation/domain mapping.

Working mastery gate remains provisional pending pilot data. A high total score cannot override failure on prerequisite integrity or catastrophic domain/scope collapse.

## 6. Quality-review decision

**Decision: L19 POOL COMPLETE — READY FOR CONTENT QUALITY REVIEW, NOT PRODUCTION-FROZEN.**

Before operational use:
1. Arabic-content review all MEDIUM/HIGH ambiguity items;
2. remove or rewrite any K58+ leakage;
3. item-quality review for prompt clarity and scoring segmentation;
4. pilot assembly simulation with human examinees;
5. psychometric/cut-score validation;
6. RIQA OS mapping and immutable item-version policy after pilot begins.

## 7. Next work package

Open **L21 Placement Pilot — S5 Qur'anic Integration/Capstone (K58–K65)** using the same 36-item minimum architecture, but with stronger transfer, cross-relation integration, and capstone safeguards.

## 8. Governance

Research layer only. Completion of the pool does not alter canonical competency definitions or production QURBATA content.