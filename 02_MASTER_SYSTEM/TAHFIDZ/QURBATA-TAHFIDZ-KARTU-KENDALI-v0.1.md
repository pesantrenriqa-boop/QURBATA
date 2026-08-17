# QURBATA TAHFIDZ — KARTU KENDALI v0.1

**Status:** WORKING BASELINE / NOT FROZEN  
**Scope:** Kartu fisik + sumber data digital RIQA OS

## Prinsip

Kartu harus mudah dipakai guru dan santri, tetapi tetap merekam perjalanan tahfidz lengkap. Satu kartu tidak boleh berubah menjadi formulir administrasi yang rumit.

Kartu fisik dan RIQA OS memakai objek data yang sama.

## Identitas

- Nama Peserta
- ID Peserta RIQA
- Kelas / Unit
- Jilid QURBATA
- Guru / Musyrif
- Tanggal Mulai Tahfidz
- Posisi Awal
- Target Jilid
- Tanggal Selesai Jilid

## Tabel Kendali Harian

| Halaman | Target Surat/Ayat | Hafalan Baru | Murojaah | Tanggal | Paraf |
|---|---|---|---|---|---|
| P001 | sesuai baseline frozen | ☐ | ☐ | | |
| P002 | sesuai baseline frozen | ☐ | ☐ | | |
| ... | ... | ... | ... | ... | ... |
| P040 | sesuai baseline frozen | ☐ | ☐ | | |

Status sederhana:

- `BLM` = belum
- `PROSES` = sedang dihafal
- `LULUS` = hafalan baru lulus
- `TERJAGA` = lolos murojaah
- `MUTQIN` = lolos seluruh gate mutqin

## Ujian Bertingkat

Kartu harus memuat checkpoint berikut tanpa menjadikannya kolom wajib pada setiap halaman:

### UHB — Uji Hafalan Baru
Menguji target baru yang baru saja diselesaikan.

### UAA-1 — Uji Awal–Akhir 1
Penguji memilih titik awal dan titik akhir pada corpus yang sudah dicapai.

### UAA-2 — Uji Awal–Akhir 2
Cakupan lebih luas dan lebih acak daripada UAA-1.

### UK — Uji Komprehensif
Mengambil sampel dari keseluruhan hafalan yang telah dicapai.

### MUTQIN
Status akhir untuk corpus yang sudah terbukti stabil melalui hafalan baru, murojaah, dan ujian bertingkat.

## Ringkasan Ujian

| Jenis Uji | Cakupan | Tanggal | Hasil | Penguji | Catatan |
|---|---|---|---|---|---|
| UHB | | | | | |
| UAA-1 | | | | | |
| UAA-2 | | | | | |
| UK | | | | | |
| MUTQIN | | | | | |

## Ringkasan Perjalanan

- Mulai Tahfidz: ______
- Saat Ini: Jilid ___ P___
- Capaian: ___ / 320 target
- Terjaga: ___ / ___ target tercapai
- Mutqin: ___ / ___ target tercapai
- Waktu Perjalanan: otomatis di RIQA OS
- Surat/Juz selesai: ______
- Catatan guru: ______

## Integrasi RIQA OS

Fitur khusus Tahfidz QURBATA wajib menyediakan:

1. `Mulai Hafalan`
2. `Catat Hafalan Baru`
3. `Murojaah`
4. `Uji`
5. `Tetapkan Mutqin`
6. `Lihat Progres`
7. `Perjalanan Tahfidz`

Dashboard menampilkan minimal:

- target saat ini;
- posisi Jilid/Halaman;
- hafalan baru terakhir;
- target murojaah;
- capaian;
- terjaga;
- mutqin;
- tanggal mulai;
- lama perjalanan;
- riwayat ujian;
- hasil terbaru.

## Model Data Minimum

`participant_id`
`qurbata_volume`
`qurbata_page`
`surah`
`ayah_start`
`ayah_end`
`new_hifz_status`
`review_status`
`test_type`
`test_result`
`mutqin_status`
`started_at`
`completed_at`
`tested_at`
`teacher_id`
`notes`

## Integrasi Sistem

Baseline ini mengikuti contract:

`ChatGPT ↔ GitHub ↔ Google Drive ↔ Supabase ↔ RIQA OS Web ↔ RIQA OS App`

GitHub = source of truth spesifikasi.  
Drive = dokumen/kartu operasional dan arsip.  
Supabase = data transaksi/progres peserta.  
RIQA OS Web/App = antarmuka pengguna.

## Next

1. Turunkan baseline frozen surat/ayat Jilid 1 ke kartu nyata P001–P040.
2. Buat versi kartu siap cetak.
3. Buat schema Supabase untuk perjalanan tahfidz.
4. Buat UX RIQA OS Tahfidz dengan aksi sederhana.