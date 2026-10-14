# INDEKS INVENTARIS PERCAKAPAN QURBATA — 8 JILID

Status: **inventaris draf per halaman tersedia (320/320); bukan 320 halaman siap cetak**.

## Berkas tiap jilid

| Jilid | Inventaris percakapan | Pengayaan jawaban santri | Status |
|---|---|---|---|
| 1 | QJ1_P001-P010_DIALOG_TERINTEGRASI_v0.2.md dan QJ1_P011-P040_DIALOG_TERINTEGRASI_v0.3.md | jawaban posisi ditambahkan pada P001–P010 dan respons P011–P040 | Draf; J1 Tartil tunduk register FROZEN |
| 2 | QJ2_P001-P040_DIALOG_TERINTEGRASI_v0.1.md | QJ2_P001-P040_JAWABAN_KONTEKSTUAL_v0.2.md | Draf |
| 3 | QJ3_P001-P040_DIALOG_TERINTEGRASI_v0.1.md | QJ3_P001-P040_JAWABAN_KONTEKSTUAL_v0.2.md | Draf |
| 4 | QJ4_P001-P040_DIALOG_TERINTEGRASI_v0.1.md | QJ4_P001-P040_JAWABAN_KONTEKSTUAL_v0.2.md | Draf |
| 5 | QJ5_P001-P040_DIALOG_TERINTEGRASI_v0.1.md | QJ5_P001-P040_JAWABAN_KONTEKSTUAL_v0.2.md | Draf |
| 6 | QJ6_P001-P040_DIALOG_TERINTEGRASI_v0.1.md | QJ6_P001-P040_JAWABAN_KONTEKSTUAL_v0.2.md | Draf |
| 7 | QJ7_P001-P040_DIALOG_TERINTEGRASI_v0.1.md | QJ7_P001-P040_JAWABAN_KONTEKSTUAL_v0.2.md | Draf |
| 8 | QJ8_P001-P040_DIALOG_TERINTEGRASI_v0.1.md | QJ8_P001-P040_JAWABAN_KONTEKSTUAL_v0.2.md | Draf |

Semua nama berkas di atas berada dalam folder ini.

## Aturan isi

Tiap halaman mengandung fokus Tartil, pengantar guru, respons santri, dialog Tahfidz, dan penutup/asesmen. Kalimat bahasa Arab yang disusun guru adalah materi komunikasi pedagogis, bukan ayat. Respons santri harus dipasangkan dengan objek aktual; jangan menganggap jawaban posisi atau hukum yang kondisional sebagai kunci final.

## Kesenjangan sebelum produksi

1. Contoh Qurani autentik, surah dan nomor ayat per kompetensi Tartil, belum diaudit untuk 320 halaman.
2. Distribusi Tahfidz yang spesifik belum lengkap dan perlu dicocokkan dengan baseline resmi, khususnya Jilid 2–8.
3. Akhlak/Hadits per halaman beserta sumber dan status ayat/hadits belum terintegrasi lengkap.
4. Dialog Arab masih ada pola generik; butuh penyuntingan bahasa dan jawaban yang benar-benar sesuai setiap contoh.
5. Kelayakan beban teks untuk buku A5, proporsi Tartil dominan, dan pemisahan materi buku santri dari buku guru belum diputuskan.

**Gate:** jangan mengubah register FROZEN Jilid 1, jangan menyebut seluruh isi final, dan jangan produksi PDF massal sebelum audit domain dan nash selesai.

## Pembaruan audit sumber Tahfidz 14 Oktober 2026

- `QURBATA_8J_TAHFIDZ_CROSSWALK_FROZEN_320P_v0.1.md` menginventaris 320 target surah/ayat dari mapping yang secara eksplisit dirujuk FROZEN distribusi.
- `QJ1_P001-P040_MATRIKS_SUMBER_4_DOMAIN_QA_v0.1.md` mengikat Tartil dan Bi'ah/Akhlak J1 ke register masing-masing.
- `AUDIT_KONFLIK_TAHFIDZ_J1_BLOKER_v0.1.md` mengungkap konflik mapping Tahfidz J1 dengan register halaman; **status BLOCKER** tetap berlaku.
- Catatan pembetulan: frasa 'Tahfidz P011–P020 belum memiliki sumber' pada matriks awal berarti tidak eksplisit dalam register Tartil yang dibaca, **bukan** bahwa target belum dipetakan di repositori. Sumber distribusi lengkap ditemukan kemudian.
- Belum ada tashih nash Qurani per ayat, verifikasi terjemah, atau pemeriksaan beban. Jangan sebut siap cetak.

## Matriks produksi J1 lengkap P001–P040 (14 Oktober 2026)

- P001–P010: `QJ1_P001-P040_MATRIKS_SUMBER_4_DOMAIN_QA_v0.1.md` serta pilot `QJ1_P001-P006_PILOT_AYAT_TAHFIDZ_TALQIN_QA_v0.1.md` dan `QJ1_P007-P010_PILOT_TAHFIDZ_BIAH_AKHLAK_QA_v0.1.md`.
- P011–P020: `QJ1_P011-P020_PRODUCTION_CONTROL_v0.1.md`.
- P021–P030: `QJ1_P021-P030_PRODUCTION_CONTROL_v0.1.md`.
- P031–P040: `QJ1_P031-P040_PRODUCTION_CONTROL_v0.1.md`.
- Cakupan matriks kendali sumber: **40/40 halaman**. Ini tidak berarti naskah pedagogis, contoh ayat, terjemah, tashih, layout atau PDF sudah selesai.
- **BLOCKER:** konflik Tahfidz antarsumber J1; baca `AUDIT_KONFLIK_TAHFIDZ_J1_BLOKER_v0.1.md`. Jangan mencampur jalur target Tahfidz tanpa keputusan kurikulum.
