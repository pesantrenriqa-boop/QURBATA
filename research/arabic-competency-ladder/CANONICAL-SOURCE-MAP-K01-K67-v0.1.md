# Canonical Source Map K01–K67 v0.1

**Status:** AUTHORITATIVE EXTRACTION MAP  
**Purpose:** identify the exact frozen source files that must be used to build the canonical registry without reconstructing definitions from memory.

## Source hierarchy

When multiple files discuss the same K, use the highest-priority source available:

1. `FINAL-GATE-...-v1.0.md`
2. `DRAFT-FROZEN-...-v1.0.md`
3. evidence/stress/head-to-head files only as supporting context

Do not rewrite a competency from a rescan or candidate file when a frozen source exists.

## K01–K10

Authoritative source:

- `DRAFT-FROZEN-K01-K10-v1.0.md`

Supporting source:

- `DRAFT-FREEZE-K1-K10-v0.1.md`
- `AUDIT-K05-INTEGRITY-K01-K10-v0.1.md`
- `EVIDENCE-BANK-K01-K10-v0.1.md`

## K11–K14

Authoritative source:

- `FINAL-GATE-K11-K14-v1.0.md`

## K15–K17

Authoritative source:

- `FINAL-GATE-K15-K17-v1.0.md`

## K18–K20

Authoritative source:

- `FINAL-GATE-K18-K20-v1.0.md`

## K21–K23

Authoritative source:

- `FINAL-GATE-K21-K23-v1.0.md`

## K24–K25

Authoritative source:

- `FINAL-GATE-K24-K25-v1.0.md`

## K26–K27

Authoritative source:

- `FINAL-GATE-K26-K27-v1.0.md`

## K28–K29

Authoritative source:

- `FINAL-GATE-K28-K29-v1.0.md`

## K30–K31

Authoritative source:

- `FINAL-GATE-K30-K31-v1.0.md`

## K32–K33

Authoritative source:

- `FINAL-GATE-K32-K33-v1.0.md`

## K34–K67

Each K has its own authoritative final gate:

- `FINAL-GATE-K34-v1.0.md`
- `FINAL-GATE-K35-v1.0.md`
- `FINAL-GATE-K36-v1.0.md`
- `FINAL-GATE-K37-v1.0.md`
- `FINAL-GATE-K38-v1.0.md`
- `FINAL-GATE-K39-v1.0.md`
- `FINAL-GATE-K40-v1.0.md`
- `FINAL-GATE-K41-v1.0.md`
- `FINAL-GATE-K42-v1.0.md`
- `FINAL-GATE-K43-v1.0.md`
- `FINAL-GATE-K44-v1.0.md`
- `FINAL-GATE-K45-v1.0.md`
- `FINAL-GATE-K46-v1.0.md`
- `FINAL-GATE-K47-v1.0.md`
- `FINAL-GATE-K48-v1.0.md`
- `FINAL-GATE-K49-v1.0.md`
- `FINAL-GATE-K50-v1.0.md`
- `FINAL-GATE-K51-v1.0.md`
- `FINAL-GATE-K52-v1.0.md`
- `FINAL-GATE-K53-v1.0.md`
- `FINAL-GATE-K54-v1.0.md`
- `FINAL-GATE-K55-v1.0.md`
- `FINAL-GATE-K56-v1.0.md`
- `FINAL-GATE-K57-v1.0.md`
- `FINAL-GATE-K58-v1.0.md`
- `FINAL-GATE-K59-v1.0.md`
- `FINAL-GATE-K60-v1.0.md`
- `FINAL-GATE-K61-v1.0.md`
- `FINAL-GATE-K62-v1.0.md`
- `FINAL-GATE-K63-v1.0.md`
- `FINAL-GATE-K64-v1.0.md`
- `FINAL-GATE-K65-v1.0.md`
- `FINAL-GATE-K66-v1.0.md`
- `FINAL-GATE-K67-v1.0.md`

## Extraction batches

To reduce accidental drift, extract and normalize in these batches:

- Batch A: K01–K10
- Batch B: K11–K20
- Batch C: K21–K33
- Batch D: K34–K45
- Batch E: K46–K57
- Batch F: K58–K67 (already normalized in `CANONICAL-REGISTRY-K58-K67-v0.1.md`)

## Required fields per extracted K

- K ID
- canonical name
- one-sentence definition
- learner operation
- primary domain
- direct prerequisites
- exclusions
- assessment signature
- architecture status
- evidence maturity

## Integrity rule

No competency may be renamed, merged, split, or semantically broadened during extraction. Any suspected overlap must be recorded in the later overlap audit rather than silently repaired inside the canonical registry.

## Next action

Fetch authoritative batches A–E and construct `CANONICAL-REGISTRY-K01-K67-v0.1.md` by preserving frozen wording first, then normalizing metadata fields around it.