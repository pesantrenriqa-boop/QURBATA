# AUD-QJ1-CONTENT-001 — Audit Isi Aktual QJ1-P001–QJ1-P010

**Document-ID:** AUD-QJ1-CONTENT-001  
**Versi:** 0.1.0-id  
**Status:** DRAFT TERKENDALI — ACTION REQUIRED  
**Tanggal:** 29 Juli 2026  
**Cakupan:** `books/jilid-1/pages/QJ1-P001.md` sampai `QJ1-P010.md`  
**Cabang:** `feature/qj1-master-structure`

## 1. Tujuan

Mengaudit isi aktual sepuluh halaman pertama QURBATA Jilid 1 terhadap prinsip desain yang telah disepakati: 24 latihan per halaman, urutan dua lalu tiga huruf, bentuk terpisah, fathah pendek, larangan mad/sambung/unsur prasyarat yang belum dibuka, penguatan kumulatif, dan kesiapan asesmen.

## 2. Ringkasan Hasil

| Aspek | Hasil | Status |
|---|---:|---|
| Halaman tersedia | 10/10 | PASS |
| Memiliki 24 item | 10/10 | PASS |
| P001–P009: item 1–8 dua huruf dan 9–24 tiga huruf | 9/9 | PASS |
| P010: 24 sampel evaluasi | 1/1 | PASS |
| Huruf latihan ditulis terpisah dengan spasi | 10/10 | PASS-SOURCE |
| Tidak ditemukan mad, tanwin, sukun, atau tasydid pada latihan inti | 10/10 | PASS-SOURCE |
| Seluruh latihan inti memakai fathah | 10/10 | PASS |
| Seluruh identitas terdahulu diupayakan hadir melalui pemerataan | 9/9 | PASS-POLICY |
| Rasio materi baru 60% dan review 40% | 1/10 sesuai/berlaku | FAIL-POLICY-CONFLICT |
| Verifikasi hasil render agar tidak tersambung | 0/10 | BLOCKED-RENDER |
| Validasi ahli huruf, harakat, makhraj, dan istilah | 0/10 | BLOCKED-EXPERT |
| Ambang kelulusan teruji | 0/10 | BLOCKED-VALIDATION |

## 3. Temuan per Halaman

| Page-ID | Materi/Fungsi | Temuan Utama | Keputusan Audit |
|---|---|---|---|
| QJ1-P001 | بَ تَ ثَ | 24 latihan; 8 item dua huruf dan 16 item tiga huruf; seluruh materi baru; tidak ada review | PASS-DRAFT; pengecualian rasio wajar untuk halaman pembuka |
| QJ1-P002 | ءَ أَ + review بَ تَ ثَ | Semua lima identitas dibagi hampir merata; token materi baru tidak dominan 60% | REVISE-DISTRIBUTION |
| QJ1-P003 | جَ حَ خَ + review kumulatif | Delapan identitas masing-masing 8 token; materi baru sekitar 24/64 token atau 37,5% | REVISE-DISTRIBUTION |
| QJ1-P004 | دَ ذَ رَ زَ + review kumulatif | Dua belas identitas dibagi 5–6 token; materi baru sekitar sepertiga, bukan 60% | REVISE-DISTRIBUTION |
| QJ1-P005 | سَ شَ + review kumulatif | Empat belas identitas dibagi 4–5 token; materi baru sangat kecil terhadap review | REVISE-DISTRIBUTION |
| QJ1-P006 | صَ ضَ + review kumulatif | Enam belas identitas masing-masing 4 token; dua huruf baru hanya 8/64 token | REVISE-DISTRIBUTION |
| QJ1-P007 | طَ ظَ + review kumulatif | Delapan belas identitas dibagi 3–4 token; materi baru tidak cukup untuk fase akuisisi | REVISE-DISTRIBUTION |
| QJ1-P008 | عَ غَ + review kumulatif | Dua puluh identitas dibagi 3–4 token; materi baru terlalu jarang | REVISE-DISTRIBUTION |
| QJ1-P009 | فَ قَ + review kumulatif | Dua puluh dua identitas dibagi 2–3 token; materi baru hanya sebagian kecil latihan | REVISE-DISTRIBUTION |
| QJ1-P010 | evaluasi ءَ–قَ | Tidak memperkenalkan materi baru; 22 identitas terwakili; struktur diagnostik tepat | PASS-DRAFT-ASSESSMENT |

## 4. Temuan Mayor

### F-01 — Konflik Kebijakan Distribusi

Dokumen halaman P002–P009 menjalankan `DEC-CUR-002` berupa pemerataan mutlak seluruh identitas yang telah sah. Kebijakan ini bertentangan dengan arahan pedagogis halaman akuisisi: materi baru sekitar 60% dan review sekitar 40%.

Dampak:

1. huruf baru muncul terlalu sedikit;
2. kesempatan pembentukan otomatisasi bunyi baru berkurang;
3. beban pencarian visual meningkat karena terlalu banyak identitas lama;
4. fungsi halaman akuisisi berubah menjadi halaman review luas;
5. target halaman dan isi latihan tidak sepenuhnya selaras.

**Severity:** MAJOR  
**Status:** OPEN  
**Action:** revisi atau supersede bagian DEC-CUR-002 yang mewajibkan pemerataan mutlak pada setiap halaman akuisisi.

### F-02 — Klaim 50:50 Tidak Konsisten dengan Distribusi Aktual

Beberapa bagian risiko/riwayat masih menyebut murojaah kumulatif 50:50, sedangkan isi aktual dibangkitkan dengan pemerataan semua identitas. Untuk P006–P009, proporsi materi baru jauh di bawah 50%.

**Severity:** MAJOR  
**Status:** OPEN  
**Action:** hapus klaim rasio lama atau bangkitkan ulang latihan dengan rasio terkendali yang benar.

### F-03 — Render Belum Dibuktikan

Spasi pada sumber Markdown mengurangi risiko sambung, tetapi tidak membuktikan keluaran PDF/Slides tidak mengubah shaping, kerning, atau pemisahan visual.

**Severity:** MAJOR-RELEASE  
**Status:** BLOCKED  
**Action:** render seluruh halaman, inspeksi visual, dan terbitkan Evidence-ID per batch.

### F-04 — Validasi Makhraj dan Ortografi Belum Ada

Semua gate ahli masih belum dicentang. Halaman memuat pasangan yang berisiko tinggi seperti ء/أ, ح/خ, د/ذ, ص/ض, ط/ظ, ع/غ, dan ف/ق.

**Severity:** MAJOR-RELEASE  
**Status:** BLOCKED  
**Action:** telaah ahli Al-Qur'an/qiraat dan pemeriksa ortografi.

### F-05 — P010 Belum Memiliki Aturan Keputusan Tervalidasi

P010 sudah layak sebagai draf instrumen diagnostik, tetapi belum boleh menentukan kelulusan final karena ambang dan ruleset belum tervalidasi.

**Severity:** MODERATE  
**Status:** OPEN  
**Action:** tautkan ke rubrik Tilawah Level 1 dan pilot item.

## 5. Keputusan Desain yang Direkomendasikan

Untuk halaman akuisisi P002–P009:

- target token materi baru: 38–40 dari 64 token;
- target token review: 24–26 dari 64 token;
- seluruh identitas lama tidak harus hadir pada setiap halaman;
- cakupan kumulatif penuh dijamin melalui siklus beberapa halaman dan halaman evaluasi;
- review diprioritaskan pada huruf paling dekat secara bentuk, makhraj, serta kesalahan aktual peserta;
- 24 item tetap unik;
- item 1–8 tetap dua huruf;
- item 9–24 tetap tiga huruf;
- tidak ada sambung, mad, tanwin, sukun, atau tasydid.

## 6. Rencana Koreksi

| Urutan | Tindakan | Artefak |
|---:|---|---|
| 1 | Tetapkan kebijakan distribusi 60:40 sebagai pengendali halaman akuisisi | DEC-CUR baru/revisi |
| 2 | Bangkitkan ulang P002–P009 | delapan file halaman |
| 3 | Jalankan audit token otomatis | laporan frekuensi per halaman |
| 4 | Audit P010 terhadap Assessment-ID Tilawah | matriks asesmen |
| 5 | Render P001–P010 | PDF/Slides pilot |
| 6 | Inspeksi shaping dan keterbacaan | Evidence-ID render |
| 7 | Telaah ahli dan editorial | Evidence-ID ahli |

## 7. Keputusan Gate

Batch QJ1-P001–P010 **BELUM SIAP UJI LAPANGAN**.

- Struktur sumber: memadai sebagai draf.
- Isi P001 dan P010: dapat dipertahankan sebagai kandidat dengan validasi lanjutan.
- Isi P002–P009: wajib diregenerasi agar fungsi akuisisi tidak dikalahkan oleh pemerataan review.
- Tidak ada Competency-ID, Assessment-ID, atau halaman yang diaktifkan melalui audit ini.

## 8. Riwayat

| Versi | Tanggal | Ringkasan |
|---|---|---|
| 0.1.0-id | 29 Juli 2026 | Audit isi aktual P001–P010 dan penetapan konflik pemerataan mutlak terhadap target 60:40 |
