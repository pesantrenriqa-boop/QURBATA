# QLO Batch 0001 — Surah Al-Fatihah

**Status:** CANONICAL-ACTIVE  
**Jumlah:** 24 QLO  
**Rentang ID:** QLO-000001 s.d. QLO-000024  
**Sumber:** Surah Al-Fatihah ayat 1–7  
**Ortografi:** `NORMALIZED_ARABIC`

## Tujuan batch

Batch ini menjadi implementasi pertama schema QURBATA Learning Object. Setiap record memuat:

- teks kata;
- rujukan surah dan ayat;
- kompetensi target;
- seluruh kompetensi prasyarat;
- kompetensi kumulatif;
- tingkat kesulitan;
- batas jilid dan halaman;
- prioritas review;
- status sumber dan ortografi.

## Prinsip penting

1. Satu QLO bukan sekadar kosakata, tetapi objek pembelajaran yang mempunyai dependency graph.
2. Kata hanya dapat dipilih generator jika seluruh `RequiredCompetencies` sudah aktif.
3. `CumulativeCompetencies` berisi kompetensi target ditambah seluruh kompetensi sebelumnya yang dibutuhkan.
4. Pengulangan halaman dilakukan dengan memilih QLO lain yang melatih kompetensi lama, bukan mengulang QLO yang sama.
5. QLO dengan unsur lanjutan tetap disimpan, tetapi `AllowedFromJilid` dan `AllowedFromPage` mencegah kemunculan terlalu dini.

## Ringkasan tingkat penggunaan

| Kelompok | Jumlah |
|---|---:|
| Dapat mulai Jilid 3 | 4 |
| Dapat mulai Jilid 4 | 5 |
| Dapat mulai Jilid 5 | 9 |
| Dapat mulai Jilid 6 | 6 |
| Total | 24 |

## Catatan validasi

- `SourceType=QURAN_VERIFIED` berarti bentuk kata dan rujukan ayat sudah ditetapkan sebagai sumber Al-Qur'an.
- Ortografi batch memakai bentuk Arab ternormalisasi untuk kebutuhan metadata dan pencarian.
- Bentuk Utsmani final untuk cetak akan disimpan dalam field terpisah ketika pipeline mushaf Utsmani diaktifkan.
- Penetapan kode kompetensi masih tunduk pada audit akhir QCF; ID QLO tidak boleh berubah meskipun tag kompetensi direvisi.

## File data

`content/qlo/QLO-BATCH-0001-AL-FATIHAH.csv`
