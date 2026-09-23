"""Generate specimen/index.html from what is in fonts/ — never from sources/.

The specimen shows exactly what a user would download. Owned by docs/systems/specimen.md.
"""
import hashlib
import json
import tomllib
from pathlib import Path

from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent.parent
FONTS = ROOT / "fonts"
OUT = ROOT / "specimen" / "index.html"


def gsub_features(font):
    """Feature tags in GSUB, each with the ligatures it forms as (input text, output glyph) pairs."""
    if "GSUB" not in font:
        return []
    gsub = font["GSUB"].table
    char_of = {name: chr(code) for code, name in font.getBestCmap().items()}
    features = {}
    for rec in gsub.FeatureList.FeatureRecord:
        entry = features.setdefault(rec.FeatureTag, {"tag": rec.FeatureTag, "ligatures": []})
        for index in rec.Feature.LookupListIndex:
            lookup = gsub.LookupList.Lookup[index]
            for sub in lookup.SubTable:
                sub = sub.ExtSubTable if lookup.LookupType == 7 else sub
                for first, ligs in getattr(sub, "ligatures", {}).items():
                    for lig in ligs:
                        names = [first, *lig.Component]
                        if all(n in char_of for n in names):
                            entry["ligatures"].append({"text": "".join(char_of[n] for n in names), "glyph": lig.LigGlyph})
    for entry in features.values():
        seen = {}
        for lig in entry["ligatures"]:
            seen.setdefault(lig["glyph"], lig)   # one example per ligature glyph; class rules expand to many inputs
        entry["ligatures"] = list(seen.values())
    return list(features.values())


def family_data(family_out):
    meta = tomllib.loads((family_out / "family.toml").read_text())
    # Single-master families have no variable font (ADR-0008); preview their first static instead.
    [vf, *_] = sorted((family_out / "variable").glob("*.ttf")) or sorted((family_out / "ttf").glob("*.ttf"))
    font = TTFont(vf)
    axes = [
        {"tag": a.axisTag, "min": a.minValue, "default": a.defaultValue, "max": a.maxValue}
        for a in (font["fvar"].axes if "fvar" in font else [])
    ]
    name = font["name"]
    instances = (
        [{"name": name.getDebugName(i.subfamilyNameID), "coords": i.coordinates} for i in font["fvar"].instances]
        if "fvar" in font
        else [{"name": name.getDebugName(2), "coords": {}}]
    )
    chars = sorted(c for c in font.getBestCmap() if c > 0x20)
    woff2 = family_out / "webfonts" / vf.with_suffix(".woff2").name
    # Content hash in the URL: a rebuilt font gets a new URL, so browsers never show a cached old build.
    webfont = f"../fonts/{family_out.name}/webfonts/{woff2.name}?v={hashlib.sha256(woff2.read_bytes()).hexdigest()[:10]}"
    downloads = {
        kind: [f"../fonts/{family_out.name}/{kind}/{p.name}" for p in sorted((family_out / kind).glob("*"))]
        for kind in ("variable", "ttf", "otf", "webfonts")
        if (family_out / kind).is_dir()
    }
    return {**meta, "axes": axes, "instances": instances, "features": gsub_features(font), "chars": "".join(map(chr, chars)), "webfont": webfont, "downloads": downloads}


def main():
    families = [family_data(p.parent) for p in sorted(FONTS.glob("*/family.toml"))]
    template = (ROOT / "scripts" / "specimen.template.html").read_text()
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(template.replace("/*FAMILIES*/[]", json.dumps(families, ensure_ascii=False).replace("</", "<\\/")))
    print(f"wrote {OUT.relative_to(ROOT)} ({len(families)} families)")


if __name__ == "__main__":
    main()
