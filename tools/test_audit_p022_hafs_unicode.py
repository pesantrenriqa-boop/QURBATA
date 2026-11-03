"""Offline smoke tests; synthetic data only, not Quran source certification."""
import csv
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("audit_p022_hafs_unicode.py")

class CheckerTests(unittest.TestCase):
    def test_rejects_wrong_archive_hash_without_report(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            archive = root / "unverified.zip"
            archive.write_bytes(b"not the official archive")
            data = root / "verses.csv"
            data.write_text("sura_no,aya_no,aya_text_unicode\n", encoding="utf-8")
            register = root / "register.md"
            register.write_text("| P022 | Ikhfa syafawi |\n", encoding="utf-8")
            output = root / "report.json"
            result = subprocess.run([sys.executable, str(SCRIPT), "--archive", str(archive),
                "--data", str(data), "--register", str(register), "--output", str(output)],
                text=True, capture_output=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("SHA-256 mismatch", result.stderr)
            self.assertFalse(output.exists())

    def test_expected_reference_manifest_has_sixteen_distinct_slots(self):
        import importlib.util
        spec = importlib.util.spec_from_file_location("checker", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.assertEqual(len(module.REFERENCES), 16)
        self.assertEqual(len(set(module.REFERENCES)), 16)
        self.assertEqual(len(module.EXPECTED_SHA256), 64)

if __name__ == "__main__":
    unittest.main()
