# ADR-0001 — Decisions are recorded as numbered, immutable ADRs

- **Status**: Accepted
- **Date**: 2026-09-23

## Context

Font Forge is meant to take contributors beyond its founder. Choices about source formats, naming, licensing and build output are hard to reverse once fonts ship, and a newcomer can't reconstruct why they were made from the files alone.

Options: (a) no written record, decisions live in chat and PR threads — lost on the first handover; (b) one growing `DECISIONS.md` — cheap, but entries get silently rewritten and the history of *why* disappears; (c) one numbered Architecture Decision Record per decision, never edited after acceptance, superseded by a new record when the decision changes.

## Decision

Record every choice between real alternatives as `docs/decisions/NNNN-<the-decision-as-a-sentence>.md` using the template in `docs/decisions/TEMPLATE.md`. Accepted ADRs are immutable: a changed decision gets a new ADR that supersedes the old one, linked both ways. How things work *today* lives in `docs/systems/`; mistakes worth not repeating live in `docs/pitfalls.md`. `docs/README.md` indexes all three — a doc missing from the index does not exist.

## Consequences

- A contributor can answer "why is it like this?" without asking anyone.
- Every meaningful change carries a writing cost, and a superseded ADR stays in the tree as history.
- The index in `docs/README.md` is maintained by hand in the same change as the ADR; reviewers check it.

## Notes

"Nothing was decided, code just got written" needs no ADR. Don't manufacture them.
