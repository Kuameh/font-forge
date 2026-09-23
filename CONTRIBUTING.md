# Contributing

## Before you start

1. Read [docs/pitfalls.md](docs/pitfalls.md). It's short.
2. `make setup` (Python 3.11+). Everything installs into `.venv`, nothing global.

## Editing an existing family

1. Open the UFOs in `sources/<Family>/` with any UFO editor: [Fontra](https://fontra.xyz) (free, browser), Glyphs, RoboFont or FontForge.
2. Change **every master** the same way (same contours, points, order). See pitfall #2.
3. `make build FAMILY=<Family>`, then `make serve`. Drag every axis slider end to end and look for twisting or broken shapes.
4. Commit sources, `fonts/` and `specimen/` together.

## Adding a family

1. Create `sources/<FamilyName>/` with at least two compatible UFO 3 masters, a `<FamilyName>.designspace` (axes, masters, named instances; the default must sit on a master) and `family.toml`. A one-weight family is a single UFO with no designspace instead ([ADR-0008](docs/decisions/0008-single-master-families-ship-static-fonts-only.md)). Copy the fields from `sources/ForgeDemo/family.toml`.
2. Set in each UFO's font info: family and style name, `unitsPerEm`, vertical metrics, and the OFL licence + URL.
3. Add yourself to `AUTHORS.txt`, and add the family to the table in `README.md`.
4. Build, check the specimen, commit.

## Decisions

If your change picks between real alternatives (a new axis convention, a new output format, a change to the build), add an ADR in `docs/decisions/` using `TEMPLATE.md` and link it from `docs/README.md` in the same PR. Never edit an accepted ADR. Supersede it instead. If something bit you, add a row to `docs/pitfalls.md`.

## Review checklist

- [ ] All masters still interpolate (specimen sliders look right end to end)
- [ ] `fonts/` and `specimen/` rebuilt in this change
- [ ] Docs, ADRs and pitfalls updated where relevant, and indexed in `docs/README.md`
