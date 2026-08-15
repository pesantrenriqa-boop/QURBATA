# QURBATA TAHFIDZ SYSTEM — BASELINE v0.2

**Status:** WORKING BASELINE / BELUM FROZEN  
**Tanggal awal:** 15 Agustus 2026  
**Pembaruan:** 15 Agustus 2026  
**Repository:** `pesantrenriqa-boop/QURBATA`  
**Scope:** Tahfidz terintegrasi QURBATA Jilid 1–8  

---

## 1. Tujuan Dokumen

Dokumen ini menjadi file induk khusus pengembangan **Sistem Tahfidz QURBATA**. Tahap pertama berfokus pada penentuan surat, ayat, dan unit hafalan yang akan ditampilkan pada setiap halaman QURBATA Jilid 1–8.

Tahfidz QURBATA dibedakan dari program tahfidz lanjutan 30 juz.

---

## 2. Prinsip Dasar

1. Setiap halaman/pertemuan QURBATA mempunyai target tahfidz yang jelas.
2. Target tahfidz ditampilkan langsung pada halaman buku.
3. Target tidak dipaksakan dengan rumus `1 ayat = 1 halaman`.
4. Unit dapat berupa beberapa ayat sangat pendek, satu ayat, atau bagian dari ayat panjang.
5. Pembagian target mempertimbangkan panjang, jumlah kata, kompleksitas bacaan, level tartil, retensi, dan kontinuitas makna.
6. Hafalan baru dan murojaah adalah dua lapisan berbeda.
7. Tahfidz harus berkembang seiring kemampuan tartil QURBATA.
8. Pada level awal, hafalan dapat lebih banyak berbasis talqin; kemampuan membaca mandiri meningkat bertahap mengikuti jilid.

Format tampilan buku yang direncanakan:

`TAHFIDZ: QS. An-Nas [114]: 1–2`

atau bila satu ayat panjang dibagi:

`TAHFIDZ: QS. Al-Baqarah [2]: 255 — Bagian 1`

---

## 3. Kapasitas Kurikulum

Dengan baseline kerja sekitar **40 halaman/pertemuan per jilid**, delapan jilid menyediakan sekitar:

`8 jilid × 40 halaman = ±320 slot pembelajaran`

Angka 320 adalah **kapasitas slot**, bukan berarti harus ada 320 ayat baru. Sebagian slot dapat digunakan untuk ayat panjang yang dibagi, konsolidasi, evaluasi, atau target yang lebih ringan.

---

## 4. Unit Data Pemetaan

`JILID → HALAMAN → SURAT → AYAT → BAGIAN AYAT → BEBAN → STATUS`

| Jilid | Halaman | Surat | Ayat | Bagian | Beban | Status |
|---|---:|---|---:|---|---|---|
| J1 | P001 | TBD | TBD | - | TBD | DRAFT |
| J1 | P002 | TBD | TBD | - | TBD | DRAFT |
| ... | ... | ... | ... | ... | ... | ... |
| J8 | P040 | TBD | TBD | - | TBD | DRAFT |

---

## 5. Kandidat Corpus Awal

Untuk fase QURBATA, kandidat paling logis adalah memulai dari surat-surat pendek di bagian akhir Al-Qur'an. Alasannya:

- relatif cocok untuk peserta pemula;
- banyak digunakan dalam shalat dan ibadah harian;
- memungkinkan pengalaman keberhasilan hafalan sejak dini;
- unit ayatnya relatif mudah dibagi ke pertemuan;
- dapat ditingkatkan bertahap menuju surat yang lebih panjang.

Namun urutan final **tidak harus mengikuti urutan mushaf secara mekanis**. Urutan akan ditentukan berdasarkan beban pedagogis dan kesesuaian dengan perkembangan tartil.

---

## 6. Tiga Skenario Target Akhir

### Skenario A — Fondasi Ringan

**Target:** sekitar surat An-Nas sampai Ad-Duha dan pilihan surat/ayat fungsional.

Karakter:
- sangat aman untuk kelas reguler dengan jam terbatas;
- memberi ruang murojaah sangat besar;
- risiko ketertinggalan rendah;
- tetapi kapasitas 8 jilid berpotensi kurang dimanfaatkan.

**Status:** kandidat konservatif.

### Skenario B — Juz 30 sebagai Corpus Inti

**Target:** peserta menyelesaikan corpus hafalan **Juz 30** sepanjang QURBATA Jilid 1–8.

Karakter:
- target akhir mudah dipahami sekolah, guru, orang tua, dan peserta;
- cukup besar untuk menjadi capaian nyata QURBATA;
- tersedia ±320 slot sehingga beban dapat dibuat sangat bertahap;
- memungkinkan ayat panjang dibagi tanpa mengejar target secara agresif;
- masih menyediakan ruang untuk konsolidasi dan evaluasi.

**Status:** **REKOMENDASI BASELINE untuk diuji.**

Catatan: rekomendasi ini belum berarti setiap halaman langsung mendapat target final. Distribusi harus diuji terhadap panjang ayat dan struktur halaman QURBATA.

### Skenario C — Juz 30 + Corpus Pilihan

**Target:** Juz 30 ditambah surat/ayat pilihan yang sangat relevan untuk ibadah dan pendidikan.

Kandidat tambahan baru boleh dipilih setelah kapasitas nyata Juz 30 dihitung. Contoh kategori, bukan keputusan final:
- ayat/surat yang sering dibaca dalam praktik ibadah;
- ayat perlindungan/doa;
- ayat inti akidah/adab;
- surat pilihan yang menjadi jembatan menuju program tahfidz 30 juz.

Karakter:
- memanfaatkan kapasitas QURBATA lebih maksimal;
- hasil lulusan lebih kaya;
- tetapi berisiko mengurangi ruang retensi jika corpus terlalu besar.

**Status:** kandidat ekspansi setelah simulasi Skenario B.

---

## 7. Rekomendasi Kerja v0.2

Untuk pemetaan teknis berikutnya, digunakan hipotesis kerja:

> **Juz 30 menjadi corpus inti yang diuji untuk Tahfidz QURBATA Jilid 1–8.**

Alasan utama bukan mengejar jumlah juz, tetapi karena corpus ini dapat dibentangkan dalam ±320 slot secara bertahap sambil memberi ruang besar untuk pembagian ayat panjang dan penjagaan kualitas.

Keputusan ini masih **WORKING HYPOTHESIS**, belum FROZEN.

---

## 8. Prinsip Urutan Hafalan

Urutan tidak akan ditetapkan hanya berdasarkan urutan nomor surat. Pemetaan akan menggunakan prinsip:

1. mulai dari unit yang paling pendek dan mudah ditirukan;
2. mengutamakan surat yang fungsional dalam ibadah peserta;
3. meningkatkan panjang target secara gradual;
4. menghindari lonjakan beban antarhalaman;
5. mempertimbangkan kompetensi tartil yang sudah dipelajari;
6. mempertahankan kesinambungan satu surat sebisa mungkin;
7. memotong ayat panjang hanya pada batas lafaz/makna yang layak;
8. tidak menggunakan target hafalan untuk memaksa peserta membaca pola yang jauh melampaui kompetensi tartilnya tanpa dukungan talqin.

---

## 9. Model Gradasi Jilid yang Akan Diuji

### Jilid 1 — Entry / Talqin Dominan
Target sangat pendek. Fokus membangun kebiasaan mendengar, meniru, dan mengulang.

### Jilid 2 — Hafalan Pendek Stabil
Surat/ayat pendek dengan peningkatan kecil pada panjang unit.

### Jilid 3 — Transisi
Peserta mulai lebih banyak menghubungkan hafalan dengan kemampuan membaca yang berkembang.

### Jilid 4 — Menengah Awal
Unit hafalan bertambah dan mulai menerima ayat sedang.

### Jilid 5 — Menengah
Ayat sedang dan surat dengan struktur lebih panjang.

### Jilid 6 — Menengah Lanjut
Beban dapat meningkat, tetapi tetap adaptif terhadap panjang ayat.

### Jilid 7 — Lanjut
Masuk bagian Juz 30 yang relatif lebih panjang/kompleks.

### Jilid 8 — Penyelesaian Corpus
Menyelesaikan corpus inti sekaligus memperkuat kesiapan menuju tahfidz lanjutan.

Pembagian surat per jilid **belum dibekukan** sampai simulasi kuantitatif selesai.

---

## 10. Sistem Bobot Ayat — Draft

Agar distribusi tidak subjektif, setiap target nantinya akan diberi bobot berdasarkan:

- **L** = panjang/jumlah kata;
- **R** = kompleksitas lafaz dan repetisi;
- **T** = kompleksitas tartil/tajwid relatif terhadap level;
- **M** = kemudahan pemotongan pada batas makna;
- **F** = familiaritas/fungsi dalam praktik peserta.

Bobot ini tidak dimaksudkan untuk menilai kemuliaan ayat, melainkan hanya **beban pedagogis unit hafalan**.

Kategori keluaran sementara:

`Sangat Ringan → Ringan → Sedang → Berat → Sangat Berat`

Ayat kategori berat dapat memperoleh beberapa slot.

---

## 11. Hafalan Baru vs Murojaah

### Hafalan Baru
Target surat/ayat/bagian ayat yang diperkenalkan pada halaman tersebut.

### Murojaah
Target sebelumnya yang harus dipertahankan melalui sistem retensi tersendiri.

Peta 320 slot tidak boleh dianggap seluruhnya sebagai penambahan materi tanpa mempertimbangkan konsolidasi.

---

## 12. Problematika Kelas Besar

Kendala implementasi utama adalah banyaknya siswa dan terbatasnya waktu tatap muka. Pemeriksaan satu per satu pada setiap pertemuan tidak skalabel.

Masalah ini dicatat sebagai subsistem:

**QURBATA Tahfidz Retention & Validation System (QTRVS)**

Tujuannya nanti adalah memastikan hafalan terjaga tanpa menjadikan guru sebagai satu-satunya titik pemeriksaan setiap siswa pada setiap pertemuan.

**Belum dikerjakan pada fase corpus.**

---

## 13. Tahapan Pengembangan

- **T1A — Target Scenario:** DONE v0.2; tiga skenario dibuat, Juz 30 dipilih sebagai hipotesis kerja.
- **T1B — Corpus Inventory:** NEXT; inventaris seluruh surat/ayat Juz 30 beserta panjang dan bobot.
- **T1C — Pedagogical Sequence:** menentukan urutan hafalan.
- **T2 — Distribution by Volume:** membagi corpus ke Jilid 1–8.
- **T3 — Distribution by Page:** menetapkan J1-P001 sampai J8-P040.
- **T4 — Tartil Alignment Audit:** sinkronisasi dengan kompetensi tartil tiap jilid.
- **T5 — Retention/Murojaah System.**
- **T6 — Large-Class Validation System.**
- **T7 — Book + RIQA OS Integration.**

---

## 14. Decision Register

| ID | Keputusan | Status |
|---|---|---|
| QTS-D001 | Tahfidz QURBATA J1–J8 dibuat sebagai sistem khusus | ACTIVE |
| QTS-D002 | Setiap halaman mempunyai target tahfidz | ACTIVE |
| QTS-D003 | Target adaptif; tidak memakai aturan 1 ayat = 1 halaman | ACTIVE |
| QTS-D004 | Hafalan baru dipisahkan dari murojaah | ACTIVE |
| QTS-D005 | Program 30 juz berada di luar scope awal | ACTIVE |
| QTS-D006 | ±320 slot digunakan sebagai baseline kapasitas | WORKING |
| QTS-D007 | Juz 30 menjadi corpus inti untuk simulasi pertama | WORKING — NOT FROZEN |
| QTS-D008 | Urutan hafalan bersifat pedagogis, bukan mekanis | ACTIVE |

---

## 15. Pekerjaan Berikutnya

Langkah berikutnya **bukan menebak pembagian surat per jilid**. Sistem harus terlebih dahulu membuat inventaris Juz 30 pada level ayat, menghitung beban relatif, kemudian mensimulasikan distribusi terhadap ±320 slot.

Output T1B yang diperlukan:

`Surat | Ayat | Jumlah Kata | Beban Relatif | Kandidat Unit | Catatan Pemotongan | Level Tartil Minimum`

Setelah itu baru dapat ditentukan dengan dasar yang lebih kuat:

`J1-P001 → ... → J8-P040`

---

**Document ID:** `QTS-BASELINE-001`  
**Version:** `0.2`  
**State:** `ACTIVE WORKING DOCUMENT`