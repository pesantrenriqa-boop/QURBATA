# QURBATA TAHFIDZ — AYAT DISTRIBUTION AUDIT v0.1

**Status:** SIMPLE AUDIT / NOT FROZEN  
**Date:** 15 August 2026

## Tujuan

Audit ini sengaja sederhana. Hanya memeriksa working map 320 halaman dari sisi:

1. urutan surat/ayat;
2. ayat terlewat;
3. ayat ganda;
4. beban halaman yang jelas terlalu berat;
5. titik akhir corpus.

## Hasil Utama

### A. Struktur corpus

Working map telah mencapai 320/320 halaman.

Arah corpus yang terbentuk:

- Al-Fatihah sebagai tambahan wajib khusus;
- Juz 30 lengkap;
- Juz 29 lengkap;
- Juz 28 lengkap;
- Juz 27 lengkap;
- Juz 26 sebagian, sampai Al-Hujurat 1–5.

### B. Kontinuitas besar

Secara urutan besar, jalur berjalan konsisten dari surat-surat pendek menuju awal juz sebelumnya:

`Juz 30 → Juz 29 → Juz 28 → Juz 27 → Juz 26`

Tidak ditemukan kebutuhan mengubah model corpus pada tahap ini.

### C. Temuan beban yang harus diperbaiki

Working map belum layak di-freeze karena distribusi beban antarhalaman masih sangat tidak rata.

Titik paling jelas:

- **J4-P040 = An-Naba 1–40** → TERLALU BERAT. Satu surat penuh 40 ayat tidak boleh menjadi satu unit hanya untuk memaksa Juz 30 selesai di J4.
- **J5-P039 = Al-Haqqah 1–26** → sangat berat dibanding halaman J5 sebelumnya.
- **J5-P040 = Al-Haqqah 27–52** → sangat berat.
- Beberapa bagian akhir J4 (Abasa/An-Nazi'at) dan J7–J8 memuat rentang ayat besar; perlu diseimbangkan berdasarkan panjang teks, bukan jumlah ayat saja.

### D. Prinsip koreksi

Koreksi berikutnya tidak mengubah corpus. Hanya menggeser batas halaman.

Aturan sederhana:

- jangan memaksa satu surat selesai hanya karena batas jilid;
- ayat pendek boleh lebih banyak dalam satu halaman;
- ayat panjang harus lebih sedikit atau dapat dibagi;
- jika akhir jilid penuh, sisa surat otomatis diteruskan ke jilid berikutnya;
- target akhir corpus boleh mundur sedikit dari Al-Hujurat 1–5 jika diperlukan agar beban 320 halaman lebih realistis.

## Status per Jilid

| Jilid | Status mapping | Audit awal |
|---|---|---|
| J1 | 40/40 | relatif ringan; pertahankan sebagai level awal |
| J2 | 40/40 | relatif stabil |
| J3 | 40/40 | perlu cek keseimbangan, tetapi tidak ada stress ekstrem seperti J4-P040 |
| J4 | 40/40 | **REBALANCE REQUIRED** |
| J5 | 40/40 | **REBALANCE REQUIRED** |
| J6 | 40/40 | perlu cek panjang ayat Juz 28 |
| J7 | 40/40 | perlu cek volume teks |
| J8 | 40/40 | perlu cek volume teks dan titik akhir corpus |

## Keputusan Audit v0.1

`320/320 MAPPED = PASS`

`READY TO FREEZE = NO`

`CORPUS DIRECTION = PASS`

`LOAD BALANCE = REVISION REQUIRED`

## Langkah Berikutnya

Buat **Ayat Distribution v0.2** dengan satu pekerjaan saja: meratakan beban halaman, terutama mulai J4–J8, tanpa membuka sistem murojaah atau subsistem lain.

Target setelah koreksi:

`320/320 halaman + urutan corpus benar + tidak ada pemaksaan surat panjang dalam satu halaman`.
