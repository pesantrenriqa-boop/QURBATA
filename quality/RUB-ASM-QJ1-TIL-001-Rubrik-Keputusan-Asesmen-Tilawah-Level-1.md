# RUB-ASM-QJ1-TIL-001 — Rubrik Keputusan Asesmen Tilawah Level 1

**Document-ID:** RUB-ASM-QJ1-TIL-001  
**Versi:** 0.1.0-id  
**Status:** DRAFT TERKENDALI  
**Tanggal:** 29 Juli 2026  
**Pengendali:** QCF-QUR-003, REG-ASM-QJ1-001, SMP-ASM-QJ1-TIL-001  
**Cakupan:** ASM-QJ1-TIL-001 sampai ASM-QJ1-TIL-006  
**Cabang kerja:** `feature/qj1-master-structure`

## 1. Fungsi

Rubrik ini mengendalikan pencatatan performa dan keputusan sementara asesmen Tilawah Level 1. Rubrik belum menjadi standar kelulusan final sampai direview ahli dan diuji melalui pilot.

## 2. Dimensi Analitik

| Dimensi | Yang diamati |
|---|---|
| Identitas | ketepatan mengenali dan menyebut huruf |
| Titik | ketepatan membedakan posisi/jumlah titik |
| Bunyi | ketepatan pelafalan bunyi sasaran |
| Harakat | ketepatan fathah, kasrah, dan dhammah |
| Urutan | tidak menambah, mengurangi, atau menukar unsur |
| Kelancaran | kesinambungan tanpa jeda berlebihan |
| Kemandirian | tingkat bantuan yang dibutuhkan |
| Retensi | kemampuan mempertahankan materi setelah jeda |
| Transfer | kemampuan membaca rangkaian baru dari unsur yang telah dipelajari |

## 3. Skala Deskriptif Kandidat

| Status | Deskripsi |
|---|---|
| NOT-ASSESSED | asesmen belum dilaksanakan atau bukti tidak memadai |
| EMERGING | sebagian target dikenali tetapi bantuan masih dominan |
| DEVELOPING | mayoritas target dapat dilakukan dengan bantuan terbatas; kesalahan material masih muncul |
| PROVISIONAL-MASTERY | performa kandidat memenuhi kriteria sementara tanpa kesalahan kritis berulang |
| RETEST-REQUIRED | bukti menunjukkan perlunya remedial dan uji ulang |
| BLOCKED | asesmen tidak sah karena prasyarat, instrumen, safeguarding, atau validasi belum terpenuhi |

## 4. Kesalahan Material

Kesalahan berikut wajib dicatat secara analitik:

- E-ID — salah identitas huruf;
- E-DOT — salah atau mengabaikan titik;
- E-VOW — salah harakat;
- E-SEQ — salah urutan;
- E-OMI — menghilangkan unsur;
- E-ADD — menambah unsur;
- E-GUESS — menebak tanpa proses membaca;
- E-DEP — ketergantungan dominan pada model/prompt.

Batas numerik final belum ditetapkan. Sampai review selesai, keputusan tidak boleh hanya menggunakan jumlah salah total; pola dan jenis kesalahan harus dianalisis.

## 5. Aturan Keputusan Sementara

### EMERGING

Diberikan apabila peserta:

- baru mengenali sebagian target;
- sering memerlukan S3 atau S4;
- belum stabil membedakan keluarga huruf;
- belum dapat menjaga urutan dua atau tiga unsur.

### DEVELOPING

Diberikan apabila peserta:

- mengenali mayoritas target;
- mampu membaca sebagian besar sampel dengan S0–S2;
- masih memiliki kesalahan material yang perlu remedial;
- belum menunjukkan retensi atau transfer yang stabil.

### PROVISIONAL-MASTERY

Hanya dapat diberikan apabila:

1. prasyarat halaman terpenuhi;
2. sampel sesuai whitelist materi;
3. performa mayoritas menggunakan S0 atau S1;
4. tidak ada pola pertukaran identitas/titik/harakat yang berulang;
5. rangkaian dua dan tiga unsur dibaca sesuai urutan;
6. bukti retensi dekat tersedia;
7. tidak ada masalah integritas atau safeguarding asesmen.

Status ini bukan MASTERED dan wajib diuji ulang setelah interval retensi yang kelak ditetapkan.

### RETEST-REQUIRED

Diberikan apabila:

- kesalahan material berulang;
- performa berubah tajam antarbagian;
- bantuan S3/S4 dominan;
- retensi gagal;
- instruksi atau kondisi asesmen tidak cukup adil untuk keputusan akhir.

## 6. Remedial Kandidat

| Temuan | Remedial |
|---|---|
| E-ID/E-DOT | kembali ke kontras bentuk keluarga huruf |
| E-VOW | talqin ulang bunyi harakat dengan sampel terbatas |
| E-SEQ/E-OMI/E-ADD | latihan urutan dua unsur sebelum tiga unsur |
| E-GUESS | perlambat tempo dan wajibkan menunjuk tiap unsur |
| E-DEP | kurangi model bertahap dari S4 menuju S0 |
| gagal retensi | jadwalkan murojaah dekat lalu berjarak |

## 7. Aturan Retest

1. Retest tidak boleh menggunakan urutan sampel identik.
2. Unsur dan tingkat kesulitan harus setara dengan asesmen awal.
3. Remedial harus tercatat sebelum retest.
4. Retest wajib memiliki Evidence-ID tersendiri setelah sistem bukti diaktifkan.
5. Jumlah retest dan interval final menunggu validasi ahli.

## 8. Safeguarding

- asesmen tidak boleh mempermalukan peserta;
- kesalahan tidak diumumkan kepada kelompok tanpa tujuan pedagogis yang aman;
- perekaman hanya dilakukan bila mempunyai dasar, persetujuan, penyimpanan, dan masa retensi yang sah;
- guru tidak boleh menggunakan ancaman, ejekan, atau perbandingan yang merendahkan;
- kebutuhan khusus dan kondisi peserta harus dicatat secara proporsional.

## 9. Gate Aktivasi

Rubrik baru dapat berstatus ACTIVE setelah:

1. review ahli Tilawah/Qira'at;
2. review ahli asesmen;
3. review safeguarding;
4. pilot dengan sampel peserta yang sah;
5. analisis pola kesalahan dan konsistensi penilai;
6. revisi kriteria keputusan;
7. Evidence-ID validasi;
8. Decision-ID aktivasi.

## 10. Batas Klaim

- Rubrik ini belum membuktikan validitas atau reliabilitas.
- Belum ada batas skor final.
- Belum ada peserta yang dinyatakan lulus melalui rubrik ini.
- Progres proyek tidak otomatis naik hanya karena rubrik dibuat.

## 11. Riwayat

| Versi | Tanggal | Ringkasan |
|---|---|---|
| 0.1.0-id | 29 Juli 2026 | Rubrik kandidat keputusan, remedial, retest, dan safeguarding Tilawah Level 1 |