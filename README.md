# Font Forge

Open-source font families, built from editable sources, with a live specimen.

## See the fonts

Online: **https://kuameh.github.io/font-forge/specimen/**

Locally:

```sh
make setup   # once
make serve   # then open http://localhost:8000/specimen/
```

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
| [Forge Demo](sources/ForgeDemo/) | Draft (pipeline demo, 9 caps) | wght 300–800 |
| [Noble Hand](sources/NobleHand/) | Draft (handwriting, A–Z a–z 0–9, basic punctuation) | none (one weight) |

## Build

```sh
make build                     # every family, then the specimen
make build FAMILY=ForgeDemo    # one family
```

## Layout

```
sources/<Family>/   UFO masters + .designspace + family.toml   ← edit these
fonts/<slug>/       built output, committed                    ← generated
specimen/           generated gallery                          ← generated
scripts/            build.py, specimen.py, specimen template
docs/               decisions (ADRs), systems, pitfalls
```

Contributing: [CONTRIBUTING.md](CONTRIBUTING.md). Why things are this way: [docs/](docs/README.md).

## License

Fonts: [SIL Open Font License 1.1](OFL.txt). Code: [MIT](LICENSE).
