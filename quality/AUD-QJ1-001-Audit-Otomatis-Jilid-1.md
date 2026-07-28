# AUD-QJ1-001 — Audit Otomatis Buku QURBATA Jilid 1

**Audit-ID:** AUD-QJ1-001  
**Status:** Draf Terkendali  
**Tanggal Audit:** 28 Juli 2026  
**Cakupan:** QJ1-P001–QJ1-P040 pada PR #2  
**Pengendali:** QC-000, CUR-QJ1-001, DEC-CUR-002, QJ1-MASTER  
**Catatan:** Audit otomatis tidak menggantikan penelaahan ahli.

## 1. Hasil Utama

| Pemeriksaan | Hasil |
|---|---:|
| File halaman tersedia | 40/40 |
| Halaman baca | 36 |
| Halaman khusus lisan/akhlak | 4 |
| Halaman baca dengan 24 baris | 36/36 |
| Halaman baca dengan 64 token | 36/36 |
| Halaman baca tanpa baris duplikat | 36/36 |
| Halaman lulus pemerataan identitas | 36/36 |
| Halaman tanpa harakat prematur | 36/36 |
| Siklus P033–P034 menutup 29 × 3 kombinasi | Lulus |
| Halaman dengan kandidat leksikal | 31/36 |
| Rujukan rasio lama dalam isi aktif | 0 |

Halaman P001–P005 belum diberi kandidat akar karena inventaris huruf yang tersedia belum memadai. Kombinasi terkontrol tetap digunakan.

## 2. Pemerataan

- Sebelum alfabet lengkap, 64 token dibagi dengan rumus `floor(64/L)` dan kelebihan diputar.
- Setelah 29 identitas lengkap, setiap identitas muncul 2–3 kali.
- Alif berhamza dan hamza mandiri menerima jatah setara.
- Setelah seluruh tiga harakat lengkap:
  - P033: 22 fathah, 21 kasrah, 21 dhammah;
  - P034: 21 fathah, 22 kasrah, 21 dhammah;
  - P035: 21 fathah, 21 kasrah, 22 dhammah.
- Rotasi diteruskan pada P037, P039, dan P040.
- P033–P034 secara gabungan menampilkan seluruh kombinasi identitas–harakat sedikitnya satu kali.

## 3. Temuan yang Sudah Ditutup

1. Rasio 60/40 dan 50:50 dicabut oleh DEC-CUR-002.
2. Ketimpangan alif/hamza ditutup melalui pembagian maksimal selisih satu.
3. Kasrah prematur pada identitas yang belum sah telah dihapus.
4. Distribusi P020 dan P030 diselaraskan dengan DEC-CUR-002.
5. Siklus P033–P034 diperbaiki agar menutup semua kombinasi tiga harakat.
6. Narasi historis 50:50 pada P020 dan P030 dibersihkan.

## 4. Batas Audit

Audit belum membuktikan:

- ketepatan makhraj;
- akurasi istilah dan ortografi Arab, termasuk ءُ;
- keterbacaan hasil render/font;
- kesesuaian usia;
- validitas ambang asesmen;
- efektivitas pedagogis;
- kelayakan materi Hafalan/Bahasa Arab;
- kepatuhan akhir tanpa review independen.

## 5. Kesimpulan

Struktur dan integritas distribusi otomatis Jilid 1 dinyatakan **LULUS-DRAF**. Buku belum Siap Uji dan belum dapat keluar dari Draft sampai gate manusia, materi khusus, render, asesmen, safeguarding, dan otorisasi diselesaikan.

## 6. Riwayat

| Versi | Tanggal | Ringkasan |
|---|---|---|
| 0.1.0-id | 28 Juli 2026 | Audit otomatis pertama untuk seluruh QJ1-P001–QJ1-P040 |
