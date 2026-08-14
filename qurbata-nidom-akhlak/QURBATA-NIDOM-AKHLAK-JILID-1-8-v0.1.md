# QURBATA NIDOM AKHLAK
## Buku Pendamping QURBATA Jilid 1-8 - Prototipe Produk v0.1

Status: `PRODUCT_PROTOTYPE_V0.1`

Tujuan: membangun gradasi kompetensi akhlak berbasis hadits yang berjalan sejajar dengan QURBATA Jilid 1-8. Hafalan hadits adalah penguat; target utama adalah pemahaman dan perilaku yang dapat diamati.

## Gradasi

| Jilid | Fokus | Unit |
|---|---|---|
| 1 | Adab diri paling konkret | Salam; Bersih; Rapi dan Indah |
| 2 | Kasih sayang dan keramahan | Kasih Sayang; Berkata Baik; Senyum |
| 3 | Malu, emosi, kelembutan | Malu yang Baik; Jangan Marah; Bersikap Lembut |
| 4 | Empati dan adab sosial | Mencintai Kebaikan; Menjaga Lisan dan Tangan; Baik kepada Keluarga |
| 5 | Kejujuran dan amanah | Jujur; Tidak Curang; Amanah dan Janji |
| 6 | Regulasi diri dan konflik | Menguasai Diri; Bicara atau Diam; Memaafkan |
| 7 | Karakter sosial matang | Tawaduk; Menolong; Istiqamah |
| 8 | Integritas dan kebermanfaatan | Niat; Syukur; Belajar dan Mengajarkan |

## 24 Hadits Jangkar

1. `أَفْشُوا السَّلَامَ بَيْنَكُمْ` - HR. Muslim 54.
2. `الطُّهُورُ شَطْرُ الْإِيمَانِ` - HR. Muslim 223.
3. `إِنَّ اللهَ جَمِيلٌ يُحِبُّ الْجَمَالَ` - HR. Muslim 91.
4. `مَنْ لَا يَرْحَمْ لَا يُرْحَمْ` - Muttafaq 'alaih.
5. `الْكَلِمَةُ الطَّيِّبَةُ صَدَقَةٌ` - Muttafaq 'alaih.
6. `تَبَسُّمُكَ فِي وَجْهِ أَخِيكَ لَكَ صَدَقَةٌ` - HR. at-Tirmidzi 1956.
7. `الْحَيَاءُ شُعْبَةٌ مِنَ الْإِيمَانِ` - Muttafaq 'alaih.
8. `لَا تَغْضَبْ` - HR. al-Bukhari 6116.
9. `إِنَّ اللهَ رَفِيقٌ يُحِبُّ الرِّفْقَ` - HR. Muslim 2593.
10. `لَا يُؤْمِنُ أَحَدُكُمْ حَتَّى يُحِبَّ لِأَخِيهِ مَا يُحِبُّ لِنَفْسِهِ` - Muttafaq 'alaih.
11. `الْمُسْلِمُ مَنْ سَلِمَ الْمُسْلِمُونَ مِنْ لِسَانِهِ وَيَدِهِ` - Muttafaq 'alaih.
12. `خَيْرُكُمْ خَيْرُكُمْ لِأَهْلِهِ` - HR. at-Tirmidzi 3895.
13. `إِنَّ الصِّدْقَ يَهْدِي إِلَى الْبِرِّ` - Muttafaq 'alaih.
14. `مَنْ غَشَّنَا فَلَيْسَ مِنَّا` - HR. Muslim 101.
15. `آيَةُ الْمُنَافِقِ ثَلَاثٌ...` - Muttafaq 'alaih.
16. `لَيْسَ الشَّدِيدُ بِالصُّرَعَةِ...` - Muttafaq 'alaih.
17. `مَنْ كَانَ يُؤْمِنُ بِاللهِ وَالْيَوْمِ الْآخِرِ فَلْيَقُلْ خَيْرًا أَوْ لِيَصْمُتْ` - Muttafaq 'alaih.
18. `وَمَا زَادَ اللهُ عَبْدًا بِعَفْوٍ إِلَّا عِزًّا` - HR. Muslim 2588.
19. `وَمَا تَوَاضَعَ أَحَدٌ لِلهِ إِلَّا رَفَعَهُ اللهُ` - HR. Muslim 2588.
20. `وَاللهُ فِي عَوْنِ الْعَبْدِ مَا كَانَ الْعَبْدُ فِي عَوْنِ أَخِيهِ` - HR. Muslim 2699.
21. `أَحَبُّ الْأَعْمَالِ إِلَى اللهِ أَدْوَمُهَا وَإِنْ قَلَّ` - Muttafaq 'alaih.
22. `إِنَّمَا الْأَعْمَالُ بِالنِّيَّاتِ` - Muttafaq 'alaih.
23. `لَا يَشْكُرُ اللهَ مَنْ لَا يَشْكُرُ النَّاسَ` - HR. Abu Dawud 4811; at-Tirmidzi 1954.
24. `خَيْرُكُمْ مَنْ تَعَلَّمَ الْقُرْآنَ وَعَلَّمَهُ` - HR. al-Bukhari 5027.

## Struktur Unit Produk

Setiap unit memiliki: `competency_id`, target kompetensi, matan hadits, makna ringkas, NIDOM/praktik, cek capaian empat tahap, dan catatan guru/orang tua.

Cek capaian: `BELUM_TAMPAK -> MULAI_DIBIMBING -> TERBIASA_DENGAN_BANTUAN -> MANDIRI_KONSISTEN`.

## Batas Sistem

- Ini adalah pendamping QURBATA, bukan pengganti materi membaca Al-Qur'an.
- Tidak dicampur dengan kurikulum Sistem Diniyah RIQA.
- Hadits menjadi jangkar nilai, tetapi kelulusan akhlak tidak ditentukan oleh hafalan matan saja.
- Review editorial/takhrij final, pemetaan usia, ilustrasi, dan rubrik observasi rinci dilakukan pada versi berikutnya.
- Integrasi RIQA OS dilakukan melalui ID kompetensi dan evidence NIDOM/Akhlak.
