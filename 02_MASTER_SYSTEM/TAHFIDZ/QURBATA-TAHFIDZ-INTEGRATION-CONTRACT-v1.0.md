# QURBATA TAHFIDZ — INTEGRATION CONTRACT v1.0

**Status:** FROZEN PRINCIPLE  
**Date:** 17 August 2026  
**Scope:** Tahfidz QURBATA + RIQA OS ecosystem

## Wajib Terintegrasi

Sistem Tahfidz QURBATA harus terus dirancang sebagai satu alur terpadu:

`ChatGPT ↔ GitHub ↔ Google Drive ↔ Supabase ↔ RIQA OS Web ↔ RIQA OS App`

Tidak boleh dibangun sebagai modul yang berdiri sendiri dan terputus dari ekosistem RIQA.

## Peran Tiap Lapisan

### ChatGPT
- ruang kerja analisis, penyusunan aturan, mapping, revisi, dan asistensi operasional;
- membantu membuat/meninjau artefak yang kemudian disimpan pada sumber resmi;
- tidak menjadi sumber data produksi tunggal.

### GitHub
- sumber versi dan governance untuk spesifikasi, mapping ayat, aturan, skema fitur, dokumentasi teknis, migration, dan source code;
- semua keputusan frozen yang memengaruhi sistem harus dapat dilacak versinya.

### Google Drive
- repositori dokumen operasional/non-code: kartu kendali, handbook, formulir, laporan, PDF, materi pengguna, dan arsip ekspor;
- digunakan sebagai lapisan distribusi dokumen yang mudah dibaca pengguna.

### Supabase
- database produksi utama untuk data Tahfidz RIQA OS;
- menyimpan peserta, target, progres, tanggal mulai, perjalanan hafalan, murojaah, hasil uji, status mutqin, histori perubahan, dan relasi user/role;
- menjadi single source of truth untuk data transaksi/progres aplikasi.

### RIQA OS Web
- antarmuka admin, guru, penguji, supervisor, cabang, dan monitoring;
- mengelola target, capaian, uji, laporan, dan dashboard perjalanan tahfidz.

### RIQA OS App
- antarmuka peserta/guru yang paling mudah untuk penggunaan harian;
- fokus pada aksi sederhana: target hari ini, mulai hafalan, murojaah, uji, hasil, progres, perjalanan, dan status mutqin.

## Fitur Khusus Tahfidz di RIQA OS

RIQA OS wajib mempunyai ruang/menu khusus **TAHFIDZ QURBATA** dengan minimal fitur:

- target saat ini;
- capaian total;
- hafalan baru;
- murojaah;
- Uji Hafalan Baru;
- Uji Awal–Akhir 1;
- Uji Awal–Akhir 2;
- Uji Komprehensif;
- status Mutqin;
- tanggal mulai perjalanan tahfidz;
- waktu berjalan sejak start;
- posisi saat ini (jilid/halaman/surat/ayat);
- histori perjalanan menghafal;
- hasil uji dan penguji;
- ringkasan capaian/terjaga/mutqin;
- target berikutnya otomatis dari mapping ayat frozen.

## Prinsip UX

Sistem backend boleh detail, tetapi penggunaan harus sederhana.

Aksi utama pengguna maksimal berorientasi pada beberapa tombol jelas, misalnya:

`Mulai Hafalan` — `Murojaah` — `Uji` — `Lihat Progres`

Pengguna tidak boleh dipaksa memahami struktur database, level teknis, atau proses administratif yang rumit.

## Data Minimum Per Peserta

- participant_id / RIQA ID;
- program = QURBATA_TAHFIDZ;
- start_at;
- current_jilid;
- current_page;
- current_surah;
- current_ayah_start;
- current_ayah_end;
- total_target_completed;
- total_retained;
- total_mutqin;
- latest_test_type;
- latest_test_result;
- latest_test_at;
- updated_at.

Detail histori disimpan pada tabel/event terpisah agar perjalanan tidak hilang ketika posisi saat ini berubah.

## Sinkronisasi Artefak

- perubahan aturan/mapping: ChatGPT → GitHub;
- dokumen kartu/handbook/laporan: GitHub source/spec → Drive artifact;
- struktur data produksi: GitHub schema/migration → Supabase;
- data Supabase → RIQA OS Web/App;
- ChatGPT dapat membantu membaca/merumuskan perubahan, tetapi data transaksi tetap berasal dari Supabase/RIQA OS.

## Change Control

Prinsip integrasi ini dianggap wajib dan tidak boleh dihapus diam-diam.

Jika arsitektur berubah, buat versi baru dan jelaskan alasan perubahan. Jangan memutus salah satu lapisan tanpa migrasi yang jelas.

## Next

1. Definisikan Kartu Kendali Tahfidz QURBATA sebagai representasi fisik dari data yang sama.
2. Definisikan schema Supabase Tahfidz.
3. Definisikan UI/UX fitur Tahfidz di RIQA OS Web/App.
4. Hubungkan ekspor laporan/kartu ke Google Drive.