# Placement Pilot L19 — Batch 01 v1.0

**Status:** WORKING RESEARCH — NON-AUTHORITATIVE  
**Branch:** `agent/quranic-arabic-competency-ladder`  
**Scope:** adaptive placement checkpoint L19  
**Competency band:** K40–K57  
**Stage:** S4 — Complex Clause Integration  
**Guardrail:** item boleh menguji integrasi klausa sampai K57, tetapi tidak boleh membutuhkan S5/K58+ Qur'anic integration/capstone reasoning untuk memperoleh jawaban benar.

## 1. Tujuan

Membuka bank placement L19 setelah L04, L10, dan L13 masing-masing mencapai pool minimum 36/36. L19 menguji kemampuan mempertahankan relasi sintaksis ketika struktur memuat lebih dari satu unit, subordinasi, condition-result, embedded/relative material, atau urutan permukaan yang tidak sederhana.

Target pool minimum: **36 item**. Batch pertama: **12 item**.

## 2. Item schema

Item ID; target K; prerequisite; Qur'anic reference; target span; response class; prompt; expected response; scoring key; critical misconception; error code; feature ceiling; ambiguity; review status.

## 3. Pilot items P01–P12

### L19-P01 — Complex conditional anchor
- Target: K40
- Prerequisite: K39
- Reference: QS 110:1–2
- Target span: `إِذَا جَاءَ نَصْرُ اللَّهِ وَالْفَتْحُ ۝ وَرَأَيْتَ النَّاسَ يَدْخُلُونَ`
- Response class: clause integration
- Prompt: petakan domain pembuka `إذا` dan perluasan unit yang berada sebelum respons utama; jangan masuk ke interpretasi retoris surah.
- Expected: peserta mempertahankan `إذا` sebagai pembuka domain dan mengenali bahwa material verbal/koordinatif berikut berada dalam konstruksi kompleks sebelum respons berikutnya.
- Critical misconception: menganggap setiap `و` otomatis menutup domain conditional.
- Error: E05/E08
- Feature ceiling: no discourse/rhetorical interpretation.
- Ambiguity: MEDIUM
- Status: PILOT WITH REVIEW NOTE

### L19-P02 — Condition-result relation
- Target: K41
- Prerequisite: K39/K40
- Reference: QS 110:1–3
- Target span: `إِذَا جَاءَ نَصْرُ اللَّهِ ... فَسَبِّحْ بِحَمْدِ رَبِّكَ`
- Response class: relation/integration
- Prompt: identifikasi protasis/domain awal dan unit respons yang ditandai setelahnya.
- Expected: domain `إذا ...` dipetakan sebagai bagian awal; `فسبح ...` dikenali sebagai respons/result pada ceiling K41.
- Critical misconception: marker `فـ` dikenali tetapi relation condition-result tidak dapat dipetakan.
- Error: E05/E08
- Ambiguity: MEDIUM
- Status: PILOT

### L19-P03 — Embedded relative inside larger nominal frame
- Target: K42
- Prerequisite: K31/K36
- Reference: QS 1:7
- Target span: `صِرَاطَ الَّذِينَ أَنْعَمْتَ عَلَيْهِمْ`
- Response class: embedded relation
- Prompt: tentukan unit relative dan jelaskan bagaimana ia berada di dalam frasa nominal yang lebih besar tanpa memberi tafsir makna ayat.
- Expected: `الذين أنعمت عليهم` dikenali sebagai relative unit yang memodifikasi/menentukan unsur `صراط` melalui konstruksi lokal yang relevan.
- Critical misconception: relative clause dianalisis terpisah sehingga hubungannya dengan frame nominal hilang.
- Error: E05/E08
- Ambiguity: MEDIUM
- Status: PILOT REVIEW

### L19-P04 — Multi-verb coordination with retained local roles
- Target: K43
- Prerequisite: K32/K33/K34/K38
- Reference: QS 2:3
- Target span: `يُؤْمِنُونَ بِالْغَيْبِ وَيُقِيمُونَ الصَّلَاةَ وَمِمَّا رَزَقْنَاهُمْ يُنْفِقُونَ`
- Response class: integration
- Prompt: petakan tiga unit verbal dan pertahankan complement/object lokal masing-masing sambil menunjukkan koordinasinya.
- Expected: tiga predikasi verbal lokal dibedakan; complement/object tidak dipindahkan ke verba yang salah; koordinasi antarkomponen dikenali.
- Critical misconception: parsing benar pada satu unit tetapi runtuh ketika tiga unit digabung.
- Error: E05/E08
- Ambiguity: MEDIUM
- Status: PILOT INTEGRATIVE

### L19-P05 — Fronting inside complex verbal frame
- Target: K44
- Prerequisite: K33/K37
- Reference: QS 1:5
- Target span: `إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ`
- Response class: integration/contrast
- Prompt: pertahankan relasi objek–verba pada dua unit dengan objek didahulukan dan koordinasi di tengah.
- Expected: setiap `إياك` dipetakan ke verba lokalnya; `و` menghubungkan dua unit; posisi depan tidak mengubah fungsi objek.
- Critical misconception: fronting mengubah objek menjadi mubtada' atau objek pertama dipasangkan ke kedua verba.
- Error: E05/E08
- Ambiguity: LOW
- Status: PILOT

### L19-P06 — Reconstruction boundary
- Target: K45
- Prerequisite: K31–K44 sampled
- Reference: QS 39:3
- Target span: `أَلَا لِلَّهِ الدِّينُ الْخَالِصُ`
- Response class: reconstruction/boundary
- Prompt: tentukan relasi inti yang dapat dipulihkan secara lokal tanpa mengubah urutan Qur'ani atau mengandalkan terjemahan.
- Expected: peserta mengidentifikasi predikasi inti `لله` ↔ `الدين الخالص` dan modifier lokal; tidak diwajibkan membuat parafrasa bebas.
- Critical misconception: reconstruction berarti menulis ulang ayat menurut urutan bahasa Indonesia.
- Error: E01/E05/E08
- Ambiguity: MEDIUM
- Status: PILOT BOUNDARY

### L19-P07 — Modifier-chain integration
- Target: K46
- Prerequisite: K31/K35/K36
- Reference: QS 1:7
- Target span: `صِرَاطَ الَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ الْمَغْضُوبِ عَلَيْهِمْ`
- Response class: integration/boundary
- Prompt: tunjukkan dua lapisan modifikasi/dependency lokal yang dapat dibedakan tanpa memutus frame utama.
- Expected: peserta membedakan relative unit `الذين ...` dari material `غير ...` sebagai lapisan dependency lain, sambil mempertahankan keterkaitan dengan frame `صراط`.
- Critical misconception: semua material pasca-`صراط` dianggap satu clause datar.
- Error: E05/E08
- Ambiguity: HIGH; content review mandatory.
- Status: PILOT REVIEW/HOLD-CANDIDATE

### L19-P08 — Complex verbal complement boundary
- Target: K47
- Prerequisite: K32/K33/K38
- Reference: QS 107:2
- Target span: `فَذَٰلِكَ الَّذِي يَدُعُّ الْيَتِيمَ`
- Response class: integration
- Prompt: petakan frame demonstratif/relative dan relasi verba–objek di dalam unit relative.
- Expected: `ذلك` berada pada frame utama; `الذي ...` membentuk relative unit; `يدع` berelasi dengan `اليتيم` sebagai objek lokal.
- Critical misconception: objek pada embedded unit diperlakukan sebagai unsur langsung frame utama.
- Error: E05/E08
- Ambiguity: MEDIUM
- Status: PILOT

### L19-P09 — Passive/subject relation in larger domain
- Target: K48
- Prerequisite: K32/K38
- Reference: QS 99:1
- Target span: `إِذَا زُلْزِلَتِ الْأَرْضُ زِلْزَالَهَا`
- Response class: integration/transfer
- Prompt: pertahankan domain `إذا` sambil menentukan relasi lokal verba pasif dengan `الأرض`; jangan menilai seluruh jawab `إذا`.
- Expected: domain conditional/temporal dikenali; `الأرض` dipetakan pada relasi lokal yang sesuai dengan verba pasif; material sesudahnya tidak menghapus domain awal.
- Critical misconception: keberadaan `إذا` membuat peserta gagal melakukan parsing lokal di dalam domain.
- Error: E05/E06/E08
- Ambiguity: MEDIUM
- Status: PILOT TRANSFER REVIEW

### L19-P10 — Negative control: complexity is not mere length
- Target: K49
- Prerequisite: K38
- Reference: QS 112:1–2
- Target span: `قُلْ هُوَ اللَّهُ أَحَدٌ ۝ اللَّهُ الصَّمَدُ`
- Response class: negative/contrast
- Prompt: apakah dua ayat pendek yang berdampingan otomatis membentuk satu complex-clause dependency yang harus dianalisis sebagai unit K49?
- Expected: tidak; panjang atau jumlah ayat bukan bukti adanya dependency kompleks tertentu.
- Critical misconception: kompleksitas ditentukan oleh banyaknya token/ayat, bukan relation structure.
- Error: E07/E08
- Ambiguity: LOW
- Status: PILOT NEGATIVE CONTROL

### L19-P11 — Prerequisite integrity under embedding
- Target: K50
- Prerequisite: K31/K32/K33/K36
- Reference: QS 107:1–2
- Target span: `أَرَأَيْتَ الَّذِي يُكَذِّبُ بِالدِّينِ ۝ فَذَٰلِكَ الَّذِي يَدُعُّ الْيَتِيمَ`
- Response class: prerequisite/integration
- Prompt: tunjukkan dua relative units dan satu verb–object relation di dalamnya; jika prerequisite relation gagal, jangan memberi kredit hanya karena peserta mengenali `الذي`.
- Expected: dua `الذي` dikenali bersama silah lokalnya; relasi `يدع`–`اليتيم` dipertahankan sebagai embedded verbal relation.
- Critical misconception: marker recognition dianggap sama dengan integrated dependency mastery.
- Error: E04/E05/E08
- Ambiguity: MEDIUM
- Status: PILOT PREREQUISITE INTEGRATION

### L19-P12 — First integrative discriminator
- Target: K40–K57 sampled integration
- Prerequisite: K39/K41/K43/K44
- Reference: QS 110:1–3
- Target span: full three-verse local structure
- Response class: integration/discrimination
- Prompt: petakan (a) pembuka/domain conditional, (b) minimal dua unit verbal di dalam domain, dan (c) unit respons/result; jangan menggunakan tafsir sebagai pengganti bukti sintaksis.
- Expected: peserta mempertahankan domain dan unit lokal secara konsisten serta menunjukkan respons `فسبح...` pada ceiling L19.
- Critical misconception: mengenali semua marker tetapi gagal membangun relation map.
- Error: E01/E05/E08
- Feature ceiling: no K58+ semantic/discourse capstone inference.
- Ambiguity: HIGH; segmented rubric mandatory.
- Status: PILOT INTEGRATIVE REVIEW

## 4. Batch-01 distribution audit

Pool size: **12/36 = 33.33%**.

Initial coverage:
- K40 conditional-domain expansion: P01/P12
- K41 condition-result: P02/P12
- K42 embedded relative: P03
- K43 multi-verb coordination: P04
- K44 fronting in integrated frame: P05
- K45 reconstruction boundary: P06
- K46 modifier-chain integration: P07
- K47 embedded verbal relation: P08
- K48 local relation inside larger domain: P09
- K49 complexity contrast: P10
- K50 prerequisite under embedding: P11
- K51–K57: explicit independent coverage still required in P13–P24.

## 5. Expansion priorities P13–P24

1. independent evidence for K51–K57;
2. additional condition/result environments outside QS 110;
3. nested/embedded relations with strict local scoring;
4. prerequisite-routing probes capable of distinguishing L14–L18 gaps;
5. at least two negative controls where surface length looks complex but target relation is not;
6. HOLD any item requiring K58+ semantic/discourse/capstone reasoning.

## 6. Working six-item assembly gate

A selected L19 checkpoint form must include:
- >=4 distinct primary K;
- >=1 prerequisite-integrity probe;
- >=1 negative/contrast item;
- >=1 transfer item;
- >=2 complex-integration items;
- >=1 item requiring explicit domain/relation mapping rather than category naming.

Failure opens local diagnosis inside L14–L19 rather than resetting to earlier stages unless prerequisite probes independently demonstrate lower-stage gaps.

## 7. Governance

Research layer only. No production freeze. Arabic-content review is mandatory for all MEDIUM/HIGH ambiguity items. Promotion requires item-quality review, pilot evidence, cut-score validation, and RIQA OS mapping.