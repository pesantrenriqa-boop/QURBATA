# QWO Permanent ID Policy V1

## Core rule
A QWO identifier is permanent. It is never reused, renumbered, or reassigned after publication.

## Format

`QWO-NNNNNN`

Examples:
- `QWO-000001`
- `QWO-000250`
- `QWO-010000`

## Identity model

One QWO row represents one canonical learning object. The initial production model uses a verified Qur'anic surface-form occurrence as the source anchor. Identical surface forms may share a `DuplicateKey`, but they retain separate occurrence references when pedagogical or orthographic context differs.

## Lifecycle

- `REVIEW`: created but not yet approved for generator use.
- `ACTIVE`: source and competency mapping approved.
- `HOLD`: valid record temporarily excluded from curriculum generation.
- `RETIRED`: preserved for traceability but no longer selectable.

No row is physically deleted after an ID has been issued. Corrections are made through a new revision while preserving the ID and audit history.

## Allocation

1. Allocate IDs sequentially.
2. Never fill historical gaps.
3. Reserve no semantic meaning in the numeric part.
4. Curriculum placement belongs in `WhitelistLevel`, not in the ID.
5. Batch number is stored separately and must not alter the permanent ID.

## Duplicate handling

`DuplicateKey` groups normalized identical forms. Duplicate detection does not automatically merge objects because the same word may differ by:

- source occurrence,
- orthographic form,
- grammatical role,
- reading context,
- competency target,
- error risk,
- phrase or ayah relationship.

## Versioning

Schema changes use semantic versions. Object IDs do not change when the schema changes.

## Audit requirement
Every status transition must record reviewer, date, reason, and affected fields before integration with production generators.
