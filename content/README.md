# QURBATA Canonical Content

## Folder

```text
content/
├── curriculum/
├── tartil/
│   ├── jilid-01/
│   ├── jilid-02/
│   ├── jilid-03/
│   ├── jilid-04/
│   ├── jilid-05/
│   ├── jilid-06/
│   ├── jilid-07/
│   └── jilid-08/
├── arabic/
├── nidom/
├── meetings/
├── sources/
├── review/
└── publication/
```

## Kode Kanonik

### Buku Tartil

- Kompetensi: `QT-CMP-###`
- Unit kompetensi: `QT-UK-###`
- Halaman: `QB-J##-H##`
- Kotak: `QB-J##-H##-K##`

### Bahasa Arab

- Kompetensi: `AR-CMP-###`
- Unit kompetensi: `AR-UK-###`
- Mufradat: `AR-J##-MF-###`
- Kalimat: `AR-J##-KL-###`
- Paragraf: `AR-J##-PR-###`

### NIDOM/Akhlak

- Kompetensi: `ND-CMP-###`
- Unit kompetensi: `ND-UK-###`
- Hadits: `ND-J##-HD-###`
- Nilai/adab: `ND-J##-AD-###`

### Pertemuan

- Pertemuan: `MTG-J##-###`

Setiap pertemuan menghubungkan bagian tartil, Bahasa Arab, NIDOM/Akhlak, hafalan, evaluasi, dan prasyarat.

## Status

- `DRAFT`: sedang disusun.
- `REVIEW`: menunggu pemeriksaan.
- `APPROVED`: boleh dipakai di ruang belajar.
- `EXAM_READY`: boleh dipakai generator ujian.
- `FROZEN`: baseline publikasi yang tidak boleh diubah tanpa keputusan versi.

## Larangan

- Tidak boleh ada kode ganda.
- Tidak boleh ada mufradat atau hadits berulang tanpa relasi REVIEW.
- Tidak boleh ada kotak tanpa Unit Kompetensi.
- Tidak boleh ada materi ujian yang belum pernah masuk jalur belajar atau latihan.
- Tidak boleh mengubah Jilid 1-2 baseline tanpa audit dampak ke seluruh jilid berikutnya.
