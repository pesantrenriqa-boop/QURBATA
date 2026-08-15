# QURBATA TAHFIDZ — JILID 1 RETENTION & VALIDATION MATRIX v0.1

**Document ID:** QTS-J1-RVM-001  
**Status:** ACTIVE DESIGN / NOT FROZEN  
**Date:** 15 August 2026  
**Input:** `QURBATA-TAHFIDZ-J1-P001-P040-MAP-v0.2.md`

---

## 1. Tujuan

Dokumen ini mendesain sistem menjaga hafalan Tahfidz QURBATA Jilid 1 untuk kelas besar dengan waktu terbatas.

Masalah yang harus diselesaikan:

> Guru tidak mungkin mendengarkan seluruh siswa satu per satu pada setiap pertemuan tanpa menghabiskan jam pembelajaran.

Karena itu validasi hafalan menggunakan **evidence layering**, bukan full individual checking setiap hari.

---

## 2. Prinsip Utama

1. Semua siswa tetap mengulang hafalan pada setiap pertemuan.
2. Tidak semua siswa harus dites individual pada setiap pertemuan.
3. Validasi dilakukan berlapis: kelas → pasangan/kelompok → sampling guru → individual terarah → gate formal.
4. Siswa yang aman tidak perlu terus menerus diperiksa penuh; siswa yang terindikasi lemah mendapat frekuensi pemeriksaan lebih tinggi.
5. Review gate P010, P020, P030, P040 menjadi checkpoint formal.
6. Sistem harus dapat berjalan tanpa aplikasi, tetapi metadata disiapkan agar nanti dapat diintegrasikan ke RIQA OS.

---

## 3. Lima Lapisan Validasi

### L1 — Jama'i / Collective Recitation

Seluruh kelas membaca hafalan terpilih bersama-sama mengikuti imam/guru atau audio acuan.

Fungsi:
- aktivasi memori;
- menjaga ritme kelas;
- koreksi global makhraj/lafaz;
- tidak dianggap sebagai bukti individual final.

### L2 — Pair / Small-Group Check

Siswa berpasangan atau kelompok kecil 3–4 orang. Satu membaca, lainnya menyimak menggunakan checklist sederhana.

Fungsi:
- memperbanyak kesempatan retrieval;
- memberi bukti awal siapa yang lancar/tersendat;
- mengurangi bottleneck guru.

### L3 — Random Teacher Spot Check

Guru memilih sampel acak per pertemuan.

Target awal kandidat:
- 10–20% siswa per sesi;
- dapat ditingkatkan bila kelas kecil;
- rotasi memastikan seluruh siswa tersampel dalam beberapa pertemuan.

Spot check cukup pendek: satu ayat, sambung ayat, awal tengah akhir surat, atau cue acak.

### L4 — Targeted Individual Check

Hanya untuk siswa berstatus risiko:
- sering terhenti;
- salah lafaz berulang;
- laporan peer check rendah;
- gagal spot check;
- absen beberapa pertemuan;
- gagal review gate sebelumnya.

### L5 — Formal Review Gate

Dilaksanakan pada P010, P020, P030, P040.

Pada gate, validasi lebih kuat dan hasilnya menentukan status retensi.

---

## 4. Status Retensi Siswa

Setiap siswa memiliki status sederhana:

- `GREEN` — hafalan stabil; cukup rotasi normal.
- `YELLOW` — ada keraguan/kesalahan; perlu targeted review.
- `RED` — hafalan tidak stabil/gagal gate; wajib intervensi individual.
- `RECOVERY` — sedang mengejar ketertinggalan karena absen/gagal berulang.

Status tidak bersifat permanen dan harus dapat naik/turun berdasarkan bukti terbaru.

---

## 5. Algoritma Pertemuan Biasa

Untuk halaman non-gate:

### Langkah A — Review Lama

Ambil 2 jenis murojaah:

- **Near Review:** target 1–3 pertemuan terakhir.
- **Far Review:** surat/ayat lama yang dipilih rotasi.

### Langkah B — Collective Recitation

Semua siswa membaca Near Review bersama.

### Langkah C — Pair Retrieval

Siswa berpasangan:
- A membaca;
- B menyimak;
- tukar peran;
- gunakan cue sambung ayat atau awal surat.

### Langkah D — Teacher Sampling

Guru mengambil sampel acak dan targeted sample dari Yellow/Red.

### Langkah E — Hafalan Baru

Guru melakukan talqin target baru.

### Langkah F — Quick Exit Retrieval

Sebelum selesai, kelas mengulang target baru tanpa melihat sebanyak 1–3 kali.

---

## 6. Rasio Near / Far Review

Kandidat awal:

- 60% waktu murojaah = Near Review;
- 40% = Far Review.

Setelah corpus bertambah, rasio dapat bergeser menuju:

- 40% Near;
- 60% Far.

Rasio ini **belum frozen** dan perlu uji lapangan.

---

## 7. Spaced Rotation Candidate

Setiap target baru masuk jadwal review berulang:

`D0 → D1 → D3 → D7 → D14 → D30 → monthly rotation`

Makna:
- D0 = hari target diperkenalkan;
- D1 = pertemuan berikut;
- D3 = sekitar tiga pertemuan setelahnya;
- dst.

Dalam implementasi sekolah yang pertemuannya tidak harian, angka dibaca sebagai **interval pertemuan**, bukan hari kalender.

---

## 8. Gate Matrix Jilid 1

### P010 — Gate 1

Corpus:
- An-Nas lengkap;
- Al-Falaq 1–3.

Validasi:
1. jama'i;
2. pair check;
3. sampling guru minimal 20%;
4. semua Yellow/Red wajib individual singkat.

### P020 — Gate 2

Corpus:
- An-Nas;
- Al-Falaq;
- Al-Ikhlas;
- Al-Fatihah 1–4.

Validasi:
- random cue antar-surah;
- sambung ayat;
- awal ayat acak;
- targeted individual untuk Yellow/Red.

### P030 — Gate 3

Corpus:
- seluruh corpus sebelumnya;
- Al-Fatihah lengkap;
- Al-Kawthar;
- An-Nasr;
- Al-Kafirun 1–2.

Fokus:
- retensi lintas surat;
- random switching;
- tidak hanya membaca urut dari awal.

### P040 — Terminal Gate

Corpus kandidat J1:
- 9 surat lengkap termasuk Al-Fatihah.

Hasil terminal:
- `J1-TAHFIDZ-PASS`
- `J1-TAHFIDZ-PASS-WITH-SUPPORT`
- `J1-TAHFIDZ-RECOVERY`

---

## 9. Sampling Rotation Engine

Agar adil, guru tidak memilih siswa yang sama terus menerus.

Setiap siswa memiliki:

`LAST_SAMPLE_PAGE`
`SAMPLE_COUNT`
`RISK_STATUS`

Prioritas sampling:

1. RED;
2. YELLOW;
3. siswa yang paling lama belum tersampel;
4. random GREEN.

Dengan model ini guru dapat memeriksa sebagian kelas tiap pertemuan tetapi seluruh siswa tetap masuk radar.

---

## 10. Peer Check Safeguard

Peer checking bukan sertifikasi final.

Aturan:
- siswa hanya memberi indikator sederhana: lancar / ragu / perlu bantuan;
- tidak memberi nilai resmi;
- kesalahan tajwid kompleks tidak dibebankan pada peer;
- guru tetap pemegang keputusan status formal.

---

## 11. Rubrik Cepat Guru

Spot check 15–30 detik dapat memakai tiga indikator:

- `L` = lancar;
- `R` = ragu/terputus;
- `E` = error lafaz/urutan.

Contoh keputusan:

- `L,L` → GREEN;
- `L,R` → tetap GREEN/YELLOW tergantung pola;
- `R,R` atau `E` berulang → YELLOW;
- gagal gate / tidak mampu melanjutkan → RED.

---

## 12. Estimasi Skalabilitas

Contoh kelas 36 siswa:

Jika guru spot-check 6 siswa per pertemuan, maka dalam 6 pertemuan seluruh kelas dapat tersentuh minimal sekali, di luar siswa Yellow/Red yang mendapat pemeriksaan tambahan.

Guru tidak perlu mendengar 36 setoran penuh setiap hari.

---

## 13. Metadata RIQA OS Candidate

Per siswa:

`TAHFIDZ_STATUS`
`LAST_VALIDATED_TARGET`
`RETENTION_COLOR`
`LAST_SAMPLE_PAGE`
`SAMPLE_COUNT`
`GATE_RESULT`
`RECOVERY_TARGET`
`ABSENCE_RISK`

Per kelas:

`CURRENT_PAGE`
`NEAR_REVIEW_SET`
`FAR_REVIEW_SET`
`RANDOM_SAMPLE_QUEUE`
`RISK_QUEUE`

---

## 14. Aturan Anti-Bottleneck

1. Full-class individual checking hanya dilakukan bila memang diperlukan, bukan default.
2. Gate formal juga boleh memakai dua tahap: screening cepat → individual hanya untuk yang belum jelas.
3. Guru fokus pada koreksi berkualitas, bukan mendengar repetisi siswa yang sudah stabil terus-menerus.
4. Evidence dari jama'i dan peer dipakai untuk screening, bukan sebagai kelulusan final tunggal.

---

## 15. Hubungan dengan P039 Stress Point

Jika P039 terlalu berat, indikator yang diamati:
- proporsi Yellow/Red naik tajam;
- gate P040 banyak gagal;
- waktu talqin melebihi alokasi;
- Far Review runtuh karena seluruh waktu habis untuk target baru.

Jika salah satu terjadi secara konsisten, bagian Al-Ma'un harus digeser ke J2.

---

## 16. Freeze Criteria

Matrix ini dapat dibekukan setelah uji minimal pada satu kelas nyata dengan data:

- ukuran kelas;
- durasi pembelajaran;
- rata-rata siswa tersampel per sesi;
- proporsi GREEN/YELLOW/RED;
- tingkat kelulusan P010/P020/P030/P040;
- waktu yang dihabiskan untuk murojaah;
- failure point P039.

---

## 17. Next Artifact

Create:

`QURBATA-TAHFIDZ-J1-TEACHER-FLOW-v0.1.md`

Target: prosedur operasional guru 5–10 menit bagian tahfidz per pertemuan, lengkap dengan script alur kelas, sampling, pair-check, dan pencatatan status.

---

**State:** ACTIVE DESIGN  
**Freeze:** NOT YET  
**Next:** Teacher Flow + field-test protocol