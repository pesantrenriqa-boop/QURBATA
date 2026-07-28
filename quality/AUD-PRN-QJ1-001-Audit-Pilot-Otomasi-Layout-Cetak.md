# AUD-PRN-QJ1-001 — Audit Pilot Otomasi Layout Cetak Jilid 1

**Audit-ID:** AUD-PRN-QJ1-001  
**Status:** PILOT 1 HALAMAN LULUS — BUILD 40 HALAMAN BELUM DIJALANKAN  
**Tanggal:** 28 Juli 2026  
**Objek:** `production/print/generate_qurbata_pdf.py`  
**Edisi:** Buku peserta  
**Keputusan:** PR #2 tetap Draft

## 1. Cakupan Pilot

Pilot memakai fixture terkendali QJ1-P001 dengan 24 latihan. Generator membentuk PDF A4 lanskap dengan bleed 3 mm, safe area 12 mm, crop marks, grid 4 × 6, metadata Draft, font tertanam, dan pemisahan konten guru–peserta.

## 2. Hasil Teknis

| Pemeriksaan | Hasil |
|---|---|
| jumlah sumber pilot | 1 halaman |
| jumlah halaman PDF | 1 halaman |
| jumlah latihan | 24/24 |
| susunan | 4 kolom × 6 baris |
| urutan tangga | kanan atas menuju kiri, lalu turun |
| urutan rangkaian Arab | RTL sesuai urutan sumber |
| ukuran MediaBox | A4 lanskap + bleed 3 mm |
| crop marks | hadir |
| safe area | 12 mm |
| shaping/harakat Arab | tampil pada render PNG |
| kebocoran marker guru | tidak ditemukan oleh preflight |
| inspeksi visual PNG | tidak ditemukan clipping, overlap, kotak hitam, atau harakat terpotong |

## 3. Koreksi Selama Pilot

Render pertama menempatkan urutan kotak dan rangkaian secara tidak tepat untuk alur kanan-ke-kiri. Generator dikoreksi sehingga:

- Tangga 1 dimulai dari kanan atas;
- urutan empat tangga bergerak dari kanan ke kiri;
- token Arab diolah agar tampilan visual mempertahankan urutan logis sumber;
- render kedua diperiksa ulang dan lulus secara visual.

## 4. Yang Sudah Diotomatisasi

- parsing 24 latihan/sampel dari sumber Markdown;
- validasi tepat 24 butir;
- pembuatan halaman peserta;
- pemisahan otomatis pada marker `Segmen Bahasa Arab 5 Menit — Pilot`;
- bleed, safe area, crop marks, grid, header, footer, dan nasihat akhlak;
- PDF metadata;
- pemeriksaan jumlah halaman, MediaBox, serta marker kebocoran guru.

## 5. Yang Masih Terbuka

1. menjalankan build terhadap 40 sumber nyata pada cabang;
2. menangani empat halaman khusus yang tidak semuanya memakai tabel 24 latihan;
3. menetapkan font Arab produksi dan lisensinya;
4. membangkitkan serta memeriksa PNG seluruh halaman;
5. membuat edisi guru otomatis;
6. menetapkan cover, punggung, halaman legal, daftar isi, dan halaman pembuka;
7. menetapkan CMYK/profil warna sesuai percetakan;
8. proof print fisik, binding, kertas, finishing, dan persetujuan Evidence-ID.

## 6. Keputusan Audit

Pipeline otomatis **LAYAK DILANJUTKAN** dan pilot teknis satu halaman **LULUS**. Namun, status **siap cetak final belum boleh diberikan** sampai build 40 halaman, inspeksi visual penuh, proof print, review ahli, editorial, safeguarding, serta otorisasi selesai.
