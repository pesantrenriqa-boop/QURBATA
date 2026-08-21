# QURBATA — Pipeline Data ke Adobe InDesign

**Status:** ACTIVE WORKFLOW  
**Prinsip:** isi materi berasal dari master/halaman kanonik repository; InDesign hanya menerima hasil ekspor.  
**Tidak mengubah:** urutan kompetensi, contoh latihan, harakat, Source-ID, status akademik, atau aturan frozen.

## Prioritas Saat Ini

1. Mengisi susunan materi terlebih dahulu.
2. Memakai kembali contoh-contoh QURBATA yang sudah pernah disusun di repository.
3. Menjadikan hasilnya siap diimpor ke template Adobe InDesign.
4. Penyempurnaan desain dilakukan setelah data materi terbaca utuh.

## Sumber

- `books/jilid-1/pages/QJ1-P001.md` dst.
- `books/jilid-2/pages/QJ2-P001.md` dst.
- `books/jilid-3/pages/` dan jalur recovery/kanonik sesuai baseline.
- Jilid berikutnya mengikuti master resmi masing-masing.

## Exporter PowerShell

File:

`tools/export-qurbata-indesign.ps1`

Jalankan dari root repository:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\export-qurbata-indesign.ps1
```

Atau:

```powershell
.\tools\export-qurbata-indesign.ps1
```

Output:

- `dist/indesign-data/QURBATA-INDESIGN-DATA-MERGE.csv`
- `dist/indesign-data/QURBATA-INDESIGN-DATA.json`
- `dist/indesign-data/QURBATA-INDESIGN-EXPORT-AUDIT.csv`

CSV disimpan UTF-8 BOM agar teks Arab aman dibuka oleh Adobe InDesign/Excel pada Windows.

## Kolom Inti Data Merge

Setiap baris CSV = satu halaman QURBATA.

Kolom utama:

- `PageCode`
- `Jilid`
- `PageNumber`
- `Title`
- `Status`
- `Version`
- `Outcome`
- `ArabicOral`
- `Akhlak`
- `SourceFile`
- `TanggaCount`
- `ExerciseID01` ... `ExerciseID24`
- `Type01` ... `Type24`
- `Slot01` ... `Slot24`

Dengan struktur tersebut, satu template InDesign dapat mempunyai 24 text frame latihan yang dihubungkan ke `Slot01` sampai `Slot24` melalui Data Merge.

## Contoh yang Sudah Ada

QJ1-P001 sudah mempunyai 24 tangga nyata, misalnya `بَ تَ`, `ثَ ثَ`, `بَ بَ`, sampai latihan tiga huruf pada Slot09–Slot24.

QJ2-P001 juga sudah mempunyai 24 contoh nyata, antara lain `كَتَبَ`, `سَأَلَ`, `جَلَسَ`, `دَخَلَ`, `خَرَجَ`, `ذَكَرَ`, `صَدَقَ`, `شَكَرَ`, `صَبَرَ`, `عَمِلَ`, `فَتَحَ` dan contoh review lain yang tersimpan pada halaman kanonik.

Exporter tidak membuat contoh baru. Ia mengekstrak contoh yang sudah tersimpan di file halaman.

## Audit

`QURBATA-INDESIGN-EXPORT-AUDIT.csv` menunjukkan jumlah tangga pada setiap halaman dan kolom `ReadyFor24SlotMerge`.

- `TRUE` = tersedia 24 tangga dan langsung dapat dipetakan ke 24 slot template.
- `FALSE` = halaman perlu ditangani sesuai tipe halaman/master, bukan diisi dengan contoh buatan otomatis.

Halaman non-latihan atau halaman dengan format berbeda tidak boleh dipaksa menjadi 24 tangga bila master tidak menetapkannya.

## Aturan Kerja

GitHub master/frozen → PowerShell exporter → CSV/JSON → Adobe InDesign → PDF.

InDesign bukan sumber isi. Revisi materi dilakukan di master/halaman kanonik lalu exporter dijalankan ulang sehingga perubahan dapat masuk secara massal ke template.
