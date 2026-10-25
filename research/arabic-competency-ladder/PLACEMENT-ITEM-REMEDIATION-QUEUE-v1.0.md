# Placement Item Remediation Queue v1.0

**Status:** ACTIVE REMEDIATION QUEUE — NON-PRODUCTION

## 1. Versioning rule

Every substantive change to target construct, target span, expected response, feature ceiling, or scoring rubric requires a new item version. Original pilot IDs remain traceable; no historical record is overwritten semantically.

Suggested versioned form:
`ARB-PL-Lxx-Pyyy-v1.1`

## 2. Priority queue

### L04-P34 v1.1 candidate
Problem: expected response overstates one exclusive nominal analysis for `هو الله`.
Action: retain recognition of `هو` and require a ceiling-safe nominal relation; accept multiple valid pedagogical labels supported by expert rubric. Do not require full-verse i'rab.

### L10-P30 v1.1 candidate
Problem: target K22/K23 is too broad and the item combines `إنّ` with a following verbal form in a way that risks unclear construct attribution.
Action: split into a marker-classification item and, if needed, a separate transfer item. One scored construct per core item.

### L10-P34 v1.1 candidate
Problem: conditional environment risks requiring K31+ relation reasoning.
Action: reduce target to marker recognition + identification of local verbal units only; if domain membership itself is required, move item to L13 instead of forcing it into L10.

### L13-P28 v1.1 candidate
Problem: mixed `فـ/و` scope discrimination is under-specified and may rely on discourse interpretation.
Action: replace with a narrower coordination-scope pair where the units connected by `و` are explicit and other markers are excluded from scoring.

### L19-P28 v1.1 candidate
Problem: `إذا الشمس كورت` requires careful syntactic treatment and could force one analysis.
Action: human-review only until an alternate-analysis rubric is written. If objective automation remains impossible, keep as reviewer-led oral item or retire from routing.

### L19-P36 v1.1 candidate
Problem: two conditional frames + embedded relative unit create high cognitive and scoring complexity.
Action: keep as capstone diagnostic with segmented sub-scores, or split into two items. Do not use one holistic correctness score.

### L21-P31 v1.1 candidate
Problem: meta-evaluative prompt asks learner to critique an evaluator claim rather than directly demonstrate Quranic Arabic analysis.
Action: convert to an objective alternate-analysis task on an actual span. The learner must select/justify supported claims, not discuss evaluator authority.

## 3. Remediation exit criteria

An item leaves this queue only when:
- revised construct is singular and explicit;
- target span is sufficient but not excessive;
- feature ceiling is testable;
- expected answer is objectively scorable or explicitly human-reviewed;
- alternate analyses are handled;
- duplicate-risk family is checked;
- new version ID is assigned.

## 4. Governance

No queued item is production-enabled. Retiring an item does not reduce competency coverage until coverage audit confirms a replacement or redundant coverage exists.