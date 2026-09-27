# QURBATA JILID 1 — P010 CHECKPOINT FATHAH

Status: **CURATED v0.1 — DATA ONLY / NO RENDER AUTHORITY**  
Authority: `QURBATA-J1-TARTIL-PAGE-REGISTER-FROZEN-v1.0.md` v1.1.  
Focus P010: `تَقْيِيمُ الْفَتْحَةِ` — seluruh kompetensi legal P001–P009.

> P010 adalah evaluasi, bukan halaman pengenalan huruf baru. Karena itu tidak memakai pola 6 TARGET-only + 18 target-practice. Semua kelompok dikurasi untuk menguji keterbacaan seluruh huruf Fathah yang telah dipelajari.

## KOMPETENSI LEGAL P010
`بَ تَ ثَ ءَ أَ جَ حَ خَ دَ ذَ رَ زَ سَ شَ صَ ضَ طَ ظَ عَ غَ فَ قَ`

Total = **22 kompetensi**.

## STRUKTUR EVALUASI
- 24 kelompok total.
- Kelompok 01–06 = EXACT-2, sebagai pemanasan/evaluasi cepat.
- Kelompok 07–24 = EXACT-3.
- Semua unit detached/tunggal.
- Zero duplicate.
- Tidak ada huruf di luar P001–P009.
- Tidak ada huruf baru P011 (`كَ لَ`) atau sesudahnya.
- `أَ` dan `ءَ` tetap dinilai sebagai kompetensi berbeda.
- Pemerataan diukur dari **jumlah kemunculan per huruf pada seluruh P010**, bukan dari keluarga huruf saja.

## BARIS 1–2 — EXACT-2
1. بَ ءَ  
2. تَ أَ  
3. ثَ جَ  
4. حَ خَ  
5. دَ ذَ  
6. رَ زَ  

## BARIS 3–8 — EXACT-3
7. سَ شَ صَ  
8. ضَ طَ ظَ  
9. عَ غَ فَ  
10. قَ بَ تَ  
11. ءَ ثَ حَ  
12. أَ جَ خَ  
13. دَ رَ سَ  
14. ذَ زَ شَ  
15. صَ طَ عَ  
16. ضَ ظَ غَ  
17. فَ قَ بَ  
18. تَ ءَ دَ  
19. ثَ أَ ذَ  
20. جَ حَ رَ  
21. خَ زَ صَ  
22. سَ ضَ فَ  
23. شَ طَ قَ  
24. ظَ عَ غَ

## FREQUENCY AUDIT P010
Total unit = `6×2 + 18×3 = 66`.

| Huruf | Count |
|---|---:|
| بَ | 3 |
| تَ | 3 |
| ثَ | 3 |
| ءَ | 3 |
| أَ | 3 |
| جَ | 3 |
| حَ | 3 |
| خَ | 3 |
| دَ | 3 |
| ذَ | 3 |
| رَ | 3 |
| زَ | 3 |
| سَ | 3 |
| شَ | 3 |
| صَ | 3 |
| ضَ | 3 |
| طَ | 3 |
| ظَ | 3 |
| عَ | 3 |
| غَ | 3 |
| فَ | 3 |
| قَ | 3 |

**Hasil:** 22 huruf × 3 kemunculan = **66/66 unit**. Tidak ada huruf yang lebih dominan dan tidak ada huruf yang hilang.

## QA GATES
- GROUP_COUNT = 24/24 → PASS
- EXACT-2 = 6/6 → PASS
- EXACT-3 = 18/18 → PASS
- LEGAL_COMPETENCY = P001–P009 only → PASS
- FUTURE_COMPETENCY = 0 → PASS
- ZERO_DUPLICATE = PASS
- COVERAGE = 22/22 → PASS
- FREQUENCY_BALANCE = setiap kompetensi tepat 3× → PASS
- `أَ` coverage = 3× → PASS
- `ءَ` coverage = 3× → PASS

## PEDAGOGICAL NOTE
P010 sengaja dibuat sangat seimbang karena berfungsi sebagai checkpoint Fathah. Pola ini **tidak otomatis diterapkan pada halaman regular**: halaman regular tetap harus mendominankan TARGET baru dan memakai review secara kumulatif. P010 hanya menguji apakah seluruh kompetensi Fathah P001–P009 masih terbaca sebelum peserta masuk ke `كَ لَ` pada P011.

## STATUS
**P010 DATA PASS v0.1 — MENUNGGU INTEGRASI KE MASTER DATA DAN AUDIT VISUAL KEMUDIAN.**

Renderer belum diberi kewenangan membuat atau mengganti isi P010.
