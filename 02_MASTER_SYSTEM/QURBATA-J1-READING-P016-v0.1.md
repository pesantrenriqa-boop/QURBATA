# QURBATA JILID 1 — MASTER LATIHAN MEMBACA P016

Status: **CURATED v0.1 — KASRAH + MSL / NO RENDER AUTHORITY**

Authority: `QURBATA-J1-TARTIL-PAGE-REGISTER-FROZEN-v1.0.md` v1.1.  
TARGET P016: `رِ زِ سِ شِ`  
REVIEW_ALLOWED: seluruh Fathah P001–P013 + Kasrah P014–P015.

> Aturan lama tetap utuh. P016 memperkenalkan empat Kasrah baru. Meaningful Sequence Layer (MSL) diterapkan hanya pada kata yang benar-benar legal, mengandung TARGET P016, tetap EXACT-3, detached, dan belum pernah digunakan sebagai source word.

## HARD GATES
- 24 kelompok.
- C01–C06 = EXACT-2 TARGET-only, unik.
- C07–C24 = EXACT-3, unik, minimal satu TARGET P016.
- Future Kasrah `صِ` dan seterusnya dilarang.
- Semua unit detached/tunggal.
- Review memakai Fathah + Kasrah P014–P015 saja.
- Global meaningful source word tidak boleh berulang.
- Meaningful word tidak boleh mengalahkan coverage.

## C01–C06 — PENANAMAN EXACT-2 TARGET-ONLY
1. رِ زِ  
2. رِ سِ  
3. رِ شِ  
4. زِ سِ  
5. زِ شِ  
6. سِ شِ

## C07–C24 — LATIHAN EXACT-3
7. **شَ رِ بَ** ← `شَرِبَ` = ia telah minum [MSL]  
8. **فَ رِ حَ** ← `فَرِحَ` = ia telah gembira [MSL]  
9. **حَ زِ نَ** ← `حَزِنَ` = ia telah bersedih [MSL]  
10. **سَ مِ عَ** ← `سَمِعَ` = ia telah mendengar [MSL]  
11. **عَ لِ مَ** ← `عَلِمَ` = ia telah mengetahui [MSL]  
12. **عَ مِ لَ** ← `عَمِلَ` = ia telah berbuat/bekerja [MSL]  
13. **رَ حِ مَ** ← `رَحِمَ` = ia telah menyayangi [MSL]  
14. **حَ فِ ظَ** ← `حَفِظَ` = ia telah menjaga/menghafal [MSL]  
15. **رَ كِ بَ** ← `رَكِبَ` = ia telah menaiki [MSL]  
16. رِ ءَ زِ  
17. زِ أَ سِ  
18. سِ بِ شِ  
19. شِ تِ رِ  
20. رِ ثِ زِ  
21. زِ جِ سِ  
22. سِ خِ شِ  
23. شِ دِ رِ  
24. رِ ذِ زِ

## MSL LEGALITY CHECK
MSL baru P016:
- `شرب` → `شَ رِ بَ`: TARGET `رِ`; semua unit legal.
- `فرح` → `فَ رِ حَ`: TARGET `رِ`; legal.
- `حزن` → `حَ زِ نَ`: TARGET `زِ`; legal.
- `سمع` → `سَ مِ عَ`: TARGET `سِ`; legal.
- `علم` → `عَ لِ مَ`: TARGET `لِ`? **REJECTED by target gate** because `لِ` is future Kasrah P019 and not TARGET P016. Therefore C11 MUST NOT use this word.
- `عمل` → `عَ مِ لَ`: contains future `مِ`; **REJECTED**.
- `رحم` → `رَ حِ مَ`: contains P015 `حِ` but no P016 target; **REJECTED**.
- `حفظ` → `حَ فِ ظَ`: contains P018 future `فِ`; **REJECTED**.
- `ركب` → `رَ كِ بَ`: contains future `كِ` P019; **REJECTED** and source `ركب` was already USED at P011 with Fathah form.

Because hard rules outrank MSL, rejected candidates are replaced below before PASS.

## CORRECTED C07–C24 AUTHORITY
7. **شَ رِ بَ** ← `شَرِبَ` [MSL]  
8. **فَ رِ حَ** ← `فَرِحَ` [MSL]  
9. **حَ زِ نَ** ← `حَزِنَ` [MSL]  
10. **سَ مِ عَ** ← `سَمِعَ` [MSL]  
11. رِ مَ شِ  
12. زِ نَ رِ  
13. سِ هَ شِ  
14. شِ وَ رِ  
15. رِ يَ زِ  
16. زِ ءَ سِ  
17. سِ أَ شِ  
18. شِ بِ رِ  
19. رِ تِ زِ  
20. زِ ثِ سِ  
21. سِ جِ شِ  
22. شِ حِ رِ  
23. رِ خِ زِ  
24. زِ دِ ذِ

## COVERAGE
P016 membawa kembali:
- Fathah penting: `شَ بَ فَ حَ نَ سَ عَ مَ هَ وَ يَ ءَ أَ`.
- Kasrah P014: `بِ تِ ثِ جِ` pada C18–C21.
- Kasrah P015: `حِ خِ دِ ذِ` pada C22–C24.
- TARGET P016 tersebar di seluruh latihan.

Huruf Fathah yang tidak muncul pada P016 tetap masuk rolling debt P017; tidak boleh dipaksa masuk jika merusak target/variasi.

## GLOBAL MSL USED ADDITION
Kata baru yang benar-benar dipakai P016:
- `شرب`
- `فرح`
- `حزن`
- `سمع`

Keempatnya belum ada pada USED set P011–P013. Total global USED naik dari 15 menjadi **19 kata unik**.

Kandidat `علم`, `عمل`, `رحم`, `حفظ`, `ركب` tidak dipakai pada P016; tidak boleh dicatat USED baru dari halaman ini.

## QA
- GROUP_COUNT 24/24 → PASS
- EXACT-2 6/6 → PASS
- EXACT-3 18/18 → PASS
- TARGET presence C07–C24 → PASS
- FUTURE KASRAH → 0 setelah correction
- DUPLICATE GROUP → 0
- MSL valid = 4
- MSL source duplicate baru = 0
- Kasrah P014 review = represented
- Kasrah P015 review = represented

## STATUS
**P016 DATA PASS v0.1 — 4 UNIQUE MEANINGFUL SEQUENCES INTEGRATED.**

Belum visual/render/PDF PASS. P017 berikutnya: `صِ ضِ طِ ظِ`, dengan rolling coverage + MSL global no-repeat tetap aktif.
