# Pedagogical Engine Foundation V1 — Complete

Tanggal: 4 Agustus 2026
Branch: `content/qurbata-jilid-1-8-production`
Status: FOUNDATION COMPLETE — PAGE GENERATION LOCKED UNTIL REGENERATION

## Ruang lingkup yang diselesaikan

Fondasi mesin pedagogis V1 dinyatakan lengkap untuk mengendalikan produksi QURBATA Jilid 1–8.

Komponen aktif:

1. Dependency map C0001–C0041.
2. Policy matrix lengkap C0001–C0041.
3. Rule matrix executable untuk pemeriksaan fitur objek.
4. Dependency graph validator.
5. Object-level pedagogical gate.
6. Page-level pedagogical gate.
7. Larangan pengulangan `CanonicalKey` pada halaman dan seri.
8. Kewajiban `SourceRef` Al-Qur'an.
9. Regression tests untuk hamzah, sukun, tanwin, tasydid, dan mad.
10. Pemisahan bab khusus Lafzul Jalalah.

## Urutan keputusan mesin

`COMPETENCY -> DEPENDENCY CHECK -> OBJECT TYPE -> FEATURE WHITELIST -> FEATURE BLACKLIST -> SOURCE CHECK -> DUPLICATE CHECK -> PAGE OUTPUT`

Corpus tidak boleh lagi langsung memilih objek berdasarkan panjang saja.

## Hard gate

Objek ditolak apabila:

- kompetensi prasyarat belum dikuasai;
- huruf belum masuk whitelist;
- harakat belum diizinkan;
- hamzah muncul sebelum bab hamzah;
- mad, tanwin, sukun, atau tasydid muncul sebelum kompetensinya;
- bentuk sambungan tidak sesuai target;
- jenis objek salah;
- panjang objek melampaui policy;
- `SourceRef` kosong;
- `CanonicalKey` pernah dipakai sebagai objek utama.

## Tes regresi

Tes lokal menghasilkan `ALL_TESTS_PASSED` untuk kasus berikut:

- `بَ`, `بِ`, `بُ` diterima pada kompetensi yang tepat;
- `ؤُ` ditolak sebelum bab hamzah;
- `إِ` ditolak sebelum bab hamzah;
- tanwin, sukun, dan tasydid ditolak pada huruf awal;
- `بَا` ditolak sebelum bab mad;
- `هُوَ` tidak diklasifikasikan sebagai mad waw;
- `قُولُوا` tetap dikenali memiliki mad waw.

## Dampak terhadap hasil lama

Semua halaman kandidat yang dibuat sebelum fondasi ini, termasuk Halaman 10, dianggap tidak sah untuk produksi dan wajib diregenerasi melalui Pedagogical Engine V1.

Tidak ada halaman lama yang otomatis dipromosikan menjadi `REVIEWED_PAGE`.

## Definisi 100 persen

Angka 100 persen pada dokumen ini berarti fondasi kontrol mesin V1 telah lengkap: dependency, policy, validator objek, validator halaman, sumber, deduplikasi, dan tes regresi tersedia.

Angka ini tidak berarti isi delapan jilid telah selesai. Produksi halaman dimulai kembali setelah seluruh kandidat melewati gate baru.

## Langkah berikutnya

1. Regenerasi Halaman 1 dan Halaman 10 menggunakan gate baru.
2. Audit hasil terhadap tangga kompetensi.
3. Setelah dua halaman lolos, regenerasi seluruh Jilid 1.
4. Susun contoh layout satu halaman untuk persetujuan visual.
