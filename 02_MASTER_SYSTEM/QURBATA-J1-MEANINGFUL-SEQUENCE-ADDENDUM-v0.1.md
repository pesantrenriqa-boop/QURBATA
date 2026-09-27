# QURBATA JILID 1 — MEANINGFUL SEQUENCE LAYER (MSL)

Status: **ADDENDUM v0.1 — ADDITIVE ONLY / NON-DESTRUCTIVE**

## PRINSIP UTAMA
Addendum ini **tidak mengubah, mengganti, menghapus, atau melonggarkan aturan lama** QURBATA Jilid 1. Semua HARD RULE, TARGET, REVIEW_ALLOWED, EXACT-2/EXACT-3, detached-letter, coverage rotation, future-competency prohibition, dan zero-duplicate yang telah berlaku tetap menjadi otoritas lebih tinggi.

MSL hanya menjadi lapisan preferensi pemilihan contoh setelah seluruh aturan lama terpenuhi.

## DEFINISI
**Meaningful Sequence** = kelompok unit huruf/harakat detached yang urutannya berasal dari kata Arab bermakna yang sah.

Contoh konsep:
- kata sumber: `كَتَبَ`
- tampilan latihan: `كَ تَ بَ`

Tampilan tetap berupa unit huruf tunggal/pisah. MSL **tidak memberi izin** untuk menampilkan bentuk sambung pada fase yang mensyaratkan detached letters.

## URUTAN OTORITAS
Pemilihan setiap kelompok latihan wajib mengikuti urutan berikut:
1. Aturan lama/frozen.
2. TARGET kompetensi halaman.
3. REVIEW_ALLOWED.
4. EXACT-2 / EXACT-3 sesuai struktur halaman.
5. Detached-letter.
6. Future-competency prohibition.
7. Coverage/pemerataan kumulatif.
8. Zero duplicate kelompok.
9. **Global meaningful-source uniqueness.**
10. Meaningful Sequence preference.

Jika kata bermakna bertentangan dengan salah satu aturan 1–8, kata tersebut **ditolak**. Makna tidak boleh mengalahkan kompetensi.

## HARD RULE: TIDAK BOLEH MENGULANG KUMPULAN KATA YANG SAMA
1. Satu kata sumber bermakna hanya boleh digunakan **satu kali sebagai sumber meaningful sequence dalam Jilid 1**, kecuali kelak ada keputusan kurikulum eksplisit yang membekukan pengecualian.
2. Bentuk detached dan bentuk sambung dianggap sumber yang sama. Contoh `كَتَبَ` dan `كَ تَ بَ` adalah satu `source_word_key` yang sama.
3. Perbedaan posisi pada halaman tidak membuatnya menjadi contoh baru.
4. Pengulangan kata sumber pada halaman berbeda tetap dihitung DUPLIKAT.
5. Kata yang sama dengan sekadar perubahan spasi/tampilan tidak boleh digunakan kembali.
6. Setiap meaningful sequence wajib memiliki metadata `source_word_key`, `source_word`, `meaning`, `page`, dan `cell`.
7. Sebelum kata baru diterima, validator harus mengecek registry global Jilid 1.
8. Jika `source_word_key` sudah ada, hasil = `MEANINGFUL_SOURCE_DUPLICATE_FAIL`.

## NORMALISASI SOURCE WORD KEY
Untuk pemeriksaan duplikasi, registry harus menormalkan kata sumber secara konsisten:
- Unicode NFC;
- menghapus spasi pemisah tampilan detached;
- mempertahankan identitas huruf;
- tidak menganggap perubahan layout sebagai kata baru.

Harakat yang berbeda karena kompetensi berbeda harus ditinjau secara kurikulum, tetapi **tidak boleh sengaja dipakai untuk menyamarkan pengulangan kata yang sama**.

## TARGET PROPORSI
MSL adalah preferensi, bukan kuota yang memaksa. Pada halaman tertentu:
- gunakan sebanyak mungkin meaningful sequence yang legal dan belum pernah dipakai;
- slot yang tidak mempunyai kandidat legal tetap diisi latihan fonetik/decoding curated sesuai aturan lama;
- jangan memasukkan huruf/harakat masa depan hanya demi mendapatkan kata bermakna;
- jangan mengorbankan coverage review demi mengejar meaningful sequence.

## REGISTRY WAJIB
Sebelum data P001–P040 dinyatakan final, buat satu registry global:

| source_word_key | source_word | detached_display | meaning | page | cell | legal_target | coverage_ok | status |
|---|---|---|---|---|---:|---|---|---|
| كتب | كَتَبَ | كَ تَ بَ | menulis/telah menulis | TBD | TBD | TBD | TBD | CANDIDATE |

Registry ini adalah satu-satunya sumber pemeriksaan apakah sebuah kata bermakna sudah pernah dipakai.

## QA GATES TAMBAHAN
- `MEANINGFUL_LEGALITY_FAIL`: source word membutuhkan kompetensi yang belum legal.
- `MEANINGFUL_SOURCE_DUPLICATE_FAIL`: source word pernah digunakan sebelumnya di Jilid 1.
- `MEANINGFUL_DISPLAY_JOINED_FAIL`: meaningful sequence ditampilkan sambung pada fase detached.
- `MEANINGFUL_METADATA_MISSING_FAIL`: source word digunakan tanpa metadata registry.

## NON-REGRESSION
Addendum ini dilarang mengubah data latihan yang sudah lolos hanya secara otomatis. Integrasi meaningful sequence dilakukan dengan **substitusi curated satu per satu**, lalu halaman wajib diaudit ulang untuk:
- target presence;
- exact length;
- zero duplicate;
- future competency;
- cumulative coverage;
- meaningful-source uniqueness.

## KEPUTUSAN
**MSL diterima sebagai aturan tambahan. Aturan lama tetap utuh. Pengulangan kumpulan/kata sumber bermakna yang sama di seluruh Jilid 1 dilarang.**
