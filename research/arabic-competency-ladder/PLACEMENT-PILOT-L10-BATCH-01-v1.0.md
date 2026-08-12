# Placement Pilot L10 — Batch 01 v1.0

**Status:** WORKING RESEARCH — NON-AUTHORITATIVE  
**Branch:** `agent/quranic-arabic-competency-ladder`  
**Scope:** adaptive placement checkpoint L10  
**Competency band:** K13–K30  
**Guardrail:** item hanya boleh menuntut operasi sampai checkpoint L10. Struktur Stage 3+ boleh tampak pada ayat hanya jika tidak diperlukan untuk memperoleh jawaban benar; jika tidak, item harus HOLD/PREMATURE.

## 1. Tujuan

Membuka verse-level pilot bank L10 setelah pool L04 mencapai 36/36. L10 menguji controlled morphosyntax: relasi bentuk–fungsi yang lebih kaya daripada L04, tetapi belum mengandalkan sentence-relation reasoning Stage 3.

## 2. Item schema

Setiap item menyimpan: Item ID; target K; prerequisite K; Qur'anic reference; target span; response class; prompt; expected response; scoring key; critical misconception; error code; feature ceiling; ambiguity; review status.

## 3. Pilot items P01–P12

P01–P12 dipertahankan dari batch awal: direct morphology recognition, object recognition, object-vs-subject negative control, coordination boundary/direct coordination, demonstrative recognition/contrast, relative-pronoun recognition/transfer, conditional-marker boundary, serta integrative morphology–relation items.

## 4. Expansion P13–P24

### L10-P13 — Target K15 boundary
- Target: K15
- Prerequisite: K13/K14
- Reference: QS 1:5
- Target span: `نَسْتَعِينُ`
- Response class: classification/boundary
- Prompt: klasifikasikan bentuk verbal target dan tentukan apakah span tunggal ini cukup untuk membuktikan objek langsung zhahir.
- Expected: fi'il mudhari'; tidak ada objek langsung zhahir pada span tunggal.
- Critical misconception: menambahkan objek hanya karena terjemahan membutuhkannya.
- Error: E03/E07
- Ambiguity: LOW
- Status: PILOT BOUNDARY

### L10-P14 — K17 direct marker recognition
- Target: K17
- Reference: QS 112:3
- Target span: `لَمْ يَلِدْ`
- Response class: recognition/classification
- Prompt: identifikasi marker yang memengaruhi bentuk fi'il mudhari' pada span tanpa meminta penjelasan Stage 3.
- Expected: `لم` dikenali sebagai marker yang meng-govern fi'il mudhari' sesudahnya pada ceiling L10.
- Critical misconception: menganggap `لم` hanya unsur terjemahan negatif tanpa efek gramatikal.
- Error: E02/E03
- Ambiguity: LOW
- Status: PILOT

### L10-P15 — K18 contrast control
- Target: K18
- Reference: QS 109:2
- Target span: `لَا أَعْبُدُ`
- Response class: contrast/boundary
- Prompt: tentukan apakah `لا` pada span ini cukup disamakan dengan `لم` dari sisi governance bentuk fi'il.
- Expected: tidak; marker berbeda dan tidak boleh disamakan hanya karena sama-sama bernuansa negatif.
- Critical misconception: semua partikel negatif dianggap satu operasi gramatikal.
- Error: E03/E07
- Ambiguity: MEDIUM
- Status: PILOT NEGATIVE CONTROL

### L10-P16 — K19 direct recognition
- Target: K19
- Reference: QS 2:2
- Target span: `لَا رَيْبَ`
- Response class: recognition/relation-lite
- Prompt: identifikasi marker negatif pada span dan bedakan dari negasi verbal.
- Expected: `لا` dikenali sebagai marker pada struktur nominal; scoring tidak meminta analisis lengkap fungsi lanjutannya.
- Critical misconception: memaksakan pola negasi verbal pada struktur nominal.
- Error: E02/E04
- Feature ceiling: no advanced case explanation required.
- Ambiguity: MEDIUM
- Status: PILOT WITH CEILING NOTE

### L10-P17 — K20 prerequisite probe
- Target: K20
- Prerequisite: K08/K13
- Reference: QS 2:255
- Target span: `اللَّهُ لَا إِلَٰهَ`
- Response class: prerequisite/boundary
- Prompt: identifikasi unsur nominal awal dan marker negatif berikutnya; jangan analisis keseluruhan ayat.
- Expected: `الله` = unsur nominal; `لا` = marker negatif nominal pada target span.
- Critical misconception: gagal mempertahankan kategori unsur ketika struktur menjadi lebih panjang.
- Error: E04/E05
- Ambiguity: MEDIUM
- Status: PILOT PREREQUISITE

### L10-P18 — K21 transfer
- Target: K21
- Prerequisite: K16/K17
- Reference: QS 2:3
- Target span: `وَيُقِيمُونَ الصَّلَاةَ`
- Response class: transfer/relation
- Prompt: identifikasi marker koordinasi dan bentuk verbal sesudahnya tanpa meminta relation Stage 3.
- Expected: `و` = koordinasi; `يقيمون` = fi'il mudhari'.
- Critical misconception: transfer gagal saat marker menempel pada fi'il.
- Error: E05/E06
- Ambiguity: LOW
- Status: PILOT TRANSFER

### L10-P19 — K22 negative control
- Target: K22
- Reference: QS 103:2
- Target span: `إِنَّ الْإِنسَانَ`
- Response class: recognition/contrast
- Prompt: apakah span ini merupakan konstruksi demonstratif atau relative-pronoun?
- Expected: tidak; target membuka konstruksi lain dan bukan K24/K26.
- Critical misconception: menyamakan semua particle-led nominal structures.
- Error: E02/E07
- Ambiguity: LOW
- Status: PILOT NEGATIVE CONTROL

### L10-P20 — K23 direct classification
- Target: K23
- Prerequisite: K08/K13
- Reference: QS 103:2
- Target span: `إِنَّ الْإِنسَانَ لَفِي خُسْرٍ`
- Response class: relation-lite
- Prompt: identifikasi marker pembuka dan unsur nominal yang langsung berada di bawah pengaruhnya, tanpa meminta analisis khabar kompleks.
- Expected: `إنّ` = marker pembuka; `الإنسان` = unsur nominal langsung sesudahnya.
- Critical misconception: menganalisis seluruh struktur semantik untuk menjawab target lokal.
- Error: E04/E05
- Feature ceiling: full khabar analysis not scored.
- Ambiguity: MEDIUM
- Status: PILOT WITH CEILING NOTE

### L10-P21 — K25 contrast demonstrative/relative
- Target: K25
- Prerequisite: K24/K26
- Reference: QS 2:5
- Target span: `أُولَٰئِكَ عَلَىٰ هُدًى`
- Response class: contrast/transfer
- Prompt: identifikasi jenis bentuk awal dan bedakan dari isim maushul.
- Expected: `أولئك` = isim isyarah, bukan isim maushul.
- Critical misconception: mengandalkan makna 'mereka' lalu salah klasifikasi.
- Error: E02/E06/E07
- Ambiguity: LOW
- Status: PILOT CONTRAST TRANSFER

### L10-P22 — K27 direct relation-lite
- Target: K27
- Prerequisite: K26
- Reference: QS 107:1
- Target span: `الَّذِي يُكَذِّبُ`
- Response class: relation-lite
- Prompt: tentukan unsur relative-pronoun dan awal silah tanpa melacak referential dependency lebih tinggi.
- Expected: `الذي` = isim maushul; `يكذب` = awal silah.
- Critical misconception: memasukkan antecedent/resumptive reasoning Stage 3 ke target lokal.
- Error: E04/E05
- Ambiguity: LOW
- Status: PILOT

### L10-P23 — K28 prerequisite/transfer
- Target: K28
- Prerequisite: K13/K16
- Reference: QS 2:4
- Target span: `وَبِالْآخِرَةِ هُمْ يُوقِنُونَ`
- Response class: prerequisite/transfer
- Prompt: identifikasi marker awal, dhamir munfashil, dan fi'il mudhari' yang tampak; hubungan sentence-level penuh tidak dinilai.
- Expected: `و` = koordinasi; `هم` = dhamir munfashil; `يوقنون` = fi'il mudhari'.
- Critical misconception: gagal mengintegrasikan beberapa operasi lokal yang sudah dikuasai.
- Error: E05/E06
- Feature ceiling: no Stage-3 clause relation scoring.
- Ambiguity: MEDIUM
- Status: PILOT PREREQUISITE TRANSFER

### L10-P24 — K29/K30 contrast discriminator
- Target: K29/K30
- Prerequisite: K13
- Reference: QS 110:1
- Target span: `إِذَا جَاءَ نَصْرُ اللَّهِ`
- Response class: contrast/discrimination
- Prompt: identifikasi marker kondisional dan tentukan apakah span ini sudah memuat jawab syarat lengkap.
- Expected: `إذا` = marker kondisional; span ini belum memuat jawab syarat lengkap.
- Critical misconception: menganggap keberadaan marker sudah sama dengan struktur syarat + jawab lengkap.
- Error: E04/E07
- Ambiguity: LOW
- Status: PILOT NEGATIVE/BOUNDARY CONTROL

## 5. Distribution audit after P24

Pool size: **24/36 = 66.67%**.

Coverage status:
- K13–K30 now broadly represented, including previously missing K15, K17–K23, K25, K27–K30;
- direct/classification exposure is adequate for most subskills;
- negative/contrast controls increased through P15, P19, P21, P24;
- prerequisite probes strengthened through P17, P23;
- transfer coverage strengthened through P18, P21, P23;
- integrative coverage still needs expansion in final 12 items.

Remaining gaps before completion:
1. more independent examples for K17–K23;
2. more integrative items combining 2–3 local operations without Stage-3 leakage;
3. at least two additional prerequisite probes;
4. final PREMATURE/feature-ceiling audit across all 36;
5. final six-item assembly simulation.

## 6. Working routing gate

Selected six dari pool L10 harus memuat:
- minimal 4 target K berbeda;
- 1 prerequisite integrity probe;
- 1 contrast/negative control;
- 1 transfer item;
- 1 integrative item.

Mastery sementara tetap bukan skor mentah saja. Kegagalan prerequisite atau transfer membuka diagnosis lokal L05–L10.

## 7. Next batch P25–P36

Final 12 items harus memprioritaskan integrative discrimination, independent examples K17–K23, prerequisite depth, dan PREMATURE audit. Setelah 36/36, status dapat naik menjadi `POOL COMPLETE — READY FOR CONTENT QUALITY REVIEW`, bukan production freeze.

## 8. Governance

Dokumen berada di research layer PR #4. Tidak mengubah registry produksi. Production freeze membutuhkan Arabic-content review, item-quality review, pilot data, dan mapping RIQA OS.