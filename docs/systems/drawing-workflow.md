# Drawing workflow

How someone who doesn't use a font editor gets letters into a family and checks them. Decision: [ADR-0010](../decisions/0010-new-letters-come-from-a-guided-sheet-and-are-reviewed-on-a-proof-page.md).

1. **Sheet.** Open `sheet/` (`make serve` → http://localhost:8000/sheet/, or on Pages). Set the family name, designer, characters and ligatures (comma separated), choose A4 or Letter, then **Print**. The settings are kept in the URL, so a link reproduces the same sheet.
2. **Draw.** One character per box, with the same pen throughout, sitting on the orange baseline. Ligature boxes are double width: draw the letters joined.
3. **Scan.** 300 dpi, or a flat daylight photo showing all four corner marks.
4. **Trace (Claude).** Straighten the scan using the corner marks. Each box's guidelines map 1:1 onto font units (UPM 1000: ascender 800, cap 700, x-height 500, baseline 0, descender −250). Glyphs are written straight into the UFO, which is the source from then on (ADR-0002). The import script is a one-off and isn't committed.
5. **Build.** `make build FAMILY=<Dir>`, which also regenerates `specimen/index.html` and `specimen/proof.html`.
6. **Proof.** Open `specimen/proof.html`. Pick a family and style, check the spacing strips (HOH/non control strings, or your own words) and each glyph on its metric lines, and mark it **OK** or **Fix** with a note. **Copy review** produces text to paste to Claude, who applies the fixes and rebuilds. Repeat until everything is OK.

## Proof page details

- `scripts/proof.py` reads every static TTF in `fonts/<slug>/ttf/`. For each glyph in glyph order (except `.notdef`) it writes SVG path data, advance and bounds, plus metrics from `hhea` (ascender/descender) and `OS/2` (cap height, x-height). Style names use name ID 17, falling back to ID 2.
- Glyphs are drawn from outlines, not text, so the proof shows exactly what's in the font, including unencoded glyphs (ligatures, `.alt`s). Cards have a fixed height and a width taken from each glyph, so one scale holds across the family.
- Spacing strips lay glyphs out by advance width only. They show no kerning and no ligatures, which isolates spacing.
- Marks are stored in `localStorage` under `proof:<slug>:<style>`, per browser.

## Gaps

- The sheet's metrics can't be changed from the page. A family with different proportions draws on the defaults.
- Tracing is done by Claude per request. There is no committed import tool.
- No kerning review.
