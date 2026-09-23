# ADR-0005 — Every family ships a variable font and static instances

- **Status**: Accepted
- **Date**: 2026-09-23

## Context

Variable fonts (one file, continuous axes such as weight) are what the web and modern apps want. Static fonts (one file per named weight) are still what Office, older design tools and some print workflows need.

Options: variable only (smallest, breaks older apps); static only (loses the axis); both.

## Decision

Every family has at least two masters and ships both: `variable/` (one TTF with every axis) and statics for every named instance in the designspace as `ttf/` (autohinted) and `otf/` (CFF), plus `webfonts/` woff2 of each. `scripts/build.py` owns this list.

## Consequences

- Users always find a format that works.
- Designers maintain at least two compatible masters — every glyph needs the same contours, points and order in each (see `docs/pitfalls.md`).
- A single-master family doesn't fit; supporting one would need a new ADR.
