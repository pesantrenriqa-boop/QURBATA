# QWO Competency Labeling Rules V1

Tanggal: 4 Agustus 2026
Status: ACTIVE FOR V1

## Tujuan

Memberi label kompetensi pada 2.500 kandidat QWO berdasarkan fitur teks Al-Qur'an. Kompetensi menentukan kelayakan objek; jilid bukan label utama.

## Prinsip wajib

1. Semua objek berasal dari corpus Al-Qur'an terverifikasi.
2. Satu objek memiliki satu `PrimaryCompetencyID` dan dapat memiliki banyak `SecondaryCompetencyIDs`.
3. Kompetensi utama adalah kompetensi paling akhir dalam dependency yang benar-benar diuji oleh objek.
4. Kompetensi prasyarat dicatat sebagai kompetensi sekunder, bukan diulang sebagai materi baru.
5. Objek yang sama tidak boleh dipakai dua kali sebagai objek utama di seri Jilid 1–8.
6. Kompetensi boleh diulang melalui objek Al-Qur'an yang berbeda.
7. Lafzul Jalalah hanya boleh menjadi materi utama pada C0030–C0032.
8. Setelah C0032 dikuasai, Lafzul Jalalah boleh muncul sebagai bagian objek integratif.
9. QWO hanya mencakup kata. Frasa dan ayat dibuat dari occurrence corpus pada tahap komposisi.
10. Semua hasil otomatis berstatus `CANDIDATE` sampai audit pedagogis.

## Urutan keputusan label

1. Validasi `SourceRef` dan `OccurrenceID`.
2. Baca fitur aktual token Utsmani.
3. Tentukan semua kompetensi yang muncul.
4. Hapus kompetensi yang belum memenuhi prerequisite.
5. Pilih kompetensi paling tinggi sebagai `PrimaryCompetencyID`.
6. Simpan sisanya sebagai `SecondaryCompetencyIDs`.
7. Simpan `RuleTrace` dan `ReviewFlags`.

## Aturan khusus

### Mad

- Mad alif: fathah diikuti alif atau alif khanjariyah yang benar-benar berfungsi sebagai mad.
- Mad ya: kasrah diikuti ya mati; ya berharakat tidak dihitung.
- Mad waw: dhammah diikuti waw mati; waw berharakat tidak dihitung.

### Sukun

Sukun umum diberi C0020. Jika huruf bersukun berupa hamzah, ain/ghain, atau huruf tebal, tambahkan C0021, C0022, atau C0023 sesuai keadaan.

### Tasydid

Objek bertasydid minimal C0024. Tasydid tidak otomatis menjadikan Lafzul Jalalah.

### Lafzul Jalalah

Bentuk dasar dan bentuk dengan awalan harus dideteksi melalui bentuk Utsmani aktual, bukan hanya canonical key tanpa harakat.

### Panjang objek

Jumlah huruf bukan kompetensi utama bila objek memiliki mad, tanwin, sukun, tasydid, hamzah, atau materi khusus yang lebih tinggi.

## Field output minimum

- `QWO_ID`
- `ArabicWord`
- `CanonicalKey`
- `SourceRef`
- `OccurrenceID`
- `PrimaryCompetencyID`
- `SecondaryCompetencyIDs`
- `RequiredCompetencyIDs`
- `RuleTrace`
- `ReviewFlags`
- `UsageStatus`
- `LifecycleStatus`

## UsageStatus

- `UNUSED`
- `RESERVED`
- `CONSUMED_PRIMARY`
- `USED_SECONDARY_CONTEXT`

Objek berstatus `CONSUMED_PRIMARY` tidak boleh dipilih kembali sebagai objek utama. Pemunculan kontekstual pada ayat utuh dicatat terpisah dan tidak mengubah prinsip bahwa pengulangan latihan dilakukan melalui kompetensi, bukan pengulangan objek utama.
