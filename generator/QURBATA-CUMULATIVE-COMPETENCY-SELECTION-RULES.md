# QURBATA Generator — Cumulative Competency Selection Rules

**Status:** ACTIVE RULESET

## Input halaman

Setiap halaman harus memberikan:

- `Volume`
- `Page`
- `NewCompetencies`
- `PreviouslyActivatedCompetencies`
- `UsedWordIdsCurrentBlock`
- `TargetWordCount` = 24

## Kompetensi tersedia

```text
AvailableCompetencies
= PreviouslyActivatedCompetencies ∪ NewCompetencies
```

## Filter wajib

Kandidat hanya lolos bila:

1. seluruh `RequiredCompetencies` berada dalam `AvailableCompetencies`;
2. `AllowedFromVolume` dan `AllowedFromPage` sudah tercapai;
3. `Status = ACTIVE`;
4. `SourceStatus = QURAN_VERIFIED`;
5. `WordId` belum digunakan dalam blok 10 halaman aktif;
6. tidak mengandung unsur yang kompetensinya belum aktif;
7. berupa kata utuh untuk Jilid 3 dan sesudahnya.

## Komposisi halaman

- Materi baru: contoh baru yang memuat `NewCompetencies`.
- Review kompetensi dekat: contoh baru yang memuat kompetensi 1–3 halaman sebelumnya.
- Review kompetensi menengah: contoh baru dari kompetensi 4–10 halaman sebelumnya.
- Review kompetensi lama: contoh baru dari seluruh kompetensi awal jilid/jilid sebelumnya.

Tidak satu pun kategori review boleh diisi dengan menyalin contoh lama secara otomatis.

## Urutan pemilihan

1. Pilih kandidat materi baru dengan dependency paling sederhana.
2. Pilih kandidat review kompetensi dekat yang belum pernah dipakai.
3. Pilih kandidat review menengah.
4. Pilih kandidat review lama berdasarkan `ReviewWeight` dan review debt.
5. Seimbangkan panjang kata, bentuk huruf, makhraj, mad, sukun, tanwin, serta tingkat kesulitan.
6. Tolak halaman bila jumlah contoh valid kurang dari 24.

## Review debt

```text
ReviewDebt = CurrentPage - LastCompetencyAppearancePage
```

Semakin besar nilai `ReviewDebt`, semakin tinggi prioritas kompetensi tersebut untuk diulang dengan contoh baru.

## Validator

Halaman gagal bila:

- ada contoh yang dependency-nya belum aktif;
- ada contoh yang sama dalam blok 10 halaman;
- ada dua huruf/suku kata sebagai filler pada Jilid 3+;
- jumlah kata bukan 24;
- seluruh review hanya berasal dari kompetensi dekat dan tidak mewakili kompetensi lama;
- terdapat materi baru yang belum didefinisikan sebagai Unit Kompetensi.
