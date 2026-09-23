# ADR-0004 — Built fonts are committed to the repository under fonts/

- **Status**: Accepted
- **Date**: 2026-09-23

## Context

People who don't build — designers trying a family, developers wanting a woff2 — must be able to see and download current fonts.

Options: (a) never commit binaries, publish via GitHub Releases or CI artifacts — clean history, but nothing is browsable without a release step and the specimen can't be served from the repo; (b) **commit `fonts/`** — the Google Fonts convention; the specimen and downloads work straight from a clone or GitHub Pages; (c) commit only woff2 — half-measure, desktop users still need to build.

## Decision

`make build` writes `fonts/<slug>/{variable,ttf,otf,webfonts}/` plus a copy of `family.toml`, and those files are committed in the same change as the source edit that produced them.

## Consequences

- Clone → open `specimen/index.html` → download. No toolchain needed to *use* the fonts.
- History grows with binaries (tens of KB per family today; fine at this scale, reconsider past ~50 MB).
- `fonts/` can drift from `sources/` if someone forgets to rebuild. Nothing enforces this yet — see Gaps in `docs/systems/build.md`.
