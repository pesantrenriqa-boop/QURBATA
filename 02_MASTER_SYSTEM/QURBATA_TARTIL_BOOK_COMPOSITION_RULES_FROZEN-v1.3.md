# QURBATA TARTIL — ATURAN PENYUSUNAN BUKU

Status: **FROZEN v1.3**
Effective: 2026-09-17
Authority: **BOOK COMPOSITION MASTER**
Scope: penyusunan isi, repetisi domain, tipografi latihan, dan prinsip layout seluruh Buku QURBATA Tartil
Supersedes: `QURBATA_TARTIL_BOOK_COMPOSITION_RULES_FROZEN-v1.2.md`

## 1. Urutan kerja wajib
1. Master kurikulum.
2. Master masing-masing domain: Tartil, Bi'ah Arabiyah, Tahfidz, Akhlak.
3. Page register/lesson register.
4. Audit integrasi isi.
5. Freeze konten.
6. Baru generator/layout.
7. Audit visual.
8. FINAL.

**Layout tidak boleh dipakai untuk menentukan atau memperbaiki kurikulum.**

## 2. Empat domain QURBATA
- **Quran/Tartil** — kompetensi membaca Al-Qur'an; domain utama.
- **Bi'ah Arabiyah** — bahasa Arab instruksional/komunikatif yang membangun bi'ah selama pembelajaran Al-Qur'an.
- **Tahfidz** — hafalan Al-Qur'an bertahap dan berurutan.
- **Akhlak** — pembiasaan adab melalui ayat, hadis, atau nasihat ringkas.

Keempatnya terintegrasi dalam satu pertemuan tetapi tidak boleh saling mencampur fungsi.

## 3. Fungsi per halaman/pertemuan
Setiap halaman harus jelas sebelum layout:
- Tartil: kompetensi membaca yang ditanam/dilatih.
- Bi'ah: ungkapan Arab yang dipakai/dikuasai.
- Tahfidz: target hafalan/review.
- Akhlak: adab/nash yang dibiasakan.

## 4. Aturan integrasi dan repetisi pedagogis
- Tartil mengendalikan urutan kompetensi membaca dan murojaah kumulatif.
- Tahfidz mengikuti urutan hafalan master, bukan dipilih hanya karena cocok dengan huruf Tartil.
- **Bi'ah Arabiyah dan Akhlak TIDAK wajib berganti materi pada setiap halaman.**
- Satu materi/ungkapan Bi'ah dapat dipertahankan dan diulang selama **1–3 pertemuan berturut-turut** sesuai kebutuhan pembiasaan, penguasaan lisan, dan konteks kelas.
- Satu nash/tema Akhlak dapat dipertahankan dan diulang selama **1–3 pertemuan berturut-turut** agar menjadi pembiasaan, bukan sekadar informasi baru.
- Materi baru diperkenalkan setelah materi sebelumnya memperoleh pengulangan yang memadai; variasi praktik boleh berubah tanpa mengganti inti materi.
- Pengulangan yang direncanakan harus tercatat pada page register sebagai `INTRODUCE`, `REPEAT-1`, `REPEAT-2`, atau `REINFORCE`, sehingga tidak dianggap duplikasi tidak sengaja.
- Tidak boleh mengejar banyaknya materi dengan mengganti Bi'ah/Akhlak setiap halaman apabila hal itu mengurangi penguasaan dan pembiasaan.

**Prinsip:** sedikit materi yang dipakai berulang dan dikuasai lebih utama daripada banyak materi yang hanya muncul sekali.

## 5. Aturan Bi'ah Arabiyah
Wajib mengikuti master Bi'ah yang berlaku. Khusus buku Tartil:
- jalur utama adalah bahasa Arab yang relevan dengan ekosistem belajar Al-Qur'an;
- ungkapan bersifat kumulatif dan dipraktikkan;
- tidak ada bab nahwu/sharaf terpisah di panel Bi'ah;
- satu ungkapan dapat diulang 1–3 pertemuan sebelum berganti;
- page register wajib membedakan materi baru dan pengulangan.

## 6. Aturan teks Arab dan teks makna pada panel integrasi
Untuk panel **Tahfidz – Bahasa Arab/Bi'ah Arabiyah – Akhlak**:
1. Baris Arab menampilkan **materi/nash/ungkapan utama**.
2. Baris kecil tepat di bawah teks Arab menampilkan **ARTI/MAKNA bahasa Indonesia dari teks Arab tersebut**, bukan instruksi aktivitas.
3. Contoh: teks `اِقْرَأْ` → bawahnya `Bacalah`; teks hadis/nasihat → bawahnya terjemah ringkas dan tepat; ayat Tahfidz → bawahnya arti ayat/bagian ayat yang tampil.
4. Instruksi praktik, bila diperlukan, ditempatkan terpisah pada metadata guru/RIQA OS/page register dan **tidak menggantikan kolom arti**.
5. Terjemah dibuat ringkas, komunikatif, setia pada makna, dan cukup untuk menambah wawasan santri.
6. Setiap panel harus lolos audit pasangan `TEKS ARAB ↔ ARTI INDONESIA` sebelum produksi.

## 7. Aturan bentuk huruf Arab — Ha tunggal
- Seluruh **huruf ه tunggal/detached** pada materi Tartil wajib menggunakan bentuk **ha dua lubang** sesuai standar visual QURBATA/KFGQPC Uthman Taha.
- Bentuk ha tunggal satu lubang yang muncul akibat glyph/substitusi/karakter yang salah **dilarang**.
- Generator harus menggunakan karakter/sequence Unicode dan font yang menghasilkan bentuk dua lubang yang disetujui pada posisi tunggal.
- Audit glyph wajib memeriksa seluruh kemunculan ha tunggal pada judul, penanaman, latihan, evaluasi, dan checkpoint.
- Aturan ini tidak boleh mengubah bentuk kontekstual huruf ketika kelak kompetensi huruf sambung memang diperkenalkan pada jilid yang sesuai.

## 8. Aturan ukuran contoh dan latihan Tartil
- Teks Arab pada **contoh/penanaman kompetensi baru** harus tampak jelas dan lebih besar daripada teks penjelas biasa.
- Teks latihan membaca tetap menjadi elemen visual dominan.
- Ukuran diperbesar **secara proporsional sampai batas aman**, dengan syarat tidak menyentuh garis kotak, tidak memotong harakat, dan tidak bertabrakan dengan sel tetangga.
- Harus tersedia clear space visual di atas/bawah glyph dan harakat; ukuran maksimum ditentukan oleh bounding box aktual font KFGQPC Uthman Taha, bukan hanya angka pt.
- Dilarang mengecilkan huruf latihan hanya untuk memberi ruang pada dekorasi/padding yang tidak esensial.
- Audit visual wajib memeriksa clipping harakat, tabrakan garis, baseline, dan keterbacaan pada ukuran cetak A5.

## 9. Aturan page register
Setiap entry minimal memuat:
- ID halaman/pertemuan;
- kompetensi Tartil baru/aktif + pool murojaah;
- jenis halaman;
- Bi'ah: teks Arab + arti + status repetisi (`INTRODUCE/REPEAT-1/REPEAT-2/REINFORCE`);
- Tahfidz: teks/target + arti + status review;
- Akhlak: nash + arti + status repetisi;
- catatan glyph/premature competency bila relevan.

## 10. Audit isi sebelum layout
### Tartil
Tangga benar; materi baru/review benar; tidak prematur; murojaah kumulatif; checkpoint benar; ha tunggal dua lubang.
### Bi'ah
Relevan dengan ekosistem; kumulatif; dapat dipraktikkan; repetisi 1–3 pertemuan terencana; teks Arab dan arti tepat.
### Tahfidz
Urutan benar; tidak lompat tanpa keputusan master; teks dan arti tepat; review jelas.
### Akhlak
Nash/tema benar; pembiasaan jelas; repetisi 1–3 pertemuan terencana; teks dan arti tepat.

**Semua audit isi harus lulus sebelum editing layout.**

## 11. Zona kerja guru — Tanggal, Nilai, TTD
1. `Tanggal`, `Nilai`, `TTD` berada pada **baseline vertikal yang sama** di bagian bawah zona kerja guru.
2. Tidak boleh ada satu label—termasuk `TTD`—yang tertinggal lebih tinggi daripada dua label lainnya.
3. Ruang menulis berada **DI ATAS** ketiga label, bukan di bawahnya.
4. Area TTD di atas label minimum **12 mm**, target nyaman 14–18 mm bila memungkinkan.
5. Area Tanggal dan Nilai boleh lebih kompak tetapi tetap mempunyai ruang tulis nyata di atas label.
6. Ruang kosong besar di bawah label dilarang; bawah label hanya untuk baseline/identitas/footer/safe area yang proporsional.
7. QR RIQA OS tidak boleh memaksa label TTD naik; QR ditempatkan pada kolom tersendiri dan tidak mengubah baseline ketiga label.
8. Generator wajib menerapkan satu struktur/grid yang sama untuk ketiga field; pengecualian CSS `last-child` yang mengubah posisi vertikal TTD **dilarang**.
9. Audit visual wajib membandingkan posisi Tanggal–Nilai–TTD pada halaman awal, tengah, checkpoint, dan akhir.

## 12. Invariant proporsi halaman
- Satu pertemuan tetap satu halaman.
- Tartil tetap dominan.
- Jumlah/urutan latihan tidak dikurangi karena perubahan footer.
- Penyesuaian dilakukan dengan redistribusi ruang di ukuran halaman tetap, bukan overflow.
- PDF harus tetap sesuai jumlah halaman page register.

## 13. Gate FINAL
**CURRICULUM PASS → DOMAIN PASS → PAGE REGISTER PASS → CONTENT FREEZE → GLYPH PASS → LAYOUT PASS → PDF PASS.**

PDF/layout v1.2 dan sebelumnya kembali berstatus **AUDIT/OBSOLETE** sampai seluruh aturan v1.3 diturunkan ke register, generator, dan build terbaru.

## 14. Changelog
### v1.3 — 2026-09-17
- Menetapkan Tanggal–Nilai–TTD wajib satu baseline; TTD tidak boleh naik sendiri.
- Menetapkan ruang tulis tetap di atas label.
- Membekukan aturan **ha tunggal dua lubang** dan audit glyph.
- Menetapkan contoh/latihan Arab diperbesar proporsional tanpa clipping/tabrakan garis.
- Membekukan repetisi pedagogis Bi'ah dan Akhlak selama **1–3 pertemuan** sebelum perlu berganti.
- Mengubah baris bawah panel Tahfidz/Bi'ah/Akhlak menjadi **arti/terjemah materi Arab**, bukan instruksi.
- Menambah status repetisi pada page register dan gate `GLYPH PASS`.

### v1.2 — 2026-09-17
- Spasi tulis berada di atas label Tanggal–Nilai–TTD.
- Invariant proporsi satu pertemuan/satu halaman.

### v1.1 — 2026-09-17
- Zona penilaian sebagai ruang kerja guru dan area TTD minimum.

### v1.0 — 2026-09-15
- Freeze awal aturan penyusunan Buku QURBATA Tartil.
