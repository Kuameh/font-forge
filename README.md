# Font Forge

Open-source font families, built from editable sources, with a live specimen.

## See the fonts

Online: **https://kuameh.github.io/font-forge/specimen/**

Locally:

```sh
make setup   # once
make serve   # then open http://localhost:8000/specimen/
```

| Page | What it's for |
|---|---|
| [Specimen](https://kuameh.github.io/font-forge/specimen/) | Type in any family, try weights and ligatures, download. |
| [Alignment proof](https://kuameh.github.io/font-forge/specimen/proof.html) | Every glyph on its baseline, x-height and cap lines. Mark OK/Fix, then paste the review to Claude. |
| [Drawing sheet](https://kuameh.github.io/font-forge/sheet/) | Print, draw one letter per box, scan: the starting point for a new family. |

Built fonts are already committed under [`fonts/`](fonts/), so you don't need to build to use them. Each family has:

| Folder | Use it for |
|---|---|
| `variable/` | One file with every weight (a slider). Modern apps and the web. Multi-weight families only. |
| `ttf/` | One hinted file per weight. Windows, Office, older apps. |
| `otf/` | One file per weight, CFF outlines. Print and design apps. |
| `webfonts/` | woff2 for `@font-face`. |

## Families

| Family | Status | Axes |
|---|---|---|
| [Forge Demo](sources/ForgeDemo/) | Draft (pipeline demo, 9 caps, TT/FF/LT ligatures) | wght 300–800 |
| [Noble Hand](sources/NobleHand/) | Draft (handwriting, A–Z a–z 0–9, basic punctuation, ff/ft/tt ligatures) | none (one weight) |
| [El Display](sources/ElDisplay/) | Draft (unicase display, A–Z 0–9, punctuation, Le/LL/Lo ligatures via `dlig`) | none (one weight) |

## Build

```sh
make build                     # every family, then the specimen
make build FAMILY=ForgeDemo    # one family
```

## Layout

```
sources/<Family>/   UFO masters + .designspace + family.toml   ← edit these
fonts/<slug>/       built output, committed                    ← generated
specimen/           gallery + alignment proof                  ← generated
scripts/            build.py, specimen.py, proof.py + their templates
sheet/              printable drawing sheet (static)
docs/               decisions (ADRs), systems, pitfalls
```

Contributing: [CONTRIBUTING.md](CONTRIBUTING.md). Why things are this way: [docs/](docs/README.md).

## License

Fonts: [SIL Open Font License 1.1](OFL.txt). Code: [MIT](LICENSE).
