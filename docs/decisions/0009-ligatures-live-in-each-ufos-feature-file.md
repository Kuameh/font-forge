# ADR-0009 — Ligatures live in each UFO's feature file, and the designer picks liga or dlig

- **Status**: Accepted
- **Date**: 2026-09-23
- **Extends**: ADR-0002. It adds `features.fea` to what a UFO source holds, and it doesn't change which formats count as sources.

## Context

Families now have ligatures: TT, FF and LT in Forge Demo, ff, ft and tt in Noble Hand, and Le, LL and Lo in El Display. A ligature needs a glyph *and* an OpenType substitution rule that tells apps when to use it. There are also two kinds. Standard ligatures (`liga`) are on by default everywhere. Discretionary ligatures (`dlig`) only appear when the user turns them on.

Options:
- **Hand-written `features.fea` inside each UFO**: the UFO standard. fontmake compiles it and every UFO editor shows it. The rules sit next to the glyphs they use.
- **Generate the rules from glyph names** (`f_f` → `sub f f by f_f`). Less typing, but it hides the liga/dlig choice, can't express class rules (`sub [L l] [e E] by L_e`) and adds a tool of our own.
- **No OpenType rules, just glyphs**: people would have to pick ligatures from a glyph palette by hand, which most apps and every browser can't do.

## Decision

Each family writes its substitution rules in its UFO's `features.fea`. In a multi-master family, every master carries an identical copy. Ligature glyphs are unencoded and named by their components joined with underscores (`f_f`, `T_T`, `L_e`), following the Adobe Glyph List convention. The family's designer decides per ligature: `liga` for joins that should always happen, `dlig` for stylistic ones people opt into. `scripts/specimen.py` reads the compiled GSUB table. It shows one toggle per feature it finds, starting at the browser default (liga/calt on, dlig off), plus a Ligatures list that always shows each ligature formed. `scripts/proof.py` shows the ligature glyphs on the metric lines like any other glyph.

## Consequences

- Ligatures work in every app that supports OpenType, with no extra tooling.
- In multi-master families, the feature file is duplicated per master and can drift. fontmake uses the default master's copy, so an edit made only in another master is silently ignored (pitfall #11).
- Ligature glyphs are drawn and reviewed like any other glyph: in the sheet's wide boxes, then on the proof page.
- Ligatures the specimen can't turn back into text (a rule whose inputs have no Unicode) are left out of its Ligatures list, but still appear on the proof page.
