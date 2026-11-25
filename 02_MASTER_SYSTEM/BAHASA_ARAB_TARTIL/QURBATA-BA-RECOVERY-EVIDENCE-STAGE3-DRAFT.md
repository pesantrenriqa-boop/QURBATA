# Tahap 3 — bukti recovery J2 dan J3 (DRAFT)

J2 P028 belum memiliki teks lisan disahkan; J3 koneksi makna bukan otomatis panel instruksional. Salinan sumber verbatim.

## books/jilid-2/RECOVERY-SOURCES.md
Blob: 12e7bd7ff53464272801ecae63abe1886ab7080d

1: # QJ2 — Register Sumber Recovery
2: 
3: **Status:** ACTIVE  
4: **Induk:** `books/RECOVERY-CONSOLIDATION-INDEX-JILID-1-3.md`
5: 
6: ## Baseline Sumber
7: 
8: Commit `67a42c40d796cbdcead4e98f5d03da370ac22406` mencatat cakupan sumber Jilid 2 mencapai 40/40 halaman:
9: 
10: - P001–P020: `COMPLETE-DRAFT`;
11: - P021–P040: `STAGED-BLOCKED`.
12: 
13: Master pengendali: `books/jilid-2/QJ2-MASTER-Struktur-40-Halaman.md` versi 0.22.0-id atau penerus sahnya.
14: 
15: ## Register
16: 
17: | Rentang | Status | Audit/Keputusan | Ketentuan recovery |
18: |---|---|---|---|
19: | P001–P015 | FOUND-COMPLETE-DRAFT | DEC-CUR-010 | Pilih hasil regenerasi sah. Versi lama dinyatakan `SUPERSEDED` dan tidak boleh digunakan. |
20: | P016–P020 | FOUND-COMPLETE-DRAFT | AUD-QJ2-CONTENT-011 | Ekstrak sebagai baseline fondasi bentuk lanjutan. |
21: | P021–P024 | FOUND-STAGED-BLOCKED | AUD-QJ2-TAN-003; BLK-QJ2-ORTHO-001 | Simpan isi tanwin sebagai sumber terblokir; jangan otorisasi cetak. |
22: | P025 | FOUND-STAGED-BLOCKED | Objek hafalan khusus | Isi dan metadata khusus harus dipisahkan dari pola halaman latihan biasa. |
23: | P026–P027 | FOUND-STAGED-BLOCKED | AUD-QJ2-MAD-001 | Kandidat mad alif dan mad ya; verifikasi urutan tangga terbaru. |
24: | P028 | FOUND-STAGED-BLOCKED | Objek Bahasa Arab khusus | Materi lisan dan materi baca peserta wajib dipisahkan. |
25: | P029–P030 | FOUND-STAGED-BLOCKED | AUD-QJ2-MAD-001 | Kandidat mad waw dan evaluasi mad. |
26: | P031–P040 | FOUND-STAGED-BLOCKED | AUD-QJ2-FINAL-001 | Ekstrak sebagai sumber akhir, lalu audit kata, frasa, evaluasi, dan halaman khusus. |
27: 
28: ## Larangan
29: 
30: - Jangan mengambil QJ2-P001–P015 dari draf warisan yang telah superseded.
31: - Jangan mengubah status `STAGED-BLOCKED` menjadi siap cetak hanya karena file ditemukan.
32: - Jangan mencampur contoh peserta, naskah guru, audit, dan blocker dalam dataset latihan yang sama.
33: 

## books/jilid-2/recovery/QJ2-RECOVERED-SOURCE-P021-P040.md
Blob: 34b256ccdfe8848dafc69d20a0004ef618d24fe4

1: # QURBATA Jilid 2 — Recovery Terintegrasi P021–P040
2: 
3: **Kode:** QJ2-REC-P021-P040  
4: **Status:** RECOVERED-SOURCE-REGISTERED / STAGED-BLOCKED  
5: **Tanggal recovery:** 1 Agustus 2026  
6: **Sumber baseline:** commit `67a42c40d796cbdcead4e98f5d03da370ac22406`  
7: **Jalur sumber lama:** `books/jilid-2/regenerated/`  
8: **Master:** `books/jilid-2/QJ2-MASTER-Struktur-40-Halaman.md`
9: 
10: Dokumen ini mengunci keberadaan dan klasifikasi sumber P021–P040. Status `STAGED-BLOCKED` dipertahankan. Dokumen ini bukan otorisasi cetak dan tidak menggantikan gate ahli, audit ortografi, render, audio, asesmen, safeguarding, Evidence-ID, dan Decision-ID.
11: 
12: ## Register Halaman
13: 
14: | Halaman | Fokus Recovery | Status | Audit/Blocker |
15: |---|---|---|---|
16: | QJ2-P021 | Fathatain | STAGED-BLOCKED | AUD-QJ2-TAN-003; BLK-QJ2-ORTHO-001 |
17: | QJ2-P022 | Kasratain | STAGED-BLOCKED | AUD-QJ2-TAN-003; BLK-QJ2-ORTHO-001 |
18: | QJ2-P023 | Dhammatain | STAGED-BLOCKED | AUD-QJ2-TAN-003; BLK-QJ2-ORTHO-001 |
19: | QJ2-P024 | Integrasi tiga tanwin | STAGED-BLOCKED | AUD-QJ2-TAN-003; BLK-QJ2-ORTHO-001 |
20: | QJ2-P025 | Orientasi pendek–panjang | STAGED-BLOCKED | Objek khusus; materi dengar/tunjuk/tirukan |
21: | QJ2-P026 | Fathah pendek vs fathah + alif | STAGED-BLOCKED | AUD-QJ2-MAD-001 |
22: | QJ2-P027 | Alif mad pada tiga huruf | STAGED-BLOCKED | AUD-QJ2-MAD-001 |
23: | QJ2-P028 | Alif mad empat huruf dan pemutus | STAGED-BLOCKED | Objek khusus/transfer |
24: | QJ2-P029 | Transfer alif mad ke kata bermakna/Qurani | STAGED-BLOCKED | AUD-QJ2-MAD-001; Source-ID wajib |
25: | QJ2-P030 | Evaluasi alif mad dan kontras pendek | STAGED-BLOCKED | AUD-QJ2-MAD-001 |
26: | QJ2-P031 | Kasrah pendek vs kasrah + ya mad | STAGED-BLOCKED | AUD-QJ2-FINAL-001 |
27: | QJ2-P032 | Ya mad pada tiga huruf | STAGED-BLOCKED | AUD-QJ2-FINAL-001 |
28: | QJ2-P033 | Ya mad empat huruf dan transfer | STAGED-BLOCKED | AUD-QJ2-FINAL-001 |
29: | QJ2-P034 | Ya mad vs ya konsonan; murojaah alif | STAGED-BLOCKED | AUD-QJ2-FINAL-001 |
30: | QJ2-P035 | Dhammah pendek vs dhammah + waw mad | STAGED-BLOCKED | AUD-QJ2-FINAL-001 |
31: | QJ2-P036 | Waw mad pada tiga huruf | STAGED-BLOCKED | AUD-QJ2-FINAL-001 |
32: | QJ2-P037 | Waw mad empat huruf dan transfer | STAGED-BLOCKED | AUD-QJ2-FINAL-001 |
33: | QJ2-P038 | Waw mad vs waw konsonan; murojaah alif/ya | STAGED-BLOCKED | AUD-QJ2-FINAL-001 |
34: | QJ2-P039 | Integrasi tiga mad dan kontras pendek–panjang | STAGED-BLOCKED | AUD-QJ2-FINAL-001 |
35: | QJ2-P040 | Evaluasi akhir + Checkpoint Nama Huruf IV | STAGED-BLOCKED | AUD-QJ2-FINAL-001; panel lisan terpisah |
36: 
37: ## Bukti Isi yang Ditemukan
38: 
39: Salah satu sumber staging nyata adalah QJ2-P031 pada commit `d82cbc440b49d91ad692e0ecff47420a934cc4b4`, dengan jalur:
40: 
41: `books/jilid-2/regenerated/QJ2-P031-Pendek-Panjang.md`
42: 
43: Contoh di dalamnya antara lain:
44: 
45: - `قَالَ`
46: - `قِيلَ`
47: - `نُورُ`
48: - `أَحَدٌ`
49: - `رَجُلٍ`
50: - `عَمَلًا`
51: - `بَاعَ`
52: - `فِيهِ`
53: - `كِتَابَ`
54: - `كَبِيرِ`
55: - `رَسُولُ`
56: - `شَجَرَةٌ`
57: - `بَقَرَةٍ`
58: - `حَسَنَةً`
59: - `عَذَابَ`
60: - `رَحِيمِ`
61: - `يَقُولُ`
62: - `صَدَقَةٌ`
63: - `حِسَابَ`
64: - `عَلِيمِ`
65: - `قُلُوبُ`
66: - `نَفَقَةٍ`
67: - `مَكَانَ`
68: - `سُجُودُ`
69: 
70: Contoh tersebut dibekukan sebagai data recovery, bukan sebagai materi final siap cetak.
71: 
72: ## Aturan Integrasi
73: 
74: 1. Isi sumber lama tetap berada di `books/jilid-2/regenerated/` sampai salinan recovery per halaman selesai dibuat.
75: 2. Setiap file recovery berikutnya harus mencatat path dan commit asal.
76: 3. Status `STAGED-BLOCKED` tidak boleh diubah hanya karena isi telah ditemukan.
77: 4. Tanwin, mad, kata bermakna, kandidat Qurani, evaluasi, dan panel nama huruf harus tetap dipisahkan menurut fungsi.
78: 5. Klaim kata atau frasa Qurani wajib mempunyai Source-ID dan verifikasi teks.
79: 6. Tidak boleh membuat contoh baru untuk menggantikan isi staging yang belum diekstrak.
80: 
81: ## Status
82: 
83: - Sumber P021–P040: **FOUND 20/20**.
84: - Register recovery terintegrasi: **COMPLETE 20/20**.
85: - Salinan isi penuh per halaman ke folder recovery resmi: **NEXT STEP**.
86: - Kesiapan cetak: **BLOCKED**.
87: 

## books/jilid-2/regenerated/QJ2-P028-Bahasa-Arab-2.md
Blob: 209a916982ca3fcea89f0fcb4fc7289e70a0c50c

1: # QJ2-P028 — Bahasa Arab 2
2: 
3: **Kode:** QJ2-P028  
4: **Jenis:** HALAMAN KHUSUS — BAHASA ARAB 5 MENIT  
5: **Status:** STAGED-BLOCKED — WHITELIST LISAN BELUM DISAHKAN
6: 
7: ## Kompetensi Kandidat
8: 
9: Peserta merespons satu pola lisan sederhana tentang benda di sekitar menggunakan mufradat yang tidak mengulang unit sebelumnya. Tulisan Arab peserta belum diaktifkan agar materi bahasa tidak membocorkan pola baca yang belum sah.
10: 
11: ## Alur 5 Menit
12: 
13: | Menit | Guru | Peserta |
14: |---:|---|---|
15: | 1 | menunjukkan benda nyata | memperhatikan |
16: | 2 | memberi satu model pertanyaan | menirukan |
17: | 3 | memberi dua model jawaban | menjawab bersama |
18: | 4 | mengacak benda/pertanyaan | menjawab individu |
19: | 5 | koreksi cepat dan murojaah | memperbaiki respons |
20: 
21: ## Gate
22: 
23: Memerlukan Arabic Object-ID, daftar mufradat tanpa pengulangan, teks tervokalisasi guru, arti, konteks penggunaan, Source-ID leksikon, audit ACP, dan Reviewer-ID.
24: 

## books/JILID-3/PAGE-001-010.md
Blob: 3137ae8614c1ce8866e927f175786686fe3efe85

1: # QURBATA JILID 3
2: ## PAGE 001-010 (Draft Master)
3: 
4: ## Tujuan Tahap
5: 
6: Jilid 3 melanjutkan kemampuan membaca dari Jilid 2 menuju pembacaan kata dan frasa Qurani. Fokus bukan lagi pengenalan huruf dasar, tetapi peningkatan keterampilan membaca, mengenali pola, dan membangun hubungan dengan bahasa Al-Qur'an.
7: 
8: ## Prinsip Penyusunan
9: 
10: - Materi baru ±60%
11: - Murojaah ±40%
12: - Contoh diutamakan dari pola kata Al-Qur'an yang sesuai tingkat kemampuan.
13: - Tidak memaksakan ayat yang belum sesuai tangga kompetensi.
14: 
15: ---
16: 
17: # PAGE 001
18: Fokus:
19: - Penguatan kata berharakat lengkap.
20: - Kelancaran membaca tanpa mengeja.
21: 
22: Contoh latihan:
23: 
24: كَتَبَ
25: ذَهَبَ
26: جَلَسَ
27: عَلِمَ
28: 
29: Koneksi makna:
30: 
31: كِتَابٌ = buku
32: عِلْمٌ = ilmu
33: 
34: QA Revisi:
35: - Arah materi sesuai.
36: - Perlu dilengkapi tangga latihan bertahap seperti standar QURBATA Jilid 1.
37: - Koneksi makna tetap sebagai pendukung, bukan materi utama.
38: 
39: ---
40: 
41: # PAGE 002
42: Fokus:
43: Pengenalan pola kata yang sering muncul.
44: 
45: Contoh:
46: 
47: عَلِمَ
48: يَعْلَمُ
49: عَالِمٌ
50: 
51: Pengamatan:
52: Pola kata dikenalkan sebagai pola bacaan Qurani, bukan pembelajaran shorof.
53: 
54: QA Revisi:
55: - Hindari penjelasan teori perubahan bentuk kata.
56: - Fokus pada pengenalan visual dan kelancaran membaca.
57: 
58: ---
59: 
60: # PAGE 003
61: Fokus:
62: Latihan sukun dalam kata.
63: 
64: Contoh:
65: 
66: يَكْتُبُ
67: يَسْمَعُ
68: يَدْخُلُ
69: 
70: QA Revisi:
71: - Sesuai dengan target Jilid 3.
72: - Perlu dibuat kontras latihan dan murojaah.
73: 
74: ---
75: 
76: # PAGE 004
77: Fokus:
78: Mad dalam kata Qurani.
79: 
80: Contoh:
81: 
82: قَالَ
83: فِيهِ
84: نُورٌ
85: 
86: QA Revisi:
87: - Sesuai.
88: - Prioritas tetap latihan membaca, bukan teori mad.
89: 
90: ---
91: 
92: # PAGE 005
93: Fokus:
94: Akhiran kata yang sering ditemukan.
95: 
96: Contoh:
97: 
98: مُؤْمِنُونَ
99: يَعْلَمُونَ
100: يَعْمَلُونَ
101: 
102: Catatan:
103: Santri mulai mengenali pola ونَ yang sering muncul dalam Al-Qur'an.
104: 
105: QA Revisi:
106: - Materi sangat sesuai.
107: - Tambahkan latihan bertingkat dari bentuk pendek menuju frasa Qurani.
108: 
109: ---
110: 
111: # PAGE 006-010
112: Status:
113: Dilanjutkan berdasarkan hasil validasi tangga kompetensi dan draft progres sebelumnya.
114: 
115: Arah lanjutan:
116: - frasa Qurani 2 kata
117: - penguatan pola kata
118: - pengenalan hubungan bacaan dan makna
119: 
120: ---
121: 
122: # QA NOTE JILID 3 v0.2
123: 
124: Hasil audit:
125: 
126: 1. DNA QURBATA tetap dipertahankan.
127: 2. Bahasa Arab hanya sebagai pendukung makna, bukan pembelajaran nahwu/shorof.
128: 3. Materi halaman harus mengikuti standar learning object QURBATA:
129:    - tujuan halaman
130:    - batas materi
131:    - tangga latihan
132:    - murojaah
133:    - evaluasi.
134: 4. Draft PAGE 001-005 dinyatakan dapat dilanjutkan dengan penyempurnaan format.

## books/JILID-3/PAGE-011-020.md
Blob: 195da2afedadb09e8c7cf99abed647b69442fa0a

1: # QURBATA JILID 3
2: ## PAGE 011-020
3: 
4: ## Tahap: Penguatan Kata dan Frasa Qur'ani
5: 
6: ### Tujuan Pembelajaran
7: Peserta mampu membaca kata dan gabungan kata Arab sederhana dengan tartil, mengenali pola yang sering muncul dalam Al-Qur'an, serta mulai menghubungkan bacaan dengan makna.
8: 
9: ---
10: 
11: ## Halaman 11
12: Fokus: Penguatan mad dan sukun
13: 
14: Latihan:
15: 
16: قَالَ
17: كَانَ
18: مَالِكِ
19: 
20: Catatan guru:
21: Perhatikan panjang mad asli dan ketepatan harakat akhir.
22: 
23: ---
24: 
25: ## Halaman 12
26: Fokus: Pola kata berakhiran ونَ
27: 
28: Latihan:
29: 
30: يَعْلَمُونَ
31: يَعْمَلُونَ
32: يُؤْمِنُونَ
33: 
34: Kompetensi:
35: Mengenali pola jamak/fi'il yang sering muncul dalam bacaan Qur'an.
36: 
37: ---
38: 
39: ## Halaman 13
40: Fokus: Membandingkan pola kata
41: 
42: عَلِمَ
43: يَعْلَمُ
44: عَالِمٌ
45: 
46: Latihan:
47: Membedakan perubahan bentuk kata tanpa membebani teori sharaf.
48: 
49: ---
50: 
51: ## Halaman 14
52: Fokus: Frasa dua kata
53: 
54: هُدًى لِلْمُتَّقِينَ
55: 
56: لَا رَيْبَ
57: 
58: Latihan:
59: Membaca dengan sambungan yang benar.
60: 
61: ---
62: 
63: ## Halaman 15
64: Fokus: Penguatan kata Qur'ani
65: 
66: اللَّهُ
67: رَبِّي
68: الْحَمْدُ
69: 
70: Integrasi:
71: Mengenal kata yang sering ditemukan dalam Al-Qur'an.
72: 
73: ---
74: 
75: ## Halaman 16
76: Fokus: Frasa pendek
77: 
78: رَبِّ الْعَالَمِينَ
79: مَالِكِ يَوْمِ الدِّينِ
80: 
81: Latihan:
82: Membaca dengan tartil dan memperhatikan waqaf.
83: 
84: ---
85: 
86: ## Halaman 17
87: Fokus: Pola pengulangan Qur'an
88: 
89: مِنَ اللَّهِ
90: مِنْ عَذَابٍ
91: مِنْ فَضْلِ
92: 
93: Kompetensi:
94: Mengenali perubahan bacaan karena pertemuan huruf.
95: 
96: ---
97: 
98: ## Halaman 18
99: Fokus: Ayat pendek pilihan
100: 
101: وَاللَّهُ عَلِيمٌ
102: 
103: Latihan:
104: Menghubungkan bacaan dengan arti sederhana.
105: 
106: ---
107: 
108: ## Halaman 19
109: Fokus: Murojaah kumulatif
110: 
111: Gabungan materi:
112: - kata dasar
113: - mad
114: - sukun
115: - frasa Qur'ani
116: 
117: ---
118: 
119: ## Halaman 20
120: Evaluasi Tengah Bagian
121: 
122: Peserta membaca:
123: - kata pilihan
124: - frasa dua kata
125: - potongan ayat pendek
126: 
127: Penilaian:
128: 1. Ketepatan huruf
129: 2. Panjang pendek
130: 3. Kelancaran
131: 4. Adab membaca Al-Qur'an
132: 
133: ---
134: 
135: Catatan: Materi ini merupakan kelanjutan Jilid 3 dan akan dikembangkan melalui QA sebelum menjadi master cetak.

## books/JILID-3/PAGE-021-030.md
Blob: b631e4c1b5ed51819f1148df5bb79b681d05bbc1

1: # QURBATA JILID 3
2: ## PAGE 021-030
3: 
4: ## Fokus Tahap
5: Penguatan bacaan Qurani melalui kata dan frasa pendek yang sering muncul dalam Al-Qur'an.
6: 
7: ## Prinsip Pembelajaran
8: - Membaca dengan tartil.
9: - Mengenali pola kata.
10: - Menghubungkan bacaan dengan makna sederhana.
11: - Menjaga keseimbangan materi baru dan murojaah.
12: 
13: ## Materi Utama
14: 
15: ### Pola Kata Qurani
16: - كِتَابٌ
17: - الْكِتَابُ
18: - كُتُبٌ
19: 
20: Perhatikan perubahan bentuk kata dan fungsi sederhana.
21: 
22: ### Pola Fi'il
23: - عَلِمَ
24: - يَعْلَمُ
25: - يَعْلَمُونَ
26: 
27: Santri mengenali bahwa perubahan bentuk kata memiliki pola yang berulang dalam Al-Qur'an.
28: 
29: ## Frasa Qurani Bertahap
30: 
31: - فِي الْكِتَابِ
32: - مِنَ الْعِلْمِ
33: - عَلَى الْحَقِّ
34: - لَا رَيْبَ
35: 
36: ## Koneksi Makna
37: Setiap bacaan dikenalkan dengan makna sederhana agar membaca tidak terpisah dari pemahaman.
38: 
39: ## Evaluasi
40: Santri mampu:
41: 1. Membaca kata dengan tepat.
42: 2. Membedakan bentuk kata yang mirip.
43: 3. Membaca frasa pendek dengan tartil.
44: 4. Mengingat makna dasar beberapa kata pilihan.
45: 

## books/JILID-3/PAGE-031-040.md
Blob: 71f06afad5d24546f23dcff2da8098d89d217234

1: # QURBATA JILID 3
2: ## PAGE 031-040
3: 
4: ## Fokus Tahap
5: Penguatan bacaan Qurani melalui kata, frasa, dan potongan ayat pendek.
6: 
7: ## Prinsip
8: - Materi baru tetap mengikuti tangga kemampuan.
9: - Review kumulatif dipertahankan.
10: - Membaca mulai diarahkan kepada pengenalan pola bahasa Al-Qur'an.
11: 
12: ## Kompetensi
13: Peserta mampu:
14: - membaca gabungan kata dengan lancar,
15: - mengenali pola kata yang sering muncul,
16: - menghubungkan bacaan dengan makna sederhana.
17: 
18: ## Pola Latihan
19: Contoh pengembangan:
20: 
21: عَلِمَ
22: يَعْلَمُ
23: يَعْلَمُونَ
24: 
25: كَتَبَ
26: يَكْتُبُ
27: يَكْتُبُونَ
28: 
29: ## Frasa Qurani Bertahap
30: 
31: لَا رَيْبَ
32: 
33: فِي الْكِتَابِ
34: 
35: مِنَ الْعِلْمِ
36: 
37: هُدًى لِلْمُتَّقِينَ
38: 
39: ## Evaluasi Akhir Jilid 3
40: 
41: - Ketepatan makhraj
42: - Panjang pendek bacaan
43: - Kelancaran membaca frasa
44: - Kemampuan mengenali pola kata
45: 
46: ## Catatan QA
47: Dokumen ini merupakan draft master dan harus melalui pemeriksaan kesesuaian materi sebelum publikasi final.