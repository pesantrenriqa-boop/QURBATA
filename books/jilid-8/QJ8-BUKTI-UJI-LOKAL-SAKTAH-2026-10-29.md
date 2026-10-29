# QJ8 — Bukti eksekusi uji lokal Saktah
Tanggal: 29 Oktober 2026. Status: **PASS STRUKTUR / HOLD TEKS**.

## Perintah yang benar-benar dijalankan
```bash
python /mnt/data/qj8/validate_saktah_source_gate.py --csv /mnt/data/qj8/prototipe_saktah_konteks.csv --gate /mnt/data/qj8/saktah_source_gate.json
python /mnt/data/qj8/test_saktah_gate_regression.py
```

## Keluaran aktual
```text
PASS: four cases; twelve unique required verse references.
HOLD: No authentic Uthmani verse source supplied; no text validated.
PASS: valid fixture accepted, missing verse rejected, blank verse rejected
HOLD: synthetic fixture is not Quran text; no source imported
```

## Ruang lingkup
- Pengujian di atas menggunakan salinan berkas kerja lokal `/mnt/data/qj8`, bukan eksekusi GitHub Actions.
- Empat kasus dan 12 rujukan adalah **struktur referensi**; bukan 12 ayat yang sudah diimpor.
- Fixture pengujian berisi teks sintetis; **bukan ayat Al-Qur'an**.
- Teks Arab sebelum–target–sesudah belum tersedia dari sumber mushaf resmi; tidak ada klaim tashih atau siap cetak.

## Tindak lanjut yang benar-benar membuka pekerjaan
1. Impor teks Utsmani resmi verbatim beserta checksum sumber.
2. Isi 12 ayat unik dalam empat panel Saktah dan jalankan pemeriksaan sumber.
3. Tashih tanda saktah dan jalur bacaan Hafs dengan ahli.
4. Baru susun PDF A5 kontekstual; jangan pakai 360 fragmen lama sebagai ayat penuh.
