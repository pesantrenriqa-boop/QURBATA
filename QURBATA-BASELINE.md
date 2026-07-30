# QURBATA — Baseline Sumber Tunggal

**Status:** AKTIF — PENGENDALI KONSOLIDASI  
**Tanggal:** 30 Juli 2026  
**Branch resmi:** `main`  
**Pemilik akademik:** Aris Liswanto  
**Tujuan:** mengembalikan seluruh pekerjaan QURBATA ke satu rangkaian sejak awal dan mencegah versi materi, kode, contoh, atau keputusan berjalan sendiri-sendiri.

## 1. Prinsip Pengendali

1. `main` adalah satu-satunya sumber kerja resmi.
2. Buku QURBATA adalah fokus produk utama. Produk turunan dibuat setelah struktur dan isi buku stabil.
3. Setiap jilid memakai kode halaman tetap: `QJ1-P001` dan seterusnya sampai `QJ8-P040`.
4. Master jilid mengendalikan urutan kompetensi; halaman, data, asesmen, audio, flashcard, dan aplikasi harus merujuk ke kode halaman yang sama.
5. Registry resmi tidak boleh diganti dengan skema kode baru tanpa Decision-ID.
6. Materi yang berbeda tetapi masih diperlukan untuk sejarah dipindahkan ke `archive/`.
7. Materi yang salah, terduplikasi, atau telah digantikan tidak boleh berada di folder produksi aktif.
8. Contoh Qurani wajib memiliki Source-ID dan tashih; contoh latihan tidak boleh diklaim sebagai Qurani tanpa sumber.
9. Tidak boleh ada regresi tangga kompetensi: jilid lebih tinggi tidak kembali menjadi latihan huruf tunggal atau dua huruf kecuali remedial guru yang tidak dicetak sebagai materi inti.
10. Seluruh keputusan sejak awal tetap berlaku kecuali secara eksplisit digantikan oleh keputusan yang lebih baru.

## 2. Hierarki Sumber Kebenaran

Urutan pengendali adalah:

`QC-000 → QCF/RCP/ACP/HCP → DEC-CUR → MASTER JILID → REGISTRY/MATRIX → HALAMAN → DATA ITEM → ASESMEN → PRODUK TURUNAN`

Bila dua file berbeda, file yang lebih rendah dalam hierarki harus menyesuaikan file yang lebih tinggi. Bila dua file setingkat berbeda, keputusan terbaru yang secara eksplisit menyatakan `supersedes` menjadi pengendali; versi lain dipindahkan ke arsip.

## 3. Registry Resmi yang Dipertahankan

- `curriculum/REG-QCF-001-Master-Kompetensi-QURBATA.md`
- `curriculum/REG-CUR-001-Register-Objek-Isi-QURBATA.md`
- `curriculum/REG-ARB-001-Register-Objek-Kompetensi-Bahasa-Arab.md`
- `curriculum/REG-ARB-002-Master-Contoh-Kalimat.md`
- `curriculum/REG-ARB-003-Master-Teks-Kumulatif-Terintegrasi.md`
- `curriculum/REG-ARB-004-Master-Siklus-Pembelajaran-Bahasa-Arab.md`
- `curriculum/REG-HAD-001-Master-Hadis-Akhlak.md`
- `curriculum/SRC-QJ2-MAD-001-Register-Source-ID-Kata-Qurani.md`
- `curriculum/REG-QJ3-FRQ-001-Registry-Frasa-Qurani-P031-P040.md`
- `docs/id/REG-GOV-001-Register-Knowledge-ID-QURBATA.md`

Registry baru hanya boleh dibuat bila objeknya benar-benar berbeda dan tidak dapat dimasukkan ke registry di atas.

## 4. Baseline Buku Aktif

### Jilid 1

- Master: `books/jilid-1/QJ1-MASTER-Struktur-40-Halaman.md`
- Halaman resmi: `books/jilid-1/pages/QJ1-P001.md`–`QJ1-P040.md`
- Pemetaan: `curriculum/MAT-QJ1-PAGE-001-Matriks-Keterlacakan-40-Halaman.md`
- Status: 40 halaman tersedia sebagai draf terkendali; isi tetap tunduk pada audit dan review ahli.

### Jilid 2

- Master: `books/jilid-2/QJ2-MASTER-Struktur-40-Halaman.md`
- Baseline kompetensi aktif:
  - P001–P020: bentuk sambung dan keluarga huruf;
  - P021–P024: tiga tanwin;
  - P025–P040: tangga mad asli dan kontras pendek–panjang sesuai `DEC-CUR-012` dan `DEC-CUR-013`.
- Folder `regenerated/` adalah sumber terbaru untuk P001–P024.
- Folder `rebased/` adalah sumber terbaru untuk P025–P040.
- Folder `pages/` lama tidak boleh dianggap otomatis sebagai sumber resmi bila bertentangan dengan versi regenerated/rebased.
- Target konsolidasi: seluruh versi aktif dinormalisasi menjadi satu jalur `books/jilid-2/pages/QJ2-P001.md`–`QJ2-P040.md`; versi lama dipindahkan ke `archive/`.

### Jilid 3

- Master: `books/jilid-3/QJ3-MASTER-Struktur-40-Halaman.md`
- Urutan resmi: sukun non-qalqalah → lam sukun → alif-lam qamariyah → kata/frasa Qurani terkendali.
- Kode resmi: `QJ3-P001`–`QJ3-P040`.
- `QJ3-B01A` telah dibekukan dan dipindahkan ke arsip.
- `QJ3-B01B` dan batch berikutnya menjadi materi aktif sementara sampai dinormalisasi menjadi 40 file halaman individual.
- Data item per batch di `data/jilid-3/` harus mengikuti master dan audit terbaru.

### Jilid 4–8

Master struktur tersedia, tetapi produksi halaman tidak boleh mendahului penutupan dependency jilid sebelumnya.

## 5. Aturan Kode yang Tidak Boleh Diubah Diam-diam

- Jilid: `QJ1`–`QJ8`
- Halaman: `QJx-P001`–`QJx-P040`
- Kompetensi: mengikuti `QCF`, `RCP`, `ACP`, dan registry kompetensi resmi.
- Sumber teks: `Source-ID`
- Bukti validasi/pilot: `Evidence-ID`
- Keputusan perubahan: `Decision-ID` atau `DEC-*`
- Knowledge-ID: mengikuti `docs/id/REG-GOV-001-Register-Knowledge-ID-QURBATA.md`

Kode sementara batch seperti `B01A`, `B01B`, dan sejenisnya hanya boleh dipakai selama produksi. Setelah isi stabil, objek harus diturunkan ke kode halaman resmi dan kode batch tidak menjadi identitas buku peserta.

## 6. Keputusan Konsolidasi

1. Konsep “Master Content Engine” tidak mengganti sistem yang sudah dibangun. Ia hanya boleh menjadi fungsi teknis dari registry dan halaman resmi.
2. Tidak dibuat bank materi baru yang berdiri di luar registry yang sudah ada.
3. Semua contoh lama dipulihkan konteksnya melalui halaman, kompetensi, Source-ID, dan status audit.
4. Materi yang bertentangan dengan master terbaru dipindahkan ke arsip atau dihapus dari area aktif.
5. Pekerjaan lanjutan dimulai dari normalisasi Jilid 2 dan penyelesaian contoh nyata Jilid 3, bukan membuat arsitektur baru.

## 7. Urutan Kerja Resmi Berikutnya

1. Konsolidasikan Jilid 2 menjadi 40 file halaman tunggal.
2. Audit silang halaman Jilid 1–2 terhadap registry kompetensi dan keputusan kurikulum.
3. Pulihkan dan normalisasi semua contoh Jilid 3 ke `QJ3-P001`–`QJ3-P040`.
4. Lengkapi Source-ID, LO/KO, distribusi 50–50, N+1/N+2/N+4/N+8, dan audit materi prematur.
5. Baru melanjutkan produksi Jilid 4.

## 8. Larangan

Dilarang:

- membuat struktur kode baru tanpa membaca baseline ini;
- menyebut versi lama sebagai final;
- memakai file dalam `archive/` untuk cetak atau aplikasi;
- mengganti urutan jilid hanya untuk mempercepat produksi;
- memindahkan fokus dari buku utama ke flashcard, presentasi, atau aplikasi sebelum materi buku stabil;
- menghapus riwayat penting tanpa memindahkannya ke arsip dan mencatat alasan.

Dokumen ini menjadi pintu masuk operasional seluruh pekerjaan QURBATA setelah konsolidasi branch ke `main`.