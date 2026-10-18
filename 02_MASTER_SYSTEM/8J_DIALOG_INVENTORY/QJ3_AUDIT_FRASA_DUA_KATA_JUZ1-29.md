# Audit frasa Qur'ani dua kata — Jilid 3 (Juz 1–29)

Tanggal: 18 Oktober 2026. Status: audit awal; **tidak ada frasa yang disahkan untuk cetak**.

## Sumber dan batas
- Sumber kurikulum: `curriculum/DEC-CUR-018-Urutan-Sukun-Berdasarkan-Huruf.md`.
- Mesin korpus tersedia: `quran_corpus_competency_index_v0_1.py` dan `quran_corpus_select_diverse_v0_1.py`. Keduanya memerlukan berkas TSV mushaf yang diotorisasi; repo yang diperiksa tidak memuat hasil indeks lengkap 114 surah yang dapat dipakai untuk mengklaim audit komprehensif.
- Kandidat harus dua token berurutan dalam ayat yang sama, surah di Juz 1–29, dan harus dicek bacaan sambung, bukan sekadar bentuk tulisan.
- Dilarang: نْ, sukun selain huruf yang sudah diajarkan, qalqalah, tasydid, mad, dan hukum pertemuan nun/mim/tanwin yang belum diajarkan.

## Inventaris latihan yang lolos

**Belum ada entri yang disahkan.** Hanya frasa yang lulus semua larangan (termasuk tanpa mad pada kedua kata) boleh dimasukkan ke bagian ini.

## Log penolakan (bukan contoh latihan)

| Frasa | Alasan ditolak |
|---|---|
| أَمْ لَمْ (2:6; 23:69; 26:136; 36:10) | Memerlukan pemeriksaan hukum mim sukun pada pertemuan dua kata; belum dapat disahkan dengan kriteria ketat |
| أَمْ يَقُولُونَ | Mengandung mad — dilarang |
| لَمْ يَعْرِفُوا | Mengandung mad dan sukun lain yang belum diajarkan pada P001 — dilarang |
| لَمْ تُنْذِرْهُمْ | Mengandung نْ dan رْ — dilarang untuk P001 |

**Aturan keras:** setiap frasa yang mengandung mad, tasydid, nun sukun, qalqalah, atau sukun di luar kompetensi halaman harus langsung masuk log penolakan; jangan tampilkan sebagai kandidat latihan.

## Hasil sementara
Tidak boleh menyimpulkan tersedia 24 contoh lolos per halaman sebelum tersedia korpus mushaf lengkap, penyaringan tanda dan tajwid, serta tashih ahli. Frasa `أَمْ لَمْ` ditemukan di beberapa ayat tetapi bukan empat frasa unik. **Jumlah disahkan: 0.**

## Tindak lanjut teknis
1. Pasok TSV token mushaf Utsmani berlisensi dengan kolom `surah,ayah,token_index,uthmani`.
2. Buat semua pasangan token bertetangga dalam satu ayat; batasi Juz 1–29 memakai batas juz resmi, bukan asumsi nomor surah.
3. Audit diakritik semua huruf dan kategori hukum bacaan sambung. Perlakukan indikasi tidak pasti sebagai tahan, bukan lolos.
4. Peta kelulusan per halaman sesuai kompetensi kumulatif dan simpan surah:ayat serta posisi token.
5. Tashih mushaf, tajwid, dan kelayakan pedagogis sebelum pemakaian.
