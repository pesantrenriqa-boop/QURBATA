# QURBATA InDesign Template Specification v0.1

Status: DRAFT BASELINE
Date: 2026-08-21
Purpose: Menjadi spesifikasi sumber untuk pembangunan master template buku QURBATA di Adobe InDesign.

## 1. Prinsip Halaman

Satu halaman = satu pertemuan QURBATA.

Hierarki halaman:
1. Materi Tartil QURBATA = fokus utama dan dominan (sekitar 80% area pembelajaran).
2. NIDOM = blok pendukung kecil.
3. Bahasa Arab QURBATA = blok pendukung kecil.
4. Tahfidz = blok pendukung kecil.
5. Header/footer/identitas = elemen sistem halaman.

## 2. Grid Tartil Utama

Area Tartil selalu mempunyai tepat 8 baris vertikal:
- TARTIL_ROW_01
- TARTIL_ROW_02
- TARTIL_ROW_03
- TARTIL_ROW_04
- TARTIL_ROW_05
- TARTIL_ROW_06
- TARTIL_ROW_07
- TARTIL_ROW_08

Jumlah baris tidak berubah antarhalaman. Yang berubah adalah jumlah slot/kotak horizontal pada setiap baris.

### Variant slot per baris

#### GRID-4
Empat slot sama lebar:
`[01-A] [01-B] [01-C] [01-D]`

Diprioritaskan untuk Jilid 1 dan Jilid 2 pada materi huruf tunggal/kelompok pendek.

#### GRID-3
Tiga slot sama lebar:
`[01-A] [01-B] [01-C]`

#### GRID-2
Dua slot sama lebar:
`[01-A] [01-B]`

#### GRID-1
Satu slot penuh:
`[01-A]`

Setiap dari 8 baris dapat memakai GRID-4, GRID-3, GRID-2, atau GRID-1 secara independen sesuai materi halaman.

## 3. Model Data Layout

Setiap halaman harus dapat direpresentasikan dengan data, bukan formatting manual.

Contoh struktur:

```yaml
page_id: J1-P001
jilid: 1
meeting: 1
rows:
  - row: 1
    grid: 4
    items: ["", "", "", ""]
  - row: 2
    grid: 4
    items: ["", "", "", ""]
  - row: 3
    grid: 3
    items: ["", "", ""]
  - row: 4
    grid: 3
    items: ["", "", ""]
  - row: 5
    grid: 2
    items: ["", ""]
  - row: 6
    grid: 2
    items: ["", ""]
  - row: 7
    grid: 1
    items: [""]
  - row: 8
    grid: 1
    items: [""]
nidom: ""
bahasa_arab: ""
tahfidz:
  surah: ""
  ayat: ""
```

## 4. Blok Pendukung

Setelah 8 baris Tartil terdapat satu strip integrasi yang terdiri dari tiga blok:

`[ NIDOM ] [ BAHASA ARAB QURBATA ] [ TAHFIDZ ]`

Ketiganya tidak boleh mengalahkan dominasi visual materi Tartil.

### NIDOM
Memuat 1 hadits NIDOM/pertemuan dalam ukuran ringkas.

### Bahasa Arab QURBATA
Memuat instruksi kelas, pertanyaan-jawaban, atau language environment sesuai pertemuan.

### Tahfidz
Memuat minimal nama surah dan nomor ayat target hafalan. Teks ayat lengkap bersifat opsional berdasarkan desain final.

## 5. Elemen Tetap Parent Page

Elemen kandidat Parent Page:
- Logo QURBATA
- Identitas `QURBATA JILID n`
- Nomor halaman otomatis
- Footer
- Slogan `تعلّم – اِعمل – علِّم`
- Keterangan buku yang memang konstan

Nama materi yang berubah antarhalaman tidak boleh dikunci sebagai elemen permanen Parent Page.

## 6. Style System Wajib

Tidak boleh mengatur font/ukuran secara manual per kotak pada produksi massal.

Paragraph/Object Style minimal:
- `QB-TARTIL-PRIMARY`
- `QB-TARTIL-SECONDARY`
- `QB-NIDOM`
- `QB-ARABIC-INSTRUCTION`
- `QB-TAHFIDZ`
- `QB-HEADER`
- `QB-FOOTER`
- `QB-ARABIC-WORLD-READY`

Perubahan font, ukuran, alignment, leading, dan composer dilakukan melalui Style sehingga seluruh halaman dapat berubah serentak.

## 7. Arabic Typesetting

- Gunakan font Qurani/Utsmani yang telah lolos uji tampilan.
- Gunakan Adobe World-Ready Paragraph Composer untuk teks Arab.
- Uji sambungan huruf dan posisi fathah, kasrah, dhammah, sukun, tasydid, tanwin, serta tanda Qurani sebelum font di-freeze.
- Font final belum di-freeze pada v0.1 ini.

## 8. Prinsip Otomasi

Target workflow:

`MASTER DATA QURBATA -> LAYOUT VARIANT 4/3/2/1 -> INDESIGN TEMPLATE -> PDF PRINT`

Data materi harus dipisahkan dari aturan visual. Word dapat menjadi sumber konten sementara, tetapi master data terstruktur (CSV/JSON/YAML atau format setara) lebih disukai untuk produksi massal. PDF bukan sumber data utama untuk mengisi frame secara otomatis.

## 9. Baseline Dokumen InDesign Saat Ini

- Intent: Print
- Page: B5 / 176 x 250 mm
- Orientation: Portrait
- Facing Pages: Off untuk master awal
- Margin: 15 mm semua sisi
- Bleed: 3 mm semua sisi
- Slug: 0

## 10. Urutan Pembangunan

1. Freeze spesifikasi isi halaman.
2. Freeze sistem 8 baris dan variant GRID-4/3/2/1.
3. Susun schema data halaman.
4. Buat Paragraph Styles dan Object Styles.
5. Buat empat variant row di InDesign.
6. Bangun 8 row Tartil.
7. Bangun strip NIDOM / Bahasa Arab / Tahfidz.
8. Bangun Parent Page header/footer.
9. Uji satu halaman Jilid 1 dan satu halaman dengan kombinasi grid berbeda.
10. Baru produksi template buku dan otomasi import data.

## 11. Keputusan v0.1

FROZEN FOR TEMPLATE DEVELOPMENT:
- 8 baris Tartil per halaman.
- Setiap baris mendukung 4, 3, 2, atau 1 kotak.
- Jilid 1 dan 2 membutuhkan GRID-4 karena fase huruf tunggal/kelompok pendek.
- NIDOM, Bahasa Arab QURBATA, dan Tahfidz selalu tersedia sebagai tiga blok pendukung.
- Tartil tetap menjadi elemen visual dominan.

NOT YET FROZEN:
- Font final.
- Ukuran font final per variant.
- Tinggi row/gutter final.
- Stroke/warna kotak.
- Detail dekoratif.
- Mekanisme import final (Data Merge/script/XML/alternatif).
