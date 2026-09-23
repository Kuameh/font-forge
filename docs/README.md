# Docs

Start here. A doc not linked from this page doesn't exist.

- **[Pitfalls](pitfalls.md)**: read before your first change.
- **Decisions** (`decisions/`): immutable, numbered. Change a decision by writing a new ADR that supersedes the old one ([template](decisions/TEMPLATE.md)).
- **Systems** (`systems/`): how things work *today*. Update them in the same change as the code.

## Decisions

| # | Decision |
|---|---|
| [0001](decisions/0001-decisions-are-recorded-as-numbered-adrs.md) | Decisions are recorded as numbered, immutable ADRs |
| [0002](decisions/0002-ufo-and-designspace-are-the-only-font-sources.md) | UFO masters plus a designspace are the only font sources |
| [0003](decisions/0003-fontmake-builds-every-family-through-one-script.md) | fontmake builds every family through one script |
| [0004](decisions/0004-built-fonts-are-committed-to-the-repository.md) | Built fonts are committed to the repository under `fonts/` |
| [0005](decisions/0005-every-family-ships-variable-and-static-builds.md) | Every family ships a variable font and static instances |
| [0006](decisions/0006-fonts-are-licensed-under-the-sil-open-font-license.md) | Fonts are licensed under the SIL Open Font License 1.1 |
| [0007](decisions/0007-the-specimen-is-generated-from-built-fonts.md) | The specimen is generated from built fonts, not sources |
| [0008](decisions/0008-single-master-families-ship-static-fonts-only.md) | Single-master families are a lone UFO and ship static fonts only (supersedes 0005 for them) |
| [0009](decisions/0009-ligatures-live-in-each-ufos-feature-file.md) | Ligatures live in each UFO's feature file, and the designer picks liga or dlig |
| [0010](decisions/0010-new-letters-come-from-a-guided-sheet-and-are-reviewed-on-a-proof-page.md) | New letters come from a guided drawing sheet and are reviewed on a proof page |

## Systems

- [Build](systems/build.md): sources → `fonts/`
- [Specimen](systems/specimen.md): `fonts/` → `specimen/index.html`
- [Drawing workflow](systems/drawing-workflow.md): `sheet/` → tracing → `specimen/proof.html` review
