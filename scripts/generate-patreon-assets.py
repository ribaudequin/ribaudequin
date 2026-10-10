#!/usr/bin/env python3
"""
Patreon assets for Bandua Studio.

Generates what Patreon needs and the existing set does not cover:

    profiles/patreon/profile-1024.png   1024 x 1024  profile image   (1:1)
    profiles/patreon/cover-2500x1000.png 2500 x 1000 cover photo     (2.5:1)
    profiles/patreon/tier-supporter.png   460 x 200  tier card      (2.3:1)
    profiles/patreon/tier-backer.png      460 x 200
    profiles/patreon/tier-patron.png      460 x 200

Patreon's own guidance, which drives the layout choices here:

  - The cover should keep key visuals on the RIGHT half, because the page title and
    About section sit on the left. Text on the cover is discouraged.
  - Tier images are wide, compact cards: one clear benefit, not detailed text.

Same rules as the other generators: integer block sizes on the UNIT=8 grid,
measured centring, rendered 1:1. Run scripts/verify-shipped-assets.py afterwards.

    /usr/bin/python3 scripts/generate-patreon-assets.py
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "profiles" / "patreon"
WORK = OUT / ".work"

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

WORD_RATIO = 28.0 / 144.0
STUDIO_RATIO = 12.0 / 144.0
TAG_RATIO = 11.0 / 144.0


def block_for(h: int, fraction: float) -> int:
    raw = h * fraction / HB
    return max(UNIT, int(round(raw / UNIT)) * UNIT)


def mark_svg(cx: float, cy: float, block: int, outer: str, inner: str,
             opacity: float = 1.0, indent: str = "  ") -> str:
    assert block % UNIT == 0, f"block must be a multiple of {UNIT}, got {block}"
    k = block // UNIT
    ox = round(cx - WB * block / 2) - X0 * k
    oy = round(cy - HB * block / 2) - Y0 * k
    opa = f' opacity="{opacity}"' if opacity != 1.0 else ""
    parts = [f'{indent}<g transform="translate({ox},{oy})"{opa}>']
    for fill, blocks in ((outer, ARC_OUTER), (inner, ARC_INNER)):
        parts.append(f'{indent}  <g fill="{fill}">')
        for x, y in blocks:
            parts.append(f'{indent}    <rect x="{x * k}" y="{y * k}" '
                         f'width="{block}" height="{block}"/>')
        parts.append(f"{indent}  </g>")
    parts.append(f"{indent}</g>")
    return "\n".join(parts)


def svg(w: int, h: int, body: str, title: str) -> str:
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" role="img" aria-label="{title}">\n'
            f"  <title>{title}</title>\n{body}\n</svg>\n")


def render(text: str, out_png: Path, w: int) -> None:
    WORK.mkdir(parents=True, exist_ok=True)
    src = WORK / (out_png.stem + ".svg")
    src.write_text(text)
    subprocess.run(INKSCAPE + [f"--export-filename={out_png}", f"--export-width={w}", str(src)],
                   check=True, capture_output=True)


# ---------------------------------------------------------------- profile

def build_profile() -> Path:
    """1024 x 1024. Patreon crops it to a circle, so the mark is centred with
    margin and in a single colour."""
    size = 1024
    block = block_for(size, 0.26)
    c = size / 2
    body = (f'  <rect width="{size}" height="{size}" fill="{TEAL}"/>\n'
            + mark_svg(c, c, block, MIST, MIST))
    out = OUT / "profile-1024.png"
    render(svg(size, size, body, "Bandua Studio profile image"), out, size)
    return out


# ---------------------------------------------------------------- cover

def build_cover() -> Path:
    """2500 x 1000. Key visuals on the RIGHT half — Patreon puts the page title
    and About on the left. No text, per Patreon's guidance."""
    w, h = 2500, 1000
    block = block_for(h, 0.42)
    mark_h = HB * block
    # right-of-centre, clear of the left-hand title area
    cx = w * 0.68
    cy = h / 2
    body = [f'  <rect width="{w}" height="{h}" fill="{DEEP}"/>']
    # the arc, enlarged, bleeding off the right edge
    body.append(mark_svg(w + mark_h * 0.4, h / 2, block * 3, MIST, MIST, opacity=0.07))
    body.append(mark_svg(cx, cy, block, MIST, MIST))
    out = OUT / "cover-2500x1000.png"
    render(svg(w, h, "\n".join(body), "Bandua Studio cover"), out, w)
    return out


# ---------------------------------------------------------------- tiers

TIERS = [
    ("supporter", "Supporter", TEAL, MIST),
    ("backer", "Backer", MOSS, MIST),
    ("patron", "Patron", DEEP, MIST),
]


def measure_text(text: str, size: float) -> float:
    """Real rendered width of `text` at `size`, in px.

    Estimating width from len(text) gave the Supporter card a wider text block
    than Backer or Patron, which pushed its mark off-centre and made the three
    tier marks different sizes. Measure, do not estimate.
    """
    WORK.mkdir(parents=True, exist_ok=True)
    probe = svg(900, 300,
                f'  <text x="20" y="200" font-family="Space Grotesk" font-size="{size:.1f}" '
                f'font-weight="700" fill="#000000">{text}</text>',
                "probe")
    src = WORK / "_measure_text.svg"
    src.write_text(probe)
    png = WORK / "_measure_text.png"
    subprocess.run(INKSCAPE + [f"--export-filename={png}", "--export-width=900", str(src)],
                   check=True, capture_output=True)
    with Image.open(png).convert("RGB") as im:
        px = im.load()
        xs = [x for y in range(0, im.height, 2) for x in range(im.width) if px[x, y] != (255, 255, 255)]
    return (max(xs) - min(xs) + 1) if xs else 0


def build_tier(name: str, label: str, field: str, fg: str) -> Path:
    """460 x 200. A wide card: one mark and one word. Patreon's guidance is one
    clear benefit, not detailed text — so the tier name only.

    The mark block size is fixed across all three tiers, so the marks match.
    """
    w, h = 460, 200
    block = block_for(h, 0.52)
    mark_h = HB * block
    mark_w = WB * block
    word = mark_h * WORD_RATIO * 1.25
    gap = mark_h * 0.28

    text_w = measure_text(label, word)
    total = mark_w + gap + text_w
    x0 = round((w - total) / 2)

    # Deep field needs a rim to hold on dark surfaces; the others do not.
    rim = ""
    if field == DEEP:
        rim = (f'  <rect x="1.5" y="1.5" width="{w-3}" height="{h-3}" rx="8" '
               f'fill="none" stroke="{MIST}" stroke-width="3" stroke-opacity="0.35"/>\n')

    body = [f'  <rect width="{w}" height="{h}" fill="{field}"/>']
    body.append(mark_svg(x0 + mark_w / 2, h / 2, block, fg, fg))
    body.append(
        f'  <text x="{x0 + mark_w + gap:.0f}" y="{h/2 + word*0.35:.0f}" '
        f'font-family="Space Grotesk" font-size="{word:.0f}" font-weight="700" '
        f'fill="{fg}">{label}</text>'
    )
    if rim:
        body.append(rim.rstrip())
    out = OUT / f"tier-{name}.png"
    render(svg(w, h, "\n".join(body), f"Bandua Studio tier: {label}"), out, w)
    return out


def main() -> int:
    if shutil.which("flatpak") is None:
        print("flatpak not found", file=sys.stderr)
        return 1
    OUT.mkdir(parents=True, exist_ok=True)

    made = [build_profile(), build_cover()]
    for name, label, field, fg in TIERS:
        made.append(build_tier(name, label, field, fg))

    print(f"generated: {len(made)}")
    for p in made:
        from PIL import Image
        with Image.open(p) as im:
            print(f"  {str(p.relative_to(ROOT)):<44} {im.width}x{im.height}  {p.stat().st_size} B")

    shutil.rmtree(WORK, ignore_errors=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
