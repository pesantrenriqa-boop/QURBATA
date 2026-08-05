# QURBATA Jilid 1 — Source, Layout, and Render

## Single source of truth

Do not edit generated PDF or PNG files.

Edit only:

1. `data/page-XXX.yaml` for lesson content.
2. `layout/master-layout-v1.css` for the visual system shared by all pages.
3. `templates/page.html.j2` only when the page structure changes.

## Automatic outputs

Every push affecting the book runs `.github/workflows/render-qurbata-books.yml`.

The workflow generates:

- `dist/jilid-1/QURBATA-JILID-1.pdf` — print master.
- `dist/jilid-1/png/page-XXX.png` — review previews.
- `dist/jilid-1/html/page-XXX.html` — browser proof.

The files are delivered as the GitHub Actions artifact `QURBATA-JILID-1-render`.

## Revision behavior

- Change one page YAML: only that page's content changes, then the whole PDF is rebuilt.
- Change master CSS: all pages are restyled automatically.
- Change the template: all pages are restructured automatically.
- Add `page-002.yaml`: the next build automatically adds page 2 to PDF and PNG outputs.

## Frozen page rule for Jilid 1

- One displayed slot equals one learning object.
- An object contains one, two, or three separate letters.
- Two-letter and three-letter objects are not connected letterforms.
- Page 1 uses fathah only.
- No QR code in the master layout.
- Material remains visually dominant; supporting information stays small.

## Local render

```bash
python -m pip install -r requirements-render.txt
playwright install chromium
python tools/render_qurbata.py
```
