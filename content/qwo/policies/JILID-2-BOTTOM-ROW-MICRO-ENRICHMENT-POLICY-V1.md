# Jilid 2 Bottom-Row Micro-Enrichment Policy V1

Status: ACTIVE_CANDIDATE
Scope: QURBATA Jilid 2

## Purpose
Setiap halaman dapat memakai baris paling bawah sebagai micro-enrichment terjadwal. Micro-enrichment tidak boleh menggeser kompetensi inti membaca, tidak boleh memperkenalkan hukum bacaan yang belum dipelajari, dan tidak dihitung sebagai objek latihan inti.

## Prinsip
1. Materi inti halaman tetap dominan.
2. Bottom row hanya satu kategori per halaman reguler.
3. Materi enrichment harus singkat, visual, dan dapat dibaca/ditunjuk dalam 1-2 menit.
4. Kategori yang mengandung bentuk bacaan baru hanya boleh muncul setelah kompetensi prasyarat aktif.
5. Halaman kumulatif/review boleh memuat 2-3 kategori enrichment yang seluruhnya sudah pernah diperkenalkan sebelumnya.
6. Enrichment tidak boleh menyebabkan LAYOUT_OVERFLOW atau mengurangi ukuran baseline materi inti.
7. Baseline tipografi inti Jilid 2 tetap presentation 52 pt dan practice 39 pt kecuali keputusan governance baru.

## Urutan kategori enrichment
E01 — Nama huruf hijaiyah: اَلِفٌ، بَاءٌ، تَاءٌ ...; fokus nama, bukan materi baca baru.
E02 — Angka Arab/Indic: ٠ ١ ٢ ٣ ٤ ٥ ٦ ٧ ٨ ٩ lalu ١٠ dst.; pengenalan simbol dan nama secara bertahap.
E03 — Nama harakat dan tanda baca yang SUDAH dikuasai: فَتْحَة، كَسْرَة، ضَمَّة، سُكُون ...; tidak mendahului kompetensi inti.
E04 — Bentuk huruf awal–tengah–akhir: satu keluarga huruf yang sudah dipelajari, untuk kesadaran bentuk.
E05 — Huruf mirip/kontras visual: pasangan/kelompok seperti ب ت ث; ج ح خ; س ش; ص ض; ط ظ; ع غ; ف ق sesuai level yang telah aktif.
E06 — Huruf pemutus sambungan: ا د ذ ر ز و; identifikasi posisi dan efek putus sambungan tanpa menambah hukum baru.
E07 — Awailus-suwar/huruf muqatta'ah: hanya sebagai pengenalan visual/identifikasi pada titik yang telah dijadwalkan; cara baca mengikuti kompetensi yang sudah tersedia.
E08 — Tanda mushaf dasar: nomor ayat, tanda akhir ayat, rubu'/hizb/juz/sajdah atau tanda mushaf lain secara bertahap; pengenalan simbol tidak boleh dicampur dengan hukum waqaf sebelum waktunya.
E09 — Tanda waqaf dasar: م، لا، ج، قلى، صلى dan lainnya hanya setelah kompetensi waqaf dijadwalkan; sebelum itu tidak digunakan sebagai materi baca.
E10 — Kosakata Qurani mini: 1-3 kata yang seluruh grafem/harakat/hukum bacaannya berada di bawah atau sama dengan level halaman.
E11 — Potongan Qurani mini: fragmen sangat pendek yang 100% lolos competency leakage gate.
E12 — Makhraj/sifat mikro: satu pengingat artikulasi atau kontras bunyi yang relevan dengan huruf halaman, tanpa teori panjang.

## Distribusi reguler
Kategori diputar, bukan ditumpuk. Urutan default setelah kategori tersedia adalah E01 -> E02 -> E03 -> E04 -> E05 -> E06 -> E07 -> E08 -> E09 -> E10 -> E11 -> E12 lalu mengulang dengan objek baru. Jika kategori belum eligible, lompat ke kategori eligible berikutnya.

## Halaman kumulatif
Halaman dengan fungsi cumulative/review/transfer wajib memiliki blok enrichment kumulatif di bagian bawah bila ruang aman tersedia. Blok dapat memuat maksimal 3 kategori yang sudah diperkenalkan, dengan prioritas:
A. recall simbolik: nama huruf / angka Arab;
B. kesadaran tulisan-mushaf: bentuk huruf / pemutus sambungan / tanda mushaf;
C. transfer Qurani: awailus-suwar / kosakata Qurani / potongan Qurani sesuai gate.
Tidak boleh memasukkan materi enrichment yang belum pernah diperkenalkan pada halaman reguler sebelumnya.

## Governance fields
Setiap halaman baru harus dapat mencatat: ENRICHMENT_CATEGORY, ENRICHMENT_ITEM, ENRICHMENT_PREREQUISITE, ENRICHMENT_STATUS, dan CUMULATIVE_ENRICHMENT bila halaman kumulatif.
