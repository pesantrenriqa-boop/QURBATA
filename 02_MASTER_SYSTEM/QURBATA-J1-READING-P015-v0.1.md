# QURBATA JILID 1 — MASTER LATIHAN MEMBACA P015

Status: **CURATED v0.1 — KASRAH / NO RENDER AUTHORITY**

Authority: `QURBATA-J1-TARTIL-PAGE-REGISTER-FROZEN-v1.0.md` v1.1.  
TARGET P015: `حِ خِ دِ ذِ`  
REVIEW_ALLOWED: seluruh Fathah P001–P013 + Kasrah P014 (`بِ تِ ثِ جِ`).

> Aturan lama tidak berubah. P015 memperkenalkan empat Kasrah baru. Review Fathah yang menjadi debt dari P014 diprioritaskan tanpa menggeser TARGET P015.

## HARD GATES
- 24 kelompok.
- C01–C06 EXACT-2 TARGET-only, unik.
- C07–C24 EXACT-3, unik, minimal satu TARGET P015.
- Kasrah masa depan `رِ` dan seterusnya dilarang.
- Semua unit detached/tunggal.
- MSL tidak boleh mengalahkan target/coverage.

## C01–C06 — PENANAMAN EXACT-2
1. حِ خِ  
2. حِ دِ  
3. حِ ذِ  
4. خِ دِ  
5. خِ ذِ  
6. دِ ذِ

## C07–C24 — LATIHAN EXACT-3
7. حِ فَ خِ  
8. خِ قَ دِ  
9. دِ كَ ذِ  
10. ذِ لَ حِ  
11. حِ مَ دِ  
12. خِ نَ ذِ  
13. دِ هَ حِ  
14. ذِ وَ خِ  
15. حِ يَ دِ  
16. خِ ءَ ذِ  
17. دِ أَ حِ  
18. ذِ بِ خِ  
19. حِ تِ دِ  
20. خِ ثِ ذِ  
21. دِ جِ حِ  
22. ذِ بَ خِ  
23. حِ سَ شَ  
24. خِ عَ غَ

## COVERAGE DEBT RESOLUTION
Debt P014: `فَ قَ كَ لَ مَ نَ هَ وَ يَ`.

P015 resolves seluruh debt tersebut:
- C07 `فَ`
- C08 `قَ`
- C09 `كَ`
- C10 `لَ`
- C11 `مَ`
- C12 `نَ`
- C13 `هَ`
- C14 `وَ`
- C15 `يَ`

Tambahan review:
- `ءَ` C16
- `أَ` C17
- Kasrah P014: `بِ تِ ثِ جِ` pada C18–C21
- Fathah lain tetap diputar pada C22–C24.

## MSL
Tidak ada MSL baru yang dipaksakan pada v0.1. Semua kandidat meaningful harus cocok persis dengan harakat legal dan tetap mengandung TARGET P015. Jika tidak, latihan fonetik curated dipertahankan.

Global meaningful USED tetap 15; duplicate baru = 0.

## QA
- GROUP_COUNT 24/24 → PASS
- EXACT-2 6/6 → PASS
- EXACT-3 18/18 → PASS
- TARGET-only planting → PASS
- TARGET presence practice → PASS
- FUTURE KASRAH → 0
- DUPLICATE GROUP → 0
- P014 Fathah coverage debt 9/9 resolved → PASS
- P014 Kasrah review (`بِ تِ ثِ جِ`) 4/4 represented → PASS

## STATUS
**P015 DATA PASS v0.1.**

Belum visual/render/PDF PASS. P016 berikutnya memperkenalkan `رِ زِ سِ شِ`; review harus tetap memakai Fathah + Kasrah P014–P015 sesuai register, dengan rolling coverage debt dihitung ulang setelah P015.
