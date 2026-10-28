# QJ8 V2 — Keputusan Audit P010, P032, P033 dan Register Anti-Duplikasi

28 Oktober 2026. **Keputusan editorial sementara**, bukan fatwa qiraat, bukan tashih guru, dan bukan perubahan kompetensi resmi. Dokumen ini melanjutkan audit P001–P040.

## 1. P010 — بِئْسَ ٱلِٱسْمُ (Al-Hujurat 49:11)

- **Lokasi ayat jelas:** Al-Hujurat 49:11, teks ayat utuh telah tercatat pada master P001–P010.
- **Masalah:** label 'naql' pada draf sebelumnya belum didukung rujukan pedagogis yang ditetapkan. Jangan otomatis menamainya naql Hafsh.
- **Keputusan:** **HOLD LABEL, RETAIN AYAT**. Judul kerja: *bacaan khusus pada بِئْسَ ٱلِٱسْمُ*, tanpa menyebut kaidah yang belum ditashih.
- **Syarat rilis:** guru ahli mengesahkan istilah, wajah bacaan, dan contoh audio.

## 2. P032 — ثَمُودَا (An-Najm 53:51)

- **Lokasi kandidat teridentifikasi:** An-Najm 53:51: وَثَمُودَا۟ فَمَآ أَبْقَىٰ.
- **Masalah:** ayat ini sudah tercakup dalam konteks P022 (An-Najm 53:49–51). Mengulangnya pada P032 sebagai 'contoh baru' menimbulkan duplikasi.
- **Keputusan editorial:** ubah P032 dari HOLD kompetensi menjadi **DRAF PENGUATAN — mad/qasr pada lafaz ثَمُودَا**, bukan contoh ayat unik baru. Sumber pembelajaran tajwid yang ditemukan menyebut ثَمُودَا dibaca pendek dan memberi contoh An-Najm 53:51; namun kategori, cara praktik, dan teks mushaf tetap perlu disahkan guru Hafsh sebelum produksi. P022 tetap dihitung sebagai konteks berulang.
- **Syarat rilis:** verifikasi mushaf Hafsh dan putuskan apakah tetap berdiri sendiri atau digabung dengan halaman tanda alif.

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

Rujukan pembelajaran tajwid yang ditemukan menjelaskan lafaz ثَمُودَا sebagai bacaan pendek, dengan contoh pada An-Najm 53:51. Oleh sebab itu P032 dapat diteruskan sebagai **draf penguatan mad/qasr**, tetapi bukan contoh ayat unik. Validasi guru Hafsh dan mushaf acuan masih wajib. P033 tetap HOLD.
Rujukan pendukung: https://tafsiralquran.id/bacaan-gharib-dalam-al-quran-menurut-riwayat-imam-hafs/.
