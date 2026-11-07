# K03 — Mengenali Nakirah dan Tanwin

**Kode:** REC-NAK-TAN  
**Layer:** A — Fondasi Pengenalan  
**Status:** CONTENT COMPLETE / QURAN EVIDENCE VERIFIED / EXPERT REVIEW PENDING  
**Prasyarat:** K01 — Mengenali Isim Dasar; K02 — Mengenali Alif Lam  
**Standar:** COMPETENCY-AUTHORING-STANDARD-v1.1 + BEGINNER-PEDAGOGY-RULES-v1.0

## AHA K03
**Saya bisa melihat tanwin di akhir sebagian isim Al-Qur'an, meskipun belum mengetahui arti katanya.**

## Capaian
Peserta mampu mengenali tanda tanwin **ـٌ / ـٍ / ـً** pada isim Qurani sederhana dan menggunakannya sebagai salah satu ciri mudah untuk menemukan bentuk nakirah sederhana, tanpa menganggap tanwin sebagai satu-satunya penentu seluruh konsep nakirah.

# 1. LIHAT — لاحظ
Jangan mulai dengan definisi. Minta peserta melihat **bagian akhir kata**. Gunakan subset `stage=lihat` dari bank canonical.

Contoh mudah:
- **أَحَدٌ**
- **عَابِدٌ**
- **خُسْرٍ**
- **غَاسِقٍ**
- **عَلَقٍ**
- **كُفُوًا**
- **نَارًا**
- **أَفْوَاجًا**

Instruksi pemula: **tidak perlu menerjemahkan semuanya. Cari dua harakat di bagian akhir kata.**

# 2. TEMUKAN — اكتشف
Bandingkan bentuk bertanwin dan tidak bertanwin:
- **أَحَدٌ** ↔ **ٱلصَّمَدُ**
- **عَابِدٌ** ↔ **عَابِدُونَ**
- **خُسْرٍ** ↔ **ٱلْإِنسَانَ**
- **غَاسِقٍ** ↔ **ٱلْفَلَقِ**
- **حَبْلٌ** ↔ **ٱلْحَطَبِ**

### Recycle
K01: apakah target termasuk isim?  
K02: apakah ada **ال**?  
K03: apakah ada **tanwin** di akhirnya?

# 3. CIRI MUDAH
1. Lihat **akhir isim**.
2. Jika ada **ـٌ, ـٍ, atau ـً**, itu adalah bentuk tanwin yang menjadi target visual K03.
3. Tanwin adalah petunjuk yang sangat berguna untuk menemukan banyak isim nakirah sederhana.
4. Ciri ini **bukan rumus mutlak** bahwa semua nakirah harus bertanwin.
5. Fokus K03 adalah mata cepat menemukan tanwin, bukan teori lengkap ma'rifah–nakirah, i'rab, atau tajwid tanwin.

# 4. PAHAMI — افهم
**Tanwin (التنوين)** pada tahap ini dikenali dari tanda akhir **ـٌ / ـٍ / ـً**. Istilah diberikan setelah peserta terlebih dahulu melihat dan menemukan pola.

### Ingat
**Lihat akhir kata → cari dua harakat → tandai tanwin.**

### Belum perlu
- seluruh pembagian ma'rifah dan nakirah;
- sebab i'rab raf', nasb, dan jar;
- hukum tajwid nun/tanwin;
- jenis-jenis tanwin lanjutan;
- analisis fungsi sintaksis.

# 5. COBA — طبّق
Bank latihan menggerakkan peserta dari satu token → pasangan → potongan ayat. Operasi utama: lingkari, pilih, cocokkan, bedakan, tandai jenis bentuk tanwin, dan temukan target pada evidence Qurani.

# 6. BUKTIKAN — أثبت
Tujuh evidence `stage=buktikan` disimpan sebagai **unseen set** dan tidak digunakan pada LIHAT/TEMUKAN/COBA. Peserta harus menemukan target tanpa bantuan arti. Reserve set disimpan untuk variasi RIQA OS, remedial, pengayaan, dan asesmen alternatif.

# Bank Canonical K03
- `quran-examples.json` — **45 evidence**, dengan metadata stage dan status verifikasi.
- `vocabulary.json` — **15 vocabulary** awal/recycle.
- `assessment.json` — **30 item** recognition → discrimination → application → analysis → transfer, lengkap dengan answer/explanation.
- `teacher-notes.md` — panduan mengajar, boundary, miskonsepsi, dan QA gate.

## Distribusi Evidence
**13 LIHAT + 10 TEMUKAN + 11 COBA + 7 BUKTIKAN + 4 RESERVE = 45 evidence.**

Duplikasi lintas stage tertentu adalah recycle pedagogis dan tidak dianggap lexical diversity baru. BUKTIKAN tetap dipisahkan sebagai unseen evidence.

## QA Qurani
Evidence utama dan bentuk tanwin telah diaudit terhadap sumber Qur'an/corpus. Sebelum layout PDF final, pipeline tetap wajib menjalankan normalisasi orthography Utsmani canonical agar bentuk tampilan mengikuti satu mushaf source secara konsisten. Normalisasi tampilan tidak mengubah target kompetensi atau rujukan evidence.

## Production Gate K03
- [x] capaian dan boundary ditetapkan
- [x] AHA tunggal ditetapkan
- [x] pedagogi LIHAT → TEMUKAN → CIRI MUDAH → PAHAMI → COBA → BUKTIKAN diterapkan
- [x] recycle K01–K02 dirancang
- [x] 40–50 evidence Qurani tersedia — **45 evidence**
- [x] distribusi evidence pedagogis final — **13/10/11/7/4**
- [x] vocabulary bank — **15 item**
- [x] 25–40 latihan/soal — **30 item**
- [x] answer key + pembahasan tersedia di `assessment.json`
- [x] teacher notes tersedia
- [x] QA evidence Qurani dan rujukan
- [x] unseen BUKTIKAN dipisahkan dari teaching/practice set
- [ ] normalisasi orthography Utsmani canonical saat production pipeline
- [ ] review ahli Bahasa Arab/nahwu
- [ ] review ahli pembelajaran Bahasa Arab
- [ ] validasi mastery threshold melalui pilot
- [ ] K03 FROZEN v1.0

### Aturan status
Artifact yang sudah selesai wajib langsung dicentang. Status FROZEN hanya diberikan setelah review ahli dan pilot/validasi yang diwajibkan selesai.