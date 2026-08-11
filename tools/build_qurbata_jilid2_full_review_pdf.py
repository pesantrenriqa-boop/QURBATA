#!/usr/bin/env python3
from __future__ import annotations
import argparse, asyncio, html, re, subprocess, sys
from dataclasses import dataclass
from pathlib import Path
from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / 'tools') not in sys.path:
    sys.path.insert(0, str(ROOT / 'tools'))

import render_qurbata_jilid2_p001_v19_kfgqpc as kfgloader
import render_qurbata_jilid2_sukun_lab_v5 as sukunlab

CURRENT_SRC = ROOT / 'books/jilid-2/rebased'
RECOVERY_COMMIT = '67a42c40d796cbdcead4e98f5d03da370ac22406'
DEFAULT = ROOT / 'dist/jilid-2-full-review'

@dataclass
class PageSource:
    number: int
    name: str
    text: str
    origin: str
    path: str


def page_number(name: str):
    m = re.search(r'QJ2-P(\d{3})', name, re.I)
    return int(m.group(1)) if m else None


def git(*args: str) -> str:
    p = subprocess.run(
        ['git', *args], cwd=ROOT, text=True, encoding='utf-8',
        errors='replace', stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    if p.returncode != 0:
        raise RuntimeError('GIT_COMMAND_FAILED: git ' + ' '.join(args) + '\n' + p.stderr.strip())
    return p.stdout


def current_sources():
    pages: dict[int, PageSource] = {}
    if not CURRENT_SRC.exists():
        return pages
    for path in sorted(CURRENT_SRC.glob('QJ2-P*.md')):
        n = page_number(path.name)
        if n and 1 <= n <= 40 and n not in pages:
            pages[n] = PageSource(
                n, path.name, path.read_text(encoding='utf-8'),
                'CURRENT_BRANCH', str(path.relative_to(ROOT)).replace('\\', '/')
            )
    return pages


def historical_sources(commit: str):
    pages: dict[int, PageSource] = {}
    listing = git('ls-tree', '-r', '--name-only', commit, '--', 'books/jilid-2')
    candidates = []
    for raw in listing.splitlines():
        path = raw.strip()
        if not path.lower().endswith('.md'):
            continue
        n = page_number(Path(path).name)
        if n and 1 <= n <= 40:
            candidates.append((n, path))

    # Prefer paths that look like active/rebased/staging page sources over audits/maps.
    def rank(item):
        n, p = item
        low = p.lower()
        score = 0
        if '/rebased/' in low: score += 100
        if '/staging/' in low: score += 80
        if '/pages/' in low: score += 60
        if '/draft' in low: score += 20
        if 'audit' in low or 'map-' in low or 'register' in low: score -= 100
        return (n, -score, p)

    for n, path in sorted(candidates, key=rank):
        if n in pages:
            continue
        try:
            text = git('show', f'{commit}:{path}')
        except RuntimeError:
            continue
        pages[n] = PageSource(n, Path(path).name, text, f'GIT_RECOVERY_{commit[:8]}', path)
    return pages


def merged_sources():
    current = current_sources()
    recovery = historical_sources(RECOVERY_COMMIT)
    merged: dict[int, PageSource] = {}
    for n in range(1, 41):
        # Latest active branch wins; verified 40/40 snapshot fills gaps only.
        if n in current:
            merged[n] = current[n]
        elif n in recovery:
            merged[n] = recovery[n]
    return merged, current, recovery


def esc(text: str):
    return html.escape(text).replace('**', '')


def markdown_preview(text: str):
    out = []
    for line in text.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.startswith('# '):
            out.append('<h1>' + esc(s[2:]) + '</h1>')
        elif s.startswith('## '):
            out.append('<h2>' + esc(s[3:]) + '</h2>')
        elif s.startswith('|'):
            out.append('<div class="row">' + esc(s) + '</div>')
        elif s.startswith('- '):
            out.append('<div class="bullet">• ' + esc(s[2:]) + '</div>')
        else:
            out.append('<p>' + esc(s) + '</p>')
    return ''.join(out)


def build(source_pages: dict[int, PageSource], font_uri: str):
    pages = []
    for n in range(1, 41):
        source = source_pages.get(n)
        if source:
            body = markdown_preview(source.text)
            source_line = f'{source.origin} · {source.path}'
        else:
            body = '<div class="missing">SOURCE MISSING AFTER RECOVERY</div>'
            source_line = 'MISSING'
        pages.append(
            f'<section class="sheet"><div class="inner">'
            f'<div class="tag">JILID 2 FULL REVIEW · RECOVERY PROOF · NOT FINAL PRINT</div>'
            f'<div class="folio">{n:02d}</div>'
            f'<div class="src">{html.escape(source_line)}</div>{body}'
            f'</div></section>'
        )

    css = f'''@page{{size:A5;margin:0}}
*{{box-sizing:border-box}}
@font-face{{font-family:q;src:url("{font_uri}")}}
body{{margin:0;background:#ddd}}
.sheet{{width:148mm;height:210mm;page-break-after:always;background:#fff;padding:8mm;overflow:hidden}}
.inner{{height:100%;position:relative;transform-origin:top left;font:7.2pt/1.2 q,Arial}}
.tag{{font:700 5.2pt Arial;color:#777;border-bottom:.2mm solid #b98a2f;padding-bottom:1mm}}
.folio{{position:absolute;right:0;top:-1mm;background:#064d37;color:white;padding:1.5mm 2mm;font:700 8pt Arial}}
.src{{font:4.6pt Consolas;color:#999;margin:1mm 0;direction:ltr;text-align:left}}
h1{{font:700 10pt Arial;color:#064d37;margin:1mm 0}}
h2{{font:700 8pt Arial;color:#064d37;margin:1.3mm 0 .5mm}}
p,.row,.bullet{{margin:.45mm 0}}
.row{{font-size:6.4pt;border-bottom:.1mm solid #ddd;padding:.25mm}}
.missing{{margin-top:60mm;text-align:center;color:#b00;font:700 14pt Arial}}
'''
    script = '''<script>
(async () => {
  await document.fonts.ready;
  for (const sheet of document.querySelectorAll('.sheet')) {
    const inner = sheet.querySelector('.inner');
    const available = sheet.clientHeight;
    const needed = inner.scrollHeight;
    if (needed > available) {
      const zoom = Math.max(0.42, available / needed);
      inner.style.transform = 'scale(' + zoom + ')';
      inner.style.width = (100 / zoom) + '%';
    }
  }
})();
</script>'''
    return '<!doctype html><html><head><meta charset="utf-8"><style>' + css + '</style></head><body>' + ''.join(pages) + script + '</body></html>'


async def render(html_path: Path, out: Path):
    pdf = out / 'QURBATA-JILID-2-FULL-REVIEW-P001-P040-RECOVERED.pdf'
    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        page = await browser.new_page(viewport={'width': 1120, 'height': 1584})
        await page.goto(html_path.resolve().as_uri(), wait_until='networkidle')
        await page.evaluate('document.fonts.ready')
        await page.wait_for_timeout(350)
        count = await page.locator('.sheet').count()
        if count != 40:
            raise RuntimeError(f'PAGE_COUNT={count}')
        await page.pdf(path=str(pdf), format='A5', print_background=True,
                       margin={'top':'0','right':'0','bottom':'0','left':'0'})
        await browser.close()
    return pdf


def write_manifest(out: Path, pages: dict[int, PageSource]):
    manifest = out / 'JILID-2-RECOVERY-MANIFEST.tsv'
    lines = ['page\torigin\tpath\tname']
    for n in range(1, 41):
        s = pages.get(n)
        if s:
            lines.append(f'P{n:03d}\t{s.origin}\t{s.path}\t{s.name}')
        else:
            lines.append(f'P{n:03d}\tMISSING\t\t')
    manifest.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    return manifest


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output-dir', default=str(DEFAULT.relative_to(ROOT)))
    ap.add_argument('--font-file')
    ap.add_argument('--font-zip')
    ap.add_argument('--amiri-font')
    args = ap.parse_args()

    out = Path(args.output_dir)
    out = out if out.is_absolute() else ROOT / out
    out.mkdir(parents=True, exist_ok=True)

    source_pages, current, recovery = merged_sources()
    missing = [n for n in range(1, 41) if n not in source_pages]
    manifest = write_manifest(out, source_pages)
    if missing:
        raise RuntimeError('RECOVERY_INCOMPLETE_MISSING=' + ','.join(f'P{x:03d}' for x in missing) + f' MANIFEST={manifest.relative_to(ROOT)}')

    kfg, _ = kfgloader.discover_font(args.font_file, args.font_zip, out)
    amiri = sukunlab.discover_amiri(args.amiri_font, out)
    hybrid = out / '_runtime_font' / 'KFGQPC-QURBATA-REVIEW-FROZEN-SUKUN.ttf'
    sukunlab.patch_font(kfg, amiri, hybrid, -1700)

    html_path = out / 'QURBATA-JILID-2-FULL-REVIEW-RECOVERED.html'
    html_path.write_text(build(source_pages, hybrid.resolve().as_uri()), encoding='utf-8')
    pdf = asyncio.run(render(html_path, out))

    current_used = sum(1 for s in source_pages.values() if s.origin == 'CURRENT_BRANCH')
    recovered_used = 40 - current_used
    print('QURBATA_JILID2_FULL_REVIEW_RECOVERED=PASS')
    print('TOTAL_PAGES=40')
    print(f'CURRENT_BRANCH_PAGES={current_used}')
    print(f'HISTORICAL_RECOVERY_PAGES={recovered_used}')
    print(f'RECOVERY_BASELINE={RECOVERY_COMMIT}')
    print('MISSING=NONE')
    print('ARTIFACT=REVIEW_PROOF_NOT_FINAL_PRINT')
    print(f'MANIFEST={manifest.relative_to(ROOT)}')
    print(f'PDF={pdf.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
