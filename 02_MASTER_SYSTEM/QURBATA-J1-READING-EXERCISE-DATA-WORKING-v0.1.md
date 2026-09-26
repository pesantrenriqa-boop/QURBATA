# QURBATA JILID 1 — MASTER DATA LATIHAN MEMBACA

Status: **WORKING v0.3 — CUMULATIVE COVERAGE CONTROLLED / NO RENDER AUTHORITY**

Authority target halaman: `QURBATA-J1-TARTIL-PAGE-REGISTER-FROZEN-v1.0.md` (status internal v1.1 SOURCE-ALIGNED).

> Ini adalah sumber isi latihan membaca. Renderer tidak boleh membuat kombinasi sendiri.

## HARD RULE LATIHAN MEMBACA
1. Halaman REGULAR/TRANSITION = 24 kelompok.
2. Kelompok 01–06 = EXACT-2 dan unik.
3. TARGET >=3: kelompok 01–06 TARGET-only.
4. Halaman 2-TARGET: 01–04 = AB, BA, AA, BB; 05–06 = TARGET + REVIEW legal yang dipilih berdasarkan coverage debt.
5. Kelompok 07–24 = EXACT-3, unik, wajib memuat TARGET halaman.
6. Tidak ada huruf/harakat masa depan.
7. Semua unit tetap detached.
8. Review bukan pilihan bebas: harus mengikuti **cumulative coverage rotation**.
9. Huruf lama tidak wajib muncul di setiap halaman, tetapi tidak boleh hilang terus-menerus. Setelah jumlah huruf lama membesar, pemerataan dinilai dalam rolling window beberapa halaman.
10. `أَ` dan `ءَ` dihitung sebagai dua kompetensi berbeda dan wajib tetap masuk rotasi setelah P002.
11. Posisi TARGET harus tersebar awal–tengah–akhir.
12. Zero duplicate per halaman.
13. Generator hanya membaca curated data; fallback/random/cycling dilarang.

## COVERAGE POLICY
- P003–P005: semua kompetensi lama yang memungkinkan harus tampak kembali dalam halaman atau window sangat dekat.
- P006–P009: review disebar sebagai rotation set agar seluruh huruf lama mendapat giliran; huruf yang tidak muncul pada halaman N mendapat prioritas pada N+1/N+2.
- Tidak boleh ada kompetensi lama yang sengaja terabaikan karena contoh terasa lebih mudah dibuat dengan huruf tertentu.
- Audit wajib menghasilkan tabel frekuensi per huruf dan `last_seen_page`.

## P001 — بَ تَ ثَ
### Penanaman EXACT-2
1. بَ تَ | 2. بَ ثَ | 3. تَ بَ | 4. تَ ثَ | 5. ثَ بَ | 6. ثَ تَ
### Latihan EXACT-3
7. بَ تَ ثَ | 8. بَ ثَ تَ | 9. تَ بَ ثَ | 10. تَ ثَ بَ | 11. ثَ بَ تَ | 12. ثَ تَ بَ  
13. بَ بَ تَ | 14. بَ بَ ثَ | 15. تَ تَ بَ | 16. تَ تَ ثَ | 17. ثَ ثَ بَ | 18. ثَ ثَ تَ  
19. بَ تَ بَ | 20. بَ ثَ بَ | 21. تَ بَ تَ | 22. تَ ثَ تَ | 23. ثَ بَ ثَ | 24. ثَ تَ ثَ

## P002 — ءَ أَ | review P001
### Penanaman EXACT-2
1. ءَ أَ | 2. أَ ءَ | 3. ءَ ءَ | 4. أَ أَ | 5. ءَ بَ | 6. أَ تَ
### Latihan EXACT-3
7. ءَ بَ أَ | 8. أَ تَ ءَ | 9. ءَ ثَ أَ | 10. بَ ءَ أَ | 11. تَ أَ ءَ | 12. ثَ ءَ أَ  
13. ءَ أَ بَ | 14. أَ ءَ تَ | 15. ءَ بَ ثَ | 16. أَ تَ بَ | 17. بَ أَ ثَ | 18. تَ ءَ بَ  
19. ثَ أَ تَ | 20. بَ ثَ ءَ | 21. تَ بَ أَ | 22. ثَ تَ ءَ | 23. بَ ءَ ثَ | 24. تَ أَ ثَ

## P003 — جَ حَ خَ | review بَ تَ ثَ ءَ أَ
### Penanaman EXACT-2
1. جَ حَ | 2. جَ خَ | 3. حَ جَ | 4. حَ خَ | 5. خَ جَ | 6. خَ حَ
### Latihan EXACT-3
7. جَ بَ حَ | 8. حَ تَ خَ | 9. خَ ثَ جَ | 10. بَ جَ خَ | 11. تَ حَ جَ | 12. ثَ خَ حَ  
13. جَ أَ خَ | 14. حَ ءَ جَ | 15. خَ بَ حَ | 16. أَ جَ حَ | 17. ءَ حَ خَ | 18. بَ خَ جَ  
19. جَ ثَ حَ | 20. حَ بَ خَ | 21. خَ تَ جَ | 22. ثَ جَ خَ | 23. تَ خَ حَ | 24. أَ حَ جَ

## P004 — دَ ذَ رَ زَ | review kumulatif P001–P003
### Penanaman EXACT-2
1. دَ ذَ | 2. دَ رَ | 3. دَ زَ | 4. ذَ رَ | 5. ذَ زَ | 6. رَ زَ
### Latihan EXACT-3
7. دَ بَ ذَ | 8. ذَ تَ رَ | 9. رَ ثَ زَ | 10. بَ دَ زَ | 11. تَ ذَ دَ | 12. ثَ رَ ذَ  
13. دَ جَ رَ | 14. ذَ حَ زَ | 15. رَ خَ دَ | 16. جَ زَ ذَ | 17. حَ دَ رَ | 18. خَ ذَ زَ  
19. دَ أَ زَ | 20. ذَ ءَ رَ | 21. رَ بَ دَ | 22. أَ دَ ذَ | 23. ءَ زَ رَ | 24. بَ رَ زَ

## P005 — سَ شَ | COVERAGE REBALANCED
### Penanaman EXACT-2
1. سَ شَ | 2. شَ سَ | 3. سَ سَ | 4. شَ شَ | 5. سَ أَ | 6. شَ ءَ
### Latihan EXACT-3
7. سَ بَ شَ | 8. شَ تَ سَ | 9. سَ ثَ شَ | 10. بَ سَ شَ | 11. تَ شَ سَ | 12. ثَ سَ شَ  
13. سَ جَ حَ | 14. شَ خَ جَ | 15. حَ سَ خَ | 16. جَ شَ حَ | 17. خَ سَ جَ | 18. حَ شَ خَ  
19. سَ دَ ذَ | 20. شَ رَ زَ | 21. دَ سَ رَ | 22. ذَ شَ زَ | 23. أَ سَ ءَ | 24. ءَ شَ أَ

## P006 — صَ ضَ | COVERAGE REBALANCED
### Penanaman EXACT-2
1. صَ ضَ | 2. ضَ صَ | 3. صَ صَ | 4. ضَ ضَ | 5. صَ أَ | 6. ضَ ءَ
### Latihan EXACT-3
7. صَ بَ ضَ | 8. ضَ تَ صَ | 9. صَ ثَ ضَ | 10. بَ صَ ضَ | 11. تَ ضَ صَ | 12. ثَ صَ ضَ  
13. صَ جَ حَ | 14. ضَ خَ جَ | 15. حَ صَ خَ | 16. جَ ضَ حَ | 17. خَ صَ جَ | 18. أَ ضَ ءَ  
19. صَ دَ ذَ | 20. ضَ رَ زَ | 21. دَ صَ سَ | 22. ذَ ضَ شَ | 23. رَ صَ أَ | 24. زَ ضَ ءَ

## P007 — طَ ظَ | COVERAGE REBALANCED
### Penanaman EXACT-2
1. طَ ظَ | 2. ظَ طَ | 3. طَ طَ | 4. ظَ ظَ | 5. طَ أَ | 6. ظَ ءَ
### Latihan EXACT-3
7. طَ بَ ظَ | 8. ظَ تَ طَ | 9. طَ ثَ ظَ | 10. بَ طَ ظَ | 11. تَ ظَ طَ | 12. ثَ طَ ظَ  
13. طَ جَ حَ | 14. ظَ خَ جَ | 15. حَ طَ خَ | 16. دَ ظَ ذَ | 17. رَ طَ زَ | 18. أَ ظَ ءَ  
19. طَ سَ شَ | 20. ظَ صَ ضَ | 21. سَ طَ صَ | 22. شَ ظَ ضَ | 23. جَ طَ أَ | 24. خَ ظَ ءَ

## P008 — عَ غَ | COVERAGE REBALANCED
### Penanaman EXACT-2
1. عَ غَ | 2. غَ عَ | 3. عَ عَ | 4. غَ غَ | 5. عَ أَ | 6. غَ ءَ
### Latihan EXACT-3
7. عَ بَ غَ | 8. غَ تَ عَ | 9. عَ ثَ غَ | 10. بَ عَ غَ | 11. تَ غَ عَ | 12. ثَ عَ غَ  
13. عَ جَ حَ | 14. غَ خَ دَ | 15. ذَ عَ رَ | 16. زَ غَ سَ | 17. شَ عَ صَ | 18. ضَ غَ طَ  
19. عَ ظَ أَ | 20. غَ ءَ بَ | 21. حَ عَ خَ | 22. دَ غَ ذَ | 23. سَ عَ شَ | 24. صَ غَ ضَ

## P009 — فَ قَ | COVERAGE REBALANCED
### Penanaman EXACT-2
1. فَ قَ | 2. قَ فَ | 3. فَ فَ | 4. قَ قَ | 5. فَ أَ | 6. قَ ءَ
### Latihan EXACT-3
7. فَ بَ قَ | 8. قَ تَ فَ | 9. فَ ثَ قَ | 10. بَ فَ قَ | 11. تَ قَ فَ | 12. ثَ فَ قَ  
13. فَ جَ حَ | 14. قَ خَ دَ | 15. ذَ فَ رَ | 16. زَ قَ سَ | 17. شَ فَ صَ | 18. ضَ قَ طَ  
19. فَ ظَ عَ | 20. غَ قَ أَ | 21. ءَ فَ جَ | 22. حَ قَ خَ | 23. سَ فَ شَ | 24. صَ قَ ضَ

## COVERAGE CHECKPOINT P005–P009
Tujuan revisi ini bukan membuat semua huruf muncul sama banyak dalam satu halaman. Tujuannya memastikan review kumulatif berputar dan tidak ada huruf lama hilang karena bias pemilihan contoh.

Khusus `أَ` / `ءَ`:
- P005: keduanya muncul kembali.
- P006: keduanya muncul kembali.
- P007: keduanya muncul kembali.
- P008: keduanya muncul kembali.
- P009: keduanya muncul kembali.

Huruf P001–P004 juga disebarkan kembali lintas P005–P009, bersama target-target baru. Tahap audit berikutnya harus menghitung angka frekuensi nyata; klaim pemerataan tidak boleh hanya berdasarkan inspeksi mata.

## STATUS
P001–P009 = **CURATED v0.3, MENUNGGU FREQUENCY AUDIT**.  
P010 = belum disusun.  
Renderer/PDF = tetap ditahan.
