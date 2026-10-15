# QURBATA — REVIEW 20 KASUS HADIS PRIORITAS J4–J5 v0.1

**STATUS: QA EDITORIAL, BUKAN TAKHRIJ ATAU PENGESAHAN NASH.** Dua puluh kasus diambil persis dari indeks hadis J4 dan J5, 10 kasus per jilid. Kandidat Hxx berasal dari bank hadis 12 kandidat dan bukan teks cetak yang sudah disahkan.

| Halaman | Fokus resmi staging | Hadis kandidat | Kegiatan lintas domain yang harus dibuktikan | Bloker spesifik |
|---|---|---|---|---|
| J4 P010 | Evaluasi Nun Sakinah I | H08 | uji kompetensi teknis menggunakan bank soal dan rubrik terpisah | bank contoh dan ambang lulus belum disahkan |
| J4 P018 | Hafalan 1 | H05 | setoran, murojaah, dan koreksi adab tanpa mengganti ayat FROZEN | target setoran dan rubrik hafalan belum diverifikasi |
| J4 P020 | Evaluasi Hukum Nun | H05 | uji kompetensi teknis menggunakan bank soal dan rubrik terpisah | bank contoh dan ambang lulus belum disahkan |
| J4 P028 | Bahasa Arab 4 | H07 | dialog guru–santri dengan objek kartu dan jawaban yang dapat diperiksa | dialog generik belum menunjukkan respons dan objek |
| J4 P030 | Evaluasi Mim dan Alif-Lam I | H07 | uji kompetensi teknis menggunakan bank soal dan rubrik terpisah | bank contoh dan ambang lulus belum disahkan |
| J4 P036 | Hafalan 2 | H11 | setoran, murojaah, dan koreksi adab tanpa mengganti ayat FROZEN | target setoran dan rubrik hafalan belum diverifikasi |
| J4 P037 | Simulasi baca ayat pendek | H11 | praktik bacaan nyata, umpan balik dan catatan kesalahan | contoh bacaan dan penilaian belum disahkan |
| J4 P038 | Akhlak/Hadis 4 | H11 | pilih SATU nash spesifik, cocokkan dengan usulan ayat P038 dan takhrij hadis | KONFLIK-KANDIDAT: ayat P038 vs hadis indeks; kurator wajib memilih |
| J4 P039 | Simulasi akhir | H11 | praktik bacaan nyata, umpan balik dan catatan kesalahan | contoh bacaan dan penilaian belum disahkan |
| J4 P040 | Ujian Akhir Jilid 4 | H11 | uji kompetensi teknis menggunakan bank soal dan rubrik terpisah | bank contoh dan ambang lulus belum disahkan |
| J5 P010 | Evaluasi Mad I | H04 | uji kompetensi teknis menggunakan bank soal dan rubrik terpisah | bank contoh dan ambang lulus belum disahkan |
| J5 P018 | Hafalan 1 | H06 | setoran, murojaah, dan koreksi adab tanpa mengganti ayat FROZEN | target setoran dan rubrik hafalan belum diverifikasi |
| J5 P020 | Evaluasi Mad II | H06 | uji kompetensi teknis menggunakan bank soal dan rubrik terpisah | bank contoh dan ambang lulus belum disahkan |
| J5 P028 | Bahasa Arab 5 | H11 | dialog guru–santri dengan objek kartu dan jawaban yang dapat diperiksa | dialog generik belum menunjukkan respons dan objek |
| J5 P030 | Evaluasi Mad Terpadu | H11 | uji kompetensi teknis menggunakan bank soal dan rubrik terpisah | bank contoh dan ambang lulus belum disahkan |
| J5 P035 | Simulasi baca ayat | H12 | praktik bacaan nyata, umpan balik dan catatan kesalahan | contoh bacaan dan penilaian belum disahkan |
| J5 P036 | Hafalan 2 | H12 | setoran, murojaah, dan koreksi adab tanpa mengganti ayat FROZEN | target setoran dan rubrik hafalan belum diverifikasi |
| J5 P038 | Akhlak/Hadis 5 | H12 | pilih SATU nash spesifik, cocokkan dengan usulan ayat P038 dan takhrij hadis | KONFLIK-KANDIDAT: ayat P038 vs hadis indeks; kurator wajib memilih |
| J5 P039 | Simulasi akhir | H12 | praktik bacaan nyata, umpan balik dan catatan kesalahan | contoh bacaan dan penilaian belum disahkan |
| J5 P040 | Ujian Akhir Jilid 5 | H12 | uji kompetensi teknis menggunakan bank soal dan rubrik terpisah | bank contoh dan ambang lulus belum disahkan |

## Temuan yang memerlukan keputusan
1. **J4 P038** sudah memiliki **calon ayat** `فَاسْأَلُوا أَهْلَ الذِّكْرِ إِنْ كُنْتُمْ لَا تَعْلَمُونَ` (An-Nahl 16:43) di kurasi P038, tetapi indeks hadis menunjuk H11 tentang kejujuran. **Keduanya belum final; jangan dicetak bersamaan secara otomatis.** Tema bertanya kepada guru dan kejujuran harus dipilih sesuai kegiatan aktual.
2. **J5 P038** sudah memiliki calon ayat `إِنَّ اللَّهَ مَعَ الصَّابِرِينَ` (Al-Baqarah 2:153), sedangkan indeks hadis menunjuk H12 tentang kelembutan. **Butuh putusan kurator** apakah fokus santri bersabar atau guru membimbing dengan lembut.
3. **J4 P028 dan J5 P028** adalah slot Bahasa Arab. Hadis hanya pendukung adab, **bukan** pengganti materi dialog, kosakata, contoh lisan, dan penilaian BA.
4. **J4/J5 P018 dan P036** adalah slot Hafalan. Target surah/ayat tetap mengikuti crosswalk Tahfidz FROZEN; hadis kandidat tidak menjadi target Tahfidz.
5. **Halaman evaluasi/simulasi** tidak boleh menggunakan keberadaan hadis sebagai bukti tercapainya kompetensi nun/mim/alif-lam atau mad. Dibutuhkan contoh bacaan tervalidasi, pengukuran, dan rubrik.
6. Penempatan H11 pada beberapa halaman J4 dan H12 pada beberapa halaman J5 merupakan **indeks blok**, bukan bukti kesesuaian individual. Audit ini **menolak penerimaan otomatis berdasarkan pengulangan blok**.

## Gate tindak lanjut
- G1: contoh Tartil aktual dan rubrik pada halaman evaluasi/simulasi.
- G2: dialog BA berobjek jelas, jawaban natural dan bisa diuji.
- G3: matan hadis lengkap, kitab/bab/edisi, penilaian riwayat menurut rujukan ahli, terjemah dan keputusan ayat-vs-hadis untuk P038.
- G4: kesesuaian target Tahfidz FROZEN, tashih mushaf dan beban setoran.
- G5: catatan reviewer, keputusan `ACCEPT / REVISE / REJECT`, lalu integrasi.

**Kemajuan terukur:** 20/20 kasus prioritas J4–J5 direview pada tingkat QA editorial; **0/20 disahkan final**. Total kumulatif review editorial kasus prioritas J2–J5: **30/66**.
