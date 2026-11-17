# Kebijakan sumber contoh Al-Qur'an — QURBATA Jilid 6

**Status:** Aturan kerja pengisian register (bukan pengesahan akademik).

1. Semua slot contoh tartil berisi potongan ayat Al-Qur'an yang terlacak ke surah, ayat, Source-ID, dan rasm mushaf.
2. **Dilarang** mengambil contoh dari Al-Fatihah (QS 1) atau Juz 'Amma (QS 78–114), termasuk potongan ayatnya.
3. **Dilarang mengulang** potongan ayat yang sudah digunakan di Jilid 1–5. Cek seluruh inventaris/register terdahulu, baik exact match maupun potongan yang tumpang tindih. Jika inventaris belum tersedia, status **PENDING-DEDUP** dan jangan APPROVED.
4. Ayat panjang diperbolehkan sepanjang tidak mengajarkan kompetensi baru di luar progression Jilid 1–6; audit harus melihat seluruh hukum bacaan yang muncul, bukan hanya huruf target.
5. Status CANDIDATE hanya berarti usulan; APPROVED memerlukan tashih teks, kompetensi, deduplikasi, dan reviewer manusia.
6. Preferensi variasi surah dan ayat; hindari pengulangan satu ayat untuk banyak slot kecuali ada tujuan latihan yang jelas.

## Audit perubahan 28 Oktober 2026

- Kandidat P001–P003 yang berasal dari QS 1 atau QS 78–114 dikosongkan kembali.
- Kandidat nonterlarang yang tersisa masih menunggu deduplikasi dengan Jilid 1–5.
- Pemeriksaan otomatis surah terlarang diaktifkan dalam `qj6_slots.py`.
- Pemeriksaan deduplikasi lintas jilid belum otomatis; jangan menganggap register sudah lolos aturan nomor 3.
