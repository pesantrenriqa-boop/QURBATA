# QWO Competency and Composer Status V1

Tanggal: 4 Agustus 2026
Branch: `content/qurbata-jilid-1-8-production`
Status: IMPLEMENTATION ACTIVE

## Selesai

1. Dependency Competency Map V1 dengan 41 kompetensi permanen.
2. Aturan pelabelan QWO berdasarkan kompetensi, bukan berdasarkan jilid.
3. Runtime `qwo_competency_labeler.py` untuk memberi kompetensi utama dan sekunder.
4. Runtime `book_composer.py` untuk memilih objek tanpa pengulangan CanonicalKey.
5. Template rencana halaman awal.
6. Bab khusus Lafzul Jalalah telah ditetapkan pada C0030–C0032.

## Prinsip yang dijalankan

- Urutan kompetensi mengendalikan pemilihan objek.
- Kompetensi boleh diulang dengan objek Al-Qur'an yang berbeda.
- Objek utama yang CanonicalKey-nya sudah dipakai tidak dipilih ulang.
- QWO tetap berstatus CANDIDATE sampai verifikasi pedagogis.
- Jilid 3 ke atas tidak dibatasi pada kata; objek mengikuti kompetensi dan dapat berkembang menjadi frasa, potongan ayat, dan ayat utuh.

## Hasil pelabelan lokal yang dapat direproduksi

- Input: 2.500 QWO V2 audited.
- Output terlabel: 2.500 objek.
- Objek tanpa kompetensi utama: 0.
- Pengulangan CanonicalKey: 0.
- Distribusi mengikuti 16 keluarga kompetensi QWO yang tersedia.

Dataset penuh tidak ditempel melalui Contents API karena ukurannya besar. Ia direproduksi dari input audited menggunakan runtime labeler yang disimpan pada branch ini. File contoh yang sempat tidak lengkap telah dihapus agar tidak dianggap sebagai data penuh.

## Batas saat ini

QWO adalah objek kata. Halaman awal Jilid 1 juga membutuhkan objek `LETTER` dan `WORD_FRAGMENT`. Karena itu Book Composer tidak boleh memaksa kata utuh untuk menggantikan huruf tunggal atau potongan dua huruf.

## Langkah eksekusi berikutnya

1. Membuat master objek `LETTER` dan `WORD_FRAGMENT` dari huruf dan potongan token Al-Qur'an.
2. Menjalankan composer pada halaman Jilid 1 yang objeknya sudah tersedia.
3. Menyusun QPO frasa setelah kompetensi C0033 aktif.
4. Menyusun potongan ayat dan ayat utuh berdasarkan kompetensi C0035–C0041.

Tidak ada perluasan fitur di luar kebutuhan langsung penyusunan delapan jilid.
