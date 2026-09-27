# QURBATA — COMPETENCY AUTHORING STANDARD v1.1

**Status:** FROZEN  
**Tanggal freeze:** 2026-09-27  
**Supersedes:** v1.0 untuk standar kuantitas evidence; prinsip lain v1.0 tetap berlaku.  
**Cakupan:** Tangga Kompetensi Bahasa Arab Qurani QURBATA K01–K65.

## Perubahan utama v1.1 — Evidence Density
Tujuan QURBATA adalah membangun kepekaan pola Qurani pada pemula. Karena itu bank evidence harus cukup kaya agar peserta dapat melihat pola berulang, membandingkan variasi, mencoba, lalu membuktikan kemampuan pada contoh baru tanpa bergantung pada arti.

### Target evidence per kompetensi
- **K01–K10 (fondasi/pengenalan): target 40–50 evidence Qurani terverifikasi per kompetensi.**
- **K11–K65: minimal 30 evidence Qurani terverifikasi per kompetensi**, dan dapat dinaikkan menjadi 40–50 bila target membutuhkan variasi lebih besar.
- Angka tersebut adalah ukuran **bank repo**, bukan jumlah yang harus dicetak sekaligus di buku.

### Distribusi pedagogis yang disarankan
Dari bank yang tersedia, evidence dipisahkan berdasarkan fungsi agar tidak bocor antara pengajaran dan transfer:
- **LIHAT:** 12–15 evidence yang sangat jelas dan mudah;
- **TEMUKAN/CIRI MUDAH:** 8–10 evidence untuk perbandingan dan pencarian pola;
- **COBA:** 8–10 evidence untuk latihan terbimbing;
- **BUKTIKAN:** 5–8 evidence baru yang belum dipakai pada paparan/latihan utama;
- **RESERVE:** sisanya untuk RIQA OS, remedial, pengayaan, ujian alternatif, dan edisi berikutnya.

Distribusi adalah pedoman, bukan kuota mekanis. Satu evidence boleh dipakai pada LIHAT dan TEMUKAN bila pedagogis, tetapi evidence BUKTIKAN harus dijaga sebagai unseen evidence.

## Diversity Rule
Penambahan evidence tidak boleh sekadar menggandakan kata yang sama. Bank harus mengusahakan variasi:
- surah dan ayat;
- bentuk kata;
- lingkungan teks;
- tingkat kesulitan;
- kosakata;
- fenomena visual/struktural yang tetap berada dalam boundary kompetensi.

Pengulangan diperbolehkan jika disengaja sebagai **recycle**, tetapi harus diberi metadata recycle dan tidak dihitung sebagai keragaman baru.

## Beginner Rule
Untuk K01–K10, evidence harus mendukung pola:

**LIHAT → TEMUKAN → CIRI MUDAH → PAHAMI → COBA → BUKTIKAN**.

Peserta tidak diwajibkan mengetahui arti seluruh kata/ayat untuk menemukan target visual atau struktural. Terjemah berfungsi membantu makna dan vocabulary, bukan menjadi syarat pattern recognition.

## Evidence Metadata
Setiap evidence minimal menyimpan:
- ID unik;
- teks/token Qurani terverifikasi;
- surah dan ayat;
- target span;
- makna ringkas bila diperlukan;
- tingkat kesulitan;
- fungsi pedagogis (`lihat`, `temukan`, `coba`, `buktikan`, `reserve`);
- status verifikasi;
- recycle/source history bila relevan.

## Production Gate tambahan
Kompetensi K01–K10 belum boleh dinyatakan **CONTENT BANK COMPLETE** jika evidence terverifikasi belum mencapai minimal 40 item, kecuali ada alasan linguistik terdokumentasi bahwa target tidak memiliki cukup evidence Qurani yang sah.

## Ketentuan buku
Buku siswa tidak harus memuat seluruh bank. Buku memilih subset terbaik agar halaman tetap ringan. Repo adalah sumber kaya; PDF adalah seleksi pedagogis.

## Ketentuan lain
Semua ketentuan `COMPETENCY-AUTHORING-STANDARD-v1.0` tentang backbone K01–K65, korpus inti Qurani, dua jalur Qurani/Bi'ah, asesmen, vocabulary governance, struktur data, dan production gate tetap berlaku sepanjang tidak bertentangan dengan v1.1 ini.

## Freeze policy
Baseline **v1.1 FROZEN**. Perubahan target evidence atau prinsip pemisahan unseen evidence harus dibuat melalui versi standar berikutnya.