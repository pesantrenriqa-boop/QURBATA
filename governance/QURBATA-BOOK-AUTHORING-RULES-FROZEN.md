# QURBATA — ATURAN BAKU PENYUSUNAN BUKU (FROZEN)

**Status:** FROZEN / NORMATIF  
**Kedudukan:** Guardrail wajib untuk seluruh penyusunan, generator, audit, layout, dan build buku QURBATA.  
**Prinsip:** Repository adalah source of truth. Dilarang menyusun ulang kurikulum dari ingatan atau improvisasi jika keputusan sudah tersedia di repository.

## 1. Hirarki sumber
1. Dokumen governance/FROZEN/decision register.
2. Curriculum master, competency framework, progression, matriks jilid.
3. Source/regenerated halaman yang telah disahkan.
4. Data produksi dan generator.
Jika terjadi konflik, data produksi/generator wajib tunduk pada sumber normatif di atas. Jangan mengubah aturan frozen hanya agar build lolos.

## 2. Tangga kompetensi
- Kompetensi wajib diajarkan bertahap dari prasyarat ke kompetensi baru.
- **Competency leakage = 0:** huruf, bentuk sambung, harakat, tanda baca, tajwid, panjang bacaan, atau struktur yang belum eligible DILARANG muncul.
- Kompetensi baru harus dominan pada halaman akuisisi, tetapi murojaah kompetensi eligible wajib tersebar merata.
- Murojaah tidak boleh hanya mengambil materi terdekat; gunakan prinsip kumulatif/spacing yang ditetapkan repository (termasuk N+1/N+2/N+4/N+8 bila berlaku).
- Jangan regresi ke tahap lebih rendah jika progression jilid telah menetapkan bentuk minimal yang lebih tinggi.
- Tangga mikro halaman harus mengikuti dokumen jilid: jumlah huruf/rangkaian, posisi sambung awal–tengah–akhir, dan kenaikan 3→4 huruf hanya saat legal.
- Untuk Jilid 2, ikuti QJ2 MASTER/DEC-CUR/MAT yang berlaku; sukun dan tasydid bukan kompetensi Jilid 2 kecuali keputusan resmi repository menyatakan lain.

## 3. Blok PENANAMAN KOMPETENSI BARU — WAJIB
Setiap halaman yang memperkenalkan kompetensi baru wajib memiliki blok visual eksplisit **sebelum grid latihan**.
- Menampilkan bentuk/bunyi lama yang telah dikenal → bentuk/bunyi baru.
- Untuk sambung: tampilkan perubahan yang relevan (tunggal/awal/tengah/akhir) sesuai kompetensi halaman.
- Ukuran huruf sekurang-kurangnya setara huruf latihan; bukan keterangan kecil.
- Berfungsi sebagai bahan talqin/penjelasan guru dan sumber konten penjelasan RIQA OS.
- Pada halaman materi baru, jumlah baris latihan boleh dikurangi agar blok ini mendapat ruang layak.
- Jangan membuat blok materi baru yang kedua sisinya sama; harus memperlihatkan transformasi kompetensi nyata dan arah baca RTL yang benar.

## 4. Latihan Tartil
- Contoh diutamakan **kata Arab bermakna**: Qurani → hadis → mufradat Arab yang sah → drill terkendali yang mendekati pola/makna jika keterbatasan tangga belum memungkinkan kata utuh.
- Kata bermakna tidak boleh menjadi alasan memasukkan kompetensi masa depan.
- Harakat harus sesuai bentuk/kata yang sah; dilarang merangkai harakat acak hanya demi variasi.
- Jangan membuat rangkaian semu yang tidak berfungsi pedagogis.
- Setiap contoh harus memiliki fungsi: **F Fokus / M Murojaah / T Transfer / E Evaluasi**.
- Hindari halaman/baris yang identik dan pengulangan contoh tanpa alasan pedagogis.
- Frekuensi kompetensi baru harus cukup terlihat; jangan sampai materi baru hanya muncul satu contoh sementara murojaah mendominasi.
- Murojaah harus merata dan acak-terkendali sesuai kompetensi yang sudah eligible.

## 5. Bentuk huruf dan font
- Teks Arab buku menggunakan jalur font Utsmani resmi proyek (KFGQPC/KFGQPC Uthman Taha sesuai asset repository).
- Dilarang ada glyph/font Arab non-Utsmani yang menyusup di header atau area materi.
- Bentuk **ه** harus mengikuti bentuk Utsmani yang disahkan proyek; jangan memakai bentuk visual “satu lubang” yang pernah ditolak.
- Tatweel/kashida tidak boleh dipakai untuk memalsukan jumlah huruf atau kompetensi.
- Header, judul Arab, dan blok kompetensi wajib diaudit font/glyph-nya.

## 6. Integrasi Tahfidz — Bahasa Arab — NIDHOM
- Ketiganya progresif dan terhubung dengan halaman/kompetensi Tartil.
- **Tidak boleh mengulang target yang sudah selesai** tanpa label murojaah yang disengaja.
- Tahfidz: target baru jelas, murojaah terpisah dan kumulatif.
- Bahasa Arab: bukan sekadar nahwu; diarahkan pada bi'ah 'Arabiyah dan penggunaan ungkapan/mufradat yang relevan dengan ekosistem belajar.
- NIDHOM: pembelajaran akhlak melalui potongan hadis/nasihat terstruktur dan aplikatif; bukan nazam/matan nahwu.
- Sebelum finalisasi jilid, audit duplikasi lintas halaman untuk Tahfidz, Bahasa Arab, dan NIDHOM.

## 7. Layout buku
- Ikuti **QURBATA-BOOK-BLUEPRINT-v1.0-FROZEN** dan keputusan layout repository.
- Area latihan Tartil tetap menjadi area dominan.
- Blok integrasi bawah dibuat ringkas agar tidak mengambil dominasi latihan.
- QR/ID kompetensi menghubungkan halaman buku dengan RIQA OS.
- Jangan mengubah ukuran, grid, tipografi, header/footer, atau anatomi halaman yang sudah frozen tanpa decision baru.

## 8. RIQA OS
Setiap kompetensi buku harus dapat dipetakan ke RIQA OS untuk:
- penjelasan/talqin materi baru;
- contoh audio;
- latihan/ujian;
- rekaman peserta/assessor bila diperlukan;
- QR resolver/competency ID.
Buku dan RIQA OS adalah satu ekosistem, bukan dua kurikulum terpisah.

## 9. Gate sebelum PDF
Setiap halaman wajib lolos:
1. source-of-truth gate;
2. prerequisite/eligibility gate;
3. competency leakage = 0;
4. blok penanaman materi baru (jika acquisition page);
5. meaningful-word/controlled-drill gate;
6. harakat & bentuk huruf gate;
7. F/M/T/E + distribusi murojaah gate;
8. duplikasi gate;
9. integrasi Tahfidz–BA–NIDHOM gate;
10. Utsmani font/glyph gate;
11. layout/FROZEN blueprint gate;
12. RIQA OS mapping gate.
Build SUCCESS secara teknis **tidak berarti** halaman benar secara akademik.

## 10. Prosedur kerja wajib
- Sebelum mengedit jilid, baca kembali dokumen FROZEN + curriculum controlling documents jilid tersebut.
- Jangan menciptakan curriculum map baru jika repository sudah memiliki keputusan.
- Kerjakan/audit halaman secara terkontrol; perubahan massal hanya setelah pola halaman lolos audit.
- Bila user membekukan/menyetujui halaman, jadikan baseline dan jangan diubah diam-diam.
- Setiap revisi harus menyebut sumber aturan yang dipakai dan tidak boleh menurunkan keputusan lama.
- PDF hanya dikirim sebagai “hasil benar” setelah gate akademik dan visual lolos, bukan hanya karena CI SUCCESS.

## 11. Larangan keras
- Mengandalkan ingatan percakapan sebagai pengganti repository.
- Menyisipkan kompetensi masa depan.
- Mengubah progression agar cocok dengan contoh yang telanjur dibuat.
- Memaksakan kata bermakna dengan mad/tasydid/sukun/tanwin/bentuk sambung yang belum legal.
- Mengulang Tahfidz/BA/NIDHOM tanpa tujuan murojaah eksplisit.
- Mengganti font Utsmani dengan font Arab umum.
- Mengirim ulang PDF lama/salah sebagai hasil revisi baru.

---
Dokumen ini merangkum koreksi pengguna dan keputusan repository yang harus diperlakukan sebagai guardrail permanen. Jika ada aturan jilid yang lebih spesifik dan telah FROZEN, aturan spesifik tersebut mengalahkan aturan umum ini.
