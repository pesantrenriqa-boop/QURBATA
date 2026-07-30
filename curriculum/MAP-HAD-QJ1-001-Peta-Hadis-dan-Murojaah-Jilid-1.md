# MAP-HAD-QJ1-001 — Peta Hadis Akhlak dan Murojaah Jilid 1

**Map-ID:** MAP-HAD-QJ1-001  
**Status:** COMPLETE-DRAFT — SOURCE-CHECK / HOLD-PARTICIPANT  
**Tanggal:** 29 Juli 2026  
**Versi:** 0.2.0-id  
**Pengendali:** HCP-QUR-001 dan REG-HAD-001  
**Cakupan:** P001–P040

## 1. Tujuan

Peta ini menghubungkan 40 kandidat Hadith-ID Jilid 1 dengan halaman pengenalan dan putaran murojaah. Peta tidak mengaktifkan teks, tidak menggantikan takhrij, dan tidak memberi izin cetak kepada peserta.

## 2. Prinsip Murojaah

1. **Kumulatif lintas-jilid:** setelah diperkenalkan, setiap Hadith-ID masuk kolam murojaah sampai mencapai bukti retensi; objek akhir Jilid 1 dibawa ke awal Jilid 2.
2. **Berjarak:** halaman biasa memanggil kembali kandidat pada jarak sekitar 1, 3, 7, dan 14 pertemuan.
3. **Merata terjadwal:** checkpoint setiap delapan halaman menambah kandidat dengan frekuensi review terendah, tetapi beban dibatasi maksimum delapan prompt.
4. **Bertahap:** peserta cukup mengenali tema, makna sederhana, dan satu tindakan; teks Arab tetap kanal guru sampai whitelist disahkan.
5. **Tidak mengulang sebagai materi baru:** Hadith-ID hanya memiliki satu halaman intro. Kemunculan berikutnya selalu berlabel REVIEW.
6. **Error-aware:** guru memberi koreksi segera; recall yang salah tidak diulang tanpa pembetulan.
7. **Aman:** tidak ada hukuman, pelabelan iman, pemaksaan hafalan, pengungkapan kondisi keluarga, pungutan, atau perbandingan sedekah.

Prinsip 50% materi baru–50% murojaah pada latihan huruf/harakat tidak diterapkan sebagai hitungan teks hadis. Segmen hadis menggunakan **satu fokus baru + recall kumulatif terjadwal**, karena menampilkan seluruh matan terdahulu pada setiap halaman melampaui beban lima menit dan bertentangan dengan status HOLD-PARTICIPANT.

## 3. Format Lima Menit Usulan

| Waktu | Aktivitas |
|---:|---|
| 60 detik | recall kandidat terdekat tanpa melihat jawaban |
| 90 detik | guru menyampaikan tema/makna kandidat baru secara lisan |
| 60 detik | contoh tindakan atau skenario sederhana |
| 60 detik | recall kandidat berjarak/checkpoint terstratifikasi |
| 30 detik | umpan balik rahmah dan pencatatan bantuan |

Checkpoint P008, P016, P024, P032, dan P040 menggunakan maksimal delapan prompt pendek. Checkpoint tidak boleh berubah menjadi pembacaan ulang seluruh matan.

## 4. Pemetaan P001–P040

| Halaman | Intro | Tema | Review terjadwal | Mode |
|---|---|---|---|---|
| P001 | HAD-000001 | kasih sayang | — | INTRO + respons tindakan |
| P002 | HAD-000002 | ucapan baik | HAD-000001 | INTRO + recall berjarak |
| P003 | HAD-000003 | bersuci dan kebersihan | HAD-000002 | INTRO + recall berjarak |
| P004 | HAD-000004 | wajah ramah | HAD-000001, HAD-000003 | INTRO + recall berjarak |
| P005 | HAD-000005 | haya’ terpuji | HAD-000002, HAD-000004 | INTRO + recall berjarak |
| P006 | HAD-000006 | kelembutan | HAD-000003, HAD-000005 | INTRO + recall berjarak |
| P007 | HAD-000007 | salam | HAD-000004, HAD-000006 | INTRO + recall berjarak |
| P008 | HAD-000008 | kebaikan kecil | HAD-000001, HAD-000002, HAD-000003, HAD-000004, HAD-000005, HAD-000006, HAD-000007 | INTRO + CHECKPOINT TERSTRATIF |
| P009 | HAD-000009 | niat | HAD-000002, HAD-000006, HAD-000008 | INTRO + recall berjarak |
| P010 | HAD-000010 | konsistensi | HAD-000003, HAD-000007, HAD-000009 | INTRO + recall berjarak |
| P011 | HAD-000011 | tidak mengganggu | HAD-000004, HAD-000008, HAD-000010 | INTRO + recall berjarak |
| P012 | HAD-000012 | kendali marah | HAD-000005, HAD-000009, HAD-000011 | INTRO + recall berjarak |
| P013 | HAD-000013 | kebaikan bagi sesama | HAD-000006, HAD-000010, HAD-000012 | INTRO + recall berjarak |
| P014 | HAD-000014 | membantu sesama | HAD-000007, HAD-000011, HAD-000013 | INTRO + recall berjarak |
| P015 | HAD-000015 | belajar Al-Qur’an | HAD-000001, HAD-000008, HAD-000012, HAD-000014 | INTRO + recall berjarak |
| P016 | HAD-000016 | berkata baik | HAD-000002, HAD-000009, HAD-000010, HAD-000011, HAD-000012, HAD-000013, HAD-000014, HAD-000015 | INTRO + CHECKPOINT TERSTRATIF |
| P017 | HAD-000017 | kekuatan bermanfaat | HAD-000003, HAD-000010, HAD-000014, HAD-000016 | INTRO + recall berjarak |
| P018 | HAD-000018 | berterima kasih | HAD-000004, HAD-000011, HAD-000015, HAD-000017 | INTRO + recall berjarak |
| P019 | HAD-000019 | menguasai diri | HAD-000005, HAD-000012, HAD-000016, HAD-000018 | INTRO + recall berjarak |
| P020 | HAD-000020 | akhlak baik | HAD-000006, HAD-000013, HAD-000017, HAD-000019 | INTRO + recall berjarak |
| P021 | HAD-000021 | saling menguatkan | HAD-000007, HAD-000014, HAD-000018, HAD-000020 | INTRO + recall berjarak |
| P022 | HAD-000022 | tidak menipu | HAD-000008, HAD-000015, HAD-000019, HAD-000021 | INTRO + recall berjarak |
| P023 | HAD-000023 | menyingkirkan gangguan | HAD-000009, HAD-000016, HAD-000020, HAD-000022 | INTRO + recall berjarak |
| P024 | HAD-000024 | ihsan | HAD-000010, HAD-000017, HAD-000018, HAD-000019, HAD-000020, HAD-000021, HAD-000022, HAD-000023 | INTRO + CHECKPOINT TERSTRATIF |
| P025 | HAD-000025 | kejujuran | HAD-000011, HAD-000018, HAD-000022, HAD-000024 | INTRO + recall berjarak |
| P026 | HAD-000026 | setiap kebaikan | HAD-000012, HAD-000019, HAD-000023, HAD-000025 | INTRO + recall berjarak |
| P027 | HAD-000027 | persaudaraan aman | HAD-000013, HAD-000020, HAD-000024, HAD-000026 | INTRO + recall berjarak |
| P028 | HAD-000028 | anti-kezaliman | HAD-000014, HAD-000021, HAD-000025, HAD-000027 | INTRO + recall berjarak |
| P029 | HAD-000029 | kasih sayang luas | HAD-000015, HAD-000022, HAD-000026, HAD-000028 | INTRO + recall berjarak |
| P030 | HAD-000030 | tawaduk | HAD-000016, HAD-000023, HAD-000027, HAD-000029 | INTRO + recall berjarak |
| P031 | HAD-000031 | persaudaraan tanpa iri | HAD-000017, HAD-000024, HAD-000028, HAD-000030 | INTRO + recall berjarak |
| P032 | HAD-000032 | nasihat tulus | HAD-000018, HAD-000025, HAD-000026, HAD-000027, HAD-000028, HAD-000029, HAD-000030, HAD-000031 | INTRO + CHECKPOINT TERSTRATIF |
| P033 | HAD-000033 | kelembutan memperindah | HAD-000019, HAD-000026, HAD-000030, HAD-000032 | INTRO + recall berjarak |
| P034 | HAD-000034 | memudahkan dan menggembirakan | HAD-000020, HAD-000027, HAD-000031, HAD-000033 | INTRO + recall berjarak |
| P035 | HAD-000035 | menunjukkan kebaikan | HAD-000021, HAD-000028, HAD-000032, HAD-000034 | INTRO + recall berjarak |
| P036 | HAD-000036 | kasih muda dan hormat tua | HAD-000022, HAD-000029, HAD-000033, HAD-000035 | INTRO + recall berjarak |
| P037 | HAD-000037 | kelapangan bermuamalah | HAD-000023, HAD-000030, HAD-000034, HAD-000036 | INTRO + recall berjarak |
| P038 | HAD-000038 | menjaga anak yatim | HAD-000024, HAD-000031, HAD-000035, HAD-000037 | INTRO + recall berjarak |
| P039 | HAD-000039 | membantu keluarga rentan | HAD-000025, HAD-000032, HAD-000036, HAD-000038 | INTRO + recall berjarak |
| P040 | HAD-000040 | kebaikan kecil yang ikhlas | HAD-000026, HAD-000033, HAD-000034, HAD-000035, HAD-000036, HAD-000037, HAD-000038, HAD-000039 | INTRO + CHECKPOINT TERSTRATIF |

## 5. Aturan Pemerataan

- Satu unit review dicatat ketika peserta memperoleh prompt bermakna dan umpan balik, bukan hanya melihat judul.
- Beban sumber adalah 0–8 prompt per halaman; guru mengurangi jumlah bila pilot menunjukkan durasi berlebih.
- Pada checkpoint, objek dengan frekuensi terendah diprioritaskan setelah interval 1/3/7/14.
- Guru menggunakan rotasi peserta sehingga kesempatan menjawab tidak dikuasai peserta yang sama.
- Hadith-ID yang gagal diingat mendapat review remedial pada pertemuan berikut tanpa menghapus jadwal objek lain; remedial dicatat terpisah dari frekuensi rencana.
- HAD-000037–HAD-000040 dan objek lain yang belum mencapai paparan tervalidasi wajib masuk carryover awal Jilid 2.
- Setelah pilot, frekuensi aktual dihitung per Hadith-ID dan per peserta. Pemerataan dinilai terhadap kesempatan yang tersedia sejak halaman intro, bukan dengan menyamakan angka mentah objek awal dan akhir.
- P040 menjadi audit retensi akhir Jilid 1, bukan ambang universal kelulusan.

## 6. Pra-Audit Jadwal

| Ukuran | Hasil desain |
|---|---:|
| Halaman intro unik | 40/40 |
| Intro ganda | 0 |
| Maksimum prompt review satu halaman | 8 |
| Checkpoint | 5 |
| Review terencana HAD-000001–HAD-000039 dalam Jilid 1 | 1–5 kali |
| Review HAD-000040 setelah intro P040 | carryover wajib Jilid 2 |
| Status APPROVED | 0 |

Angka 1–5 bukan ambang efektivitas. Interval dan jumlah final harus ditentukan melalui uji durasi serta retensi.

## 7. Bukti yang Wajib Sebelum Aktivasi

- hasil takhrij, edisi, matan, grading, dan audit Full-Hadith-ID;
- teks dan terjemah yang disahkan;
- batas guru/peserta serta whitelist literasi;
- hasil uji durasi lima menit dan beban kognitif;
- rubrik recall, tindakan, remedial, dan safeguarding;
- tabel frekuensi aktual setiap Hadith-ID;
- peta carryover Jilid 2;
- Reviewer-ID, Evidence-ID, Decision-ID, dan otorisasi.

## 8. Riwayat

| Versi | Tanggal | Ringkasan |
|---|---|---|
| 0.2.0-id | 29 Juli 2026 | Membatasi checkpoint maksimum delapan prompt, memakai prioritas frekuensi terendah, dan menetapkan carryover Jilid 2 |
| 0.1.0-id | 29 Juli 2026 | Membentuk mapping intro dan interval awal |

## 9. Status

Pemetaan kandidat dan jadwal murojaah Jilid 1 telah lengkap secara desain. Status semua objek tetap SOURCE-CHECK, 0 APPROVED, dan 0 izin teks peserta. BLOCKED-CUR-HAD-001 tetap OPEN sampai seluruh bukti pada Bagian 7 tersedia.
