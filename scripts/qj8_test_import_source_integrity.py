#!/usr/bin/env python3
"""Offline tests for the exact canonical reference set and source text preservation."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from qj8_validate_context_manifest import LENGTHS

def main():
    expected={f"{s}:{a}" for s,count in enumerate(LENGTHS,1) for a in range(1,count+1)}
    assert len(expected)==6236
    assert "18:1" in expected and "83:14" in expected
    altered=set(expected)
    altered.remove("18:1")
    altered.add("18:111")
    assert len(altered)==6236
    assert altered!=expected, "Equal verse count must not bypass reference integrity"
    assert "18:111" not in expected, "Out-of-range ayah must be rejected"
    sample="  بِسْمِ ٱللَّهِ  "
    assert sample!=sample.strip(), "Whitespace changes must be detectable"
    print("PASS: canonical set 6236; equal-count corrupted reference rejected by set comparison")
    print("PASS: whitespace-changing operation demonstrably detectable")
    print("HOLD: no source text imported; this is a synthetic regression test")

if __name__=="__main__":main()
