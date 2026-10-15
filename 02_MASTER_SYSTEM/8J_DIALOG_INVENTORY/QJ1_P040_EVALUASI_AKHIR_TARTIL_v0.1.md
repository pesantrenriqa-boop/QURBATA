# QURBATA Jilid 1 — P040 Evaluasi Akhir Tartil v0.1

**DRAF QA; belum FROZEN / belum print-ready.** Acuan: `02_MASTER_SYSTEM/QURBATA-J1-TARTIL-PAGE-REGISTER-FROZEN-v1.0.md`, register P031–P040 FROZEN, overlay integrasi v1.3, matriks empat inventaris P021–P040.

## A. Mengenal huruf tanpa harakat (29 identitas)

1. ء · 2. ا · 3. ب · 4. ت · 5. ث · 6. ج · 7. ح · 8. خ · 9. د · 10. ذ · 11. ر · 12. ز · 13. س · 14. ش · 15. ص · 16. ض · 17. ط · 18. ظ · 19. ع · 20. غ · 21. ف · 22. ق · 23. ك · 24. ل · 25. م · 26. ن · 27. ه · 28. و · 29. ي

Catatan: identitas alif dan hamzah dipisahkan dalam daftar 29; glyph masing-masing harus diverifikasi dengan KFGQPC Uthman Taha. Jangan mengganti ha dengan varian Unicode lain.

## B. Mengenal nama dan tanda harakat

- **فَتْحَةٌ — Fathah:** بَ
- **كَسْرَةٌ — Kasrah:** بِ
- **ضَمَّةٌ — Dhammah:** بُ

## C. Evaluasi membaca huruf lepas (8 × 3 kelompok)

Setiap kelompok berisi tepat tiga huruf lepas, satu Fathah, satu Kasrah, satu Dhammah. Urutan posisi perlu dirandomisasi secara pedagogis pada tahap kurasi guru, tanpa melanggar distribusi. Ini bukan kata Arab bersambung.

| Baris | Kelompok 1 | Kelompok 2 | Kelompok 3 |
|---|---|---|---|
| 1 | بَ جِ خُ | جَ سِ عُ | رَ غِ ءُ |
| 2 | ضَ هِ سُ | فَ ثِ لُ | نَ زِ حُ |
| 3 | تَ عِ ظُ | حَ نِ يُ | زَ تِ زُ |
| 4 | طَ رِ كُ | قَ ظِ جُ | هَ مِ طُ |
| 5 | ثَ بِ وُ | خَ ذِ رُ | سَ طِ قُ |
| 6 | ظَ لِ ثُ | كَ إِ ضُ | وَ دِ هُ |
| 7 | ءَ ضِ ذُ | دَ كِ فُ | شَ ءِ تُ |
| 8 | عَ خِ صُ | لَ صِ نُ | يَ قِ دُ |

## D. Rekap audit awal

- 29 identitas huruf tanpa harakat; 3 nama/tanda harakat.
- 24 kelompok unik: PASS (24/24).
- 72 token: 24 Fathah, 24 Kasrah, 24 Dhammah.
- Tidak ada kompetensi baru, huruf sambung, mad, tanwin, sukun, atau tasydid sebagai materi Tartil.
- Target Tahfidz panel **Al-Ma'un ayat 5–7** sesuai distribusi; Bi'ah **الْحَمْدُ لِلَّهِ**; Akhlak **تَعَلَّمْ — اِعْمَلْ — عَلِّمْ** sesuai overlay v1.3. Teks lengkap ayat dan arti wajib tashih sebelum cetak.

## E. Gate sebelum FINAL

1. Audit sebaran 29 identitas pada evaluasi membaca; jika tidak tercakup, perlu perbaikan kurasi.
2. Uji visual A5, font KFGQPC Uthman Taha, arah RTL, ha dua lubang dan harakat tanpa clipping.
3. Pastikan slot Nilai–Tanggal–Paraf dan QR RIQA OS tidak mengurangi area evaluasi.
4. Periksa pedagogi urutan soal dan arti panel empat inventaris.
5. Jangan mengubah master FROZEN; status tetap DRAF QA.
