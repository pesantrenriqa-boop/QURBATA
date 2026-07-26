# QC-002 — Standar Penomoran dan Pengkodean Dokumen

**Kode Dokumen:** QC-002  
**Judul:** Standar Penomoran dan Pengkodean Dokumen QURBATA  
**Bahasa Induk:** Bahasa Indonesia  
**Status:** Draf Normatif  
**Versi:** 0.2.0-id  
**Pemilik Dokumen:** Fungsi Tata Kelola QURBATA  
**Otoritas Persetujuan:** Pendiri dan Peneliti Utama/Dewan Konstitusi setelah aktif  
**Tanggal Berlaku:** Setelah persetujuan sesuai kewenangan  
**Tinjauan Berikutnya:** Maksimal tiga tahun setelah berlaku atau ketika dipicu perubahan material  
**Klasifikasi Akses:** Publik  
**Induk Normatif:** QC-000 — Konstitusi QURBATA  


**Kode Dokumen:** QC-002  
**Judul:** Standar Penomoran dan Pengkodean Dokumen QURBATA  
**Bahasa Induk:** Bahasa Indonesia  
**Status:** Draf Normatif  
**Versi:** 0.1.0-id  
**Induk Normatif:** QC-000 — Konstitusi QURBATA  
**Dokumen Terkait:** QC-001 — Governance Architecture

---

## 1. Tujuan

Standar ini menetapkan tata cara pemberian kode, nomor, nama berkas, versi, status, bahasa, dan hubungan antar dokumen dalam ekosistem QURBATA agar setiap dokumen:

1. dapat dikenali secara unik;
2. mudah ditelusuri asal, fungsi, pemilik, dan versinya;
3. tidak mengalami duplikasi kode atau benturan kewenangan;
4. dapat dihubungkan dengan kebijakan, SOP, modul RIQA OS, basis data, dan bukti audit;
5. tetap konsisten pada seluruh bahasa, unit, dan media publikasi.

---

## 2. Ruang Lingkup

Standar ini berlaku untuk seluruh dokumen resmi QURBATA, termasuk:

- konstitusi dan kebijakan induk;
- manual tata kelola;
- standar akademik dan kurikulum;
- kebijakan peserta didik dan pengembangan manusia;
- kebijakan SDM;
- kebijakan keuangan dan aset;
- kebijakan informasi, data, keamanan, dan sistem digital;
- dokumen penjaminan mutu;
- SOP, instruksi kerja, formulir, register, dan rekaman;
- spesifikasi produk, buku, aplikasi, basis data, dan integrasi;
- dokumen audit, evaluasi, tindakan korektif, dan peningkatan berkelanjutan.

---

## 3. Prinsip Dasar

### 3.1 Keunikan

Setiap dokumen resmi wajib mempunyai satu kode unik. Satu kode tidak boleh dipakai untuk dua dokumen yang berbeda.

### 3.2 Ketetapan

Kode dokumen tidak berubah hanya karena judul, struktur, penanggung jawab, atau isi dokumen direvisi. Perubahan mendasar yang mengubah fungsi normatif dapat menghasilkan kode baru melalui proses legislasi dokumen.

### 3.3 Keterlacakan

Setiap dokumen wajib dapat ditelusuri kepada:

- dokumen induk;
- dokumen turunan;
- pemilik dokumen;
- status persetujuan;
- versi yang berlaku;
- riwayat perubahan;
- objek implementasi;
- bukti audit.

### 3.4 Bahasa Induk

Bahasa Indonesia merupakan bahasa induk normatif. Versi bahasa Inggris dan bahasa Arab adalah terjemahan resmi yang harus mempertahankan kode dokumen yang sama dengan penanda bahasa berbeda.

### 3.5 Keterbacaan Mesin

Nama berkas, metadata, dan kode harus dapat dibaca manusia serta diproses oleh RIQA OS, sistem pencarian, otomasi, dan mesin audit.

---

## 4. Struktur Kode Dokumen

Format dasar kode dokumen adalah:

```text
[PREFIX]-[NOMOR]
```

Contoh:

```text
QC-000
QC-200
SOP-ACA-001
FRM-FIN-004
REG-HR-002
```

Untuk dokumen turunan yang memerlukan domain dan nomor urut, digunakan format:

```text
[JENIS]-[DOMAIN]-[NOMOR]
```

Untuk dokumen yang mempunyai bagian terpisah, dapat digunakan sufiks bagian:

```text
[JENIS]-[DOMAIN]-[NOMOR]-[BAGIAN]
```

Contoh:

```text
CUR-QJ1-001
SOP-ACA-003-A
SPEC-OS-012
```

---

## 5. Kelompok Kode Utama

### 5.1 Seri QC

Seri `QC` digunakan untuk konstitusi, arsitektur tata kelola, manual kebijakan, dan standar pengendalian tingkat organisasi.

| Rentang | Kelompok Dokumen |
|---|---|
| QC-000–QC-099 | Konstitusi, arsitektur, legislasi, terminologi, dan pengendalian dokumen |
| QC-100–QC-199 | Visi, strategi, kelembagaan, dan tata kelola pimpinan |
| QC-200–QC-299 | Tata kelola akademik, kurikulum, pembelajaran, asesmen, dan sertifikasi |
| QC-300–QC-399 | Peserta didik, perlindungan, adab, kesejahteraan, dan pengembangan manusia |
| QC-400–QC-499 | SDM, guru, pengurus, karier, kompetensi, dan kinerja |
| QC-500–QC-599 | Keuangan, pembayaran, aset, pengadaan, dan keberlanjutan ekonomi |
| QC-600–QC-699 | Informasi, data, privasi, keamanan, teknologi, dan RIQA OS |
| QC-700–QC-799 | Penjaminan mutu, evaluasi, akreditasi, dan kepatuhan |
| QC-800–QC-899 | Kerangka SOP, layanan operasional, dan pengendalian pelaksanaan |
| QC-900–QC-999 | Audit, insiden, tindakan korektif, risiko, dan peningkatan berkelanjutan |

### 5.2 Kode Jenis Dokumen Turunan

| Kode | Jenis Dokumen |
|---|---|
| `POL` | Kebijakan khusus |
| `MAN` | Manual |
| `STD` | Standar |
| `SOP` | Prosedur Operasional Standar |
| `WI` | Instruksi Kerja |
| `CUR` | Kurikulum atau struktur pembelajaran |
| `SYL` | Silabus |
| `MOD` | Modul pembelajaran |
| `ASM` | Instrumen asesmen |
| `RUB` | Rubrik penilaian |
| `FRM` | Formulir |
| `REG` | Register atau daftar kendali |
| `REC` | Rekaman atau bukti pelaksanaan |
| `SPEC` | Spesifikasi sistem, produk, data, atau integrasi |
| `ADR` | Catatan keputusan arsitektur |
| `API` | Kontrak antarmuka aplikasi |
| `DB` | Skema atau kamus data |
| `REP` | Laporan |
| `AUD` | Dokumen audit |
| `CAPA` | Tindakan korektif dan pencegahan |
| `RSK` | Register risiko |
| `TMP` | Templat |

---

## 6. Kode Domain

Domain menunjukkan wilayah fungsi utama dokumen.

| Kode | Domain |
|---|---|
| `GOV` | Tata kelola dan kelembagaan |
| `STR` | Strategi dan perencanaan |
| `ACA` | Akademik |
| `CUR` | Kurikulum |
| `LRN` | Pembelajaran |
| `ASM` | Asesmen dan ujian |
| `CRT` | Sertifikasi |
| `STD` | Peserta didik atau santri |
| `PRT` | Perlindungan dan keselamatan |
| `HR` | Sumber daya manusia |
| `FIN` | Keuangan |
| `AST` | Aset dan fasilitas |
| `PRC` | Pengadaan |
| `DAT` | Data dan informasi |
| `SEC` | Keamanan informasi |
| `OS` | RIQA OS dan aplikasi |
| `INT` | Integrasi sistem |
| `QA` | Penjaminan mutu |
| `AUD` | Audit dan kepatuhan |
| `RSK` | Risiko |
| `PUB` | Publikasi dan penerbitan |
| `RSC` | Riset dan pengembangan |
| `COM` | Komunikasi dan hubungan publik |

Kode domain baru hanya dapat ditetapkan melalui pengelola dokumen resmi dan harus dicatat dalam register terminologi.

---

## 7. Penomoran

1. Nomor menggunakan tiga digit, dimulai dari `001`, kecuali dokumen induk khusus yang menggunakan nomor `000`.
2. Nomor diberikan secara berurutan dalam kelompok atau domain yang sama.
3. Nomor dokumen yang dibatalkan tidak boleh dipakai kembali.
4. Nomor yang dicadangkan harus dicatat dalam register kendali dokumen.
5. Dokumen terjemahan tidak memperoleh nomor baru.
6. Lampiran yang tidak berdiri sendiri mengikuti kode dokumen induk dan nomor lampiran.

Contoh:

```text
SOP-ACA-001
SOP-ACA-002
FRM-ACA-001
FRM-ACA-002
```

---

## 8. Struktur Nama Berkas

Format nama berkas resmi:

```text
[KODE]-[Judul-Ringkas].[ekstensi]
```

Untuk versi bahasa:

```text
[KODE]-[Judul-Ringkas].[bahasa].[ekstensi]
```

Kode bahasa yang digunakan:

- `id` — Bahasa Indonesia;
- `en` — Academic English;
- `ar` — Bahasa Arab formal.

Contoh:

```text
QC-002-Standar-Penomoran-dan-Pengkodean-Dokumen.md
QC-002-Document-Numbering-and-Coding-Standard.en.md
QC-002-Miyar-Tarqim-wa-Tarmiz-al-Wathaiq.ar.md
```

Ketentuan nama berkas:

1. gunakan huruf Latin, angka, dan tanda hubung;
2. hindari spasi, garis miring, tanda tanya, dan karakter yang tidak portabel;
3. nama berkas tidak memuat nomor versi;
4. nomor versi dicatat dalam metadata dokumen dan riwayat Git;
5. judul ringkas harus tetap dapat dikenali tanpa membuka berkas.

---

## 9. Pengendalian Versi

QURBATA menggunakan pola versi semantik dokumen:

```text
MAYOR.MINOR.PATCH-bahasa
```

Contoh:

```text
1.0.0-id
1.1.0-id
1.1.1-id
```

### 9.1 Perubahan Mayor

Nomor mayor berubah apabila terdapat:

- perubahan mandat atau fungsi utama dokumen;
- perubahan besar struktur normatif;
- perubahan yang berdampak luas terhadap banyak kebijakan, SOP, atau modul sistem;
- penggantian dokumen lama dengan kerangka yang secara substansial baru.

### 9.2 Perubahan Minor

Nomor minor berubah apabila terdapat:

- penambahan pasal, bagian, aturan, indikator, atau tanggung jawab;
- perluasan ruang lingkup tanpa mengganti mandat utama;
- perubahan implementasi yang memerlukan penyesuaian SOP atau sistem.

### 9.3 Perubahan Patch

Nomor patch berubah untuk:

- koreksi ejaan;
- perbaikan rujukan;
- klarifikasi redaksional tanpa mengubah makna normatif;
- penyesuaian format dan metadata.

---

## 10. Status Dokumen

Setiap dokumen wajib menggunakan salah satu status berikut:

| Status | Makna |
|---|---|
| `Konsep` | Gagasan awal; belum menjadi draf resmi |
| `Draf` | Sedang disusun; belum berlaku |
| `Dalam Review` | Sedang diperiksa oleh pihak berwenang |
| `Disetujui` | Telah disahkan dan siap diberlakukan |
| `Berlaku` | Menjadi acuan resmi aktif |
| `Ditangguhkan` | Pemberlakuan dihentikan sementara |
| `Dicabut` | Tidak berlaku lagi karena keputusan resmi |
| `Digantikan` | Tidak berlaku dan telah mempunyai dokumen pengganti |
| `Arsip` | Dipertahankan sebagai rekaman historis |

Draf tidak boleh digunakan sebagai dasar keputusan operasional final kecuali terdapat persetujuan sementara yang terdokumentasi.

---

## 11. Metadata Wajib

Setiap dokumen normatif sekurang-kurangnya memuat:

- kode dokumen;
- judul resmi;
- versi;
- bahasa;
- status;
- pemilik dokumen;
- penyusun;
- pemeriksa;
- pengesah;
- tanggal berlaku;
- tanggal review berikutnya;
- dokumen induk;
- dokumen terkait;
- klasifikasi akses;
- ringkasan perubahan.

Untuk dokumen digital, metadata tersebut harus tersedia dalam isi berkas atau format data terstruktur yang dapat dibaca RIQA OS.

---

## 12. Hubungan Dokumen

Hubungan antar dokumen menggunakan tipe berikut:

| Tipe | Makna |
|---|---|
| `INDUK-DARI` | Dokumen menjadi dasar langsung dokumen lain |
| `TURUNAN-DARI` | Dokumen diturunkan dari dokumen yang lebih tinggi |
| `MERUJUK` | Dokumen menggunakan ketentuan dokumen lain |
| `MENGIMPLEMENTASIKAN` | SOP, sistem, atau modul melaksanakan ketentuan normatif |
| `MENGGANTIKAN` | Dokumen menggantikan dokumen lama |
| `BUKTI-UNTUK` | Rekaman menjadi bukti pelaksanaan atau kepatuhan |
| `DIUJI-OLEH` | Dokumen atau kontrol diperiksa melalui audit tertentu |

Setiap hubungan yang bersifat normatif wajib dicatat dalam matriks keterlacakan.

---

## 13. Pengkodean Implementasi RIQA OS

Setiap fitur utama RIQA OS wajib mempunyai identitas implementasi yang dapat ditautkan kepada dokumen QC, SOP, dan skema data.

Format yang disarankan:

```text
OS-[DOMAIN]-[NOMOR]
```

Contoh:

```text
OS-ACA-001  Profil Peserta
OS-ASM-001  Pengelolaan Ujian
OS-CRT-001  Penerbitan Sertifikat
OS-FIN-001  Pencatatan Pembayaran
OS-HR-001   Profil dan Karier SDM
```

Setiap identitas implementasi sekurang-kurangnya harus mencatat:

- pasal atau kebijakan sumber;
- SOP pelaksana;
- peran yang berwenang;
- data yang diproses;
- kontrol akses;
- bukti transaksi atau log;
- kriteria penerimaan;
- pengujian kepatuhan.

Kode implementasi bukan pengganti kode dokumen. Kode tersebut berfungsi sebagai penghubung antara tata kelola dan perangkat lunak.

---

## 14. Pengkodean Produk Buku QURBATA

Untuk produk buku dan materi pembelajaran QURBATA, format kode unit isi adalah:

```text
QJ[JILID]-P[HALAMAN]
```

Contoh:

```text
QJ1-P001
QJ1-P040
QJ2-P001
```

Apabila diperlukan identitas latihan atau objek di dalam halaman, digunakan format:

```text
QJ[JILID]-P[HALAMAN]-[JENIS][NOMOR]
```

Contoh:

```text
QJ1-P001-L01
QJ1-P001-ASM01
QJ1-P001-AUD01
```

Keterangan:

- `L` — latihan;
- `ASM` — asesmen;
- `AUD` — audio;
- `IMG` — gambar;
- `VID` — video;
- `VOC` — mufradat atau kosakata;
- `MEM` — hafalan;
- `AKH` — materi akhlak.

Kode isi wajib dipertahankan pada buku, spreadsheet sumber, presentasi, flashcard, audio, asesmen, dan integrasi RIQA OS.

---

## 15. Larangan

Dilarang:

1. membuat dokumen resmi tanpa kode;
2. mengganti kode dokumen yang sudah berlaku tanpa keputusan resmi;
3. menggunakan satu kode untuk lebih dari satu fungsi;
4. menerbitkan terjemahan dengan nomor berbeda dari dokumen induknya;
5. menghapus versi lama yang wajib dipertahankan sebagai arsip;
6. mengubah status menjadi berlaku tanpa otorisasi;
7. memasukkan nomor versi ke dalam nama berkas resmi;
8. memakai kode sementara dalam sistem produksi tanpa pemetaan ke register resmi.

---

## 16. Tanggung Jawab

### 16.1 Pemilik Dokumen

Pemilik dokumen bertanggung jawab atas ketepatan isi, relevansi, review berkala, dan usulan perubahan.

### 16.2 Pengelola Dokumen

Pengelola dokumen bertanggung jawab atas:

- pemberian kode dan nomor;
- pemeriksaan metadata;
- pencegahan duplikasi;
- pengelolaan register;
- publikasi versi yang berlaku;
- pengarsipan versi lama;
- pemeliharaan matriks keterlacakan.

### 16.3 Pengelola Sistem

Pengelola RIQA OS bertanggung jawab memastikan kode dokumen, kode fitur, skema data, log, dan bukti audit tetap saling terhubung.

### 16.4 Seluruh Unit

Setiap unit wajib menggunakan versi dokumen yang berstatus berlaku dan melaporkan dokumen tidak terkendali atau kode yang bertabrakan.

---

## 17. Register Kendali Dokumen

Register kendali dokumen sekurang-kurangnya memuat:

| Elemen | Keterangan |
|---|---|
| Kode | Identitas unik dokumen |
| Judul | Judul resmi |
| Jenis | QC, SOP, FRM, SPEC, dan lainnya |
| Domain | Bidang fungsi |
| Versi | Versi aktif |
| Status | Status dokumen |
| Pemilik | Unit atau jabatan penanggung jawab |
| Lokasi | Path repository atau lokasi resmi |
| Induk | Dokumen sumber |
| Pengganti | Dokumen pengganti bila ada |
| Tanggal Berlaku | Awal pemberlakuan |
| Review Berikutnya | Jadwal peninjauan |
| Klasifikasi | Publik, internal, terbatas, atau rahasia |

Register resmi harus menjadi sumber tunggal status dokumen.

---

## 18. Ketentuan Peralihan

1. Dokumen lama yang belum mempunyai kode harus diinventarisasi dan diberi kode secara bertahap.
2. Kode lama dapat dicatat sebagai alias untuk menjaga keterlacakan.
3. Dokumen yang isinya tumpang tindih harus diaudit sebelum digabungkan, dicabut, atau digantikan.
4. Selama masa transisi, repository QURBATA menjadi sumber utama dokumen kerja, sedangkan status pemberlakuan tetap mengikuti keputusan pengesahan resmi.
5. QC-002 menjadi acuan penamaan bagi seluruh dokumen baru setelah tanggal penerbitannya.

---

## 19. Kriteria Kepatuhan

Suatu dokumen dinilai patuh apabila:

- mempunyai kode unik;
- mengikuti format nama berkas;
- mempunyai metadata wajib;
- menggunakan versi dan status yang sah;
- tercatat dalam register kendali;
- mempunyai hubungan induk dan turunan yang jelas;
- dapat ditelusuri ke implementasi serta bukti pelaksanaan apabila relevan;
- tidak bertentangan dengan QC-000 dan dokumen yang lebih tinggi.

---

## 20. Riwayat Perubahan

| Versi | Status | Ringkasan |
|---|---|---|
| 0.1.0-id | Draf Normatif | Pembentukan standar awal penomoran, pengkodean, versi, status, metadata, dan keterlacakan dokumen QURBATA |
