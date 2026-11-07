# Arabic Competency Generator Spec v1.0

**Status:** CORE GENERATOR ARCHITECTURE — NON-PRODUCTION  
**Scope:** K01–K67 canonical Arabic competency ladder  
**Purpose:** convert the competency ladder into reusable engines for examples, questions, and books/guides without over-constraining future development.

## 1. Project boundary

This project is intentionally limited to four outcomes:
1. a detailed, ordered, extensible Arabic competency ladder;
2. automatic example generation/selection;
3. automatic question generation;
4. automatic book/guide generation.

Deep psychometric validation, production placement calibration, and exhaustive assessment science are **not blockers** for this project. They may be implemented by downstream systems later.

## 2. Source of truth

The canonical competency source is K01–K67. Each K is treated as an independent reusable unit with:
- `competency_id`
- `name`
- `learner_operation`
- `definition`
- `direct_prerequisites`
- `allowed_features`
- `forbidden_future_features`
- `evidence_rules`
- `difficulty_controls`
- `example_templates`
- `question_templates`
- `teaching_templates`
- `extension_hooks`

Core rule:

> An artifact generated for Kn may use features from K01..Kn, but must not require mastery of K(n+1)+ unless explicitly declared as enrichment/non-scored material.

## 3. Competency object model

Recommended machine-readable object:

```yaml
competency_id: K20
version: 1.0
status: canonical-core
name: "..."
learner_operation: "..."
definition: "..."
prerequisites:
  hard: [K01, K04]
  soft: []
feature_ceiling: K20
allowed_operations: []
forbidden_operations: []
example_policy:
  source: quran
  min_examples: 5
  preferred_examples: 20
  ambiguity_max: medium
question_policy:
  allowed_types: []
  default_count: 10
teaching_policy:
  explanation_depth: basic
  teacher_notes: true
extension:
  supersedes: null
  children: []
  tags: []
```

The schema may grow without changing the identity of existing K records.

## 4. Example Generator

### 4.1 Inputs

The generator accepts:
- target K or K range;
- number of examples;
- source restriction: Qur'an only / curated bank / synthetic pedagogical example if later enabled;
- difficulty: easy / standard / advanced-within-ceiling;
- learner age/level;
- output type: word / phrase / clause / verse span / mixed;
- novelty requirement;
- exclude previously used examples;
- teaching vs assessment use.

### 4.2 Generation logic

For target `Kn`:
1. load canonical definition and prerequisites;
2. construct allowed feature set = K01..Kn;
3. exclude all examples that require K(n+1)+ for correct target analysis;
4. select examples that visibly instantiate the target operation;
5. score each candidate for ambiguity, lexical load, length, and structural complexity;
6. rank by requested difficulty;
7. return target span + Qur'an reference + target operation + minimal explanation;
8. attach `feature_signature` for audit and reuse.

### 4.3 Example record

```yaml
example_id: EX-K20-0001
competency_id: K20
source: quran
reference: "2:..."
span_ar: "..."
target_feature: "..."
features_present: [K01, K04, K20]
features_required_for_solution: [K04, K20]
difficulty: easy
ambiguity: low
use:
  teaching: true
  assessment: true
  book: true
```

### 4.4 Safety against leakage

A candidate is rejected when:
- solving it requires an unmastered later K;
- the target operation is only inferable from tafsir rather than linguistic structure;
- ambiguity exceeds the requested ceiling;
- the example duplicates the same function/verse family beyond configured limits.

## 5. Question Generator

### 5.1 Inputs

- target K / K range;
- count;
- difficulty;
- question type;
- objective vs open response;
- teaching practice vs evaluation;
- include answer key;
- include rationale;
- exclude examples already used in lesson;
- cumulative review percentage.

### 5.2 Question families

Allowed reusable families:
- recognition;
- choose-the-correct-form;
- identify target element;
- pair/match;
- classify;
- segmentation;
- relation mapping;
- error detection;
- contrast between two structures;
- short constructed response;
- guided i'rab/analysis only within feature ceiling;
- cumulative review;
- enrichment/non-scored challenge.

Not every K must support every family. Each competency declares compatible templates.

### 5.3 Question generation pipeline

`K → operation → compatible template → eligible example → distractor rules → answer key → ceiling check → output`

Every generated question must carry:
- `question_id`;
- `target_K`;
- `tested_operation`;
- `source_example_id`;
- `question_type`;
- `prompt`;
- `options` if relevant;
- `correct_answer`;
- `rationale`;
- `difficulty`;
- `feature_signature`;
- `ceiling_check = pass/fail`.

### 5.4 Distractor generation

Distractors must be generated from plausible learner errors, for example:
- confuse noun vs verb;
- confuse subject vs object;
- confuse recognition vs relation;
- confuse one learned particle with another;
- choose a structurally similar but functionally wrong form.

Distractors may not depend on concepts above the learner's feature ceiling.

## 6. Book / Guide Generator

### 6.1 Supported outputs

The same K database can generate:
- student textbook;
- teacher guide;
- workbook;
- exercise bank;
- evaluation booklet;
- remediation booklet;
- enrichment booklet;
- competency handbook;
- curriculum scope-and-sequence;
- lesson-plan skeleton;
- QURBATA-compatible module.

### 6.2 Book generation inputs

- competency range, e.g. K01–K12;
- number of pages/meetings;
- audience;
- language of explanation;
- examples per K;
- questions per K;
- review ratio;
- enrichment ratio;
- page template;
- include teacher notes yes/no;
- include answers yes/no.

### 6.3 Default chapter/unit structure

For each K, generator may assemble:
1. competency objective;
2. prerequisite reminder;
3. one concise explanation;
4. worked examples;
5. guided practice;
6. independent practice;
7. cumulative review;
8. quick check/evaluation;
9. remediation;
10. enrichment;
11. teacher note when requested.

This structure is configurable, not mandatory.

### 6.4 Separation of content and layout

Generator architecture must separate:
- **content model** — K, examples, questions, explanations;
- **assembly model** — page/unit sequence;
- **presentation model** — typography, colors, layout, branding.

Therefore a design/template change must not require rewriting the competency content.

## 7. Guide Generator

Teacher/author guides can be generated from the same records with additional fields:
- what the K means;
- common errors;
- prerequisites to review;
- how to explain simply;
- suggested talqin/talaqqi/practice pattern;
- example progression;
- formative questions;
- remediation actions;
- enrichment options;
- boundaries: what **not** to teach yet.

The final field is mandatory because it preserves the cumulative ladder.

## 8. Open-ended extension architecture

K67 is the current core endpoint, **not the final boundary of Arabic knowledge**.

Future growth may use:
- new sequential competency: `K68`, `K69`, ...;
- subcompetency: `K38.1`, `K38.2` when granularity is needed;
- mastery depth separate from K identity;
- optional domain/plugin competencies;
- alternative pathways for age/program differences.

### Compatibility rules

1. existing K IDs are immutable once published as canonical;
2. revised definitions use versioning, not silent replacement;
3. new K may depend on old K, but old generated artifacts remain reproducible against their recorded version;
4. generator requests must record `registry_version`;
5. deprecated K is retained with status metadata and migration notes.

## 9. Minimal APIs / commands

Conceptual interfaces:

```text
generate_examples(K="K20", count=20, difficulty="easy")

generate_questions(K="K20", count=10, types=["recognition","relation"], answers=true)

generate_book(K_from="K01", K_to="K12", meetings=40, template="QURBATA-J1")

generate_teacher_guide(K_from="K01", K_to="K12")
```

Outputs should be deterministic when `seed` and `registry_version` are supplied.

## 10. Quality controls kept intentionally lightweight

Before generated output is accepted:
- target K exists;
- prerequisite graph is valid;
- feature ceiling check passes;
- exact Qur'an reference exists for sourced examples;
- target operation is present;
- answer key is consistent;
- duplicate threshold is respected;
- ambiguity does not exceed requested level.

No psychometric requirement is imposed by this generator core.

## 11. Project completion definition

This Arabic Competency Ladder project is considered functionally complete when:
- K01–K67 detailed canonical ladder exists;
- generator-ready schema exists for every K;
- Example Generator can produce ceiling-safe examples;
- Question Generator can produce answerable ceiling-safe questions;
- Book/Guide Generator can assemble selected K ranges into configurable artifacts;
- extension/versioning rules allow K68+ and deeper future development without breaking prior outputs.

## 12. Immediate implementation sequence

1. normalize K01–K67 into generator-ready records;
2. define shared `example_schema` and `question_schema`;
3. attach generator metadata to each K;
4. implement example selection/generation rules;
5. implement question template routing;
6. implement book/guide assembly manifest;
7. run three proof tests:
   - one early K;
   - one middle K;
   - one late K;
8. freeze generator contract v1.0 while leaving competency extension open.

## Governance decision

**The project is not required to become a complete assessment-science platform.** Its core role is a durable Arabic competency knowledge engine that can automatically supply examples, questions, and educational publications to QURBATA, RIQA OS, or future products.