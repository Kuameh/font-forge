# Build

How sources become fonts today. Decisions behind it: [ADR-0002](../decisions/0002-ufo-and-designspace-are-the-only-font-sources.md), [0003](../decisions/0003-fontmake-builds-every-family-through-one-script.md), [0004](../decisions/0004-built-fonts-are-committed-to-the-repository.md), [0005](../decisions/0005-every-family-ships-variable-and-static-builds.md).

## Inputs

```
sources/<FamilyName>/
  <FamilyName>.designspace     axes, masters, named instances
  <FamilyName>-<Style>.ufo/    one per master (UFO 3)
  family.toml                  name, slug, status, designers, description, sample
```

A directory is a family if and only if it contains `family.toml`.

## Pipeline — `scripts/build.py`

For each family (all, or those passed as arguments / `make build FAMILY=X`):

1. Delete `fonts/<slug>/` so removed styles don't linger.
2. `fontmake -o variable` → `variable/<Family>-VF.ttf` (overlaps kept, flagged — correct for variable TTFs).
3. `fontmake -i -o ttf --autohint` → `ttf/` one per named instance, overlaps removed, ttfautohint applied.
4. `fontmake -i -o otf` → `otf/` one per named instance (CFF outlines).
5. woff2-compress the variable and every static TTF → `webfonts/`.
6. Copy `family.toml` into `fonts/<slug>/`; delete `sources/<Family>/instances/`.

Then `make build` runs `scripts/specimen.py` ([specimen.md](specimen.md)).

## Toolchain

`requirements.txt` (pinned) into `.venv` via `make setup`: fontmake, fontTools, ufo2ft, ufoLib2, glyphsLib, skia-pathops (overlap removal), ttfautohint-py (hinting, bundled binary), brotli (woff2). Python ≥ 3.11 (`tomllib`).

## CI

`.github/workflows/build.yml` runs `make setup && make build` on every push and PR, and uploads `fonts/` as an artifact.

`.github/workflows/pages.yml` publishes the committed `fonts/` and `specimen/` (it doesn't rebuild them) to GitHub Pages on every push to `main`: https://kuameh.github.io/font-forge/specimen/

## Gaps

- Nothing checks that committed `fonts/` match `sources/`. Builds aren't byte-reproducible yet (timestamps), so a diff check would always fail. Fix: pin `SOURCE_DATE_EPOCH` and add a `git diff --exit-code fonts specimen` step.
- No quality checks (fontbakery, outline checks) run yet.
- Only a `wght` axis has been exercised. Other axes should work through fontmake but are untested here.
