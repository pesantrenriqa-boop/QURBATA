# Matriks Keterlacakan Konstitusional QURBATA

Dokumen ini menjadi matriks pengendali untuk menelusuri hubungan antara prinsip Konstitusi QURBATA, dokumen pelaksana, bukti penerapan, penanggung jawab, risiko, dan kebutuhan implementasi pada RIQA OS.

## 1. Kedudukan

1. QC-000 tetap menjadi sumber normatif tertinggi.
2. Matriks ini tidak membuat norma baru dan tidak menggantikan isi dokumen QC.
3. Apabila terdapat perbedaan antara matriks dan dokumen QC, isi dokumen QC yang berlaku menjadi rujukan.
4. Matriks wajib diperbarui ketika terdapat perubahan substansial pada QC-000 sampai QC-012.
5. Setiap baris harus dapat ditelusuri ke bukti yang nyata, bukan hanya pernyataan administratif.

## 2. Status Keterlacakan

| Status | Makna |
|---|---|
| Terpenuhi | Norma, pengendali, pemilik, dan bukti telah tersedia. |
| Sebagian | Sebagian pengendali atau bukti telah tersedia, tetapi masih ada kekosongan. |
| Direncanakan | Norma telah ditetapkan, tetapi penerapan atau buktinya belum tersedia. |
| Tidak sesuai | Terdapat konflik, kekurangan material, atau penerapan yang bertentangan. |
| Tidak berlaku | Persyaratan tidak relevan terhadap ruang lingkup yang dinilai dan alasannya terdokumentasi. |

## 3. Matriks Utama

| ID Keterlacakan | Persyaratan konstitusional | Dokumen pengendali utama | Dokumen pendukung | Bukti minimum | Pemilik utama | Objek RIQA OS | Status awal |
|---|---|---|---|---|---|---|---|
| CTM-GOV-001 | QC-000 menjadi satu-satunya konstitusi normatif tertinggi. | QC-000 | QC-001, QC-003 | daftar dokumen terkendali, riwayat pencabutan dokumen lama | Otoritas Konstitusional | document_register, document_version | Sebagian |
| CTM-GOV-002 | Struktur tata kelola, garis kewenangan, dan pemisahan fungsi harus jelas. | QC-001 | QC-006, QC-007 | bagan kewenangan, surat penetapan peran, matriks RACI | Pimpinan QURBATA | organization_unit, role, authority_assignment | Direncanakan |
| CTM-DOC-001 | Setiap dokumen resmi memiliki identitas, nomor, versi, status, pemilik, dan riwayat perubahan. | QC-002 | QC-003, QC-004 | metadata dokumen, log perubahan, persetujuan | Pengendali Dokumen | document, document_metadata, approval_log | Sebagian |
| CTM-DOC-002 | Dokumen harus disusun, ditelaah, disetujui, diterbitkan, direvisi, dan dicabut secara terkendali. | QC-003 | QC-002, QC-006, QC-007 | workflow persetujuan, catatan telaah, bukti publikasi | Pengendali Dokumen | document_workflow, review_task, publication_record | Direncanakan |
| CTM-TRC-001 | Norma, keputusan, materi, asesmen, dan bukti harus dapat ditelusuri dua arah. | QC-004 | QC-002, QC-003 | tautan sumber-ke-turunan, hubungan versi, catatan dampak perubahan | Pemilik Pengetahuan | trace_link, source_relation, impact_record | Direncanakan |
| CTM-TRM-001 | Istilah resmi harus digunakan secara konsisten pada seluruh dokumen dan sistem. | QC-005 | QC-002, QC-003, QC-004 | glosarium terkendali, hasil audit terminologi | Pemilik Terminologi | terminology, term_translation, usage_audit | Sebagian |
| CTM-ACC-001 | Setiap peran mempunyai kewenangan, tanggung jawab, batas, pengganti, dan akuntabilitas. | QC-006 | QC-001, QC-007, QC-008 | uraian peran, delegasi, log keputusan, evaluasi kinerja | Pimpinan dan Pemilik Proses | role, delegation, accountability_record | Direncanakan |
| CTM-DEC-001 | Keputusan dan ratifikasi harus mengikuti tingkat kewenangan serta menyimpan dasar dan bukti. | QC-007 | QC-006, QC-008 | agenda, notula, hasil pemungutan suara, persetujuan, dasar keputusan | Sekretariat Tata Kelola | decision, meeting, ratification, vote_record | Direncanakan |
| CTM-ETH-001 | Konflik kepentingan harus dinyatakan, dinilai, ditangani, dan diawasi. | QC-008 | QC-006, QC-007 | deklarasi konflik, keputusan mitigasi, pembatasan akses | Pejabat Etik atau Otoritas Independen | conflict_disclosure, recusal, mitigation_plan | Direncanakan |
| CTM-CMP-001 | Pengaduan, keberatan, banding, dan pelaporan harus aman, adil, rahasia, dan bebas pembalasan. | QC-009 | QC-006, QC-008, QC-012 | registrasi perkara, klasifikasi risiko, bukti pemeriksaan, keputusan, tindak lanjut | Pengelola Pengaduan | complaint, appeal, case, protection_measure | Direncanakan |
| CTM-RSK-001 | Risiko harus diidentifikasi, dinilai, ditangani, dimonitor, dan dilaporkan. | QC-010 | QC-006, QC-007, QC-008 | risk register, pemilik risiko, kontrol, rencana tindakan | Pemilik Risiko | risk, control, treatment_plan, risk_review | Direncanakan |
| CTM-BCM-001 | Layanan kritis harus mempunyai strategi keberlangsungan dan pengaturan operasi darurat. | QC-010 | QC-011, QC-012 | daftar layanan kritis, rencana kontinuitas, latihan | Koordinator Keberlangsungan | critical_service, continuity_plan, exercise | Direncanakan |
| CTM-DR-001 | Setiap layanan kritis harus mempunyai MTPD, RTO, RPO, cadangan, dan prosedur pemulihan teruji. | QC-011 | QC-010, QC-012 | hasil BIA, log backup, hasil restore test, laporan simulasi | Pemilik Layanan dan Pemilik Sistem | business_impact, recovery_target, backup_test | Direncanakan |
| CTM-SAFE-001 | Kepentingan terbaik, keselamatan, martabat, dan kesejahteraan peserta didik harus menjadi prioritas. | QC-012 | QC-006, QC-009, QC-010, QC-011 | asesmen risiko kegiatan, catatan perlindungan, tindakan pemulihan | Penanggung Jawab Perlindungan Peserta Didik | safeguarding_case, learner_risk, protection_plan | Direncanakan |
| CTM-SAFE-002 | Seluruh personel yang memiliki akses kepada peserta didik harus melalui pemeriksaan, orientasi, dan pengawasan proporsional. | QC-012 | QC-006, QC-008 | verifikasi personel, orientasi, pelatihan, evaluasi kelayakan | SDM dan Penanggung Jawab Perlindungan | personnel_screening, training_record, suitability_review | Direncanakan |
| CTM-DAT-001 | Data dan bukti sensitif harus dibatasi, dicatat, dilindungi, dipertahankan, dan dimusnahkan secara sah. | QC-002 | QC-003, QC-009, QC-010, QC-011, QC-012 | klasifikasi data, log akses, jadwal retensi, bukti pemusnahan | Pemilik Data | data_asset, access_log, retention_rule, disposal_record | Sebagian |
| CTM-LNG-001 | Bahasa Indonesia menjadi teks pengendali; terjemahan resmi wajib harmonis dan tidak mengubah norma. | QC-000 | QC-003, QC-005 | register terjemahan, hasil harmonisasi, persetujuan penerjemah/penelaah | Otoritas Konstitusional dan Penelaah Bahasa | translation_version, equivalence_review | Sebagian |
| CTM-KID-001 | Setiap unit pengetahuan yang perlu ditelusuri harus mempunyai Knowledge-ID yang unik, stabil, dan tidak didaur ulang. | QC-002 | QC-004, QC-005 | register Knowledge-ID, aturan pencabutan, riwayat relasi | Pemilik Pengetahuan | knowledge_item, knowledge_id, supersession_link | Direncanakan |
| CTM-AUD-001 | Kepatuhan, efektivitas, dan kelengkapan bukti harus diaudit secara berkala dan independen secara proporsional. | QC-001 | QC-004, QC-006, QC-008, QC-010 | program audit, temuan, tindakan korektif, verifikasi penutupan | Auditor atau Penelaah Independen | audit, finding, corrective_action, verification | Direncanakan |
| CTM-IMP-001 | Setiap ketidaksesuaian dan insiden harus menghasilkan koreksi, analisis sebab, tindakan korektif, dan pembelajaran. | QC-010 | QC-003, QC-004, QC-009, QC-011, QC-012 | laporan insiden, root cause analysis, CAPA, lessons learned | Pemilik Proses | incident, root_cause, corrective_action, lesson | Direncanakan |

## 4. Struktur Bukti Minimum

Setiap bukti yang dirujuk dalam matriks sekurang-kurangnya memiliki:

1. ID bukti;
2. jenis bukti;
3. judul atau ringkasan;
4. dokumen atau persyaratan yang didukung;
5. pemilik;
6. tanggal pembuatan;
7. periode berlaku;
8. lokasi penyimpanan;
9. klasifikasi akses;
10. versi atau hash apabila relevan;
11. status validasi;
12. validator;
13. tanggal validasi; dan
14. hubungan dengan temuan, risiko, keputusan, atau tindakan korektif.

## 5. Aturan Knowledge-ID untuk Matriks

1. ID matriks menggunakan pola `CTM-DOMAIN-NNN`.
2. Domain awal yang digunakan adalah `GOV`, `DOC`, `TRC`, `TRM`, `ACC`, `DEC`, `ETH`, `CMP`, `RSK`, `BCM`, `DR`, `SAFE`, `DAT`, `LNG`, `KID`, `AUD`, dan `IMP`.
3. ID yang telah diterbitkan tidak boleh dipakai kembali untuk persyaratan lain.
4. Persyaratan yang dicabut tetap dipertahankan dalam riwayat dengan status `dicabut`.
5. Perubahan redaksi yang mengubah makna material harus menghasilkan versi baru dan analisis dampak.
6. Hubungan antara CTM, QC, bukti, risiko, dan tindakan harus dapat ditelusuri dua arah.

## 6. Audit Keterlacakan

Audit matriks sekurang-kurangnya memeriksa:

- apakah seluruh norma material QC-000 telah mempunyai dokumen pelaksana;
- apakah setiap dokumen pelaksana mempunyai pemilik yang sah;
- apakah bukti benar-benar tersedia dan dapat diverifikasi;
- apakah bukti masih berlaku dan relevan;
- apakah terdapat persyaratan tanpa pengendali;
- apakah terdapat pengendali tanpa dasar konstitusional;
- apakah perubahan telah dianalisis dampaknya;
- apakah konflik lintas dokumen telah diselesaikan;
- apakah akses terhadap bukti sesuai klasifikasi; dan
- apakah tindakan korektif telah ditutup secara efektif.

## 7. Prioritas Penyelesaian Sebelum PR Keluar dari Draft

Prioritas wajib adalah:

1. menyelesaikan harmonisasi QC-000 Bahasa Indonesia;
2. menetapkan pola final Knowledge-ID pada QC-002;
3. menyelaraskan penggunaan istilah berdasarkan QC-005;
4. menambahkan cross-reference yang tepat pada setiap QC;
5. memastikan tidak ada nomor atau identitas dokumen yang ganda;
6. menetapkan pemilik dan status setiap dokumen dalam register;
7. menyelesaikan hubungan bahasa Indonesia–Inggris;
8. mencatat kesenjangan bahasa Arab secara terbuka;
9. menguji seluruh tautan pada indeks tata kelola; dan
10. melakukan audit final terhadap matriks ini.

## 8. Implementasi RIQA OS

RIQA OS sekurang-kurangnya harus mendukung:

- register persyaratan konstitusional;
- relasi persyaratan ke dokumen;
- relasi persyaratan ke bukti;
- relasi persyaratan ke pemilik, risiko, kontrol, keputusan, insiden, dan tindakan;
- status keterlacakan;
- pengingat peninjauan;
- riwayat perubahan;
- kontrol akses;
- ekspor laporan audit; dan
- dasbor kesenjangan keterlacakan.

Implementasi digital tidak menggantikan kewajiban penilaian substansi oleh pihak yang kompeten.

## 9. Peninjauan

Matriks ini ditinjau:

- sekurang-kurangnya satu kali setiap tahun;
- ketika QC-000 diubah;
- ketika dokumen QC baru diterbitkan atau dicabut;
- setelah insiden material;
- setelah audit menemukan kelemahan sistemik; atau
- sebelum perubahan status konstitusi dari Draft menjadi berlaku.
