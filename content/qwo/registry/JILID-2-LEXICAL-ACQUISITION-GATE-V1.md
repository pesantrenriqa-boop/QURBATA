# JILID 2 — Lexical Acquisition Gate V1

Status: FROZEN

Tujuan aturan ini adalah mencegah huruf baru hanya muncul sebagai dekorasi judul tanpa memperoleh paparan latihan yang cukup.

## Gate wajib

1. Setiap huruf baru yang dinyatakan sebagai `AcquisitionLetters` wajib memiliki minimal **8 objek CURRENT** yang bermakna dan berstatus `ALLOWED,CURATED` pada lexical foundation halaman tersebut.
2. Huruf baru tidak boleh digabung dalam satu halaman apabila salah satu huruf belum memenuhi ambang minimum 8 objek CURRENT.
3. Contoh judul/presentation tidak dihitung sebagai pemenuhan gate latihan.
4. Murojaah tidak dihitung sebagai objek acquisition untuk huruf baru.
5. Jika corpus aman belum cukup karena batas huruf yang telah dipelajari, huruf tersebut **ditunda**, bukan dipaksakan dengan kata tidak bermakna atau dengan membocorkan huruf masa depan.
6. Renderer wajib gagal (`LEXICAL_ACQUISITION_GATE_FAIL`) bila gate tidak terpenuhi.
7. Setelah urutan kompetensi bertambah dan corpus aman mencukupi, huruf yang ditunda dapat dijadwalkan ulang pada halaman berikutnya atau halaman khusus keluarga bentuk.

## Keputusan P006

- `ط` memenuhi gate dan tetap menjadi acquisition P006.
- `ظ` ditunda karena corpus aman pada posisi P006 belum memenuhi ambang minimum.
- P006 kembali menjadi `AcquisitionLetters=ط`.

Aturan ini berlaku untuk halaman Jilid 2 berikutnya sampai direvisi melalui keputusan kurikulum baru.