# ADR-0008 — Single-master families ship static fonts only

- **Status**: Accepted
- **Date**: 2026-09-23
- **Supersedes / Extends / Constrained by**: Supersedes ADR-0005 *for single-master families only*: families with two or more masters still ship a variable font and statics. Narrows ADR-0002: a single-master family has no designspace; UFO remains the only source format.

## Context

Noble Hand is traced from one handwriting sheet: there is one weight and nothing to interpolate. ADR-0005 requires at least two masters and a variable font, and says a single-master family needs a new ADR.

Options:
- **Synthesize a second master** (offset every point along its normal) to get a weight axis. Keeps ADR-0005, but invents a design nobody drew, and tight counters (e, a, 8) fill in at the heavy end.
- **One-master designspace**. fontmake can take it, but a variable font with no axis is meaningless, and a designspace with no axes only adds a file.
- **A lone UFO with no designspace, built to static fonts only.** Honest to the source; the build needs to tell the two kinds of family apart.

## Decision

A family directory holding `family.toml` and exactly one `.ufo` (no `.designspace`) is a single-master family. `scripts/build.py` builds it with `fontmake -u` into `ttf/` (autohinted), `otf/` and `webfonts/`, and writes no `variable/`. `scripts/specimen.py` previews such a family from its first static TTF and shows no axis sliders. A family with a designspace is unchanged: ADR-0005 still applies to it.

## Consequences

- Handwriting and other one-off designs can join without faking a weight axis.
- Such families have one weight; users who want Bold get the app's faux bold.
- Adding a weight later means drawing a second compatible master and a designspace, and the family then falls under ADR-0005.
- `build.py` and `specimen.py` each carry a branch for the no-designspace case.

## Notes

Reference art a family was traced from (for example an SVG sheet) may live in `sources/<Family>/art/`. It is provenance, not a build input; the UFO is the source after the one-off import (ADR-0002).
