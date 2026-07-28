# STAT-QUR-001 — Dashboard Progres Keseluruhan QURBATA

**Status-ID:** STAT-QUR-001  
**Status:** BASELINE TERKENDALI  
**Tanggal pengukuran:** 29 Juli 2026  
**Cakupan:** QURBATA Jilid 1–8 sampai rilis tervalidasi  
**Cabang bukti:** `feature/qj1-master-structure`  
**Catatan:** persentase adalah progres penyelesaian artefak dan gate, bukan klaim efektivitas pendidikan.

## 1. Hasil Utama

| Indikator | Nilai |
|---|---:|
| Progres keseluruhan QURBATA menuju 100% | **31%** |
| Kesiapan Jilid 1 keluar-Draft | **25% — 2 dari 8 gate makro** |
| Governance QURBATA v1.0 | **100% untuk baseline yang telah diratifikasi** |
| Buku dengan sumber halaman lengkap | **1 dari 8 jilid** |
| Halaman buku formal tersedia | **40 halaman Jilid 1** |
| Jilid 2–8 dengan halaman formal | **0 dari 7 jilid** |

Angka 31% tidak boleh dibaca sebagai “Jilid 1 sudah 31%”. Angka itu adalah gabungan berbobot seluruh proyek 8 jilid. Angka 25% hanya mengukur gate keluar-Draft Jilid 1.

## 2. Definisi QURBATA 100%

QURBATA dinyatakan 100% pada baseline produk pertama apabila:

1. governance dan konstitusi tetap terkendali;
2. arsitektur kurikulum lintas Jilid 1–8 lengkap;
3. seluruh halaman Jilid 1–8 selesai, terlacak, dan konsisten;
4. progression baca Al-Qur’an, Tahfidz, Bahasa Arab, dan Akhlak/Hadis selesai;
5. kosa kata, kalimat, teks, nahwu/struktur, dan murojaah mempunyai sumber tunggal;
6. hadis akhlak sahih, bertahap, tidak berulang, dan telah diverifikasi;
7. asesmen, remedial, safeguarding, dan aturan kenaikan jilid tervalidasi;
8. review ahli, pilot, revisi, Evidence-ID, dan otorisasi selesai;
9. buku guru/peserta serta PDF final Jilid 1–8 lulus produksi;
10. paket rilis memiliki version snapshot, arsip, dan audit trail.

Flashcard, presentasi, atau RIQA OS tidak menjadi syarat menyebut **delapan buku inti** selesai, tetapi integrasi sumber tunggal dan kesiapan data turunannya tetap wajib.

## 3. Model Bobot

| Domain | Bobot terhadap 100% | Ketercapaian domain | Kontribusi |
|---|---:|---:|---:|
| Governance dan kontrol konstitusional | 10% | 100% | 10,0% |
| Arsitektur kurikulum lintas jilid | 20% | 65% | 13,0% |
| Isi buku Jilid 1–8 | 45% | 8,75% | 3,94% |
| Validasi ilmiah, ahli, asesmen, dan pilot | 15% | 20% | 3,0% |
| Produksi dan rilis final | 10% | 15% | 1,5% |
| **Total mentah** | **100%** |  | **31,44%** |
| **Nilai laporan dibulatkan** |  |  | **31%** |

### Rumus domain buku

Domain buku mempunyai bobot terbesar karena produk utama QURBATA adalah delapan jilid buku.

```text
Ketercapaian domain buku
= (ketercapaian Jilid 1 + ... + ketercapaian Jilid 8) / 8
= (70% + 0% + 0% + 0% + 0% + 0% + 0% + 0%) / 8
= 8,75%
```

Nilai internal Jilid 1 sebesar 70% berarti sumber 40 halaman, audit distribusi, pemetaan Bahasa Arab/Tahfidz, dan prototipe cetak tersedia. Nilai ini tidak berarti Jilid 1 siap terbit; gate manusia dan keputusan material masih terbuka.

## 4. Dasar Penilaian per Domain

### A. Governance — 100% dari bobot domain

Bukti:

- QC-000–QC-012 tersedia;
- register governance dan bukti tersedia;
- DEC-GOV-004 meratifikasi Governance v1.0 efektif 27 Juli 2026;
- baseline governance dibekukan dan memiliki audit trail.

Pekerjaan pemeliharaan governance tidak menurunkan baseline 100%, kecuali ditemukan cacat material atau perubahan organisasi.

### B. Arsitektur kurikulum lintas jilid — 65%

Sudah tersedia:

- model PO/LO/KO/BO/CUR dan register objek;
- DEC-CUR-001–003;
- Arabic Competency Progression;
- baseline 640 lema Jilid 1–8;
- register kosa kata, kalimat, teks, dan siklus;
- mapping Bahasa Arab Jilid 1;
- mapping dan kontrol Tahfidz Jilid 1;
- prinsip murojaah kumulatif;
- HCP-QUR-001 dan REG-HAD-001 sebagai progression serta sumber tunggal Hadis Akhlak Jilid 1–8 (belum berisi objek aktif).

Masih belum lengkap:

- progression baca/tajwid formal Jilid 2–8;
- mapping Tahfidz Jilid 2–8;
- inventaris Hadith-ID nyata, takhrij, terjemah, mapping halaman, dan validasi ahli atas hadis akhlak Jilid 1–8;
- pembagian final Bahasa Arab Jilid 2–8;
- aturan kenaikan jilid lintas-strand yang tervalidasi.

### C. Isi buku Jilid 1–8 — 8,75%

| Jilid | Status isi formal | Estimasi internal |
|---:|---|---:|
| 1 | 40 halaman sumber, audit, mapping, dan prototipe tersedia; tetap Draft | 70% |
| 2 | halaman formal belum tersedia | 0% |
| 3 | halaman formal belum tersedia | 0% |
| 4 | halaman formal belum tersedia | 0% |
| 5 | halaman formal belum tersedia | 0% |
| 6 | halaman formal belum tersedia | 0% |
| 7 | halaman formal belum tersedia | 0% |
| 8 | halaman formal belum tersedia | 0% |

### D. Validasi ilmiah/ahli/pilot — 20%

Sudah tersedia:

- protokol dan paket review;
- rubrik serta form bukti Bahasa Arab;
- rubrik, form, paket ahli, dan audit keterlacakan Tahfidz;
- register blocker dan gate.

Belum tersedia:

- keputusan ahli Al-Qur’an/Qira’at dan Bahasa Arab;
- Evidence-ID validasi;
- review akademik/editorial/asesmen/safeguarding lengkap;
- pilot kelas dan analisis hasil;
- reliabilitas/validitas rubrik;
- keputusan kelayakan lintas Jilid 1–8.

### E. Produksi dan rilis — 15%

Sudah tersedia:

- generator PDF;
- contoh A5 potret;
- font Amiri Quran dan kontrol lisensi;
- build teknis Jilid 1;
- audit kebocoran prototipe.

Belum tersedia:

- finishing final;
- proof fisik;
- persetujuan percetakan;
- buku guru final;
- PDF final terotorisasi Jilid 1;
- seluruh keluaran Jilid 2–8;
- paket rilis dan arsip versi final.

## 5. Kesiapan Keluar-Draft Jilid 1

| No. | Gate | Status |
|---:|---|---|
| 1 | Struktur 40 halaman lengkap | COMPLETE |
| 2 | Audit otomatis distribusi dan whitelist | COMPLETE |
| 3 | Keputusan materi khusus | OPEN |
| 4 | Review akademik/Arab/Qira’at | OPEN |
| 5 | Review editorial dan render | OPEN |
| 6 | Validasi asesmen dan safeguarding | OPEN |
| 7 | Otorisasi dan audit trail | OPEN |
| 8 | Penutupan seluruh blocker | OPEN |

Kesiapan Jilid 1 keluar-Draft tetap **25%**. Artefak internal tambahan memperbaiki kesiapan di dalam gate terbuka, tetapi satu gate hanya berubah COMPLETE setelah seluruh syarat gate tersebut terpenuhi.

## 6. Aturan Perubahan Persentase

1. Persentase hanya naik bila ada artefak atau gate yang dapat diperiksa.
2. Draf tidak dihitung sama dengan validasi.
3. Satu dokumen administratif tidak boleh menaikkan progres secara tidak proporsional.
4. Pekerjaan ulang untuk memperbaiki cacat tidak otomatis menambah persentase; ia menjaga integritas baseline.
5. Jilid 2–8 baru memperoleh nilai isi setelah mempunyai sumber halaman formal.
6. Keputusan ahli dan pilot menaikkan domain validasi, bukan domain isi.
7. PDF final menaikkan produksi hanya setelah isi dan otorisasi lulus.
8. Angka dibulatkan ke bilangan bulat untuk laporan pengguna; nilai mentah dipertahankan untuk audit.

## 7. Target Kenaikan Berikutnya

Jalur tercepat yang sah dari 31%:

1. menetapkan materi khusus Jilid 1 melalui keputusan ahli dan Pemilik Akademik;
2. menyelesaikan review akademik, editorial, asesmen, serta safeguarding Jilid 1;
3. menyusun master hadis akhlak sahih dan progression Tahfidz Jilid 1–8;
4. membentuk struktur halaman formal Jilid 2;
5. menjalankan pilot Jilid 1 dan menerapkan koreksi;
6. mengulang pipeline terkendali untuk Jilid 2–8.

## 8. Riwayat

| Versi | Tanggal | Ringkasan |
|---|---|---|
| 0.2.0-id | 29 Juli 2026 | Progression dan register Hadis Akhlak menambah ketercapaian arsitektur menjadi 65%; total mentah 31,44%, laporan 31% |
| 0.1.0-id | 28 Juli 2026 | Baseline berbobot pertama: progres keseluruhan 30%, kesiapan keluar-Draft Jilid 1 25% |
