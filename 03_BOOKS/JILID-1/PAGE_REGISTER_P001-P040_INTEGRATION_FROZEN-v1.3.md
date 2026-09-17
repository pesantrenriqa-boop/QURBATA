# QURBATA JILID 1 — PAGE REGISTER INTEGRASI P001–P040

Status: **FROZEN v1.3 — CONTENT CONTROL**  
Effective: 2026-09-17  
Authority: PAGE REGISTER INTEGRATION OVERLAY  
Parent: `QURBATA_TARTIL_J1_MASTER_CURRICULUM_FROZEN-v1.1.md`  
Composition: `QURBATA_TARTIL_BOOK_COMPOSITION_RULES_FROZEN-v1.3.md`

Dokumen ini **tidak mengubah urutan kompetensi Tartil** pada empat register v1.0. Ia mengendalikan migrasi domain pendukung dan gate visual v1.3 sebelum generator/PDF dibangun ulang.

## 1. Authority

Urutan Tartil tetap berasal dari:
- `PAGE_REGISTER_P001-P010_FROZEN-v1.0.md`
- `PAGE_REGISTER_P011-P020_FROZEN-v1.0.md`
- `PAGE_REGISTER_P021-P030_FROZEN-v1.0.md`
- `PAGE_REGISTER_P031-P040_FROZEN-v1.0.md`

Jika teks domain pendukung pada register lama bertentangan dengan dokumen ini, **overlay v1.3 menang untuk Bi'ah/Akhlak/arti/layout metadata**. Tahfidz tetap mengikuti baseline distribusi Tahfidz frozen yang berlaku dan target halaman yang sudah disahkan; setiap panel Tahfidz wajib menambahkan arti Indonesia dari ayat/target yang tampil.

## 2. Schema wajib setiap halaman

```yaml
page: P001
TARTIL: {source_register: ..., active: ..., review: ...}
TAHFIDZ: {arabic: ..., meaning_id: ..., status: NEW|REVIEW}
BIAH: {arabic: ..., meaning_id: ..., repetition: INTRODUCE|REPEAT-1|REPEAT-2|REINFORCE}
AKHLAK: {arabic: ..., meaning_id: ..., repetition: INTRODUCE|REPEAT-1|REPEAT-2|REINFORCE}
GLYPH: {detached_ha_two_holes: REQUIRED}
LAYOUT: {teacher_labels_same_baseline: REQUIRED, writing_space_above_labels: REQUIRED}
```

`meaning_id` berarti teks kecil yang dicetak di bawah Arab adalah **arti Indonesia**, bukan instruksi aktivitas.

## 3. Distribusi Bi'ah Arabiyah P001–P040

Satu materi dipertahankan 1–3 pertemuan. Materi lama tetap boleh dipakai secara lisan secara kumulatif walau panel menampilkan fokus saat ini.

| Halaman | Arab | Arti panel | Status |
|---|---|---|---|
| P001 | السَّلَامُ عَلَيْكُمْ | Semoga keselamatan tercurah atas kalian | INTRODUCE |
| P002 | السَّلَامُ عَلَيْكُمْ | Semoga keselamatan tercurah atas kalian | REPEAT-1 |
| P003 | السَّلَامُ عَلَيْكُمْ | Semoga keselamatan tercurah atas kalian | REPEAT-2 |
| P004 | اُنْظُرْ | Lihatlah / perhatikan | INTRODUCE |
| P005 | اُنْظُرْ | Lihatlah / perhatikan | REPEAT-1 |
| P006 | اُنْظُرْ | Lihatlah / perhatikan | REPEAT-2 |
| P007 | اِسْتَمِعْ | Dengarkanlah | INTRODUCE |
| P008 | اِسْتَمِعْ | Dengarkanlah | REPEAT-1 |
| P009 | اِسْتَمِعْ | Dengarkanlah | REPEAT-2 |
| P010 | اِسْتَمِعْ | Dengarkanlah | REINFORCE |
| P011 | اِقْرَأْ | Bacalah | INTRODUCE |
| P012 | اِقْرَأْ | Bacalah | REPEAT-1 |
| P013 | اِقْرَأْ | Bacalah | REPEAT-2 |
| P014 | أَعِدْ | Ulangilah | INTRODUCE |
| P015 | أَعِدْ | Ulangilah | REPEAT-1 |
| P016 | أَعِدْ | Ulangilah | REPEAT-2 |
| P017 | اِفْتَحِ الْكِتَابَ | Bukalah buku | INTRODUCE |
| P018 | اِفْتَحِ الْكِتَابَ | Bukalah buku | REPEAT-1 |
| P019 | اِفْتَحِ الْكِتَابَ | Bukalah buku | REPEAT-2 |
| P020 | اِقْرَأْ | Bacalah | REINFORCE |
| P021 | أَغْلِقِ الْكِتَابَ | Tutuplah buku | INTRODUCE |
| P022 | أَغْلِقِ الْكِتَابَ | Tutuplah buku | REPEAT-1 |
| P023 | أَغْلِقِ الْكِتَابَ | Tutuplah buku | REPEAT-2 |
| P024 | مَرَّةً أُخْرَى | Sekali lagi | INTRODUCE |
| P025 | مَرَّةً أُخْرَى | Sekali lagi | REPEAT-1 |
| P026 | مَرَّةً أُخْرَى | Sekali lagi | REPEAT-2 |
| P027 | قِفْ | Berhentilah | INTRODUCE |
| P028 | قِفْ | Berhentilah | REPEAT-1 |
| P029 | قِفْ | Berhentilah | REPEAT-2 |
| P030 | اِقْرَأْ مَرَّةً أُخْرَى | Bacalah sekali lagi | REINFORCE |
| P031 | وَاصِلْ | Lanjutkanlah | INTRODUCE |
| P032 | وَاصِلْ | Lanjutkanlah | REPEAT-1 |
| P033 | وَاصِلْ | Lanjutkanlah | REPEAT-2 |
| P034 | نَعَمْ | Ya | INTRODUCE |
| P035 | نَعَمْ | Ya | REPEAT-1 |
| P036 | لَا | Tidak | INTRODUCE |
| P037 | لَا | Tidak | REPEAT-1 |
| P038 | أَحْسَنْتَ | Bagus / kamu telah berbuat baik | INTRODUCE |
| P039 | أَحْسَنْتَ | Bagus / kamu telah berbuat baik | REPEAT-1 |
| P040 | الْحَمْدُ لِلَّهِ | Segala puji bagi Allah | REINFORCE/CLOSING |

Catatan: kalimat nominal lama seperti `هَذَا كِتَابٌ`, `هَذَا قَلَمٌ`, `هَذِهِ صَفْحَةٌ` tidak dipakai sebagai jalur utama panel J1.

## 4. Distribusi Akhlak P001–P040

Akhlak dibentuk sebagai **pembiasaan 2–3 pertemuan**, bukan nash baru setiap halaman.

| Halaman | Tema / Arab | Arti panel | Status |
|---|---|---|---|
| P001–P003 | أَفْشُوا السَّلَامَ بَيْنَكُمْ | Sebarkanlah salam di antara kalian | INTRODUCE → REPEAT-2 |
| P004–P006 | وَقُلْ رَبِّ زِدْنِي عِلْمًا | Ya Tuhanku, tambahkanlah ilmuku | INTRODUCE → REPEAT-2 |
| P007–P009 | فَاسْتَمِعُوا لَهُ وَأَنْصِتُوا | Dengarkanlah dan perhatikanlah dengan tenang | INTRODUCE → REPEAT-2 |
| P010 | أَفْشُوا السَّلَامَ بَيْنَكُمْ | Sebarkanlah salam di antara kalian | REINFORCE |
| P011–P013 | إِنَّ اللَّهَ مَعَ الصَّابِرِينَ | Sesungguhnya Allah bersama orang-orang yang sabar | INTRODUCE → REPEAT-2 |
| P014–P016 | وَلَكَ الْجَنَّةُ | Dan bagimu surga | INTRODUCE → REPEAT-2 |
| P017–P019 | وَقُولُوا لِلنَّاسِ حُسْنًا | Berkatalah yang baik kepada manusia | INTRODUCE → REPEAT-2 |
| P020 | وَقُلْ رَبِّ زِدْنِي عِلْمًا | Ya Tuhanku, tambahkanlah ilmuku | REINFORCE |
| P021–P023 | أَدِّ الْأَمَانَةَ إِلَى مَنِ ائْتَمَنَكَ | Tunaikan amanah kepada orang yang mempercayaimu | INTRODUCE → REPEAT-2 |
| P024–P026 | وَلَا تُسْرِفُوا | Janganlah berlebih-lebihan | INTRODUCE → REPEAT-2 |
| P027–P029 | فَاسْتَبِقُوا الْخَيْرَاتِ | Berlomba-lombalah dalam kebaikan | INTRODUCE → REPEAT-2 |
| P030 | فَاسْتَقِمْ كَمَا أُمِرْتَ | Beristiqamahlah sebagaimana diperintahkan kepadamu | INTRODUCE |
| P031–P033 | إِنَّمَا الْمُؤْمِنُونَ إِخْوَةٌ | Sesungguhnya orang-orang beriman itu bersaudara | INTRODUCE → REPEAT-2 |
| P034–P036 | وَالْعَافِينَ عَنِ النَّاسِ | Orang-orang yang memaafkan manusia | INTRODUCE → REPEAT-2 |
| P037–P039 | وَرَتِّلِ الْقُرْآنَ تَرْتِيلًا | Bacalah Al-Qur'an dengan tartil | INTRODUCE → REPEAT-2 |
| P040 | تَعَلَّمْ — اِعْمَلْ — عَلِّمْ | Belajarlah — amalkanlah — ajarkanlah | REINFORCE/CLOSING |

Setiap rentang tiga halaman menggunakan status berurutan `INTRODUCE`, `REPEAT-1`, `REPEAT-2`.

## 5. Tahfidz + arti

- Target Tahfidz tidak diubah oleh migrasi v1.3.
- Sumber baseline: master distribusi Tahfidz FROZEN dan register halaman yang berlaku.
- Pada setiap halaman, generator wajib membawa `TAHFIDZ_ARABIC` bersama `TAHFIDZ_MEANING_ID`.
- `TAHFIDZ_MEANING_ID` adalah terjemah ringkas Indonesia dari ayat/bagian ayat yang benar-benar ditampilkan.
- Pada halaman review/checkpoint, teks Arab dapat berupa target murojaah/ringkasan yang sah; baris bawah tetap makna, bukan instruksi.
- Tidak boleh mencetak teks seperti `Hafalkan`, `Ulangi`, `Baca bersama guru` pada slot arti.

## 6. Gate glyph ha tunggal

Untuk seluruh Tartil P001–P040:
- detached `هَ / هِ / هُ / ه` harus dirender sebagai **ha dua lubang** sesuai bentuk QURBATA yang disetujui;
- audit wajib mencakup P013, P019, P027, P040 dan seluruh hasil pencarian glyph;
- varian karakter `ھ / ہ / ۀ / ە` dilarang sebagai jalan pintas;
- perbaikan dilakukan pada sequence/font/rendering yang benar, bukan mengganti identitas huruf.

## 7. Gate ukuran contoh/penanaman

- contoh penanaman Fathah/Kasrah/Dhammah diperbesar sampai batas aman;
- latihan utama tetap besar dan dominan;
- bounding box KFGQPC Uthman Taha wajib memiliki clear space dari garis kotak;
- tidak boleh ada clipping harakat;
- ukuran tidak boleh diperkecil hanya demi dekorasi.

## 8. Gate Tanggal–Nilai–TTD

- ketiga label berada pada baseline vertikal yang sama;
- ruang tulis berada di atas label;
- TTD tidak boleh naik karena QR;
- QR mempunyai kolom tersendiri;
- dilarang CSS khusus `last-child` yang menggeser TTD secara vertikal.

## 9. Status register lama

Empat register v1.0 tetap authority untuk **urutan Tartil**, tetapi field Bi'ah/Akhlak/layout metadata lama yang bertentangan dengan v1.3 berstatus **SUPERSEDED BY INTEGRATION OVERLAY v1.3**.

## 10. Production gate

Generator belum boleh dibangun dari PDF lama. Urutan berikut wajib:

`REGISTER v1.3 PASS → ARAB↔MEANING PASS → GLYPH PASS → GENERATOR MIGRATION → 40-PAGE BUILD → VISUAL AUDIT`.

PDF v1.2 dan sebelumnya: **OBSOLETE FOR CONTENT/LAYOUT v1.3**.
