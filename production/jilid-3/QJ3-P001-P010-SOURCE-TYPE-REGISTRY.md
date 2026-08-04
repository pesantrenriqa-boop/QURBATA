# QJ3 P001–P010 — Source Type Registry

**Status:** ACTIVE-CONTROL
**Cakupan:** 240 kotak pada `QJ3-P001-P010-PRODUCTION-BATCH.md`

## Klasifikasi resmi

1. `ARABIC_LEXICON`
   - Kata Arab sah untuk latihan baca.
   - Tidak otomatis diklaim sebagai kutipan Al-Qur’an.
   - Dapat dinaikkan menjadi `QURAN_VERIFIED` setelah verifikasi mushaf dan Source-ID.

2. `CONTROLLED_DRILL`
   - Bentuk latihan yang sengaja dibangun untuk tujuan visual, artikulasi, mad, atau sukun.
   - Bukan klaim kata atau ayat Al-Qur’an.

3. `CONTROLLED_PATTERN`
   - Pola morfologis/struktur bacaan untuk latihan pengenalan bentuk.
   - Tidak diajarkan sebagai teori nahwu atau sharaf.

4. `QURAN_VERIFIED`
   - Hanya diberikan setelah verifikasi mushaf.
   - Wajib memiliki `Source-ID`, nama surah, dan nomor ayat.

5. `RECOVERY_SOURCE`
   - Menandai contoh yang berasal dari data recovery lama.
   - Tetap harus masuk salah satu tipe substansi di atas sebelum `APPROVED`.

## Controlled drill P001–P010

Contoh berikut wajib bertipe `CONTROLLED_DRILL`:

- `بَتَثَ`
- `جَحَخَ`
- `بَتَ`
- `نَيَ`
- `بَا`
- `تَا`
- `بِي`
- `تِي`
- `بُو`
- `تُو`
- `بَا بِي بُو`
- `تَا تِي تُو`
- `أَبْ`
- `عَبْ`
- `غَفْ`

Contoh berikut wajib bertipe `CONTROLLED_PATTERN`:

- `يَفْعَلُ`
- `يَفْعِلُ`

Semua contoh lain pada batch sementara bertipe `ARABIC_LEXICON` sampai verifikasi mushaf selesai.

## Koreksi duplikasi

Duplikasi internal P009 dikoreksi:

- `QB-J03-H09-K11`: dari `يَسْمَعُ` menjadi `يَفْتَحُ`.

## Aturan promosi status

Sebuah kotak hanya boleh berstatus `APPROVED` jika:

- memiliki `SourceType`;
- tidak duplikat tanpa tujuan review;
- sesuai whitelist kompetensi halaman;
- harakat sudah diaudit;
- jika diklaim Qur’ani, sudah berstatus `QURAN_VERIFIED`;
- jika drill, tidak ditampilkan seolah-olah kata Qur’ani.
