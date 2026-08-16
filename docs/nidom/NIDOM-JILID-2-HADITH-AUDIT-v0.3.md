# QURBATA NIDOM JILID 2 — HADITH CONTENT AUDIT v0.3

Status: PRE-FREEZE AUDIT GATE
Scope: P001–P040

## Production rule
1. Kompetensi/tema boleh diulang 3–5 halaman.
2. Redaksi hadits utama tidak boleh monoton pada halaman berurutan.
3. Hadits berbeda harus tetap satu rumpun kompetensi.
4. Kamus Arab–Indonesia harus mengikuti redaksi hadits pada halaman itu.
5. Potongan hadits harus diberi konteks yang tidak mengubah makna asal.
6. Prioritas sumber: Sahih al-Bukhari, Sahih Muslim; kemudian riwayat hasan/sahih yang jelas statusnya.
7. Terjemah untuk anak boleh disederhanakan, tetapi tidak boleh menggeser makna matan.
8. Font matan dan kamus: Uthman Taha production font.

## Audit matrix
| Pages | Competency | Audit focus | Status |
|---|---|---|---|
| P001–P004 | Salam, senyum, membuat nyaman | variasi senyum/wajah ceria/salam/kebaikan | REVIEWED |
| P005–P008 | Menjaga lisan | keselamatan lisan/berkata baik/kalimah tayyibah/tidak menyakiti | REVIEWED |
| P009–P013 | Sabar & kendali reaksi | sabar awal/menguasai marah/larangan marah/rifq | REVIEWED |
| P014–P018 | Jujur & janji | sidq/kadhib/wa'd/amanah | REVIEWED |
| P019–P020 | Checkpoint | tanpa pemaksaan hadits baru | REVIEWED |
| P021–P024 | Rahmah | kasih sayang dan praktik empati | REVIEWED |
| P025–P028 | Amanah | menunaikan amanah/tanggung jawab | REVIEWED |
| P029–P032 | Hormat & adab | muda-tua/adab/akhlak | REVIEWED |
| P033–P035 | Menolong benar | pertolongan dalam kebaikan | REVIEWED |
| P036–P040 | Evaluasi akhir | recall lintas kompetensi; hadits tidak dipaksakan | REVIEWED |

## Verified anchors
- Rifq: `إِنَّ الرِّفْقَ لَا يَكُونُ فِي شَيْءٍ إِلَّا زَانَهُ...` — Sahih Muslim 2594. Digunakan sebagai jangkar kompetensi kelembutan/kendali reaksi.
- Sidq: `عَلَيْكُمْ بِالصِّدْقِ...` / `إِنَّ الصِّدْقَ يَهْدِي إِلَى الْبِرِّ` — muttafaq/alaih; Sahih Muslim 2607 sebagai jangkar kompetensi jujur.

## Freeze gate
Jilid 2 belum boleh diberi label CONTENT-FROZEN sebelum:
- [ ] seluruh nomor sumber pada renderer diaudit satu per satu;
- [ ] setiap matan dibandingkan dengan sumber rujukan;
- [ ] terjemah Indonesia diperiksa semantik;
- [ ] kamus per kata diperiksa terhadap matan aktual;
- [ ] duplicate detector memastikan tidak ada pengulangan monoton;
- [ ] PDF final 40/40 PASS tanpa overflow/font fallback.

## Decision
Struktur pedagogis Jilid 2 diterima sebagai baseline. Freeze konten ditahan sampai audit sumber per halaman selesai. Ini mencegah PDF yang secara visual PASS tetapi memiliki citation drift atau matan/kamus yang tidak sinkron.
