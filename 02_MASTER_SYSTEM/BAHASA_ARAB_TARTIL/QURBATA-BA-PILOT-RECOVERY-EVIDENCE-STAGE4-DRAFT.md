# Tahap 4A — bukti JSON, recovery dan paket pilot (DRAFT)

Salinan verbatim; kandidat tidak otomatis disahkan sebagai panel instruksional.

## 03_BOOKS/BAHASA-ARAB/JILID-3/qurbata-j3-formula-registry-v0.1.json
Blob: e6852f6eb6c605028fee6e9f7675048900ac3782

1: {
2:   "schema_version": "0.1",
3:   "updated_at": "2026-09-25",
4:   "scope": "QURBATA Bahasa Arab Jilid 3 P001-P012",
5:   "policy": "Repeat for mastery, expand for richness",
6:   "rules": {
7:     "review_pages": ["P005", "P006", "P012"],
8:     "count_narrative_as_mastered": false,
9:     "count_surface_variants_as_unique_lemma": false,
10:     "duplicate_guard_statuses": ["NEW", "EXPANSION", "VALUABLE_REUSE", "REDUNDANT"],
11:     "exposure_levels": ["ACTIVE", "RECEPTIVE", "NARRATIVE"]
12:   },
13:   "items": [
14:     {"item_id":"F-J3-001","item_type":"FORMULA","arabic_surface":"مَاذَا تَقْرَأُ؟","lemma_family":["قرأ"],"first_seen":"P001","first_active_target":"P001","exposure_level":"ACTIVE","communicative_function":"ASK_READING_OBJECT","reuse_value":"NEW","source_status":"FROZEN","riqa_os_status":"READY_FOR_IMPORT"},
15:     {"item_id":"F-J3-002","item_type":"FORMULA","arabic_surface":"أَقْرَأُ الْقُرْآنَ","lemma_family":["قرأ"],"first_seen":"P001","first_active_target":"P002","exposure_level":"ACTIVE","communicative_function":"ANSWER_READING_OBJECT","reuse_value":"EXPANSION","source_status":"FROZEN","riqa_os_status":"READY_FOR_IMPORT"},
16:     {"item_id":"F-J3-003","item_type":"FORMULA","arabic_surface":"اِقْرَأْ مِنْ هُنَا","lemma_family":["قرأ"],"first_seen":"P003","first_active_target":"P003","exposure_level":"ACTIVE","communicative_function":"SET_START_POINT","reuse_value":"EXPANSION","source_status":"FROZEN","riqa_os_status":"READY_FOR_IMPORT"},
17:     {"item_id":"F-J3-004","item_type":"FORMULA","arabic_surface":"اِقْرَأْ إِلَى هُنَا","lemma_family":["قرأ"],"first_seen":"P004","first_active_target":"P004","exposure_level":"ACTIVE","communicative_function":"SET_END_POINT","reuse_value":"EXPANSION","source_status":"REVIEWED_RECOVERED","riqa_os_status":"READY_FOR_IMPORT"},
18:     {"item_id":"F-J3-005","item_type":"FORMULA","arabic_surface":"دَوْرُ مَنْ؟","lemma_family":["دور"],"first_seen":"P007","first_active_target":"P007","exposure_level":"ACTIVE","communicative_function":"ASK_TURN","reuse_value":"NEW","source_status":"REVIEWED_RECOVERED","riqa_os_status":"READY_FOR_IMPORT"},
19:     {"item_id":"F-J3-006","item_type":"FORMULA","arabic_surface":"دَوْرِي","lemma_family":["دور"],"first_seen":"P008","first_active_target":"P008","exposure_level":"ACTIVE","communicative_function":"CLAIM_TURN","reuse_value":"EXPANSION","source_status":"REVIEWED_RECOVERED","riqa_os_status":"READY_FOR_IMPORT"},
20:     {"item_id":"F-J3-007","item_type":"FORMULA","arabic_surface":"الْآنَ دَوْرُكَ","lemma_family":["دور"],"first_seen":"P009","first_active_target":"P009","exposure_level":"ACTIVE","communicative_function":"TRANSFER_TURN","reuse_value":"EXPANSION","source_status":"REVIEWED_RECOVERED","riqa_os_status":"READY_FOR_IMPORT"},
21:     {"item_id":"F-J3-008","item_type":"FORMULA","arabic_surface":"اِقْرَأْ بَعْدَ صَدِيقِكَ","lemma_family":["قرأ","بعد","صديق"],"first_seen":"P010","first_active_target":"P010","exposure_level":"ACTIVE","communicative_function":"PEER_SEQUENCE_READING","reuse_value":"EXPANSION","source_status":"REVIEWED_RECOVERED","riqa_os_status":"READY_FOR_IMPORT"},
22:     {"item_id":"F-J3-009","item_type":"FORMULA","arabic_surface":"اِسْمَعْ إِلَى صَدِيقِكَ","lemma_family":["سمع","استمع"],"first_seen":"P011","first_active_target":"P011","exposure_level":"ACTIVE","communicative_function":"PEER_LISTENING","reuse_value":"NEW_FUNCTION","source_status":"REVIEWED_RECOVERED","riqa_os_status":"REVIEW_MORPHOLOGY_BEFORE_IMPORT"}
23:   ]
24: }
25: 

## 03_BOOKS/BAHASA-ARAB/JILID-3/qurbata-j3-lemma-registry-v0.1.json
Blob: 1afd683fe6659a9026538872291d9c2cb77fb86e

1: {
2:   "schema_version": "0.1",
3:   "updated_at": "2026-09-25",
4:   "scope": "QURBATA Bahasa Arab Jilid 3 P001-P012",
5:   "counting_policy": {
6:     "count_surface_forms_as_unique_lemmas": false,
7:     "count_narrative_as_mastered": false,
8:     "active_mastery_requires_first_active_target": true,
9:     "review_does_not_increment_unique_lemma_count": true
10:   },
11:   "duplicate_guard": {
12:     "match_order": ["normalized_family", "lemma", "surface_form", "formula", "communicative_function"],
13:     "existing_lemma_default_status": "REVIEW_OR_EXPANSION",
14:     "new_lemma_requires": ["not_found_in_registry", "meaning_validated", "first_active_target_assigned"],
15:     "manual_review_families": ["سمع/استمع"]
16:   },
17:   "items": [
18:     {"lemma_id":"L-J3-001","lemma":"قَرَأَ","normalized_family":"قرأ","meaning":"membaca","first_seen":"P001","first_active_target":"P001","exposure_level":"ACTIVE","status":"CORE","domain":"READING","surface_examples":["أَقْرَأُ","تَقْرَأُ","يَقْرَأُ","اِقْرَأْ","اِقْرَئِي","قِرَاءَةٌ"]},
19:     {"lemma_id":"L-J3-002","lemma":"الْقُرْآنُ","normalized_family":"قرآن","meaning":"Al-Qur'an","first_seen":"P001","first_active_target":"P002","exposure_level":"ACTIVE","status":"CORE","domain":"QURAN"},
20:     {"lemma_id":"L-J3-003","lemma":"مَاذَا","normalized_family":"ماذا","meaning":"apa","first_seen":"P001","first_active_target":"P001","exposure_level":"ACTIVE","status":"CORE","domain":"QUESTION"},
21:     {"lemma_id":"L-J3-004","lemma":"هُنَا","normalized_family":"هنا","meaning":"di sini","first_seen":"P003","first_active_target":"P003","exposure_level":"ACTIVE","status":"CORE","domain":"NAVIGATION"},
22:     {"lemma_id":"L-J3-005","lemma":"مِنْ","normalized_family":"من-prep","meaning":"dari","first_seen":"P001","first_active_target":"P003","exposure_level":"ACTIVE","status":"EXPANSION","domain":"NAVIGATION"},
23:     {"lemma_id":"L-J3-006","lemma":"إِلَى","normalized_family":"إلى","meaning":"ke/sampai","first_seen":"P001","first_active_target":"P004","exposure_level":"ACTIVE","status":"EXPANSION","domain":"NAVIGATION"},
24:     {"lemma_id":"L-J3-007","lemma":"دَوْرٌ","normalized_family":"دور","meaning":"giliran","first_seen":"P003","first_active_target":"P007","exposure_level":"ACTIVE","status":"CORE","domain":"TURN_MANAGEMENT","surface_examples":["دَوْرِي","دَوْرُكَ","دَوْرُهُ","دَوْرُهَا"]},
25:     {"lemma_id":"L-J3-008","lemma":"مَنْ","normalized_family":"من-interrogative","meaning":"siapa","first_seen":"P001","first_active_target":"P007","exposure_level":"ACTIVE","status":"EXPANSION","domain":"QUESTION"},
26:     {"lemma_id":"L-J3-009","lemma":"الْآنَ","normalized_family":"الآن","meaning":"sekarang","first_seen":"P003","first_active_target":"P009","exposure_level":"ACTIVE","status":"EXPANSION","domain":"TIME"},
27:     {"lemma_id":"L-J3-010","lemma":"بَعْدَ","normalized_family":"بعد","meaning":"setelah","first_seen":"P001","first_active_target":"P010","exposure_level":"ACTIVE","status":"EXPANSION","domain":"SEQUENCING"},
28:     {"lemma_id":"L-J3-011","lemma":"صَدِيقٌ","normalized_family":"صديق","meaning":"teman","first_seen":"P001","first_active_target":"P010","exposure_level":"ACTIVE","status":"EXPANSION","domain":"PEER_INTERACTION","surface_examples":["صَدِيقِي","صَدِيقِكَ"]},
29:     {"lemma_id":"L-J3-012","lemma":"اِسْتَمَعَ","normalized_family":"استمع","meaning":"mendengarkan","first_seen":"P003","first_active_target":"P011","exposure_level":"ACTIVE","status":"REVIEW_REQUIRED","domain":"LISTENING","note":"validate سمع/استمع source morphology before production import"},
30:     {"lemma_id":"L-J3-015","lemma":"صَفْحَةٌ","normalized_family":"صفحة","meaning":"halaman","first_seen":"P001","first_active_target":null,"exposure_level":"RECEPTIVE","status":"CANDIDATE_ACTIVE","domain":"QURAN_NAVIGATION"},
31:     {"lemma_id":"L-J3-017","lemma":"آيَةٌ","normalized_family":"آية","meaning":"ayat","first_seen":"P001","first_active_target":null,"exposure_level":"RECEPTIVE","status":"CANDIDATE_ACTIVE","domain":"QURAN_NAVIGATION"},
32:     {"lemma_id":"L-J3-019","lemma":"مُصْحَفٌ","normalized_family":"مصحف","meaning":"mushaf","first_seen":"P001","first_active_target":null,"exposure_level":"RECEPTIVE","status":"CANDIDATE_ACTIVE","domain":"QURAN_NAVIGATION"},
33:     {"lemma_id":"L-J3-020","lemma":"سُورَةٌ","normalized_family":"سورة","meaning":"surah","first_seen":"P001","first_active_target":null,"exposure_level":"RECEPTIVE","status":"CANDIDATE_ACTIVE","domain":"QURAN_NAVIGATION"},
34:     {"lemma_id":"L-J3-021","lemma":"سَطْرٌ","normalized_family":"سطر","meaning":"baris","first_seen":"P003","first_active_target":null,"exposure_level":"RECEPTIVE","status":"CANDIDATE_ACTIVE","domain":"TEXT_NAVIGATION"},
35:     {"lemma_id":"L-J3-024","lemma":"صَحِيحٌ","normalized_family":"صحيح","meaning":"benar","first_seen":"P003","first_active_target":null,"exposure_level":"RECEPTIVE","status":"CANDIDATE_ACTIVE","domain":"FEEDBACK"},
36:     {"lemma_id":"L-J3-025","lemma":"تَدْرِيبٌ","normalized_family":"تدريب","meaning":"latihan","first_seen":"P012","first_active_target":null,"exposure_level":"NARRATIVE","status":"KNOWN","domain":"AUTONOMY"},
37:     {"lemma_id":"L-J3-026","lemma":"تَنْظِيمٌ","normalized_family":"تنظيم","meaning":"pengaturan","first_seen":"P012","first_active_target":null,"exposure_level":"NARRATIVE","status":"KNOWN","domain":"AUTONOMY"},
38:     {"lemma_id":"L-J3-027","lemma":"أَدَارَ","normalized_family":"إدارة","meaning":"mengelola","first_seen":"P012","first_active_target":null,"exposure_level":"NARRATIVE","status":"KNOWN","domain":"AUTONOMY","surface_examples":["يُدِيرُوا"]},
39:     {"lemma_id":"L-J3-028","lemma":"تَعَاوَنَ","normalized_family":"تعاون","meaning":"bekerja sama","first_seen":"P012","first_active_target":null,"exposure_level":"NARRATIVE","status":"KNOWN","domain":"COLLABORATION","surface_examples":["يَتَعَاوَنُوا"]},
40:     {"lemma_id":"L-J3-029","lemma":"نِظَامٌ","normalized_family":"نظام","meaning":"keteraturan/sistem","first_seen":"P012","first_active_target":null,"exposure_level":"NARRATIVE","status":"KNOWN","domain":"AUTONOMY"}
41:   ]
42: }
43: 

## books/jilid-3/recovery/QJ3-RECOVERED-SOURCE-P001-P010.md
Blob: cae3b4862489951151d2de599a9afe52c825ddb1

1: # QJ3 — Recovery Source P001–P010
2: 
3: **Status:** RECOVERED-SOURCE / NOT FINAL  
4: **Sumber asli:** `books/JILID-3/PAGE-001-010.md`  
5: **Commit sumber:** `3c47a20fb8bb2f9688f4f1521c1068db53274a7c`  
6: **Aturan:** isi di bawah dipertahankan sebagai data recovery. Koreksi kurikulum dilakukan pada file kanonik per halaman, bukan dengan menghapus sumber ini.
7: 
8: ---
9: 
10: # QURBATA JILID 3
11: ## PAGE 001-010 (Draft Master)
12: 
13: ## Tujuan Tahap
14: 
15: Jilid 3 melanjutkan kemampuan membaca dari Jilid 2 menuju pembacaan kata dan frasa Qurani. Fokus bukan lagi pengenalan huruf dasar, tetapi peningkatan keterampilan membaca, mengenali pola, dan membangun hubungan dengan bahasa Al-Qur'an.
16: 
17: ## Prinsip Penyusunan
18: 
19: - Materi baru ±60%
20: - Murojaah ±40%
21: - Contoh diutamakan dari pola kata Al-Qur'an yang sesuai tingkat kemampuan.
22: - Tidak memaksakan ayat yang belum sesuai tangga kompetensi.
23: 
24: ---
25: 
26: # PAGE 001
27: Fokus:
28: - Penguatan kata berharakat lengkap.
29: - Kelancaran membaca tanpa mengeja.
30: 
31: Contoh latihan:
32: 
33: كَتَبَ
34: ذَهَبَ
35: جَلَسَ
36: عَلِمَ
37: 
38: Koneksi makna:
39: 
40: كِتَابٌ = buku
41: عِلْمٌ = ilmu
42: 
43: ---
44: 
45: # PAGE 002
46: Fokus:
47: Pengenalan pola kata yang sering muncul.
48: 
49: Contoh:
50: 
51: عَلِمَ
52: يَعْلَمُ
53: عَالِمٌ
54: 
55: Pengamatan:
56: Satu akar kata dapat berubah bentuk dan makna.
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
70: ---
71: 
72: # PAGE 004
73: Fokus:
74: Mad dalam kata Qurani.
75: 
76: Contoh:
77: 
78: قَالَ
79: فِيهِ
80: نُورٌ
81: 
82: ---
83: 
84: # PAGE 005
85: Fokus:
86: Akhiran kata yang sering ditemukan.
87: 
88: Contoh:
89: 
90: مُؤْمِنُونَ
91: يَعْلَمُونَ
92: يَعْمَلُونَ
93: 
94: Catatan:
95: Santri mulai mengenali pola ونَ yang sering muncul dalam Al-Qur'an.
96: 
97: ---
98: 
99: # PAGE 006-010
100: Status:
101: Dilanjutkan berdasarkan hasil validasi tangga kompetensi dan draft progres sebelumnya.
102: 
103: Arah lanjutan:
104: - frasa Qurani 2 kata
105: - penguatan pola kata
106: - pengenalan hubungan bacaan dan makna
107: 

## books/jilid-3/recovery/QJ3-RECOVERED-SOURCE-P011-P020.md
Blob: 090dccaa9e2aa085b71d6eebff004c0c969f1a0e

1: # QJ3 — Recovery Source P011–P020
2: 
3: **Status:** RECOVERED-SOURCE / NOT FINAL  
4: **Sumber asli:** `books/JILID-3/PAGE-011-020.md`  
5: **Commit sumber:** `aadd8918ba865a2a4338fdfdf736ceb154b95173`  
6: **Aturan:** isi di bawah dipertahankan sebagai data recovery. Unsur yang melampaui tangga sukun/tasydid terbaru tetap dicatat, tetapi tidak otomatis menjadi materi cetak.
7: 
8: ---
9: 
10: # QURBATA JILID 3
11: ## PAGE 011-020
12: 
13: ## Tahap: Penguatan Kata dan Frasa Qur'ani
14: 
15: ### Tujuan Pembelajaran
16: Peserta mampu membaca kata dan gabungan kata Arab sederhana dengan tartil, mengenali pola yang sering muncul dalam Al-Qur'an, serta mulai menghubungkan bacaan dengan makna.
17: 
18: ---
19: 
20: ## Halaman 11
21: Fokus: Penguatan mad dan sukun
22: 
23: Latihan:
24: 
25: قَالَ
26: كَانَ
27: مَالِكِ
28: 
29: Catatan guru:
30: Perhatikan panjang mad asli dan ketepatan harakat akhir.
31: 
32: ---
33: 
34: ## Halaman 12
35: Fokus: Pola kata berakhiran ونَ
36: 
37: Latihan:
38: 
39: يَعْلَمُونَ
40: يَعْمَلُونَ
41: يُؤْمِنُونَ
42: 
43: Kompetensi:
44: Mengenali pola jamak/fi'il yang sering muncul dalam bacaan Qur'an.
45: 
46: ---
47: 
48: ## Halaman 13
49: Fokus: Membandingkan pola kata
50: 
51: عَلِمَ
52: يَعْلَمُ
53: عَالِمٌ
54: 
55: Latihan:
56: Membedakan perubahan bentuk kata tanpa membebani teori sharaf.
57: 
58: ---
59: 
60: ## Halaman 14
61: Fokus: Frasa dua kata
62: 
63: هُدًى لِلْمُتَّقِينَ
64: 
65: لَا رَيْبَ
66: 
67: Latihan:
68: Membaca dengan sambungan yang benar.
69: 
70: ---
71: 
72: ## Halaman 15
73: Fokus: Penguatan kata Qur'ani
74: 
75: اللَّهُ
76: رَبِّي
77: الْحَمْدُ
78: 
79: Integrasi:
80: Mengenal kata yang sering ditemukan dalam Al-Qur'an.
81: 
82: ---
83: 
84: ## Halaman 16
85: Fokus: Frasa pendek
86: 
87: رَبِّ الْعَالَمِينَ
88: مَالِكِ يَوْمِ الدِّينِ
89: 
90: Latihan:
91: Membaca dengan tartil dan memperhatikan waqaf.
92: 
93: ---
94: 
95: ## Halaman 17
96: Fokus: Pola pengulangan Qur'an
97: 
98: مِنَ اللَّهِ
99: مِنْ عَذَابٍ
100: مِنْ فَضْلِ
101: 
102: Kompetensi:
103: Mengenali perubahan bacaan karena pertemuan huruf.
104: 
105: ---
106: 
107: ## Halaman 18
108: Fokus: Ayat pendek pilihan
109: 
110: وَاللَّهُ عَلِيمٌ
111: 
112: Latihan:
113: Menghubungkan bacaan dengan arti sederhana.
114: 
115: ---
116: 
117: ## Halaman 19
118: Fokus: Murojaah kumulatif
119: 
120: Gabungan materi:
121: - kata dasar
122: - mad
123: - sukun
124: - frasa Qur'ani
125: 
126: ---
127: 
128: ## Halaman 20
129: Evaluasi Tengah Bagian
130: 
131: Peserta membaca:
132: - kata pilihan
133: - frasa dua kata
134: - potongan ayat pendek
135: 
136: Penilaian:
137: 1. Ketepatan huruf
138: 2. Panjang pendek
139: 3. Kelancaran
140: 4. Adab membaca Al-Qur'an
141: 
142: ---
143: 
144: Catatan: Materi ini merupakan kelanjutan Jilid 3 dan akan dikembangkan melalui QA sebelum menjadi master cetak.
145: 

## books/jilid-3/recovery/QJ3-RECOVERED-SOURCE-P021-P030.md
Blob: cd7bbe686f03fffdeb02d4a98451c59857e12690

1: # QJ3 — Recovery Source P021–P030
2: 
3: **Status:** RECOVERED-SOURCE / NOT FINAL  
4: **Sumber asli:** `books/JILID-3/PAGE-021-030.md`  
5: **Commit sumber:** `05dfd094584c39e1ef09cee181d75516f52c63a8`  
6: **Aturan:** isi di bawah dipertahankan sebagai data recovery dan wajib dipetakan per halaman sebelum menjadi sumber cetak.
7: 
8: ---
9: 
10: # QURBATA JILID 3
11: ## PAGE 021-030
12: 
13: ## Fokus Tahap
14: Penguatan bacaan Qurani melalui kata dan frasa pendek yang sering muncul dalam Al-Qur'an.
15: 
16: ## Prinsip Pembelajaran
17: - Membaca dengan tartil.
18: - Mengenali pola kata.
19: - Menghubungkan bacaan dengan makna sederhana.
20: - Menjaga keseimbangan materi baru dan murojaah.
21: 
22: ## Materi Utama
23: 
24: ### Pola Kata Qurani
25: - كِتَابٌ
26: - الْكِتَابُ
27: - كُتُبٌ
28: 
29: Perhatikan perubahan bentuk kata dan fungsi sederhana.
30: 
31: ### Pola Fi'il
32: - عَلِمَ
33: - يَعْلَمُ
34: - يَعْلَمُونَ
35: 
36: Santri mengenali bahwa perubahan bentuk kata memiliki pola yang berulang dalam Al-Qur'an.
37: 
38: ## Frasa Qurani Bertahap
39: 
40: - فِي الْكِتَابِ
41: - مِنَ الْعِلْمِ
42: - عَلَى الْحَقِّ
43: - لَا رَيْبَ
44: 
45: ## Koneksi Makna
46: Setiap bacaan dikenalkan dengan makna sederhana agar membaca tidak terpisah dari pemahaman.
47: 
48: ## Evaluasi
49: Santri mampu:
50: 1. Membaca kata dengan tepat.
51: 2. Membedakan bentuk kata yang mirip.
52: 3. Membaca frasa pendek dengan tartil.
53: 4. Mengingat makna dasar beberapa kata pilihan.
54: 

## books/jilid-3/recovery/QJ3-RECOVERED-SOURCE-P031-P040.md
Blob: 2a236d5d7b3b10806edb68c4244b0cf29fc84f2c

1: # QJ3 — Recovery Source P031–P040
2: 
3: **Status:** RECOVERED-SOURCE / NOT FINAL  
4: **Sumber asli:** `books/JILID-3/PAGE-031-040.md`  
5: **Commit sumber:** `fb0a15ddf60239d99aa299dc40ce85a4a531c997`  
6: **Aturan:** isi di bawah dipertahankan sebagai data recovery dan wajib dipetakan per halaman sebelum menjadi sumber cetak.
7: 
8: ---
9: 
10: # QURBATA JILID 3
11: ## PAGE 031-040
12: 
13: ## Fokus Tahap
14: Penguatan bacaan Qurani melalui kata, frasa, dan potongan ayat pendek.
15: 
16: ## Prinsip
17: - Materi baru tetap mengikuti tangga kemampuan.
18: - Review kumulatif dipertahankan.
19: - Membaca mulai diarahkan kepada pengenalan pola bahasa Al-Qur'an.
20: 
21: ## Kompetensi
22: Peserta mampu:
23: - membaca gabungan kata dengan lancar,
24: - mengenali pola kata yang sering muncul,
25: - menghubungkan bacaan dengan makna sederhana.
26: 
27: ## Pola Latihan
28: Contoh pengembangan:
29: 
30: عَلِمَ
31: يَعْلَمُ
32: يَعْلَمُونَ
33: 
34: كَتَبَ
35: يَكْتُبُ
36: يَكْتُبُونَ
37: 
38: ## Frasa Qurani Bertahap
39: 
40: لَا رَيْبَ
41: 
42: فِي الْكِتَابِ
43: 
44: مِنَ الْعِلْمِ
45: 
46: هُدًى لِلْمُتَّقِينَ
47: 
48: ## Evaluasi Akhir Jilid 3
49: 
50: - Ketepatan makhraj
51: - Panjang pendek bacaan
52: - Kelancaran membaca frasa
53: - Kemampuan mengenali pola kata
54: 
55: ## Catatan QA
56: Dokumen ini merupakan draft master dan harus melalui pemeriksaan kesesuaian materi sebelum publikasi final.
57: 

## books/jilid-3/recovery/README.md
Blob: bc1725d79160ac948f1172a8befef2566edfabe2

1: # QURBATA Jilid 3 — Indeks Recovery Terintegrasi
2: 
3: **Status:** RECOVERED-SOURCE-COMPLETE / NOT FINAL  
4: **Tanggal recovery:** 1 Agustus 2026  
5: **Induk:** `books/QURBATA-JILID-1-3-RECOVERY-FREEZE.md`
6: 
7: ## File Recovery
8: 
9: | Rentang | File terintegrasi | Commit sumber asli | Status |
10: |---|---|---|---|
11: | P001–P010 | `QJ3-RECOVERED-SOURCE-P001-P010.md` | `3c47a20fb8bb2f9688f4f1521c1068db53274a7c` | RECOVERED |
12: | P011–P020 | `QJ3-RECOVERED-SOURCE-P011-P020.md` | `aadd8918ba865a2a4338fdfdf736ceb154b95173` | RECOVERED |
13: | P021–P030 | `QJ3-RECOVERED-SOURCE-P021-P030.md` | `05dfd094584c39e1ef09cee181d75516f52c63a8` | RECOVERED |
14: | P031–P040 | `QJ3-RECOVERED-SOURCE-P031-P040.md` | `fb0a15ddf60239d99aa299dc40ce85a4a531c997` | RECOVERED |
15: 
16: ## Aturan Penggunaan
17: 
18: 1. File recovery adalah salinan terkendali dari data lama yang ditemukan di riwayat GitHub.
19: 2. Tidak boleh menghapus contoh recovery hanya karena tidak sesuai tangga kurikulum terbaru.
20: 3. File recovery bukan otomatis sumber cetak.
21: 4. File kanonik per halaman harus ditempatkan pada `books/jilid-3/pages/QJ3-P001.md` sampai `QJ3-P040.md`.
22: 5. Pemindahan ke file kanonik wajib mencatat `RECOVERED-FROM`, commit asal, status validasi, dan blocker.
23: 6. Contoh yang mengandung tasydid, mad, tanwin, atau struktur di luar progression tetap disimpan, lalu dipindahkan ke halaman/jilid yang tepat melalui revisi terkontrol.
24: 
25: ## Contoh Data yang Berhasil Dikembalikan
26: 
27: - Kata dasar: كَتَبَ، ذَهَبَ، جَلَسَ، عَلِمَ
28: - Pola fi'il: يَعْلَمُ، يَعْلَمُونَ، يَعْمَلُونَ، يَكْتُبُ، يَكْتُبُونَ
29: - Sukun: يَكْتُبُ، يَسْمَعُ، يَدْخُلُ
30: - Mad: قَالَ، فِيهِ، نُورٌ
31: - Frasa: لَا رَيْبَ، فِي الْكِتَابِ، مِنَ الْعِلْمِ، عَلَى الْحَقِّ
32: - Frasa lanjut: هُدًى لِلْمُتَّقِينَ، رَبِّ الْعَالَمِينَ، مَالِكِ يَوْمِ الدِّينِ
33: 
34: ## Keputusan Freeze
35: 
36: Seluruh empat batch P001–P040 telah ditemukan dan dikembalikan ke struktur resmi proyek. Status `RECOVERED-SOURCE-COMPLETE` berarti data sumber aman dan lengkap menurut batch yang ditemukan, bukan berarti 40 halaman telah selesai divalidasi atau siap cetak.
37: 

## curriculum/BAT-ARB-004-Paket-Integrasi-Pilot-Tahap-7.md
Blob: e9c9de047f4373650917fed770c7e4bd613e060b

1: # BAT-ARB-004 — Paket Integrasi Pilot Tahap 7
2: 
3: **Batch-ID:** BAT-ARB-004  
4: **Cycle-ID:** AR-CYC-000003  
5: **Status:** DRAF PILOT — GERBANG BELUM DIJALANKAN  
6: **Tanggal:** 28 Juli 2026  
7: **Teks tujuan:** AR-TXT-000001  
8: **Pengendali:** DEC-CUR-003, ACP-QUR-001, MAT-ARB-002, STD-ARB-002  
9: **Prasyarat sumber:** LEX-ARB-001–003, BAT-ARB-001–003
10: 
11: ## 1. Tujuan
12: 
13: Menguji secara terkendali apakah unsur yang diperlukan untuk AR-TXT-000001 telah cukup dikuasai sebelum paragraf diberikan. Dokumen ini bukan bukti bahwa peserta telah lulus dan belum menetapkan halaman final.
14: 
15: ## 2. Inventaris Prasyarat Teks
16: 
17: ### 2.1 Kosa Kata dan Bentuk
18: 
19: | Fungsi dalam teks | Lexeme-ID | Bentuk teks | Status yang diperlukan |
20: |---|---|---|---|
21: | ruang kelas | AR-LEX-000017 | فَصْلٌ / الْفَصْلَ | REVIEW-MASTERED |
22: | pelajar | AR-LEX-000013 | الطَّالِبُ | REVIEW-MASTERED |
23: | kursi | AR-LEX-000004 | الْكُرْسِيِّ | REVIEW-MASTERED |
24: | guru | AR-LEX-000011 | الْمُعَلِّمُ / الْمُعَلِّمَ | REVIEW-MASTERED |
25: | mushaf | AR-LEX-000007 | الْمُصْحَفَ | REVIEW-MASTERED |
26: | buku | AR-LEX-000001 | الْكِتَابَ | REVIEW-MASTERED |
27: | bersih | AR-LEX-000027 | نَظِيفٌ | REVIEW-MASTERED |
28: | masuk | AR-LEX-000038 | يَدْخُلُ | DERIVED-FORM-MASTERED |
29: | duduk | AR-LEX-000034 | يَجْلِسُ | DERIVED-FORM-MASTERED |
30: | membuka | AR-LEX-000036 | يَفْتَحُ | DERIVED-FORM-MASTERED |
31: | membaca | AR-LEX-000032 | يَقْرَأُ | DERIVED-FORM-MASTERED |
32: | mendengar | AR-LEX-000044 | يَسْمَعُ | DERIVED-FORM-MASTERED |
33: 
34: Pemakaian bentuk ma‘rifah, perubahan akhir, dan mudhari‘ tidak menambah hitungan lema, tetapi wajib mempunyai bukti penguasaan bentuk.
35: 
36: ### 2.2 Struktur, Pola, dan Contoh
37: 
38: | Jenis | ID | Peran |
39: |---|---|---|
40: | Grammar | AR-GRM-000005 | isim + na‘at |
41: | Grammar | AR-GRM-000010 | mudhari‘ + fa‘il |
42: | Grammar | AR-GRM-000011 | mudhari‘ + fa‘il + objek/preposisi |
43: | Function word | AR-FW-000006 | عَلَى |
44: | Pattern | AR-PAT-000005 | deskripsi |
45: | Pattern | AR-PAT-000010 | tindakan kini |
46: | Sentence | AR-SEN-000029 | deskripsi ruang kelas |
47: | Sentence | AR-SEN-000049 | membaca buku |
48: | Sentence | AR-SEN-000051 | duduk di kursi |
49: | Sentence | AR-SEN-000053 | membuka objek |
50: | Sentence | AR-SEN-000055 | masuk ruang kelas |
51: | Sentence | AR-SEN-000081 | mendengar guru |
52: 
53: AR-SEN-000053 berfungsi sebagai pola; penggantian الْبَابَ menjadi الْمُصْحَفَ pada teks adalah transfer dari dua unsur yang telah tersedia.
54: 
55: ## 3. Rangkaian Siklus Pilot
56: 
57: | Fase | Materi | Bukti calon |
58: |---|---|---|
59: | A — Akuisisi | 12 lema yang diperlukan teks | AR-EVD-CYC03-A |
60: | B — Pemantapan | makna, referen, recall, dan bentuk perlu | AR-EVD-CYC03-B |
61: | C — Frasa/pola | sifat, عَلَى, pelaku–tindakan–objek | AR-EVD-CYC03-C |
62: | D — Kalimat | enam Sentence-ID prasyarat | AR-EVD-CYC03-D |
63: | E — Gerbang | audit reseptif, terbimbing, transfer, dan review | AR-EVD-CYC03-GATE |
64: | F — Integrasi | AR-TXT-000001 | hanya setelah SIAP INTEGRASI |
65: | G — Transfer | retelling dan penggantian unsur | AR-EVD-CYC03-TR |
66: | H — Retensi | pemeriksaan tertunda | AR-EVD-CYC03-RET |
67: 
68: Evidence-ID di atas adalah slot bukti calon, bukan bukti yang sudah tersedia.
69: 
70: ## 4. Instrumen Gerbang Pilot
71: 
72: | Gate-Item | Tugas | Lulus bila |
73: |---|---|---|
74: | AR-GATE-000001 | memilih makna/referen 12 lema dalam urutan acak | pola bukti memadai menurut rubrik tervalidasi |
75: | AR-GATE-000002 | mengenali lima bentuk mudhari‘ | tidak bergantung pada contoh identik |
76: | AR-GATE-000003 | memasangkan pelaku, tindakan, objek/tempat | hubungan makna dipahami |
77: | AR-GATE-000004 | melengkapi enam pola kalimat prasyarat | unsur dan struktur tepat |
78: | AR-GATE-000005 | menyusun dua kombinasi baru dari unsur lama | menunjukkan transfer terbimbing |
79: | AR-GATE-000006 | mengingat kembali target lama setelah jeda | retensi cukup menurut protokol |
80: | AR-GATE-000007 | pemeriksaan beban, aksesibilitas, dan safeguarding | tidak ada risiko yang belum dimitigasi |
81: 
82: Ambang numerik sengaja belum ditetapkan sebelum review asesmen dan pilot empiris.
83: 
84: ## 5. Aturan Keputusan
85: 
86: - **BELUM SIAP:** prasyarat inti belum dipahami; kembali ke fase terkait.
87: - **BERKEMBANG:** sudah ada bukti tetapi belum stabil/mandiri; lakukan latihan dan pemeriksaan ulang.
88: - **SIAP INTEGRASI:** seluruh prasyarat teks memiliki pola bukti yang memadai; AR-TXT-000001 boleh dibuka.
89: - **TERPELIHARA:** retensi tertunda dan transfer telah dibuktikan setelah integrasi.
90: 
91: Satu keberhasilan sesaat tidak cukup untuk mengubah status menjadi SIAP INTEGRASI.
92: 
93: ## 6. Kegiatan Setelah Gerbang Lulus
94: 
95: 1. sima‘ teks utuh tanpa menampilkan unsur baru;
96: 2. menunjukkan pemahaman umum;
97: 3. menjawab AR-TQ-000001–000003;
98: 4. membaca terpandu hanya bila whitelist literasi mengizinkan;
99: 5. retelling dengan AR-TP-000001;
100: 6. transfer dengan AR-TP-000002;
101: 7. retensi tertunda dengan AR-TP-000003.
102: 
103: ## 7. Blocker
104: 
105: AR-CYC-000003 belum dapat dipetakan final karena:
106: 
107: - daftar lema dan tashrif belum lulus review ahli;
108: - naturalitas, vokalisasi, dan i‘rab belum disahkan;
109: - instrumen serta rubrik gerbang belum divalidasi;
110: - beban peserta dan jadwal jeda belum diuji;
111: - whitelist literasi halaman belum dipetakan;
112: - DEC-CUR-003 dan Arabic progression belum diratifikasi.
113: 
114: ## 8. Riwayat
115: 
116: | Versi | Tanggal | Ringkasan |
117: |---|---|---|
118: | 0.1.0-id | 28 Juli 2026 | Paket operasional pertama untuk gerbang AR-TXT-000001 |
119: 

## curriculum/BAT-ARB-005-Paket-Integrasi-Pilot-Tahap-1-3.md
Blob: 3c4af7e277f3a6d1fc41faf6373f5919fffcb979

1: # BAT-ARB-005 — Paket Integrasi Pilot Tahap 1–3
2: 
3: **Batch-ID:** BAT-ARB-005  
4: **Cycle-ID:** AR-CYC-000001  
5: **Status:** DRAF PILOT — GERBANG BELUM DIJALANKAN  
6: **Tanggal:** 28 Juli 2026  
7: **Teks tujuan:** AR-TXT-000002  
8: **Pengendali:** DEC-CUR-003, ACP-QUR-001, MAT-ARB-002, STD-ARB-002  
9: **Prasyarat:** LEX-ARB-001, BAT-ARB-001
10: 
11: ## 1. Microtext Tujuan
12: 
13: > هٰذَا مُعَلِّمٌ. هٰذَا كِتَابٌ. هٰذَا قَلَمٌ.
14: 
15: Arti: Ini guru laki-laki. Ini buku. Ini pena.
16: 
17: Teks terdiri atas tiga kalimat identifikasi dan tidak memuat kosa kata, bentuk, atau kaidah baru tersembunyi.
18: 
19: ## 2. Prasyarat
20: 
21: | Jenis | ID/objek |
22: |---|---|
23: | Lema | AR-LEX-000011, AR-LEX-000001, AR-LEX-000002 |
24: | Unsur fungsional | AR-FW-000001 — هٰذَا |
25: | Struktur | AR-GRM-000001 |
26: | Pola | AR-PAT-000001 |
27: | Kalimat | AR-SEN-000009, AR-SEN-000001, AR-SEN-000002 |
28: 
29: ## 3. Gerbang Ketuntasan
30: 
31: | Gate-Item | Bukti yang dicari |
32: |---|---|
33: | AR-GATE-000008 | mengenali dan menunjuk tiga referen dalam urutan acak |
34: | AR-GATE-000009 | memahami fungsi هٰذَا |
35: | AR-GATE-000010 | menyusun pola هٰذَا + isim dengan tiga lema |
36: | AR-GATE-000011 | mengganti satu lema dengan lema lama lain |
37: | AR-GATE-000012 | mengulang setelah jeda terencana |
38: | AR-GATE-000013 | beban, aksesibilitas, dan safeguarding diterima |
39: 
40: Status SIAP INTEGRASI hanya diberikan setelah pola bukti memadai; satu jawaban benar tidak cukup. Ambang numerik menunggu validasi.
41: 
42: ## 4. Setelah Gerbang
43: 
44: - sima‘ tiga kalimat sebagai satu microtext;
45: - memilih urutan gambar/referen;
46: - menyebut kembali dengan bantuan;
47: - mengganti satu benda menggunakan kosa kata lama;
48: - pemeriksaan retensi tertunda.
49: 
50: ## 5. Blocker
51: 
52: Review ahli bahasa, validasi instrumen, penetapan jadwal jeda, whitelist literasi, dan pemetaan halaman masih terbuka.
53: 
54: ## 6. Riwayat
55: 
56: | Versi | Tanggal | Ringkasan |
57: |---|---|---|
58: | 0.1.0-id | 28 Juli 2026 | Paket gerbang microtext pertama Tahap 1–3 |
59: 

## curriculum/BAT-ARB-006-Paket-Integrasi-Pilot-Tahap-4-6.md
Blob: 176692639cb4201ad2adeb08583c022d9aba3bf4

1: # BAT-ARB-006 — Paket Integrasi Pilot Tahap 4–6
2: 
3: **Batch-ID:** BAT-ARB-006  
4: **Cycle-ID:** AR-CYC-000002  
5: **Status:** DRAF PILOT — GERBANG BELUM DIJALANKAN  
6: **Tanggal:** 28 Juli 2026  
7: **Teks tujuan:** AR-TXT-000003  
8: **Pengendali:** DEC-CUR-003, ACP-QUR-001, MAT-ARB-002, STD-ARB-002  
9: **Prasyarat:** LEX-ARB-001–002, BAT-ARB-001–002
10: 
11: ## 1. Paragraf Tujuan
12: 
13: > هٰذَا فَصْلٌ نَظِيفٌ. هٰذِهِ نَافِذَةٌ مَفْتُوحَةٌ. الْكِتَابُ عَلَى الْمَكْتَبِ. الْقَلَمُ عَلَى الْكِتَابِ. هٰذَا كِتَابُ الطَّالِبِ.
14: 
15: Arti: Ini ruang kelas yang bersih. Ini jendela yang terbuka. Buku itu berada di atas meja. Pena itu berada di atas buku. Ini buku milik pelajar.
16: 
17: ## 2. Prasyarat
18: 
19: | Jenis | ID/objek |
20: |---|---|
21: | Lema | AR-LEX-000017, 000027, 000020, 000030, 000001, 000031, 000002, 000013 |
22: | Unsur fungsional | AR-FW-000001, AR-FW-000002, AR-FW-000006 |
23: | Struktur | AR-GRM-000005–000007 |
24: | Pola | AR-PAT-000005–000007 |
25: | Kalimat | AR-SEN-000029, 000032–000034, 000039 |
26: 
27: Bentuk muannats sifat, ال, dan perubahan akhir bernilai nol pada hitungan lema tetapi tetap memerlukan bukti penguasaan.
28: 
29: ## 3. Murojaah Kumulatif
30: 
31: - هٰذَا, كِتَابٌ, قَلَمٌ, طَالِبٌ berasal dari tahap sebelumnya;
32: - kosa kata tahap lama muncul dalam struktur yang lebih kaya;
33: - teks menguji transfer dari identifikasi menuju deskripsi, lokasi, dan kepemilikan;
34: - tidak ada target baru yang disamarkan sebagai review.
35: 
36: ## 4. Gerbang Ketuntasan
37: 
38: | Gate-Item | Bukti yang dicari |
39: |---|---|
40: | AR-GATE-000014 | memahami delapan lema dan bentuk yang diperlukan |
41: | AR-GATE-000015 | memasangkan sifat sesuai gender |
42: | AR-GATE-000016 | memahami lokasi dengan عَلَى |
43: | AR-GATE-000017 | memahami idhafah sederhana |
44: | AR-GATE-000018 | menyusun dua kalimat baru dari unsur lama |
45: | AR-GATE-000019 | mempertahankan target Tahap 1–3 setelah jeda |
46: | AR-GATE-000020 | beban, aksesibilitas, dan safeguarding diterima |
47: 
48: Status SIAP INTEGRASI memerlukan pola bukti reseptif, terbimbing, transfer, dan retensi. Ambang numerik menunggu validasi.
49: 
50: ## 5. Setelah Gerbang
51: 
52: - sima‘ paragraf;
53: - identifikasi gambaran umum dan informasi lokasi;
54: - menjawab siapa pemilik buku;
55: - retelling dengan gambar kelas;
56: - mengganti satu benda/sifat memakai inventaris lama;
57: - retensi tertunda.
58: 
59: ## 6. Blocker
60: 
61: Naturalitas dan i‘rab, posisi pengenalan ال, kelayakan idhafah Tahap 5, validasi instrumen, whitelist literasi, serta pemetaan halaman masih terbuka.
62: 
63: ## 7. Riwayat
64: 
65: | Versi | Tanggal | Ringkasan |
66: |---|---|---|
67: | 0.1.0-id | 28 Juli 2026 | Paket gerbang paragraf Tahap 4–6 |
68: 