from pathlib import Path
from pedagogical_engine import load_rules, validate, has_madd

RULES = load_rules(Path(__file__).parents[1] / "PEDAGOGICAL-RULE-MATRIX-V1.csv")

def must_pass(text, object_type, competency):
    decision = validate(text, object_type, competency, RULES)
    assert decision.passed, (text, competency, decision.reasons)

def must_fail(text, object_type, competency, reason):
    decision = validate(text, object_type, competency, RULES)
    assert not decision.passed and reason in decision.reasons, (text, competency, decision.reasons)

must_pass("بَ", "LETTER", "C0002")
must_pass("بِ", "LETTER", "C0003")
must_pass("بُ", "LETTER", "C0004")
must_fail("ؤُ", "LETTER", "C0004", "HAMZA_FORBIDDEN")
must_fail("إِ", "LETTER", "C0003", "HAMZA_FORBIDDEN")
must_fail("بّ", "LETTER", "C0001", "SHADDA_FORBIDDEN")
must_fail("بْ", "LETTER", "C0001", "SUKUN_FORBIDDEN")
must_fail("بٌ", "LETTER", "C0001", "TANWIN_FORBIDDEN")
must_fail("بَا", "WORD_FRAGMENT", "C0006", "MADD_FORBIDDEN")
assert not has_madd("هُوَ")
assert has_madd("قُولُوا")
print("ALL_TESTS_PASSED")
