# Audit frasa Qur'ani dua kata — Jilid 3 (Juz 1–29)

Tanggal: 18 Oktober 2026. Status: audit awal; **tidak ada frasa yang disahkan untuk cetak**.

## Sumber dan batas
- Sumber kurikulum: `curriculum/DEC-CUR-018-Urutan-Sukun-Berdasarkan-Huruf.md`.
- Mesin korpus tersedia: `quran_corpus_competency_index_v0_1.py` dan `quran_corpus_select_diverse_v0_1.py`. Keduanya memerlukan berkas TSV mushaf yang diotorisasi; repo yang diperiksa tidak memuat hasil indeks lengkap 114 surah yang dapat dipakai untuk mengklaim audit komprehensif.
- Kandidat harus dua token berurutan dalam ayat yang sama, surah di Juz 1–29, dan harus dicek bacaan sambung, bukan sekadar bentuk tulisan.
- Dilarang: نْ, sukun selain huruf yang sudah diajarkan, qalqalah, tasydid, mad, dan hukum pertemuan nun/mim/tanwin yang belum diajarkan.

## Kandidat nyata, bukan materi disahkan
| Surah:ayat | Dua kata berurutan | Pemeriksaan | Keputusan |
|---|---|---|---|
| 2:6 | أَمْ لَمْ | Dua مْ, tidak ada نْ, tasydid, atau mad dalam dua kata; namun pertemuan مْ + ل membutuhkan penilaian bacaan mim sukun (izhar syafawi). | TAHAN: tidak memenuhi larangan mutlak atas hukum tajwid lain |
| 23:69 | أَمْ لَمْ | Sama seperti 2:6; bukan bentuk unik baru. | TAHAN |
| 26:136 | أَمْ لَمْ | Sama; duplikasi frasa. | TAHAN |
| 36:10 | أَمْ لَمْ | Sama; duplikasi frasa. | TAHAN |
| 23:69 | أَمْ يَقُولُونَ | Memuat mad pada يَقُولُونَ. | GUGUR |
| 23:69 | لَمْ يَعْرِفُوا | Memuat عْ dan رْ yang belum masuk P001; mad pada akhir kata kedua. | GUGUR P001 |
| 2:6 | لَمْ تُنْذِرْهُمْ | Memuat نْ, رْ selain مْ. | GUGUR P001 |

## Hasil sementara
Tidak boleh menyimpulkan tersedia 24 contoh lolos per halaman sebelum tersedia korpus mushaf lengkap, penyaringan tanda dan tajwid, serta tashih ahli. Frasa `أَمْ لَمْ` ditemukan di beberapa ayat tetapi bukan empat frasa unik. **Jumlah disahkan: 0.**

## Tindak lanjut teknis
1. Pasok TSV token mushaf Utsmani berlisensi dengan kolom `surah,ayah,token_index,uthmani`.
2. Buat semua pasangan token bertetangga dalam satu ayat; batasi Juz 1–29 memakai batas juz resmi, bukan asumsi nomor surah.
3. Audit diakritik semua huruf dan kategori hukum bacaan sambung. Perlakukan indikasi tidak pasti sebagai tahan, bukan lolos.
4. Peta kelulusan per halaman sesuai kompetensi kumulatif dan simpan surah:ayat serta posisi token.
5. Tashih mushaf, tajwid, dan kelayakan pedagogis sebelum pemakaian.
