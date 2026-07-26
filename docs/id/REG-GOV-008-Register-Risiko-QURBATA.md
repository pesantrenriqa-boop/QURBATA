# REG-GOV-008 — Register Risiko QURBATA

## 1. Tujuan
Register ini mengendalikan risiko yang dapat mengganggu integritas keilmuan, mutu pembelajaran, keselamatan peserta didik, keberlanjutan layanan, keamanan data, hukum, reputasi, dan keberhasilan implementasi QURBATA.

## 2. Skala Penilaian
Probabilitas dan dampak dinilai 1–5. Nilai risiko = probabilitas × dampak.

| Nilai | Kategori | Tindakan |
|---:|---|---|
| 1–4 | Rendah | Pantau dan kendalikan rutin |
| 5–9 | Sedang | Rencana mitigasi dan pemilik wajib |
| 10–16 | Tinggi | Mitigasi prioritas dan pelaporan berkala |
| 17–25 | Kritis | Eskalasi langsung; aktivitas dapat dihentikan |

## 3. Kategori Risiko
- GOV: tata kelola dan kewenangan;
- CUR: kurikulum dan validitas akademik;
- PED: pedagogi dan hasil belajar;
- ASM: asesmen dan keputusan kelulusan;
- SFG: safeguarding;
- DAT: privasi, kualitas, dan keamanan data;
- TEC: teknologi dan keberlangsungan sistem;
- LEG: hukum, lisensi, dan hak cipta;
- OPS: operasional dan SDM;
- REP: reputasi dan komunikasi publik.

## 4. Register Awal
| Risk-ID | Kategori | Risiko | P | D | Nilai | Kontrol Saat Ini | Mitigasi Lanjutan | Pemilik | Status |
|---|---|---|---:|---:|---:|---|---|---|---|
| RSK-GOV-001 | GOV | Dua sumber normatif menimbulkan konflik kewenangan | 2 | 5 | 10 | QC-000 ditetapkan sebagai norma tertinggi | Audit seluruh rujukan dan hapus sumber lama | Governance Lead | Mitigasi berjalan |
| RSK-GOV-002 | GOV | Dokumen digunakan sebelum disetujui | 3 | 4 | 12 | Status dokumen dan branch PR | Terapkan validasi status otomatis | Document Controller | Terbuka |
| RSK-CUR-001 | CUR | Urutan materi tidak sesuai prasyarat belajar | 3 | 5 | 15 | Review kurikulum dan knowledge graph | Bekukan competency/prerequisite graph sebelum buku final | Curriculum Lead | Terbuka |
| RSK-PED-001 | PED | Buku terlalu kompleks atau terlalu cepat bagi peserta pemula | 4 | 4 | 16 | Review pedagogis dan pola bertahap | Pilot, data kesalahan, dan revisi berbasis bukti | Pedagogy Lead | Terbuka |
| RSK-ASM-001 | ASM | Soal tidak benar-benar mengukur kompetensi target | 3 | 5 | 15 | Traceability target–soal | Audit kualitas butir dan validasi assessment graph | Assessment Lead | Terbuka |
| RSK-SFG-001 | SFG | Laporan perlindungan peserta terlambat ditangani | 2 | 5 | 10 | QC-012 dan jalur eskalasi | Uji simulasi dan SLA respons | Safeguarding Lead | Terbuka |
| RSK-DAT-001 | DAT | Data peserta bocor atau diakses tanpa kewenangan | 3 | 5 | 15 | Role-based access direncanakan | Minimasi data, audit log, backup, dan kontrol akses | Data Lead | Terbuka |
| RSK-TEC-001 | TEC | RIQA OS menjadi ketergantungan tunggal tanpa pemulihan | 3 | 4 | 12 | QC-011 | Backup, ekspor portabel, RTO/RPO, uji pemulihan | Technology Lead | Terbuka |
| RSK-LEG-001 | LEG | Contoh, gambar, font, audio, atau materi melanggar lisensi | 3 | 4 | 12 | Asset register direncanakan | Bukti lisensi dan provenance wajib | Legal/IP Owner | Terbuka |
| RSK-OPS-001 | OPS | Visi sistem terlalu besar memperlambat penyelesaian buku | 4 | 4 | 16 | Prioritas buku sebagai produk utama | Stage gate: fondasi minimum lalu produksi buku | Program Lead | Mitigasi berjalan |

## 5. Respons Risiko
- Hindari;
- Kurangi;
- Alihkan;
- Terima dengan persetujuan;
- Eksploitasi untuk peluang positif.

Risiko kritis tidak boleh diterima oleh pemilik operasional sendiri.

## 6. Data Wajib RIQA OS
`risk_id`, `category`, `statement`, `cause`, `impact`, `probability`, `severity`, `inherent_score`, `controls`, `residual_score`, `response`, `owner`, `review_date`, `linked_requirement`, `linked_finding`, `linked_capa`, `status`.

## 7. Review
- Kritis: mingguan;
- Tinggi: bulanan;
- Sedang: triwulanan;
- Rendah: semesteran;
- seluruh risiko: setiap perubahan mayor atau insiden.

## 8. Catatan Perubahan
| Versi | Tanggal | Perubahan |
|---|---|---|
| 0.1.0 | 2026-07-26 | Register risiko awal dan sepuluh risiko prioritas dibuat |
