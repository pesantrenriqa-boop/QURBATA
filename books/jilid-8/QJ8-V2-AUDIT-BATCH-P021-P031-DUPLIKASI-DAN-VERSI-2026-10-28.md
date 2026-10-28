# QJ8 V2 — Audit Batch P021–P031: Teks, Kompetensi, dan Duplikasi

28 Oktober 2026. Audit berbasis perbandingan berkas repo yang tersedia. Ini audit **konsistensi dokumen**, bukan tashih rasm/qiraat eksternal. Semua teks tetap draf.

## Temuan per halaman

| Halaman | Status audit | Temuan sistematis | Tindakan |
|---|---|---|---|
| P021 | DRAF + overlap | Al-Kahfi 18:38–39 memuat target لَّٰكِنَّا; ayat 39 juga dipakai P028 | Pertahankan, tandai 18:39 sebagai ayat berulang untuk target lain |
| P022 | DRAF + overlap | An-Najm 53:49–51 target عَادًا ٱلْأُولَىٰ; ayat 51 memuat ثَمُودَا untuk calon P032 | Jangan klaim ثَمُودَا sebagai contoh unik P032 |
| P023 | PARSIAL pada file utama | File utama P021–P025 masih hanya menyalin 25:69, meski file pelengkap kemudian memuat 25:68–70 | Sumber kanonik harus file pelengkap; update file utama atau tandai arsip |
| P024 | DRAF | Az-Zumar 39:7 tersedia, target يَرْضَهُ لَكُمْ | Perlu tashih kaidah ha kinayah; jangan otomatis menganggap semua ha kinayah sama |
| P025 | DRAF | Asy-Syu'ara 26:62–64 tersedia, target فِرْقٍ | Label kompetensi dan rincian bacaan harus disahkan guru |
| P026 | DRAF | Al-Baqarah 2:1–3; huruf muqaththa'ah | Uji font dan talaqqi nama huruf/panjang |
| P027 | DRAF | Maryam 19:1–3; huruf muqaththa'ah | Uji font dan talaqqi nama huruf/panjang |
| P028 | DRAF + overlap | Al-Kahfi 18:39–40 target أَنَا; ayat 39 di P021 | Catat sebagai penggunaan ulang, bukan ayat unik baru |
| P029 | PARSIAL pada file utama | File P026–P030 hanya menyalin 33:10; file pelengkap memuat 33:9–11 | Sumber kanonik file pelengkap; update file utama atau tandai arsip |
| P030 | PARSIAL pada file utama | File P026–P030 hanya menyalin 33:66; file pelengkap memuat 33:65–67 | Sumber kanonik file pelengkap; tandai irisan 33:66 dengan P031 |
| P031 | DRAF + overlap | Al-Ahzab 33:66–68; target 33:67; 33:66 dipakai P030 | Tandai ayat 66 sebagai konteks berulang |

## Keputusan sistem untuk mencegah versi ganda

1. **Berkas pelengkap** untuk P023/P029/P030 adalah sumber paling baru bagi konteks ayat lengkap, tetapi berkas utama belum disinkronkan. Sampai sinkronisasi, jangan gunakan berkas utama sebagai sumber cetak.
2. Daftar ayat unik harus memakai kunci `surah:ayat`; daftar kompetensi memakai `page_id + target_lafaz + competency_id`. Ini memisahkan hitungan ayat unik dari hitungan latihan.
3. Relasi pengulangan yang sudah diketahui: P021↔P028 (18:39); P022↔P032 (53:51, P032 HOLD); P030↔P031 (33:66 konteks, target berbeda).
4. P032 tetap HOLD, P033 tetap HOLD. P010 juga tetap HOLD label kompetensi.
5. Jangan tandai status 'tashih' dari sekadar ada teks; kolom rasm, guru, audio, dan layout harus memiliki bukti tersendiri.

## Antrian kerja berikutnya

- Sinkronkan P023/P029/P030 ke berkas utama atau tetapkan satu sumber kanonik.
- Jalankan audit yang sama untuk P036–P040 (rubrik dan bank ujian), lalu buat indeks kanonik yang menunjuk ke semua file tanpa menduplikasi teks Arab.
- Setelah itu, lakukan tashih guru pada batch kecil per kompetensi.

## Sumber
- [P021–P025 utama](QJ8-V2-AYAT-NYATA-P021-P025-2026-10-28.md)
- [P026–P030 utama](QJ8-V2-AYAT-NYATA-P026-P030-2026-10-28.md)
- [Pelengkap P023/P029/P030](QJ8-V2-PELENGKAP-AYAT-P023-P029-P030-2026-10-28.md)
- [P031–P035 dan HOLD](QJ8-V2-P031-P035-AYAT-DAN-AUDIT-HOLD-2026-10-28.md)

**Kesimpulan batch:** 11 halaman ditinjau; 3 halaman punya versi utama yang masih parsial; 3 relasi pengulangan teridentifikasi; 0 halaman disahkan siap cetak.


## Koreksi setelah revisi P032 — 28 Oktober 2026

Catatan lama yang mengaitkan P032 sebagai pengulangan An-Najm 53:51 kini hanya berlaku untuk draf lama. Contoh utama P032 dipindahkan ke Hud 11:68 (lafaz ثَمُودَا), sebagaimana didokumentasikan pada `QJ8-V2-REVISI-P032-THAMUDA-HUD-11-68-2026-10-28.md` dan diselaraskan ke `QJ8-V2-P031-P035-AYAT-DAN-AUDIT-HOLD-2026-10-28.md`. P022 tetap menggunakan An-Najm 53:49–51 dengan target عَادًا ٱلْأُولَىٰ; ayat 53:51 hanya konteks. Status P032 tetap DRAF karena perbedaan wajah qiraat yang ditampilkan sumber daring dan tanda rasm harus disahkan guru Hafs serta dibandingkan dengan mushaf acuan.
