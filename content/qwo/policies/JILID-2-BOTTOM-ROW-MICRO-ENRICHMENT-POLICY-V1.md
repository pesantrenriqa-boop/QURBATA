# Jilid 2 Bottom-Row Micro-Enrichment Policy V1

Status: ACTIVE_CANDIDATE
Scope: QURBATA Jilid 2

## Purpose
Setiap halaman dapat memakai baris paling bawah sebagai micro-enrichment terjadwal. Micro-enrichment tidak boleh menggeser kompetensi inti membaca, tidak boleh memperkenalkan hukum bacaan yang belum dipelajari, dan tidak dihitung sebagai objek latihan inti.

## Prinsip
1. Materi inti halaman tetap dominan.
2. Bottom row hanya satu kategori utama per halaman reguler.
3. Materi enrichment harus singkat, visual, dan dapat dibaca/ditunjuk dalam 1-2 menit.
4. Kategori yang mengandung bentuk bacaan baru hanya boleh muncul setelah kompetensi prasyarat aktif.
5. Halaman kumulatif/review boleh memuat 2-3 kategori enrichment yang seluruhnya sudah pernah diperkenalkan sebelumnya.
6. Enrichment tidak boleh menyebabkan LAYOUT_OVERFLOW atau mengurangi ukuran baseline materi inti.
7. Baseline tipografi inti Jilid 2 tetap presentation 52 pt dan practice 39 pt kecuali keputusan governance baru.
8. Materi mikro TIDAK wajib berganti pada setiap halaman. Satu kategori/item boleh dipertahankan lintas beberapa halaman sampai tujuan pengenalan dan penguatan tercapai.
9. Perpindahan ke materi mikro berikutnya dilakukan berdasarkan ketuntasan blok, bukan nomor halaman.
10. Pada halaman akuisisi huruf baru, bottom row boleh tetap memakai materi mikro dari blok sebelumnya agar beban kognitif tidak bertambah terlalu cepat.

## Urutan kategori enrichment
E01 — Nama huruf hijaiyah: kategori referensi; penggunaan tulisan nama huruf Arab pada halaman produksi dinonaktifkan kecuali ada keputusan khusus.
E02 — Angka Arab/Indic: ٠ ١ ٢ ٣ ٤ ٥ ٦ ٧ ٨ ٩ lalu ١٠ dst.; pengenalan simbol secara bertahap.
E03 — Nama harakat dan tanda baca yang SUDAH dikuasai: hanya setelah tanda tersebut aktif pada kompetensi inti.
E04 — Bentuk huruf awal–tengah–akhir: satu keluarga huruf yang sudah dipelajari, untuk kesadaran bentuk.
E05 — Huruf mirip/kontras visual: pasangan/kelompok seperti ب ت ث; ج ح خ; س ش; ص ض; ط ظ; ع غ; ف ق sesuai level yang telah aktif.
E06 — Huruf pemutus sambungan: ا د ذ ر ز و; identifikasi posisi dan efek putus sambungan tanpa menambah hukum baru.
E07 — Awailus-suwar/huruf muqatta'ah: hanya sebagai pengenalan visual/identifikasi pada titik yang telah dijadwalkan; cara baca mengikuti kompetensi yang sudah tersedia.
E08 — Tanda mushaf dasar: nomor ayat, tanda akhir ayat, rubu'/hizb/juz/sajdah atau tanda mushaf lain secara bertahap; pengenalan simbol tidak boleh dicampur dengan hukum waqaf sebelum waktunya.
E09 — Tanda waqaf dasar: م، لا، ج، قلى، صلى dan lainnya hanya setelah kompetensi waqaf dijadwalkan; sebelum itu tidak digunakan sebagai materi baca.
E10 — Kosakata Qurani mini: 1-3 kata yang seluruh grafem/harakat/hukum bacaannya berada di bawah atau sama dengan level halaman.
E11 — Potongan Qurani mini: fragmen sangat pendek yang 100% lolos competency leakage gate.
E12 — Makhraj/sifat mikro: satu pengingat artikulasi atau kontras bunyi yang relevan dengan huruf halaman, tanpa teori panjang.

## Distribusi berbasis blok
Kategori enrichment tidak diputar setiap halaman. Satu blok memakai satu kategori/item sampai cukup dikenali dan dikuatkan. Urutan default kategori setelah blok sebelumnya dinyatakan tuntas adalah E02 -> E04 -> E05 -> E06 -> E07 -> E08 -> E09 -> E10 -> E11 -> E12. E01 tidak dipakai pada produksi normal. Jika kategori berikutnya belum eligible, kategori aktif dipertahankan atau dilompati ke kategori eligible berikutnya.

Contoh implementasi:
- Blok A: angka Arab ٠–٩ dapat dipertahankan pada beberapa halaman berturut-turut.
- Blok B: setelah angka dasar tuntas, pindah ke bentuk huruf awal–tengah–akhir dan pertahankan sampai keluarga huruf terkait cukup kuat.
- Blok C: berikutnya dapat masuk pemutus sambungan, awailus-suwar, tanda mushaf, dan seterusnya sesuai prasyarat.

## Halaman kumulatif
Halaman dengan fungsi cumulative/review/transfer wajib memiliki blok enrichment kumulatif di bagian bawah bila ruang aman tersedia. Blok dapat memuat maksimal 3 kategori yang sudah diperkenalkan, tetapi tidak wajib menambah kategori baru. Prioritas:
A. recall simbolik: angka Arab;
B. kesadaran tulisan-mushaf: bentuk huruf / pemutus sambungan / tanda mushaf;
C. transfer Qurani: awailus-suwar / kosakata Qurani / potongan Qurani sesuai gate.
Tidak boleh memasukkan materi enrichment yang belum pernah diperkenalkan pada halaman reguler sebelumnya.

## Governance fields
Setiap halaman baru harus dapat mencatat: ENRICHMENT_CATEGORY, ENRICHMENT_ITEM, ENRICHMENT_BLOCK_ID, ENRICHMENT_PREREQUISITE, ENRICHMENT_STATUS, dan CUMULATIVE_ENRICHMENT bila halaman kumulatif.
