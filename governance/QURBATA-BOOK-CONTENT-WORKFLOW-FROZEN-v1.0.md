# QURBATA — FREEZE Alur Penyusunan Buku via ChatGPT

**Status:** FROZEN  
**Versi:** 1.0  
**Tanggal:** 2026-09-10  
**Pemilik akademik:** Aris Liswanto  
**Repositori:** pesantrenriqa-boop/QURBATA

## 1. Tujuan Freeze

Dokumen ini membekukan langkah kerja penyusunan buku QURBATA agar proses tidak langsung meloncat ke PDF/layout sebelum struktur kurikulum halaman disepakati.

Urutan wajib:

1. **SPEC KURIKULUM HALAMAN**
2. **FREEZE KONTEN**
3. **PROMPT / FORMAT LAYOUT**
4. **PRODUKSI PDF**

Layout, Vivliostyle, PDF, dan data produksi tidak boleh mengubah keputusan kurikulum yang sudah dibekukan.

---

## 2. Hierarki Sumber

Gunakan urutan berikut:

**Keputusan pemilik akademik / FROZEN terbaru → Hard Lock jilid → DEC-CUR → Master jilid → matriks/peta kompetensi → halaman kanonik → bank contoh/revisi → data produksi → PDF.**

Jika terjadi konflik, sumber yang lebih rendah harus menyesuaikan sumber yang lebih tinggi.

---

## 3. Konstitusi Jilid 1

### 3.1 Kompetensi akhir

Peserta mampu membaca seluruh huruf hijaiyah dalam keadaan **terpisah** dengan tiga harakat dasar:

**Fathah → Kasrah → Dhammah**

Jilid 1 belum mengajarkan:
- huruf sambung;
- tanwin;
- mad;
- sukun;
- tasydid;
- hukum tajwid lanjutan.

### 3.2 Tangga latihan

Kontrak kurikulum:
- 24 tangga per halaman;
- tangga 1–8 = rangkaian 2 huruf;
- tangga 9–24 = rangkaian 3 huruf;
- seluruh huruf tetap terpisah.

Kontrak layout terbaru:
- pada halaman kompetensi baru, satu baris latihan diganti blok **Penanaman Kompetensi Baru**;
- maka halaman cetak akuisisi menampilkan **1 blok penanaman + 7 baris × 3 kolom = 21 contoh**;
- bank kurikulum tetap dapat menyimpan 24 kandidat, tetapi hanya 21 yang dirender setelah kurasi.

### 3.3 Rasio materi baru dan murojaah

Untuk pekerjaan Jilid 1 saat ini, gunakan keputusan Hard Lock terbaru:

**±60% materi baru : ±40% murojaah**

P001 adalah pengecualian karena belum ada materi lama:
**100% materi baru.**

Urutan prioritas:
1. legalitas tangga;
2. kebenaran bentuk dan harakat;
3. materi aktif;
4. murojaah;
5. pemerataan;
6. kedekatan makna.

### 3.4 Murojaah

Murojaah mengikuti pola:
**N → N+1 → N+2 → N+4 → N+8 → rotasi kumulatif.**

Murojaah harus:
- tersebar;
- tidak hanya mengambil halaman terakhir;
- tetap berada di dalam whitelist kompetensi yang sudah legal;
- tidak memasukkan materi masa depan.

---

## 4. Aturan Penanaman Kompetensi Baru

Setiap halaman akuisisi wajib memiliki blok besar **Penanaman Kompetensi Baru** sebelum grid latihan.

Aturan:
- menampilkan kompetensi lama → kompetensi baru pada huruf yang sama;
- ukuran huruf setara huruf latihan;
- arah baca RTL;
- bukan strip teori kecil;
- tidak boleh bentuk baru → bentuk baru;
- tidak boleh memperkenalkan materi yang belum waktunya.

Contoh saat masuk kasrah:
**جَ → جِ**

Contoh saat masuk dhammah:
**جِ → جُ** atau bentuk pembanding yang ditetapkan secara konsisten.

P001 tidak memakai panah transformasi karena belum ada kompetensi lama; cukup menampilkan:
**بَ   تَ   ثَ**

---

## 5. Aturan Kata Bermakna / Keselarasan Leksikal

Prioritas contoh:

**kata Arab nyata → akar/pola Arab valid → bentuk sangat dekat dengan pola Arab → controlled drill.**

Ketentuan:
- kata bermakna tidak boleh memaksa masuknya huruf/harakat yang belum legal;
- harakat tidak boleh diganti mekanis hanya demi mencapai rasio;
- bentuk palsu seperti **كِ مِ لِ** dari kata yang seharusnya **كَ مُ لَ** dilarang;
- klaim Qurani/hadis hanya setelah Source-ID dan verifikasi;
- pada fase awal, controlled drill sah jika inventori huruf belum memungkinkan kata natural;
- semakin banyak huruf legal, proporsi contoh bermakna harus semakin meningkat.

Arah rasa leksikal Jilid 1:
- P001–P002: fondasi bunyi/bentuk;
- P003–P005: jembatan ke pola Arab;
- P006–P009: rasa mufradat/akar Arab-Qurani semakin nyata;
- P014 dan seterusnya: bank kata bermakna semakin dominan.

---

## 6. Peta Kompetensi Jilid 1 — Fase Fathah

- **P001:** بَ تَ ثَ
- **P002:** ءَ أَ + murojaah P001
- **P003:** جَ حَ خَ + murojaah
- **P004:** دَ ذَ رَ زَ + murojaah
- **P005:** سَ شَ + murojaah
- **P006:** صَ ضَ + murojaah
- **P007:** طَ ظَ + murojaah
- **P008:** عَ غَ + murojaah
- **P009:** فَ قَ + murojaah
- **P010:** evaluasi fathah I
- **P011:** كَ لَ
- **P012:** مَ نَ
- **P013:** هَ وَ يَ
- **P014:** integrasi seluruh fathah
- **P015:** otomatisasi fathah

Setelah itu:
- P016 dst. masuk Kasrah bertahap;
- setelah Kasrah lengkap dilakukan integrasi/penguatan;
- P026 dst. masuk Dhammah bertahap;
- akhir jilid untuk integrasi tiga harakat, diskriminasi bentuk, kelancaran, dan evaluasi.

---

## 7. Freeze Draft Kurikulum P001

### QJ1-P001
**Kompetensi baru:** بَ تَ ثَ  
**Murojaah:** tidak ada  
**Rasio:** 100% materi baru  
**Huruf:** terpisah  
**Harakat:** fathah saja

### Penanaman
**بَ   تَ   ثَ**

### 8 kandidat dua huruf
1. بَ تَ
2. تَ ثَ
3. ثَ بَ
4. بَ ثَ
5. ثَ تَ
6. تَ بَ
7. بَ بَ
8. ثَ ثَ

### 16 kandidat tiga huruf
1. بَ تَ ثَ
2. بَ ثَ تَ
3. تَ بَ ثَ
4. تَ ثَ بَ
5. ثَ بَ تَ
6. ثَ تَ بَ
7. بَ بَ تَ
8. بَ تَ بَ
9. تَ بَ بَ
10. تَ تَ ثَ
11. تَ ثَ ثَ
12. ثَ تَ تَ
13. ثَ ثَ بَ
14. ثَ بَ بَ
15. بَ ثَ ثَ
16. ثَ بَ ثَ

### Blacklist P001
Dilarang muncul:
- ء أ ج ح خ dan huruf lain di luar ب ت ث;
- kasrah;
- dhammah;
- sambung;
- mad;
- tanwin;
- sukun;
- tasydid.

### Catatan pedagogis
P001 tidak dipaksa menjadi kumpulan kata bermakna karena whitelist terlalu sempit. Fungsi utama adalah diskriminasi visual dan bunyi.

---

## 8. Panel Integrasi

Tahfidz, Bahasa Arab, dan Akhlak/NIDHOM adalah **panel integrasi**, bukan whitelist latihan Tartil.

Teks panel boleh berupa materi lisan/talqin yang unsur bacanya belum seluruhnya dapat didekode peserta, selama peserta tidak diminta membacanya mandiri sebagai latihan Tartil.

Panel integrasi tidak boleh menjadi alasan memasukkan huruf/harakat yang belum legal ke grid Tartil.

---

## 9. Workflow Wajib per Halaman

### A. SPEC KURIKULUM
Sebelum layout, tulis:
- Page-ID;
- kompetensi;
- prasyarat;
- materi baru;
- whitelist;
- blacklist;
- rasio materi baru/murojaah;
- jadwal murojaah;
- 24 kandidat latihan;
- klasifikasi F/M/T/E;
- kandidat Tahfidz/BA/Akhlak;
- catatan risiko.

### B. FREEZE KONTEN
Pemilik akademik memeriksa dan menyatakan halaman **FREEZE**.

Setelah freeze:
- isi tidak boleh berubah diam-diam;
- revisi harus membuka freeze;
- alasan revisi dicatat.

### C. LAYOUT
Baru setelah konten freeze:
- terapkan Blueprint visual FROZEN;
- KFGQPC Uthman Taha;
- blok penanaman;
- grid 7×3 pada halaman akuisisi;
- panel integrasi;
- Aktivitas Bi'ah;
- QR RIQA OS;
- tanggal, nilai, TTD.

### D. PDF
PDF adalah artefak turunan, bukan sumber kurikulum.

---

## 10. Larangan

Dilarang:
- membuat PDF sebelum SPEC halaman jelas;
- mengubah tangga demi mengejar kata bermakna;
- mengubah harakat kata secara mekanis;
- memasukkan kompetensi masa depan;
- menggunakan bentuk sambung di Jilid 1;
- menganggap panel Tahfidz/BA/Akhlak sebagai whitelist Tartil;
- mengubah konten yang sudah FREEZE tanpa membuka freeze;
- memperlakukan data produksi/PDF sebagai pengendali kurikulum.

---

## 11. Keputusan

Dokumen ini menjadi baseline kerja penyusunan Buku QURBATA melalui ChatGPT.

Langkah berikutnya setelah freeze ini:
1. audit/finalisasi QJ1-P001;
2. freeze QJ1-P001;
3. susun QJ1-P002 dengan format SPEC yang sama;
4. lanjut halaman demi halaman;
5. layout dan PDF dibuat setelah konten halaman selesai dibekukan.
