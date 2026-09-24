# AUDIT CORPUS BAHASA ARAB QURBATA — 03_BOOKS/BAHASA-ARAB

**Versi:** v0.1  
**Tanggal:** 2026-09-24  
**Scope repo yang ditemukan:** `03_BOOKS/BAHASA-ARAB/JILID-3`

## 1. Hasil inventaris

Pada saat audit, folder `03_BOOKS/BAHASA-ARAB/` hanya memuat **JILID-3**.

Registry Jilid 3 mengamankan:
- P001–P012 = 12 halaman/unit;
- 5 paragraf per unit;
- total **60 unit paragraf**;
- P001–P003 = FROZEN;
- P004–P011 = REVIEWED/RECOVERED;
- P012 = REVIEW COMPLETE, belum canonical FROZEN.

## 2. Kompetensi/ungkapan inti P001–P012

| Page | Ungkapan/kompetensi inti | Status |
|---|---|---|
| P001 | مَاذَا تَقْرَأُ؟ | FROZEN |
| P002 | أَقْرَأُ الْقُرْآنَ | FROZEN |
| P003 | اِقْرَأْ مِنْ هُنَا | FROZEN |
| P004 | اِقْرَأْ إِلَى هُنَا | REVIEWED/RECOVERED |
| P005 | penguatan kumulatif P001–P004 | REVIEWED/RECOVERED |
| P006 | latihan kumulatif P001–P004 | REVIEWED/RECOVERED |
| P007 | دَوْرُ مَنْ؟ | REVIEWED/RECOVERED |
| P008 | دَوْرِي | REVIEWED/RECOVERED |
| P009 | الْآنَ دَوْرُكَ | REVIEWED/RECOVERED |
| P010 | اِقْرَأْ بَعْدَ صَدِيقِكَ | REVIEWED/RECOVERED |
| P011 | اِسْمَعْ إِلَى صَدِيقِكَ | REVIEWED/RECOVERED |
| P012 | latihan komunikatif kumulatif; tanpa kompetensi baru | REVIEW COMPLETE |

## 3. Ungkapan tambahan yang terverifikasi di corpus

Corpus paragraf juga memuat variasi/ekspresi yang berguna untuk bank komunikasi:
- أَقْرَأُ مِنْ هُنَا إِلَى هُنَا
- مِنْ أَيْنَ أَبْدَأُ؟
- دَوْرُ خَالِدٍ
- دَوْرُكَ
- اِقْرَئِي مِنْ هُنَا
- اِقْرَئِي إِلَى هُنَا
- اِسْتَمِعْ إِلَى قِرَاءَةِ صَدِيقِكَ
- أَسْمَعُ إِلَى قِرَاءَةِ صَدِيقِي
- اِسْمَعْ إِلَى قِرَاءَتِي، ثُمَّ اِقْرَأْ بَعْدِي

## 4. Mufradat/lemma pedagogis yang jelas berulang

Daftar ini adalah lemma penting yang terverifikasi secara manual dari corpus inti, **bukan klaim daftar seluruh token unik 60 paragraf**:

الْقُرْآنُ، مُصْحَفٌ، كِتَابٌ، قَلَمٌ، صَفْحَةٌ، آيَةٌ، سُورَةٌ، قِرَاءَةٌ، مُرَاجَعَةٌ، دَرْسٌ، فَصْلٌ، مَسْجِدٌ، مُعَلِّمٌ، طَالِبٌ، صَدِيقٌ، زَمِيلٌ، مَجْمُوعَةٌ، حَلْقَةٌ، مَقْطَعٌ، سَطْرٌ، مَكَانٌ، مَوْضِعٌ، دَوْرٌ، بَعْدَ، قَبْلَ، أَمَامَ، إِلَى، مِنْ، هُنَا، الْآنَ.

## 5. Klasifikasi arsitektur

- **BA-for-Tartil:** master instruksional di `02_MASTER_SYSTEM/BAHASA_ARAB_TARTIL/`.
- **BA-standalone / competency paragraphs:** corpus Jilid 3 P001–P012 di `03_BOOKS/BAHASA-ARAB/`.
- **Corpus Qur'ani:** belum boleh disamakan dengan paragraf Jilid 3; perlu pipeline audit ayat/lemma tersendiri.
- **Tangga kompetensi K01–K65:** masih recovery; hanya definisi KNOWN yang boleh dicrosswalk.

## 6. Temuan penting

1. Corpus Jilid 3 sebenarnya sudah kaya dan komunikatif; bukan hanya daftar mufradat.
2. Ada kesinambungan fungsi: pertanyaan → jawaban → batas awal/akhir bacaan → giliran → mendengar teman.
3. Corpus Jilid 3 dapat menjadi sumber pengayaan Bi'ah, tetapi tidak boleh otomatis dipindah ke panel Tartil karena governance memisahkan BA-for-Tartil dan BA-standalone.
4. Status sumber harus dipertahankan: FROZEN tidak boleh disamakan dengan REVIEW/RECOVERED.
5. Untuk RIQA OS, ungkapan inti dapat diberi ID stabil dan diturunkan ke audio, latihan, dialog, serta log penggunaan.

## 7. Gate lanjutan

Audit berikutnya harus:
- melakukan ekstraksi token/lemma otomatis dari 60 paragraf bila seluruh file canonical/review telah dinormalisasi;
- menjaga harakat dan variasi morfologis tanpa menyamakan bentuk secara sembrono;
- menambahkan terjemah, fungsi, source page, status sumber, dan frekuensi;
- memisahkan lemma, surface form, phrase, sentence, dan paragraph;
- tidak memberi label “Qur'ani” kecuali ada bukti ayat/corpus Al-Qur'an.
