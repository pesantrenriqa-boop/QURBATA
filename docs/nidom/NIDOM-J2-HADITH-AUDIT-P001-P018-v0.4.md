# QURBATA NIDOM Jilid 2 — Hadith Content Audit P001–P018 v0.4

Status: CONTENT AUDIT IN PROGRESS — DO NOT FREEZE J2 YET

## Audit principles
1. Tema/kompetensi boleh berulang 3–5 halaman; redaksi hadits utama tidak boleh monoton.
2. Matan Arab harus mengikuti redaksi sumber yang dapat diverifikasi.
3. Potongan hadits boleh dipakai untuk tingkat anak, tetapi label sumber harus jelas dan potongan tidak boleh mengubah makna.
4. Terjemah Indonesia bersifat pedagogis namun tidak boleh menyimpang dari makna matan.
5. Kamus hanya mengambil kata/frasa yang benar-benar terdapat pada matan halaman tersebut.
6. Untuk Jilid 2, satu halaman tidak wajib menampilkan hadits jika modelnya kisah/kasus/praktik; tetapi bila hadits ditampilkan, hadits harus lolos audit ini.

## Verified anchors P001–P018

| Page | Theme | Matan / anchor | Source label | Audit |
|---|---|---|---|---|
| P001 | Senyum | تَبَسُّمُكَ فِي وَجْهِ أَخِيكَ لَكَ صَدَقَةٌ | Jami` at-Tirmidhi 1956 | VERIFIED; al-Tirmidhi: hasan gharib |
| P002 | Wajah ceria | لَا تَحْقِرَنَّ مِنَ الْمَعْرُوفِ شَيْئًا وَلَوْ أَنْ تَلْقَى أَخَاكَ بِوَجْهٍ طَلْقٍ | Sahih Muslim 2626 | VERIFIED |
| P003 | Salam | أَفْشُوا السَّلَامَ بَيْنَكُمْ | Sahih Muslim 54a — potongan akhir | VERIFIED; label as excerpt |
| P004 | Kebaikan | كُلُّ مَعْرُوفٍ صَدَقَةٌ | Sahih al-Bukhari 6021 / also transmitted in other collections | VERIFIED anchor; retain concise wording |
| P005 | Lisan aman | الْمُسْلِمُ مَنْ سَلِمَ الْمُسْلِمُونَ مِنْ لِسَانِهِ وَيَدِهِ | Sahih al-Bukhari / Sahih Muslim | VERIFIED |
| P006 | Berkata baik | فَلْيَقُلْ خَيْرًا أَوْ لِيَصْمُتْ | Sahih al-Bukhari 6018; Sahih Muslim 47 | VERIFIED excerpt |
| P007 | Kata baik | الْكَلِمَةُ الطَّيِّبَةُ صَدَقَةٌ | Sahih al-Bukhari / Sahih Muslim | VERIFIED |
| P008 | Tidak menyakiti | فَلَا يُؤْذِ جَارَهُ | Sahih al-Bukhari 6018; Sahih Muslim 47 | VERIFIED excerpt; theme link must explain non-harm |
| P009 | Sabar awal | إِنَّمَا الصَّبْرُ عِنْدَ الصَّدْمَةِ الْأُولَى | Sahih al-Bukhari / Sahih Muslim | VERIFIED |
| P010 | Kendali marah | لَيْسَ الشَّدِيدُ بِالصُّرَعَةِ ... عِنْدَ الْغَضَبِ | Sahih al-Bukhari 6114; Sahih Muslim 2609 | VERIFIED |
| P011 | Jangan marah | لَا تَغْضَبْ | Sahih al-Bukhari | VERIFIED concise prophetic counsel |
| P012 | Rifq | إِنَّ الرِّفْقَ لَا يَكُونُ فِي شَيْءٍ إِلَّا زَانَهُ | Sahih Muslim 2594a — first clause | VERIFIED excerpt |
| P013 | Rifq/kebaikan | مَنْ يُحْرَمِ الرِّفْقَ يُحْرَمِ الْخَيْرَ | Sahih Muslim | VERIFIED |
| P014 | Jujur | عَلَيْكُمْ بِالصِّدْقِ | Sahih al-Bukhari 6094; Sahih Muslim 2607 — excerpt | VERIFIED |
| P015 | Jujur menuju birr | إِنَّ الصِّدْقَ يَهْدِي إِلَى الْبِرِّ | Sahih al-Bukhari 6094; Sahih Muslim 2607 | VERIFIED |
| P016 | Dusta | وَإِذَا حَدَّثَ كَذَبَ | Sahih al-Bukhari / Sahih Muslim — excerpt from signs of hypocrisy | VERIFIED; MUST label as excerpt/context |
| P017 | Ingkar janji | وَإِذَا وَعَدَ أَخْلَفَ | Sahih al-Bukhari / Sahih Muslim — excerpt from signs of hypocrisy | VERIFIED; MUST label as excerpt/context |
| P018 | Khianat amanah | وَإِذَا اؤْتُمِنَ خَانَ | Sahih al-Bukhari / Sahih Muslim — excerpt from signs of hypocrisy | VERIFIED; MUST label as excerpt/context |

## Required renderer corrections after audit
- Normalize Arabic `الرِّفْق` rather than inconsistent kasrah/shadda spellings.
- Every shortened matan receives `— potongan hadits` / `— bagian hadits` in the source line.
- P016–P018 must not visually imply that each fragment is an independent complete hadith; source line must say it is a clause from the hadith on signs of hypocrisy.
- Dictionary tokens must be regenerated from the exact displayed matan after any correction.
- No J2 freeze until P019–P040 audit is completed and a final audit manifest is committed.

## External verification anchors used
- Jami` at-Tirmidhi 1956: smiling in the face of a brother is charity; graded hasan in the displayed record.
- Sahih Muslim 54a: spreading salam as a means of fostering love.
- Sahih Muslim 2594a: rifq adorns what it enters.
- Sahih al-Bukhari 6094: truthfulness leads to righteousness.

Next gate: audit P019–P040, patch source labels/matan/dictionaries, render 40/40, then freeze candidate.