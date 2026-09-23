# ADR-0006 — Fonts are licensed under the SIL Open Font License 1.1

- **Status**: Accepted
- **Date**: 2026-09-23

## Context

Contributors need to know what they're giving, users what they may do.

Options: (a) OFL 1.1 — the standard for open fonts; free use, embedding and modification, but fonts can't be sold on their own and derivatives must stay OFL; (b) Apache 2.0 / MIT — software licenses that don't address font-specific issues like embedding or renaming; (c) proprietary/commercial — possible later for specific families, incompatible with open contribution.

## Decision

All fonts are OFL 1.1 (`OFL.txt`), copyright "The Font Forge Project Authors" (`AUTHORS.txt`). No Reserved Font Names for now. Build scripts and tooling are MIT (`LICENSE`). Each UFO's `info` carries the licence and URL, so built fonts embed it.

## Consequences

- Anyone can use, embed and fork the fonts; contributions are legally clear.
- No family from this repo can later be sold as a standalone commercial font by us or anyone.
- Without a Reserved Font Name, a modified fork may keep the same family name.
