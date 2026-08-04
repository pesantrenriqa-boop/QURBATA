# QURBATA Jilid 1–8 — Launch Roadmap & Progress Status V1

Tanggal status: 5 Agustus 2026
Branch kerja: `content/qurbata-jilid-1-8-production`
Target akhir: delapan jilid siap layout, siap audit, dan siap produksi.

## Aturan pelaporan progres

1. Progres hanya naik jika ada artefak nyata dan dapat diverifikasi.
2. Dokumen konsep tidak disamakan dengan implementasi.
3. Dataset besar dinyatakan selesai hanya jika dapat direproduksi dari corpus dan runtime repository.
4. Halaman buku tidak dinyatakan selesai sebelum lolos pedagogical gate.
5. Layout tidak dimulai sebelum isi jilid terkait dibekukan.
6. Ide baru yang tidak wajib untuk launching masuk backlog V2.

## Ringkasan progres keseluruhan

**Progres terverifikasi saat ini: 31%**

Angka ini bukan progres estetika atau jumlah dokumen. Ini merupakan progres berbobot terhadap jalur launching delapan jilid.

| Fase | Bobot | Status | Progres fase | Kontribusi |
|---|---:|---|---:|---:|
| 1. Corpus dan provenance | 8% | SUBSTANTIALLY COMPLETE | 95% | 7.6% |
| 2. Token, lexicon, dan kandidat dasar | 10% | SUBSTANTIALLY COMPLETE | 90% | 9.0% |
| 3. Competency dependency map | 8% | IMPLEMENTED, NEEDS FINAL AUDIT | 80% | 6.4% |
| 4. Pedagogical engine dan validator | 14% | IMPLEMENTED, CI PASS NOT YET VERIFIED | 55% | 7.7% |
| 5. QWO/QPO/QAO production datasets | 12% | PARTIAL | 5% | 0.6% |
| 6. Book Composer production | 10% | EARLY IMPLEMENTATION | 0% | 0.0% |
| 7. Isi final Jilid 1–8 | 20% | NOT STARTED AFTER ENGINE FREEZE | 0% | 0.0% |
| 8. Layout dan readability validation | 8% | NOT STARTED | 0% | 0.0% |
| 9. QA ahli, tashih, dan proofing | 6% | NOT STARTED | 0% | 0.0% |
| 10. Release package dan launching | 4% | NOT STARTED | 0% | 0.0% |

Total kontribusi dibulatkan: **31%**.

## Roadmap menuju 100%

### M1 — Fondasi mesin terverifikasi — target kumulatif 40%

Kriteria selesai:

- seluruh competency ID valid dan tanpa dependency cycle;
- rule matrix dan policy matrix sinkron;
- object gate, page gate, jilid gate, dan series gate berjalan;
- regression test lulus pada GitHub Actions;
- kasus salah seperti `ؤُ` pada tahap awal, `هُوَ` sebagai mad waw, objek tanpa sumber, dan pengulangan lintas jilid otomatis ditolak;
- laporan hasil test tersimpan.

Status: **aktif**.

### M2 — Master object production — target kumulatif 55%

Kriteria selesai:

- QWO final tersedia dan seluruh objek memiliki source reference;
- QPO dibentuk dari frasa Al-Qur’an sesuai kompetensi;
- QAO dibentuk dari ayat dan potongan ayat;
- setiap objek memiliki feature trace, competency label, difficulty, dan status;
- deduplikasi berlaku untuk seluruh seri;
- cakupan kompetensi dan shortage report tersedia.

Status: menunggu M1.

### M3 — Book Composer production-ready — target kumulatif 65%

Kriteria selesai:

- composer selalu memulai dari kompetensi dan dependency;
- objek dipilih hanya dari whitelist yang sudah lolos gate;
- review mengulang kompetensi dengan objek baru;
- lafẓul jalālah memiliki bab khusus;
- transisi objek mengikuti perkembangan: huruf/fragmen → kata → frasa → potongan ayat → ayat utuh;
- composer menghasilkan shortage/error report, bukan memaksakan objek yang salah.

Status: menunggu M1–M2.

### M4 — Isi Jilid 1–2 dibekukan — target kumulatif 73%

Kriteria selesai per jilid:

- tangga kompetensi final;
- seluruh halaman terisi objek nyata;
- setiap halaman lolos page gate;
- seluruh jilid lolos jilid gate;
- tidak ada pengulangan objek utama;
- halaman khusus evaluasi, hafalan, akhlak, dan Bahasa Arab ditempatkan sesuai konstitusi;
- contoh satu halaman layout diuji sebelum layout penuh jilid.

Status: belum dimulai setelah invalidasi halaman legacy.

### M5 — Isi Jilid 3–4 dibekukan — target kumulatif 81%

Kriteria tambahan:

- frasa Al-Qur’an mulai dominan sesuai kompetensi;
- potongan ayat diperkenalkan bertahap;
- lafẓul jalālah tidak muncul sebelum babnya selesai;
- objek panjang mengikuti kesiapan kompetensi, bukan nomor jilid secara mekanis.

Status: belum dimulai.

### M6 — Isi Jilid 5–6 dibekukan — target kumulatif 88%

Kriteria tambahan:

- potongan ayat menengah dan ayat utuh pendek digunakan;
- integrasi mad, sukun, tasydid, tanwin, hamzah, waqaf, dan sambungan mengikuti dependency;
- ayat panjang hanya digunakan jika seluruh kompetensi di dalamnya telah dikuasai.

Status: belum dimulai.

### M7 — Isi Jilid 7–8 dibekukan — target kumulatif 93%

Kriteria tambahan:

- ayat utuh sedang dan panjang;
- integrasi multi-kompetensi;
- latihan kelancaran, waqaf, dan ibtida;
- series validator lulus untuk seluruh Jilid 1–8.

Status: belum dimulai.

### M8 — Layout, readability, dan proof — target kumulatif 97%

Kriteria selesai:

- satu halaman prototipe tiap jilid disetujui sebelum layout penuh;
- ukuran huruf, spasi, arah baca, jumlah objek, dan ritme visual diuji;
- layout A5 potret konsisten;
- font Qur’ani dan teks Utsmani tampil benar;
- guru mudah menunjuk dan santri mudah mengikuti;
- seluruh halaman diekspor dan diperiksa.

Status: belum dimulai.

### M9 — QA ahli dan release — target 100%

Kriteria selesai:

- tashih teks Al-Qur’an;
- audit pedagogis akhir;
- proofing cetak;
- checksum release;
- paket master Jilid 1–8;
- changelog dan versi rilis;
- keputusan GO untuk launching.

Status: belum dimulai.

## Sprint aktif sekarang

Nama sprint: **M1 — Foundation Verification**

Urutan kerja wajib:

1. memastikan workflow CI benar-benar menjalankan smoke test;
2. memperbaiki semua path/import yang gagal;
3. menjalankan object, page, jilid, dan series regression tests;
4. menyimpan test report;
5. menaikkan status fondasi hanya jika semua test PASS;
6. setelah itu meregenerasi Halaman 1 dan Halaman 10 sebagai acceptance test.

## Acceptance test pertama setelah M1

- Halaman 1 hanya memuat kompetensi yang telah diaktifkan.
- Halaman 10 tidak boleh memuat hamzah kompleks sebelum kompetensinya.
- Semua objek mempunyai sumber Al-Qur’an.
- Tidak ada objek utama yang berulang.
- Bila kandidat aman kurang dari kebutuhan, sistem harus menghasilkan `SHORTAGE`, bukan mengambil objek yang melompat.

## Definition of Done 100%

Proyek dinyatakan 100% hanya ketika delapan jilid:

- memiliki isi halaman nyata;
- mengikuti dependency kompetensi;
- seluruh objek berasal dari Al-Qur’an dan dapat ditelusuri;
- lulus object/page/jilid/series validator;
- tidak mengulang objek utama;
- telah melewati audit pedagogis dan tashih;
- selesai layout dan proof cetak;
- memiliki paket release yang siap diluncurkan.
