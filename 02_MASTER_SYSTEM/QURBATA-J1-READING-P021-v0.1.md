# QURBATA JILID 1 — MASTER LATIHAN MEMBACA P021

Status: **CURATED v0.1 — TRANSITION DHAMMAH / LEXICAL-FIRST**

Authority: `QURBATA-J1-TARTIL-PAGE-REGISTER-FROZEN-v1.0.md` v1.1.  
TYPE: TRANSITION  
TARGET P021: `بُ تُ ثُ جُ`  
REVIEW_ALLOWED: seluruh Fathah + Kasrah P001–P020.

> P021 adalah gerbang Dhammah. Santri harus menangkap perubahan bunyi **u** tanpa kehilangan otomatisasi Fathah dan Kasrah.

## HARD GATES
- 24 kelompok.
- C01–C06 = EXACT-2 TARGET-only, unik.
- C07–C24 = EXACT-3, unik, minimal satu TARGET P021.
- Dhammah selain `بُ تُ ثُ جُ` dilarang.
- Fathah dan Kasrah sebelumnya legal sebagai review.
- Semua unit detached/tunggal.
- Tidak ada sukun, tasydid, tanwin, atau mad baru.
- Meaningful word harus cocok huruf + harakat secara persis.
- Tidak ada pseudo-word yang diberi arti.
- Global zero-repeat aktif untuk NEW MSL.

## C01–C06 — PENANAMAN EXACT-2
1. بُ تُ
2. بُ ثُ
3. بُ جُ
4. تُ ثُ
5. تُ جُ
6. ثُ جُ

## C07–C24 — EXACT-3 LEXICAL-FIRST
7. **كُ تُ بُ** [REJECT — كُ future Dhammah]
> Bentuk `كُتُبُ` tidak legal karena `كُ` baru diperkenalkan P026. Tidak masuk authority.

7. **تُ بِ عَ** ← `تُبِعَ` = telah diikuti [MSL VERIFIED — TARGET تُ]
8. **تُ رِ كَ** ← `تُرِكَ` = telah ditinggalkan [MSL VERIFIED — TARGET تُ]
9. **تُ لِ يَ** ← `تُلِيَ` = telah dibacakan [MSL VERIFIED — TARGET تُ]
10. **بُ عِ ثَ** ← `بُعِثَ` = telah diutus / dibangkitkan [MSL VERIFIED — TARGET بُ]
11. **بُ لِ يَ** ← `بُلِيَ` = telah diuji / menjadi usang [MSL VERIFIED — TARGET بُ]
12. **جُ عِ لَ** ← `جُعِلَ` = telah dijadikan [MSL VERIFIED — TARGET جُ]
13. **جُ مِ عَ** ← `جُمِعَ` = telah dikumpulkan [MSL VERIFIED — TARGET جُ]
14. **جُ هِ لَ** ← `جُهِلَ` = tidak diketahui / telah tidak dikenali [MSL VERIFIED — TARGET جُ]
15. **ثُ بِ تَ** ← `ثُبِتَ` = telah ditetapkan / terbukti [MSL VERIFIED — TARGET ثُ]
16. **ثُ نِ يَ** ← `ثُنِيَ` = telah dilipat / dibengkokkan [MSL VERIFIED — TARGET ثُ]
17. بُ تِ رَ [PHONETIC-CURATED]
18. تُ جِ لَ [PHONETIC-CURATED]
19. ثُ دِ مَ [PHONETIC-CURATED]
20. جُ رِ نَ [PHONETIC-CURATED]
21. بُ سِ قَ [PHONETIC-CURATED]
22. تُ شِ فَ [PHONETIC-CURATED]
23. ثُ عِ لَ [PHONETIC-CURATED]
24. جُ قِ يَ [PHONETIC-CURATED]

## MEANINGFUL AUDIT — v0.1
NEW MSL awal:
- `تُبِعَ` — diikuti.
- `تُرِكَ` — ditinggalkan.
- `تُلِيَ` — dibacakan.
- `بُعِثَ` — diutus/dibangkitkan.
- `بُلِيَ` — diuji/menjadi usang.
- `جُعِلَ` — dijadikan.
- `جُمِعَ` — dikumpulkan.
- `جُهِلَ` — tidak diketahui.
- `ثُبِتَ` — ditetapkan/terbukti.
- `ثُنِيَ` — dilipat/dibengkokkan.

Meaningful EXACT-3 awal: **10/18**.

## TARGET COVERAGE MEANINGFUL
- `بُ`: بُعِثَ، بُلِيَ
- `تُ`: تُبِعَ، تُرِكَ، تُلِيَ
- `ثُ`: ثُبِتَ، ثُنِيَ
- `جُ`: جُعِلَ، جُمِعَ، جُهِلَ

Semua empat target memperoleh contoh kata nyata.

## PEDAGOGICAL NOTE
Banyak kata legal P021 berbentuk **fi'il mabni lil-majhul** (pasif), misalnya `بُعِثَ`, `جُعِلَ`, dan `جُمِعَ`. Pada tahap Tartil:
1. santri tidak perlu diberi teori nahwu/sharf;
2. fokus pertama tetap decoding `بُ عِ ثَ`;
3. setelah berhasil membaca, guru cukup memberi arti sederhana “telah diutus”;
4. istilah “pasif/majhul” tidak perlu diajarkan pada halaman ini.

Dengan demikian kata tetap autentik tanpa membebani pemula dengan teori.

## HARAKAT PROTECTION
- `كُتُبُ` ditolak walaupun kata nyata karena memuat future Dhammah `كُ`.
- Akar kata yang benar tetapi target Dhammah tidak muncul persis juga ditolak.
- Tidak boleh mengganti Fathah/Kasrah asli suatu kata agar tampak cocok dengan P021.

## GLOBAL MSL — NEW P021
Kandidat USED baru:
`تبع`, `ترك`, `تلي`, `بعث`, `بلي`, `جعل`, `جمع`, `جهل`, `ثبت`, `ثني`.

Wajib audit global terhadap P001–P020 sebelum renderer final.

## QA STATUS
- GROUP_COUNT 24/24 → PASS
- C01–C06 EXACT-2 → PASS
- C01–C06 TARGET-only → PASS
- C07–C24 EXACT-3 → PASS
- C07–C24 target presence → PASS
- future Dhammah in authority → 0
- meaningful EXACT-3 → **10/18**
- phonetic curated → **8/18**
- all four targets meaningful-covered → PASS
- pseudo-word berlabel meaningful → 0
- detached-letter rule → ACTIVE
- renderer/PDF → PENDING

## NEXT OPTIMIZATION
C17–C24 harus dicoba diganti satu per satu dengan kata nyata. Kandidat hanya diterima bila:
1. tepat tiga unit;
2. memuat `بُ/تُ/ثُ/جُ` persis;
3. Dhammah lain tidak muncul;
4. Fathah/Kasrah pendamping sudah legal;
5. source word belum USED;
6. bentuk dan maknanya dapat dipertanggungjawabkan.

**Kebenaran bahasa dan urutan pedagogis tetap lebih tinggi daripada target 18/18 meaningful.**