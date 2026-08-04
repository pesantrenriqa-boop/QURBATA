# QCI Validation Rules V1

## Tujuan
Menetapkan pemeriksaan wajib sebelum data kompetensi QCI digunakan oleh QWO, QPO, QAO, QLO, atau generator.

## 1. Validasi Identitas
- `CompetencyID` wajib unik.
- Format ID: `QCI-{DIMENSION}-{NNNN}`.
- ID yang sudah diterbitkan tidak boleh diubah atau digunakan ulang.
- `Code` wajib unik dan mudah dibaca manusia.

## 2. Validasi Dependency
- Semua ID pada `Requires` wajib tersedia di MASTER QCI.
- Dependency melingkar dilarang.
- Kompetensi tidak boleh mensyaratkan dirinya sendiri.
- Prasyarat harus lebih mendasar secara pedagogis daripada kompetensi target.
- Perubahan dependency wajib menaikkan versi definisi.

## 3. Validasi Pedagogis
Setiap kompetensi ACTIVE wajib mempunyai:
- definisi yang tunggal dan tidak tumpang tindih;
- contoh positif;
- batasan atau non-contoh;
- indikator Recognition;
- indikator Reading;
- indikator Fluency;
- indikator Retention;
- tingkat kesulitan dasar;
- prioritas murojaah.

## 4. Validasi Granularitas
Kompetensi harus dipecah apabila:
- membutuhkan prasyarat yang berbeda;
- memiliki indikator lulus yang berbeda;
- kesalahannya memerlukan remedial yang berbeda;
- generator perlu mengaktifkannya pada waktu yang berbeda.

Kompetensi boleh digabung apabila perbedaannya hanya berupa variasi contoh dan tidak mengubah indikator penguasaan.

## 5. Validasi Mapping Kurikulum
- QCI tidak menyimpan jilid sebagai identitas permanen.
- Pemetaan QCI ke jilid, level, halaman, dan produk disimpan terpisah.
- Satu kompetensi dapat muncul pada lebih dari satu produk.
- Kompetensi baru harus memiliki porsi materi baru dan porsi murojaah yang ditentukan pada QLO.

## 6. Validasi Status
Status yang diperbolehkan:
- `DRAFT`: belum boleh digunakan generator produksi.
- `REVIEW`: menunggu pemeriksaan akademik/pedagogis.
- `ACTIVE`: boleh digunakan.
- `HOLD`: ditunda karena urutan atau bukti belum cukup.
- `RETIRED`: tidak digunakan untuk konten baru, tetapi dipertahankan untuk data lama.

## 7. Validasi Integrasi QWO
Sebuah QWO hanya boleh ACTIVE jika:
- seluruh `RequiredCompetencies` valid;
- seluruh `TargetCompetencies` valid;
- tidak ada kompetensi HOLD/RETIRED tanpa alasan kompatibilitas;
- level penggunaan tidak lebih rendah daripada dependency tertinggi;
- metadata visual, fonologis, dan bentuk sambung selaras dengan QCI.

## 8. Validasi Generator
Generator wajib menolak kandidat bila:
- mengandung kompetensi di luar whitelist level;
- dependency belum dikuasai;
- porsi materi baru melebihi batas QLO;
- variasi visual tidak seimbang;
- review kompetensi kritis tidak terpenuhi;
- kata/frasa berulang tanpa tujuan pedagogis.

## 9. Aturan Penguasaan
Status pembelajar untuk setiap kompetensi:
- `NOT_INTRODUCED`
- `INTRODUCED`
- `PRACTICING`
- `MASTERED`
- `RETENTION_RISK`
- `REMEDIAL`

Perpindahan ke `MASTERED` harus berdasarkan bukti performa, bukan kehadiran atau selesainya halaman.

## 10. Definition of Valid
Satu kompetensi dinyatakan valid apabila:
1. ID dan kode unik;
2. definisi tidak ambigu;
3. dependency sah dan bebas siklus;
4. indikator penguasaan tersedia;
5. status dan versi tersedia;
6. dapat dipetakan ke objek latihan;
7. dapat diuji;
8. dapat diremediasi;
9. dapat dipertahankan melalui murojaah.

## Pemeriksaan Awal Seed V1
Seed awal QCI masih berstatus fondasi. Pekerjaan berikutnya:
- menambah seluruh keluarga visual huruf;
- memecah kompetensi bentuk huruf per keluarga dan posisi;
- menyusun indikator penguasaan rinci;
- membuat mapping awal Jilid 1–8;
- menghubungkan MASTER_QWO Batch 0003 ke ID QCI;
- membuat validator otomatis untuk format CSV/JSON.
