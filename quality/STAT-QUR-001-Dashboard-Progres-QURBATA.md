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
| Progres keseluruhan QURBATA menuju 100% | **42%** |
| Kesiapan Jilid 1 keluar-Draft | **38% — 3 dari 8 gate makro** |
| Governance QURBATA v1.0 | **100% untuk baseline yang telah diratifikasi** |
| Buku dengan sumber halaman lengkap | **1 dari 8 jilid**; master formal seluruh Jilid 1–8 tersedia |
| Halaman buku formal tersedia | **40 halaman Jilid 1** |
| Jilid 2–8 dengan halaman formal | **7 dari 7 master tersedia; isi nyata Jilid 2: 15/40, total 15/280** |

Angka 42% tidak boleh dibaca sebagai “Jilid 1 sudah 42%”. Angka itu adalah gabungan berbobot seluruh proyek 8 jilid. Angka 38% hanya mengukur gate keluar-Draft Jilid 1.

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
| Arsitektur kurikulum lintas jilid | 20% | 90% | 18,0% |
| Isi buku Jilid 1–8 | 45% | 20,9375% | 9,422% |
| Validasi ilmiah, ahli, asesmen, dan pilot | 15% | 22% | 3,3% |
| Produksi dan rilis final | 10% | 15% | 1,5% |
| **Total mentah** | **100%** |  | **42,222%** |
| **Nilai laporan dibulatkan** |  |  | **42%** |

### Rumus domain buku

Domain buku mempunyai bobot terbesar karena produk utama QURBATA adalah delapan jilid buku.

```text
Ketercapaian domain buku
= (ketercapaian Jilid 1 + ... + ketercapaian Jilid 8) / 8
= (70% + 37,5% + 10% + 10% + 10% + 10% + 10% + 10%) / 8
= 20,9375%
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

### B. Arsitektur kurikulum lintas jilid — 90%

Sudah tersedia:

- model PO/LO/KO/BO/CUR dan register objek;
- DEC-CUR-001–005;
- Arabic Competency Progression;
- baseline 640 lema Jilid 1–8;
- register kosa kata, kalimat, teks, dan siklus;
- mapping Bahasa Arab Jilid 1;
- mapping dan kontrol Tahfidz Jilid 1;
- prinsip murojaah kumulatif;
- HCP-QUR-001 dan REG-HAD-001 sebagai progression serta sumber tunggal Hadis Akhlak Jilid 1–8 (belum berisi objek aktif);
- RCP-QUR-001 sebagai progression baca dan tajwid formal Jilid 1–8;
- QJ2-MASTER–QJ8-MASTER sebagai struktur formal masing-masing 40 halaman Jilid 2–8;
- seluruh delapan jilid sekarang mempunyai outcome, dependency, cakupan, peta 40 halaman, gate, dan blocker formal.

Masih belum lengkap:

- mapping Tahfidz Jilid 2–8;
- inventaris Hadith-ID nyata, takhrij, terjemah, mapping halaman, dan validasi ahli atas hadis akhlak Jilid 1–8;
- pembagian final Bahasa Arab Jilid 2–8;
- aturan kenaikan jilid lintas-strand yang tervalidasi.

### C. Isi buku Jilid 1–8 — 20,9375%

| Jilid | Status isi formal | Estimasi internal |
|---:|---|---:|
| 1 | 40 halaman sumber, audit, mapping, dan prototipe tersedia; tetap Draft | 70% |
| 2 | QJ2-P001–P015 dan 360 latihan tersedia; P016–P017 diblokir gate ortografi tanwin | 37,5% |
| 3 | master formal 40 halaman tersedia; isi nyata halaman belum diproduksi | 10% |
| 4 | master formal 40 halaman tersedia; isi nyata halaman belum diproduksi | 10% |
| 5 | master formal 40 halaman tersedia; isi nyata halaman belum diproduksi | 10% |
| 6 | master formal 40 halaman tersedia; isi nyata halaman belum diproduksi | 10% |
| 7 | master formal 40 halaman tersedia; isi nyata halaman belum diproduksi | 10% |
| 8 | master formal 40 halaman tersedia; isi nyata halaman belum diproduksi | 10% |

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

Jalur tercepat yang sah dari 42%:

1. menyelesaikan review ahli Tahfidz/Qira’at, Bahasa Arab, dan ortografi ءُ;
2. menyelesaikan review akademik, editorial, asesmen, serta safeguarding Jilid 1;
3. memperoleh Evidence-ID dan menanam hasil tervalidasi ke P018, P028, P036, register, dan PDF;
4. menyusun master hadis akhlak sahih dan progression Tahfidz Jilid 1–8;
5. memproduksi sumber nyata QJ2-P001–QJ2-P040 dari QJ2-MASTER;
6. membentuk LO/KO, whitelist, Source-ID, dan isi nyata secara berurutan mulai QJ2-P001;
7. menjalankan pilot Jilid 1 dan menerapkan koreksi;
8. mengulang pipeline audit, validasi, render, dan produksi sampai Jilid 8.

### Target angka terdekat

| Target | Syarat utama |
|---|---|
| **45% keseluruhan** | isi nyata batch awal Jilid 2, LO/KO, whitelist, dan audit distribusi tersedia; atau Evidence-ID material Jilid 1 menutup gate validasi |
| **50% kesiapan keluar-Draft Jilid 1** | Gate 4 review akademik/Arab/Qira’at selesai |
| **63% kesiapan keluar-Draft Jilid 1** | Gate 5 editorial dan render final selesai |
| **100% kesiapan keluar-Draft Jilid 1** | seluruh 8 gate dan semua blocker ditutup |

## 8. Riwayat

| Versi | Tanggal | Ringkasan |
|---|---|---|
| 0.18.0-id | 29 Juli 2026 | Peta P016–P021 selesai dan lulus audit distribusi 44:44; progres tetap 42% karena halaman masih tertahan Evidence-ID |
| 0.17.0-id | 29 Juli 2026 | Audit otomatis 24 lema/72 bentuk tanwin lulus dan paket ahli siap; progres tetap 42% sampai Evidence-ID tersedia |
| 0.16.0-id | 29 Juli 2026 | WLT-QJ2-TAN-001 menghasilkan 24 kata nyata dan 72 bentuk tanwin kandidat; progres tetap 42% karena verifikasi ahli/Utsmani belum menutup P016 |
| 0.15.0-id | 29 Juli 2026 | DEC-CUR-009 dikoreksi: setiap halaman empat-huruf diawali 8 tangga tiga-huruf, lalu 16 tangga empat-huruf; progres tetap 42% |
| 0.14.0-id | 29 Juli 2026 | DEC-CUR-009 menetapkan transisi kata empat huruf mulai tanwin; progres tetap 42% karena isi P016 masih menunggu whitelist ortografi |
| 0.13.0-id | 29 Juli 2026 | Koreksi DEC-CUR-008 diterapkan pada QJ2-P001–P015: tidak ada lagi tangga dua huruf; 1.080 token lulus audit, progres tetap 42% karena pekerjaan ulang |
| 0.12.0-id | 29 Juli 2026 | Regenerasi korektif QJ2-P001–P015 lulus audit 50:50 dan cakupan 29 identitas; progres tetap 42% karena pekerjaan ulang menjaga integritas baseline |
| 0.11.0-id | 29 Juli 2026 | P014–P015 menyelesaikan integrasi posisi; BLK-QJ2-ORTHO-001 mencegah contoh tanwin keliru; 360 latihan lulus audit, total mentah 42,222%, laporan 42% |
| 0.10.0-id | 29 Juli 2026 | QJ2-P011–P013 melengkapi keluarga huruf utama; 312 latihan/sampel lulus audit kumulatif, domain isi menjadi 20,3125%, total mentah 41,941%, laporan tetap 42% |
| 0.9.0-id | 29 Juli 2026 | Siklus pertama Jilid 2 ditutup sampai QJ2-P010; 240 latihan/sampel lulus checkpoint struktur, domain isi menjadi 19,375%, total mentah 41,519%, laporan 42% |
| 0.8.0-id | 29 Juli 2026 | Isi nyata Jilid 2 diperluas sampai QJ2-P006; 144 latihan lulus audit struktur kumulatif, domain isi menjadi 18,125%, total mentah 40,956%, laporan tetap 41% |
| 0.7.0-id | 29 Juli 2026 | Produksi isi nyata Jilid 2 dimulai: QJ2-P001–P003, 72 latihan, dan AUD-QJ2-CONTENT-001; domain isi menjadi 17,8125%, total mentah 40,816%, laporan tetap 41% |
| 0.6.0-id | 29 Juli 2026 | QJ5-MASTER–QJ8-MASTER menutup struktur formal seluruh delapan jilid; arsitektur naik 75%→90%, domain isi menjadi 17,5%, total mentah 40,675%, laporan 41% |
| 0.5.0-id | 29 Juli 2026 | QJ3-MASTER dan QJ4-MASTER membentuk struktur formal masing-masing 40 halaman; arsitektur naik 70%→75%, domain isi menjadi 12,5%, total mentah 35,425%, laporan 35% |
| 0.4.0-id | 29 Juli 2026 | RCP-QUR-001 menetapkan progression baca/tajwid Jilid 1–8 dan QJ2-MASTER membentuk struktur formal 40 halaman Jilid 2; arsitektur naik 65%→70%, domain isi menjadi 10%, total mentah 33,3%, laporan 33% |
| 0.3.0-id | 29 Juli 2026 | DEC-CUR-004 dan DEC-CUR-005 menutup Gate 3 keputusan materi khusus; kesiapan keluar-Draft naik 25%→38%, validasi domain naik 20%→22%, total mentah 31,74% dan laporan 32% |
| 0.2.0-id | 29 Juli 2026 | Progression dan register Hadis Akhlak menambah ketercapaian arsitektur menjadi 65%; total mentah 31,44%, laporan 31% |
| 0.1.0-id | 28 Juli 2026 | Baseline berbobot pertama: progres keseluruhan 30%, kesiapan keluar-Draft Jilid 1 25% |