# QURBATA JILID 1 — CHECKPOINT P020

Status: **CURATED v0.1 — FATHAH + KASRAH CHECKPOINT / NO NEW COMPETENCY**

Authority: `QURBATA-J1-TARTIL-PAGE-REGISTER-FROZEN-v1.0.md` v1.1.  
TYPE: CHECKPOINT  
FOCUS: `تَقْيِيمُ الْفَتْحَةِ وَالْكَسْرَةِ`  
LEGAL INVENTORY: seluruh kompetensi P001–P019.

> P020 bukan halaman pengenalan huruf/harakat baru. Ia menguji kemampuan santri membedakan, membaca, dan merangkai Fathah–Kasrah yang telah dipelajari.

## HARD GATES
- 24 kelompok curated.
- Tidak memakai pola REGULAR C01–C06 EXACT-2 TARGET-only.
- Tidak ada TARGET baru.
- Hanya Fathah + Kasrah legal P001–P019.
- Semua huruf detached/tunggal.
- Tidak ada Dhammah, sukun, tasydid, tanwin, atau mad sebagai kompetensi baru.
- Tidak ada kelompok 1 huruf.
- Tidak ada duplikasi kelompok.
- Meaningful Sequence Layer diprioritaskan.
- Kata meaningful tidak boleh dimanipulasi harakatnya.
- Global zero-repeat tetap aktif untuk source word meaningful.

## STRUKTUR EVALUASI

### A. DISKRIMINASI HARAKAT — EXACT-2
1. بَ بِ
2. تِ تَ
3. جَ جِ
4. دِ دَ
5. رَ رِ
6. سِ سَ

Tujuan: memastikan santri tidak sekadar mengenali huruf, tetapi benar-benar membedakan Fathah dan Kasrah pada huruf yang sama.

### B. DECODING CAMPURAN — EXACT-3
7. صَ ضِ طَ
8. ظِ عَ غِ
9. فَ قِ كَ
10. لِ مَ نِ
11. هَ وِ يَ
12. ءِ أَ إِ

Tujuan: perpindahan Fathah–Kasrah secara cepat tanpa bantuan makna.

### C. MEANINGFUL READING — EXACT-3
13. **كَ تِ بَ** ← `كَتِبَ` = bentuk leksikal yang tidak dipakai sebagai target makna utama; baca murni [PHONETIC/LEXICAL CAUTION]
14. **فَ هِ مَ** ← `فَهِمَ` = telah memahami [MSL — bila belum USED global]
15. **عَ لِ مَ** ← `عَلِمَ` = telah mengetahui [MSL — bila belum USED global]
16. **حَ مِ دَ** ← `حَمِدَ` = telah memuji [MSL — bila belum USED global]
17. **رَ كِ بَ** ← `رَكِبَ` = telah menaiki [MSL — bila belum USED global]
18. **سَ كِ نَ** ← `سَكِنَ` = telah tinggal/tenang [MSL — bila belum USED global]

> CATATAN ZERO-REPEAT: C14–C18 berasal dari bank kata legal yang sudah dikenal. Jika global rule dimaknai sebagai larangan pengulangan bahkan pada checkpoint, slot ini wajib diganti sebelum produksi. Jika checkpoint memang berfungsi menguji retensi, pengulangan terkontrol dapat diberi status REVIEW-REUSE dan tidak dihitung sebagai NEW MSL.

### D. TRANSFER / UNSEEN CURATED — EXACT-3
19. بَ لِ غَ
20. جَ لِ سَ
21. نَ زِ لَ
22. خَ دِ مَ
23. رَ جِ عَ
24. كَ سِ بَ

Kandidat bentuk tersambung:
- `بَلِغَ` — mencapai / menjadi balig; verifikasi konteks makna sebelum teacher note.
- `جَلِسَ` — telah duduk.
- `نَزِلَ` — bentuk ini perlu verifikasi morfologi; jangan beri makna sebelum QA.
- `خَدِمَ` — telah melayani.
- `رَجِعَ` — telah kembali.
- `كَسِبَ` — telah memperoleh.

## CHECKPOINT PEDAGOGY
P020 menguji empat lapis kemampuan:
1. **recognition** — mengenali huruf;
2. **harakat discrimination** — membedakan Fathah vs Kasrah;
3. **decoding** — merangkai tiga unit tanpa menebak;
4. **transfer** — membaca susunan/kata yang tidak bergantung pada hafalan halaman sebelumnya.

Makna tidak ditampilkan kepada santri sebelum ia selesai membaca. Guru menggunakan makna hanya sebagai penguatan setelah decoding.

## SCORING DRAFT
- Bagian A: 6 item × 2 poin = 12
- Bagian B: 6 item × 3 poin = 18
- Bagian C: 6 item × 5 poin = 30
- Bagian D: 6 item × 5 poin = 30
- Kelancaran keseluruhan = 10
- TOTAL = **100**

### RUBRIK KELANCARAN 10 POIN
- 9–10: lancar, tepat, hampir tanpa jeda.
- 7–8: tepat dengan beberapa jeda.
- 5–6: masih mengeja tetapi mayoritas benar.
- 3–4: banyak koreksi/bantuan.
- 0–2: belum mampu membaca mandiri.

## QA STATUS
- CHECKPOINT structure curated → PASS
- GROUP_COUNT 24/24 → PASS
- single-letter group → 0
- future competency → 0
- Dhammah → 0
- Fathah/Kasrah discrimination explicitly tested → PASS
- decoding without meaning explicitly tested → PASS
- meaningful/transfer layer → ACTIVE
- global duplicate policy on REVIEW-REUSE → **NEEDS FINAL POLICY LOCK**
- lexical form `نَزِلَ` → **NEEDS LEXICAL QA before production**
- renderer/PDF → NOT YET AUDITED

## PRODUCTION GATE
P020 belum boleh diberi label FINAL sampai:
1. REVIEW-REUSE policy diputuskan untuk checkpoint;
2. seluruh kandidat meaningful/transfer diaudit bentuk kamusnya;
3. tidak ada item yang menguji kompetensi di luar P001–P019;
4. visual renderer memastikan 24 kelompok detached terbaca jelas;
5. lembar nilai memuat nilai, tanggal, dan tanda tangan sesuai freeze halaman evaluasi.