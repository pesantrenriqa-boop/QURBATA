# REG-GOV-010 — Dashboard Tata Kelola QURBATA

## 1. Tujuan
Dashboard ini merangkum kondisi tata kelola QURBATA dalam satu tampilan agar pimpinan dapat melihat kesiapan ratifikasi, kepatuhan, risiko, audit, CAPA, review, dan integrasi RIQA OS.

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
| Review terlambat | review lewat tenggat | 0 |
| Konflik ID | ID ganda/yatim/ambigu | 0 |

## 3. Status Awal per 26 Juli 2026
| Area | Status | Catatan |
|---|---|---|
| Konstitusi QC-000 | Kuning | Master Indonesia tersedia tetapi masih harmonisasi akhir |
| QC-001–QC-012 | Kuning | Substansi tersedia; audit lintas dokumen belum selesai |
| Governance toolkit | Kuning | Register inti tersedia; implementasi dan bukti belum lengkap |
| Bahasa Inggris | Merah | Belum harmonis penuh dengan master Indonesia |
| Bahasa Arab | Merah | Belum menjadi terjemahan resmi lengkap |
| Knowledge-ID | Kuning | Skema tersedia; populasi seluruh objek belum selesai |
| Safeguarding | Kuning | Kebijakan tersedia; simulasi implementasi belum selesai |
| RIQA OS integration | Kuning | Model data dirumuskan; implementasi belum selesai |
| Governance Freeze | Belum Lulus | Menunggu seluruh gate kritis |

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
Dashboard harus menampilkan:
- jumlah dokumen per status dan versi;
- dokumen/review yang terlambat;
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
| 4 | Lengkapi bukti safeguarding dan simulasi | Safeguarding Lead |
| 5 | Tutup temuan mayor dan verifikasi CAPA | QA Lead |
| 6 | Putuskan Governance Freeze melalui Decision-ID | Pimpinan QURBATA |

## 9. Catatan Perubahan
| Versi | Tanggal | Perubahan |
|---|---|---|
| 0.1.0 | 2026-07-26 | Dashboard tata kelola awal dan stage gate Governance Freeze dibuat |
