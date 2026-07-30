# REG-QCF-001 — Master Kompetensi QURBATA

**Register-ID:** REG-QCF-001  
**Versi:** 0.1.0-id  
**Status:** DRAFT TERKENDALI  
**Tanggal:** 29 Juli 2026  
**Pengendali:** QCF-QUR-001 dan QCF-QUR-002  
**Cakupan:** Competency-ID program inti QURBATA Level 1–8  
**Cabang kerja:** `feature/qj1-master-structure`

## 1. Fungsi Register

Register ini merupakan sumber tunggal identitas kompetensi QURBATA. Competency-ID tidak boleh dibuat langsung di halaman buku, asesmen, RIQA OS, atau produk turunan tanpa tercatat terlebih dahulu di sini.

Seluruh entri versi 0.1.0-id berstatus **CANDIDATE**. Register belum merupakan validasi ahli dan belum mengaktifkan standar kelulusan.

## 2. Aturan Status

| Status | Makna |
|---|---|
| CANDIDATE | rancangan kompetensi telah dicatat tetapi belum direview |
| REVIEW | sedang berada dalam proses review terdokumentasi |
| BLOCKED | tidak boleh dilanjutkan karena temuan atau prasyarat belum selesai |
| ACTIVE | telah divalidasi, diputuskan, dan boleh digunakan |
| RETIRED | tidak lagi digunakan tetapi riwayatnya dipertahankan |

Perubahan menjadi ACTIVE wajib memiliki Reviewer-ID, Evidence-ID, dan Decision-ID.

## 3. Struktur Data Minimum

| Field | Ketentuan |
|---|---|
| Competency-ID | unik, permanen, tidak digunakan ulang |
| Domain | TIL, HIF, FAH, AMT, atau KHT |
| Level | 1–8 |
| Pernyataan kompetensi | kemampuan yang dapat diperagakan |
| Prasyarat | Competency-ID sebelumnya atau NONE |
| Indikator minimum | bukti performa yang harus terlihat |
| Mapping | halaman/unit terkait |
| Assessment-ID | instrumen terkendali |
| Evidence-ID | bukti asesmen/validasi |
| Reviewer-ID | penelaah berwenang |
| Decision-ID | keputusan aktivasi/perubahan |
| Status | status terkendali |

## 4. Register Baseline Kompetensi Level 1–8

### 4.1 Domain Tilawah — TIL

| Competency-ID | Level | Pernyataan kompetensi | Prasyarat | Indikator minimum | Mapping | Assessment | Evidence | Status |
|---|---:|---|---|---|---|---|---|---|
| QCF-TIL-L1-001 | 1 | membedakan identitas huruf dan bunyi target yang telah diajarkan | NONE | menunjuk, menyebut, dan melafalkan target tanpa bantuan dominan | MAP-QCF-QJ1-001: TBD | TBD | TBD | CANDIDATE |
| QCF-TIL-L2-001 | 2 | membaca rangkaian dua dan tiga unsur secara stabil | QCF-TIL-L1-001 | menjaga urutan, titik, dan harakat pada sampel terkontrol | Jilid 2: TBD | TBD | TBD | CANDIDATE |
| QCF-TIL-L3-001 | 3 | menerapkan pola baca dasar dan melakukan koreksi mandiri awal | QCF-TIL-L2-001 | memperbaiki kesalahan setelah isyarat minimal | Jilid 3: TBD | TBD | TBD | CANDIDATE |
| QCF-TIL-L4-001 | 4 | membaca potongan Qurani terkontrol sesuai prasyarat | QCF-TIL-L3-001 | tidak menebak dan mempertahankan kaidah pada lafaz nyata | Jilid 4: TBD | TBD | TBD | CANDIDATE |
| QCF-TIL-L5-001 | 5 | membaca ayat dengan kelancaran dan tajwid yang semakin konsisten | QCF-TIL-L4-001 | ketepatan, kelancaran, dan kaidah lulus rubrik | Jilid 5: TBD | TBD | TBD | CANDIDATE |
| QCF-TIL-L6-001 | 6 | membaca bagian panjang dengan tartil terpimpin serta waqaf-ibtida' dasar | QCF-TIL-L5-001 | mempertahankan makhraj, tempo, waqaf, dan adab | Jilid 6: TBD | TBD | TBD | CANDIDATE |
| QCF-TIL-L7-001 | 7 | mengintegrasikan ketepatan, kelancaran, adab, dan performa tilawah | QCF-TIL-L6-001 | menangani sampel baru serta menerima tashih rinci | Jilid 7: TBD | TBD | TBD | CANDIDATE |
| QCF-TIL-L8-001 | 8 | menunjukkan kemandirian bacaan program inti dan kesiapan jalur lanjut | QCF-TIL-L7-001 | lulus ujian akhir yang tervalidasi tanpa klaim sanad otomatis | Jilid 8: TBD | TBD | TBD | CANDIDATE |

### 4.2 Domain Hifzh — HIF

| Competency-ID | Level | Pernyataan kompetensi | Prasyarat | Indikator minimum | Mapping | Assessment | Evidence | Status |
|---|---:|---|---|---|---|---|---|---|
| QCF-HIF-L1-001 | 1 | menirukan dan menjaga unit hafalan sangat pendek melalui talqin | NONE | setoran berurutan dan murojaah pada sesi berikutnya | P018/P036: menunggu validasi | TBD | TBD | CANDIDATE |
| QCF-HIF-L2-001 | 2 | menyetor hafalan pendek dan menjaga murojaah dekat | QCF-HIF-L1-001 | merespons awal unit serta menjaga urutan | Jilid 2: TBD | TBD | TBD | CANDIDATE |
| QCF-HIF-L3-001 | 3 | menjaga beberapa unit hafalan dengan jadwal sederhana | QCF-HIF-L2-001 | mengidentifikasi dan memperbaiki bagian lemah | Jilid 3: TBD | TBD | TBD | CANDIDATE |
| QCF-HIF-L4-001 | 4 | menyambungkan hafalan dan memulihkan bagian lemah dengan bantuan | QCF-HIF-L3-001 | sambung antarbagiannya stabil pada sampel | Jilid 4: TBD | TBD | TBD | CANDIDATE |
| QCF-HIF-L5-001 | 5 | menjaga hafalan melalui murojaah dekat dan berjarak | QCF-HIF-L4-001 | mampu merespons uji sambung/acak sesuai rubrik | Jilid 5: TBD | TBD | TBD | CANDIDATE |
| QCF-HIF-L6-001 | 6 | mempertahankan hafalan lintas-sesi dan menjalankan pemulihan | QCF-HIF-L5-001 | catatan murojaah jujur dan performa retensi tersedia | Jilid 6: TBD | TBD | TBD | CANDIDATE |
| QCF-HIF-L7-001 | 7 | mengelola ayat serupa serta strategi penguat berbasis makna | QCF-HIF-L6-001 | membedakan titik kemiripan tanpa kehilangan urutan mushaf | Jilid 7: TBD | TBD | TBD | CANDIDATE |
| QCF-HIF-L8-001 | 8 | lulus uji hafalan program inti dan memiliki sistem murojaah berkelanjutan | QCF-HIF-L7-001 | mutu, retensi, pemulihan, dan rencana lanjut terbukti | Jilid 8: TBD | TBD | TBD | CANDIDATE |

### 4.3 Domain Fahm — FAH

| Competency-ID | Level | Pernyataan kompetensi | Prasyarat | Indikator minimum | Mapping | Assessment | Evidence | Status |
|---|---:|---|---|---|---|---|---|---|
| QCF-FAH-L1-001 | 1 | mengenali makna sangat dasar dari unsur pilihan | NONE | menghubungkan lafaz dengan makna/konteks sederhana | MAP-QCF-QJ1-001: TBD | TBD | TBD | CANDIDATE |
| QCF-FAH-L2-001 | 2 | mengenali mufradat dan frasa sederhana | QCF-FAH-L1-001 | mengenali serta menggunakan ulang objek yang telah diajarkan | Jilid 2: TBD | TBD | TBD | CANDIDATE |
| QCF-FAH-L3-001 | 3 | memahami hubungan bentuk, bunyi, kata, dan makna dasar | QCF-FAH-L2-001 | menjelaskan hubungan pada sampel terkontrol | Jilid 3: TBD | TBD | TBD | CANDIDATE |
| QCF-FAH-L4-001 | 4 | mengenali tema pendek, struktur dasar, dan pesan utama | QCF-FAH-L3-001 | membedakan terjemah kata dan penjelasan makna | Jilid 4: TBD | TBD | TBD | CANDIDATE |
| QCF-FAH-L5-001 | 5 | memahami mufradat, pola kalimat, dan hubungan makna tingkat awal-menengah | QCF-FAH-L4-001 | menggunakan teks kumulatif setelah gate prasyarat | Jilid 5: TBD | TBD | TBD | CANDIDATE |
| QCF-FAH-L6-001 | 6 | menjelaskan tema, kosakata, struktur, dan hubungan antarbagian | QCF-FAH-L5-001 | menggunakan sumber dan membedakan teks, terjemah, serta tafsir | Jilid 6: TBD | TBD | TBD | CANDIDATE |
| QCF-FAH-L7-001 | 7 | menghubungkan bacaan, Bahasa Arab, tema, dan ayat serupa | QCF-FAH-L6-001 | menyusun penjelasan singkat berbasis sumber | Jilid 7: TBD | TBD | TBD | CANDIDATE |
| QCF-FAH-L8-001 | 8 | menghasilkan penjelasan dan karya Qurani tingkat program inti | QCF-FAH-L7-001 | argumentasi bertanggung jawab dan referensi terlacak | Jilid 8: TBD | TBD | TBD | CANDIDATE |

### 4.4 Domain Amal dan Tazkiyah — AMT

| Competency-ID | Level | Pernyataan kompetensi | Prasyarat | Indikator minimum | Mapping | Assessment | Evidence | Status |
|---|---:|---|---|---|---|---|---|---|
| QCF-AMT-L1-001 | 1 | menunjukkan adab dasar belajar Al-Qur'an | NONE | menyimak, menjaga bahan, dan menerima koreksi | seluruh sesi Jilid 1: TBD | TBD | TBD | CANDIDATE |
| QCF-AMT-L2-001 | 2 | menunjukkan disiplin, giliran, dan sikap anti-ejekan | QCF-AMT-L1-001 | perilaku konsisten dalam observasi berulang | Jilid 2: TBD | TBD | TBD | CANDIDATE |
| QCF-AMT-L3-001 | 3 | menyelesaikan amanah belajar sederhana | QCF-AMT-L2-001 | tugas selesai dan kesulitan dilaporkan dengan adab | Jilid 3: TBD | TBD | TBD | CANDIDATE |
| QCF-AMT-L4-001 | 4 | menerapkan satu nilai Qurani dalam kegiatan harian | QCF-AMT-L3-001 | bukti observasi dan refleksi sederhana tersedia | Jilid 4: TBD | TBD | TBD | CANDIDATE |
| QCF-AMT-L5-001 | 5 | menunjukkan disiplin ibadah, tanggung jawab, dan kepedulian | QCF-AMT-L4-001 | konsistensi lintas-situasi dan anti-bullying | Jilid 5: TBD | TBD | TBD | CANDIDATE |
| QCF-AMT-L6-001 | 6 | melakukan refleksi, perbaikan diri, dan layanan kelompok | QCF-AMT-L5-001 | rencana perbaikan serta bukti tindak lanjut tersedia | Jilid 6: TBD | TBD | TBD | CANDIDATE |
| QCF-AMT-L7-001 | 7 | memimpin dengan adab dan menjaga amanah proyek | QCF-AMT-L6-001 | tugas diselesaikan tanpa merendahkan peserta lain | Jilid 7: TBD | TBD | TBD | CANDIDATE |
| QCF-AMT-L8-001 | 8 | menunjukkan konsistensi adab, amanah, khidmah, dan evaluasi diri | QCF-AMT-L7-001 | portofolio perilaku dan keputusan kelayakan tersedia | Jilid 8: TBD | TBD | TBD | CANDIDATE |

### 4.5 Domain Khidmah dan Tamkin — KHT

| Competency-ID | Level | Pernyataan kompetensi | Prasyarat | Indikator minimum | Mapping | Assessment | Evidence | Status |
|---|---:|---|---|---|---|---|---|---|
| QCF-KHT-L1-001 | 1 | membantu menyiapkan dan merapikan pembelajaran | NONE | tugas sederhana dilakukan tertib | Jilid 1: TBD | TBD | TBD | CANDIDATE |
| QCF-KHT-L2-001 | 2 | bekerja berpasangan dan memberi contoh adab dasar | QCF-KHT-L1-001 | kerja sama berlangsung tanpa mengambil peran guru | Jilid 2: TBD | TBD | TBD | CANDIDATE |
| QCF-KHT-L3-001 | 3 | membantu teman pada materi yang telah dikuasai di bawah arahan | QCF-KHT-L2-001 | bantuan tepat, aman, dan dilaporkan | Jilid 3: TBD | TBD | TBD | CANDIDATE |
| QCF-KHT-L4-001 | 4 | menyampaikan kembali pelajaran singkat dengan panduan | QCF-KHT-L3-001 | isi akurat dan batas kewenangan dipatuhi | Jilid 4: TBD | TBD | TBD | CANDIDATE |
| QCF-KHT-L5-001 | 5 | menghasilkan karya Qurani awal secara terbimbing | QCF-KHT-L4-001 | karya, proses, dan sumber terdokumentasi | Jilid 5: TBD | TBD | TBD | CANDIDATE |
| QCF-KHT-L6-001 | 6 | mendampingi kegiatan terbatas di bawah supervisi | QCF-KHT-L5-001 | tugas layanan selesai dan supervisi tercatat | Jilid 6: TBD | TBD | TBD | CANDIDATE |
| QCF-KHT-L7-001 | 7 | menghasilkan dan mempresentasikan proyek spesialisasi terbimbing | QCF-KHT-L6-001 | karya direview dan direvisi berdasarkan umpan balik | Jilid 7: TBD | TBD | TBD | CANDIDATE |
| QCF-KHT-L8-001 | 8 | melakukan pengabdian awal sesuai kewenangan yang diberikan | QCF-KHT-L7-001 | ruang lingkup, supervisor, dan hasil layanan terdokumentasi | Jilid 8: TBD | TBD | TBD | CANDIDATE |

## 5. Rekapitulasi Register

| Domain | Jumlah kandidat | REVIEW | ACTIVE | BLOCKED | RETIRED |
|---|---:|---:|---:|---:|---:|
| Tilawah | 8 | 0 | 0 | 0 | 0 |
| Hifzh | 8 | 0 | 0 | 0 | 0 |
| Fahm | 8 | 0 | 0 | 0 | 0 |
| Amal/Tazkiyah | 8 | 0 | 0 | 0 | 0 |
| Khidmah/Tamkin | 8 | 0 | 0 | 0 | 0 |
| **Total** | **40** | **0** | **0** | **0** | **0** |

## 6. Ketergantungan Kritis

1. QCF-TIL-L1-001 harus dipetakan ke QJ1-P001–P040 melalui MAP-QCF-QJ1-001.
2. QCF-HIF-L1-001 tidak boleh diaktifkan sebelum materi P018 dan P036 memperoleh validasi Tahfidz/Qira'at.
3. QCF-FAH-L1-001 harus konsisten dengan ACP-QUR-001, REG-ARB-001, serta gate integrasi Bahasa Arab.
4. QCF-AMT-L1-001 memerlukan rubrik observasi aman dan review safeguarding.
5. QCF-KHT-L1-001 tidak boleh berubah menjadi kewenangan mengajar.
6. Semua level memerlukan standar indikator dan penguasaan dari QCF-QUR-003.

## 7. Aturan Perubahan Register

- ID yang telah diterbitkan tidak boleh digunakan ulang.
- Perubahan substansi wajib menaikkan versi dan mencatat alasan.
- Pemecahan satu kompetensi menjadi beberapa kompetensi baru harus menjaga relasi supersedes/superseded-by.
- Entri ACTIVE tidak boleh diedit diam-diam; perubahan memerlukan Decision-ID.
- Penghapusan tidak diperbolehkan; gunakan RETIRED untuk mempertahankan audit trail.
- Field TBD harus ditutup sebelum aktivasi.

## 8. Pekerjaan Berikutnya

1. menyusun QCF-QUR-003 untuk indikator, tingkat bantuan, jenis kesalahan, dan mastery gate;
2. memetakan kandidat Level 1 ke 40 halaman Jilid 1;
3. menetapkan Assessment-ID kandidat;
4. mengirim domain kepada panel reviewer;
5. mencatat temuan, remedial desain, Evidence-ID, dan keputusan aktivasi.

## 9. Batas Klaim

- Empat puluh Competency-ID adalah kandidat arsitektur, bukan empat puluh kompetensi tervalidasi.
- Tidak ada Evidence-ID, Reviewer-ID, atau Decision-ID aktivasi dalam versi ini.
- Register tidak menaikkan gate keluar-Draft Jilid 1 secara otomatis.
- Persentase proyek hanya berubah setelah dashboard berbobot diperbarui berdasarkan artefak dan gate yang sah.

## 10. Riwayat

| Versi | Tanggal | Ringkasan |
|---|---|---|
| 0.1.0-id | 29 Juli 2026 | Membentuk sumber tunggal 40 kandidat Competency-ID untuk lima domain dan delapan level |
