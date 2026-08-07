# QWO Production Engine v1.0 — Freeze Record

## Status

**FROZEN — READY CANDIDATE POOL**

Freeze date: 2026-08-07
Branch: `content/qurbata-jilid-1-8-production`

## Verified foundations

- Quran Uthmani corpus: 6,236 ayat
- Master Quran objects generated: 647,901
- Real-object acceptance fixtures: 47/47 PASS
- Candidate sufficiency: C0001–C0041 PASS
- Shortage competencies: 0
- Candidate pool status: READY_CANDIDATE_POOL

## Frozen runtime

- `content/qwo/pedagogy/runtime/pedagogical_engine.py`
- `content/qwo/production/runtime/corpus_candidate_generator.py`
- `content/qwo/production/runtime/candidate_sufficiency_pipeline_v2.py`
- `content/qwo/composer/runtime/letter_fragment_extractor_v2.py`
- `content/qwo/production/runtime/merge_foundation_objects.py`

## Tracked verification artifacts

- `JILID-1-FOUNDATION-OBJECTS-V2.csv`
- `CANDIDATE-SUFFICIENCY-REPORT-V2.csv`
- `CANDIDATE-SUFFICIENCY-REPORT-V3.csv`

Large generated master and labeled datasets are reproducible build artifacts and are intentionally excluded from normal Git tracking.

## Verification commands

```powershell
python content/qwo/pedagogy/runtime/real_object_acceptance_test.py

Import-Csv content/qwo/production/generated/CANDIDATE-SUFFICIENCY-REPORT-V3.csv |
Where-Object Status -eq "SHORTAGE"
```

Expected results:

- `QURBATA real-object gate: VERIFIED_PASS`
- no rows with status `SHORTAGE`

## Change control

Any modification to this frozen foundation must be released as `v1.1` or `v2.0` and must rerun all acceptance and sufficiency gates.
