# AUD-QJ7-039 — Audit Prioritas Duplikasi Lintas Halaman

**Tanggal:** 28 Oktober 2026  
**Status:** AUDIT PRIORITAS; belum merupakan tashih atau persetujuan materi cetak  
**Sumber kerja:** register QURBATA Jilid 7, 360 slot; audit metadata Tahap 36–38  
**Master pengendali:** `books/jilid-7/QJ7-MASTER-Struktur-40-Halaman.md`  
**Branch:** `main`

## Tujuan

Mempercepat audit register dengan mengurutkan contoh Qurani yang berulang lintas halaman. Audit ini tidak mengubah teks, rujukan surah/ayat, atau slot sumber. Frekuensi pengulangan dipakai sebagai sinyal pemeriksaan, bukan bukti bahwa kutipan salah.

## Hasil penyaringan

- Cakupan register: 360 slot / 40 halaman.
- Slot dengan frekuensi kutipan tercatat ≥4: 67.
- Prioritas P1: 44 slot.
- Prioritas P2: 23 slot.
- Penggantian otomatis: 0.
- Status teks dan hukum bacaan: tetap memerlukan verifikasi mushaf Utsmani dan tashih.
- Prasyarat Jilid 1–6: belum dapat disahkan karena mapping kompetensi Jilid 6 di registry master masih TBD.

## Temuan utama: pengulangan di P031–P035

Dua kutipan terlihat berulang pada beberapa halaman berturut-turut dengan fokus waqaf–ibtida yang berbeda:

1. `وَمَا تَوْفِيقِي إِلَّا بِاللَّهِ` — Hud 11:88.
2. `وَمَا اللَّهُ بِغَافِلٍ عَمَّا تَعْمَلُونَ` — Al-Baqarah 2:74.

Kutipan tersebut tidak otomatis salah. Namun, karena P031–P035 masing-masing mempunyai fokus berbeda (waqaf–ibtida, jenis waqaf, tanda waqaf, praktik, evaluasi), pengulangan perlu dibuktikan memiliki tujuan pedagogis spesifik. Jika tidak, slot dapat diusulkan untuk penggantian setelah calon alternatif diperiksa.

Contoh lain dengan frekuensi tinggi: `وَاسْتَعِينُوا بِالصَّبْرِ وَالصَّلَاةِ` — Al-Baqarah 2:45, tercatat enam kali pada halaman yang berfokus berbeda. Perlu ditentukan apakah pengulangan itu disengaja untuk makhraj, lahn, dan integrasi atau hanya duplikasi yang belum dikendalikan.

## Protokol keputusan cepat dan aman

Untuk setiap slot prioritas:

1. Cocokkan lafaz dan nomor ayat dengan mushaf Utsmani yang menjadi rujukan.
2. Pastikan kutipan cukup memuat objek kompetensi, tidak sekadar menampilkan kata sasaran.
3. Untuk P031–P035, periksa konteks sebelum dan sesudah titik waqaf serta kelayakan ibtida.
4. Bandingkan dengan semua slot lain dalam Jilid 7 dan cek prasyarat Jilid 1–6 dari master yang disahkan.
5. Tetapkan salah satu status: **PERTAHANKAN (pengulangan disengaja)**, **USUL GANTI (alternatif belum disahkan)**, atau **BLOCKED (teks/konteks belum terverifikasi)**.
6. Jangan memindahkan slot ke status final tanpa Source-ID, bukti tashih, dan catatan keputusan.

## Batasan

Laporan ini adalah antrean prioritas berbasis metadata/frekuensi yang ada di workbook audit. Ini bukan verifikasi mandiri seluruh 360 kutipan terhadap mushaf, bukan validasi ahli tajwid, dan bukan content freeze. Tidak ada kandidat ayat baru yang dikarang atau disahkan dalam tahap ini.

## Langkah berikutnya

Mulai dari P031–P035: audit konteks dan tujuan pedagogis untuk kutipan yang berulang, lalu susun daftar **usulan penggantian** tanpa menerapkannya ke register utama sampai teks, kompetensi, dan sumber terverifikasi.
