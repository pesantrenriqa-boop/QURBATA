# Audit lanjutan QJ5 P039/K04 dan P039/K07 — 2026-11-01

Status: AUDIT DRAF / HOLD PENGGANTIAN / BELUM TASHIH FINAL.

## Bukti sumber
- Branch: `audit/j4-tashih-20261024`.
- Register: `02_MASTER_SYSTEM/BANK_REFERENSI_PER_KOMPETENSI/REGISTER_24_KELOMPOK_JILID_5.md`.
- P039/K04 aktif: `وَجَاءُوا أَبَاهُمْ عِشَاءً يَبْكُونَ` — QS 12:16. Target: mad wajib muttasil dan jaiz munfasil. Rujukan ayat diulang pada P003, P027, P037 menurut audit terdahulu.
- P039/K07 aktif: `وَالسَّمَاءِ ذَاتِ الْحُبُكِ` — QS 51:7. Target: mad wajib muttasil pada `السَّمَاءِ`. Rujukan ayat diulang pada P003 dan P033 menurut audit terdahulu.
- Nilai Sah P039: 0/8; jangan dinaikkan otomatis.

## Temuan penting
- K04 memuat dua target hukum mad; alternatif wajib menguji keduanya secara jelas, atau perubahan rancangan asesmen harus disetujui.
- K07 memerlukan contoh mad wajib muttasil dalam satu kata; jangan keliru mengklasifikasikan mad jaiz munfasil.
- Kebaruan harus diuji terhadap rujukan ayat dan teks NFC pada semua register yang benar-benar dapat dibuka, bukan hanya di dalam P039.
- Teks Arab calon pengganti harus dibandingkan dengan mushaf Utsmani otoritatif, termasuk tanda mad, hamzah, dan batas potongan ayat.
- Dokumen ini tidak mengesahkan kandidat pengganti, tidak mengubah register aktif, dan tidak mengubah Sah.

## Gate sebelum penggantian
1. Identifikasi 3 alternatif untuk K04 dan 3 untuk K07 beserta sumber QS dan posisi hukum.
2. Audit duplikasi lintas jilid/branch, simpan daftar file dan hasil.
3. Tashih rasm Utsmani dan klasifikasi tajwid oleh pemeriksa berwenang.
4. Arsipkan teks lama dan SHA register; ubah satu slot per commit menggunakan blob SHA terkini.
5. Audit ulang baris P039 dan pastikan Sah tetap 0 sampai pengesahan.

Keputusan: HOLD K04/K07. Perubahan berikutnya harus terpisah dari catatan audit ini.
