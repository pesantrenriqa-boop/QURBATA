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
| Progres keseluruhan QURBATA menuju 100% | **32%** |
| Kesiapan Jilid 1 keluar-Draft | **38% — 3 dari 8 gate makro** |
| Governance QURBATA v1.0 | **100% untuk baseline yang telah diratifikasi** |
| Buku dengan sumber halaman lengkap | **1 dari 8 jilid** |
| Halaman buku formal tersedia | **40 halaman Jilid 1** |
| Jilid 2–8 dengan halaman formal | **0 dari 7 jilid** |

Angka 32% tidak boleh dibaca sebagai “Jilid 1 sudah 32%”. Angka itu adalah gabungan berbobot seluruh proyek 8 jilid. Angka 38% hanya mengukur gate keluar-Draft Jilid 1.

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
| Validasi ilmiah, ahli, asesmen, dan pilot | 15% | 22% | 3,3% |
| Produksi dan rilis final | 10% | 15% | 1,5% |
| **Total mentah** | **100%** |  | **31,74%** |
| **Nilai laporan dibulatkan** |  |  | **32%** |

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
- DEC-CUR-001–005;
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

### D. Validasi ilmiah/ahli/pilot — 22%

Sudah tersedia:

- protokol dan paket review;
- rubrik serta form bukti Bahasa Arab;
- rubrik, form, paket ahli, dan audit keterlacakan Tahfidz;
- register blocker dan gate;
- keputusan Pemilik Akademik untuk kandidat Tahfidz melalui DEC-CUR-004;
- keputusan arah integrasi Bahasa Arab melalui DEC-CUR-005;
- paket pengiriman validasi ahli terintegrasi DSP-VAL-QJ1-001.

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
| 3 | Keputusan materi khusus | COMPLETE — DEC-CUR-004 dan DEC-CUR-005 |
| 4 | Review akademik/Arab/Qira’at | OPEN |
| 5 | Review editorial dan render | OPEN |
| 6 | Validasi asesmen dan safeguarding | OPEN |
| 7 | Otorisasi dan audit trail | OPEN |
| 8 | Penutupan seluruh blocker | OPEN |

Kesiapan Jilid 1 keluar-Draft sekarang **38% (3 dari 8 gate)**. Gate 3 selesai karena arah materi khusus sudah diputuskan oleh Pemilik Akademik. Materi tetap belum aktif karena validasi ahli berada pada Gate 4 dan Evidence-ID belum tersedia.

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

Jalur tercepat yang sah dari 32%:

1. menyelesaikan review ahli Tahfidz/Qira’at, Bahasa Arab, dan ortografi ءُ;
2. menyelesaikan review akademik, editorial, asesmen, serta safeguarding Jilid 1;
3. memperoleh Evidence-ID dan menanam hasil tervalidasi ke P018, P028, P036, register, dan PDF;
4. menyusun master hadis akhlak sahih dan progression Tahfidz Jilid 1–8;
5. membentuk struktur halaman formal Jilid 2;
6. menjalankan pilot Jilid 1 dan menerapkan koreksi;
7. mengulang pipeline terkendali untuk Jilid 2–8.

### Target angka terdekat

| Target | Syarat utama |
|---|---|
| **35% keseluruhan** | sebagian keputusan ahli dan Evidence-ID material tersedia; atau struktur formal Jilid 2 mulai terbentuk |
| **50% kesiapan keluar-Draft Jilid 1** | Gate 4 review akademik/Arab/Qira’at selesai |
| **63% kesiapan keluar-Draft Jilid 1** | Gate 5 editorial dan render final selesai |
| **100% kesiapan keluar-Draft Jilid 1** | seluruh 8 gate dan semua blocker ditutup |

## 8. Riwayat

| Versi | Tanggal | Ringkasan |
|---|---|---|
| 0.3.0-id | 29 Juli 2026 | DEC-CUR-004 dan DEC-CUR-005 menutup Gate 3 keputusan materi khusus; kesiapan keluar-Draft naik 25%→38%, validasi domain naik 20%→22%, total mentah 31,74% dan laporan 32% |
| 0.2.0-id | 29 Juli 2026 | Progression dan register Hadis Akhlak menambah ketercapaian arsitektur menjadi 65%; total mentah 31,44%, laporan 31% |
| 0.1.0-id | 28 Juli 2026 | Baseline berbobot pertama: progres keseluruhan 30%, kesiapan keluar-Draft Jilid 1 25% |