# Placement Pilot L04 — Batch 01 v1.0

**Status:** WORKING RESEARCH — NON-AUTHORITATIVE  
**Branch:** `agent/quranic-arabic-competency-ladder`  
**Scope:** adaptive placement checkpoint L04  
**Guardrail:** item hanya boleh menuntut operasi yang telah tersedia sampai checkpoint L04; struktur lebih tinggi boleh muncul hanya bila tidak diperlukan untuk menjawab target atau item harus ditandai REVIEW/PREMATURE.

## 1. Tujuan

Membuka verse-level pilot bank untuk checkpoint L04 sebagai implementasi awal dari adaptive placement architecture. Batch ini menguji format item, scoring, prerequisite integrity, transfer, dan integrative discrimination sebelum pool diperluas menjadi minimum 36 item.

## 2. Item record schema

Setiap item wajib menyimpan:

- Item ID
- Checkpoint/Level
- Target competency/competencies
- Prerequisite competencies
- Qur'anic reference
- Target span
- Response class
- Prompt
- Expected response
- Scoring key
- Critical misconception
- Error code
- Feature ceiling
- Ambiguity flag
- Review status

## 3. Pilot core set

### L04-P01 — Direct recognition
- Target: early nominal recognition
- Reference: QS 112:2
- Target span: `اللَّهُ الصَّمَدُ`
- Response class: recognition/classification
- Prompt: identifikasi unsur nominal utama pada span tanpa meminta analisis struktur di atas feature ceiling.
- Expected: peserta mengenali token nominal yang relevan dan tidak mengubah tugas menjadi terjemahan.
- Critical misconception: lexical guessing tanpa identifikasi bentuk.
- Error: E01/E02
- Ambiguity: LOW
- Status: PILOT

### L04-P02 — Marker recognition
- Target: definite nominal marker
- Reference: QS 1:2
- Target span: `الْحَمْدُ`
- Response class: recognition
- Prompt: tunjukkan penanda bentuk nominal yang menjadi target.
- Expected: pengenalan `الـ` pada isim.
- Critical misconception: menyebut arti kata tetapi gagal mengenali marker.
- Error: E01/E02
- Ambiguity: LOW
- Status: PILOT

### L04-P03 — Contrast control
- Target: nominal definiteness contrast
- Reference: QS 2:2
- Target span: `هُدًى`
- Response class: contrast/classification
- Prompt: klasifikasikan bentuk target terhadap definite/nakirah sesuai operasi yang sudah dikuasai.
- Expected: nakirah/tanwin recognition.
- Critical misconception: semua isim dianggap ma'rifah karena berasal dari ayat Al-Qur'an.
- Error: E02/E03
- Ambiguity: LOW
- Status: PILOT

### L04-P04 — Prerequisite integrity
- Target: frequent preposition recognition + nominal target
- Reference: QS 1:2
- Target span: `لِلَّهِ`
- Response class: recognition/relation-lite
- Prompt: identifikasi huruf jar dan unsur nominal sesudahnya tanpa meminta i'rab lanjutan.
- Expected: mengenali `لِـ` sebagai huruf jar dan `الله` sebagai unsur nominal target.
- Critical misconception: membaca keseluruhan token sebagai satu label leksikal tanpa segmentasi minimal.
- Error: E02/E05
- Ambiguity: LOW
- Status: PILOT

### L04-P05 — Transfer
- Target: independent recognition on unseen Qur'anic span
- Reference: QS 103:2
- Target span: `الْإِنسَانَ`
- Response class: transfer/classification
- Prompt: terapkan operasi pengenalan marker nominal pada contoh baru.
- Expected: pengenalan isim dengan `الـ`; tidak mensyaratkan analisis fungsi sintaksis ayat.
- Critical misconception: transfer gagal ketika kata berbeda dari contoh latihan.
- Error: E06
- Ambiguity: LOW
- Status: PILOT

### L04-P06 — Integrative discriminator
- Target: combine early form recognitions without higher-stage reasoning
- Reference: QS 114:1
- Target span: `بِرَبِّ النَّاسِ`
- Response class: integration
- Prompt: identifikasi marker awal, unsur nominal, dan definite marker yang tampak; jangan meminta analisis dependency di atas checkpoint.
- Expected: mengenali `بِـ` sebagai huruf jar; `رَبِّ` sebagai isim; `النَّاسِ` sebagai isim dengan `الـ`.
- Critical misconception: peserta hanya menerjemahkan span atau memaksakan analisis struktur yang belum menjadi target.
- Error: E01/E02/E05
- Ambiguity: MEDIUM — karena konstruksi idhafah ada pada permukaan; scoring core hanya menghitung operasi yang berada di bawah ceiling dan tidak meminta analisis idhafah.
- Status: PILOT WITH CEILING NOTE

## 4. Provisional routing rule

Checkpoint L04 tidak dinyatakan mastered hanya dari total skor mentah.

Working gate:
- minimum 5/6 core item benar;
- prerequisite-integrity item harus benar;
- transfer item harus benar;
- tidak ada critical misconception yang menunjukkan fondasi recognition belum stabil.

Jika 4/6 atau prerequisite/transfer gagal, sistem membuka diagnostic probe lokal sebelum menentukan placement.

## 5. Quality controls

1. Translation-only answer tidak cukup bila prompt meminta linguistic recognition.
2. Item tidak boleh membutuhkan K di atas checkpoint untuk memperoleh jawaban benar.
3. Kehadiran fitur lebih tinggi pada ayat harus di-lock/ignore secara eksplisit atau item dipindah ke REVIEW.
4. Satu ayat tidak boleh menjadi satu-satunya bukti mastery.
5. Retest memakai verse/span berbeda dengan operasi target yang sama.
6. Semua item sebelum production harus melalui Arabic-content review dan item-quality review.

## 6. Expansion target

Pool L04 minimum sebelum pilot operasional:
- 12 direct items
- 6 negative/contrast controls
- 6 prerequisite-integrity items
- 6 transfer items
- 6 integrative items

Total target: **36 items**.

Batch berikutnya harus memperluas L04-P07+ dengan sebaran surah yang lebih luas, negative controls yang lebih tajam, dan audit PREMATURE untuk setiap span.

## 7. Governance note

Dokumen ini berada di research layer PR #4 dan tidak mengubah registry produksi QURBATA. Promotion ke assessment production membutuhkan freeze terpisah setelah content review, psychometric/pilot review, dan mapping RIQA OS.