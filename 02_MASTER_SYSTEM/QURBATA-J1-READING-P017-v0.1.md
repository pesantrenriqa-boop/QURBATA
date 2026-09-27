# QURBATA JILID 1 — MASTER LATIHAN MEMBACA P017

Status: **CURATED v0.2 — LEXICAL-FIRST / PEDAGOGICAL SAFE**

Authority: `QURBATA-J1-TARTIL-PAGE-REGISTER-FROZEN-v1.0.md` v1.1.  
TARGET P017: `صِ ضِ طِ ظِ`  
REVIEW_ALLOWED: seluruh Fathah P001–P013 + Kasrah P014–P016.

> Prinsip P017: kata Arab nyata didahulukan. TARGET, urutan kompetensi, ketepatan harakat, dan zero pseudo-word tetap lebih tinggi daripada mengejar kuota meaningful.

## HARD GATES
- 24 kelompok.
- C01–C06 = EXACT-2 TARGET-only, unik.
- C07–C24 = EXACT-3, unik, setiap kelompok minimal satu TARGET P017.
- Future Kasrah `عِ` dan seterusnya dilarang.
- Semua unit detached/tunggal.
- Review hanya kompetensi legal sampai P016.
- Kata sumber meaningful tidak boleh diulang dari registry sebelumnya.
- Tidak boleh mengubah harakat kata demi membuatnya tampak bermakna.

## C01–C06 — PENANAMAN EXACT-2
1. صِ ضِ  
2. صِ طِ  
3. صِ ظِ  
4. ضِ طِ  
5. ضِ ظِ  
6. طِ ظِ

## C07–C24 — LATIHAN EXACT-3 LEXICAL-FIRST
7. **وَ صِ لَ** ← `وَصِلَ` = telah sampai / tersambung [MSL VERIFIED]  
8. **خَ صِ مَ** ← `خَصِمَ` = berselisih / menjadi lawan [MSL VERIFIED]  
9. **حَ صِ رَ** ← `حَصِرَ` = menjadi sempit / terhalang [MSL VERIFIED]  
10. **بَ صِ رَ** ← `بَصِرَ` = melihat / mengetahui dengan jelas [MSL VERIFIED]  
11. **مَ رِ ضَ** ← `مَرِضَ` = telah sakit [MSL VERIFIED — TARGET ضِ]  
12. **رَ ضِ يَ** ← `رَضِيَ` = telah rela / rida [MSL VERIFIED — TARGET ضِ]  
13. **حَ فِ ظَ** ← `حَفِظَ` = telah menjaga / menghafal [MSL VERIFIED — TARGET ظِ]  
14. **يَ قِ ظَ** ← `يَقِظَ` = terjaga / waspada [MSL VERIFIED — TARGET ظِ]  
15. **فَ طِ نَ** ← `فَطِنَ` = cerdas / tanggap [MSL VERIFIED — TARGET طِ]  
16. **نَ ظِ فَ** ← `نَظِفَ` = menjadi bersih [MSL VERIFIED — TARGET ظِ]  
17. **عَ طِ شَ** ← `عَطِشَ` = telah haus [MSL VERIFIED — TARGET طِ]  
18. صِ حِ نَ [PHONETIC-CURATED]  
19. ضِ خِ رَ [PHONETIC-CURATED]  
20. طِ دِ سَ [PHONETIC-CURATED]  
21. ظِ ذِ فَ [PHONETIC-CURATED]  
22. صِ رِ كَ [PHONETIC-CURATED]  
23. ضِ زِ لَ [PHONETIC-CURATED]  
24. طِ سِ شَ [PHONETIC-CURATED]

## LEXICAL-FIRST AUDIT
Meaningful yang dipertahankan pada P017:
- `وَصِلَ` — TARGET `صِ`.
- `خَصِمَ` — TARGET `صِ`.
- `حَصِرَ` — TARGET `صِ`.
- `بَصِرَ` — TARGET `صِ`.
- `مَرِضَ` — TARGET `ضِ`.
- `رَضِيَ` — TARGET `ضِ`.
- `حَفِظَ` — TARGET `ظِ`.
- `يَقِظَ` — TARGET `ظِ`.
- `فَطِنَ` — TARGET `طِ`.
- `نَظِفَ` — TARGET `ظِ`.
- `عَطِشَ` — TARGET `طِ`.

Dengan optimasi ini target `طِ` tidak lagi hanya diwakili latihan fonetik: `فَطِنَ` dan `عَطِشَ` memberi contoh kata nyata yang harakatnya legal pada P017.

## PEDAGOGICAL RULE
1. Santri membaca bentuk detached terlebih dahulu.
2. Setelah berhasil membaca, guru boleh menunjukkan bentuk tersambung dan maknanya.
3. Makna menjadi penguat asosiasi bunyi–kata, bukan syarat membaca.
4. Kosakata umum, konkret, dan mudah divisualkan diprioritaskan.
5. Kata langka tidak dipilih hanya untuk menaikkan persentase MSL.
6. Pseudo-word tidak boleh diberi arti.
7. Bila kata meaningful aman tersedia, ia menggantikan slot fonetik.
8. Bila tidak tersedia, latihan fonetik curated tetap sah dan lebih baik daripada kata semu.

## COVERAGE
Keempat target P017 kini memiliki representasi meaningful:
- `صِ`: وَصِلَ، خَصِمَ، حَصِرَ، بَصِرَ
- `ضِ`: مَرِضَ، رَضِيَ
- `طِ`: فَطِنَ، عَطِشَ
- `ظِ`: حَفِظَ، يَقِظَ، نَظِفَ

Slot C18–C24 tetap phonetic-curated untuk memperluas review Kasrah legal dan menjaga variasi decoding.

## GLOBAL MSL — NEW P017
USED baru P017:
`وصل`, `خصم`, `حصر`, `بصر`, `مرض`, `رضي`, `حفظ`, `يقظ`, `فطن`, `نظف`, `عطش`.

Semua tetap tunduk pada audit global zero-repeat sebelum renderer produksi.

## QA STATUS
- GROUP_COUNT 24/24 → PASS
- EXACT-2 6/6 → PASS
- EXACT-3 18/18 → PASS
- TARGET-only planting → PASS
- TARGET presence C07–C24 → PASS
- FUTURE KASRAH → 0
- meaningful EXACT-3 → 11/18
- phonetic curated → 7/18
- seluruh TARGET memiliki contoh meaningful → PASS
- pseudo-word berlabel meaningful → 0
- lexical-first policy → ACTIVE

## PRODUCTION NOTE
P017 v0.2 tidak memaksakan 100% meaningful. Prioritas berikutnya adalah mengganti C18–C24 hanya bila ditemukan kata Arab tiga-unit yang benar, harakatnya legal, mengandung TARGET P017, belum pernah digunakan, dan pedagogis untuk pemula. Jika tidak, slot fonetik tetap dipertahankan.