# Specimen

The gallery at `specimen/index.html`. Decision: [ADR-0007](../decisions/0007-the-specimen-is-generated-from-built-fonts.md).

- `scripts/specimen.py` reads every `fonts/*/family.toml` and that family's variable TTF (axes via `fvar`, character set via `cmap`), then injects a JSON list into `scripts/specimen.template.html`. Single-master families (ADR-0008) have no variable font, so it previews their first static TTF instead, with no axis sliders; download columns appear only for folders that exist.
- Per family, the page shows: name, Draft badge when `status = "draft"`, description + designers, its own **Type to preview** input with **Reset** (empty falls back to the family's `sample`), the preview text large, one slider per variable axis plus a size slider, one checkbox per GSUB feature the font has (named for common tags — *Standard ligatures*, *Discretionary ligatures*, *Contextual alternates* — otherwise by tag; liga/calt/kern etc. start on, dlig and the rest off, matching apps), a **Ligatures** list showing every ligature formed with its feature tag ([ADR-0009](../decisions/0009-ligatures-live-in-each-ufos-feature-file.md)), a **Weights** list rendering the text in every named instance from `fvar` (omitted for single-style families, ADR-0008, where the tester already shows the only style), a collapsible character set grid, and download links for every file in `fonts/<slug>/`.
- Text is painted so supported characters stay in one text run: ligatures and contextual rules form across them.
- Characters the font doesn't encode render in the fallback UI font, muted with a dotted accent underline, and are listed as "Not in this font yet", so a missing glyph never passes for part of the design.
- Fonts load from `../fonts/<slug>/webfonts/*-VF.woff2` (or the static woff2 for single-master families) via the `FontFace` API, with `?v=<sha256 prefix>` appended so a rebuilt font never shows from browser cache, so the page must be served over HTTP (`make serve` → http://localhost:8000/specimen/) or GitHub Pages (https://kuameh.github.io/font-forge/specimen/, deployed by `.github/workflows/pages.yml`). Opening it with `file://` blocks the fonts.
- UI colours and spacing are CSS custom properties on `:root`, with a dark theme through `prefers-color-scheme`. The UI font is Inter from Google Fonts.

## Gaps

- Weights are previewed through the variable font at each instance's coordinates, not the static binaries themselves.
- No waterfall or paragraph views.
