# REG-ARB-001 — Register Objek Kompetensi Bahasa Arab QURBATA

**Register-ID:** REG-ARB-001  
**Status:** DRAF TERKENDALI  
**Tanggal:** 28 Juli 2026  
**Pengendali:** ACP-QUR-001, DEC-CUR-003

## 1. Tujuan

Mencegah duplikasi, lompatan prasyarat, dan hitungan semu pada progression Bahasa Arab Jilid 1–8.

## 2. Jenis ID

| Objek | Pola ID | Contoh |
|---|---|---|
| tahap kompetensi | AR-STG-xxx | AR-STG-001 |
| outcome | AR-CO-xxxxxx | AR-CO-000001 |
| lema | AR-LEX-xxxxxx | AR-LEX-000001 |
| keluarga leksikal | AR-FAM-xxxxxx | AR-FAM-000001 |
| struktur | AR-GRM-xxxxxx | AR-GRM-000001 |
| fungsi komunikasi | AR-FUN-xxxxxx | AR-FUN-000001 |
| tugas asesmen | AR-ASM-xxxxxx | AR-ASM-000001 |
| bukti validasi | AR-EVD-xxxxxx | AR-EVD-000001 |
| pola kalimat | AR-PAT-xxxxxx | AR-PAT-000001 |
| contoh kalimat | AR-SEN-xxxxxx | AR-SEN-000001 |
| dialog | AR-DLG-xxxxxx | AR-DLG-000001 |

## 3. Skema Lema

Setiap AR-LEX wajib memuat:

- lema tervokalisasi;
- Lexical-Family-ID;
- arti inti;
- kategori isim/fi‘il/huruf;
- sumber: lingkungan/Qur’an/hadis/Fusha;
- frekuensi atau alasan pemilihan;
- konkret/abstrak;
- tahap pengenalan;
- halaman pertama;
- jadwal murojaah;
- bentuk turunan;
- status hitungan: DIHITUNG atau TURUNAN-NOL;
- validator dan bukti.

## 4. Skema Struktur

Setiap AR-GRM wajib memuat:

- nama operasional dan istilah Arab;
- fungsi komunikatif;
- pola contoh;
- prasyarat;
- kosa kata yang diperlukan;
- mode reseptif/produktif/analitis;
- batas cakupan;
- kesalahan umum;
- remedial;
- tahap;
- halaman;
- asesmen transfer;
- status validasi.

## 5. Register Tahap Awal

| Stage-ID | Tahap | Status objek rinci | Status pemetaan jilid |
|---|---:|---|---|
| AR-STG-001 | 1 | TO-DESIGN | UNMAPPED |
| AR-STG-002 | 2 | TO-DESIGN | UNMAPPED |
| AR-STG-003 | 3 | TO-DESIGN | UNMAPPED |
| AR-STG-004 | 4 | TO-DESIGN | UNMAPPED |
| AR-STG-005 | 5 | TO-DESIGN | UNMAPPED |
| AR-STG-006 | 6 | TO-DESIGN | UNMAPPED |
| AR-STG-007 | 7 | TO-DESIGN | UNMAPPED |
| AR-STG-008 | 8 | TO-DESIGN | UNMAPPED |
| AR-STG-009 | 9 | TO-DESIGN | UNMAPPED |
| AR-STG-010 | 10 | TO-DESIGN | UNMAPPED |
| AR-STG-011 | 11 | TO-DESIGN | UNMAPPED |
| AR-STG-012 | 12 | TO-DESIGN | UNMAPPED |
| AR-STG-013 | 13 | TO-DESIGN | UNMAPPED |
| AR-STG-014 | 14 | TO-DESIGN | UNMAPPED |
| AR-STG-015 | 15 | TO-DESIGN | UNMAPPED |
| AR-STG-016 | 16 | TO-DESIGN | UNMAPPED |
| AR-STG-017 | 17 | TO-DESIGN | UNMAPPED |
| AR-STG-018 | 18 | TO-DESIGN | UNMAPPED |
| AR-STG-019 | 19 | TO-DESIGN | UNMAPPED |
| AR-STG-020 | 20 | TO-DESIGN | UNMAPPED |

## 6. Aturan Dedup

- satu lema hanya satu AR-LEX berstatus DIHITUNG;
- bentuk turunan menunjuk AR-FAM yang sama dan bernilai nol tambahan;
- kemunculan halaman kedua dan berikutnya bukan pengenalan baru;
- homograf dengan makna/fungsi berbeda wajib ditelaah, tidak otomatis digabung;
- partikel berulang tetap satu objek;
- perubahan vokalisasi yang mengubah lema/fungsi harus diputuskan ahli.

## 6A. Hubungan dengan Master Kalimat

- STD-ARB-001 mengendalikan aturan pembentukan contoh.
- REG-ARB-002 menyimpan frasa, kalimat, dialog, dan teks.
- Setiap AR-LEX harus dapat ditelusuri ke contoh pemakaian.
- Setiap AR-GRM harus mempunyai Pattern-ID dan contoh reseptif, produktif, serta transfer.
- Pengulangan lema dalam contoh tidak menambah hitungan kosa kata.

## 6A. Register Fungsi Komunikasi Jilid 1

| Function-ID | Fungsi | Sumber pertama | Status |
|---|---|---|---|
| AR-FUN-000001 | mengenali benda | BAT-ARB-001 | DRAF PILOT |
| AR-FUN-000002 | mengenali orang | BAT-ARB-001 | DRAF PILOT |
| AR-FUN-000003 | menunjukkan dan mengidentifikasi | BAT-ARB-001 | DRAF PILOT |
| AR-FUN-000004 | bertanya identitas benda/orang | BAT-ARB-001 | DRAF PILOT |
| AR-FUN-000005 | mendeskripsikan benda/tempat | BAT-ARB-002 | LANGUAGE-REVIEW |
| AR-FUN-000006 | menyatakan lokasi benda | BAT-ARB-002 | LANGUAGE-REVIEW |
| AR-FUN-000007 | menyatakan tindakan yang telah terjadi | BAT-ARB-003 | LANGUAGE-REVIEW |
| AR-FUN-000008 | menyatakan tindakan yang sedang/umum terjadi | BAT-ARB-003 | LANGUAGE-REVIEW |

## 6B. Batch Objek Nyata

| Batch-ID | Cakupan | Isi | Status |
|---|---|---|---|
| LEX-ARB-001 | AR-STG-001–003 | 16 entri; 14 target terhitung; tampilan pedagogis dan alfabetis | CANDIDATE |
| BAT-ARB-001 | AR-STG-001–003 | 4 struktur, 4 fungsi, 4 pola, 24 kalimat, 6 asesmen | DRAF PILOT |
| LEX-ARB-002 | AR-STG-004–006 | 15 entri; 14 target terhitung; akumulasi 28 | CANDIDATE |
| BAT-ARB-002 | AR-STG-004–006 | 5 struktur, 2 fungsi tambahan, 34 kalimat/pasangan, 6 asesmen | DRAF PILOT / LANGUAGE-REVIEW |
| LEX-ARB-003 | AR-STG-007–009 | 14 entri; 12 target terhitung; akumulasi baseline 40 | CANDIDATE |
| BAT-ARB-003 | AR-STG-007–009 | 6 struktur, 2 fungsi tambahan, 4 pola, 38 contoh, 6 asesmen | DRAF PILOT / LANGUAGE-REVIEW |
| MAT-ARB-001 | Jilid 1–8 | baseline progresif 40/50/60/70/80/100/120/120; total 640 | DRAF PERENCANAAN |
| STD-ARB-002 | Jilid 1–8 | standar satu teks kumulatif terintegrasi per pelajaran | DRAF TERKENDALI |
| REG-ARB-003 | Jilid 1–8 | master microtext, paragraf, dan wacana; AR-TXT-000001 tersedia | PILOT |

Batch belum mengubah status UNMAPPED pada pemetaan jilid/halaman.

## 7. Riwayat

| Versi | Tanggal | Ringkasan |
|---|---|---|
| 0.8.0-id | 28 Juli 2026 | Mencatat AR-FUN-000001–000008 serta memperbarui total BAT-ARB-002/003 menjadi 34/38 contoh |
| 0.7.0-id | 28 Juli 2026 | Menautkan STD-ARB-002, REG-ARB-003, dan teks kumulatif pertama |
| 0.6.0-id | 28 Juli 2026 | Mencatat LEX-ARB-003 dan BAT-ARB-003; kandidat baseline Jilid 1 mencapai 40 |
| 0.5.0-id | 28 Juli 2026 | Mencatat LEX-ARB-002 dan BAT-ARB-002 untuk Tahap 4–6 |
| 0.4.0-id | 28 Juli 2026 | Menautkan MAT-ARB-001 dan baseline progresif nonseragam |
| 0.3.0-id | 28 Juli 2026 | Mencatat LEX-ARB-001 dan BAT-ARB-001 sebagai batch nyata pertama |
| 0.2.0-id | 28 Juli 2026 | Menautkan pola, kalimat, dialog, dan master contoh |
| 0.1.0-id | 28 Juli 2026 | Skema register dan 20 Stage-ID |
