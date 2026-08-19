# RIQA M01 — TAHFIDZ QURBATA CROSSWALK FROZEN v1.0

**Competency ID:** RIQA-M01-TAHFIDZ-01  
**Marhalah:** M01  
**Status:** FROZEN CROSSWALK  
**Date:** 19 August 2026  
**Proposed SKR:** 2.00

## Canonical Source

Repository: `pesantrenriqa-boop/QURBATA`  
Branch: `main`

Primary frozen baseline:
- `02_MASTER_SYSTEM/TAHFIDZ/QURBATA-TAHFIDZ-AYAT-DISTRIBUTION-FROZEN-v1.0.md`

Jilid 1 page source used by the frozen baseline:
- `02_MASTER_SYSTEM/TAHFIDZ/QURBATA-TAHFIDZ-AYAT-DISTRIBUTION-WORKING-v0.1.md`

Integration contract:
- `02_MASTER_SYSTEM/TAHFIDZ/QURBATA-TAHFIDZ-INTEGRATION-CONTRACT-v1.0.md`

## M01 Mapping

`RIQA-M01-TAHFIDZ-01` is mapped to the QURBATA Tahfidz Jilid 1 track, P001–P040, as the canonical Tahfidz source for Marhalah 1.

The frozen J1–J8 distribution establishes the official corpus architecture. For Jilid 1, the frozen baseline explicitly delegates page-level mapping to `QURBATA-TAHFIDZ-AYAT-DISTRIBUTION-WORKING-v0.1.md`.

The Jilid 1 track begins with light memorization load and follows the QURBATA Tahfidz corpus sequence. The broader frozen architecture locks Al-Fatihah as a required special corpus and the main memorization path through Juz 30 onward.

## Governance Rule

- This crosswalk does not create a new memorization corpus.
- It binds RIQA M01 to the already-frozen QURBATA Tahfidz corpus.
- Future changes to the QURBATA Tahfidz frozen distribution require a new crosswalk version; this v1.0 must not be silently overwritten.
- Participant mastery/evidence remains governed by RIQA OS assessment and Tahfidz validation rules; this file only establishes canonical source identity and scope.

## Readiness Decision

The previous placeholder `crosswalk/unit-mapping-pending` is superseded by this exact canonical crosswalk.

Expected source status for `RIQA-M01-TAHFIDZ-01`: `CROSSWALK_FROZEN`.

Expected approval readiness after database reconciliation: `READY_FOR_HUMAN_APPROVAL`, subject to the normal RIQA approval engine and no additional source dependency blockers.
