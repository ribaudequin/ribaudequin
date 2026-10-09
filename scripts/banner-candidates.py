#!/usr/bin/env python3
"""
Bandua Studio — banner variants C and D, for every platform.

Generates both candidate treatments at all five platform sizes, so they can be
uploaded side by side and judged in place. Seeing a banner in the actual profile
is the only test that settles it.

    python3 scripts/banner-candidates.py

Output:
    profiles/banners/c/<platform>-<w>x<h>.png   C — arc bleeding off the right
    profiles/banners/d/<platform>-<w>x<h>.png   D — arc bleed + pixel field

Both use the mark's own geometry as the only decoration: the arc enlarged and
bled off the edge (C), optionally with a sparse block field on the mark's grid
(D). No new shapes, no colours outside the palette.

Same rules as the main generator: integer block sizes on the UNIT=8 grid,
measured centring, rendered 1:1.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "profiles" / "banners"
WORK = ROOT / "profiles" / ".work-cand"

INKSCAPE = [
    "flatpak", "run", "--command=inkscape", "org.inkscape.Inkscape",
    "--export-type=png",
]

MIST = "#F2F5EE"
TEAL = "#1F5F66"
MOSS = "#5B7B3A"
DEEP = "#0F2A2E"

UNIT = 8
ARC_OUTER = (
    [(-20, -40), (-12, -40), (-4, -40), (4, -40), (12, -40), (20, -40)]
    + [(-28, -32), (28, -32)]
    + [(-36, -24), (36, -24)]
    + [(x, y) for y in (-16, -8, 0, 8, 16, 24) for x in (-40, 40)]
)
ARC_INNER = (
    [(-12, -24), (-4, -24), (4, -24), (12, -24)]
    + [(-20, -16), (20, -16)]
    + [(x, y) for y in (-8, 0, 8, 16) for x in (-24, 24)]
)
X0, Y0 = -40, -40
WB, HB = 11, 9

# Type scale, read from the brandboard's Main logo lockup (mark 144, word 28,
# STUDIO 12, tagline 11). Never invent these.
WORD_RATIO = 28.0 / 144.0
STUDIO_RATIO = 12.0 / 144.0
TAG_RATIO = 11.0 / 144.0

# Treatment constants
BLEED_OPACITY = 0.07        # C and D: the arc bleeding off the right edge
FIELD_OPACITY = 0.045       # D only: sparse block field
FIELD_STEP = 5              # field spacing, in mark blocks
MARK_H_FRACTION = 0.56      # mark height as a fraction of banner height

PLATFORMS = [
    ("github",   1280, 640),
    ("x",        1500, 500),
    ("linkedin", 1584, 396),
    ("patreon",  1600, 400),
    ("kofi",     1200, 400),
]


def block_for(h: int) -> int:
    """Mark block size — a multiple of UNIT — for a banner of height h."""
    raw = h * MARK_H_FRACTION / HB
    return max(UNIT, int(round(raw / UNIT)) * UNIT)


def mark_svg(cx: float, cy: float, block: int, fill: str, opacity: float = 1.0,
             indent: str = "  ") -> str:
    """The Pixel Arc. `block` must be a multiple of UNIT or the renderer
    anti-aliases the edges and the pixel grid is lost."""
    assert block % UNIT == 0, f"block must be a multiple of {UNIT}, got {block}"
    k = block // UNIT
    ox = round(cx - WB * block / 2) - X0 * k
    oy = round(cy - HB * block / 2) - Y0 * k
    opa = f' opacity="{opacity}"' if opacity != 1.0 else ""
    parts = [f'{indent}<g transform="translate({ox},{oy})"{opa}>']
    for blocks in (ARC_OUTER, ARC_INNER):
        parts.append(f'{indent}  <g fill="{fill}">')
        for x, y in blocks:
            parts.append(f'{indent}    <rect x="{x * k}" y="{y * k}" '
                         f'width="{block}" height="{block}"/>')
        parts.append(f"{indent}  </g>")
    parts.append(f"{indent}</g>")
    return "\n".join(parts)


def field_svg(w: int, h: int, block: int, fill: str, opacity: float,
              indent: str = "  ") -> str:
    """Sparse grid of blocks on the mark's own grid — texture in the brand's
    language rather than a new pattern."""
    step = block * FIELD_STEP
    parts = [f'{indent}<g fill="{fill}" opacity="{opacity}">']
    for y in range(0, h, step):
        for x in range(0, w, step):
            parts.append(f'{indent}  <rect x="{x}" y="{y}" width="{block}" height="{block}"/>')
    parts.append(f"{indent}</g>")
    return "\n".join(parts)


def text_svg(tx: float, h: int, mark_h: float) -> str:
    word = mark_h * WORD_RATIO
    studio = mark_h * STUDIO_RATIO
    tag = mark_h * TAG_RATIO
    lw, ls, lt = word * 1.35, studio * 1.7, tag * 1.6
    top = (h - (lw + ls + lt)) / 2
    y1 = top + word
    y2 = y1 + ls
    y3 = y2 + lt
    return f"""  <g font-family="Space Grotesk" fill="{MIST}">
    <text x="{tx:.0f}" y="{y1:.0f}" font-size="{word:.0f}" font-weight="700" letter-spacing="-0.02em">bandua</text>
    <text x="{tx:.0f}" y="{y2:.0f}" font-size="{studio:.0f}" font-weight="500" letter-spacing="0.34em" opacity="0.78">STUDIO</text>
    <text x="{tx:.0f}" y="{y3:.0f}" font-size="{tag:.0f}" font-weight="400" opacity="0.66">Things built to last.</text>
  </g>"""


def svg(w: int, h: int, body: str, title: str) -> str:
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" role="img" aria-label="{title}">\n'
            f"  <title>{title}</title>\n{body}\n</svg>\n")


def render(text: str, out_png: Path, w: int) -> None:
    WORK.mkdir(parents=True, exist_ok=True)
    src = WORK / (out_png.parent.name + "-" + out_png.stem + ".svg")
    src.write_text(text)
    subprocess.run(INKSCAPE + [f"--export-filename={out_png}", f"--export-width={w}", str(src)],
                   check=True, capture_output=True)


def measure_lockup(body_fn, w: int, h: int) -> int:
    """Ink width of the lockup, measured on a padded canvas. Never estimate it —
    an estimate left the lockup 5% off-centre."""
    margin = w // 4
    canvas = w + 2 * margin
    WORK.mkdir(parents=True, exist_ok=True)
    src = WORK / "_measure.svg"
    src.write_text(svg(canvas, h, body_fn(margin, canvas), "probe"))
    png = WORK / "_measure.png"
    subprocess.run(INKSCAPE + [f"--export-filename={png}", f"--export-width={canvas}", str(src)],
                   check=True, capture_output=True)
    bg = tuple(int(DEEP.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))
    with Image.open(png).convert("RGB") as im:
        px = im.load()
        xs = [x for y in range(0, im.height, 2) for x in range(0, im.width, 2)
              if px[x, y] != bg]
    return max(xs) - min(xs) + 1


def build(name: str, w: int, h: int, variant: str) -> Path:
    block = block_for(h)
    mark_w, mark_h = WB * block, HB * block
    gap = round(mark_h * 0.30)

    def lockup(offset: float) -> str:
        return (mark_svg(offset + mark_w / 2, h / 2, block, MIST) + "\n"
                + text_svg(offset + mark_w + gap, h, mark_h))

    def lockup_only(offset: float, canvas_w: int) -> str:
        """For measuring. The decoration must be excluded: the bleed mark is far
        wider than the lockup, and including it made the measured width larger
        than the canvas — which pushed the lockup off the left edge."""
        return (f'  <rect width="{canvas_w}" height="{h}" fill="{DEEP}"/>\n' + lockup(offset))

    def full_body(offset: float, canvas_w: int) -> str:
        parts = [f'  <rect width="{canvas_w}" height="{h}" fill="{DEEP}"/>']
        if variant == "d":
            parts.append(field_svg(canvas_w, h, block, MIST, FIELD_OPACITY))
        # the arc, enlarged, bleeding off the right edge
        parts.append(mark_svg(canvas_w + mark_h * 0.30, h / 2, block * 3, MIST, BLEED_OPACITY))
        parts.append(lockup(offset))
        return "\n".join(parts)

    lock_w = measure_lockup(lockup_only, w, h)
    x0 = round((w - lock_w) / 2)

    out = OUT / variant / f"{name}-{w}x{h}.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    render(svg(w, h, full_body(x0, w),
               f"Bandua Studio banner, variant {variant.upper()}, {name}"), out, w)
    return out


def verify(p: Path) -> str:
    with Image.open(p).convert("RGB") as im:
        w, h = im.size
        px = im.load()
        bg = tuple(int(DEEP.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))
        # centre of the opaque lockup only: ignore the low-opacity bleed/field
        def strong(x, y):
            c = px[x, y]
            return abs(c[0] - bg[0]) + abs(c[1] - bg[1]) + abs(c[2] - bg[2]) > 200
        xs = [x for y in range(h) for x in range(w) if strong(x, y)]
        cx = (min(xs) + max(xs)) / 2
    return f"lockup centre {cx:.1f} vs {w/2} (offset {cx - w/2:+.1f}px)"


def main() -> int:
    if shutil.which("flatpak") is None:
        print("flatpak not found", file=sys.stderr)
        return 1
    made = []
    for variant in ("c", "d"):
        for name, w, h in PLATFORMS:
            made.append((variant, build(name, w, h, variant)))

    print(f"generated: {len(made)}")
    for variant, p in made:
        print(f"  {str(p.relative_to(ROOT)):<48} {verify(p)}")

    shutil.rmtree(WORK, ignore_errors=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
