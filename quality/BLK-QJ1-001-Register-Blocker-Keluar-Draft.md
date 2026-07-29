# BLK-QJ1-001 — Register Blocker Keluar-Draft Jilid 1

**Register-ID:** BLK-QJ1-001  
**Status:** OPEN  
**Tanggal:** 28 Juli 2026  
**Cakupan:** PR #2 — Buku QURBATA Jilid 1

## 1. Blocker Materi dan Keilmuan

| Blocker-ID | Lokasi | Kebutuhan | Pemilik Keputusan | Status |
|---|---|---|---|---|
| BLOCKED-CUR-HAF-001 | QJ1-P018 | Teks Hafalan 1, sumber, batas potongan, model bacaan, Hafalan Object-ID, pengesah | Pemilik Akademik + ahli | OPEN |
| BLOCKED-CUR-ARB-001 | QJ1-P001–P040/P028 | Validasi ahli atas model bahasa dan AR-SEN-000082–000096, model pelafalan, batas literasi, keputusan gerbang, Arabic Learning Object-ID, serta otorisasi | Pemilik Akademik + ahli Bahasa Arab | OPEN — PRODUK SIAP REVIEW |
| BLOCKED-CUR-ARB-002 | Jilid 1–8 | Validasi ACP-QUR-001 dan pemetaan Stage-ID/AR-LEX/AR-GRM/AR-FUN/AR-ASM ke jilid dan halaman | Pemilik Akademik + panel ahli | OPEN |
| BLOCKED-CUR-HAF-002 | QJ1-P036 | Teks Hafalan 2, sumber, batas potongan, model bacaan, Hafalan Object-ID, pengesah | Pemilik Akademik + ahli | OPEN |
| BLOCKED-CUR-HAD-001 | Jilid 1–8 | Inventaris hadis akhlak sahih, audit keunikan Full-Hadith-ID, takhrij, terjemah, mapping halaman, whitelist, asesmen, dan otorisasi | Pemilik Akademik + ahli hadis/syar‘i | OPEN — KANDIDAT JILID 1 LENGKAP, VALIDASI BELUM ADA |
| BLOCKED-ORTHO-QJ1-001 | QJ1-P033 | Verifikasi fungsi, penulisan, dan penyajian ءُ dalam urutan Jilid 1 | Ahli Bahasa Arab/Qira’at | OPEN |

## 1A. Substatus Blocker Tahfidz

| Komponen | Bukti | Status |
|---|---|---|
| kandidat Hafalan 1 | Al-Fatihah ayat 1–3; PROP-CUR-QJ1-001 | PROPOSED |
| kandidat Hafalan 2 | Al-Fatihah ayat 4–7 + murojaah ayat 1–3; PROP-CUR-QJ1-001 | PROPOSED |
| pemetaan halaman | MAP-HAF-QJ1-001; P001–P040 | COMPLETE-DRAFT |
| pola akuisisi dan murojaah | sima’, talqin, recall, penyambungan, distributed review, delayed retention | COMPLETE-DRAFT |
| Hafalan Object-ID | HAF-000001–000003 terdaftar di REG-CUR-001 | PROPOSED-INACTIVE |
| Decision Record aktivasi | DEC-CUR-004 | PROPOSED — keputusan/bukti belum diisi |
| audit keterlacakan | AUD-HAF-QJ1-001; mapping 40/40 dan Object-ID global | COMPLETE-DRAFT |
| keputusan Pemilik Akademik | setuju/ubah/tolak dan Decision-ID | NOT PROVIDED |
| teks dan sumber resmi | teks Utsmani, nomor ayat, versi sumber, hak penggunaan | NOT PROVIDED |
| tashih dan model bacaan | ahli Al-Qur’an/Qira’at, tajwid, waqaf-ibtida’, audio | NOT PROVIDED |
| rubrik checkpoint | RUB-HAF-QJ1-001 dan FRM-HAF-QJ1-001 untuk P018, P036, dan P040 | COMPLETE-DRAFT |
| paket validasi ahli | REV-HAF-QJ1-001: sumber, teks, ayat, potongan, audio, mapping, rubrik, safeguarding, dan form keputusan | READY-FOR-EXPERT |
| safeguarding dan uji beban | durasi lima menit, remedial, penghentian aman | NOT PROVIDED |

Pemetaan halaman mengurangi ketidakjelasan implementasi, tetapi tidak menutup BLOCKED-CUR-HAF-001/002 sebelum keputusan dan bukti ahli tersedia.

## 1B. Substatus Blocker Bahasa Arab

| Komponen | Bukti | Status |
|---|---|---|
| baseline kosa kata Jilid 1 | 45 entri aktual; 40 target terhitung; turunan tidak dihitung ulang | COMPLETE-DRAFT |
| master kalimat | 96 Sentence-ID unik; 0 duplikasi | COMPLETE-DRAFT |
| struktur/fungsi | AR-GRM dan AR-FUN-000001–000008 terdaftar | COMPLETE-DRAFT |
| pemetaan halaman | MAP-ARB-QJ1-001; P001–P040 | COMPLETE-DRAFT |
| panduan guru lima menit | GDE-ARB-QJ1-001; 40 halaman | COMPLETE-DRAFT |
| penanaman sumber ke halaman | 40/40 memiliki Sentence-ID/Text-ID dan status; 0 hilang/duplikat | COMPLETE-DRAFT |
| audit keterlacakan | AUD-ARB-QJ1-002 | COMPLETE-DRAFT |
| paket ahli 15 kalimat | REV-ARB-QJ1-002; 15/15 PRECHECK-PASS | READY-FOR-EXPERT |
| keputusan ahli kalimat | 15/15 keputusan dan Evidence-ID | NOT PROVIDED |
| validasi 81 kalimat terdahulu dan tiga teks | bukti ahli bahasa/pedagogi/syar‘i | NOT PROVIDED |
| model pelafalan/audio resmi | sumber, pengisi suara, review, hak penggunaan | NOT PROVIDED |
| batas audiens sumber halaman | 40/40 segmen berlabel GURU dan bukan teks baca peserta; larangan tampil sebelum whitelist/editorial/render | COMPLETE-DRAFT |
| audit silang whitelist sumber | AUD-ARB-QJ1-003; 40/40 segmen HOLD-PARTICIPANT, 0/40 izin teks baca peserta | COMPLETE-DRAFT |
| otomasi layout cetak | generator A5 potret, Amiri Quran 1.003, bleed, crop marks, grid 3×8, cover contoh, identitas, panel integrasi, rekam guru, RTL deterministik, dan preflight | COMPLETE-DRAFT |
| build penuh buku peserta | PDF 42 halaman: cover + identitas + 36×24 butir + 4 halaman khusus; render diperiksa | TECHNICAL-PASS |
| persetujuan produksi cetak | proof keterbacaan Amiri Quran 18 pt, cover, CMYK, proof fisik, percetakan, Evidence-ID | NOT PROVIDED |
| whitelist produk render peserta | prototipe A5 potret 42 halaman: 0 kebocoran marker guru; render final dan Evidence-ID tetap diperlukan | PROTOTYPE TECHNICAL-PASS / FINAL OPEN |
| gerbang siklus | P010, P020, P028 | 0/3 SIAP; GATE NOT RUN |
| safeguarding dan uji durasi kelas | bukti pelaksanaan dan tindak lanjut | NOT PROVIDED |
| otorisasi akademik dan Document Controller | keputusan, tanggal, audit trail | NOT PROVIDED |

COMPLETE-DRAFT berarti artefak telah tersedia dan terlacak, bukan telah divalidasi atau disahkan. Karena unsur NOT PROVIDED dan OPEN masih material, BLOCKED-CUR-ARB-001/002 tetap OPEN.

## 1C. Substatus Blocker Hadis Akhlak

| Komponen | Bukti | Status |
|---|---|---|
| progression Jilid 1–8 | HCP-QUR-001 | COMPLETE-DRAFT |
| sumber tunggal dan skema deduplikasi | REG-HAD-001 | COMPLETE-DRAFT |
| kapasitas desain | sampai 320 slot; kuota final belum disahkan | CONTROLLED-ASSUMPTION |
| kandidat Hadith-ID | HAD-000001–000040 dalam BAT-HAD-001–005; 40 kandidat, 0 aktif | SOURCE-CHECK |
| sumber dan metadata grading awal | 40/40 memiliki locator awal; takhrij/edisi final belum disahkan | COMPLETE-CANDIDATE / EXPERT REVIEW OPEN |
| terjemah, whitelist, asesmen, safeguarding | belum ada | NOT PROVIDED |
| mapping halaman Jilid 1–8 | MAP-HAD-QJ1-001 v0.2 memetakan intro, interval 1/3/7/14, checkpoint maksimum 8 prompt, dan carryover; validasi serta Jilid 2–8 belum ada | COMPLETE-DRAFT / PILOT OPEN |
| pra-audit internal | AUD-HAD-QJ1-001: identitas/mapping lengkap; overload checkpoint dikoreksi; klaster tema, usia, dan safeguarding dipetakan | COMPLETE-INTERNAL / EXPERT OPEN |
| paket review ahli | REV-HAD-QJ1-001 memuat matriks 40 objek, audit murojaah, risiko, dan form keputusan | READY-FOR-EXPERT |
| rubrik dan form pilot | RUB-HAD-QJ1-001 + FRM-HAD-QJ1-001; dimensi perkembangan, checkpoint, log frekuensi, carryover, dan safeguarding | READY-FOR-PILOT-AUTHORIZATION |
| protokol dan otorisasi pilot | PRO-HAD-QJ1-001 bertahap; DEC-HAD-QJ1-001 kosong dan efektif NO-GO | READY-FOR-AUTHORIZATION / NOT ACTIVE |
| data pilot | durasi, load aktual, retensi, remedial, dan frekuensi per peserta belum ada | NOT PROVIDED |
| hasil review, Reviewer-ID, Evidence-ID, Decision-ID | belum ada | NOT PROVIDED |

Arsitektur, inventaris 40 kandidat, mapping murojaah, dan paket ahli menutup gap desain Jilid 1. BLOCKED-CUR-HAD-001 tetap OPEN sampai takhrij, validasi, whitelist, uji durasi, bukti, dan otorisasi tersedia.

## 2. Usulan Penutupan yang Tersedia

[PROP-CUR-QJ1-001](https://github.com/pesantrenriqa-boop/QURBATA/blob/feature/qj1-master-structure/quality/PROP-CUR-QJ1-001-Usulan-Materi-Khusus.md) telah menyiapkan rekomendasi terkontrol:

- P018: Surah Al-Fatihah ayat 1–3;
- P028: rekomendasi tema lama superseded parsial; MAP-ARB-QJ1-001 kini menyediakan pemetaan pilot P001–P040 dan kandidat AR-CYC-000003/AR-TXT-000001, tetapi belum divalidasi;
- P036: Surah Al-Fatihah ayat 4–7 disertai murojaah ayat 1–3.

Proposal belum mengikat dan tidak mengubah status blocker. Pemilik Akademik harus memilih, lalu ahli terkait memverifikasi sumber, teks, vokalisasi, pelafalan, beban, serta kelayakannya.

## 3. Gate Penelaahan

| Gate-ID | Cakupan hasil pindai | Bukti yang Dibutuhkan | Status |
|---|---:|---|---|
| GATE-ACA-QJ1 | 39 halaman menunggu pemeriksa akademik | Nama, tanggal, temuan, keputusan, tanda persetujuan | OPEN |
| GATE-EDT-QJ1 | 39 halaman menunggu pemeriksa editorial | Koreksi bahasa, konsistensi istilah, layout source | OPEN |
| GATE-RND-QJ1 | build 40/40 dan audit internal render lulus; proof serta otorisasi belum tersedia | Font produksi, review 40 halaman, proof fisik, percetakan, Evidence-ID | OPEN — TECHNICAL BUILD PASS |
| GATE-ASM-QJ1 | 38 halaman memerlukan telaah asesmen | Rubrik, bukti, aturan keputusan, bentuk paralel | OPEN |
| GATE-SAFE-QJ1 | 40 halaman memerlukan safeguarding | Beban, bahasa rahmah, penghentian aman, non-stigmatisasi | OPEN |
| GATE-AUTH-QJ1 | 38 halaman menunggu pengesah | Identitas otoritas dan keputusan eksplisit | OPEN |

Jumlah berasal dari audit metadata otomatis dan harus dikonfirmasi Document Controller saat review.

## 4. Gate Makro Keluar-Draft

| No. | Gate Makro | Status |
|---:|---|---|
| 1 | Struktur 40 halaman lengkap | COMPLETE |
| 2 | Audit otomatis distribusi dan whitelist | COMPLETE |
| 3 | Keputusan materi khusus | OPEN |
| 4 | Review akademik/Arab/Qira’at | OPEN |
| 5 | Review editorial dan render | OPEN |
| 6 | Validasi asesmen dan safeguarding | OPEN |
| 7 | Otorisasi serta audit trail persetujuan | OPEN |
| 8 | Penutupan seluruh blocker | OPEN |

Kesiapan keluar-Draft berbasis gate saat ini: **2 dari 8 gate makro selesai (25%)**. Angka ini bukan persentase efektivitas buku atau persentase keseluruhan proyek QURBATA.

Persentase keseluruhan proyek QURBATA Jilid 1–8 dicatat terpisah dalam `STAT-QUR-001`; baseline 28 Juli 2026 adalah **30%**.

## 5. Urutan Tindak Lanjut

1. Pemilik Akademik menetapkan panel ahli hadis/syar‘i, standar sumber/locator, dan metode takhrij untuk mengisi REG-HAD-001 tanpa duplikasi.
2. Pemilik Akademik menilai kandidat dan MAP-HAF-QJ1-001, lalu menetapkan atau mengubah materi Hafalan 1 dan Hafalan 2 serta memastikan ruang lingkup review Bahasa Arab.
3. Ahli Bahasa Arab mengisi REV-ARB-QJ1-002, menilai 81 kalimat terdahulu dan tiga teks, lalu mencatat Evidence-ID.
4. Ahli memverifikasi ءُ, model pelafalan, batas literasi, dan kandidat leksikal; gunakan AUD-ARB-QJ1-003 sebagai baseline, lalu editorial/render membuktikan bahwa naskah guru tidak bocor menjadi bacaan peserta.
5. Pemeriksa akademik menelaah urutan, bentuk, harakat, makhraj, dan beban.
6. Editorial serta render memeriksa seluruh sumber halaman.
7. Tim asesmen dan safeguarding mengesahkan rubrik serta kontrol peserta.
8. Document Controller mencatat bukti, versi, penutupan blocker, dan otorisasi.
9. PR baru dapat dipertimbangkan keluar dari Draft.

## 6. Riwayat

| Versi | Tanggal | Ringkasan |
|---|---|---|
| 0.27.0-id | 29 Juli 2026 | Menambahkan PRO-HAD-QJ1-001 dan DEC-HAD-QJ1-001; pilot dibagi lima fase dan tetap NO-GO sampai otorisasi |
| 0.26.0-id | 29 Juli 2026 | Menambahkan RUB-HAD-QJ1-001 dan FRM-HAD-QJ1-001; instrumen pilot siap-draf tanpa data, persetujuan, atau Evidence-ID |
| 0.25.0-id | 29 Juli 2026 | Menambahkan AUD-HAD-QJ1-001 dan mengoreksi checkpoint 39 menjadi maksimum 8 prompt; carryover Jilid 2 diwajibkan |
| 0.24.0-id | 29 Juli 2026 | Menambahkan MAP-HAD-QJ1-001 dan REV-HAD-QJ1-001; mapping kandidat serta paket keputusan ahli lengkap-draf, 0 APPROVED |
| 0.23.0-id | 29 Juli 2026 | Menambahkan BAT-HAD-005 dan HAD-000033–000040; kandidat Jilid 1 lengkap 40/40, 0 APPROVED; audit ahli dan mapping murojaah tetap OPEN |
| 0.22.0-id | 29 Juli 2026 | Menambahkan BAT-HAD-004 dan HAD-000025–000032; akumulasi 32 kandidat, 0 APPROVED |
| 0.21.0-id | 29 Juli 2026 | Menambahkan BAT-HAD-003 dan HAD-000017–000024; akumulasi 24 kandidat, 0 APPROVED |
| 0.20.0-id | 29 Juli 2026 | Menambahkan BAT-HAD-002 dan HAD-000009–000016; akumulasi 16 kandidat, 0 APPROVED |
| 0.19.0-id | 29 Juli 2026 | Menambahkan BAT-HAD-001 dan HAD-000001–000008; sumber awal tersedia, tetapi 0 APPROVED dan review ahli tetap OPEN |
| 0.18.0-id | 29 Juli 2026 | Menambahkan HCP-QUR-001 dan REG-HAD-001; arsitektur Hadis Akhlak lintas Jilid 1–8 tersedia, tetapi objek, takhrij, mapping, dan validasi tetap OPEN |
| 0.17.0-id | 28 Juli 2026 | Menautkan dashboard STAT-QUR-001: progres keseluruhan QURBATA 30%, terpisah dari kesiapan Jilid 1 25% |
| 0.16.0-id | 28 Juli 2026 | Menutup inkonsistensi format Object-ID menjadi HAF-000001–000003 dan menambahkan AUD-HAF-QJ1-001 |
| 0.15.0-id | 28 Juli 2026 | Mendaftarkan HAF-000001–000003 sebagai PROPOSED-INACTIVE dan menyiapkan DEC-CUR-004 tanpa mengaktifkan objek |
| 0.14.0-id | 28 Juli 2026 | Menambahkan REV-HAF-QJ1-001; blocker Tahfidz kini memiliki paket keputusan ahli lengkap tetapi belum memiliki hasil/Evidence-ID |
| 0.13.0-id | 28 Juli 2026 | Menambahkan rubrik dan form bukti checkpoint Tahfidz P018/P036/P040; validasi dan ambang tetap terbuka |
| 0.12.0-id | 28 Juli 2026 | Menambahkan MAP-HAF-QJ1-001 dan substatus Tahfidz; pemetaan P001–P040 selesai-draf tanpa menutup keputusan serta validasi ahli |
| 0.11.0-id | 28 Juli 2026 | Mengubah prototipe ke A5 potret 42 halaman dan menutup audit kebocoran render pada tingkat teknis; finishing/final approval tetap terbuka |
| 0.10.0-id | 28 Juli 2026 | Mengunci A5 lanskap dan Amiri Quran 1.003; build 40/40 serta audit visual ulang lulus teknis |
| 0.9.0-id | 28 Juli 2026 | Build PDF peserta 40/40 lulus teknis; empat halaman khusus dipisahkan; proof dan persetujuan tetap terbuka |
| 0.8.0-id | 28 Juli 2026 | Menambahkan pipeline layout otomatis dan AUD-PRN-QJ1-001; pilot satu halaman lulus, build penuh belum dijalankan |
| 0.7.0-id | 28 Juli 2026 | Menutup audit silang sumber melalui AUD-ARB-QJ1-003; 40/40 ditahan dari area baca peserta, audit render tetap terbuka |
| 0.6.0-id | 28 Juli 2026 | Menetapkan batas audiens guru pada 40/40 sumber halaman; audit whitelist produk render tetap terbuka |
| 0.5.0-id | 28 Juli 2026 | Memecah blocker Bahasa Arab menjadi substatus selesai-draf versus bukti/validasi yang masih terbuka |
| 0.4.0-id | 28 Juli 2026 | Menautkan pemetaan pilot Bahasa Arab tanpa menutup blocker |
| 0.3.0-id | 28 Juli 2026 | Menambahkan blocker validasi dan pemetaan Arabic Competency Progression |
| 0.2.0-id | 28 Juli 2026 | Menautkan usulan materi khusus tanpa menutup blocker |
| 0.1.0-id | 28 Juli 2026 | Register blocker dan gate pertama setelah struktur 40/40 selesai |
