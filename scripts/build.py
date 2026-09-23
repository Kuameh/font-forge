"""Build every family in sources/ (or the ones named) into fonts/<slug>/.

Usage: python scripts/build.py [FamilyDir ...]
Owns the output layout described in docs/systems/build.md.
"""
import shutil
import subprocess
import sys
import tomllib
from pathlib import Path

from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "sources"
FONTS = ROOT / "fonts"


def fontmake(designspace, out_dir, *args):
    out_dir.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [sys.executable, "-m", "fontmake", "-m", str(designspace), "--output-dir", str(out_dir), *args],
        check=True,
    )


def build_family(family_dir):
    meta = tomllib.loads((family_dir / "family.toml").read_text())
    [designspace] = family_dir.glob("*.designspace")
    out = FONTS / meta["slug"]
    shutil.rmtree(out, ignore_errors=True)
    print(f"==> {meta['name']} -> {out.relative_to(ROOT)}")

    fontmake(designspace, out / "variable", "-o", "variable")
    fontmake(designspace, out / "ttf", "-i", "-o", "ttf", "--autohint")
    fontmake(designspace, out / "otf", "-i", "-o", "otf")

    webfonts = out / "webfonts"
    webfonts.mkdir()
    for src in [*(out / "variable").glob("*.ttf"), *(out / "ttf").glob("*.ttf")]:
        font = TTFont(src)
        font.flavor = "woff2"
        font.save(webfonts / src.with_suffix(".woff2").name)

    shutil.copy(family_dir / "family.toml", out / "family.toml")
    shutil.rmtree(family_dir / "instances", ignore_errors=True)  # fontmake's interpolated UFOs, not sources


def main():
    names = sys.argv[1:]
    dirs = [SOURCES / n for n in names] if names else sorted(p.parent for p in SOURCES.glob("*/family.toml"))
    for d in dirs:
        build_family(d)


if __name__ == "__main__":
    main()
