# REG-GOV-010 — Dasbor Tata Kelola QURBATA

**Kode Dokumen:** REG-GOV-010  
**Judul:** Dasbor Tata Kelola QURBATA  
**Bahasa Induk:** Bahasa Indonesia  
**Status:** Draf Terkendali  
**Versi:** 0.11.0-id  
**Pemilik Dokumen:** Fungsi Tata Kelola QURBATA  
**Otoritas Persetujuan:** Pendiri dan Peneliti Utama/Dewan Konstitusi setelah aktif  
**Tanggal Berlaku:** Setelah persetujuan sesuai kewenangan  
**Tinjauan Berikutnya:** Tahunan atau ketika terdapat perubahan material  
**Klasifikasi Akses:** Internal; ringkasan dapat dipublikasikan  
**Induk Normatif:** QC-000 — Konstitusi QURBATA  
**Dokumen Pengendali:** QC-001, QC-003, QC-004, QC-006, dan QC-007  


## 1. Tujuan
Dasbor ini merangkum kondisi tata kelola QURBATA dalam satu tampilan agar pimpinan dapat melihat kesiapan ratifikasi, kepatuhan, risiko, audit, CAPA, penelaahan, dan integrasi RIQA OS.

## 2. Indikator Utama
| Indikator | Rumus | Target Governance Freeze |
|---|---|---:|
| Kelengkapan dokumen | dokumen wajib tersedia / dokumen wajib | 100% |
| Kelengkapan metadata | metadata lengkap / seluruh dokumen | 100% |
| Validitas rujukan silang | rujukan valid / seluruh rujukan | 100% |
| Keterlacakan persyaratan | persyaratan dengan pemilik+bukti / seluruh persyaratan kritis | 100% |
| Kepatuhan kritis | butir kritis lulus / seluruh butir kritis | 100% |
| Penyelesaian temuan mayor | temuan mayor ditutup / seluruh temuan mayor | 100% sebelum ratifikasi |
| CAPA efektif | CAPA terverifikasi efektif / CAPA selesai | 100% |
| Risiko kritis tak terkendali | jumlah risiko kritis tanpa mitigasi | 0 |
| Penelaahan terlambat | penelaahan lewat tenggat | 0 |
| Konflik ID | ID ganda/yatim/ambigu | 0 |

## 3. Status Awal per 26 Juli 2026
| Area | Status | Catatan |
|---|---|---|
| Konstitusi QC-000 | Kuning | Master Indonesia lengkap secara substantif; audit terminologi internal selesai, validasi editorial independen dan ratifikasi belum selesai |
| QC-001–QC-012 | Kuning | Metadata dan arsitektur telah diharmonisasikan; verifikasi bukti implementasi belum selesai |
| Governance toolkit | Kuning | Register inti tersedia; implementasi dan bukti belum lengkap |
| Bahasa Inggris | Abu-abu | Tindak lanjut non-blocking; tidak termasuk baseline Governance v1.0 Bahasa Indonesia |
| Bahasa Arab | Abu-abu | Tindak lanjut non-blocking; tidak termasuk baseline Governance v1.0 Bahasa Indonesia |
| Knowledge-ID | Kuning | Audit format, duplikasi, dan referensi CTM awal lulus; validasi kelengkapan substantif dan populasi objek isi belum selesai |
| Safeguarding | Hijau | Kebijakan dan kesiapan operasional awal tervalidasi; audit efektivitas berkala tetap wajib |
| RIQA OS integration | Kuning | Model data dirumuskan; implementasi belum selesai |
| Governance Freeze | Belum Lulus—84,4% informatif | 13 PASS, 1 PARTIAL, 2 FAIL; satu FAIL tetap memblokir freeze |

## 4. Stage Gate Governance Freeze
Governance v1.0 hanya boleh dibekukan jika:
1. QC-000–QC-012 tidak saling bertentangan;
2. seluruh dokumen memiliki metadata minimum;
3. semua rujukan silang valid;
4. istilah konsisten dengan QC-005;
5. RACI dan otoritas persetujuan konsisten;
6. seluruh persyaratan kritis memiliki pemilik dan bukti;
7. temuan kritis dan mayor ditutup atau memiliki keputusan risiko yang sah;
8. tidak ada risiko kritis tak terkendali;
9. Knowledge-ID kritis tidak ganda, yatim, atau ambigu;
10. master Bahasa Indonesia telah ditelaah substantif dan editorial;
11. safeguarding dan pemulihan diuji;
12. keputusan ratifikasi tercatat dalam REG-GOV-003.

## 5. Skema Lampu Status
- **Hijau:** memenuhi target dan bukti tersedia.
- **Kuning:** sebagian selesai atau menunggu verifikasi.
- **Merah:** belum memenuhi persyaratan kritis.
- **Abu-abu:** belum berlaku atau belum dinilai.

## 6. Tampilan Minimum RIQA OS
Dasbor harus menampilkan:
- jumlah dokumen per status dan versi;
- dokumen/penelaahan yang terlambat;
- temuan audit per tingkat;
- CAPA per status dan efektivitas;
- risiko inheren dan residual;
- keputusan menunggu persetujuan;
- konflik Knowledge-ID;
- kepatuhan CHK-GOV-001;
- readiness score setiap stage gate;
- tautan langsung ke bukti dan pemilik tindakan.

## 7. Aturan Readiness Score
Skor agregat hanya informatif. Satu kegagalan pada butir kritis tetap menggagalkan stage gate walaupun skor total tinggi. Sistem dilarang menyatakan “siap” hanya berdasarkan rata-rata persentase.

## 8. Ringkasan Tindakan Prioritas
| Prioritas | Tindakan | Pemilik |
|---:|---|---|
| 1 | Audit metadata dan rujukan QC-000–QC-012 | Document Controller/QA |
| 2 | Tutup gap master Bahasa Indonesia | Governance & Editorial Leads |
| 3 | Selesaikan ontology dan populasi Knowledge-ID | Knowledge Architect |
| 4 | Pertahankan audit efektivitas berkala safeguarding | Safeguarding Lead |
| 5 | Tutup temuan mayor dan verifikasi CAPA | QA Lead |
| 6 | Putuskan Governance Freeze melalui Decision-ID | Pimpinan QURBATA |

## 9. Register Governance Freeze

Keputusan kesiapan freeze wajib dicatat pada REG-GOV-011. Dasbor hanya menyajikan ringkasan dan tidak dapat menggantikan bukti, penilaian gate, keberatan, persetujuan, atau Decision-ID pada register tersebut.

## 10. Catatan Perubahan
| Versi | Tanggal | Perubahan |
|---|---|---|
| 0.1.0 | 2026-07-26 | Dasbor tata kelola awal dan stage gate Governance Freeze dibuat |
| 0.2.0-id | 2026-07-26 | Pembaruan status QC-000, seri QC, Knowledge-ID, dan integrasi REG-GOV-011 |
| 0.4.0-id | 2026-07-27 | Menyelaraskan istilah dasbor serta status audit editorial dan Knowledge-ID |
| 0.5.0-id | 2026-07-27 | Memperbarui readiness informatif menjadi 65,6% setelah GF-09 PASS |
| 0.6.0-id | 2026-07-27 | Memperbarui readiness informatif menjadi 68,8% setelah GF-02 PASS |
| 0.7.0-id | 2026-07-27 | Memperbarui readiness informatif menjadi 71,9% setelah GF-06 PASS |
| 0.8.0-id | 2026-07-27 | Memperbarui readiness informatif menjadi 75,0% setelah GF-04 PASS |
| 0.9.0-id | 2026-07-27 | Memperbarui readiness informatif menjadi 78,1% setelah GF-11 PASS |
| 0.10.0-id | 2026-07-27 | Memperbarui readiness informatif menjadi 81,3% setelah GF-07 PASS |
| 0.11.0-id | 2026-07-27 | Memperbarui readiness informatif menjadi 84,4% setelah GF-12 PASS |
