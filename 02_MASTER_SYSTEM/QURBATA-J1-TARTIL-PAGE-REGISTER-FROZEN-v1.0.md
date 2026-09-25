# QURBATA JILID 1 — TARTIL PAGE REGISTER

Status: **FROZEN v1.1 — SOURCE-ALIGNED**  
Effective: 2026-09-25  
Authority isi: master curriculum/spec halaman yang sudah ada di renderer + `QURBATA_TARTIL_BOOK_COMPOSITION_RULES_FROZEN-v1.4.md` status v1.6.6.

> Koreksi v1.1: register v1.0 sebelumnya salah karena memetakan ulang urutan huruf. v1.1 mengembalikan TARGET persis ke spesifikasi halaman yang sudah ada. Generator tidak boleh mengubah urutan kompetensi ini.

## ATURAN STRUKTUR
- `REGULAR`: 2 baris pertama = 6 kelompok EXACT-2 TARGET-only; 6 baris berikut = 18 kelompok EXACT-3, relevan dengan TARGET dan hanya memakai REVIEW_ALLOWED sebagai unsur pendamping.
- `TRANSITION`: aturan REGULAR, tetapi fokus pada perpindahan harakat sesuai TARGET halaman.
- `REVIEW/CURATED`: tidak memakai pola TARGET baru; 24 kelompok harus dikurasi dari kompetensi legal yang disebut.
- `CHECKPOINT`: struktur khusus curated; tidak boleh memakai fallback global.
- Semua huruf Tartil tetap detached/tunggal.
- Kelompok satu huruf dilarang.

## PAGE REGISTER — SESUAI MASTER YANG SUDAH ADA

| Page | Type | TARGET / FOCUS | REVIEW_ALLOWED |
|---|---|---|---|
| P001 | REGULAR-FOUNDATION | بَ تَ ثَ | — |
| P002 | REGULAR | ءَ أَ | P001 |
| P003 | REGULAR | جَ حَ خَ | P001–P002 |
| P004 | REGULAR | دَ ذَ رَ زَ | P001–P003 |
| P005 | REGULAR | سَ شَ | P001–P004 |
| P006 | REGULAR | صَ ضَ | P001–P005 |
| P007 | REGULAR | طَ ظَ | P001–P006 |
| P008 | REGULAR | عَ غَ | P001–P007 |
| P009 | REGULAR | فَ قَ | P001–P008 |
| P010 | CHECKPOINT | تَقْيِيمُ الْفَتْحَةِ | seluruh kompetensi legal P001–P009 |
| P011 | REGULAR | كَ لَ | seluruh Fathah P001–P009 |
| P012 | REGULAR | مَ نَ | P001–P011 |
| P013 | REGULAR | هَ وَ يَ | P001–P012 |
| P014 | TRANSITION | بِ تِ ثِ جِ | seluruh Fathah P001–P013 |
| P015 | REGULAR | حِ خِ دِ ذِ | Fathah + Kasrah P014 |
| P016 | REGULAR | رِ زِ سِ شِ | Fathah + Kasrah P014–P015 |
| P017 | REGULAR | صِ ضِ طِ ظِ | Fathah + Kasrah P014–P016 |
| P018 | REGULAR | عِ غِ فِ قِ | Fathah + Kasrah P014–P017 |
| P019 | REGULAR-CURATED | كِ لِ مِ نِ هِ وِ يِ ءِ إِ | Fathah + Kasrah P014–P018 |
| P020 | CHECKPOINT | تَقْيِيمُ الْفَتْحَةِ وَالْكَسْرَةِ | seluruh kompetensi legal P001–P019 |
| P021 | TRANSITION | بُ تُ ثُ جُ | seluruh Fathah + Kasrah |
| P022 | TRANSITION | حُ خُ دُ ذُ | P001–P021 |
| P023 | TRANSITION | رُ زُ سُ شُ | P001–P022 |
| P024 | TRANSITION | صُ ضُ طُ ظُ | P001–P023 |
| P025 | TRANSITION | عُ غُ فُ قُ | P001–P024 |
| P026 | TRANSITION | كُ لُ مُ نُ | P001–P025 |
| P027 | TRANSITION | هُ وُ يُ ءُ | P001–P026 |
| P028 | REVIEW-CURATED | تَدْرِيبُ الضَّمَّةِ | seluruh Dhammah legal P021–P027 + review terdahulu yang diperlukan |
| P029 | REVIEW-CURATED | مُرَاجَعَةُ الْحَرَكَاتِ | seluruh Fathah + Kasrah + Dhammah legal |
| P030 | REVIEW-CURATED | مُرَاجَعَةٌ شَامِلَةٌ | seluruh kompetensi legal P001–P029 |
| P031 | REVIEW-CURATED | مُرَاجَعَةٌ تَرَاكُمِيَّةٌ | seluruh kompetensi legal P001–P030 |
| P032 | REVIEW-CURATED | مُرَاجَعَةٌ تَرَاكُمِيَّةٌ | seluruh kompetensi legal P001–P031 |
| P033 | REVIEW-CURATED | مُرَاجَعَةٌ تَرَاكُمِيَّةٌ | seluruh kompetensi legal P001–P032 |
| P034 | REVIEW-CURATED | تَدْرِيبٌ خِتَامِيٌّ | seluruh kompetensi legal P001–P033 |
| P035 | REVIEW-CURATED | تَدْرِيبٌ خِتَامِيٌّ | seluruh kompetensi legal P001–P034 |
| P036 | REVIEW-CURATED | تَقْوِيَةٌ تَقْيِيمِيَّةٌ | seluruh kompetensi legal P001–P035 |
| P037 | REVIEW-CURATED | تَقْوِيَةٌ تَقْيِيمِيَّةٌ | seluruh kompetensi legal P001–P036 |
| P038 | REVIEW-CURATED | تَقْوِيَةٌ تَقْيِيمِيَّةٌ | seluruh kompetensi legal P001–P037 |
| P039 | REVIEW-CURATED | مُحَاكَاةُ التَّقْيِيمِ | seluruh kompetensi legal P001–P038 |
| P040 | CHECKPOINT-FINAL | التَّقْيِيمُ الْخِتَامِيُّ | seluruh kompetensi legal Jilid 1 |

## CONTOH SENTINEL P003
TARGET P003 = `جَ حَ خَ`.

Dua baris penanaman wajib enam pasangan unik TARGET-only:
- Baris 1: `جَ حَ` | `جَ خَ` | `حَ جَ`
- Baris 2: `حَ خَ` | `خَ جَ` | `خَ حَ`

Baris 3–8:
- setiap kelompok tepat 3 huruf;
- minimal satu posisi memuat `جَ/حَ/خَ`;
- posisi lain hanya boleh memakai P001–P002 (`بَ تَ ثَ ءَ أَ`) atau TARGET P003;
- tidak boleh ada huruf P004 ke atas;
- tidak boleh ada kelompok 1/2 huruf.

## HARD GATES
1. `TARGET_MISSING` → FAIL untuk REGULAR/TRANSITION.
2. REGULAR/TRANSITION cell 1–6 bukan EXACT-2 → `PLANTING_LENGTH_FAIL`.
3. REGULAR/TRANSITION cell 7–24 bukan EXACT-3 → `PRACTICE_LENGTH_FAIL`.
4. Cell 1–6 mengandung non-TARGET → `COMPETENCY_MISMATCH_FAIL`.
5. Cell 7–24 tidak relevan dengan TARGET → `COMPETENCY_MISMATCH_FAIL`.
6. Unsur di luar TARGET + REVIEW_ALLOWED → `FUTURE_COMPETENCY_FAIL`.
7. Kelompok 1 huruf di mana pun → `SINGLE_LETTER_GROUP_FAIL`.
8. Duplikasi kelompok → `DUPLICATE_GROUP_FAIL`.
9. REVIEW/CHECKPOINT harus memakai daftar curated; fallback algoritmik → `CURATION_REQUIRED_FAIL`.
10. Semua output wajib lolos `DETACHED-LETTER` dan `HA-GLYPH`.

## PRODUCTION RULE
Generator wajib membaca/mencerminkan register ini. Data `intro`/`specs` yang bertentangan dengan register harus membuat build FAIL, bukan memilih salah satunya secara diam-diam.
