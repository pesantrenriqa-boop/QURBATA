# Draf pemetaan ungkapan Bi'ah Arabiyah QURBATA — 5 slot per halaman

**Status:** CANDIDATE / belum untuk cetak. **Branch:** draft/ungkapan-biah-arabiyah-5-slot
**Sumber pengendali:** QURBATA-BASELINE.md; REG-ARB-001, REG-ARB-002, REG-ARB-004; master dan halaman jilid terkait.
**Cakupan:** QJ1–QJ8, P001–P040; 320 halaman × 5 pasangan = 1.600 pasangan instruksi/pertanyaan dan respons (3.200 tuturan).

## Aturan
- S01–S02: masing-masing satu pertanyaan dan satu jawaban percakapan umum.
- S03: instruksi guru dan respons santri untuk materi Tartil pada halaman tersebut.
- S04: instruksi guru dan respons santri untuk tema Akhlak pada halaman tersebut.
- S05: instruksi guru dan respons santri untuk target Tahfidz pada halaman tersebut.
- Tiap pasangan wajib memiliki Page-ID, kompetensi dan dependency, Source-ID jika mengutip Qur'an/hadis, AR-FUN, AR-GRM, Pattern-ID, status, serta mode **lisan guru** atau **teks peserta**.
- Dilarang mencetak teks Arab pada halaman peserta bila tidak lolos whitelist baca halaman. Lisan guru boleh lebih maju dengan scaffolding; tidak boleh dianggap kompetensi baca peserta.
- Jangan menambah register otoritatif baru: pasangan masuk REG-ARB-002 sebagai AR-QA/AR-DLG; dokumen ini hanya draf pemetaan.
- Audit duplikasi membandingkan pasangan dan fungsi; repetisi pola yang disengaja untuk retensi ditandai review, bukan materi baru.
- K01–K65 dari sistem placement RIQA OS **belum terverifikasi ekuivalensinya** dengan AR-STG/AR-GRM QURBATA; tidak boleh disamakan tanpa crosswalk.

## Pilot QJ1-P001 (semua CANDIDATE)
Materi halaman: بَ تَ ثَ terpisah, fathah pendek; akhlak mendengarkan dan menirukan guru. Segmen bahasa Arab yang sudah ada: كِتَابٌ، قَلَمٌ secara **lisan**, bukan cetak peserta.

| Slot | Ujaran A (guru/pertanyaan) | Ujaran B (santri/jawaban) | Kesesuaian | Mode | Status |
|---|---|---|---|---|---|
| S01 | مَا هٰذَا؟ | هٰذَا كِتَابٌ. | Identifikasi benda konkret; prasyarat pola هٰذَا masih perlu gate | Lisan | CANDIDATE |
| S02 | أَهٰذَا قَلَمٌ؟ | نَعَمْ، هٰذَا قَلَمٌ. | Identifikasi pena; partikel tanya perlu audit dependency | Lisan | CANDIDATE |
| S03 | اِقْرَأْ: بَ، تَ، ثَ. | بَ، تَ، ثَ. | Fathah pendek, huruf terpisah; guru mengecek panjang bunyi | Lisan; model baca hanya huruf whitelist | CANDIDATE |
| S04 | اِسْتَمِعْ جَيِّدًا. | حَاضِرٌ، يَا أُسْتَاذُ. | Adab mendengarkan; kosakata respons perlu review | Lisan | CANDIDATE |
| S05 | رَدِّدْ بَعْدِي. | حَسَنًا، سَأُرَدِّدُ. | **Hanya contoh prosedur lisan**; target hafalan P001 belum diverifikasi | Lisan | BLOCKED: cek target Tahfidz |

## Checklist sebelum promosi
1. Ambil master terbaru dan konten halaman spesifik dari branch resmi.
2. Audit keselarasan Tartil, Akhlak, Tahfidz per Page-ID.
3. Crosswalk 65 kompetensi RIQA OS dengan registry AR-GRM/AR-FUN, tanpa mengasumsikan identitas.
4. Audit bahasa, i'rab, gender, naturalitas, duplikasi, beban N+1, dan mode lisan/cetak.
5. Setelah disetujui, integrasikan pasangan ke REG-ARB-002 dengan Object-ID resmi dan Evidence-ID.

**Catatan:** Tidak ada entri berstatus VALIDATED atau FINAL dalam pilot ini.
