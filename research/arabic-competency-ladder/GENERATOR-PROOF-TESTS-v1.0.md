# Generator Proof Tests v1.0

**Purpose:** prove that the K ladder can drive examples, questions, and publication assembly without turning this project into a full assessment-science platform.

## Test A — Early competency

Target: one early canonical K from the K01–K12 band.

Expected generator behavior:
1. load target definition and prerequisites;
2. select/generate examples whose required features do not exceed target K;
3. produce at least recognition + identify questions when compatible;
4. produce a student section and teacher-note section;
5. reject any candidate whose solution requires a later K.

PASS when the same competency record can feed all three outputs without rewriting the competency definition.

## Test B — Middle competency

Target: one canonical K from the K31–K40 band.

Expected generator behavior:
1. distinguish simple recognition from relational analysis where the ladder separates them;
2. select examples within the target ceiling;
3. generate at least two compatible question families;
4. include a boundary note telling the teacher what not to teach yet;
5. preserve registry version in every generated record.

PASS when example, question, and guide outputs remain aligned to the same target operation.

## Test C — Late competency

Target: one canonical K from the K58–K67 band.

Expected generator behavior:
1. allow longer clause spans when the target relation requires them;
2. preserve explicit marker/relation evidence;
3. reject tafsir-only inference as a linguistic target;
4. generate relation-mapping or short-response questions rather than forcing inappropriate recognition MCQ;
5. assemble an advanced guide section without changing lower-K records.

PASS when late complexity is handled by metadata/templates rather than by changing the core generator contract.

## Cross-test acceptance criteria

All three tests must satisfy:
- target K exists;
- prerequisite graph resolves;
- `feature_ceiling` is respected;
- output carries `registry_version`;
- Qur'an-sourced examples carry exact reference/span;
- question answer is derivable from the displayed linguistic evidence;
- output type can change without changing competency identity;
- extension to K68+ requires no renumbering of K01–K67.

## Minimal generation flow

```text
COMPETENCY RECORD
      |
      +--> EXAMPLE SELECTOR --> EXAMPLE RECORDS
      |
      +--> QUESTION ROUTER --> QUESTION RECORDS
      |
      +--> GUIDE CONTENT --> TEACHER/STUDENT BLOCKS

EXAMPLE + QUESTION + GUIDE BLOCKS
      |
      v
ASSEMBLY MANIFEST
      |
      v
PRESENTATION TEMPLATE
      |
      v
BOOK / GUIDE / WORKBOOK / QURBATA MODULE
```

## Decision

The proof target is **reusability and ceiling safety**, not psychometric perfection. Once these three classes of competency can use the shared schema, the generator contract is considered viable for expansion across K01–K67.