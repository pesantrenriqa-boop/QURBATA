# REG-ARB-002 — Master Contoh Kalimat Bahasa Arab QURBATA

**Register-ID:** REG-ARB-002  
**Status:** DRAF TERKENDALI — BELUM DIISI FINAL  
**Tanggal:** 28 Juli 2026  
**Pengendali:** ACP-QUR-001, STD-ARB-001  
**Cakupan:** Jilid 1–8 dan seluruh turunannya

## 1. Fungsi

Menjadi sumber tunggal semua frasa, kalimat, tanya–jawab, dialog, paragraf, serta contoh Qurani/hadis yang digunakan dalam QURBATA.

## 2. Pola ID

| Objek | Pola |
|---|---|
| frasa | AR-PHR-xxxxxx |
| kalimat | AR-SEN-xxxxxx |
| pasangan tanya–jawab | AR-QA-xxxxxx |
| dialog | AR-DLG-xxxxxx |
| paragraf/teks | AR-TXT-xxxxxx |

## 3. Metadata Wajib

Setiap objek memuat:

- Object-ID;
- teks Arab tervokalisasi;
- arti/konteks;
- Source-Type;
- daftar AR-LEX;
- daftar AR-FAM/bentuk turunan;
- daftar FUNCTION-WORD-ID;
- AR-GRM;
- AR-FUN;
- Stage-ID;
- mode reseptif/produktif/analitis;
- status unsur baru dan murojaah;
- halaman pengenalan;
- halaman pemeliharaan;
- tingkat kesulitan;
- kesalahan umum;
- tugas asesmen;
- sumber dan hak penggunaan;
- validator;
- status.

## 4. Status

- CANDIDATE;
- LANGUAGE-REVIEW;
- PEDAGOGY-REVIEW;
- APPROVED-DRAFT;
- VALIDATED;
- REJECTED;
- RETIRED.

Hanya APPROVED-DRAFT atau VALIDATED yang boleh masuk prototipe halaman. Status VALIDATED memerlukan bukti sesuai VAL-ARB-001.

## 5. Aturan Dedup

Dua kalimat tidak otomatis dianggap duplikat bila fungsi atau struktur berbeda. Namun variasi yang hanya mengganti satu lema harus disimpan sebagai anggota satu Pattern-ID agar register tidak menggelembung.

Contoh pola:

- Pattern: `هٰذَا + [ISIM]`;
- anggota dapat memakai lema berbeda;
- setiap anggota mempunyai Sentence-ID bila dipakai sebagai bukti/halaman;
- Pattern-ID menjadi sumber pembangkitan latihan terkendali.

## 6. Hubungan Wajib

`AR-LEX/AR-FAM → AR-GRM → AR-FUN → Pattern-ID → Sentence-ID → Page-ID → AR-ASM → Evidence-ID`

Rantai yang terputus menjadi blocker.

## 7. Tampilan Turunan

Register ini harus dapat menghasilkan:

- urutan kalimat per tahap;
- urutan kalimat per jilid/halaman;
- semua kalimat yang memakai satu lema;
- semua contoh untuk satu kaidah;
- semua dialog untuk satu fungsi;
- daftar Qurani/hadis;
- daftar kalimat murojaah dan transfer;
- bahan kamus yang menampilkan contoh pemakaian.

## 8. Gate Pengisian

Pengisian contoh final dimulai setelah:

1. objek rinci tahap dibuat;
2. calon lema tersedia;
3. AR-GRM dan AR-FUN mempunyai dependency;
4. aturan vokalisasi dan sumber ditetapkan;
5. panel ahli menyetujui batch pilot.

## 8A. Batch Kalimat Terdaftar

| Batch-ID | Pattern-ID | Sentence-ID | Status |
|---|---|---|---|
| BAT-ARB-001 | AR-PAT-000001–AR-PAT-000004 | AR-SEN-000001–AR-SEN-000024 | DRAF PILOT |

Seluruh kalimat memakai kosa kata LEX-ARB-001 dan belum dipetakan final ke halaman.

## 9. Riwayat

| Versi | Tanggal | Ringkasan |
|---|---|---|
| 0.2.0-id | 28 Juli 2026 | Mencatat 4 pola dan 24 contoh dari BAT-ARB-001 |
| 0.1.0-id | 28 Juli 2026 | Skema master kalimat dan hubungan ke kosa kata/kaidah |
