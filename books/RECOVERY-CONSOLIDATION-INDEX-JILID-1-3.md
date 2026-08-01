# Indeks Konsolidasi Recovery QURBATA Jilid 1–3

**Kode:** REC-QJ123-INDEX  
**Status:** ACTIVE RECOVERY CONTROL  
**Tanggal:** 1 Agustus 2026  
**Pemilik Akademik:** Aris Liswanto  
**Cabang sumber resmi:** `main`  
**Tujuan:** menemukan, memilih, memverifikasi, dan memindahkan seluruh contoh materi Jilid 1–3 ke satu sumber resmi tanpa duplikasi atau tumpang tindih.

## 1. Prinsip Pengendalian

1. Setiap halaman hanya boleh memiliki satu file kanonik pada `books/jilid-x/pages/`.
2. File lama, staging, recovery, audit, dan batch tidak menjadi sumber produksi setelah halaman kanonik diverifikasi.
3. Isi contoh asli tidak boleh diubah selama tahap ekstraksi; koreksi pedagogis dilakukan pada tahap revisi terkontrol berikutnya.
4. Versi yang berstatus `SUPERSEDED`, `INVALID`, atau dibekukan karena kesalahan tidak boleh dipilih sebagai master.
5. PDF, slide, flashcard, audio, worksheet, dan aplikasi merupakan turunan dari sumber Markdown/data kanonik.
6. Status `SOURCE-COMPLETE` tidak sama dengan `SIAP CETAK` atau `DISETUJUI`.

## 2. Lokasi Kanonik

```text
books/
├── jilid-1/
│   ├── QJ1-MASTER-Struktur-40-Halaman.md
│   ├── RECOVERY-SOURCES.md
│   └── pages/QJ1-P001.md ... QJ1-P040.md
├── jilid-2/
│   ├── QJ2-MASTER-Struktur-40-Halaman.md
│   ├── RECOVERY-SOURCES.md
│   └── pages/QJ2-P001.md ... QJ2-P040.md
└── jilid-3/
    ├── QJ3-MASTER-Struktur-40-Halaman.md
    ├── RECOVERY-SOURCES.md
    └── pages/QJ3-P001.md ... QJ3-P040.md
```

## 3. Register Sumber Utama

### Jilid 1

| Rentang | Sumber utama sementara | Status recovery | Catatan |
|---|---|---|---|
| P001 | `books/jilid-1/pages/QJ1-P001.md`; sumber pembanding `03_BOOKS/JILID-1/PAGE-001.md` | VERIFIED-SOURCE | 64 token telah direkonstruksi menjadi 8 tangga dua huruf dan 16 tangga tiga huruf tanpa perubahan urutan. |
| P002–P040 | Commit `c820ca4c0504185bf5e63d7765089fbd7c4b4e2b` — `books(qj1): complete master through P040` | FOUND-NOT-YET-PAGE-AUDITED | Perlu ekstraksi dan verifikasi per halaman terhadap master serta versi balance terakhir yang sah. |

### Jilid 2

| Rentang | Sumber utama sementara | Status recovery | Catatan |
|---|---|---|---|
| P001–P020 | Baseline `DEC-CUR-010`; dicatat sebagai `COMPLETE-DRAFT` dalam master Jilid 2 v0.22.0-id | FOUND-COMPLETE-DRAFT | Versi lama P001–P015 dinyatakan `SUPERSEDED` dan dilarang dipilih. |
| P021–P024 | Staging tanwin; audit `AUD-QJ2-TAN-003` | FOUND-STAGED-BLOCKED | Menunggu penyelesaian `BLK-QJ2-ORTHO-001`; tetap disimpan sebagai sumber, bukan materi cetak. |
| P025–P030 | Staging materi khusus dan mad; audit `AUD-QJ2-MAD-001` | FOUND-STAGED-BLOCKED | P025 dan P028 memerlukan objek khusus; P026, P027, P029, P030 lulus audit struktur. |
| P031–P040 | Staging akhir; audit `AUD-QJ2-FINAL-001` | FOUND-STAGED-BLOCKED | Seluruh sumber ditemukan tetapi belum diotorisasi untuk cetak. |

**Baseline cakupan Jilid 2:** commit `67a42c40d796cbdcead4e98f5d03da370ac22406`, mencatat sumber tersedia 40/40: 20 `COMPLETE-DRAFT` dan 20 `STAGED-BLOCKED`.

### Jilid 3

| Rentang | File/batch yang ditemukan | Commit | Status recovery | Catatan |
|---|---|---|---|---|
| P001–P010 | `books/JILID-3/PAGE-001-010.md` | `3c47a20fb8bb2f9688f4f1521c1068db53274a7c` | FOUND-DRAFT-BATCH | P001–P005 berisi contoh; P006–P010 pada batch ini belum terisi penuh. |
| P006–P010 | Draft produksi lanjutan | `f9f9677a6a5388afa740158b969520dc61fbb7a0` | FOUND-LATER-VERSION | Harus dibandingkan dengan koreksi sukun per huruf target dan audit P001–P010. |
| P011–P020 | `books/JILID-3/PAGE-011-020.md` | `aadd8918ba865a2a4338fdfdf736ceb154b95173` | FOUND-DRAFT-BATCH | Mengandung kata, frasa, dan potongan ayat; wajib diuji terhadap tangga sukun yang kemudian ditetapkan. |
| P021–P030 | Batch Jilid 3 halaman 21–30 | `05dfd094584c39e1ef09cee181d75516f52c63a8` | FOUND-DRAFT-BATCH | Menunggu ekstraksi per halaman dan audit progression. |
| P031–P040 | Batch Jilid 3 halaman 31–40 | `fb0a15ddf60239d99aa299dc40ce85a4a531c997` | FOUND-DRAFT-BATCH | Menunggu ekstraksi per halaman dan audit progression. |
| Struktur induk | Master Jilid 3 | `e2df1c7aeca82285b23df704697c48178445f98d` | FOUND-MASTER | Wajib disejajarkan dengan keputusan Jilid 3 sebagai tahap sukun tanpa tasydid. |

## 4. Riwayat Jilid 3 yang Tidak Boleh Dipilih Otomatis

Commit/versi berikut wajib diperlakukan sebagai bukti sejarah atau sumber pembanding, bukan langsung sebagai master:

- `4c61a3dcb9390225308b031fe9944fac99f6db2d` — batch Jilid 3 dinyatakan invalid/frozen.
- Versi sebelum realignment Jilid 3 menjadi tahap sukun tanpa tasydid.
- Contoh yang memasukkan materi melampaui whitelist halaman, termasuk tasydid, hukum tajwid, atau struktur yang belum menjadi prasyarat.
- Batch yang masih menggunakan rasio 60:40 apabila bertentangan dengan keputusan 50:50 terbaru.

## 5. Status Halaman

Status baku yang digunakan:

- `NOT-FOUND`
- `FOUND-UNASSESSED`
- `FOUND-DRAFT-BATCH`
- `FOUND-STAGED-BLOCKED`
- `EXTRACTED`
- `SOURCE-VERIFIED`
- `PEDAGOGY-REVIEWED`
- `READY-FOR-PILOT`
- `FROZEN-SOURCE`

Tidak boleh melompati `SOURCE-VERIFIED` sebelum menyatakan sebuah halaman sebagai sumber resmi.

## 6. Urutan Eksekusi

1. Jilid 1 P002–P040: ekstrak isi master ke file halaman dan audit terhadap tangga 24 latihan.
2. Jilid 2 P001–P020: identifikasi file versi baseline `COMPLETE-DRAFT`; abaikan P001–P015 lama yang superseded.
3. Jilid 2 P021–P040: ekstrak sebagai sumber terblokir dengan blocker tetap tercatat.
4. Jilid 3: ekstrak empat batch ke P001–P040; pilih P006–P010 dari versi produksi/koreksi terakhir yang sah.
5. Jalankan pemeriksaan lintas jilid: prasyarat, materi baru, murojaah, harakat, sukun, mad, tanwin, contoh Qurani, dan duplikasi leksikal.
6. Setelah audit, tetapkan satu file kanonik per halaman dan tandai sumber lama `SUPERSEDED-BY` tanpa menghapus bukti sejarah.

## 7. Keputusan Sumber Tunggal

Mulai dokumen ini berlaku, lokasi produksi resmi untuk isi halaman adalah:

- `books/jilid-1/pages/QJ1-Pxxx.md`
- `books/jilid-2/pages/QJ2-Pxxx.md`
- `books/jilid-3/pages/QJ3-Pxxx.md`

Folder `books/JILID-3/`, `03_BOOKS/`, file batch, file staging, dan file recovery hanya menjadi sumber migrasi/riwayat. Tidak boleh menjadi sumber langsung untuk PDF, slide, flashcard, atau aplikasi setelah halaman kanonik tersedia dan berstatus `SOURCE-VERIFIED`.
