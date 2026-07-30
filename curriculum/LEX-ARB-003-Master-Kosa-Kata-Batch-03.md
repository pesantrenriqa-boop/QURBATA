# LEX-ARB-003 — Master Kosa Kata Bahasa Arab Batch 03

**Batch-ID:** LEX-ARB-003  
**Status:** CANDIDATE — MENUNGGU VALIDASI AHLI  
**Tanggal:** 28 Juli 2026  
**Cakupan:** AR-STG-007 sampai AR-STG-009  
**Prasyarat:** LEX-ARB-001 dan LEX-ARB-002  
**Fokus:** tindakan kini, lampau, perintah, dan larangan

## 1. Urutan Pedagogis

| Urut | Lexeme-ID | Kosa kata/lema tampilan | Arti | Family-ID | Hitungan | Tahap awal |
|---:|---|---|---|---|---:|---|
| 32 | AR-LEX-000032 | قَرَأَ | membaca/telah membaca | AR-FAM-000029 | 1 | AR-STG-007 |
| 33 | AR-LEX-000033 | كَتَبَ | menulis/telah menulis | AR-FAM-000001 | 0 | AR-STG-007 |
| 34 | AR-LEX-000034 | جَلَسَ | duduk/telah duduk | AR-FAM-000030 | 1 | AR-STG-007 |
| 35 | AR-LEX-000035 | ذَهَبَ | pergi/telah pergi | AR-FAM-000031 | 1 | AR-STG-007 |
| 36 | AR-LEX-000036 | فَتَحَ | membuka/telah membuka | AR-FAM-000028 | 0 | AR-STG-007 |
| 37 | AR-LEX-000037 | أَغْلَقَ | menutup/telah menutup | AR-FAM-000032 | 1 | AR-STG-007 |
| 38 | AR-LEX-000038 | دَخَلَ | masuk/telah masuk | AR-FAM-000033 | 1 | AR-STG-007 |
| 39 | AR-LEX-000039 | خَرَجَ | keluar/telah keluar | AR-FAM-000034 | 1 | AR-STG-007 |
| 40 | AR-LEX-000040 | شَرِبَ | minum/telah minum | AR-FAM-000035 | 1 | AR-STG-007 |
| 41 | AR-LEX-000041 | أَكَلَ | makan/telah makan | AR-FAM-000036 | 1 | AR-STG-007 |
| 42 | AR-LEX-000042 | نَامَ | tidur/telah tidur | AR-FAM-000037 | 1 | AR-STG-007 |
| 43 | AR-LEX-000043 | قَامَ | berdiri/telah berdiri | AR-FAM-000038 | 1 | AR-STG-007 |
| 44 | AR-LEX-000044 | سَمِعَ | mendengar/telah mendengar | AR-FAM-000039 | 1 | AR-STG-007 |
| 45 | AR-LEX-000045 | نَظَرَ | melihat/memandang | AR-FAM-000040 | 1 | AR-STG-007 |

**Jumlah entri Batch 03:** 14.  
**Tambahan target terhitung:** 12.  
**Keluarga yang sudah dihitung sebelumnya:** ك-ت-ب dan ف-ت-ح.  
**Akumulasi Batch 01–03:** 40 target terhitung.

## 2. Urutan Alfabet Kamus

| Abjad | Lexeme-ID | Kosa kata | Arti | Hitungan |
|---|---|---|---|---:|
| أ | AR-LEX-000041 | أَكَلَ | makan | 1 |
| أ | AR-LEX-000037 | أَغْلَقَ | menutup | 1 |
| ج | AR-LEX-000034 | جَلَسَ | duduk | 1 |
| خ | AR-LEX-000039 | خَرَجَ | keluar | 1 |
| د | AR-LEX-000038 | دَخَلَ | masuk | 1 |
| ذ | AR-LEX-000035 | ذَهَبَ | pergi | 1 |
| س | AR-LEX-000044 | سَمِعَ | mendengar | 1 |
| ش | AR-LEX-000040 | شَرِبَ | minum | 1 |
| ف | AR-LEX-000036 | فَتَحَ | membuka | 0 |
| ق | AR-LEX-000043 | قَامَ | berdiri | 1 |
| ق | AR-LEX-000032 | قَرَأَ | membaca | 1 |
| ك | AR-LEX-000033 | كَتَبَ | menulis | 0 |
| ن | AR-LEX-000042 | نَامَ | tidur | 1 |
| ن | AR-LEX-000045 | نَظَرَ | melihat/memandang | 1 |

## 3. Bentuk Turunan Bernilai Nol

Setelah review, setiap verba dapat mempunyai:

- madhi;
- mudhari‘;
- amr bila secara semantik layak;
- nahi;
- perubahan dhamir;
- mashdar dan bentuk turunan lain pada tahap yang sesuai.

Semua menunjuk Family-ID yang sama dan tidak menambah baseline 40.

## 4. Unsur Fungsional

| Function-Word-ID | Bentuk | Fungsi |
|---|---|---|
| AR-FW-000013 | إِلَى | menuju/ke |
| AR-FW-000014 | مِنْ | dari |
| AR-FW-000015 | بِـ | dengan/menggunakan |
| AR-FW-000016 | لَا | larangan ketika diikuti mudhari‘ majzum; fungsi berbeda dari respons sederhana |

## 5. Gate

- lema tampilan verba dan aturan penghitungan keluarga disahkan;
- tashrif lengkap diverifikasi;
- makna transitif/intransitif dan preposisi pasangan ditelaah;
- bentuk amr/nahi diperiksa;
- alfabet dan hamza dikolasi secara konsisten;
- penempatan Jilid 1 belum final hanya karena baseline 40 tercapai.

## 6. Riwayat

| Versi | Tanggal | Ringkasan |
|---|---|---|
| 0.1.0-id | 28 Juli 2026 | Batch ketiga: 14 entri, 12 target; akumulasi baseline 40 |
