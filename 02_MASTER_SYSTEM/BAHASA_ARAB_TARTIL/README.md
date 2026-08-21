# QURBATA BAHASA ARAB UNTUK TARTIL

Status: ACTIVE WORKSTREAM
Tanggal pemisahan arsitektur: 2026-08-21
Repository: pesantrenriqa-boop/QURBATA

## Fungsi

Workstream ini khusus untuk Bahasa Arab yang terintegrasi pada setiap pertemuan QURBATA TARTIL.

Unit integrasi:

> 1 halaman/pertemuan QURBATA Tartil = 1 unit Bī'ah 'Arabiyyah.

Bahasa Arab mengikuti aktivitas Tartil, bukan sebaliknya.

## Batas produk

Workstream ini DIBEDAKAN dari:

1. QURBATA Bahasa Arab standalone — buku/program Bahasa Arab khusus untuk guru, trainer, dan peserta Bahasa Arab.
2. Paragraf Bahasa Arab QURBATA — corpus latihan pengembangan kompetensi Bahasa Arab.

Keduanya tidak boleh dicampurkan ke materi Tartil tanpa mapping eksplisit.

## Komponen setiap pertemuan Tartil

1. `TA'BIRAT_SAFFIYYAH` — instruksi guru yang digunakan nyata di kelas.
2. `ISTIJABAH` — respons lisan/tindakan peserta.
3. `MUFRADAT_BIAH` — kosakata yang relevan dengan aktivitas dan lingkungan belajar.
4. `TA'BIR_YAUMI` — ekspresi komunikasi sederhana yang dapat dipakai berulang.
5. `MURAJAAH` — bahasa dari pertemuan sebelumnya yang tetap dipakai.
6. `NEW_INPUT` — input Bahasa Arab baru dalam beban kecil dan bertahap.

## Prinsip progresi

P001 = input awal + penggunaan nyata.
P002 = murojaah P001 + input baru.
P003 = murojaah kumulatif + input baru.
...
P040 = akumulasi Bī'ah 'Arabiyyah Jilid tersebut.

Progres berlanjut lintas Jilid 1–8 dan tidak di-reset pada awal jilid baru.

## Kontrak integrasi

Setiap unit Bahasa Arab wajib memiliki pasangan identitas:

`JILID_ID + PAGE_ID + TARTIL_ACTIVITY_ID`

Contoh:

`J1-P001 -> Bahasa Arab J1-P001`

Tidak boleh ada materi Bahasa Arab yang ditempel ke halaman Tartil tanpa pasangan tersebut.

## Status audit awal

Repository telah memiliki jalur `03_BOOKS/BAHASA-ARAB`, saat audit 2026-08-21 ditemukan materi JILID-3 dengan registry dan folder FROZEN/REVIEW. Materi lama tersebut diperlakukan sebagai corpus existing yang harus diklasifikasikan terlebih dahulu; tidak otomatis dianggap sebagai Bahasa Arab-for-Tartil.

## Urutan pengerjaan

1. Audit corpus existing.
2. Pisahkan BA-for-Tartil vs BA-standalone vs competency-paragraphs.
3. Kunci master vocabulary/instruction registry BA-for-Tartil.
4. Mapping J1 P001–P040.
5. Validasi repetisi, beban input baru, dan keterpakaian nyata di kelas.
6. Lanjut J2–J8.
7. Integrasikan field final ke sumber halaman QURBATA Tartil.
