# QJ8 — ERRATA PRIORITAS dan Audit Konsistensi Teks (28 Oktober 2026)
**Status:** audit editorial internal atas register GitHub; BUKAN verifikasi karakter-per-karakter terhadap mushaf resmi, bukan tashih qiraat. Master tidak diubah.

## ERRATA-001 — Al-Insan 76:16
Dalam transkripsi P021–P030, sejumlah kotak menggunakan **قَوَارِيرَا** untuk **QS 76:16**, padahal draf P031–P040 sudah membedakan **قَوَارِيرَ** untuk ayat 16. Teks ini tidak konsisten dan tidak boleh dipakai cetak sebelum verifikasi mushaf Hafsh.

| Slot-ID | Nilai lama | Kandidat koreksi teks | QS | Tindakan |
|---|---|---|---|---|
| QJ8-P026-K02 | قَوَارِيرَا | قَوَارِيرَ | 76:16 | GANTI setelah cocok mushaf |
| QJ8-P026-K06 | قَوَارِيرَا مِن فِضَّةٍ | قَوَارِيرَ مِن فِضَّةٍ | 76:16 | GANTI setelah cocok mushaf |
| QJ8-P028-K04 | قَوَارِيرَا | قَوَارِيرَ | 76:16 | GANTI setelah cocok mushaf |
| QJ8-P028-K08 | قَوَارِيرَا مِن فِضَّةٍ | قَوَارِيرَ مِن فِضَّةٍ | 76:16 | GANTI setelah cocok mushaf |
| QJ8-P030-K07 | قَوَارِيرَا | قَوَارِيرَ | 76:16 | GANTI setelah cocok mushaf |
| QJ8-P026-K09 | قَوَارِيرَا | **AMBIGU**: 76:15 atau 76:16 | 76:15–16 | PECAH menjadi dua rujukan/dua kotak, atau tetapkan satu ayat secara tegas |

**Catatan:** ejaan yang ditunjukkan merupakan *kandidat koreksi editorial*, bukan penetapan akhir rasm Utsmani. Penetapan cara wasal/waqaf, termasuk kemungkinan wajah yang diizinkan, harus mengikuti jalur Hafsh RIQA dan talaqqi.

## ERRATA-002 — Master dan cakupan
- Master resmi P018 = Hafalan 1, P028 = Bahasa Arab 8, P036 = Hafalan 2, P038 = Akhlak/Hadis 8; seluruhnya tertimpa dalam register alternatif gharib.
- **Tidak ada perubahan master** tanpa Decision-ID. Empat halaman ini HOLD untuk keputusan akademik, bukan siap rilis.
- P013–P014 (hamzatul washl) dan P018–P019 (muqaththa'ah) perlu dicek terhadap kurikulum jilid 1–7 agar tidak menggandakan materi.

## ERRATA-003 — Audit desain kotak
- P031–P040 berisi banyak pengulangan lafaz yang sama; ini **latihan retensi**, bukan 90 ayat baru.
- Setiap kotak membutuhkan kategori **GHARIB-TARGET**, **QURAN-CONTEXT**, **REPEAT-PRACTICE**, atau **ASSESSMENT**; hanya kategori pertama dihitung sebagai sasaran gharib.
- Teks Arab dari konteks ayat juga memerlukan pencocokan rasm/harakat dan Source-ID, bukan hanya teks sasaran.

## Gate pelaksanaan
1. Koreksi lima slot teridentifikasi dan satu slot ambigu di atas pada dokumen sumber, setelah cek mushaf.
2. Audit seluruh 360 kotak secara mekanis: rujukan, duplikasi, teks kosong, inkonsistensi teks pada ayat sama.
3. Tetapkan edisi mushaf dan jalur Hafsh; periksa teks, tanda khusus, dan panjang bacaan secara manual oleh pemeriksa berwenang.
4. Setelah itu isi Evidence-ID/reviewer/Decision-ID; jangan ubah status siap cetak sebelum seluruh gate terpenuhi.

## Progres akurat
| Indikator | Hasil |
|---|---:|
| Kotak dengan teks Arab draf | 360/360 |
| Ketidakkonsistenan spesifik teridentifikasi pada QS 76:16 | 5 slot + 1 slot ambigu |
| Kotak lolos verifikasi mushaf | 0/360 |
| Kotak lolos tashih ahli | 0/360 |
| Halaman berstatus RELEASED | 0/40 |
