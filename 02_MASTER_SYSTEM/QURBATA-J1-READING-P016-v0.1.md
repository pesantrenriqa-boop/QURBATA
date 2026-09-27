# QURBATA JILID 1 — MASTER LATIHAN MEMBACA P016

Status: **CURATED v0.2 — LEXICAL-FIRST MSL / NO RENDER AUTHORITY**

Authority: `QURBATA-J1-TARTIL-PAGE-REGISTER-FROZEN-v1.0.md` v1.1.  
TARGET P016: `رِ زِ سِ شِ`  
REVIEW_ALLOWED: seluruh Fathah P001–P013 + Kasrah P014–P015.

> Aturan lama tetap utuh. Untuk setiap slot EXACT-3, penyusun WAJIB mencari kata Arab bermakna terlebih dahulu. Slot fonetik hanya boleh dipakai jika tidak ditemukan kandidat yang sekaligus sah secara leksikal, legal secara kompetensi, memuat TARGET P016, unik global, dan tidak merusak coverage.

## HARD GATES
- 24 kelompok.
- C01–C06 = EXACT-2 TARGET-only, unik.
- C07–C24 = EXACT-3, unik, minimal satu TARGET P016.
- Future Kasrah `صِ` dan seterusnya dilarang.
- Semua unit detached/tunggal.
- Review memakai Fathah + Kasrah P014–P015 saja.
- Global meaningful source word tidak boleh berulang.
- Meaningful word tidak boleh mengalahkan coverage.
- Bentuk yang sekadar menyerupai akar Arab tidak boleh diberi label meaningful tanpa verifikasi bentuk/harakat.

## C01–C06 — PENANAMAN EXACT-2
1. رِ زِ | 2. رِ سِ | 3. رِ شِ | 4. زِ سِ | 5. زِ شِ | 6. سِ شِ

## C07–C24 — AUTHORITY
7. **شَ رِ بَ** ← `شَرِبَ` = telah minum [MSL VERIFIED]  
8. **فَ رِ حَ** ← `فَرِحَ` = telah gembira [MSL VERIFIED]  
9. **حَ زِ نَ** ← `حَزِنَ` = telah bersedih [MSL]  
10. **سَ مِ عَ** ← `سَمِعَ` = telah mendengar [MSL VERIFIED]  
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

## LEXICAL-FIRST AUDIT
Kata yang sudah dapat dipertahankan sebagai meaningful pada tahap ini:
- `شَرِبَ` — bentuk leksikal terverifikasi; TARGET `رِ`.
- `فَرِحَ` — bentuk leksikal terverifikasi; TARGET `رِ`.
- `سَمِعَ` — bentuk leksikal terverifikasi; TARGET `سِ`.
- `حَزِنَ` — dipertahankan sebagai kandidat MSL yang sesuai pola P016; wajib tetap tunduk pada registry/verifikasi final sebelum produksi.

Untuk slot 11–24, **tidak boleh langsung diasumsikan sebagai kata**. Kombinasi seperti `رِ مَ شِ`, `زِ نَ رِ`, `سِ هَ شِ`, dst. saat ini berstatus `PHONETIC-CURATED`, bukan meaningful.

Pencarian kandidat meaningful dilakukan dengan filter ketat:
1. tepat 3 unit;
2. harakat persis sesuai kata Arab yang sah;
3. minimal satu `رِ/زِ/سِ/شِ`;
4. unit Kasrah lain hanya dari P014–P015;
5. tidak memakai Kasrah P017+;
6. source word belum pernah USED;
7. tidak menghapus kebutuhan rolling coverage.

Jika kandidat gagal satu filter saja, slot fonetik dipertahankan. **Dilarang menciptakan kata semu demi mencapai 100% meaningful.**

## COVERAGE
Review tetap membawa Fathah dan Kasrah lama. `ءَ` dan `أَ` tetap hadir. Kasrah P014–P015 tetap direpresentasikan. Target P016 hadir di seluruh C07–C24.

## GLOBAL MSL
USED baru P016 yang dipertahankan: `شرب`, `فرح`, `حزن`, `سمع` (subject to final lexical registry QA for every entry). Tidak ada source word yang sengaja diulang.

## QA STATUS
- struktur 6×EXACT-2 + 18×EXACT-3: PASS
- target presence: PASS
- future Kasrah: 0
- duplicate group: 0
- lexical-first policy: ACTIVE
- phonetic slots masih ada: 14
- 100% meaningful: **TIDAK DIPAKSA**

## PRODUCTION NOTE
Sebelum P016 masuk renderer, meaningful entries harus memiliki bukti leksikal/registry; slot tanpa bukti tetap diperlakukan sebagai latihan decoding fonetik. Aturan ini berlaku juga untuk P017–P040.
