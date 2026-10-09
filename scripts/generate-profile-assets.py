#!/usr/bin/env python3
"""
Generate Bandua Studio profile assets — avatars and platform banners.

Reproducible: edit the constants, re-run, get the files. Geometry comes from the
Pixel Arc as defined in brand/brandboard.svg (22 outer + 14 inner blocks).

    python3 scripts/generate-profile-assets.py

Output: profiles/avatars/ and profiles/banners/

Two rules this script exists to enforce, both learned the hard way:

  1. CENTRING IS COMPUTED FROM THE REAL BOUNDING BOX, not from eyeballed
     constants. An earlier version used centre (4.0, -4.0) when the true bbox
     centre is (0.5, -7.5) — the mark sat ~3.5 blocks off-centre.

  2. PIXEL ART IS RENDERED 1:1 WITH INTEGER BLOCKS. Supersampling then
     downscaling blurs the block edges and shrinks the blocks below the point
     where they read as pixels. Blocks smaller than 4px read as noise.

Requires: inkscape (flatpak), Pillow.
"""

from __future__ import annotations

import math
import shutil
import subprocess
import sys
from pathlib import Path

from PIL import Image

# ---------------------------------------------------------------- paths

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "profiles"
AVATARS = OUT / "avatars"
BANNERS = OUT / "banners"
WORK = OUT / ".work"

INKSCAPE = [
    "flatpak", "run", "--command=inkscape", "org.inkscape.Inkscape",
    "--export-type=png",
]

# ---------------------------------------------------------------- palette

MIST = "#F2F5EE"
TEAL = "#1F5F66"
MOSS = "#5B7B3A"
DEEP = "#0F2A2E"

# ---------------------------------------------------------------- the mark
# Block coordinates, one unit per block. Verified against brandboard.svg.
#
# UNITS: the brandboard draws the mark on an 8-unit grid — its rects are
# width="8" and span x -40..40, giving ELEVEN blocks across, not 81. Each
# coordinate below is in those units, so the grid is 8 units per block.
# An earlier version of this script treated each unit as a block, producing a
# fine 81-block grid instead of 11 chunky blocks — the mark rendered as a
# dotted texture rather than pixel art. That was a units error, not a taste
# difference.
UNIT = 8                    # units per block, per brandboard.svg

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

BLOCKS = ARC_OUTER + ARC_INNER

# Real bounding box in UNITS, computed — never hard-coded from memory.
X0 = min(x for x, _ in BLOCKS)
X1 = max(x for x, _ in BLOCKS) + UNIT
Y0 = min(y for _, y in BLOCKS)
Y1 = max(y for _, y in BLOCKS) + UNIT
MARK_W_U, MARK_H_U = X1 - X0, Y1 - Y0      # 88 x 72 units
MARK_WB, MARK_HB = MARK_W_U // UNIT, MARK_H_U // UNIT   # 11 x 9 blocks

assert len(ARC_OUTER) == 22, len(ARC_OUTER)
assert len(ARC_INNER) == 14, len(ARC_INNER)
assert (MARK_WB, MARK_HB) == (11, 9), (MARK_WB, MARK_HB)


def mark_extent(block: int) -> float:
    """Farthest distance from the mark's centre to any occupied block corner, in
    pixels, for a given block size.

    The mark is centred, so this is a property of the mark alone: the arc's
    bounding-box corners are empty, which is why the mark can be larger than its
    bounding box suggests.
    """
    cx, cy = MARK_WB * block / 2, MARK_HB * block / 2
    worst = 0.0
    for x, y in BLOCKS:
        for dx in (0, UNIT):
            for dy in (0, UNIT):
                px = (x - X0 + dx) / UNIT * block
                py = (y - Y0 + dy) / UNIT * block
                worst = max(worst, math.hypot(px - cx, py - cy))
    return worst


def mark_svg(cx: float, cy: float, block: int, outer_fill: str, inner_fill: str,
             indent: str = "  ") -> str:
    """Pixel Arc centred on (cx, cy) in pixels, one block = `block` px.

    `block` must be a multiple of UNIT, and (cx, cy) are rounded, so every block
    edge lands on a whole pixel and stays crisp at 1:1. Fractional coordinates
    produce anti-aliased edges, which destroys the pixel-art grid.
    """
    assert block % UNIT == 0, f"block must be a multiple of {UNIT}, got {block}"
    k = block // UNIT                       # integer scale factor
    w, h = MARK_WB * block, MARK_HB * block
    ox = round(cx - w / 2) - X0 * k
    oy = round(cy - h / 2) - Y0 * k
    parts = [f'{indent}<g transform="translate({ox},{oy})">']
    for fill, blocks in ((outer_fill, ARC_OUTER), (inner_fill, ARC_INNER)):
        parts.append(f'{indent}  <g fill="{fill}">')
        for x, y in blocks:
            parts.append(
                f'{indent}    <rect x="{x * k}" y="{y * k}" '
                f'width="{block}" height="{block}"/>'
            )
        parts.append(f"{indent}  </g>")
    parts.append(f"{indent}</g>")
    return "\n".join(parts)


def measure_lockup(body_fn, w: int, h: int) -> int:
    """Return the ink width, in px, of a lockup drawn by `body_fn(offset, canvas_w)`.

    The probe canvas is wider than the banner so nothing is clipped. `body_fn`
    must paint its background across the *canvas*, not the banner width —
    otherwise the unpainted strip stays transparent, converts to black on RGB,
    and the measurement counts it as ink.
    """
    margin = w // 4
    canvas = w + 2 * margin
    WORK.mkdir(parents=True, exist_ok=True)
    src = WORK / "_measure.svg"
    src.write_text(svg(canvas, h, body_fn(margin, canvas), "probe"))
    png = WORK / "_measure.png"
    subprocess.run(INKSCAPE + [f"--export-filename={png}", f"--export-width={canvas}", str(src)],
                   check=True, capture_output=True)
    bg = tuple(int(BANNER_BG.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))
    with Image.open(png).convert("RGB") as im:
        px = im.load()
        xs = [x for y in range(0, im.height, 2) for x in range(0, im.width, 2)
              if px[x, y] != bg]
    return max(xs) - min(xs) + 1


def svg(width: int, height: int, body: str, title: str) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-label="{title}">\n'
        f"  <title>{title}</title>\n{body}\n</svg>\n"
    )


def render(svg_text: str, out_png: Path, width: int) -> None:
    """Render 1:1 — no supersampling, so pixel blocks stay on whole pixels."""
    WORK.mkdir(parents=True, exist_ok=True)
    src = WORK / (out_png.stem + ".svg")
    src.write_text(svg_text)
    subprocess.run(
        INKSCAPE + [f"--export-filename={out_png}", f"--export-width={width}", str(src)],
        check=True, capture_output=True,
    )


# ---------------------------------------------------------------- avatars

# An avatar is cropped to a circle. The mark is a single colour on a coloured
# field: two tones of the mark would lose one of them against the background.
#
# The mark is fitted by solving for the largest INTEGER block size that keeps
# every block inside a safe fraction of the inscribed radius. The arc's corners
# are empty, so the mark can be larger than its bounding box suggests.
AVATAR_COLOURWAYS = [
    ("teal", TEAL, MIST),
    ("deep", DEEP, MIST),
    ("mist", MIST, TEAL),
]
# One master render, then downscale. Rendering each platform size natively would
# quantise the block size differently per size (400px cannot hold 4px blocks),
# so the mark would change proportion between platforms. A single 512 master
# keeps the mark identical everywhere; platforms downscale an avatar anyway.
AVATAR_MASTER = 512
AVATAR_SIZES = [512, 460, 400]
AVATAR_SAFE = 0.88          # mark must stay inside 88% of the inscribed radius
AVATAR_MIN_BLOCK = 8        # multiple of UNIT, and below this blocks read as noise


def avatar_block(size: int) -> int:
    """Largest block size — a multiple of UNIT — whose farthest block corner
    fits inside the safe radius."""
    radius = size / 2 * AVATAR_SAFE
    best = AVATAR_MIN_BLOCK
    for block in range(AVATAR_MIN_BLOCK, size, UNIT):
        if mark_extent(block) > radius:
            break
        best = block
    return best


def build_avatars() -> list[tuple[Path, int]]:
    made = []
    block = avatar_block(AVATAR_MASTER)
    c = AVATAR_MASTER / 2

    for name, bg, fg in AVATAR_COLOURWAYS:
        body = (
            f'  <rect width="{AVATAR_MASTER}" height="{AVATAR_MASTER}" fill="{bg}"/>\n'
            + mark_svg(c, c, block, fg, fg)
        )
        master = WORK / f"avatar-{name}-master.png"
        render(svg(AVATAR_MASTER, AVATAR_MASTER, body, f"Bandua Studio avatar, {name}"),
               master, AVATAR_MASTER)

        with Image.open(master).convert("RGB") as im:
            for size in AVATAR_SIZES:
                out = AVATARS / f"avatar-{name}-{size}.png"
                if size == AVATAR_MASTER:
                    im.save(out)
                else:
                    im.resize((size, size), Image.LANCZOS).save(out)
                made.append((out, block))
    return made


# ---------------------------------------------------------------- banners

# Content is centred so it survives every platform's crop. The mark is sized as
# a fraction of banner height, in whole blocks, so it reads at every aspect.
BANNER_SPECS = [
    ("github",   1280, 640),
    ("x",        1500, 500),
    ("linkedin", 1584, 396),
    ("patreon",  1600, 400),
    ("kofi",     1200, 400),
]
BANNER_BG = DEEP
BANNER_FG = MIST
BANNER_MARK_H = 0.56        # mark height as a fraction of banner height
MIN_BLOCK = 8               # multiple of UNIT, and below this blocks read as noise

# Type scale, derived from the brandboard's Main logo lockup — not invented.
# There the mark is 144px tall and the wordmark is set at 28px, so word/mark =
# 0.194. An earlier version of this script used 0.34 and the wordmark came out
# 1.75x too large, which made the mark look under-weighted: the imbalance was in
# the type, not in the symbol.
BB_MARK_H = 144.0
BB_WORD = 28.0
WORD_RATIO = BB_WORD / BB_MARK_H          # 0.194
STUDIO_RATIO = 12.0 / BB_MARK_H           # brandboard "STUDIO" is 12px
TAG_RATIO = 11.0 / BB_MARK_H              # brandboard "by Marcelo Salvador" is 11px

FONT_SANS = "Space Grotesk"


def banner_block(h: int) -> int:
    """Block size — a multiple of UNIT — for a banner of height `h`."""
    raw = h * BANNER_MARK_H / MARK_HB
    return max(MIN_BLOCK, int(round(raw / UNIT)) * UNIT)


def build_banner(name: str, w: int, h: int) -> tuple[Path, int]:
    block = banner_block(h)
    mark_w, mark_h = MARK_WB * block, MARK_HB * block
    gap = round(mark_h * 0.30)

    word = mark_h * WORD_RATIO
    studio = mark_h * STUDIO_RATIO
    tag = mark_h * TAG_RATIO
    lead_word, lead_studio, lead_tag = word * 1.35, studio * 1.7, tag * 1.6

    def body(offset: float, canvas_w: int) -> str:
        return (f'  <rect width="{canvas_w}" height="{h}" fill="{BANNER_BG}"/>\n'
                + mark_svg(offset + mark_w / 2, h / 2, block, BANNER_FG, BANNER_FG)
                + text_block(offset + mark_w + gap, h, word, studio, tag,
                             lead_word, lead_studio, lead_tag))

    # Measure the real lockup width on a padded canvas, then centre on it.
    lock_w = measure_lockup(body, w, h)
    x0 = round((w - lock_w) / 2)

    out = BANNERS / f"{name}-{w}x{h}.png"
    render(svg(w, h, body(x0, w), f"Bandua Studio banner for {name}"), out, w)
    return out, block


def text_block(tx: float, h: int, word: float, studio: float, tag: float,
               lead_word: float, lead_studio: float, lead_tag: float) -> str:
    """The wordmark / STUDIO / tagline stack, vertically centred on the banner."""
    text_h = lead_word + lead_studio + lead_tag
    top = (h - text_h) / 2
    y_word = top + word
    y_studio = y_word + lead_studio
    y_tag = y_studio + lead_tag
    return f"""  <g font-family="{FONT_SANS}" fill="{BANNER_FG}">
    <text x="{tx:.0f}" y="{y_word:.0f}" font-size="{word:.0f}" font-weight="700" letter-spacing="-0.02em">bandua</text>
    <text x="{tx:.0f}" y="{y_studio:.0f}" font-size="{studio:.0f}" font-weight="500" letter-spacing="0.34em" opacity="0.78">STUDIO</text>
    <text x="{tx:.0f}" y="{y_tag:.0f}" font-size="{tag:.0f}" font-weight="400" opacity="0.66">Things built to last.</text>
  </g>"""


def build_banners() -> list[tuple[Path, int]]:
    return [build_banner(n, w, h) for n, w, h in BANNER_SPECS]


# ---------------------------------------------------------------- verify

def verify_avatar(path: Path, block: int) -> str:
    """Confirm the mark is centred and inside the inscribed circle."""
    with Image.open(path).convert("RGB") as im:
        w, h = im.size
        px = im.load()
        bg = px[1, 1]
        xs, ys, worst = [], [], 0.0
        cx, cy = w / 2, h / 2
        for y in range(h):
            for x in range(w):
                if px[x, y] != bg:
                    xs.append(x)
                    ys.append(y)
                    worst = max(worst, math.hypot(x + 0.5 - cx, y + 0.5 - cy))
    mx, my = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
    dx, dy = mx - cx, my - cy
    inside = worst <= w / 2
    return (f"block={block}px  mark {max(xs)-min(xs)+1}x{max(ys)-min(ys)+1}  "
            f"centre offset ({dx:+.1f},{dy:+.1f})px  "
            f"radius {worst:.1f}/{w/2:.0f}  {'OK' if inside else 'CLIPPED'}")


def verify_banner(path: Path, block: int) -> str:
    with Image.open(path).convert("RGB") as im:
        w, h = im.size
    return f"block={block}px  mark {MARK_WB*block}x{MARK_HB*block}  ({MARK_HB*block/h*100:.0f}% of height)"


def main() -> int:
    if shutil.which("flatpak") is None:
        print("flatpak not found — needed for Inkscape", file=sys.stderr)
        return 1
    AVATARS.mkdir(parents=True, exist_ok=True)
    BANNERS.mkdir(parents=True, exist_ok=True)

    avatars = build_avatars()
    banners = build_banners()

    print(f"avatars: {len(avatars)}")
    for p, b in avatars:
        print(f"  {str(p.relative_to(ROOT)):<44} {verify_avatar(p, b)}")
    print(f"banners: {len(banners)}")
    for p, b in banners:
        print(f"  {str(p.relative_to(ROOT)):<44} {verify_banner(p, b)}")

    shutil.rmtree(WORK, ignore_errors=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
