"""Generate specimen/proof.html: every glyph drawn on its metric lines, for alignment review.

Reads built fonts only (like specimen.py, ADR-0007). Owned by docs/systems/drawing-workflow.md.
"""
import json
import tomllib
from pathlib import Path

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent.parent
FONTS = ROOT / "fonts"
OUT = ROOT / "specimen" / "proof.html"


def style_data(path):
    font = TTFont(path)
    glyphset = font.getGlyphSet()
    by_glyph = {}
    for code, name in font.getBestCmap().items():
        by_glyph.setdefault(name, chr(code))
    glyphs = []
    for name in font.getGlyphOrder():
        if name == ".notdef" or name not in glyphset:
            continue
        svg, bounds = SVGPathPen(glyphset), BoundsPen(glyphset)
        glyphset[name].draw(svg)
        glyphset[name].draw(bounds)
        glyphs.append({
            "name": name,
            "char": by_glyph.get(name),
            "advance": glyphset[name].width,
            "d": svg.getCommands(),
            "bounds": [round(v) for v in bounds.bounds] if bounds.bounds else None,
        })
    os2, hhea = font["OS/2"], font["hhea"]
    return {
        # Typographic subfamily (ID 17) when set: a static "Light" is otherwise named "Regular" in ID 2.
        "style": font["name"].getDebugName(17) or font["name"].getDebugName(2),
        "weight": os2.usWeightClass,
        "upm": font["head"].unitsPerEm,
        "metrics": {
            "ascender": hhea.ascent, "cap": os2.sCapHeight, "x": os2.sxHeight,
            "baseline": 0, "descender": hhea.descent,
        },
        "glyphs": glyphs,
    }


def family_data(family_out):
    meta = tomllib.loads((family_out / "family.toml").read_text())
    styles = sorted((style_data(p) for p in (family_out / "ttf").glob("*.ttf")), key=lambda s: s["weight"])
    return {"name": meta["name"], "slug": meta["slug"], "styles": styles}


def main():
    families = [family_data(p.parent) for p in sorted(FONTS.glob("*/family.toml"))]
    template = (ROOT / "scripts" / "proof.template.html").read_text()
    OUT.write_text(template.replace("/*FAMILIES*/[]", json.dumps(families, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")))
    print(f"wrote {OUT.relative_to(ROOT)} ({len(families)} families)")


if __name__ == "__main__":
    main()
