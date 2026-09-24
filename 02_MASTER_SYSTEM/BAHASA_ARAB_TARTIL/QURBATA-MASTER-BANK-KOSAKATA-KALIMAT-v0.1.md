# MASTER BANK KOSAKATA & KALIMAT BAHASA ARAB QURBATA

**Status:** ACTIVE MASTER — v0.1  
**Tanggal:** 2026-09-24  
**Scope awal:** Bahasa Arab yang telah terverifikasi dari master Bi'ah Arabiyah QURBATA Tartil.  
**Tujuan:** menjadi single source of truth untuk mufradat, ta'birat, instruksi, respons, dan interaksi Bahasa Arab QURBATA yang selanjutnya dapat dipetakan ke buku, Marhalah, RIQA OS, audio, asesmen, dan penelitian.

> Catatan governance: v0.1 adalah konsolidasi awal dari sumber yang telah terverifikasi. Corpus Bahasa Arab standalone, paragraf, dan sumber lain belum boleh dianggap sudah seluruhnya terimpor sebelum audit sumber selesai.

## 1. Sumber otoritatif awal

1. `02_MASTER_SYSTEM/BAHASA_ARAB_TARTIL/MASTER-BIAH-ARABIYYAH-v0.1.md`
2. `02_MASTER_SYSTEM/QURBATA_BIAH_ARABIYAH_INSTRUCTION_MASTER_FROZEN-v1.0.md`
3. `02_MASTER_SYSTEM/BAHASA_ARAB_TARTIL/README.md`
4. `research/arabic-competency-ladder/K01-K65-DEFINITION-RECOVERY-REGISTER-v0.1.md` — hanya untuk crosswalk kompetensi yang definisinya KNOWN; tidak boleh mengarang definisi K yang UNKNOWN/PARTIAL.

## 2. Skema ID

- `INS` = instruksi guru
- `RES` = respons santri
- `INT` = interaksi pembelajaran
- `VOC` = mufradat lingkungan
- `SEQ` = rangkaian instruksi
- `QUR` = kosakata/struktur berbasis corpus Al-Qur'an (akan diisi melalui audit corpus khusus)

Field pengembangan berikutnya: `source`, `jilid`, `page`, `marhalah`, `K-ID`, `usage_context`, `audio_status`, `assessment_status`, `RIQA_OS_status`.

## 3. Bank instruksi guru

| ID | Arab | Makna | Fungsi |
|---|---|---|---|
| INS-001 | السَّلَامُ عَلَيْكُمْ | Semoga keselamatan atas kalian | Salam pembuka |
| INS-002 | اُنْظُرْ | Lihat/perhatikan | Mengarahkan perhatian |
| INS-003 | اِسْتَمِعْ | Dengarkan | Mendengarkan model |
| INS-004 | رَدِّدْ | Tirukan/ulangi | Menirukan model guru |
| INS-005 | اِقْرَأْ | Bacalah | Membaca |
| INS-006 | أَعِدْ | Ulangi | Mengulang bacaan |
| INS-007 | اِفْتَحْ | Bukalah | Membuka buku/halaman |
| INS-008 | أَغْلِقْ | Tutuplah | Menutup buku/halaman |
| INS-009 | مَرَّةً أُخْرَى | Sekali lagi | Mengulang aktivitas |
| INS-010 | قِفْ | Berhenti | Menghentikan bacaan/aktivitas |
| INS-011 | وَاصِلْ | Lanjutkan | Melanjutkan bacaan/aktivitas |
| INS-012 | أَجِبْ | Jawablah | Meminta jawaban |
| INS-013 | اِنْتَبِهْ | Perhatikan | Menguatkan perhatian |
| INS-014 | اِفْتَحِ الْكِتَابَ | Bukalah buku | Instruksi kelas |
| INS-015 | اِفْتَحِ الْمُصْحَفَ | Bukalah mushaf | Instruksi pembelajaran Al-Qur'an |
| INS-016 | أَغْلِقِ الْكِتَابَ | Tutuplah buku | Instruksi kelas |
| INS-017 | أَغْلِقِ الْمُصْحَفَ | Tutuplah mushaf | Instruksi pembelajaran Al-Qur'an |
| INS-018 | اِقْرَأْ مَرَّةً أُخْرَى | Bacalah sekali lagi | Pengulangan bacaan |

## 4. Bank respons santri

| ID | Arab | Makna | Fungsi |
|---|---|---|---|
| RES-001 | وَعَلَيْكُمُ السَّلَامُ | Dan semoga keselamatan atas kalian | Jawaban salam |
| RES-002 | نَعَمْ | Ya | Respons afirmatif |
| RES-003 | لَا | Tidak | Respons negatif |
| RES-004 | حَاضِرٌ | Siap/hadir (lk.) | Respons kesiapan |
| RES-005 | حَاضِرَةٌ | Siap/hadir (pr.) | Respons kesiapan |
| RES-006 | فَهِمْتُ | Saya paham | Konfirmasi pemahaman |
| RES-007 | لَمْ أَفْهَمْ | Saya belum paham | Menyatakan belum paham |

## 5. Bank interaksi pembelajaran

| ID | Arab | Makna | Fungsi |
|---|---|---|---|
| INT-001 | هَلْ فَهِمْتَ؟ | Apakah kamu paham? (lk.) | Cek pemahaman |
| INT-002 | هَلْ فَهِمْتِ؟ | Apakah kamu paham? (pr.) | Cek pemahaman |
| INT-003 | مَا هَذَا؟ | Apa ini? | Identifikasi objek |
| INT-004 | أَيْنَ ...؟ | Di mana ...? | Menanyakan lokasi |
| INT-005 | أَحْسَنْتَ | Bagus (lk.) | Penguatan positif |
| INT-006 | أَحْسَنْتِ | Bagus (pr.) | Penguatan positif |
| INT-007 | صَحِيحٌ | Benar | Umpan balik |
| INT-008 | خَطَأٌ | Salah | Umpan balik |

## 6. Bank mufradat lingkungan awal

| ID | Arab | Makna/konteks |
|---|---|---|
| VOC-001 | كِتَابٌ | buku |
| VOC-002 | صَفْحَةٌ | halaman |
| VOC-003 | قَلَمٌ | pena |
| VOC-004 | مُعَلِّمٌ | guru laki-laki |
| VOC-005 | مُعَلِّمَةٌ | guru perempuan |
| VOC-006 | طَالِبٌ | peserta laki-laki |
| VOC-007 | طَالِبَةٌ | peserta perempuan |
| VOC-008 | دَرْسٌ | pelajaran |
| VOC-009 | مُصْحَفٌ | mushaf — terverifikasi muncul dalam master instruksional; dimasukkan sebagai lemma untuk cross-reference |

## 7. Rangkaian bahasa kelas

| ID | Rangkaian | Fungsi |
|---|---|---|
| SEQ-001 | اِفْتَحِ الْكِتَابَ → اِسْتَمِعْ → اِقْرَأْ → أَعِدْ | buka → dengarkan → baca → ulangi |
| SEQ-002 | اِفْتَحِ الْمُصْحَفَ → اُنْظُرْ → اِقْرَأْ → قِفْ / وَاصِلْ | membuka mushaf dan mengontrol alur bacaan |

## 8. Tangga penggunaan

1. **Fase 1 — rutinitas dasar:** salam, baca, ulangi, dengarkan, lihat, buka, tutup.
2. **Fase 2 — kontrol aktivitas:** sekali lagi, berhenti, lanjutkan, jawab, perhatikan.
3. **Fase 3 — respons santri:** ya, tidak, paham, belum paham, siap.
4. **Fase 4 — interaksi dua arah:** cek pemahaman, apa ini, di mana, benar, salah, bagus.
5. **Fase 5 — kombinasi:** dua atau lebih ungkapan dikerjakan sebagai rangkaian aktivitas kelas.

## 9. Crosswalk awal ke kompetensi Bahasa Arab Qurani

Register K01–K65 yang tersedia masih berstatus recovery. Hanya K04, K09, K10, K17, K21, K27, K29, K32, K35, dan K36 yang saat ini berstatus KNOWN. Dari bank Bi'ah ini, keterkaitan yang paling langsung dan aman untuk dicatat sementara adalah:

- **K29 — imperative recognition:** berkaitan dengan bentuk instruksi seperti `اِقْرَأْ`, `أَعِدْ`, `اُنْظُرْ`, `اِسْتَمِعْ`, `اِفْتَحْ`, `أَغْلِقْ`, `قِفْ`, `وَاصِلْ`, `أَجِبْ`, `اِنْتَبِهْ`.
- **K27 — generic negation recognition:** dapat menjadi crosswalk potensial pada `لَا` dan `لَمْ أَفْهَمْ`, tetapi hubungan operasionalnya harus divalidasi sebelum dijadikan item asesmen.

Crosswalk lain tidak boleh diinferensikan hanya dari nomor K.

## 10. Aturan produksi

1. Bahasa Arab Bi'ah harus digunakan dalam aktivitas nyata, bukan menjadi daftar hafalan pasif.
2. Input baru kecil dan kumulatif; ungkapan lama terus digunakan.
3. Terjemahan Indonesia adalah scaffolding dan dikurangi setelah respons otomatis.
4. Mufradat umum tidak boleh menggantikan jalur utama bahasa instruksional.
5. Corpus Bahasa Arab standalone dan paragraf harus diimpor melalui audit eksplisit.
6. Semua turunan ke buku, generator, audio, asesmen, dan RIQA OS harus menunjuk ID master.
7. Perubahan Arab/makna/fungsi dilakukan di master terlebih dahulu, kemudian diturunkan ke produk.

## 11. Antrean konsolidasi berikutnya

- [ ] Audit seluruh `03_BOOKS/BAHASA-ARAB/`.
- [ ] Ekstrak seluruh mufradat dan kalimat unik tanpa duplikasi.
- [ ] Pisahkan BA-for-Tartil, BA-standalone, competency-paragraphs, dan corpus Qur'ani.
- [ ] Tambahkan sumber ayat/surah untuk item Qur'ani.
- [ ] Mapping ke J1–J8 dan M01–M21.
- [ ] Mapping aman ke K01–K65 setelah definisi kompetensi pulih/terverifikasi.
- [ ] Siapkan field audio dan sinkronisasi RIQA OS.
- [ ] Buat statistik jumlah lemma, ungkapan, kalimat, dan cakupan penggunaan.

## 12. Baseline v0.1

Baseline awal terverifikasi yang terkonsolidasi di file ini:
- 18 instruksi;
- 7 respons santri;
- 8 interaksi;
- 9 mufradat lingkungan;
- 2 rangkaian instruksional.

Jumlah ini **bukan** total corpus QURBATA. Ini adalah baseline yang telah ditarik dari master Bi'ah yang berhasil diverifikasi pada konsolidasi awal.
