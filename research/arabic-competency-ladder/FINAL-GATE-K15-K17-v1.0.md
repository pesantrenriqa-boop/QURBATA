# Final Gate K15–K17 v1.0

**Status:** DRAFT-FROZEN — RESEARCH LAYER ONLY  
**Parent:** `HEAD-TO-HEAD-K15-K17-v0.1.md`, `EVIDENCE-EXPANSION-K15-K17-v0.2.md`  
**Authority:** non-authoritative terhadap registry produksi.

## Frozen Research Sequence

### K15 — REC-PRON-ATT
Mengenali dhamir muttashil sebagai segmen morfologis pada host.

- target hanya recognition/segmentation;
- fungsi possessive, object, dan prep-object belum disatukan;
- evidence harus menyimpan host_type dan pronoun_form.

### K16 — REC-CONJ
Mengenali huruf 'athaf frekuen pada fungsi koordinatif yang tervalidasi.

- core: `و`, `ف`, `ثم` pada occurrence yang benar-benar berfungsi koordinatif;
- token identik dengan fungsi lain tidak boleh otomatis dilabel K16;
- construction dua unsur belum diajarkan sampai K18+.

### K17 — REL-ADJ
Na'at–man'ut sederhana.

- core dimulai dari pasangan dua token yang jelas;
- agreement diamati pada gender/number/definiteness/case sesuai evidence;
- nested idhafah, coordination, multiple adjective chain, dan struktur lebih tinggi ditahan.

## Final Integrity Check

Tidak ditemukan dependency reversal yang memaksa:
- na'at mendahului recognition dhamir muttashil;
- na'at mendahului recognition conjunction;
- construction 'athaf mendahului recognition conjunction.

Urutan K15 → K16 → K17 dipertahankan sebagai linearization pedagogis. Hard dependency tetap disimpan terpisah dari sequence order.

## Evidence Policy

- corpus bank unlimited;
- teaching set 20–30+ bila tersedia;
- PASS hanya bila seluruh dependency aktual <= current K;
- PREMATURE tetap disimpan sebagai negative evidence;
- unit pembelajaran boleh berupa potongan ayat yang utuh secara sintaksis;
- referensi surah:ayat penuh wajib disimpan.

## Status Boundary

Freeze ini TIDAK mengubah:
- REG-ARB-001;
- AR-STG-*;
- master jilid;
- halaman produksi;
- assessment produksi.

## Next Frontier

- K18-CAND — 'athaf dua unsur nominal sederhana;
- K19-CAND — dhamir muttashil sebagai mudhaf ilaih;
- K20-CAND — fa'il mustatir dasar.

Ketiganya wajib diuji head-to-head sebelum freeze berikutnya.