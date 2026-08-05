# QURBATA Arabic Engine (QAE)

QAE controls educational Arabic typography independently from the font's built-in harakat positioning.

## v1.0 production scope

- Jilid 1 only.
- Isolated Arabic letters only.
- Initial supported letters: `ب`, `ت`, `ث`.
- Initial supported mark: fathah.
- Base glyph: Amiri Quran.
- Fathah: a QURBATA-owned CSS shape, not a combining Unicode glyph.

## Rendering contract

1. Page YAML remains Unicode-friendly (`بَ`, `تَ`, `ثَ`).
2. QAE decomposes every token into base letter and mark.
3. The base letter is rendered by Amiri Quran without its combining mark.
4. The mark is drawn independently.
5. Per-letter anchors determine mark position and scale.
6. PDF and PNG are generated automatically by GitHub Actions.

## Files

- `anchors/jilid-1-fathah.yaml`: production anchors for Jilid 1.
- `tools/qae.py`: parser and page-enrichment engine.

Later marks and connected forms must be added only when their QURBATA competency stage requires them.