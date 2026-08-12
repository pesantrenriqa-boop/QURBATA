#!/usr/bin/env python3
"""Recover QURBATA Jilid 2 historical per-page visual/render history.

Scans the local Git object/history database, including files no longer present in HEAD,
without modifying the worktree. Produces a page-by-page inventory P001-P040 of likely
visual/render/material sources so frozen work is recovered before any page is rebuilt.
"""
from __future__ import annotations
import csv,re,subprocess
from collections import defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'dist/jilid-2-visual-history-recovery'
PAGE_RE=re.compile(r'(?:QJ2[-_]?P|jilid2[_-]?p)(\d{3})',re.I)
KEYWORDS=('render','visual','pdf','page','qj2','jilid-2','jilid2')

def git(*args:str,check=True)->str:
 p=subprocess.run(['git',*args],cwd=ROOT,text=True,encoding='utf-8',errors='replace',stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 if check and p.returncode!=0: raise RuntimeError('git '+' '.join(args)+'\n'+p.stderr)
 return p.stdout

def classify(path:str)->str:
 low=path.lower()
 if low.endswith('.py') and ('render' in low or 'pdf' in low): return 'RENDERER'
 if low.endswith(('.html','.htm','.css')): return 'VISUAL_SOURCE'
 if low.endswith('.pdf'): return 'PDF_ARTIFACT_TRACKED'
 if low.endswith(('.png','.jpg','.jpeg','.webp')): return 'VISUAL_ARTIFACT_TRACKED'
 if low.endswith(('.md','.csv','.json','.tsv')): return 'CONTENT_OR_SPEC'
 return 'OTHER'

def main():
 OUT.mkdir(parents=True,exist_ok=True)
 # --all is essential: frozen/older visual files may exist only on historical commits/branches.
 raw=git('log','--all','--format=@@COMMIT@@%H%x09%cI%x09%s','--name-only','--','tools','books/jilid-2','content/qwo')
 current=None; rows=[]; by_page=defaultdict(list)
 for line in raw.splitlines():
  if line.startswith('@@COMMIT@@'):
   payload=line[len('@@COMMIT@@'):]
   parts=payload.split('\t',2)
   current=(parts+['',''])[:3]
   continue
  path=line.strip()
  if not path or current is None: continue
  low=path.lower()
  if not any(k in low for k in KEYWORDS): continue
  m=PAGE_RE.search(path)
  if not m: continue
  n=int(m.group(1))
  if not 1<=n<=40: continue
  sha,date,subject=current
  rec={'page':f'P{n:03d}','kind':classify(path),'path':path,'commit':sha,'date':date,'subject':subject}
  rows.append(rec);by_page[n].append(rec)

 # Deduplicate same page/path/commit while preserving newest git-log order.
 seen=set(); unique=[]
 for r in rows:
  k=(r['page'],r['path'],r['commit'])
  if k in seen: continue
  seen.add(k);unique.append(r)

 inventory=OUT/'JILID-2-HISTORICAL-VISUAL-INVENTORY.tsv'
 with inventory.open('w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=['page','kind','path','commit','date','subject'],delimiter='\t');w.writeheader();w.writerows(unique)

 summary=OUT/'JILID-2-HISTORICAL-PAGE-SUMMARY.tsv'
 with summary.open('w',encoding='utf-8',newline='') as f:
  w=csv.writer(f,delimiter='\t');w.writerow(['page','history_hits','renderer_hits','visual_hits','latest_candidate_path','latest_candidate_commit'])
  for n in range(1,41):
   hits=by_page.get(n,[]);renderers=[x for x in hits if x['kind']=='RENDERER'];visual=[x for x in hits if x['kind'] in ('VISUAL_SOURCE','VISUAL_ARTIFACT_TRACKED','PDF_ARTIFACT_TRACKED')]
   preferred=(renderers or visual or hits)
   latest=preferred[0] if preferred else None
   w.writerow([f'P{n:03d}',len(hits),len(renderers),len(visual),latest['path'] if latest else '',latest['commit'] if latest else ''])

 missing=[n for n in range(1,41) if not by_page.get(n)]
 print('QJ2_VISUAL_HISTORY_RECOVERY=PASS')
 print(f'PAGES_WITH_HISTORY={40-len(missing)}')
 print('PAGES_WITHOUT_HISTORY='+(','.join(f'P{x:03d}' for x in missing) if missing else 'NONE'))
 print(f'HISTORY_RECORDS={len(unique)}')
 print(f'INVENTORY={inventory.relative_to(ROOT)}')
 print(f'SUMMARY={summary.relative_to(ROOT)}')
 print('WORKTREE_MODIFIED=NO')
 return 0

if __name__=='__main__': raise SystemExit(main())
