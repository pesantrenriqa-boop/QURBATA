# QURBATA — SPESIFIKASI BANK KOSAKATA KORPUS AL-QUR'AN 114 SURAH v1.0

**KEBIJAKAN WAJIB — 16 Oktober 2026.** Berlaku untuk inventaris kata/frasa/kalimat Tartil Jilid 1–8. Seluruh 114 surah menjadi **ruang pencarian kandidat**, bukan klaim bahwa seluruh kata sudah diekstrak atau diverifikasi. Jangan mengubah crosswalk Tahfidz FROZEN.

## Prinsip
1. Bangun bank dari **seluruh korpus Al-Qur'an 114 surah/30 juz**; jangan membatasi pencarian pada Juz Amma atau contoh yang sudah pernah digunakan.
2. Setiap unit `WORD` wajib menunjuk **token yang benar-benar muncul** pada ayat tertentu, dengan `surah, ayah, token_index, exact_uthmani, edition, verification`. Bentuk yang dilepaskan dari prefiks/sufiks hanya boleh menjadi analisis morfologi, **bukan** menggantikan token asli dalam buku.
3. Setiap `PHRASE`/`SENTENCE` wajib berupa **rentang token berurutan dalam ayat yang sama**; dilarang menyambung kata dari ayat berlainan menjadi latihan bacaan Tartil.
4. Indekskan atribut grafem dan fonetik: huruf, posisi sambung, harakat, tanwin, sukun, tasydid, alif/ya/waw mad, hamzah, alif kecil, waqaf/wasal, serta tingkat kesulitan.
5. Per kompetensi, lakukan pencarian menyeluruh lalu **pilih contoh bervariasi** menurut bentuk, posisi, surah, dan struktur kata. Jangan mengejar jumlah dengan mengulang token identik.
6. Urutan seleksi: keaslian sumber → kecocokan kompetensi dan prasyarat → ketepatan rasm/harakat → keterbacaan → keberagaman → kemudahan pedagogis.
7. Kartu huruf/suku kata pedagogis harus diberi label peraga; bukan kata Qurani. Dialog Bi'ah buatan guru tetap dipisah dari contoh Tartil.
8. Semua contoh untuk cetak harus ditashih pada mushaf rujukan, termasuk tampilan KFGQPC Uthman Taha; status kandidat tidak sama dengan VERIFIED-QURAN.

## Skema data bank
`id, surah, ayah, token_index, exact_uthmani, normalized_search_form, root_optional, lemma_optional, word_type, grapheme_features, tajwid_features, competencies, prerequisite_competencies, juz, source_edition, source_version, reviewer, verification_status`

`normalized_search_form` hanya untuk pencarian; kolom yang dicetak adalah `exact_uthmani` yang sudah diverifikasi. Jangan merekonstruksi rasm dari teks imlai.

## Skema pemilihan untuk halaman
`jilid, page, competence, source_word_ids[], source_span_ids[], selection_reason, diversity_score, new_vs_review_ratio, qa_status`

Untuk halaman dengan kata utuh: target kerja awal **minimal 10 kandidat berbeda per kompetensi** untuk disaring, bukan kuota wajib 10 kata per halaman. Variasikan surah/juz bila relevan dan tetap perhatikan kompetensi. Materi baru ±60% dan pengulangan ±40% dapat dipakai bila sesuai pedoman jilid, bukan alasan melanggar prasyarat.

## Pipeline produksi
1. Tentukan edisi mushaf Utsmani berlisensi/terotorisasi beserta versi dan provenance data.
2. Impor seluruh ayat dan token **tanpa mengubah teks sumber**, simpan checksum.
3. Ekstrak fitur kompetensi dengan mesin; hasil otomatis hanya `AUTO-CANDIDATE`.
4. Cari seluruh korpus, deduplikasi **untuk pemilihan** tetapi pertahankan seluruh kemunculan token dan lokasinya.
5. Pilih kandidat beragam sesuai kompetensi; hindari dominasi satu surah dan kata berulang.
6. Review guru Tartil, ahli rasm/tajwid dan editor; tandai `VERIFIED-QURAN` hanya setelah tashih.
7. Bangun latihan, kunci, dialog kontekstual dan panel akhlak terpisah; jalankan gate empat inventaris.
8. Audit cetak font dan bekukan versi data terverifikasi.

## Metrik QA yang harus dilaporkan
- cakupan surah yang telah diproses / 114;
- jumlah token korpus yang diimpor (termasuk kemunculan berulang);
- jumlah bentuk kata unik;
- jumlah kandidat dan terverifikasi per kompetensi;
- distribusi kandidat menurut surah/juz;
- tingkat pengulangan kata per halaman/jilid;
- jumlah sumber tanpa bukti ayat/token;
- jumlah contoh yang melanggar prasyarat kompetensi.

## Kondisi saat kebijakan dibuat
**Belum ada bukti di dokumen ini bahwa korpus 114 surah telah diimpor.** Bank J2 terdahulu hanya berisi sampel kandidat. Pekerjaan berikutnya adalah membangun dataset, indeks dan validasi nyata; dilarang mengklaim seluruh korpus sudah terproses.

**Keputusan:** setiap pengayaan berikutnya wajib mencari kandidat dari **seluruh korpus** dan mengutamakan variasi yang sah, bukan memperpanjang daftar contoh dari beberapa surah saja.
