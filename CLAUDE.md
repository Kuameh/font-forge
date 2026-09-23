# Font Forge — agent notes

Read `docs/README.md` and `docs/pitfalls.md` first. This repo follows the ADR contract: a meaningful decision → a new immutable ADR in `docs/decisions/`; a changed pipeline or invariant → the matching `docs/systems/` doc, in the same change; a mistake → a row in `docs/pitfalls.md`.

- Sources are UFO + designspace (ADR-0002). Never re-run a scaffold script over existing UFOs.
- Build only via `make build` / `scripts/build.py` (ADR-0003). Commit `fonts/` and `specimen/` with the source change (ADR-0004).
- Verify by `make serve` and driving every axis slider in `specimen/`, not just a clean build.
- `specimen/index.html` is generated. Edit `scripts/specimen.template.html`.
