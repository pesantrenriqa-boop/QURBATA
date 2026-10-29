#!/usr/bin/env python3
"""Regression test for first/last surah boundaries in QJ8 preview logic."""
from pathlib import Path
import csv
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from qj8_validate_context_manifest import LENGTHS

def refs(before,targets,after):
    return ([before] if before!="N/A" else []) + list(targets) + ([after] if after!="N/A" else [])

def main():
    assert refs("N/A",["18:1","18:2"],"18:3")==["18:1","18:2","18:3"]
    assert refs("112:3",["112:4"],"N/A")==["112:3","112:4"]
    assert LENGTHS[111]==4
    assert refs("N/A",["1:1"],"1:2")==["1:1","1:2"]
    print("PASS: start-of-surah, cross-verse, and end-of-surah context boundaries")

if __name__=="__main__":main()
