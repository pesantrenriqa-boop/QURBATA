# QURBATA Competency Index (QCI) Architecture V1

## Status
- Version: 1.0.0-draft
- Date: 2026-08-04
- Scope: Fondasi graf kompetensi QURBATA
- Status: ACTIVE DEVELOPMENT

## Tujuan
QURBATA Competency Index (QCI) adalah sumber kebenaran tunggal untuk seluruh kompetensi membaca Al-Qur'an yang digunakan oleh QWO, QPO, QAO, QLO, generator buku, generator ujian, remedial, rapor, dan RIQA OS.

QCI tidak hanya menyimpan daftar materi. QCI menyimpan:
- identitas kompetensi permanen;
- kategori dan dimensi kompetensi;
- prasyarat;
- tingkat penguasaan;
- aturan aktivasi;
- aturan pemeliharaan melalui murojaah;
- hubungan dengan level, jilid, dan produk pembelajaran.

## Prinsip Arsitektur
1. ID kompetensi bersifat permanen dan tidak berubah ketika urutan jilid berubah.
2. Urutan pengajaran disimpan sebagai pemetaan, bukan ditanam di dalam ID.
3. Setiap kompetensi dapat memiliki lebih dari satu prasyarat.
4. Setiap objek belajar harus dapat ditelusuri kembali ke kompetensi QCI.
5. Kompetensi baru tidak boleh menghapus kompetensi lama dari latihan kumulatif.
6. Status "pernah diajarkan" tidak sama dengan "telah dikuasai".
7. Setiap kompetensi memiliki indikator Recognition, Reading, Fluency, dan Retention.

## Dimensi Kompetensi

### 1. Grapheme
Kemampuan mengenali bentuk huruf:
- bentuk mandiri;
- bentuk awal;
- bentuk tengah;
- bentuk akhir;
- huruf yang dapat dan tidak dapat menyambung.

### 2. Visual Family
Kemampuan membedakan keluarga bentuk yang mirip, misalnya:
- ب ت ث;
- ج ح خ;
- د ذ;
- ر ز;
- س ش;
- ص ض;
- ط ظ;
- ع غ;
- ف ق.

### 3. Phonology
Kemampuan menghasilkan bunyi dengan tepat:
- fathah;
- kasrah;
- dhammah;
- mad;
- sukun;
- tanwin;
- tasydid.

### 4. Connection Pattern
Kemampuan membaca pola sambungan dua, tiga, empat, dan lebih banyak huruf.

### 5. Orthography
Kemampuan mengenali bentuk tulis khusus, termasuk:
- hamzah qatha';
- hamzah washal;
- ta marbuthah;
- alif maqshurah;
- alif lam;
- bentuk rasm Utsmani yang relevan.

### 6. Morphology
Kemampuan mengenali keluarga kata dan perubahan bentuk, tanpa menjadikan analisis sharaf sebagai beban pembaca pemula.

### 7. Fluency
Kemampuan membaca kata, frasa, dan potongan ayat secara akurat, stabil, dan semakin otomatis.

### 8. Tajwid Applied
Kompetensi tajwid yang hanya diaktifkan ketika fondasi bacaan yang dibutuhkan sudah dikuasai.

## Model Penguasaan
Setiap kompetensi dinilai pada empat tahap:

1. RECOGNITION
   - mengenali pola secara visual atau auditori.
2. READING
   - membaca pola dengan benar pada contoh terarah.
3. FLUENCY
   - membaca konsisten pada variasi kata dan frasa.
4. RETENTION
   - mempertahankan kemampuan pada materi berikutnya.

Status implementasi:
- NOT_INTRODUCED
- INTRODUCED
- PRACTICING
- MASTERED
- RETENTION_RISK
- REMEDIAL

## Hubungan Antarobjek

```text
QCI (competency graph)
  ↓
QWO (word objects)
  ↓
QPO (phrase objects)
  ↓
QAO (ayah segment objects)
  ↓
QLO (learning objects)
  ↓
Book / Test / Remedial / Report Generator
  ↓
RIQA OS
```

## Aturan Dependency Graph
- Tidak boleh ada dependency melingkar.
- Semua prasyarat wajib menggunakan ID QCI yang valid.
- Kompetensi kompleks harus dipecah jika indikator kelulusannya berbeda.
- Sebuah kompetensi dapat diperkenalkan setelah seluruh prasyarat berstatus minimal MASTERED atau sesuai kebijakan level.
- Generator wajib menolak objek yang mengandung kompetensi di luar whitelist pembelajar.

## Skema Minimal QCI

| Field | Fungsi |
|---|---|
| CompetencyID | ID permanen |
| Code | kode manusiawi |
| NameID | nama Bahasa Indonesia |
| NameAR | nama Arab bila relevan |
| Dimension | dimensi kompetensi |
| Category | kelompok operasional |
| Description | definisi kompetensi |
| Requires | daftar ID prasyarat |
| RecognitionIndicator | indikator pengenalan |
| ReadingIndicator | indikator membaca |
| FluencyIndicator | indikator kelancaran |
| RetentionIndicator | indikator retensi |
| DifficultyBase | kesulitan dasar 1-100 |
| ReviewPriority | prioritas murojaah |
| DefaultSequence | urutan default |
| Status | DRAFT/ACTIVE/HOLD/RETIRED |
| Version | versi definisi |

## Kebijakan Perubahan
- ID tidak boleh digunakan ulang.
- Nama dan deskripsi boleh disempurnakan melalui versioning.
- Perubahan prasyarat harus dicatat sebagai keputusan arsitektur.
- Kompetensi RETIRED tetap disimpan untuk kompatibilitas data lama.
- Pemetaan jilid dan level disimpan pada tabel terpisah agar kurikulum dapat berubah tanpa merusak objek.

## Definition of Done V1
QCI V1 dianggap selesai ketika:
1. kompetensi fondasi huruf, bentuk, harakat, sambungan, mad, tanwin, sukun, tasydid, dan struktur dasar telah memiliki ID;
2. seluruh dependency tervalidasi tanpa siklus;
3. indikator penguasaan tersedia;
4. tersedia mapping awal ke Jilid 1-8;
5. QWO dapat menunjuk QCI secara konsisten;
6. aturan generator dapat mengevaluasi whitelist kompetensi.
