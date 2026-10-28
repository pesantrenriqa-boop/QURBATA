# QJ8 — Audit Substansi dan Gate Produksi Gharib (28 Oktober 2026)
**Status: temuan audit internal, bukan tashih mushaf/otorisasi.** Didasarkan pada perbandingan QJ8-MASTER-Struktur-40-Halaman.md dengan register isi operasional P001–P030; P031–P040 mengikuti pola latihan integrasi.

## Temuan kritis (harus diperbaiki sebelum desain cetak)
| ID | Tingkat | Temuan nyata | Tindakan |
|---|---|---|---|
| QJ8-AUD-001 | BLOCKER | Master P001–P040 masih berfokus tashih, retensi, portofolio, khidmah; register baru mengganti hampir semua halaman menjadi gharib. | Jangan menimpa master. Siapkan keputusan akademik dan matriks perubahan LO/KO/jenis halaman. |
| QJ8-AUD-002 | BLOCKER | Master mensyaratkan Hafalan 1 P018, Bahasa Arab P028, Hafalan 2 P036, Akhlak/Hadis P038; rancangan gharib menempati keempat halaman itu. | Tentukan penempatan domain HIF/FAH/AMT/KHT tanpa menghilangkan kewajiban, atau revisi master resmi melalui Decision-ID. |
| QJ8-AUD-003 | HIGH | Klaim '360 slot isi nyata' saat ini sebenarnya 360 **instruksi latihan** yang mengulang sekitar dua lusin lafaz, bukan 360 potongan ayat Qurani yang tercetak. | Pisahkan kolom Slot-ID, Qur'an-Text, Ref, Tipe aktivitas, dan status verifikasi. Jangan label siap cetak. |
| QJ8-AUD-004 | HIGH | P011–P020 memasukkan hamzatul washl dan muqaththa'ah yang berpotensi sudah dipelajari; P013 draf awal bahkan memakai Al-Fatihah yang diminta dihindari. | Audit kompetensi J1–J7; ganti materi penguatan berlebihan dengan kasus khusus yang sah. |
| QJ8-AUD-005 | HIGH | G8-025 Al-Kafirun 109:4 diindeks tetapi tidak dipakai; P027 dipindahkan ke Al-Kahfi 18:38 dalam register operasional, tidak sinkron dengan draf pemetaan. | Tandai G8-025 DEFERRED dan sinkronkan semua dokumen setelah keputusan. |
| QJ8-AUD-006 | HIGH | Beberapa lafaz sin/shad, 'Adan al-ula, ha' kinayah, ra, alif waqaf memerlukan penetapan wajah bacaan Hafsh dan pembuktian dari mushaf rujukan. | Tetapkan jalur, bukti mushaf, reviewer ahli, dan hasil talaqqi; jangan beri instruksi fonetik final. |
| QJ8-AUD-007 | MEDIUM | Tidak ada Source-ID resmi, Evidence-ID, reviewer, tanggal tashih, atau whitelist di setiap slot. | Tambahkan register keterlacakan sebelum rilis. |
| QJ8-AUD-008 | MEDIUM | Empat evaluasi P010/020/030/040 dipertahankan tetapi belum ada rubrik kelulusan, sampel paralel, remedial terukur. | Susun rubrik dan gate kelulusan mengikuti QC-000. |

## Tindakan koreksi yang berlaku mulai sekarang
1. **STOP** menyebut 360/360 sebagai ayat siap cetak; status yang benar 360/360 **aktivitas dirancang**, 0/360 **teks tervalidasi untuk cetak**.
2. **HOLD** perubahan master dan kasus dengan opsi qiraat/waqaf sampai jalur Hafsh RIQA dan Decision-ID disetujui.
3. **PILOT** P001–P004 dengan teks lengkap yang diambil langsung dari mushaf Utsmani berlisensi/diizinkan; verifikasi tiap tanda saktah, identitas ayat, dan panjang potongan.
4. **FORMAT slot siap cetak:** `QJ8-Pxxx-Kyy | ArabicText | Surah:Ayat | G8-ID | Jenis(materi/latihan/evaluasi) | StatusText | HafshRoute | Reviewer | Evidence-ID | StatusGate`.
5. **Tidak menghitung** instruksi seperti 'tunjuk tanda', 'tirukan guru', 'tashih' sebagai kutipan ayat baru; latihan boleh tetap ada sebagai aktivitas guru terpisah dari sembilan kotak teks santri.
6. **Kebijakan bahan ajar:** 9 kotak pada halaman peserta diupayakan berisi potongan ayat autentik yang bermakna dan sesuai kompetensi; jika kasus gharib unik kurang dari sembilan, gunakan konteks ayat sah, pengulangan terarah, atau kurangi kotak dengan keputusan desain, bukan mengarang ayat.

## Kriteria batch berikutnya
- Minimum satu halaman contoh nyata P001 dengan **9 entri teks Arab terisi**, tiap entri merujuk mushaf dan lokasi ayat yang benar, status verifikasi terpisah.
- Tidak mengubah materi inti Jilid 1–7 tanpa pembandingan kompetensi.
- Status RELEASED hanya setelah reviewer dan otorisasi lembaga.
