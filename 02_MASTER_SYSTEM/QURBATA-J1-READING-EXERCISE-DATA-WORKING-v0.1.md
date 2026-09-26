# QURBATA JILID 1 — MASTER DATA LATIHAN MEMBACA

Status: **WORKING v0.1 — CURRICULUM FIRST / NO RENDER AUTHORITY**  
Authority target halaman: `QURBATA-J1-TARTIL-PAGE-REGISTER-FROZEN-v1.0.md` (status internal v1.1 SOURCE-ALIGNED).

> File ini adalah sumber isi latihan membaca. Renderer/generator tidak boleh menciptakan kombinasi sendiri. Semua kelompok harus dikurasi di sini terlebih dahulu.

## HARD RULE LATIHAN MEMBACA
1. Halaman REGULAR/TRANSITION = 24 kelompok.
2. Kelompok 01–06 = EXACT-2, TARGET-only, unik.
3. Kelompok 07–24 = EXACT-3, unik, wajib relevan dengan TARGET halaman.
4. Tidak ada huruf/harakat masa depan.
5. Tidak ada kelompok identik dalam halaman yang sama.
6. Semua huruf adalah unit tunggal/detached; spasi menandai batas unit baca.
7. Materi baru harus dominan dalam latihan; review dipakai untuk transfer, bukan untuk menggeser fokus halaman.
8. Variasi posisi TARGET wajib: awal, tengah, akhir.
9. Generator hanya membaca daftar curated. Fallback/random/cycling dilarang.
10. CHECKPOINT/REVIEW akan memiliki bank curated tersendiri; tidak dihasilkan algoritma.

## P001 — بَ تَ ثَ
### Penanaman EXACT-2
1. بَ تَ | 2. بَ ثَ | 3. تَ بَ | 4. تَ ثَ | 5. ثَ بَ | 6. ثَ تَ
### Latihan EXACT-3
7. بَ تَ ثَ | 8. بَ ثَ تَ | 9. تَ بَ ثَ | 10. تَ ثَ بَ | 11. ثَ بَ تَ | 12. ثَ تَ بَ  
13. بَ بَ تَ | 14. بَ بَ ثَ | 15. تَ تَ بَ | 16. تَ تَ ثَ | 17. ثَ ثَ بَ | 18. ثَ ثَ تَ  
19. بَ تَ بَ | 20. بَ ثَ بَ | 21. تَ بَ تَ | 22. تَ ثَ تَ | 23. ثَ بَ ثَ | 24. ثَ تَ ثَ

## P002 — ءَ أَ | review P001
> Karena TARGET hanya dua unit (`ءَ أَ`), enam pasangan TARGET-only yang unik secara urutan tidak mungkin dibuat tanpa pengulangan unit. Maka "TARGET-only" berarti pasangan tetap hanya memakai kedua TARGET; pasangan kelompok tetap unik.
### Penanaman EXACT-2
1. ءَ أَ | 2. أَ ءَ | 3. ءَ ءَ | 4. أَ أَ | 5. ءَ أَ | 6. أَ ءَ

**STATUS P002: BLOCKED — aturan register bertentangan dengan HARD GATE zero-duplicate.**  
Dengan hanya dua TARGET, ruang kombinasi EXACT-2 hanya 4 (`AA, AB, BA, BB`), sehingga tidak mungkin menghasilkan 6 kelompok unik. P002 tidak boleh dipalsukan oleh generator. Keputusan kurikulum diperlukan: (a) P002 penanaman menjadi 4 kelompok, atau (b) izinkan 2 kelompok review P001 pada penanaman, atau (c) definisikan variasi lain yang sah.

## P003 — جَ حَ خَ | review P001–P002
### Penanaman EXACT-2 — FROZEN SENTINEL
1. جَ حَ | 2. جَ خَ | 3. حَ جَ | 4. حَ خَ | 5. خَ جَ | 6. خَ حَ
### Latihan EXACT-3 — curated
7. جَ بَ حَ | 8. حَ تَ خَ | 9. خَ ثَ جَ  
10. بَ جَ خَ | 11. تَ حَ جَ | 12. ثَ خَ حَ  
13. جَ أَ خَ | 14. حَ ءَ جَ | 15. خَ بَ حَ  
16. أَ جَ حَ | 17. ءَ حَ خَ | 18. بَ خَ جَ  
19. جَ ثَ حَ | 20. حَ بَ خَ | 21. خَ تَ جَ  
22. ثَ جَ خَ | 23. تَ خَ حَ | 24. أَ حَ جَ

## P004 — دَ ذَ رَ زَ | review P001–P003
### Penanaman EXACT-2
1. دَ ذَ | 2. دَ رَ | 3. دَ زَ | 4. ذَ رَ | 5. ذَ زَ | 6. رَ زَ
### Latihan EXACT-3
7. دَ بَ ذَ | 8. ذَ تَ رَ | 9. رَ ثَ زَ  
10. بَ دَ زَ | 11. تَ ذَ دَ | 12. ثَ رَ ذَ  
13. دَ جَ رَ | 14. ذَ حَ زَ | 15. رَ خَ دَ  
16. جَ زَ ذَ | 17. حَ دَ رَ | 18. خَ ذَ زَ  
19. دَ أَ زَ | 20. ذَ ءَ رَ | 21. رَ بَ دَ  
22. أَ دَ ذَ | 23. ءَ زَ رَ | 24. بَ رَ زَ

## P005 — سَ شَ | review P001–P004
**STATUS: BLOCKED BY SAME TWO-TARGET PLANTING CONTRADICTION AS P002.**

## P006 — صَ ضَ | review P001–P005
**STATUS: BLOCKED BY SAME TWO-TARGET PLANTING CONTRADICTION AS P002.**

## P007 — طَ ظَ | review P001–P006
**STATUS: BLOCKED BY SAME TWO-TARGET PLANTING CONTRADICTION AS P002.**

## P008 — عَ غَ | review P001–P007
**STATUS: BLOCKED BY SAME TWO-TARGET PLANTING CONTRADICTION AS P002.**

## P009 — فَ قَ | review P001–P008
**STATUS: BLOCKED BY SAME TWO-TARGET PLANTING CONTRADICTION AS P002.**

## CURRICULUM DEFECT FOUND — MUST RESOLVE BEFORE CONTINUING
Register saat ini mensyaratkan sekaligus:
- enam kelompok penanaman EXACT-2;
- TARGET-only;
- semua kelompok unik.

Untuk halaman dengan tepat 2 TARGET, hanya ada 4 pasangan berurutan yang mungkin jika pengulangan unit diizinkan (`AA, AB, BA, BB`), atau hanya 2 jika satu unit tidak boleh berulang dalam kelompok (`AB, BA`). Karena itu P002, P005, P006, P007, P008, P009 tidak dapat memenuhi ketiga syarat sekaligus.

**Keputusan yang direkomendasikan untuk revisi register:** untuk halaman 2-TARGET, 2 baris penanaman tetap 6 kelompok tetapi 4 kelompok pertama TARGET-only unik dan 2 kelompok terakhir boleh TARGET + REVIEW terdahulu, tetap tanpa duplikasi. Ini mempertahankan dua baris penanaman, memperkaya latihan, dan tidak memaksa data palsu.

Sampai keputusan ini dibekukan, renderer dilarang mengisi halaman-halaman tersebut secara otomatis.
