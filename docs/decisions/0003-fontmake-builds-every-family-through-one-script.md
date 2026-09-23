# ADR-0003 — fontmake builds every family through one script

- **Status**: Accepted
- **Date**: 2026-09-23

## Context

Sources have to become installable fonts the same way on every contributor's machine and in CI.

Options: (a) hand-rolled fontTools `FontBuilder` code — full control, but reimplements overlap removal, interpolation, feature compilation and naming that already exist; (b) FontForge scripting — an extra native install and a second source model; (c) **fontmake** (fontTools + ufo2ft + skia-pathops + ttfautohint-py), the reference UFO/designspace compiler; (d) gftools builder — fontmake plus Google Fonts post-processing, more than this project needs before it targets Google Fonts.

## Decision

`scripts/build.py` is the only build path. It discovers families by `sources/*/family.toml`, calls fontmake for each output, and is invoked through `make build`. The toolchain is pinned in `requirements.txt` and installed into `.venv` by `make setup` — pure pip, no Homebrew or native installs, so Linux/Windows/CI get the same binaries (`ttfautohint-py` bundles ttfautohint).

## Consequences

- One command per machine; no per-contributor tool drift.
- fontmake's defaults (naming, overlap handling) become ours; overriding them means changing the script, not a family.
- Upgrading a pinned tool can change every binary; do it in its own change and rebuild everything.

## Notes

gftools builder is the natural successor if a family is ever submitted to Google Fonts — that would be a new ADR superseding this one.
