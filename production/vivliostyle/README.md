# QURBATA Book Production — Vivliostyle

Status: draf produksi awal

Modul ini mengubah master data QURBATA menjadi halaman buku B5 dan PDF cetak. Data materi tetap menjadi sumber; HTML dan PDF adalah turunan.

## Jalankan

```bash
npm install
npm run build
```

Hasil:

- `dist/index.html` — pratinjau browser
- `dist/QURBATA-JILID-1-PILOT.pdf` — PDF cetak

## Kontrak integrasi RIQA OS

Setiap halaman memiliki:

- kode unit resmi, misalnya `QJ1-P001`;
- URL stabil `https://www.rumahilmualquran.com/q/{pageId}`;
- QR dengan koreksi kesalahan tingkat H;
- target digital berupa resolver RIQA OS, bukan URL halaman internal yang mudah berubah.

Resolver `/q/[pageId]` pada RIQA OS kelak mencari kode unit dan mengarahkan pengguna ke materi, audio, video, latihan, asesmen, atau login bila diperlukan. QR tidak memuat identitas atau data pribadi peserta.

## Pemeriksaan otomatis awal

Build dihentikan jika halaman latihan tidak memenuhi semuanya:

- tepat 8 baris × 3 kolom;
- tepat 24 tangga;
- tangga 1-8 berisi dua huruf;
- tangga 9-24 berisi tiga huruf;
- URL mengikuti kontrak stabil RIQA OS `/q/{pageId}`.

## Font

Masukkan font resmi sesuai petunjuk `fonts/README.md`. Saat belum ada, browser memakai fallback Arab yang tersedia; fallback bukan font final produksi.
