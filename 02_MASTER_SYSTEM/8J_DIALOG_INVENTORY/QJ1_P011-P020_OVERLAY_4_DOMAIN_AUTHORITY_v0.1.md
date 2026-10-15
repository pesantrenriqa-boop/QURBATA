# J1 P011–P020 — Overlay empat domain berbasis otoritas v0.1

**DRAF INTEGRASI; BELUM SIAP CETAK.** Tartil mengacu `PAGE_REGISTER_P011-P020_FROZEN-v1.0.md`. Bi'ah/Akhlak **mengacu overlay integrasi FROZEN v1.3** (lebih tinggi dari panel domain pada register lama). Tahfidz **belum dibakukan di berkas ini**, karena staging dan skenario Opsi B memiliki target yang berbeda; harus cocokkan dengan master Tahfidz FROZEN. Semua nash Akhlak perlu klasifikasi dan verifikasi sumber.

| Halaman | Tartil wajib | Bi'ah panel v1.3 | Akhlak panel v1.3 | Tahfidz |
|---|---|---|---|---|
| P011 | كَ لَ | اِقْرَأْ | إِنَّ اللَّهَ مَعَ الصَّابِرِينَ | **PENDING** audit baseline FROZEN |
| P012 | مَ نَ | اِقْرَأْ | إِنَّ اللَّهَ مَعَ الصَّابِرِينَ | **PENDING** audit baseline FROZEN |
| P013 | هَ وَ يَ | اِقْرَأْ | إِنَّ اللَّهَ مَعَ الصَّابِرِينَ | **PENDING** audit baseline FROZEN |
| P014 | بِ تِ ثِ جِ | أَعِدْ | وَلَكَ الْجَنَّةُ | **PENDING** audit baseline FROZEN |
| P015 | حِ خِ دِ ذِ | أَعِدْ | وَلَكَ الْجَنَّةُ | **PENDING** audit baseline FROZEN |
| P016 | رِ زِ سِ شِ | أَعِدْ | وَلَكَ الْجَنَّةُ | **PENDING** audit baseline FROZEN |
| P017 | صِ ضِ طِ ظِ | اِفْتَحِ الْكِتَابَ | وَقُولُوا لِلنَّاسِ حُسْنًا | **PENDING** audit baseline FROZEN |
| P018 | عِ غِ فِ قِ | اِفْتَحِ الْكِتَابَ | وَقُولُوا لِلنَّاسِ حُسْنًا | **PENDING** audit baseline FROZEN |
| P019 | كِ لِ مِ نِ هِ وِ يِ ءِ إِ | اِفْتَحِ الْكِتَابَ | وَقُولُوا لِلنَّاسِ حُسْنًا | **PENDING** audit baseline FROZEN |
| P020 | Checkpoint Fathah + Kasrah; 29 nama huruf | اِقْرَأْ | وَقُلْ رَبِّ زِدْنِي عِلْمًا | **PENDING** audit baseline FROZEN |

## Status panel dan petunjuk guru

- P011–P013: Bi'ah اِقْرَأْ dan Akhlak إِنَّ اللَّهَ مَعَ الصَّابِرِينَ; status INTRODUCE → REPEAT-1 → REPEAT-2. Guru meminta baca كَ/لَ, مَ/نَ, هَ/وَ/يَ; jangan menjadikan kalimat dialog sebagai latihan baca huruf lepas.
- P014–P016: Bi'ah أَعِدْ dan Akhlak وَلَكَ الْجَنَّةُ, status INTRODUCE → REPEAT-2. P014 dua baris penanaman Fathah ke Kasrah, baru latihan campuran.
- P017–P019: Bi'ah اِفْتَحِ الْكِتَابَ dan Akhlak وَقُولُوا لِلنَّاسِ حُسْنًا, status INTRODUCE → REPEAT-2. P019 audit bentuk ءِ / إِ dan هِ.
- P020: Bi'ah اِقْرَأْ (REINFORCE); Akhlak وَقُلْ رَبِّ زِدْنِي عِلْمًا (REINFORCE). Checkpoint membaca Fathah/Kasrah, mengenali 29 nama huruf, dan nama dua harakat; tidak ada Dhammah.

## Konflik Tahfidz yang wajib diputuskan dengan sumber FROZEN

- Staging P011–P020 mencatat Al-Falaq 5; Al-Ikhlas 1,2,3–4; Al-Fatihah 1–6.
- Skenario Opsi B P011–P019 mencatat Al-Falaq 4,5; Al-Ikhlas 1,2,3–4; Al-Fatihah 1–4; P020 review tanpa hafalan baru.
- **Tidak boleh mengambil salah satu jalur berdasarkan dugaan**. Periksa `02_MASTER_SYSTEM/TAHFIDZ/QURBATA-TAHFIDZ-AYAT-DISTRIBUTION-FROZEN-v1.0.md` dan crosswalk sebelum mengisi panel cetak.

## Catatan QA

- Overlay v1.3 **mengungguli panel Bi'ah/Akhlak pada register v1.0**. Hal ini juga berarti overlay J1 P001–P010 yang sebelumnya disusun hanya dari register v1.0 **perlu direvisi** untuk kedua domain; jangan gunakan sebagai dasar panel final.
- Verifikasi klasifikasi nash: ayat/hadis/nasihat. Jangan otomatis menyebut semua nash sebagai hadis.
- Tahfidz wajib teks Arab + arti Indonesia yang benar; Bi'ah/Akhlak memiliki arti panel Indonesia kecil menurut overlay v1.3.
- Grid 8×3, cumulative review, A5 RTL, KFGQPC Uthman Taha, glyph ha dua lubang, tanggal–nilai–TTD, QR RIQA OS harus lolos audit tersendiri.
