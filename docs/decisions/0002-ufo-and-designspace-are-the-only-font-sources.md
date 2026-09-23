# ADR-0002 — UFO masters plus a designspace are the only font sources

- **Status**: Accepted
- **Date**: 2026-09-23

## Context

Each family needs one editable source of truth that many people, using different tools, can change and review.

Options:
- **`.glyphs` files** — excellent editor, but Glyphs is Mac-only and paid; a single binary-ish plist makes diffs and merges painful.
- **FontForge `.sfd`** — free, but one monolithic file per master, and FontForge is not a tool most type designers use today.
- **Python scripts that draw glyphs** — how the first family was scaffolded; great for geometric designs, but closes the door on designers who work by eye, and makes the code the design.
- **UFO 3 masters + a `.designspace` file** — open, text-based (one `.glif` XML file per glyph, so diffs are per letter), edited by Fontra (free, browser), Glyphs, RoboFont and FontForge, and read natively by fontmake. The Google Fonts ecosystem standard.

## Decision

Every family lives in `sources/<FamilyName>/` as UFO 3 masters, one `<FamilyName>.designspace` describing axes, masters and named instances, and a `family.toml` holding metadata the designspace can't (slug, status, designers, description, sample text). Generator scripts may *scaffold* a family once; after that the UFOs are the source and the script is not committed or re-run.

## Consequences

- Anyone can contribute with free tools; reviewers see per-glyph diffs.
- Parametric families lose their parameters once scaffolded — a global change (say, stem width) becomes a manual edit in each master, or a new one-off script run deliberately and reviewed as a normal change.
- `sources/*/instances/` is fontmake output, not source; it is gitignored and deleted by the build.
