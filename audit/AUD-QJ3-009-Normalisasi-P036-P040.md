# AUD-QJ3-009 — Normalisasi P036–P040 dan Penutupan Draf Isi Jilid 3

**Tanggal:** 30 Juli 2026  
**Tahap:** Audit Tahap II — Batch Akhir  
**Cakupan:** QJ3-P036–QJ3-P040  
**Sumber:** `books/jilid-3/pages/QJ3-B04B-Materi-P036-P040.md`  
**Status:** COMPLETE-STRUCTURAL — MENUNGGU TASHIH AHLI DAN NORMALISASI DATA

## 1. Ringkasan

Batch akhir Jilid 3 telah tersedia sebanyak **5 halaman × 24 kotak = 120 kotak**. Dengan tersedianya batch P036–P040, draf materi Jilid 3 kini mencakup P001–P040. Kelengkapan ini adalah kelengkapan sumber draf, bukan kelulusan akademik, qira’at, rasm, audio, asesmen, atau kesiapan cetak.

| Halaman | Fungsi utama | Kotak | Status struktural |
|---|---|---:|---|
| QJ3-P036 | transfer kata ke frasa bermakna | 24 | COMPLETE-DRAFT |
| QJ3-P037 | potongan Qurani kandidat | 24 | COMPLETE-DRAFT |
| QJ3-P038 | murojaah kompleks | 24 | COMPLETE-DRAFT |
| QJ3-P039 | simulasi kata ke frasa | 24 | COMPLETE-DRAFT |
| QJ3-P040 | evaluasi akhir Jilid 3 | 24 | COMPLETE-DRAFT |

## 2. Pemeriksaan Struktural

- Jumlah halaman: **5**.
- Jumlah kotak: **120**.
- Setiap halaman memuat 24 kotak.
- P036–P037 mengalihkan kemampuan dari kata tunggal menuju potongan berurutan dalam ayat.
- P038 berfungsi sebagai murojaah kompleks dan tidak boleh dihitung sebagai akuisisi lema baru.
- P039 berfungsi sebagai simulasi transfer.
- P040 berfungsi sebagai evaluasi akhir, bukan halaman akuisisi.
- Tidak ditemukan frasa yang secara eksplisit dinyatakan sebagai gabungan kata dari ayat berbeda.
- Pengulangan frasa utuh diperlakukan sebagai tikrar/kelancaran, bukan materi baru.

## 3. Potongan Qurani yang Memerlukan Source-ID Final

| Kandidat | Locator awal | Status |
|---|---|---|
| ٱلْيَوْمَ يَئِسَ | QS Al-Mā’idah 5:3 | PENDING-MUSHAF-VERIFY |
| ٱلْيَوْمَ أَكْمَلْتُ | QS Al-Mā’idah 5:3 | PENDING-MUSHAF-VERIFY |
| ٱلْعَفْوَ وَأْمُرْ | QS Al-A‘rāf 7:199 | PENDING-MUSHAF-VERIFY |
| ٱلْيَوْمَ نَخْتِمُ | QS Yā-Sīn 36:65 | PENDING-MUSHAF-VERIFY |
| ٱلْكِتَابُ لَا رَيْبَ فِيهِ | QS Al-Baqarah 2:2 | PENDING-MUSHAF-VERIFY |
| ٱلْيَوْمَ نَخْتِمُ عَلَىٰ | QS Yā-Sīn 36:65 | PENDING-MUSHAF-VERIFY |
| عَلَىٰ أَفْوَاهِهِمْ | QS Yā-Sīn 36:65 | PENDING-MUSHAF-VERIFY |
| بِمَا كَانُوا يَكْسِبُونَ | QS Yā-Sīn 36:65 | PENDING-MUSHAF-VERIFY |

Semua locator harus diverifikasi terhadap mushaf acuan yang ditetapkan. Source-ID, rasm, qira’at, titik mulai–akhir, dan model audio belum boleh dianggap selesai.

## 4. Temuan yang Memerlukan Tashih Ahli

1. Bentuk panjang seperti `يَسْتَغْفِرُونَ، يَسْتَعْمِلُونَ، يَسْتَخْرِجُونَ، يَسْتَخْلِفُونَ` memerlukan tashih morfologi, makna, dan kesesuaian beban peserta.
2. Bentuk `عَلَىٰ` memerlukan pemeriksaan apakah alif maqṣūrah dan tanda alif khanjariyyah telah berada pada tahap literasi yang sah.
3. Potongan yang berakhir pada `عَلَىٰ` memerlukan keputusan waqaf sementara karena batas kotak tidak boleh menimbulkan pola berhenti yang menyesatkan.
4. Bentuk `أَفْوَاهِهِمْ` dan `يَكْسِبُونَ` memerlukan pemeriksaan seluruh unsur bacaan terhadap whitelist Jilid 3.
5. P040 memerlukan blueprint evaluasi, rubrik, aturan keputusan, remedial, dan bentuk paralel sebelum disebut ujian akhir tervalidasi.
6. Klaim “tervalidasi kandidat” pada judul P037 harus dibaca sebagai kandidat untuk validasi, bukan sudah tervalidasi.

## 5. Status Jilid 3 Setelah Batch Ini

| Komponen | Status |
|---|---|
| Master struktur 40 halaman | COMPLETE-DRAFT |
| Sumber materi P001–P040 | COMPLETE-DRAFT |
| Normalisasi P001–P035 | COMPLETE-STRUCTURAL |
| Audit struktural P036–P040 | COMPLETE-STRUCTURAL |
| Basis data P036–P040 | BELUM DIBENTUK |
| Audit kumulatif 960 kotak | BELUM DITUTUP |
| Tashih rasm/qira’at/makhraj | OPEN |
| Source-ID potongan Qurani | OPEN |
| Audio dan uji beban | OPEN |
| Validasi evaluasi akhir | OPEN |
| Layout dan proof cetak | OPEN |

## 6. Keputusan

**Draf isi Jilid 3 telah mencapai cakupan P001–P040.** Tahap produksi isi awal tidak perlu kembali ke P001. Pekerjaan sah berikutnya adalah:

1. membentuk `data/jilid-3/QJ3-ITEMS-P036-P040.csv`;
2. menjalankan audit kumulatif seluruh 960 kotak;
3. mengunci registry delapan potongan Qurani dan Source-ID;
4. melakukan tashih ahli;
5. menyusun blueprint evaluasi P040;
6. setelah itu memulai struktur isi Jilid 4 tanpa mengklaim Jilid 3 siap cetak.
