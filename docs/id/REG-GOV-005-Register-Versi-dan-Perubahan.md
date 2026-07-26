# REG-GOV-005 — Register Versi dan Perubahan QURBATA

**Kode Dokumen:** REG-GOV-005  
**Judul:** Register Versi dan Perubahan QURBATA  
**Bahasa Induk:** Bahasa Indonesia  
**Status:** Draf Terkendali  
**Versi:** 0.2.0-id  
**Pemilik Dokumen:** Fungsi Tata Kelola QURBATA  
**Otoritas Persetujuan:** Pendiri dan Peneliti Utama/Dewan Konstitusi setelah aktif  
**Tanggal Berlaku:** Setelah persetujuan sesuai kewenangan  
**Tinjauan Berikutnya:** Tahunan atau ketika terdapat perubahan material  
**Klasifikasi Akses:** Internal; ringkasan dapat dipublikasikan  
**Induk Normatif:** QC-000 — Konstitusi QURBATA  
**Dokumen Pengendali:** QC-001, QC-003, QC-004, QC-006, dan QC-007  


## 1. Tujuan
Register ini mencatat seluruh versi resmi, alasan perubahan, dampak, keputusan, penelaah, dan status penerapan agar tidak ada revisi tanpa jejak.

## 2. Aturan Versi
QURBATA menggunakan semantic versioning:
- `MAJOR`: perubahan arsitektur, norma, atau kompatibilitas;
- `MINOR`: penambahan substansi yang kompatibel;
- `PATCH`: koreksi editorial atau teknis tanpa mengubah makna.

Versi draf menggunakan rentang `0.x.x`. Versi pertama yang diratifikasi menggunakan `1.0.0`.

## 3. Klasifikasi Perubahan
| Kode | Jenis | Contoh | Persetujuan Minimum |
|---|---|---|---|
| CHG-MAJ | Mayor | Perubahan kewenangan, struktur kurikulum, standar kelulusan | Pimpinan/Otoritas Ratifikasi |
| CHG-MIN | Minor | Penambahan kontrol, indikator, prosedur | Pemilik + Governance/QA Lead |
| CHG-PAT | Patch | Ejaan, tautan, format, metadata | Document Controller |
| CHG-EMR | Darurat | Safeguarding, keamanan, kehilangan data | Otoritas darurat lalu ratifikasi retrospektif |

## 4. Register Awal
| Change-ID | Dokumen/Objek | Dari | Menjadi | Klasifikasi | Ringkasan | Dampak | Status | Decision-ID |
|---|---|---:|---:|---|---|---|---|---|
| CHG-2026-001 | QC-000 | 0.1.0 | 0.9.0 | CHG-MAJ | Konsolidasi konstitusi sebagai norma tertinggi | Seluruh governance | Dalam harmonisasi | DEC-GOV-001 |
| CHG-2026-002 | Sistem kode | QF lama | QC/REG/MAT/CHK | CHG-MAJ | Menghapus Knowledge-ID konstitusional lama dan menetapkan keluarga kode baru | Dokumen dan integrasi OS | Diterapkan pada branch | DEC-GOV-002 |
| CHG-2026-003 | Bahasa normatif | Bilingual paralel | Indonesia sebagai master | CHG-MAJ | Menetapkan bahasa Indonesia sebagai teks pengendali | Terjemahan dan ratifikasi | Diterapkan | DEC-GOV-003 |
| CHG-2026-004 | Governance toolkit | Tidak ada | REG-GOV-001–005, MAT, CHK | CHG-MIN | Menambahkan instrumen pengendalian | Audit dan operasional | Berjalan | DEC-GOV-004 |

## 5. Data Wajib Setiap Perubahan
- Change-ID;
- objek yang diubah;
- versi lama dan baru;
- alasan dan sumber usulan;
- klasifikasi perubahan;
- analisis dampak;
- dokumen/Knowledge-ID terdampak;
- risiko dan mitigasi;
- penelaah dan pemberi persetujuan;
- tanggal berlaku;
- rencana migrasi;
- hasil verifikasi pascapenerapan.

## 6. Analisis Dampak Minimum
Perubahan material harus diperiksa terhadap:
1. QC-000 dan dokumen turunan;
2. kurikulum, buku, asesmen, dan panduan guru;
3. Knowledge Object dan Learning Object;
4. data peserta, guru, dan institusi;
5. API, database, RIQA OS, dan aset digital;
6. safeguarding dan hak peserta didik;
7. lisensi, hak cipta, dan publikasi;
8. terjemahan resmi.

## 7. Larangan
- mengubah konten efektif tanpa menaikkan versi;
- menimpa riwayat lama;
- menggunakan istilah `final` tanpa ratifikasi;
- menggabungkan perubahan mayor dengan patch editorial tanpa pemisahan;
- menerapkan perubahan darurat tanpa telaah retrospektif.

## 8. Kolom RIQA OS
`change_id`, `object_id`, `old_version`, `new_version`, `change_class`, `summary`, `rationale`, `impact`, `risk`, `decision_id`, `proposer`, `reviewer`, `approver`, `effective_at`, `verification_status`, `rollback_plan`.

## 9. Catatan Perubahan
| Versi | Tanggal | Perubahan |
|---|---|---|
| 0.1.0 | 2026-07-26 | Register versi dan perubahan pertama diterbitkan sebagai draf terkendali |
