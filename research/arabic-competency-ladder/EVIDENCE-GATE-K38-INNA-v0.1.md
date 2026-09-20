# Evidence Gate K38 — Simple `إنّ + اسمها + خبرها` v0.1

**Status:** WORKING RESEARCH — PRE-FREEZE  
**Baseline:** K1–K37 DRAFT-FROZEN.  
**Target K38:** identify simple `إنّ + اسم إنّ + خبر إنّ` relation in Qur'anic evidence.

## 1. Why K38 is distinct

K33 only recognizes the token/category `إنّ`. K38 adds a new learnable operation:

1. identify `إنّ` as governor;
2. identify its explicit اسم;
3. identify its خبر;
4. observe the governed relation in a simple construction.

This is therefore not inventory expansion, but structural integration.

## 2. Hard dependencies

- K1–K3 nominal recognition/features as needed;
- K8 nominal predication foundation;
- K33 recognition `إنّ`;
- earlier PP/idhafah/na'at competencies may appear only when fully within K1–K37.

## 3. Core evidence policy

A PASS core example should prefer:

- explicit اسم إنّ;
- simple nominal or adjectival خبر;
- no `كان/ليس` in the target relation;
- no relative clause dependency;
- no conditional linkage;
- no hidden structure that is necessary to identify اسم/خبر;
- no new government phenomenon beyond K38.

Allowed expansion after core:
- PP khabar if all internal dependencies are already frozen;
- idhafah or na'at inside اسم/خبر if already within K1–K37;
- attached pronouns if their role is already covered by frozen Ks.

## 4. Evidence classes

### Class A — Pure core

Pattern approximately:
`إنّ + اسم ظاهر/ضمير معروف + خبر اسمي بسيط`

These are preferred teaching anchors because the relation is visible and local.

### Class B — Core with mastered internal structure

Examples may include already-frozen:
- idhafah;
- na'at;
- jar–majrur;
- demonstrative/pronoun components;
- attached-pronoun morphology.

PASS only if those internal relations require no K39+ competency.

### Class C — PREMATURE

Hold examples where khabar or اسم requires:
- `ليس`/`كان` construction analysis;
- silah maushul;
- hidden subject inference not yet frozen as a relation;
- conditional/clausal linkage;
- complex clause as khabar that cannot be analyzed with K1–K38 alone.

## 5. Clean-yield assessment

Qur'anic `إنّ` is highly productive, but many occurrences immediately enter complex clauses. Therefore the gate does **not** assume every `إنّ` occurrence is a K38 example.

Expected result:
- corpus candidate pool: large;
- pure Class A subset: narrower;
- Class B expands yield substantially using already-frozen structures;
- teaching target of 20–30+ is plausible, but must be occurrence-validated rather than estimated from token frequency alone.

## 6. Candidate anchor patterns for extraction

The evidence extractor should prioritize occurrences shaped like:

- `إنّ + اسم علم/اسم ظاهر + خبر صفة/اسم`;
- `إنّ + ضمير متصل معروف الوظيفة + خبر اسمي بسيط` only when pronoun segmentation/function is already covered;
- `إنّ + اسم + لَـ...` examples should be flagged for emphatic-lam review rather than automatically passed;
- `إنّ + اسم + خبر جار ومجرور` may be secondary evidence if attachment is clear and all dependencies are frozen.

No textual occurrence is marked PASS solely from surface shape; syntax must be occurrence-specific.

## 7. Integrity stress test

### Risk A — importing `لام التوكيد`

Some clean-looking `إنّ` constructions contain `لَـ` in the khabar. If recognizing/functionally analyzing that lām is required, mark REVIEW or PREMATURE until its dependency is explicitly covered.

### Risk B — pronoun اسم إنّ

Forms like `إنه/إنهم` are morphologically accessible because attached-pronoun recognition exists, but evidence must distinguish segmentation from the syntactic role اسم إنّ.

### Risk C — clausal khabar

A verbal or nominal clause as khabar may be structurally valid Arabic but is not core K38 unless the entire clause can be analyzed from earlier Ks without hidden higher relation.

## 8. Gate result

**K38 = STRUCTURALLY READY, EVIDENCE-GATED.**

There is no dependency reversal. The main remaining requirement before freeze is an occurrence-level evidence bank demonstrating sufficient clean examples and preserving negative evidence.

## 9. Recommended metadata

Each evidence record should store:

- `ayah_ref`;
- `target_span`;
- `inna_token`;
- `inna_name_span`;
- `inna_khabar_span`;
- `khabar_type`;
- `actual_dependencies[]`;
- `status`: PASS / REVIEW / PREMATURE;
- `premature_reason`;
- `contains_emphatic_lam`;
- `contains_relative_clause`;
- `contains_nawasikh_nested`;
- `teaching_tier`: core / reinforcement / advanced.

## 10. Next action

1. build occurrence-specific K38 evidence bank;
2. target 20–30+ PASS teaching candidates without forcing count;
3. if clean yield is confirmed, issue `FINAL-GATE-K38-v1.0`;
4. then compare K39 simple `ليس` construction against K40 simple `كان` construction.