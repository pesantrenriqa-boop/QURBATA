# PRINT-SPEC-QURBATA-v1 — Spesifikasi Otomasi Layout Buku QURBATA

**Status:** Draf Terkendali — Pilot Jilid 1  
**Tanggal:** 28 Juli 2026  
**Cakupan awal:** buku peserta QURBATA Jilid 1  
**Sumber tunggal:** `books/jilid-1/pages/QJ1-P001.md`–`QJ1-P040.md`

## Profil Cetak Awal

- ukuran potong: A5 potret, 148 × 210 mm;
- bleed: 3 mm pada empat sisi;
- safe area: 8 mm dari garis potong;
- latihan: 24 kotak, susunan 3 kolom × 8 baris;
- huruf Arab latihan: Amiri Quran 16 pt sebagai baseline A5 potret; ukuran final tunduk pada uji keterbacaan dan proof print;
- warna kerja: hijau RIQA, aksen oranye, latar putih;
- keluaran: PDF buku peserta; buku guru dibangkitkan sebagai keluaran terpisah;
- crop marks: aktif pada PDF produksi;
- metadata Draft tetap tampil sampai seluruh gate selesai.
- halaman awal: cover dan identitas peserta;
- setiap halaman pelajaran menampilkan nomor halaman, tanggal, nilai, status lulus/ulang, dan paraf/TTD guru;
- setiap halaman pelajaran menyediakan panel Bahasa Arab dan Tahfidz/Murojaah;
- materi Bahasa Arab tertulis hanya boleh muncul setelah lulus whitelist literasi;
- target tahfidz hanya boleh muncul setelah mapping tahfidz per halaman disahkan.

Ukuran dan gaya visual dapat diubah melalui generator tanpa mengubah 40 sumber halaman.

## Pemisahan Edisi

Generator buku peserta hanya membaca bagian sebelum `## Segmen Bahasa Arab 5 Menit — Pilot`. Seluruh konten setelah penanda tersebut diperlakukan sebagai naskah guru dan tidak boleh masuk ke PDF peserta.

Pemisahan ini melaksanakan keputusan `AUD-ARB-QJ1-003`: 40/40 segmen Bahasa Arab berstatus `HOLD-PARTICIPANT`.

## Preflight Wajib

Build gagal apabila:

1. satu halaman baca tidak mempunyai tepat 24 latihan/sampel;
2. kode halaman atau judul tidak ditemukan;
3. jumlah halaman PDF tidak sama dengan jumlah sumber yang berhasil diproses;
4. ukuran MediaBox tidak sesuai ukuran potong + bleed;
5. marker konten guru ditemukan pada teks PDF peserta;
6. font Arab atau font antarmuka tidak tersedia.

## Font

Font Arab produksi ditetapkan **Amiri Quran**. Font antarmuka Latin pada tahap prototipe memakai DejaVu Sans.

- berkas resmi `AmiriQuran.ttf` harus ditempatkan pada `production/print/fonts/`;
- lisensi SIL Open Font License harus disimpan bersama catatan sumber;
- font harus ditanam di PDF;
- hasil shaping Arab wajib diperiksa dari render PNG, bukan hanya ekstraksi teks.

## Perintah Build

```bash
python3 -m pip install -r production/print/requirements.txt
./production/print/fetch_amiri_quran.sh
python3 production/print/generate_qurbata_pdf.py
pdfinfo output/pdf/QURBATA-Jilid-1-Peserta-print.pdf
pdftoppm -png -f 1 -singlefile output/pdf/QURBATA-Jilid-1-Peserta-print.pdf tmp/pdfs/qj1-preview
```

## Batas Klaim

Pipeline otomatis mengurangi pekerjaan layout manual dan menyediakan preflight struktural. PDF baru boleh disebut **siap cetak final** setelah:

- semua isi terkait telah disahkan;
- font produksi dan lisensi ditetapkan;
- seluruh halaman dirender ke PNG dan diperiksa visual;
- proof print fisik lulus;
- profil warna, spesifikasi mesin cetak, binding, kertas, dan finishing ditetapkan bersama percetakan;
- editorial, Arab/Qira’at, safeguarding, asesmen, serta Document Controller menandatangani Evidence-ID.
