# QURBATA TAHFIDZ SYSTEM — BASELINE v0.1

**Status:** WORKING BASELINE / BELUM FROZEN  
**Tanggal awal:** 15 Agustus 2026  
**Repository:** `pesantrenriqa-boop/QURBATA`  
**Scope:** Tahfidz terintegrasi QURBATA Jilid 1–8  

---

## 1. Tujuan Dokumen

Dokumen ini menjadi file induk khusus untuk pengembangan **Sistem Tahfidz QURBATA** agar seluruh keputusan, pemetaan, revisi, dan perkembangan kurikulum tahfidz QURBATA tidak hilang dan tidak tercampur dengan sistem tahfidz lanjutan 30 juz.

Tahap pertama berfokus pada **penentuan surat, ayat, dan unit hafalan yang ditampilkan pada setiap halaman QURBATA Jilid 1–8**.

---

## 2. Ruang Lingkup Sistem Tahfidz QURBATA

Sistem tahfidz dibagi menjadi dua lapisan besar:

1. **Tahfidz QURBATA Jilid 1–8** — scope dokumen ini.
2. **Tahfidz lanjutan / Program 30 Juz** — akan dikembangkan setelah sistem QURBATA selesai dan tidak dicampur pada tahap awal ini.

---

## 3. Prinsip Integrasi dengan Pembelajaran Tartil

Tahfidz QURBATA harus berjalan seiring dengan pembelajaran tartil QURBATA Jilid 1–8.

Prinsip dasarnya:

- setiap halaman/pertemuan QURBATA memiliki target tahfidz yang jelas;
- target tahfidz ditampilkan langsung pada halaman QURBATA;
- beban hafalan tidak dipaksakan sama untuk setiap halaman;
- satu unit hafalan dapat berupa satu ayat, beberapa ayat pendek, atau sebagian dari satu ayat panjang;
- pembagian target harus mengikuti kemampuan peserta dan tingkat kesulitan ayat;
- urutan hafalan perlu dipetakan secara pedagogis, bukan hanya mengikuti nomor ayat secara mekanis;
- tingkat kemampuan tartil pada jilid yang sedang dipelajari harus menjadi salah satu pertimbangan dalam pemilihan target hafalan.

Contoh format tampilan:

`TAHFIDZ: QS. An-Nas [114]: 1`

atau:

`TAHFIDZ: QS. Al-Baqarah [2]: 255 — Bagian 1`

Contoh tersebut belum otomatis menjadi keputusan final sampai peta Jilid 1–8 disahkan.

---

## 4. Unit Dasar Pemetaan

Unit kerja kurikulum adalah:

`JILID → HALAMAN/PERTEMUAN → SURAT → AYAT → BAGIAN AYAT → BEBAN`

Template data:

| Jilid | Halaman | Surat | Ayat | Bagian | Jenis Unit | Beban | Status |
|---|---:|---|---:|---|---|---|---|
| J1 | P001 | TBD | TBD | - | TBD | TBD | DRAFT |
| J1 | P002 | TBD | TBD | - | TBD | TBD | DRAFT |

Target awal adalah membangun peta penuh dari J1-P001 sampai akhir Jilid 8.

---

## 5. Aturan Beban Hafalan

Target hafalan **tidak harus 1 ayat = 1 halaman**.

Kemungkinan unit:

- ayat sangat pendek: beberapa ayat dalam satu pertemuan;
- ayat pendek: satu ayat dalam satu pertemuan;
- ayat sedang: satu ayat atau pembagian sesuai kebutuhan;
- ayat panjang: dapat dibagi menjadi 2, 3, atau lebih unit/pertemuan jika diperlukan.

Penilaian beban nantinya minimal mempertimbangkan:

1. panjang ayat;
2. jumlah kata;
3. kompleksitas lafaz/bacaan;
4. level kemampuan tartil peserta;
5. kemudahan pengulangan dan retensi;
6. kontinuitas makna bila ayat perlu dipotong menjadi beberapa bagian.

---

## 6. Target Baru dan Murojaah Harus Dipisahkan

Sistem harus membedakan secara eksplisit:

### A. Hafalan Baru
Ayat atau bagian ayat baru yang menjadi target halaman/pertemuan tersebut.

### B. Murojaah
Hafalan sebelumnya yang harus dipertahankan.

Pada tahap pertama, fokus utama adalah menyusun **hafalan baru per halaman**. Sistem murojaah akan dirancang sebagai lapisan tersendiri agar pemetaan surat dan ayat tidak bercampur dengan mekanisme pemeliharaan hafalan.

---

## 7. Problematika Utama yang Sudah Teridentifikasi

### 7.1 Pemetaan ayat terhadap 8 jilid

Harus ditentukan:

- surat apa yang masuk;
- urutan surat;
- urutan ayat;
- berapa ayat atau bagian ayat per pertemuan;
- target akhir hafalan setelah peserta menyelesaikan Jilid 8.

### 7.2 Menjaga hafalan pada kelas besar

Kendala utama implementasi di sekolah adalah jumlah siswa dapat sangat banyak sementara waktu pembelajaran terbatas. Pemeriksaan hafalan satu per satu oleh guru pada setiap pertemuan berpotensi menghabiskan waktu pembelajaran.

Masalah ini akan dibuat sebagai **sub-sistem Retensi & Validasi Hafalan**, tetapi belum menjadi fokus pengerjaan tahap pertama.

### 7.3 Tahfidz lanjutan 30 juz

Program tahfidz 30 juz merupakan kelanjutan setelah QURBATA dan akan dibuat sebagai sistem tersendiri yang dapat menggunakan hasil kompetensi QURBATA sebagai baseline.

---

## 8. Tahapan Pengembangan

### Fase T1 — Corpus Hafalan QURBATA
Menentukan target akhir dan daftar surat/ayat yang realistis untuk Jilid 1–8.

### Fase T2 — Distribusi Jilid
Membagi corpus ke Jilid 1 sampai Jilid 8.

### Fase T3 — Distribusi Halaman
Menetapkan target hafalan pada setiap halaman/pertemuan.

### Fase T4 — Sinkronisasi Tartil
Audit agar target hafalan sesuai dengan perkembangan kompetensi bacaan QURBATA.

### Fase T5 — Sistem Murojaah
Membangun algoritme/lapisan pengulangan dan penjagaan hafalan.

### Fase T6 — Validasi Kelas Besar
Membangun sistem efisien agar guru tidak harus mengecek seluruh siswa satu per satu pada setiap pertemuan.

### Fase T7 — Integrasi Buku & RIQA OS
Memasukkan target tahfidz ke halaman produksi QURBATA serta menyiapkan struktur data digital bila diperlukan.

---

## 9. Keputusan Baseline v0.1

Keputusan yang sudah dapat dijadikan pegangan kerja:

1. Tahfidz QURBATA Jilid 1–8 dibuat sebagai sistem khusus.
2. Setiap halaman/pertemuan QURBATA akan mempunyai target hafalan.
3. Target berupa surat + nomor ayat, dan bila perlu bagian ayat.
4. Panjang target bersifat adaptif terhadap panjang dan tingkat kesulitan ayat.
5. Hafalan baru dan murojaah dipisahkan.
6. Pemetaan surat/ayat dikerjakan sebelum desain sistem pengecekan kelas besar.
7. Program 30 juz berada di luar scope tahap pertama.
8. Dokumen ini bersifat hidup dan akan diperbarui setiap keputusan baru sampai siap dibekukan/frozen.

---

## 10. Keputusan yang Belum Ditentukan

- total hafalan akhir setelah Jilid 8;
- jumlah surat yang masuk;
- urutan surat;
- titik awal dan titik akhir corpus;
- alokasi target per jilid;
- alokasi target per halaman;
- rumus bobot ayat;
- sistem murojaah;
- sistem validasi hafalan kelas besar;
- standar kelulusan tahfidz QURBATA.

Semua poin di atas berstatus **OPEN / TO BE MAPPED**.

---

## 11. Langkah Kerja Berikutnya

Pekerjaan berikutnya adalah membuat **Peta Corpus Tahfidz QURBATA Jilid 1–8** dengan beberapa skenario target akhir yang realistis. Setelah target akhir dipilih, seluruh surat dan ayat akan didistribusikan ke halaman QURBATA secara bertahap.

---

**Document ID:** `QTS-BASELINE-001`  
**Version:** `0.1`  
**State:** `ACTIVE WORKING DOCUMENT`