# QLO Batch 0002 — Whole Quran Selection Design

Status: ACTIVE STANDARD

## Prinsip

Sumber QURBATA adalah seluruh Al-Qur'an 30 juz. Pemilihan tidak mengikuti urutan juz, tetapi mengikuti kesiapan kompetensi.

## Pipeline

Quran Corpus
→ Analisis bentuk kata
→ Kompetensi yang dibutuhkan
→ Dependency check
→ Pedagogical scoring
→ QLO selection
→ Page generator

## Objek

### QWO
Quran Word Object

Satu kata Al-Qur'an yang dipilih untuk latihan tartil.

### QPO
Quran Phrase Object

Gabungan 2-5 kata untuk transisi membaca frasa.

### QAO
Quran Ayah Object

Potongan ayat untuk tingkat lanjut.

### QSO
Quran Surah Object

Target membaca surah utuh.

## Aturan Seleksi

Kata dari seluruh juz dapat dipilih jika:

- memenuhi kompetensi halaman;
- seluruh kompetensi prasyarat sudah aktif;
- tidak memiliki hukum bacaan yang belum diperkenalkan;
- memiliki nilai pedagogis yang sesuai.

## Scoring

Setiap objek akan memiliki:

- DifficultyScore
- PedagogicalScore
- FrequencyScore
- ReviewWeight

## Target

QURBATA Jilid 1-8 menghasilkan kemampuan membaca mushaf 30 juz dengan tartil bertahap.
