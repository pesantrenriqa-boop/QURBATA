# REG-GOV-001 — Register Knowledge-ID QURBATA

**Kode Dokumen:** REG-GOV-001  
**Judul:** Register Knowledge-ID QURBATA  
**Bahasa Induk:** Bahasa Indonesia  
**Status:** Draf Terkendali  
**Versi:** 0.2.0-id  
**Induk Normatif:** QC-000 — Konstitusi QURBATA  
**Dokumen Pengendali:** QC-002, QC-003, QC-004, QC-005  

---

## 1. Tujuan

Register ini menetapkan pola resmi Knowledge-ID untuk mengidentifikasi secara unik setiap prinsip, persyaratan, definisi, keputusan, kontrol, bukti, risiko, tindakan, dan objek pengetahuan dalam ekosistem QURBATA.

Knowledge-ID digunakan agar ketentuan dapat:

1. dirujuk tanpa bergantung pada nomor halaman;
2. ditelusuri dari konstitusi menuju dokumen pelaksana dan bukti;
3. diproses oleh RIQA OS dan alat audit;
4. dipertahankan lintas versi dan bahasa;
5. diperiksa duplikasi, kehilangan hubungan, dan perubahan dampaknya; dan
6. digunakan sebagai sumber tunggal untuk buku, kurikulum, asesmen, aplikasi, laporan, serta produk turunan.

## 2. Prinsip Pengendalian

1. Setiap Knowledge-ID harus unik dalam seluruh ekosistem QURBATA.
2. Satu Knowledge-ID hanya mewakili satu objek pengetahuan utama.
3. Knowledge-ID tidak berubah hanya karena redaksi, nomor bagian, lokasi berkas, atau bahasa berubah.
4. Knowledge-ID tidak boleh digunakan kembali setelah objek dicabut.
5. Objek yang berubah makna secara material harus memperoleh Knowledge-ID baru.
6. Hubungan pengganti, gabungan, pecahan, atau pencabutan harus dicatat.
7. Bahasa Indonesia menjadi sumber makna pengendali sampai terjemahan resmi diratifikasi.
8. Nomor ID tidak memiliki makna urutan prioritas atau tingkat kewenangan kecuali dinyatakan terpisah.

## 3. Format Knowledge-ID

Format umum:

```text
KID-[DOMAIN]-[TYPE]-[NNN]
```

Keterangan:

- `KID` — penanda Knowledge-ID;
- `DOMAIN` — domain pengetahuan;
- `TYPE` — jenis objek pengetahuan;
- `NNN` — nomor unik tiga digit dalam kombinasi domain dan jenis.

Contoh:

```text
KID-GOV-PRN-001
KID-DOC-REQ-004
KID-SAFE-CTL-012
KID-RSK-RSK-003
KID-OS-SPEC-021
```

## 4. Kode Domain Knowledge-ID

| Kode | Domain |
|---|---|
| `CON` | Konstitusi dan identitas tertinggi |
| `GOV` | Tata kelola, kewenangan, keputusan, dan akuntabilitas |
| `DOC` | Dokumen, versi, kode, terminologi, dan keterlacakan |
| `ACA` | Akademik dan penyelenggaraan pendidikan |
| `CUR` | Kurikulum dan struktur kompetensi |
| `LRN` | Pembelajaran dan pengalaman belajar |
| `ASM` | Asesmen, ujian, rubrik, dan kelulusan |
| `SAFE` | Perlindungan peserta didik, keselamatan, dan kesejahteraan |
| `HR` | SDM, kompetensi, karier, dan kinerja |
| `FIN` | Keuangan, pembayaran, aset, dan pengadaan |
| `DAT` | Data, privasi, retensi, dan informasi |
| `SEC` | Keamanan informasi dan kontrol akses |
| `OS` | RIQA OS, aplikasi, basis data, API, dan integrasi |
| `RSK` | Risiko, insiden, krisis, keberlangsungan, dan pemulihan |
| `QA` | Mutu, audit, evaluasi, dan peningkatan |
| `PUB` | Publikasi, penerbitan, lisensi, dan kekayaan intelektual |
| `RSC` | Riset dan pengembangan |
| `CMR` | Komunikasi dan hubungan pemangku kepentingan |
| `CMP` | Kompetensi dan struktur kompetensi |

Kode domain harus selaras dengan QC-002. Penambahan domain baru memerlukan persetujuan pengelola dokumen dan pencatatan dalam QC-005.

## 5. Kode Jenis Objek

| Kode | Jenis Objek |
|---|---|
| `PRN` | Prinsip |
| `REQ` | Persyaratan normatif |
| `DEF` | Definisi resmi |
| `ROL` | Peran atau tanggung jawab |
| `DEC` | Keputusan atau kaidah pengambilan keputusan |
| `CTL` | Kontrol atau pengendalian |
| `PROC` | Proses |
| `RULE` | Aturan operasional |
| `IND` | Indikator |
| `OUT` | Hasil atau keluaran |
| `EVD` | Bukti atau rekaman |
| `RSK` | Risiko |
| `INC` | Insiden |
| `ACT` | Tindakan atau tindak lanjut |
| `SPEC` | Spesifikasi |
| `DATA` | Elemen atau objek data |
| `TERM` | Istilah terkelola |
| `MAP` | Hubungan atau pemetaan |
| `KO` | Knowledge Object |
| `LO` | Learning Object |
| `PO` | Page Object |
| `CO` | Chapter Object |
| `BO` | Book Object |
| `CUR` | Curriculum Object |

## 6. Status Knowledge-ID

Setiap entri menggunakan salah satu status berikut:

| Status | Makna |
|---|---|
| `PROPOSED` | Diusulkan dan belum disetujui |
| `ACTIVE-DRAFT` | Berlaku dalam dokumen draf terkendali |
| `ACTIVE` | Telah disetujui atau diratifikasi |
| `SUPERSEDED` | Digantikan oleh Knowledge-ID lain |
| `RETIRED` | Dicabut dan tidak lagi digunakan |
| `RESERVED` | Dicadangkan dan belum boleh digunakan |

Knowledge-ID berstatus `SUPERSEDED` atau `RETIRED` tidak boleh dihapus dari register.

## 7. Metadata Minimum Entri

Setiap entri sekurang-kurangnya memuat:

- Knowledge-ID;
- nama objek;
- jenis objek;
- domain;
- definisi atau ringkasan makna;
- dokumen sumber;
- bagian atau lokasi sumber;
- status;
- versi pertama;
- pemilik;
- otoritas persetujuan;
- tanggal berlaku;
- bahasa induk;
- hubungan induk, turunan, pendukung, pengganti, atau bukti;
- objek implementasi RIQA OS;
- tingkat kritikalitas;
- tanggal peninjauan; dan
- catatan perubahan.

## 8. Aturan Pemberian Nomor

1. Nomor dimulai dari `001` dalam setiap kombinasi domain dan jenis.
2. Nomor diberikan berurutan oleh register resmi.
3. Nomor yang telah digunakan tidak boleh dipakai kembali.
4. Nomor yang dicadangkan harus berstatus `RESERVED`.
5. Pembuatan ID manual di luar register dilarang untuk dokumen final.
6. Perubahan bahasa tidak menghasilkan Knowledge-ID baru.
7. Pemindahan isi antar-dokumen tidak menghasilkan ID baru selama makna tidak berubah.
8. Penggabungan beberapa objek menjadi satu objek material memerlukan ID baru dan hubungan `replaces`.
9. Pemecahan satu objek menjadi beberapa objek memerlukan ID baru untuk setiap hasil pecahan dan hubungan `derived-from`.

## 9. Jenis Hubungan

Hubungan resmi yang dapat digunakan:

| Hubungan | Makna |
|---|---|
| `parent-of` | Menjadi induk bagi objek lain |
| `child-of` | Menjadi turunan objek lain |
| `implements` | Menerapkan persyaratan atau prinsip |
| `implemented-by` | Diterapkan oleh objek lain |
| `evidenced-by` | Dibuktikan oleh rekaman atau bukti |
| `depends-on` | Bergantung pada objek lain |
| `supports` | Mendukung tanpa menjadi pelaksana utama |
| `conflicts-with` | Memiliki pertentangan yang harus diselesaikan |
| `supersedes` | Menggantikan objek lama |
| `superseded-by` | Digantikan objek baru |
| `derived-from` | Diturunkan dari objek sumber |
| `translated-as` | Memiliki terjemahan resmi |
| `implemented-in` | Diimplementasikan dalam modul atau sistem |

## 10. Register Awal Knowledge-ID Konstitusional

| Knowledge-ID | Objek | Sumber | Status | Pemilik Utama |
|---|---|---|---|---|
| KID-CON-PRN-001 | Supremasi QC-000 | QC-000 | ACTIVE-DRAFT | Otoritas Konstitusional |
| KID-CON-PRN-002 | Bahasa Indonesia sebagai teks induk normatif | QC-000, QC-002 | ACTIVE-DRAFT | Pengelola Dokumen |
| KID-GOV-PRN-001 | Akuntabilitas kewenangan | QC-006 | ACTIVE-DRAFT | Pimpinan Tata Kelola |
| KID-GOV-REQ-001 | Pemisahan tugas material | QC-006, QC-007 | ACTIVE-DRAFT | Pemilik Proses |
| KID-GOV-CTL-001 | Pengendalian konflik kepentingan | QC-008 | ACTIVE-DRAFT | Fungsi Etika |
| KID-GOV-PROC-001 | Pengaduan, keberatan, dan banding | QC-009 | ACTIVE-DRAFT | Pengelola Pengaduan |
| KID-DOC-REQ-001 | Keunikan kode dokumen | QC-002 | ACTIVE-DRAFT | Pengelola Dokumen |
| KID-DOC-REQ-002 | Pengendalian versi dan status | QC-002, QC-003 | ACTIVE-DRAFT | Pengelola Dokumen |
| KID-DOC-CTL-001 | Keterlacakan persyaratan dan bukti | QC-004 | ACTIVE-DRAFT | Pengelola Mutu |
| KID-DOC-DEF-001 | Terminologi resmi QURBATA | QC-005 | ACTIVE-DRAFT | Pengelola Terminologi |
| KID-RSK-REQ-001 | Pengelolaan risiko organisasi | QC-010 | ACTIVE-DRAFT | Pemilik Risiko |
| KID-RSK-CTL-001 | Keberlangsungan layanan kritis | QC-010, QC-011 | ACTIVE-DRAFT | Koordinator Keberlangsungan |
| KID-RSK-SPEC-001 | Penetapan MTPD, RTO, dan RPO | QC-011 | ACTIVE-DRAFT | Pemilik Layanan dan Sistem |
| KID-SAFE-PRN-001 | Kepentingan terbaik peserta didik | QC-012 | ACTIVE-DRAFT | Penanggung Jawab Safeguarding |
| KID-SAFE-CTL-001 | Pencegahan kekerasan dan eksploitasi | QC-012 | ACTIVE-DRAFT | Penanggung Jawab Safeguarding |
| KID-SAFE-PROC-001 | Respons insiden perlindungan | QC-009, QC-012 | ACTIVE-DRAFT | Tim Respons Perlindungan |
| KID-QA-CTL-001 | Audit keterlacakan konstitusional | QC-004, CTM | ACTIVE-DRAFT | Fungsi Audit dan Mutu |
| KID-OS-SPEC-001 | Register dokumen terkendali RIQA OS | QC-002, QC-003 | PROPOSED | Product Owner RIQA OS |
| KID-OS-SPEC-002 | Register Knowledge-ID RIQA OS | QC-004, REG-GOV-001 | PROPOSED | Product Owner RIQA OS |
| KID-OS-SPEC-003 | Mesin pemeriksaan hubungan dan dampak perubahan | QC-004, CTM | PROPOSED | Product Owner RIQA OS |

## 11. Integrasi dengan Matriks Keterlacakan

1. Setiap baris dalam `QURBATA-Constitutional-Traceability-Matrix.md` harus memiliki satu atau lebih Knowledge-ID.
2. Knowledge-ID mengidentifikasi objek pengetahuan; ID `CTM-*` mengidentifikasi baris keterlacakan dan pengujian kepatuhan.
3. Satu Knowledge-ID dapat muncul pada beberapa baris CTM apabila diterapkan pada beberapa konteks.
4. Setiap bukti audit material harus dapat ditelusuri ke Knowledge-ID dan persyaratan CTM terkait.
5. Ketidaksesuaian hubungan harus dicatat sebagai temuan audit.

## 12. Integrasi RIQA OS

RIQA OS sekurang-kurangnya harus menyediakan:

- generator Knowledge-ID terkendali;
- pemeriksaan keunikan;
- larangan penggunaan ulang nomor;
- status dan siklus hidup ID;
- relasi antar-objek;
- pencarian berdasarkan domain, jenis, sumber, pemilik, dan status;
- dampak perubahan;
- hubungan dengan dokumen, modul, data, asesmen, dan bukti;
- riwayat perubahan yang tidak dapat dihapus tanpa otorisasi;
- ekspor register untuk audit; dan
- peringatan ID yatim, ganda, tidak valid, atau merujuk objek yang dicabut.

## 13. Pemeriksaan Mutu

Audit register sekurang-kurangnya memeriksa:

1. duplikasi ID;
2. format tidak valid;
3. objek tanpa pemilik;
4. ID tanpa dokumen sumber;
5. ID yang tidak memiliki hubungan implementasi atau bukti padahal diwajibkan;
6. ID yatim setelah perubahan dokumen;
7. referensi kepada ID berstatus `RETIRED`;
8. perbedaan makna lintas bahasa;
9. perubahan material yang mempertahankan ID lama secara tidak sah; dan
10. nomor yang digunakan tanpa pencatatan resmi.

## 14. Masa Transisi

1. Identitas dari skema pengetahuan sebelumnya tidak otomatis dibawa ke skema ini.
2. ID lama harus dipetakan, dinilai, dan ditetapkan sebagai `mapped`, `superseded`, atau `retired`.
3. Tidak boleh ada dua skema Knowledge-ID aktif sebagai sumber otoritatif.
4. Selama masa transisi, register ini menjadi sumber rancangan tunggal pada branch konstitusi.
5. Status `ACTIVE` hanya diberikan setelah skema dan register diratifikasi sesuai QC-007.

## 15. Catatan Pengendalian

Register ini harus diperbarui apabila:

- Knowledge-ID baru dibuat;
- objek berubah secara material;
- objek dipindahkan, digabung, dipecah, digantikan, atau dicabut;
- dokumen sumber berubah;
- pemilik atau otoritas berubah;
- status bahasa berubah;
- hubungan implementasi atau bukti berubah; atau
- modul RIQA OS terkait diterbitkan.

## 16. Namespace Objek Isi Pendidikan

Objek isi pendidikan menggunakan ID kelas langsung dan tidak dibungkus ulang dengan prefix KID:

| Kelas | Format | Contoh pertama | Fungsi |
|---|---|---|---|
| Knowledge Object | KO-NNNNNN | KO-000001 | Unit pengetahuan terkecil |
| Learning Object | LO-NNNNNN | LO-000001 | Pengalaman belajar |
| Page Object | PO-NNNNNN | PO-000001 | Halaman sumber tunggal |
| Chapter Object | CO-NNNNNN | CO-000001 | Bab atau kelompok halaman |
| Book Object | BO-NNNNNN | BO-000001 | Buku atau jilid |
| Curriculum Object | CUR-NNNNNN | CUR-000001 | Kurikulum atau jalur program |

Nomor enam digit bersifat global dalam setiap kelas. ID tidak memuat jilid, halaman, level, tahun, bahasa, atau versi karena atribut tersebut dapat berubah. Kode tampilan seperti QJ1-P001 tetap dapat digunakan sebagai locator produk, tetapi wajib dipetakan kepada PO yang stabil.

## 17. Aturan Satu ID Satu Objek

1. Satu ID hanya mewakili satu objek dengan batas makna yang jelas.
2. Satu objek aktif hanya mempunyai satu ID kanonik dalam kelasnya.
3. Alias atau kode lama dicatat sebagai alias dan tidak menjadi identitas kedua.
4. Perubahan editorial mempertahankan ID.
5. Perubahan material menghasilkan ID baru dan relasi supersedes/superseded-by.
6. Pemecahan menghasilkan ID baru untuk setiap hasil; objek lama menjadi superseded.
7. Penggabungan menghasilkan ID baru; seluruh sumber tetap tercatat.
8. ID yang retired atau superseded tidak pernah diterbitkan ulang.
9. Objek lintas bahasa menggunakan ID yang sama dan versi bahasa terpisah.
10. ID hanya berstatus permanent setelah objek dan skema terkait diratifikasi atau dibekukan melalui kewenangan yang sah.

## 18. Status Kanonik

Status teknis yang diizinkan adalah PROPOSED, ACTIVE-DRAFT, ACTIVE, DEPRECATED, SUPERSEDED, RETIRED, dan RESERVED. DEPRECATED berarti masih dapat dibaca untuk kompatibilitas tetapi tidak boleh dipakai pada implementasi baru. SUPERSEDED wajib memiliki superseded-by; pengganti wajib memiliki supersedes.

## 19. Otoritas Penerbitan

Pengendali Register Knowledge-ID merupakan satu-satunya fungsi yang menerbitkan ID resmi. Penyusun dapat meminta reservasi, tetapi tidak boleh menganggap nomor sebagai resmi sebelum tercatat. RIQA OS wajib menggunakan transaksi atomik atau penguncian yang mencegah dua objek memperoleh ID sama.

## 20. Metadata Objek Isi

Selain metadata minimum pada Bagian 7, KO/LO/PO/CO/BO/CUR mencatat judul, ringkasan, versi, bahasa, status validasi, prasyarat, parent, children, sumber, capaian terkait, asesmen terkait, hak penggunaan, dan checksum konten apabila relevan.

## 21. Register Awal Model Isi

| ID | Nama Awal | Status | Catatan |
|---|---|---|---|
| KO-000001 | Objek Pengetahuan Awal QURBATA | RESERVED | Diisi setelah ontology disetujui |
| LO-000001 | Objek Pembelajaran Awal QURBATA | RESERVED | Diisi setelah desain pembelajaran disetujui |
| PO-000001 | Halaman Awal QURBATA | RESERVED | Dipetakan kemudian ke kode halaman produk |
| CO-000001 | Bab Awal QURBATA | RESERVED | Struktur bab belum dibekukan |
| BO-000001 | Buku QURBATA Jilid 1 | PROPOSED | Menunggu struktur buku final |
| CUR-000001 | Kurikulum QURBATA | PROPOSED | Menunggu arsitektur kurikulum final |

## 22. Riwayat Perubahan

| Versi | Tanggal | Ringkasan |
|---|---|---|
| 0.1.0-id | 26 Juli 2026 | Skema KID tata kelola dan register awal |
| 0.2.0-id | 26 Juli 2026 | Penambahan namespace KO/LO/PO/CO/BO/CUR, aturan satu ID, status, supersesi, dan otoritas penerbitan |
