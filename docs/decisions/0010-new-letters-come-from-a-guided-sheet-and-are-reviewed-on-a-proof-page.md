# ADR-0010 — New letters come from a guided drawing sheet and are reviewed on a proof page

- **Status**: Accepted
- **Date**: 2026-09-23

## Context

Noble Hand was traced from a free-form handwriting sheet. With no guidelines, every letter's baseline and height had to be guessed while tracing, and nobody could see alignment problems until the font was built. People who can't use a font editor need a way to (1) give Claude letters that are already aligned and (2) judge the alignment of the result.

Options for input: a free-form sheet (what happened before, alignment guessed), a **printable sheet with guidelines and one labelled box per character**, or drawing in the browser (mouse drawing looks worse than pen on paper, and it's more to build). Options for review: a **proof page where the person marks each glyph OK or Fix and pastes the result to Claude**, or drag-to-adjust in the browser (more to build, and changes still have to be written into the UFO by someone).

## Decision

`sheet/index.html` is a static, printable page. It draws one box per requested character, plus double-width boxes for ligatures, with ascender 800, cap height 700, x-height 500, baseline 0 and descender −250 on a 1000-unit em, plus a label above each box and alignment marks in the corners. The character list, ligatures, family name and paper size come from the form or URL parameters. When tracing, box coordinates map 1:1 onto UFO coordinates. `scripts/proof.py` generates `specimen/proof.html` from the built TTFs. It draws every glyph, ligatures included, as an outline on the font's own metric lines and side bearings, at one shared scale per family, with spacing strips. Each glyph has OK/Fix buttons with a note. **Copy review** turns the marks into text for Claude, who makes the fixes in the UFO. The workflow is described in `docs/systems/drawing-workflow.md`.

## Consequences

- Traced letters start aligned, and a person can judge alignment without a font editor.
- Review marks are stored in the reviewer's browser (localStorage) and only leave it through **Copy review**, so two reviewers don't see each other's marks.
- The sheet's metrics are fixed. A family with other proportions (Noble Hand's x-height is 560) still traces fine, but the metrics in its UFO then differ from the sheet's and must be set deliberately.
- The proof page reads built fonts, so it goes stale like the specimen if `fonts/` isn't rebuilt (pitfall #6).
