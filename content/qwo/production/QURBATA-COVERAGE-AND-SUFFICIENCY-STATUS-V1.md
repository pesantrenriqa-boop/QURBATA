# QURBATA Coverage and Candidate Sufficiency Status V1

## Status

`COVERAGE_COMPLETE_CANDIDATE_AUDIT_PENDING`

## Completed

- Positive real-Quran fixture coverage now exists for every competency C0001-C0041.
- Negative fixtures remain for early hamzah, early sukun, early shadda, wrong object type, wrong mad target, and short object submitted as long ayah.
- Candidate minimum requirements are defined for every competency.
- Candidate sufficiency auditor now returns PASS or SHORTAGE per competency and exits non-zero when any shortage remains.

## Production gate

The engine must not be declared READY_TO_GENERATE_QURBATA_1_8 until:

1. the full corpus-derived candidate file is produced with CompetencyID, CanonicalKey, Passed, and SourceRef;
2. candidate_sufficiency_audit.py returns READY_CANDIDATE_POOL;
3. page, volume, and series validators pass without duplicate CanonicalKey;
4. acceptance pages for Jilid 1, 2, 4, 6, and 8 pass.

## Current blocker

The full corpus-derived labeled candidate file has not yet been committed or reproduced inside the repository runtime. Therefore candidate sufficiency cannot yet be certified.
