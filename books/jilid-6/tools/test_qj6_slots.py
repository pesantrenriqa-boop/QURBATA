#!/usr/bin/env python3
"""Unit tests for QJ6 register generation and audit gates."""
import csv,importlib.util,json,tempfile,unittest
from pathlib import Path
SCRIPT=Path(__file__).with_name("qj6_slots.py")
spec=importlib.util.spec_from_file_location("qj6_slots",SCRIPT)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
MASTER=Path(__file__).resolve().parents[1]/"QJ6-MASTER-Struktur-40-Halaman.md"
class RegisterTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
  self.csv=Path(self.tmp.name)/"slots.csv";self.report=Path(self.tmp.name)/"report.json"
  self.master=m.load_master(MASTER);m.init(self.master,self.csv)
 def rows(self):
  with self.csv.open(encoding="utf-8",newline="") as f:return list(csv.DictReader(f))
 def write(self,rows):
  with self.csv.open("w",encoding="utf-8",newline="") as f:
   w=csv.DictWriter(f,fieldnames=m.FIELDS);w.writeheader();w.writerows(rows)
 def test_360_slots_and_four_special_pages(self):
  rows=self.rows()
  self.assertEqual(len(rows),360)
  self.assertEqual(len({r["slot_id"] for r in rows}),360)
  self.assertEqual(rows[0]["slot_id"],"QJ6-P001-S01")
  self.assertEqual(rows[-1]["slot_id"],"QJ6-P040-S09")
  for page,kind in m.SPECIAL.items():
   self.assertEqual({r["kind"] for r in rows if r["page_id"]==f"QJ6-P{page:03d}"},{kind})
  self.assertEqual(m.audit(self.master,self.csv,self.report),0)
 def test_duplicate_and_missing_detected(self):
  rows=self.rows();rows[1]["slot_id"]=rows[0]["slot_id"];self.write(rows)
  self.assertEqual(m.audit(self.master,self.csv,self.report),1)
  findings=json.loads(self.report.read_text())["findings"]
  self.assertTrue(any(x[1]=="DUPLICATE_ID" for x in findings))
  self.assertTrue(any(x[1]=="MISSING_SLOT" for x in findings))
 def test_unverified_text_is_blocked(self):
  rows=self.rows();rows[0]["text_uthmani"]="نَصٌّ تَجْرِيبِيٌّ";self.write(rows)
  self.assertEqual(m.audit(self.master,self.csv,self.report),1)
  findings=json.loads(self.report.read_text())["findings"]
  self.assertTrue(any(x[1]=="SOURCE_UNVERIFIED" for x in findings))
  self.assertTrue(any(x[1]=="COMPETENCY_UNVERIFIED" for x in findings))
if __name__=="__main__":unittest.main()
