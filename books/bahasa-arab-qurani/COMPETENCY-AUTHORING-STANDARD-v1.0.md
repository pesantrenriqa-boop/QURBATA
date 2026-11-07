# QURBATA — COMPETENCY AUTHORING STANDARD v1.0

**Status:** FROZEN  
**Tanggal freeze:** 2026-09-26  
**Cakupan:** Tangga Kompetensi Bahasa Arab Qurani QURBATA K01–K65  
**Prinsip:** GitHub adalah sumber kebenaran materi. PDF/buku dan RIQA OS adalah produk turunan dari data yang telah divalidasi.

## 1. Backbone tunggal K01–K65

K01–K65 adalah urutan canonical. Setiap kompetensi harus berupa satu operasi bahasa yang spesifik, terukur, memiliki prasyarat, batas materi, evidence, latihan, evaluasi, dan status validasi.

Materi tidak boleh melompati target struktur kompetensi yang belum diperkenalkan sebagai target pembelajaran.

## 2. Dua jalur, satu tangga kompetensi

### A. Bahasa Arab Qurani
Korpus inti 100% Al-Qur'an. Contoh inti, pemantik, penemuan pola, analisis, dan evidence kompetensi wajib berasal dari teks Al-Qur'an autentik dan memiliki rujukan surah–ayat.

Tidak boleh membuat kalimat buatan lalu menampilkannya seolah-olah sebagai ayat Al-Qur'an.

### B. Bi'ah 'Arabiyah QURBATA
Dikembangkan sebagai corpus dan produk tersendiri: mufradat, ungkapan, instruksi, dialog, listening, speaking, dan tugas komunikatif. Jalur Bi'ah tetap mengikuti progression K01–K65. Setiap item produktif harus memiliki `first_allowed_competency` agar struktur yang belum dipelajari tidak dijadikan target produksi terlalu dini.

## 3. Pola pedagogis setiap kompetensi

Urutan belajar canonical:

**لاحظ → اكتشف → افهم → طبّق → حلّل → استخدم**  
**Amati → Temukan → Pahami → Terapkan → Analisis → Gunakan**

Setiap K01–K65 wajib memiliki 10 komponen berikut.

1. **Capaian Kompetensi** — satu kemampuan spesifik dan terukur.
2. **Pemantik Qurani** — 1–2 potongan ayat untuk observasi awal.
3. **Temukan Polanya** — aktivitas induktif untuk menemukan ciri/hubungan sebelum teori formal.
4. **Pahami Kaidah** — penjelasan ringkas: pengertian, ciri, fungsi, batas kompetensi, dan kesalahan umum.
5. **Contoh Qurani Bertingkat** — contoh autentik dari mudah menuju lebih kompleks; setiap contoh memuat teks, surah–ayat, target, makna kontekstual, dan catatan analisis.
6. **Mufradat & Ungkapan** — kosakata/ungkapan relevan; kosakata lama harus direcycle agar akumulatif dan tidak boros pengulangan tanpa tujuan.
7. **Latihan Terbimbing** — recognition/comprehension: mengenali, menandai, mencocokkan, mengelompokkan, memilih, atau melengkapi.
8. **Latihan Penggunaan/Analisis** — application dan transfer pada evidence/contoh baru.
9. **Uji Kompetensi** — kombinasi recognition → comprehension → application → transfer; kunci dan pembahasan disimpan terpisah dari tampilan siswa bila diperlukan.
10. **Tadabbur & Transfer** — refleksi makna yang relevan dan penguatan hubungan struktur–makna. Aktivitas Bi'ah produktif dikelola pada jalur Bi'ah terpisah tetapi ditautkan ke K yang sama.

## 4. Standar bank materi per kompetensi

Repo harus lebih kaya daripada buku. Target bank per kompetensi:

- minimal 10 contoh Qurani terverifikasi; ideal 10–20;
- sekitar 10–15 mufradat/ungkapan relevan (disesuaikan kebutuhan K, bukan kuota mekanis);
- sekitar 25–40 item bank latihan/soal gabungan;
- kunci jawaban dan pembahasan;
- kesalahan umum/miskonsepsi;
- prasyarat dan batas kompetensi;
- catatan pedagogis guru;
- provenance/rujukan dan status validasi evidence.

Buku hanya memilih subset terbaik. Sisa bank digunakan untuk RIQA OS, ujian, remedial, pengayaan, guru, dan edisi berikutnya.

## 5. Aturan evidence Qurani

Setiap evidence Qurani wajib menyimpan sekurang-kurangnya:

- teks Arab yang diverifikasi;
- nama/nomor surah dan nomor ayat;
- target span/token kompetensi;
- terjemah/makna kontekstual untuk kebutuhan belajar;
- alasan contoh tersebut relevan;
- tingkat kesulitan;
- status verifikasi.

Evidence tidak boleh dipakai sebagai contoh final jika teks atau rujukannya belum diverifikasi.

## 6. Gradasi latihan dan asesmen

Bank soal harus bergerak bertahap:

1. Recognition — menemukan target.
2. Comprehension — menjelaskan/membedakan target.
3. Application — menerapkan kompetensi pada contoh baru.
4. Analysis — memetakan hubungan atau fungsi.
5. Transfer — menggunakan kompetensi pada evidence baru yang belum dipakai dalam paparan.

Soal transfer tidak boleh hanya mengulang contoh pengajaran dengan perubahan kosmetik.

## 7. Vocabulary governance

Jumlah kosakata tidak otomatis diberi label CEFR A1/A2. Metadata kosakata harus memungkinkan pemetaan kemudian terhadap benchmark eksternal.

Minimal metadata yang disiapkan: bentuk Arab, makna, first competency, kemunculan Qurani/rujukan, status receptive/productive, recycle history, dan jalur (Qurani/Bi'ah).

Target kuantitatif QURBATA dikelola terpisah dari klaim level CEFR sampai pemetaan dan validasi dilakukan.

## 8. Struktur data per kompetensi

Struktur target:

```text
Kxx/
├── competency.yaml
├── explanation.md
├── quran-examples.json
├── vocabulary.json
├── guided-practice.json
├── application.json
├── assessment.json
├── answer-key.json
└── teacher-notes.md
```

Implementasi boleh menggunakan JSON/YAML/Markdown selama schema canonical tetap konsisten dan dapat diproses otomatis.

## 9. Production gate

Urutan kerja wajib:

**canonical competency → bank materi → verifikasi → freeze kompetensi → seleksi materi buku → layout → PDF**.

PDF tidak menjadi sumber kebenaran. Perubahan substansi dilakukan pada data sumber GitHub, lalu produk PDF dibangun ulang.

## 10. Freeze policy

Dokumen ini adalah baseline **v1.0 FROZEN**. Perubahan substantif terhadap 10 komponen, prinsip korpus Qurani, dua jalur Qurani/Bi'ah, atau production gate harus dilakukan melalui versi baru (v1.1/v2.0) dengan alasan perubahan tercatat. Penambahan isi K01–K65 yang mengikuti standar ini tidak dianggap mengubah standar.
