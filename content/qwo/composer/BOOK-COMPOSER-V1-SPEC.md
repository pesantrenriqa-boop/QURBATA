# QURBATA Book Composer V1

Tanggal: 4 Agustus 2026
Status: LAUNCH-FOCUSED

## Tujuan

Menyusun isi Jilid 1–8 berdasarkan urutan kompetensi resmi, bukan berdasarkan pembagian kandidat secara manual.

## Input

1. `QURBATA-COMPETENCY-DEPENDENCY-MAP-V1.csv`
2. QWO kandidat yang telah memiliki label kompetensi
3. Corpus occurrence Al-Qur'an
4. Template 40 halaman per jilid
5. Daftar objek yang sudah dikonsumsi

## Prinsip komposisi

1. Kompetensi mengendalikan pemilihan objek.
2. Objek utama tidak diulang di seluruh seri.
3. Kompetensi lama diulang menggunakan objek Al-Qur'an yang berbeda.
4. Materi baru dan murojaah dipisahkan secara eksplisit.
5. Lafzul Jalalah memiliki bab khusus dan tidak disisipkan sebagai materi baru sebelum bab tersebut.
6. Jilid 1–2 dominan kata.
7. Jilid 3 mulai frasa.
8. Jilid 4–5 dominan potongan ayat sesuai kompetensi.
9. Jilid 6–8 meningkat menuju ayat utuh panjang.
10. Panjang objek mengikuti kesiapan kompetensi, bukan nomor jilid semata.

## Bentuk objek

- `WORD`: kata Al-Qur'an
- `PHRASE`: dua sampai empat kata berurutan dari ayat yang sama
- `AYAH_FRAGMENT`: potongan ayat berurutan
- `FULL_AYAH`: ayat utuh

## Alur pemilihan

1. Baca kompetensi target halaman.
2. Pastikan seluruh prerequisite telah ditempatkan sebelumnya.
3. Tentukan bentuk objek yang diperbolehkan.
4. Cari seluruh kandidat dari corpus.
5. Tolak objek utama yang sudah `CONSUMED_PRIMARY`.
6. Tolak objek yang mengandung kompetensi di luar whitelist halaman.
7. Beri skor kesesuaian kompetensi, keterbacaan, variasi huruf, dan keragaman sumber.
8. Pilih objek terbaik.
9. Tandai objek utama sebagai `CONSUMED_PRIMARY`.
10. Simpan alasan pemilihan dan kandidat pengganti.

## Struktur halaman V1

Setiap halaman memiliki:

- `PageID`
- `VolumeNumber`
- `PageNumber`
- `NewCompetencyIDs`
- `ReviewCompetencyIDs`
- `AllowedObjectTypes`
- `PrimaryObjects`
- `ReviewObjects`
- `SourceRefs`
- `RejectedCandidateRefs`
- `ValidationStatus`

## Gate kelulusan halaman

Sebuah halaman hanya dapat berstatus `READY_FOR_LAYOUT` jika:

- seluruh objek berasal dari Al-Qur'an;
- seluruh referensi surah dan ayat tersedia;
- tidak ada objek utama berulang;
- tidak ada kompetensi melompat;
- materi Lafzul Jalalah mengikuti bab khusus;
- panjang dan bentuk objek sesuai whitelist;
- rasio materi baru dan murojaah sesuai rancangan jilid;
- lolos audit pedagogis.

## Batas V1

Composer V1 tidak membuat desain grafis, tafsir, terjemah, audio, atau modul tambahan. Outputnya hanya susunan isi buku yang siap dipindahkan ke layout.
