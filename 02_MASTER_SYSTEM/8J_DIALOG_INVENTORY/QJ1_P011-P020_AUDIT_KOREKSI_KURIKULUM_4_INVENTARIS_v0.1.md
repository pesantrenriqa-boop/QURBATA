# Audit dan overlay kurikulum J1 P011–P020 — empat inventaris v0.1

**STATUS: AUDIT TERKENDALI / BUKAN FINAL.** Register otoritatif: `03_BOOKS/JILID-1/PAGE_REGISTER_P011-P020_FROZEN-v1.0.md`. Matriks staging dan skenario Opsi B hanya bahan historis; jangan menimpa master. Fokus audit: koreksi pergeseran Kasrah dan checkpoint, pemetaan Tahfidz baseline staging, serta gate sumber Bi'ah/Akhlak.

| Halaman | Tartil wajib sesuai register | Tahfidz tercatat pada staging (perlu crosswalk) |
|---|---|---|
| P011 | كَ لَ | Al-Falaq 5 |
| P012 | مَ نَ | Al-Ikhlas 1 |
| P013 | هَ وَ يَ | Al-Ikhlas 2 |
| P014 | بِ تِ ثِ جِ; penanaman Kasrah | Al-Ikhlas 3–4 |
| P015 | حِ خِ دِ ذِ | Al-Fatihah 1 |
| P016 | رِ زِ سِ شِ | Al-Fatihah 2 |
| P017 | صِ ضِ طِ ظِ | Al-Fatihah 3 |
| P018 | عِ غِ فِ قِ | Al-Fatihah 4 |
| P019 | كِ لِ مِ نِ هِ وِ يِ ءِ إِ | Al-Fatihah 5 |
| P020 | Checkpoint: Fathah + Kasrah, 29 nama huruf, nama 2 harakat | Al-Fatihah 6 |

## Putusan penting

- **P014**: staging historis menyebut integrasi Fathah, tetapi register FROZEN menetapkan **penanaman Kasrah** dengan perbandingan بَ→بِ, تَ→تِ, ثَ→ثِ, جَ→جِ. Dua baris pertama wajib penanaman; jangan memindahkan Kasrah ke P016.
- **P015–P019**: lanjutkan Kasrah menurut whitelist per halaman, tetap mereview Fathah dan Kasrah sebelumnya secara kumulatif. P019 membutuhkan audit tipografi khusus untuk ءِ / إِ.
- **P020**: bukan sekadar evaluasi biasa; wajib checkpoint 29 nama huruf tanpa harakat, nama Fathah/Kasrah, dan baca Fathah+Kasrah; **tanpa Dhammah**.
- **P011–P013**: penyelesaian Fathah كَ لَ, مَ نَ, هَ وَ يَ; وَ pendek bukan mad.
- **Tahfidz**: nilai tabel disalin dari staging, **belum dibandingkan teks ayat terhadap mushaf dan crosswalk FROZEN**; jangan menganggap lolos audit hanya karena tercatat.
- **Bi'ah Arabiyah**: register P011–P020 yang diperiksa tidak memuat daftar kalimat panel resmi per halaman. Staging menyebut اِقْرَأْ (P011–13), أَعِدْ (P014–16), اِفْتَحِ الْكِتَابَ (P017–19), اِقْرَأْ (P020), tetapi statusnya historis dan **tidak disahkan sebagai panel FROZEN**. Wajib cek overlay integrasi v1.3.
- **Akhlak**: staging menyebut kutipan berulang; sumber dan kategori (ayat/hadis/nasihat) **belum diverifikasi**. Jangan memaksakan takhrij atau mengganti nash tanpa dasar.

## Gate pekerjaan

1. Periksa `PAGE_REGISTER_P001-P040_INTEGRATION_FROZEN-v1.3.md` untuk panel Bi'ah/Akhlak per halaman, kemudian terbitkan overlay koreksi terpisah.
2. Susun dan audit grid nyata P011–P019 8 baris × 3 kelompok, baru sekitar 60% dan review kumulatif sekitar 40%; P020 evaluasi representatif, tidak tunduk rasio 60/40.
3. Validasi crosswalk Tahfidz, jenis nash Akhlak, bahasa Arab lisan, dan kecocokan latihan Tartil.
4. QA visual A5 RTL KFGQPC Uthman Taha, titik/harakat, ruang tanggal–nilai–TTD dan QR RIQA OS.

**Belum FROZEN dan belum siap cetak.**
