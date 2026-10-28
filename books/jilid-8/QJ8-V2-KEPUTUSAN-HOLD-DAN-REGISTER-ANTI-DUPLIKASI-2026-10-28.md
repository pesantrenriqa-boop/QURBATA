# QJ8 V2 — Keputusan Audit P010, P032, P033 dan Register Anti-Duplikasi

28 Oktober 2026. **Keputusan editorial sementara**, bukan fatwa qiraat, bukan tashih guru, dan bukan perubahan kompetensi resmi. Dokumen ini melanjutkan audit P001–P040.

## 1. P010 — Naql, بِئْسَ ٱلِٱسْمُ (Al-Hujurat 49:11)

- **Keputusan terbaru:** label P010 dipetakan sebagai **Naql** pada draf keputusan P010, commit `283e2a36`, dengan rujukan pendukung yang dicatat di berkas keputusan tersebut.
- **Status:** DRAF, bukan HOLD label. Tashih teks Utsmani, wajah bacaan, dan audio tetap wajib sebelum produksi.
- **Catatan:** keputusan editorial ini tidak menggantikan pengesahan guru Hafsh.

## 2. P032 — ثَمُودَا (contoh utama: Hud 11:68)

- **Keputusan terbaru:** kandidat utama P032 adalah QS. Hud 11:68, lafaz ثَمُودَا, bukan An-Najm 53:51.
- **Alasan:** menghindari penggunaan ulang An-Najm 53:51 yang sudah menjadi konteks P022. Sumber pembelajaran gharib menyebut contoh Hud 11:68.
- **Status:** DRAF; belum tashih karakter rasm, wajah bacaan Hafs, atau audio.
- **Sumber aktif:** [revisi P032](QJ8-V2-REVISI-P032-THAMUDA-HUD-11-68-2026-10-28.md) dan [berkas P031–P035](QJ8-V2-P031-P035-AYAT-DAN-AUDIT-HOLD-2026-10-28.md).
- **Catatan:** setiap referensi lama yang menyebut P032=An-Najm 53:51 adalah riwayat draf, bukan keputusan aktif.

## 3. P033 — 'Nun wiqayah'

- **Masalah:** نون الوقاية dalam nahwu adalah kategori gramatika; belum ada bukti dari kompetensi resmi bahwa ia perlu menjadi bab gharib bacaan Hafsh. Al-Baqarah 2:180 tidak boleh dijadikan contoh hanya karena pernah tercatat sebagai kandidat.
- **Keputusan:** **HOLD PENUH — 0 ayat baru**. Jangan memproduksi teks, audio, atau ujian P033 sebelum istilah diperjelas.
- **Opsi untuk diputuskan pengampu:** (a) ganti dengan kasus gharib Hafsh yang memang belum diajarkan dan terverifikasi; (b) jadikan halaman remedial/diagnostik dengan materi sebelumnya, bukan materi baru.

## 4. Register identitas ayat untuk mencegah duplikasi

| ID latihan | Halaman | Surah:ayat | Sasaran | Jenis | Catatan |
|---|---|---|---|---|---|
| QJ8-021 | P021 | 18:38–39 | لَّٰكِنَّا | Baru | 18:39 juga digunakan P028 |
| QJ8-028 | P028 | 18:39–40 | أَنَا | Fokus berbeda | Ulang ayat 18:39; jangan klaim unik |
| QJ8-022 | P022 | 53:49–51 | عَادًا ٱلْأُولَىٰ | Baru | 53:51 muncul lagi P032 |
| QJ8-032 | P032 | 53:51 | ثَمُودَا | Penguatan/ulang | Bukan ayat unik; fokus mad/qasr harus disahkan guru |
| QJ8-030 | P030 | 33:66 | ٱلرَّسُولَا | Baru | 33:66 juga konteks P031 |
| QJ8-031 | P031 | 33:66–68 | ٱلسَّبِيلَا | Fokus berbeda | Jangan hitung 33:66 sebagai ayat unik baru |
| QJ8-019 | P019 | 76:15 | قَوَارِيرَا | Baru | Waqf ayat 15 |
| QJ8-020 | P020 | 76:16 | قَوَارِيرَا | Baru | Waqf ayat 16, ayat berbeda |

**Kunci pemeriksaan:** `surah:ayat + target + tujuan kompetensi`. Satu ayat boleh dipakai untuk tujuan berbeda, tetapi sistem harus menandainya sebagai **ulang ayat**, bukan tambahan ayat unik. Jangan menghitung potongan lafaz sebagai ayat tersendiri.

## 5. Gerbang validasi dan langkah produksi

- [ ] Pengampu menyetujui kompetensi resmi Jilid 8 dan memutuskan P010/P032/P033.
- [ ] Satu mushaf Utsmani Hafsh menjadi sumber tunggal untuk seluruh karakter dan tanda khusus.
- [ ] Tashih audio/talaqqi untuk saktah, imalah, isymam, tashil, waqf.
- [x] Transkripsi konteks P023, P029, P030 sudah disinkronkan ke berkas utama pada commit d42e87c9 dan 4d4093d8; tashih rasm tetap belum dilakukan.
- [ ] Buat manifest halaman dengan ID, sumber, sasaran, jenis baru/ulang, status QA.
- [ ] Susun PDF A5 hanya dari bacaan yang telah disahkan.

**Status:** 40/40 halaman memiliki rancangan; 3 HOLD; 0/40 siap cetak. Jangan mengklaim 360 slot terverifikasi.

## Sumber repo
- [Audit status P001–P040](QJ8-V2-AUDIT-KONSOLIDASI-STATUS-P001-P040-2026-10-28.md)
- [Master P001–P010](QJ8-MASTER-V2-P001-P010-KONSOLIDASI-2026-10-28.md)
- [P021–P025](QJ8-V2-AYAT-NYATA-P021-P025-2026-10-28.md)
- [P026–P030](QJ8-V2-AYAT-NYATA-P026-P030-2026-10-28.md)
- [P031–P035](QJ8-V2-P031-P035-AYAT-DAN-AUDIT-HOLD-2026-10-28.md)


## Pembaruan status sinkronisasi — 28 Oktober 2026

P023, P029, dan P030 sudah tidak menunggu transkripsi konteks: rentang ayat telah disalin ke berkas utama. Statusnya tetap DRAF karena belum dicocokkan karakter demi karakter dengan mushaf rujukan dan belum ditashih guru. Catatan lama tentang konteks parsial dibaca sebagai riwayat sebelum sinkronisasi.


## Pembaruan keputusan P032 — 28 Oktober 2026

Contoh utama P032 dialihkan ke QS. Hud 11:68, lafaz ثَمُودَا, karena sumber pembelajaran gharib Hafsh menyebut contoh tersebut untuk bacaan pendek. Ini menghindari penggunaan ulang An-Najm 53:51 dari konteks P022. Lihat [revisi P032](QJ8-V2-REVISI-P032-THAMUDA-HUD-11-68-2026-10-28.md). Status DRAF; tashih guru dan rasm tetap wajib. P033 tetap HOLD.
Rujukan: https://tafsiralquran.id/bacaan-gharib-dalam-al-quran-menurut-riwayat-imam-hafs/.
