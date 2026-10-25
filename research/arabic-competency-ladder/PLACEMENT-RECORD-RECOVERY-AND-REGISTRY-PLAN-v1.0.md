# Placement Record Recovery & Registry Promotion Plan v1.0

**Status:** ACTIVE RECOVERY CONTROL  
**Scope:** 180-item placement research bank  
**Branch:** `agent/quranic-arabic-competency-ladder`

## 1. Problem statement

The research bank reached 180/180 planned item slots, but several consolidated checkpoint files preserve earlier item ranges only by summary/reference rather than complete item records. GitHub code search did not recover independent canonical files for representative missing records such as L04-P01 and L10-P01. Therefore missing records must not be reconstructed from memory and must not receive inferred production approval.

## 2. Recovery classes

- **R0 FULL:** complete record exists and can be normalized directly.
- **R1 PATCH-RECOVERABLE:** complete record exists in an accessible PR patch/history and can be reconstructed verbatim from repository evidence.
- **R2 SUMMARY-ONLY:** only coverage/summary survives; record must be rebuilt as a new version from the canonical competency definition and Qur'anic evidence, never presented as the lost original.
- **R3 UNRESOLVED:** insufficient evidence even for safe reconstruction; slot remains disabled and a replacement item must be authored.

## 3. Non-fabrication rule

For R2/R3:
1. preserve original slot ID as historical/research reference;
2. do not claim recovered wording;
3. create a replacement/versioned record such as `ARB-PL-L04-P001-v2.0` only after fresh content review;
4. `production_enabled=false` until review gates pass.

## 4. Registry promotion pipeline

`research slot -> recovery class -> canonical full record -> quality disposition -> duplicate-function signature -> Arabic-content review -> item-quality review -> pilot eligible -> psychometric evidence -> production enabled`

No shortcut is allowed from `180/180 pool complete` to production.

## 5. Required registry fields

Every row must include:
- canonical_item_id
- historical_slot_id
- version
- checkpoint
- stage
- target_competency_ids
- prerequisite_ids
- quran_reference
- target_span
- response_class
- prompt
- expected_response
- scoring_key
- critical_misconception
- error_codes
- feature_ceiling
- ambiguity
- recovery_class
- quality_status
- verse_family_id
- function_signature
- alternate_analysis_policy
- reviewer_status
- pilot_status
- production_enabled

## 6. Current known recovery debt

Quality screens establish that many early ranges remain normalization/recovery pending, while later records are fully reproduced. The exact count must be computed only from repository-verifiable full records; no guessed percentage is permitted.

Known explicit problem items already enter remediation/versioning queue:
- L04-P34 — rewrite
- L10-P30 — rewrite
- L10-P34 — hold-premature
- L13-P28 — hold-ambiguous
- L19-P28 — hold-ambiguous
- L19-P36 — hold-ambiguous
- L21-P31 — hold-ambiguous
- earlier L19 high-ambiguity review items identified by the quality screen remain human-review only.

## 7. Duplicate-control integration

Before registry promotion, each full record receives:

`function_signature = checkpoint|primary_K|operation|response_class|target_relation`

and

`verse_family_id = surah:ayah-range|normalized-span-family`

Same verse family is allowed across checkpoints when the operation genuinely progresses. Same verse family + near-identical function signature within the same routing form is a retirement/replacement candidate.

## 8. Recovery execution order

1. Recover all R1 records available from PR patches/history.
2. Mark remaining missing slots R2 or R3.
3. Normalize all R0/R1 records into canonical registry rows.
4. Version and rewrite the known remediation queue.
5. Author replacements for R2/R3 only from canonical K definitions and verified Qur'anic evidence.
6. Run duplicate-function audit on the normalized bank.
7. Arabic-content review.
8. Freeze pilot-eligible registry snapshot.

## 9. Completion definition

Record normalization reaches 100% only when every one of 180 historical slots has exactly one explicit state:
- normalized active candidate,
- superseded by a versioned replacement,
- retired duplicate,
- or disabled unresolved.

Production readiness reaches 100% only when every enabled item has passed content, quality, pilot/psychometric, and routing validation. Disabled/retired items do not block registry completeness but cannot appear in live assessment.

## 10. Decision

**RECOVERY PLAN APPROVED FOR EXECUTION.**

The project will prefer traceability over artificial completion percentages. Missing historical wording will never be invented merely to make the registry appear complete.