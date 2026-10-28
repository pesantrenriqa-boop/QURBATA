# QJ8 — Audit Tahap 3: Sin/Shad, Mad Farq, dan Waqaf Khusus (28 Oktober 2026)

**Status:** AUDIT-INDEKS / HOLD-CETAK. Ini pemeriksaan internal atas 80 kotak yang terindeks dalam matriks klasifikasi, **bukan** tashih mushaf, pengesahan wajah qiraat, atau izin rilis. Tidak ada slot menjadi PASS.

## Metode dan hasil hitung
Sumber data internal: `QJ8-MATRIKS-KLASIFIKASI-360-KOTAK-2026-10-28.md` pada commit induk `dd4c8461`. Semua baris yang berlabel SIN-SHAD, MAD-FARQ, WAQF-KHUSUS dihitung berdasarkan Slot-ID tanpa deduplikasi. Lokasi QS yang sama dihitung sekali sebagai kasus ayat (bukan sekali per kotak); pola konteks ayat tidak dianggap kasus baru.

| Label draf | Kotak | Lokasi unik setelah normalisasi QS | Keputusan tahap 3 |
|---|---:|---:|---|
| SIN-SHAD | 11 | 2 (2:245, 88:22) | LOKASI-TERINDEKS; WAJH-BACA-PENDING |
| MAD-FARQ | 26 | 4 (6:143, 10:59, 10:51, 10:91) | REVIEW-KLASIFIKASI, khususnya 10:51 dan 10:91 |
| WAQF-KHUSUS | 43 | 4 (76:4, 76:15, 76:16, 18:38) | WAQF/WASL-PENDING |
| **Total** | **80** | **10** | **0 TASHIH** |

## Kasus yang harus diperiksa ahli
| Case-ID | Label draf | QS | Lafaz dalam draf | Catatan audit |
|---|---|---|---|---|
| SS-01 | Sin/Shad | 2:245 | وَيَبْصُطُ | Harus cocokkan bentuk sin/shad serta cara baca Hafsh pada mushaf acuan; jangan menjadikan ejaan Unicode bukti bunyi. |
| SS-02 | Sin/Shad | 88:22 | بِمُصَيْطِرٍ | Harus cocokkan bentuk rasm/ḍabṭ dan pilihan bacaan jalur Hafsh; teks draf belum final. |
| MF-01 | Mad farq (draf) | 6:143 | ءَآلذَّكَرَيْنِ | Contoh interogatif dengan alif-lam; periksa label dan panjang bacaan pada referensi Hafsh. |
| MF-02 | Mad farq (draf) | 10:59 | ءَآللَّهُ | Contoh interogatif; verifikasi bentuk dan panjang pada mushaf serta talaqqi. |
| MF-03 | **KLASIFIKASI-PERLU-KOREKSI** | 10:51 | ءَآلْـَٰٔنَ | Jangan disahkan otomatis sebagai mad farq. Umumnya dibahas juga sebagai mad lazim kalimi mukhaffaf; tetapkan terminologi kurikulum dan wajah baca melalui reviewer. |
| MF-04 | **KLASIFIKASI-PERLU-KOREKSI** | 10:91 | ءَآلْـَٰٔنَ | Sama dengan MF-03, tetapi tetap ayat berbeda; jangan hilangkan dari inventaris lokasi. |
| WK-01 | Waqaf khusus | 76:4 | سَلَٰسِلَا | Periksa wajah waqaf dan wasal (termasuk alif pada akhir) sesuai jalur/edisi mushaf, bukan hanya rasm draf. |
| WK-02 | Waqaf khusus | 76:15 | قَوَارِيرَا | Bedakan tegas dari lafaz ayat 16; cek alif dan cara baca ketika berhenti/menyambung. |
| WK-03 | Waqaf khusus | 76:16 | قَوَارِيرَ | Jangan disamakan dengan ayat 15; verifikasi bentuk final dan perlakuan waqaf. |
| WK-04 | Waqaf khusus | 18:38 | لَّٰكِنَّا | Periksa pembacaan alif ketika waqaf vs wasal dan konteks ayat. |

**Catatan kewaspadaan:** jumlah 4 lokasi pada kelompok MAD-FARQ adalah *lokasi yang diberi label demikian di register*, **bukan** empat contoh yang seluruhnya telah dikonfirmasi sebagai hukum mad farq. Kasus `P023-K09` bertanda `10:51 / 10:91` adalah satu kotak ambigu yang menunjuk dua ayat; wajib dipisah rujukannya atau diperjelas instruksi latihan sebelum cetak.

## Register 80 slot (hasil ekstraksi dari matriks)
| Slot-ID | Label mekanis | Teks Arab draf | QS draf | Status |
|---|---|---|---|---|
| P009-K05 | SIN-SHAD | وَيَبْصُطُ | 2:245 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P009-K08 | SIN-SHAD | بِمُصَيْطِرٍ | 88:22 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P009-K09 | SIN-SHAD | لَّسْتَ عَلَيْهِم بِمُصَيْطِرٍ | 88:22 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P010-K08 | SIN-SHAD | وَيَبْصُطُ | 2:245 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P010-K09 | SIN-SHAD | بِمُصَيْطِرٍ | 88:22 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P033-K02 | SIN-SHAD | وَيَبْصُطُ | 2:245 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P033-K03 | SIN-SHAD | بِمُصَيْطِرٍ | 88:22 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P033-K05 | SIN-SHAD | وَيَبْصُطُ | 2:245 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P033-K06 | SIN-SHAD | بِمُصَيْطِرٍ | 88:22 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P033-K08 | SIN-SHAD | وَيَبْصُطُ | 2:245 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P033-K09 | SIN-SHAD | بِمُصَيْطِرٍ | 88:22 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P021-K02 | MAD-FARQ | ءَآلذَّكَرَيْنِ | 6:143 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P022-K07 | MAD-FARQ | قُلْ ءَآللَّهُ | 10:59 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P023-K03 | MAD-FARQ | ءَآلْـَٰٔنَ | 10:51 | REVIEW-KLASIFIKASI; TASHIH-PENDING |
| P023-K06 | MAD-FARQ | ءَآلْـَٰٔنَ | 10:91 | REVIEW-KLASIFIKASI; TASHIH-PENDING |
| P023-K09 | MAD-FARQ | ءَآلْـَٰٔنَ | 10:51 / 10:91 | REVIEW-KLASIFIKASI; TASHIH-PENDING |
| P029-K05 | MAD-FARQ | ءَآلذَّكَرَيْنِ | 6:143 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P029-K06 | MAD-FARQ | ءَآللَّهُ | 10:59 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P030-K01 | MAD-FARQ | ءَآلذَّكَرَيْنِ | 6:143 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P030-K02 | MAD-FARQ | ءَآللَّهُ | 10:59 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P030-K03 | MAD-FARQ | ءَآلْـَٰٔنَ | 10:51 | REVIEW-KLASIFIKASI; TASHIH-PENDING |
| P030-K04 | MAD-FARQ | ءَآلْـَٰٔنَ | 10:91 | REVIEW-KLASIFIKASI; TASHIH-PENDING |
| P030-K09 | MAD-FARQ | ءَآلذَّكَرَيْنِ | 6:143 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P034-K01 | MAD-FARQ | ءَآلذَّكَرَيْنِ | 6:143 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P034-K02 | MAD-FARQ | ءَآللَّهُ | 10:59 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P034-K03 | MAD-FARQ | ءَآلْـَٰٔنَ | 10:51 | REVIEW-KLASIFIKASI; TASHIH-PENDING |
| P034-K04 | MAD-FARQ | ءَآلْـَٰٔنَ | 10:91 | REVIEW-KLASIFIKASI; TASHIH-PENDING |
| P034-K05 | MAD-FARQ | ءَآلذَّكَرَيْنِ | 6:143 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P034-K06 | MAD-FARQ | ءَآللَّهُ | 10:59 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P034-K07 | MAD-FARQ | ءَآلْـَٰٔنَ | 10:51 | REVIEW-KLASIFIKASI; TASHIH-PENDING |
| P034-K08 | MAD-FARQ | ءَآلْـَٰٔنَ | 10:91 | REVIEW-KLASIFIKASI; TASHIH-PENDING |
| P034-K09 | MAD-FARQ | ءَآلذَّكَرَيْنِ | 6:143 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P038-K04 | MAD-FARQ | ءَآلذَّكَرَيْنِ | 6:143 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P038-K05 | MAD-FARQ | ءَآللَّهُ | 10:59 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P039-K06 | MAD-FARQ | ءَآلذَّكَرَيْنِ | 6:143 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P039-K09 | MAD-FARQ | ءَآللَّهُ | 10:59 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P040-K07 | MAD-FARQ | ءَآللَّهُ | 10:59 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P024-K04 | WAQF-KHUSUS | سَلَٰسِلَا | 76:4 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P024-K08 | WAQF-KHUSUS | لِلْكَٰفِرِينَ سَلَٰسِلَا | 76:4 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P024-K09 | WAQF-KHUSUS | سَلَٰسِلَا وَأَغْلَٰلًا | 76:4 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P025-K07 | WAQF-KHUSUS | قَوَارِيرَا | 76:15 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P025-K09 | WAQF-KHUSUS | كَانَتْ قَوَارِيرَا | 76:15 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P026-K01 | WAQF-KHUSUS | قَوَارِيرَا | 76:15 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P026-K02 | WAQF-KHUSUS | قَوَارِيرَ | 76:16 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P026-K06 | WAQF-KHUSUS | قَوَارِيرَ مِن فِضَّةٍ | 76:16 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P026-K08 | WAQF-KHUSUS | كَانَتْ قَوَارِيرَا | 76:15 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P026-K09 | WAQF-KHUSUS | قَوَارِيرَا | 76:15 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P027-K01 | WAQF-KHUSUS | لَّٰكِنَّا | 18:38 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P027-K07 | WAQF-KHUSUS | لَّٰكِنَّا هُوَ ٱللَّهُ | 18:38 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P028-K01 | WAQF-KHUSUS | سَلَٰسِلَا | 76:4 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P028-K03 | WAQF-KHUSUS | قَوَارِيرَا | 76:15 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P028-K04 | WAQF-KHUSUS | قَوَارِيرَ | 76:16 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P028-K05 | WAQF-KHUSUS | لَّٰكِنَّا | 18:38 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P028-K07 | WAQF-KHUSUS | سَلَٰسِلَا وَأَغْلَٰلًا | 76:4 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P028-K08 | WAQF-KHUSUS | قَوَارِيرَ مِن فِضَّةٍ | 76:16 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P028-K09 | WAQF-KHUSUS | لَّٰكِنَّا هُوَ ٱللَّهُ | 18:38 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P029-K07 | WAQF-KHUSUS | سَلَٰسِلَا | 76:4 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P029-K08 | WAQF-KHUSUS | لَّٰكِنَّا | 18:38 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P029-K09 | WAQF-KHUSUS | قَوَارِيرَا | 76:15 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P030-K05 | WAQF-KHUSUS | سَلَٰسِلَا | 76:4 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P030-K06 | WAQF-KHUSUS | قَوَارِيرَا | 76:15 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P030-K07 | WAQF-KHUSUS | قَوَارِيرَ | 76:16 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P030-K08 | WAQF-KHUSUS | لَّٰكِنَّا | 18:38 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P035-K01 | WAQF-KHUSUS | سَلَٰسِلَا | 76:4 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P035-K02 | WAQF-KHUSUS | قَوَارِيرَا | 76:15 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P035-K03 | WAQF-KHUSUS | قَوَارِيرَ | 76:16 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P035-K04 | WAQF-KHUSUS | لَّٰكِنَّا | 18:38 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P035-K05 | WAQF-KHUSUS | سَلَٰسِلَا | 76:4 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P035-K06 | WAQF-KHUSUS | قَوَارِيرَا | 76:15 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P035-K07 | WAQF-KHUSUS | قَوَارِيرَ | 76:16 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P035-K08 | WAQF-KHUSUS | لَّٰكِنَّا | 18:38 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P035-K09 | WAQF-KHUSUS | سَلَٰسِلَا | 76:4 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P038-K06 | WAQF-KHUSUS | سَلَٰسِلَا | 76:4 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P038-K07 | WAQF-KHUSUS | قَوَارِيرَا | 76:15 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P038-K08 | WAQF-KHUSUS | قَوَارِيرَ | 76:16 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P038-K09 | WAQF-KHUSUS | لَّٰكِنَّا | 18:38 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P039-K07 | WAQF-KHUSUS | سَلَٰسِلَا | 76:4 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P039-K08 | WAQF-KHUSUS | لَّٰكِنَّا | 18:38 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P040-K08 | WAQF-KHUSUS | قَوَارِيرَا | 76:15 | LOKASI-TERINDEKS; TASHIH-PENDING |
| P040-K09 | WAQF-KHUSUS | قَوَارِيرَ | 76:16 | LOKASI-TERINDEKS; TASHIH-PENDING |

## Referensi dan batas bukti
1. LPMQ, *Pedoman Pentashihan Mushaf Al-Qur'an* (koleksi resmi): https://pustakalajnah.kemenag.go.id/detail/96 — pedoman untuk proses pentashihan; bukan bukti bahwa 80 transkripsi sudah diperiksa.
2. LPMQ, *Sejarah Penulisan Mushaf Al-Qur'an Standar Indonesia*: https://pustakalajnah.kemenag.go.id/uploads/Sejarah_Mushaf_Standar_Sc.pdf — rujukan umum tentang rasm, tanda waqaf, dan mushaf standar.
3. Matriks internal QJ8 sebagai sumber daftar 80 slot: https://github.com/pesantrenriqa-boop/QURBATA/blob/main/books/jilid-8/QJ8-MATRIKS-KLASIFIKASI-360-KOTAK-2026-10-28.md

Rujukan di atas **belum** merupakan pembuktian per-karakter terhadap 10 lokasi. Bukti tiap kasus perlu cuplikan mushaf edisi spesifik dengan halaman/ayat, metadata edisi, Source-ID, Evidence-ID, reviewer bersanad, hasil talaqqi, dan Decision-ID.

## Gate tindakan
1. Pilih dan catat edisi Mushaf Standar Utsmani (penerbit/tahun/cetakan/versi digital bila digunakan) dan riwayat Hafsh/jalur yang berlaku untuk RIQA.
2. Lakukan pemeriksaan per karakter: rasm, harakat, tanda khusus, kode Unicode, arah tampilan; tandai tiap slot PASS/FAIL setelah pemeriksaan.
3. Validasi bacaan lisan sin/shad, mad, waqaf dan wasal oleh guru/ahli; catat sampel audio dan keputusan terpisah dari teks.
4. Pecahkan rujukan ambigu `P023-K09`; klarifikasi apakah `10:51` dan `10:91` memakai kompetensi mad lazim kalimi mukhaffaf, mad farq sebagai istilah pedagogis, atau lainnya sesuai sumber ajar sahih.
5. Audit benturan halaman P028 dan P038 dengan master Jilid 8, jangan lakukan overwrite tanpa Decision-ID.
6. Semua 80 slot tetap DRAFT/HOLD-CETAK; jangan masukkan ke hitungan teks siap cetak.

## Akumulasi tiga tahap audit
- Saktah: 40 kotak / 4 lokasi.
- Imalah, tashil, isymam: 40 kotak / 3 lokasi.
- Sin/shad, mad farq (label draf), waqaf khusus: 80 kotak / 10 lokasi terindeks.
- **Total ketiga tahap: 160 kotak terindeks, 17 lokasi QS terindeks, 0 slot tuntas tashih mushaf.** Jumlah lokasi adalah unit inventarisasi, bukan seluruhnya hukum yang disahkan.
