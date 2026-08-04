# Audit Recovery QURBATA Jilid 1–3

**Branch:** `content/qurbata-jilid-1-8-production`  
**Status:** ACTIVE BASELINE AUDIT  
**Tanggal:** 4 Agustus 2026

## Tujuan

Dokumen ini menetapkan kondisi nyata Jilid 1–3 sebelum produksi dilanjutkan. Audit membedakan antara sumber yang sudah ditemukan, halaman kanonik yang siap dipakai, halaman yang masih konflik, dan materi yang belum boleh dianggap final.

## Ringkasan Status

| Jilid | Struktur | Status sumber | Status produksi |
|---|---:|---|---|
| Jilid 1 | 40 halaman | ditemukan dan memiliki jalur kanonik | perlu audit konflik versi serta pemerataan contoh |
| Jilid 2 | 40 halaman | sumber 40/40 ditemukan | 20 COMPLETE-DRAFT, 20 STAGED-BLOCKED |
| Jilid 3 | 40 halaman | empat batch sumber dan versi lanjutan ditemukan | perlu migrasi per halaman dan realignment progression |

## Jilid 1

- Jalur kanonik: `books/jilid-1/pages/QJ1-P001.md` sampai `QJ1-P040.md`.
- Master struktur: `books/jilid-1/QJ1-MASTER-Struktur-40-Halaman.md`.
- P001 telah dicocokkan dengan sumber recovery.
- P002 dan P010 memiliki kandidat sumber terverifikasi dengan gate terbuka.
- P003–P009 dan beberapa halaman lain masih memiliki dua garis versi: pemerataan dan 60:40.
- Halaman khusus tidak dipaksa memakai pola 24 kotak latihan biasa.

### Tindakan

1. Audit 40 halaman satu per satu.
2. Tetapkan satu baseline konten aktif per halaman.
3. Pertahankan versi lama sebagai evidence, bukan sumber produksi.
4. Validasi distribusi huruf, harakat, dan murojaah.

## Jilid 2

- Jalur kanonik: `books/jilid-2/pages/`.
- Master struktur: `books/jilid-2/QJ2-MASTER-Struktur-40-Halaman.md`.
- Baseline sumber 40/40 ditemukan.
- Status baseline: 20 `COMPLETE-DRAFT`, 20 `STAGED-BLOCKED`.
- Versi lama P001–P015 yang berstatus `SUPERSEDED` tidak boleh menggantikan baseline terbaru.

### Tindakan

1. Kunci 20 halaman COMPLETE-DRAFT sebagai kandidat audit akademik.
2. Buka 20 STAGED-BLOCKED hanya setelah prasyarat halaman dan tangga kompetensi jelas.
3. Audit tidak adanya pengulangan kata tanpa tujuan murojaah.
4. Kaitkan setiap halaman dengan kode kompetensi dan Unit Kompetensi pembelajaran.

## Jilid 3

### Sumber Recovery

| Rentang | Commit sumber | Status |
|---|---|---|
| P001–P010 | `3c47a20fb8bb2f9688f4f1521c1068db53274a7c` | FOUND-DRAFT-BATCH |
| P006–P010 versi lanjutan | `f9f9677a6a5388afa740158b969520dc61fbb7a0` | FOUND-LATER-VERSION |
| P011–P020 | `aadd8918ba865a2a4338fdfdf736ceb154b95173` | FOUND-DRAFT-BATCH |
| P021–P030 | `05dfd094584c39e1ef09cee181d75516f52c63a8` | FOUND-DRAFT-BATCH |
| P031–P040 | `fb0a15ddf60239d99aa299dc40ce85a4a531c997` | FOUND-DRAFT-BATCH |
| Master struktur | `e2df1c7aeca82285b23df704697c48178445f98d` | FOUND-MASTER |

### Keputusan progression pengendali

Jilid 3 diposisikan sebagai tahap:

- sukun per huruf target;
- integrasi bertahap kata dan frasa;
- penguatan mad, tanwin, dan pola yang sudah lulus prasyarat;
- tanpa tasydid dan hukum tajwid lanjut sebelum whitelist;
- contoh seperti `يَعْلَمُونَ` boleh masuk hanya pada tangga halaman yang sesuai;
- frasa Al-Qur'an 2–3 kata boleh digunakan apabila seluruh unsur bacaan telah dipelajari.

### Tindakan produksi

1. Ekstrak P001–P040 menjadi halaman kanonik.
2. Audit setiap contoh terhadap whitelist materi halaman.
3. Tandai setiap contoh: NEW, REVIEW, SOURCE-QURAN, SOURCE-LEXICAL, atau HOLD.
4. Keluarkan contoh yang mengandung tasydid atau unsur di atas tangga ke HOLD, bukan dihapus.
5. Terapkan kode `QB-J03-Hxx-Kxx` untuk 24 kotak setiap halaman latihan.
6. Kaitkan setiap halaman dengan Kompetensi dan Unit Kompetensi pembelajaran.

## Ketentuan Halaman Khusus

Halaman 20 dan 40 setiap jilid dipakai secara terencana untuk literasi Al-Qur'an, antara lain:

- nama huruf hijaiyah hanya pada Jilid 1;
- fawātih al-suwar tanpa pengulangan;
- nama harakat;
- nama tanda waqaf;
- istilah bacaan sesuai tingkat;
- pengayaan lain yang belum pernah muncul.

## Gate Produksi

Satu halaman hanya boleh berstatus `CONTENT-READY` jika:

1. jumlah kotak sesuai desain;
2. seluruh contoh sesuai whitelist;
3. materi baru dan review terukur;
4. tidak ada duplikasi tak disengaja;
5. sumber dan kode contoh tercatat;
6. kompetensi dan Unit Kompetensi terhubung;
7. halaman khusus mengikuti fungsi khususnya;
8. status audit akademik tersedia.

## Titik Lanjut Resmi

Prioritas kerja berikutnya adalah **Jilid 3 P001–P010**, dengan urutan:

1. bandingkan batch awal dan versi lanjutan P006–P010;
2. tetapkan progression sukun per huruf target;
3. susun ulang 24 kotak per halaman;
4. audit murojaah dari Jilid 1–2;
5. baru lanjut P011–P040.
