# Placement Bank Quality Review Gate v1.0

**Scope:** L04/L10/L13/L19/L21 — 180 pilot items
**Status:** REVIEW GOVERNANCE — NON-PRODUCTION

## 1. Purpose

Menetapkan quality gate sebelum item placement dipromosikan dari research pool ke production registry.

## 2. Review dimensions

Setiap item diperiksa pada 10 dimensi:
1. target-K fidelity;
2. prerequisite integrity;
3. Qur'anic span accuracy;
4. linguistic answer validity;
5. feature-ceiling leakage;
6. ambiguity / alternate-analysis handling;
7. duplicate or near-duplicate function;
8. prompt clarity;
9. scoring objectivity;
10. translation/tafsir leakage.

## 3. Review statuses

- PASS: layak masuk reviewed registry.
- PASS-WITH-NOTE: layak dengan rubric/ceiling note eksplisit.
- REWRITE: konsep item valid tetapi prompt/span/scoring perlu revisi.
- HOLD-AMBIGUOUS: belum objektif untuk automated placement.
- HOLD-PREMATURE: membutuhkan kompetensi di atas checkpoint.
- RETIRE-DUPLICATE: fungsi diagnostik secara praktis diduplikasi item yang lebih baik.

## 4. Duplicate-function rule

Dua item dianggap near-duplicate jika memiliki kombinasi yang hampir sama dari primary K, response operation, misconception tested, surface-order pattern, dan routing consequence. Ayat berbeda saja tidak cukup untuk membuat fungsi diagnostiknya unik.

Setiap checkpoint tetap membutuhkan transfer diversity, sehingga duplicate lexical content dan duplicate diagnostic function dinilai terpisah.

## 5. Ambiguity gate

HIGH ambiguity tidak otomatis gagal, tetapi tidak boleh masuk automated scoring kecuali:
- semua alternate analyses yang mu'tabar diidentifikasi;
- rubric menerima alternatif sah;
- keputusan benar/salah tidak tergantung tafsir tertentu;
- scorer dapat menerapkan rubric secara konsisten.

Jika syarat ini tidak terpenuhi, status = HOLD-AMBIGUOUS.

## 6. Translation/tafsir leakage gate

Item gagal gate bila full credit dapat diperoleh hanya dengan:
- terjemahan;
- hafalan arti ayat;
- tema surah;
- asbab al-nuzul;
- pendapat tafsir;
- pengetahuan agama umum tanpa bukti bentuk/relasi linguistik.

## 7. Checkpoint-specific risk

- L04: feature-ceiling leakage dan false simplicity.
- L10: morphology vs relation confusion.
- L13: relation identification vs mere category naming.
- L19: over-analysis, domain leakage, ambiguity tinggi.
- L21: grammar vs semantics/discourse/tafsir contamination.

## 8. Review order

Review dilakukan dalam urutan:
1. structural/duplicate screen;
2. Arabic-content validation;
3. ambiguity/rubric validation;
4. assembly-balance validation;
5. pilot-data validation;
6. production promotion.

## 9. Production rule

Tidak ada item yang berstatus hanya PILOT boleh langsung dipanggil RIQA OS sebagai production item. RIQA OS hanya boleh memanggil registry entry dengan `review_status` PASS atau PASS-WITH-NOTE dan `production_enabled=true`.

## 10. Current bank state

- L04: 36 items, pool complete, quality-review ready.
- L10: 36 items, pool complete, quality-review ready.
- L13: 36 items, pool complete, quality-review ready.
- L19: 36 items, pool complete, quality-review ready.
- L21: 36 items, pool complete, quality-review ready.
- Total: 180/180 pilot items.

Completion of the pool is not equivalent to production approval.