"""Generate specimen/index.html from what is in fonts/ — never from sources/.

The specimen shows exactly what a user would download. Owned by docs/systems/specimen.md.
"""
import html
import json
import tomllib
from pathlib import Path

from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent.parent
FONTS = ROOT / "fonts"
OUT = ROOT / "specimen" / "index.html"


def family_data(family_out):
    meta = tomllib.loads((family_out / "family.toml").read_text())
    [vf] = (family_out / "variable").glob("*.ttf")
    font = TTFont(vf)
    axes = [
        {"tag": a.axisTag, "min": a.minValue, "default": a.defaultValue, "max": a.maxValue}
        for a in font["fvar"].axes
    ]
    chars = sorted(c for c in font.getBestCmap() if c > 0x20)
    webfont = f"../fonts/{family_out.name}/webfonts/{vf.with_suffix('.woff2').name}"
    downloads = {
        kind: [f"../fonts/{family_out.name}/{kind}/{p.name}" for p in sorted((family_out / kind).glob("*"))]
        for kind in ("variable", "ttf", "otf", "webfonts")
    }
    return {**meta, "axes": axes, "chars": "".join(map(chr, chars)), "webfont": webfont, "downloads": downloads}


def main():
    families = [family_data(p.parent) for p in sorted(FONTS.glob("*/family.toml"))]
    template = (ROOT / "scripts" / "specimen.template.html").read_text()
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(template.replace("/*FAMILIES*/[]", json.dumps(families, ensure_ascii=False).replace("</", "<\\/")))
    print(f"wrote {OUT.relative_to(ROOT)} ({len(families)} families)")


if __name__ == "__main__":
    main()
