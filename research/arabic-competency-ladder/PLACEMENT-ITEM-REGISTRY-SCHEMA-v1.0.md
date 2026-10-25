# Placement Item Registry Schema v1.0

**Status:** MACHINE-MAPPING SPEC — NON-PRODUCTION

## 1. Purpose

Mendefinisikan schema canonical untuk memindahkan 180 pilot items dari dokumen penelitian ke item registry yang versioned, auditable, dan siap dipanggil RIQA OS.

## 2. Canonical identity

Setiap item memiliki immutable identity:
- `item_id` — contoh `ARB-PL-L04-P001`
- `item_version` — semantic version, contoh `1.0.0`
- `checkpoint` — L04/L10/L13/L19/L21
- `stage` — S1–S5
- `primary_k`
- `secondary_k[]`

Jika isi substantif berubah setelah pilot dimulai, item_version wajib naik. `item_id` tidak boleh didaur ulang untuk soal berbeda.

## 3. Content fields

- `quran_ref`
- `target_span_ar`
- `prompt_id`
- `expected_response`
- `accepted_alternates[]`
- `response_class`
- `scoring_type`
- `max_score`
- `critical_misconception[]`
- `error_codes[]`
- `feature_ceiling`
- `ambiguity_level`

## 4. Diagnostic fields

- `prerequisite_k[]`
- `routing_failure_band`
- `remediation_k[]`
- `acceleration_signal`
- `transfer_flag`
- `negative_control_flag`
- `integrative_flag`
- `manual_review_required`

## 5. Governance fields

- `research_status`
- `review_status`
- `reviewer_role`
- `reviewed_at`
- `production_enabled`
- `retired_at`
- `superseded_by`
- `source_document`
- `source_commit`

## 6. Allowed review states

`PILOT`, `PASS`, `PASS_WITH_NOTE`, `REWRITE`, `HOLD_AMBIGUOUS`, `HOLD_PREMATURE`, `RETIRED_DUPLICATE`.

Only PASS and PASS_WITH_NOTE may become production-enabled.

## 7. Assembly metadata

Each item stores tags used by adaptive assembly:
- primary competency;
- functional class;
- surah source;
- ambiguity;
- prerequisite probe;
- transfer;
- contrast/negative;
- integrative;
- prior exposure risk.

This prevents a six-item form from accidentally drawing six items that test the same function.

## 8. Example registry record

```json
{
  "item_id": "ARB-PL-L13-P001",
  "item_version": "1.0.0",
  "checkpoint": "L13",
  "stage": "S3",
  "primary_k": "K31",
  "secondary_k": [],
  "quran_ref": "112:2",
  "target_span_ar": "اللَّهُ الصَّمَدُ",
  "response_class": "relation",
  "ambiguity_level": "LOW",
  "prerequisite_k": ["K08", "K11"],
  "review_status": "PILOT",
  "production_enabled": false
}
```

## 9. ID generation rule

- L04 items: `ARB-PL-L04-P001` … `P036`
- L10 items: `ARB-PL-L10-P001` … `P036`
- L13 items: `ARB-PL-L13-P001` … `P036`
- L19 items: `ARB-PL-L19-P001` … `P036`
- L21 items: `ARB-PL-L21-P001` … `P036`

Total canonical pilot identities: 180.

## 10. Next conversion step

Dokumen pilot tetap menjadi human-readable source. Registry berikutnya harus dibuat dalam format machine-readable (JSON/CSV/database seed) setelah quality screen menentukan status tiap item.