# QWO Batch 0002 Whole Quran Seed Expansion V1

Status: ACTIVE DEVELOPMENT

## Prinsip

Batch ini memperluas QWO dari seluruh sumber Al-Qur'an. Pemilihan tidak berdasarkan urutan juz, tetapi berdasarkan kesiapan kompetensi.

## Seleksi

Setiap kandidat wajib melalui:

- verifikasi sumber ayat;
- analisis bentuk huruf;
- analisis harakat;
- analisis mad/sukun/tanwin/tasydid;
- pemetaan kompetensi prasyarat;
- penentuan jilid minimum.

## Contoh struktur objek

QWO_ID:
QWO-000XXX

ArabicText:
[teks]

Source:
[Surah:Ayah]

TargetCompetencies:
QT-U-XXX

RequiredCompetencies:
QT-U-001 ...

CumulativeCompetencies:
semua kompetensi yang telah dikuasai

Scores:
- DifficultyScore
- PedagogicalScore
- FrequencyScore

Status:
ACTIVE / REVIEW / HOLD

## Catatan produksi

Data pada file ini adalah kerangka ekspansi batch. Pengisian QWO dilakukan bertahap setelah verifikasi mushaf dan kompetensi agar tidak terjadi kesalahan pedagogis.