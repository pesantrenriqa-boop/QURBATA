# AUD-ARB-QJ1-002 — Audit Keterlacakan Panduan Guru Bahasa Arab Jilid 1

**Audit-ID:** AUD-ARB-QJ1-002  
**Status:** DRAF TERKENDALI — TEMUAN TERBUKA  
**Tanggal:** 28 Juli 2026  
**Objek:** GDE-ARB-QJ1-001 dan MAP-ARB-QJ1-001  
**Sumber:** LEX-ARB-001–003, BAT-ARB-001–003, REG-ARB-002, REG-ARB-004  
**Keputusan:** PR tetap Draft

## 1. Tujuan

Memastikan setiap materi pada segmen Bahasa Arab P001–P040 dapat ditelusuri ke objek kompetensi resmi, dan mencegah kata, unsur fungsi, kalimat, teks, gerbang, atau klaim ketuntasan masuk secara diam-diam.

## 2. Hasil Ringkas

| Pemeriksaan | Hasil | Status |
|---|---:|---|
| halaman memiliki pemetaan operasional | 40/40 | LULUS STRUKTUR |
| entri leksikal aktual | 45 | TERDAFTAR |
| target keluarga leksikal yang dihitung | 40 | TERDAFTAR |
| bentuk turunan/keluarga bernilai nol | 5 | TERKENDALI |
| Function-Word-ID tersedia | 16 | TERDAFTAR |
| Sentence-ID master tersedia | 81 | TERDAFTAR |
| bentuk kalimat panduan yang cocok persis dengan master | 22 | TERLACAK |
| bentuk kalimat lengkap panduan yang belum memiliki Sentence-ID persis | 23 | TEMUAN TERBUKA |
| siklus berstatus SIAP INTEGRASI | 0/3 | GATE NOT RUN |

Angka 22 dan 23 mengukur bentuk kalimat lengkap dalam naskah guru, bukan seluruh kemunculan unsur Arab. Penyebutan lema tunggal, pasangan kosa kata, atau prompt parsial tidak wajib menjadi Sentence-ID, tetapi tetap harus menunjuk AR-LEX atau AR-FW.

## 3. Matriks P001–P040

| Halaman | Cycle-ID | Objek utama | Kalimat/teks terdaftar yang relevan | Status audit |
|---|---|---|---|---|
| P001 | AR-CYC-000001 | AR-LEX-000001–000002 | belum perlu; model lema | TERLACAK |
| P002 | AR-CYC-000001 | AR-LEX-000003–000004 | belum perlu; model lema | TERLACAK |
| P003 | AR-CYC-000001 | AR-LEX-000005–000006 | AR-SEN-000012–000013 dapat dipakai setelah pola dibuka | TERLACAK |
| P004 | AR-CYC-000001 | AR-LEX-000007–000008 | AR-SEN-000005–000006 | TERLACAK |
| P005 | AR-CYC-000001 | AR-LEX-000009–000010 | AR-SEN-000007–000008 | TERLACAK |
| P006 | AR-CYC-000001 | AR-LEX-000011; AR-FW-000001 | AR-SEN-000009; review AR-SEN-000001–000002 | TERLACAK |
| P007 | AR-CYC-000001 | AR-LEX-000013; AR-FW-000001 | AR-SEN-000010 | TERLACAK |
| P008 | AR-CYC-000001 | AR-LEX-000015–000016; AR-FW-000001–000002 | AR-SEN-000011, 000016 | TERLACAK |
| P009 | AR-CYC-000001 | AR-LEX-000012, 000014; AR-FW-000003–000004 | AR-SEN-000014–000024 | TERLACAK |
| P010 | AR-CYC-000001 | AR-GATE-000008–000013 | AR-TXT-000002 hanya bila SIAP INTEGRASI | GATE NOT RUN |
| P011 | AR-CYC-000002 | AR-LEX-000017–000018 | dua model identifikasi belum memiliki Sentence-ID persis | HOLD-SENTENCE-ID |
| P012 | AR-CYC-000002 | AR-LEX-000019–000020 | dua model identifikasi belum memiliki Sentence-ID persis | HOLD-SENTENCE-ID |
| P013 | AR-CYC-000002 | AR-LEX-000021–000022 | model `هٰذَا سَرِيرٌ جَدِيدٌ` belum ber-ID | HOLD-SENTENCE-ID |
| P014 | AR-CYC-000002 | AR-LEX-000023–000024 | AR-SEN-000026–000027 | TERLACAK |
| P015 | AR-CYC-000002 | AR-LEX-000025–000026 | AR-SEN-000028; model pena kecil belum ber-ID | HOLD-SENTENCE-ID |
| P016 | AR-CYC-000002 | AR-LEX-000027–000028 | AR-SEN-000029; model masjid dekat belum ber-ID | HOLD-SENTENCE-ID |
| P017 | AR-CYC-000002 | AR-LEX-000029–000030 | dua model demonstratif belum ber-ID persis | HOLD-SENTENCE-ID |
| P018 | AR-CYC-000002 | review AR-LEX-000001–000030 | tidak ada target baru | TERLACAK |
| P019 | AR-CYC-000002 | AR-LEX-000031; AR-FW-000005–000006 | AR-SEN-000033–000034, 000039; satu model `فِي` belum ber-ID | HOLD-SENTENCE-ID |
| P020 | AR-CYC-000002 | AR-GATE-000014–000020 | AR-TXT-000003 hanya bila SIAP INTEGRASI | GATE NOT RUN |
| P021 | AR-CYC-000003 | AR-LEX-000032–000033 | bentuk tanpa objek belum ber-ID; bentuk lengkap tersedia AR-SEN-000059–000060 | HOLD-SENTENCE-ID |
| P022 | AR-CYC-000003 | AR-LEX-000034–000035 | bentuk tanpa pelengkap belum ber-ID; bentuk lengkap tersedia AR-SEN-000061–000062 | HOLD-SENTENCE-ID |
| P023 | AR-CYC-000003 | AR-LEX-000036–000037 | agen pada panduan berbeda dari AR-SEN-000063–000064 | HOLD-SENTENCE-ID |
| P024 | AR-CYC-000003 | AR-LEX-000038–000039; AR-FW-000014 | AR-SEN-000065–000066 | TERLACAK |
| P025 | AR-CYC-000003 | AR-LEX-000040–000041 | dua model panduan belum ber-ID persis; model alternatif tersedia sebagian | HOLD-SENTENCE-ID |
| P026 | AR-CYC-000003 | AR-LEX-000042–000043 | dua model panduan belum ber-ID | HOLD-SENTENCE-ID |
| P027 | AR-CYC-000003 | AR-LEX-000044–000045; AR-FW-000013 | bentuk lampau belum ber-ID; bentuk kini tersedia AR-SEN-000058, 000081 | HOLD-SENTENCE-ID |
| P028 | AR-CYC-000003 | AR-GATE-000001–000007 | AR-TXT-000001 hanya bila SIAP INTEGRASI | GATE NOT RUN |
| P029 | pemeliharaan | AR-CYC-000001 | AR-TXT-000002 jika pernah dibuka sah | BERSYARAT |
| P030 | pemeliharaan | AR-CYC-000002 | AR-TXT-000003 jika pernah dibuka sah | BERSYARAT |
| P031 | pemeliharaan | AR-LEX-000001–000030 | pilih hanya AR-SEN terdaftar atau kombinasi yang telah diberi ID | KENDALI TRANSFER |
| P032 | pemeliharaan | AR-LEX-000001–000045 | pilih hanya AR-SEN terdaftar atau kandidat tercatat | KENDALI TRANSFER |
| P033 | pemeliharaan | inventaris valid | substitusi agen/objek wajib dicatat sebagai kandidat bila menghasilkan kalimat baru | KENDALI TRANSFER |
| P034 | pemeliharaan | AR-TXT-000001 | hanya bila siklus pernah SIAP INTEGRASI | BERSYARAT |
| P035 | pemeliharaan | inventaris valid | kombinasi baru tidak otomatis menjadi materi resmi | KENDALI TRANSFER |
| P036 | pemeliharaan | review ringan | tidak ada target baru | TERLACAK |
| P037 | pemeliharaan | objek berbasis bukti kelas | remedial harus menunjuk Error-Code/Support-Code | BERSYARAT BUKTI |
| P038 | pemeliharaan | AR-TXT-000001 | tema adab; bukan kutipan ayat/hadis | BERSYARAT |
| P039 | pemeliharaan | satu teks lama sah | pilih hanya teks yang telah dibuka melalui gerbang | BERSYARAT |
| P040 | pemeliharaan | semua siklus | diagnostik; tanpa ambang universal | TERLACAK |

## 4. Daftar 23 Kalimat yang Belum Memiliki Sentence-ID Persis

| No. | Halaman | Kandidat naskah guru | Tindakan wajib |
|---:|---|---|---|
| 1 | P011 | هٰذَا فَصْلٌ. | registrasi atau ganti dengan bentuk master |
| 2 | P011 | هٰذِهِ غُرْفَةٌ. | registrasi atau ganti |
| 3 | P012 | هٰذِهِ مَدْرَسَةٌ. | registrasi atau ganti |
| 4 | P012 | هٰذِهِ نَافِذَةٌ. | registrasi atau ganti |
| 5 | P013 | هٰذَا سَرِيرٌ جَدِيدٌ. | registrasi setelah review bahasa |
| 6 | P015 | هٰذَا قَلَمٌ صَغِيرٌ. | registrasi setelah review konteks |
| 7 | P016 | هٰذَا مَسْجِدٌ قَرِيبٌ. | registrasi setelah review konteks |
| 8 | P017 | هٰذَا بَابٌ مَفْتُوحٌ. | registrasi setelah review bahasa |
| 9 | P017 | هٰذَا مَسْجِدٌ بَعِيدٌ. | registrasi setelah review konteks |
| 10 | P019 | الْقَلَمُ فِي الْحَقِيبَةِ. | registrasi; tautkan AR-FW-000005 |
| 11 | P021 | قَرَأَ الطَّالِبُ. | registrasi atau gunakan AR-SEN-000059 |
| 12 | P021 | كَتَبَ الطَّالِبُ. | registrasi atau gunakan AR-SEN-000060 |
| 13 | P022 | جَلَسَ الطَّالِبُ. | registrasi atau gunakan AR-SEN-000061 |
| 14 | P022 | ذَهَبَ الطَّالِبُ. | registrasi atau gunakan AR-SEN-000062 |
| 15 | P023 | فَتَحَ الطَّالِبُ الْبَابَ. | registrasi atau samakan agen master |
| 16 | P023 | أَغْلَقَ الطَّالِبُ الْبَابَ. | registrasi atau samakan agen master |
| 17 | P025 | شَرِبَ الطَّالِبُ الْمَاءَ. | registrasi atau samakan agen master |
| 18 | P025 | أَكَلَ الطَّالِبُ. | registrasi setelah lengkapi konteks bila perlu |
| 19 | P026 | نَامَ الْوَلَدُ. | registrasi |
| 20 | P026 | قَامَ الْوَلَدُ. | registrasi |
| 21 | P027 | سَمِعَ الطَّالِبُ الْمُعَلِّمَ. | registrasi atau gunakan AR-SEN-000081 |
| 22 | P027 | نَظَرَ الطَّالِبُ إِلَى الْكِتَابِ. | registrasi atau gunakan AR-SEN-000058 |
| 23 | P028 | يَفْتَحُ الْمُعَلِّمُ الْمُصْحَفَ. | bagian AR-TXT-000001; perlu Sentence-ID atau aturan pengecualian teks |

Kalimat-kalimat tersebut secara linguistik belum dinyatakan salah. Temuannya adalah **ketiadaan identitas sumber yang persis**, sehingga kalimat tidak boleh dianggap VALIDATED hanya karena telah muncul dalam panduan.

## 5. Ketentuan Pengendalian

1. Sebelum uji kelas, 23 kandidat harus dipilih: didaftarkan, diganti dengan Sentence-ID yang sudah ada, atau ditolak.
2. Registrasi wajib memuat teks tervokalisasi, arti, AR-LEX/AR-FAM, AR-FW, AR-GRM, AR-FUN, Stage-ID, halaman pertama, status, validator, dan bukti.
3. Perubahan agen, objek, kala, jenis, atau pelengkap menghasilkan bentuk contoh berbeda dan harus dapat diaudit.
4. Kombinasi produktif spontan peserta tidak harus semuanya menjadi materi master; tetapi contoh yang dicetak atau dimodelkan guru secara baku harus mempunyai ID.
5. Teks kumulatif tidak boleh dibuka sebelum gerbang siklus berstatus SIAP INTEGRASI.
6. Temuan ini tidak mengurangi hasil audit 40/40 struktur halaman, tetapi mencegah klaim kesiapan isi.

## 6. Keputusan Audit

- Struktur keterlacakan halaman: **LULUS BERSYARAT**.
- Keterlacakan kalimat naskah guru: **BELUM LULUS — 23 kandidat terbuka**.
- Gerbang integrasi: **0/3 SIAP; seluruhnya GATE NOT RUN**.
- BLOCKED-CUR-ARB-001 dan BLOCKED-CUR-ARB-002: **tetap OPEN**.
- PR #2: **tetap Draft**.

Audit berikutnya harus menutup daftar 23 kandidat dan menjalankan validasi ahli; tidak boleh menaikkan status hanya dengan menambahkan nomor ID.