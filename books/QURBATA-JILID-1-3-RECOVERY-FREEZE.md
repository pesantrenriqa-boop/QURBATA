# QURBATA Jilid 1–3 — Recovery Freeze

**Kode:** FREEZE-QJ123-REC-001  
**Status:** FROZEN RECOVERY BASELINE  
**Tanggal:** 1 Agustus 2026  
**Pemilik Akademik:** Aris Liswanto  
**Repositori:** `pesantrenriqa-boop/QURBATA`  
**Cabang kerja resmi:** `main`

## 1. Tujuan Freeze

Dokumen ini mengunci hasil penemuan dan pengembalian sumber contoh materi QURBATA Jilid 1–3 agar tidak hilang, tidak tertimpa tanpa jejak, dan tidak dipisahkan dari sistem proyek QURBATA.

Freeze ini adalah **freeze sumber recovery**, bukan klaim bahwa seluruh materi telah disahkan secara akademik, siap pilot, atau siap cetak.

## 2. Sumber Tunggal Proyek

Lokasi produksi dan integrasi resmi:

- `books/jilid-1/`
- `books/jilid-2/`
- `books/jilid-3/`
- `books/RECOVERY-CONSOLIDATION-INDEX-JILID-1-3.md`
- `books/jilid-1/RECOVERY-SOURCES.md`
- `books/jilid-2/RECOVERY-SOURCES.md`
- `books/jilid-3/RECOVERY-SOURCES.md`

Folder lama, batch, staging, dan recovery tetap dipertahankan sebagai bukti asal, tetapi tidak boleh menjadi sumber produksi langsung setelah halaman kanonik tersedia.

## 3. Baseline Jilid 1

- Struktur resmi: 40 halaman.
- Lokasi kanonik: `books/jilid-1/pages/QJ1-P001.md` sampai `QJ1-P040.md`.
- Master struktur: `books/jilid-1/QJ1-MASTER-Struktur-40-Halaman.md`.
- Commit master sampai P040: `c820ca4c0504185bf5e63d7765089fbd7c4b4e2b`.
- P001 telah dicocokkan dengan sumber recovery `03_BOOKS/JILID-1/PAGE-001.md`.
- P002 dan P010 telah memiliki kandidat sumber terverifikasi dengan gate terbuka.
- P003–P009 serta halaman akuisisi lain yang memiliki versi pemerataan dan versi 60:40 wajib mempertahankan kedua garis sumber sampai kebijakan distribusi final diputuskan.
- Halaman hafalan, Bahasa Arab, akhlak, dan evaluasi tidak boleh dipaksa mengikuti rumus halaman latihan baca.

## 4. Baseline Jilid 2

- Struktur resmi: 40 halaman.
- Master: `books/jilid-2/QJ2-MASTER-Struktur-40-Halaman.md`.
- Lokasi kanonik yang sudah ada tetap berada pada `books/jilid-2/pages/`.
- Contoh nyata telah ditemukan pada halaman kanonik. Contoh QJ2-P001 antara lain:
  - `كَتَبَ`
  - `سَأَلَ`
  - `جَلَسَ`
  - `جَذَبَ`
  - `دَخَلَ`
  - `خَرَجَ`
  - `نَزَلَ`
  - `زَرَعَ`
  - `دَرَسَ`
  - `شَرَحَ`
  - `ذَكَرَ`
  - `صَدَقَ`
  - `رَزَقَ`
  - `شَكَرَ`
  - `طَرَكَ`
  - `صَبَرَ`
  - `طَلَبَ`
  - `عَمِلَ`
  - `فَتَحَ`
- Baseline cakupan sumber 40/40 dicatat pada commit `67a42c40d796cbdcead4e98f5d03da370ac22406`.
- Status sumber pada baseline tersebut: 20 `COMPLETE-DRAFT` dan 20 `STAGED-BLOCKED`.
- Versi lama P001–P015 yang dinyatakan `SUPERSEDED` tidak boleh menggantikan baseline terbaru.

## 5. Baseline Jilid 3

Sumber lama Jilid 3 ditemukan dalam empat batch dan wajib dipertahankan:

| Rentang | Commit sumber |
|---|---|
| P001–P010 | `3c47a20fb8bb2f9688f4f1521c1068db53274a7c` |
| P011–P020 | `aadd8918ba865a2a4338fdfdf736ceb154b95173` |
| P021–P030 | `05dfd094584c39e1ef09cee181d75516f52c63a8` |
| P031–P040 | `fb0a15ddf60239d99aa299dc40ce85a4a531c997` |
| P006–P010 versi lanjutan | `f9f9677a6a5388afa740158b969520dc61fbb7a0` |
| Master struktur | `e2df1c7aeca82285b23df704697c48178445f98d` |

Contoh yang telah ditemukan dalam batch Jilid 3 meliputi:

- `كَتَبَ`
- `ذَهَبَ`
- `جَلَسَ`
- `عَلِمَ`
- `كِتَابٌ`
- `عِلْمٌ`
- `يَعْلَمُ`
- `عَالِمٌ`
- `يَكْتُبُ`
- `يَسْمَعُ`
- `يَدْخُلُ`
- `قَالَ`
- `فِيهِ`
- `نُورٌ`
- `مُؤْمِنُونَ`
- `يَعْلَمُونَ`
- `يَعْمَلُونَ`
- `كَانَ`
- `مَالِكِ`
- `هُدًى لِلْمُتَّقِينَ`
- `لَا رَيْبَ`
- `اللَّهُ`
- `رَبِّي`
- `الْحَمْدُ`
- `رَبِّ الْعَالَمِينَ`
- `مَالِكِ يَوْمِ الدِّينِ`
- `مِنَ اللَّهِ`
- `مِنْ عَذَابٍ`
- `مِنْ فَضْلِ`
- `وَاللَّهُ عَلِيمٌ`

Contoh tersebut dibekukan sebagai **data recovery yang ditemukan**. Penempatannya dalam tangga Jilid 3 tetap harus mengikuti keputusan progression terbaru; contoh yang mengandung tasydid atau materi di atas whitelist tidak otomatis menjadi materi cetak halaman asalnya.

Commit `4c61a3dcb9390225308b031fe9944fac99f6db2d` dan versi yang dinyatakan invalid/frozen hanya dipertahankan sebagai bukti sejarah, bukan sumber final.

## 6. Aturan Keamanan Data

1. Tidak boleh menghapus file contoh, batch, staging, atau recovery sebelum isi dan asalnya tercatat pada register.
2. Tidak boleh menimpa satu halaman kanonik tanpa mencatat commit sumber, alasan perubahan, dan versi yang digantikan.
3. Jika dua versi sama-sama memuat contoh penting, keduanya disimpan sampai keputusan akademik final.
4. Semua produk turunan—PDF, slide, flashcard, worksheet, audio, aplikasi, dan RIQA OS—wajib mengambil isi dari jalur kanonik proyek.
5. Materi recovery tidak boleh diklaim sebagai ayat/hadis tanpa Source-ID dan pemeriksaan teks.
6. Freeze tidak menghapus gate ahli, editorial, asesmen, safeguarding, pilot, Evidence-ID, atau Decision-ID.

## 7. Status Freeze

| Jilid | Status keamanan sumber | Status akademik |
|---|---|---|
| Jilid 1 | FOUND / REGISTERED / CANONICAL PATH EXISTS | Masih terdapat gate dan konflik versi |
| Jilid 2 | SOURCE-COMPLETE 40/40 / PARTLY CANONICAL | 20 complete-draft + 20 staged-blocked |
| Jilid 3 | FOUR SOURCE BATCHES FOUND / COMMIT-LOCKED | Perlu migrasi per halaman dan realignment progression |

## 8. Keputusan

Mulai freeze ini:

- data contoh Jilid 1–3 dinyatakan **ditemukan dan diamankan secara sumber**;
- commit sumber yang tercantum tidak boleh diabaikan atau dihapus dari jejak recovery;
- struktur `books/jilid-1`, `books/jilid-2`, dan `books/jilid-3` adalah jalur integrasi resmi seluruh proyek QURBATA;
- revisi selanjutnya dilakukan sebagai perubahan terkontrol di atas baseline ini, bukan dengan membuat proyek atau sumber baru yang terpisah.

**FREEZE-QJ123-REC-001: BERLAKU SEBAGAI BASELINE RECOVERY AMAN.**
