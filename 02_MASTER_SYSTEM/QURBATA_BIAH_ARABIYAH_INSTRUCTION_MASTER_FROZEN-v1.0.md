# QURBATA — BI'AH ARABIYAH INSTRUCTION MASTER

Status: **FROZEN v1.0**
Effective: 2026-09-15
Authority: **DOMAIN MASTER — BAHASA ARAB QURBATA TARTIL**
Scope: seluruh Buku QURBATA Tartil, dimulai Jilid 1

## 1. Definisi resmi

Bahasa Arab pada Buku QURBATA Tartil adalah **Bi'ah Arabiyah Instruksional**: bahasa Arab yang benar-benar dipakai guru dan santri untuk menjalankan aktivitas pembelajaran Al-Qur'an di kelas.

Bahasa Arab pada panel ini **BUKAN**:
- daftar mufradat benda yang tidak berfungsi sebagai instruksi kelas;
- pelajaran nahwu/sharaf terpisah;
- materi Bahasa Arab RIQA/Qurani berbasis korpus Al-Qur'an;
- kalimat contoh umum yang tidak dipakai dalam interaksi belajar;
- terjemahan bebas yang hanya menjadi hiasan halaman.

Fungsi utamanya adalah membentuk **bi'ah 'Arabiyah di dalam ekosistem pembelajaran Al-Qur'an**.

## 2. Prinsip inti

1. **Instruksional** — ungkapan harus dapat diucapkan guru/santri ketika belajar.
2. **Aplikatif** — setiap ungkapan harus langsung dipraktikkan, bukan sekadar dibaca.
3. **Berulang dan kumulatif** — ungkapan lama terus dipakai setelah ungkapan baru masuk.
4. **Kontekstual Al-Qur'an** — prioritas pada aktivitas membuka mushaf/buku, membaca, mendengar, mengulang, menunjuk, memperhatikan, berhenti, melanjutkan, menjawab, dan mengoreksi bacaan.
5. **Ringkas** — panel tidak mengambil dominasi area Tartil.
6. **Tanpa beban teori** — tidak ada uraian nahwu/sharaf pada panel Bi'ah.
7. **Lisan dahulu** — tujuan utamanya membiasakan komunikasi Arab sederhana dalam proses belajar.

## 3. Jenis bahasa yang diperbolehkan

### A. Instruksi guru
Contoh inti:
- اِقْرَأْ — Bacalah.
- أَعِدْ — Ulangi.
- اِسْمَعْ — Dengarkan.
- اُنْظُرْ — Lihat/perhatikan.
- اِفْتَحِ الْكِتَابَ / اِفْتَحِ الْمُصْحَفَ — Bukalah buku/mushaf.
- أَغْلِقِ الْكِتَابَ / أَغْلِقِ الْمُصْحَفَ — Tutuplah buku/mushaf.
- اِقْرَأْ مَرَّةً أُخْرَى — Bacalah sekali lagi.
- قِفْ — Berhenti.
- وَاصِلْ — Lanjutkan.
- أَجِبْ — Jawablah.
- اِنْتَبِهْ — Perhatikan.

### B. Respons santri
- نَعَمْ — Ya.
- لَا — Tidak.
- حَاضِرٌ / حَاضِرَةٌ — Siap/hadir, sesuai konteks.
- فَهِمْتُ — Saya paham.
- لَمْ أَفْهَمْ — Saya belum paham.

### C. Interaksi pembelajaran
- هَلْ فَهِمْتَ؟ / هَلْ فَهِمْتِ؟ — Apakah kamu paham?
- مَا هَذَا؟ — Apa ini?
- أَيْنَ ...؟ — Di mana ...?
- أَحْسَنْتَ / أَحْسَنْتِ — Bagus.
- صَحِيحٌ — Benar.
- خَطَأٌ — Salah.

Kalimat nominal seperti `هَذَا كِتَابٌ` hanya boleh muncul jika benar-benar menjadi bagian dialog/instruksi kelas yang sedang dilatih; **tidak boleh menggantikan jalur utama bahasa instruksional**.

## 4. Tangga Bi'ah Arabiyah

### Fase 1 — rutinitas dasar
Salam, baca, ulangi, dengarkan, lihat/perhatikan, buka, tutup.

### Fase 2 — kontrol aktivitas belajar
Sekali lagi, berhenti, lanjutkan, tunjuk/perhatikan, jawab.

### Fase 3 — respons santri
Ya, tidak, saya paham, saya belum paham, siap.

### Fase 4 — interaksi dua arah
Apakah kamu paham?, apa ini?, di mana...?, benar, salah, bagus.

### Fase 5 — kombinasi instruksi
Dua atau lebih ungkapan yang telah dikuasai dipakai dalam satu rangkaian kelas, misalnya: buka buku → dengarkan → baca → ulangi.

## 5. Aturan distribusi halaman

- Satu halaman memperkenalkan maksimal **1 ungkapan baru** pada tahap awal.
- Ungkapan baru harus dipakai kembali pada halaman/pertemuan berikutnya.
- Setiap 5–10 pertemuan dilakukan penguatan tanpa harus menambah ungkapan baru.
- Setelah sebuah ungkapan diperkenalkan, guru dianjurkan menggunakan ungkapan itu sebagai bahasa kelas nyata.
- Bahasa Indonesia pada panel berfungsi sebagai bantuan makna, bukan materi utama.
- Tidak wajib ada ungkapan baru pada halaman evaluasi/checkpoint; halaman tersebut dapat mengulang ungkapan yang sudah dipelajari.

## 6. Format isi panel

Panel Bi'ah Arabiyah minimal memuat:
1. **Ungkapan Arab utama** — paling menonjol.
2. **Makna Indonesia singkat**.
3. **Fungsi/praktik** yang sangat pendek, misalnya `Guru memberi instruksi; santri langsung membaca.`

Jika ruang sangat terbatas, unsur nomor 3 boleh diwujudkan melalui ikon/label aktivitas pada layout, tetapi fungsi instruksionalnya harus tetap jelas dalam data/master.

## 7. Hubungan dengan Tartil

Bi'ah tidak mengikuti whitelist huruf Tartil untuk teks instruksinya. Ungkapan Bi'ah adalah **bahasa komunikasi kelas**, bukan objek latihan decoding Tartil. Karena itu teks seperti `اِقْرَأْ` boleh tampil meskipun memuat struktur yang belum menjadi kompetensi Tartil, selama panelnya secara visual terpisah dari grid latihan Tartil.

Generator dilarang mencampurkan teks Bi'ah ke dalam bank latihan Tartil.

## 8. Gate audit Bi'ah

Sebelum halaman/PDF diberi status FINAL:
- setiap item Bahasa Arab harus diklasifikasikan sebagai instruksi, respons, atau interaksi kelas;
- item yang hanya berupa mufradat/kalimat nominal umum harus diganti atau diberi konteks instruksional yang nyata;
- urutan harus mengikuti tangga Bi'ah dan bersifat kumulatif;
- tidak boleh berubah menjadi pelajaran nahwu/sharaf;
- tidak boleh tercampur ke grid Tartil;
- istilah panel resmi: **Bi'ah Arabiyah**.

## 9. Governance

Dokumen ini mengendalikan seluruh data Bi'ah Arabiyah QURBATA Tartil. Page register, generator, PDF, RIQA OS, audio, dan materi guru harus tunduk padanya.

Jika ada perubahan konsep Bahasa Arab, revisi dokumen ini terlebih dahulu, naikkan versi, tulis changelog, lalu turunkan ke page register. **Dilarang memperbaiki Bahasa Arab hanya pada layout/PDF tanpa memperbaiki master.**
