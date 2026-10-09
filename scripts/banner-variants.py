#!/usr/bin/env python3
"""
Banner variants for Bandua Studio — compare before choosing.

Renders the X banner (1500x500) in three treatments so the owner can pick one,
then the chosen treatment can be applied to every platform.

    python3 scripts/banner-variants.py

Output: profiles/.variants/*.png and a stacked comparison sheet.

The brandboard's own banner prescription (section 06 · Usage) is: Deep field,
mark, wordmark. That is deliberately minimal, so "plain" is on-brand. These
variants add texture using the brand's own language — the pixel grid and the arc
— rather than new shapes or colours.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "profiles" / ".variants"
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


def mark(cx: float, cy: float, block: int, outer: str, inner: str, op: float = 1.0) -> str:
    k = block // UNIT
    ox, oy = round(cx - WB * block / 2) - X0 * k, round(cy - HB * block / 2) - Y0 * k
    opa = f' opacity="{op}"' if op != 1.0 else ""
    out = [f'  <g transform="translate({ox},{oy})"{opa}>']
    for fill, blocks in ((outer, ARC_OUTER), (inner, ARC_INNER)):
        out.append(f'    <g fill="{fill}">')
        for x, y in blocks:
            out.append(f'      <rect x="{x*k}" y="{y*k}" width="{block}" height="{block}"/>')
        out.append("    </g>")
    out.append("  </g>")
    return "\n".join(out)


def pixel_field(w: int, h: int, block: int, fill: str, op: float, step: int) -> str:
    """Sparse grid of blocks on the mark's own grid — texture in the brand's language."""
    out = [f'  <g fill="{fill}" opacity="{op}">']
    for y in range(0, h, block * step):
        for x in range(0, w, block * step):
            out.append(f'    <rect x="{x}" y="{y}" width="{block}" height="{block}"/>')
    out.append("  </g>")
    return "\n".join(out)


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


# ---------------------------------------------------------------- lockup

def lockup(w: int, h: int, block: int, text: str) -> str:
    """Centred mark + text, as in the main generator."""
    mark_w, mark_h = WB * block, HB * block
    gap = round(mark_h * 0.30)
    word = mark_h * 0.194
    studio = mark_h * 0.083
    tag = mark_h * 0.076
    lw, ls, lt = word * 1.35, studio * 1.7, tag * 1.6
    total = mark_w + gap + word * 3.0
    x0 = round((w - total) / 2)
    tx = x0 + mark_w + gap
    th = lw + ls + lt
    top = (h - th) / 2
    y1, y2, y3 = top + word, top + word + ls, top + word + ls + lt
    return (mark(x0 + mark_w / 2, h / 2, block, MIST, MIST) + "\n"
            + f"""  <g font-family="Space Grotesk" fill="{MIST}">
    <text x="{tx}" y="{y1:.0f}" font-size="{word:.0f}" font-weight="700" letter-spacing="-0.02em">bandua</text>
    <text x="{tx}" y="{y2:.0f}" font-size="{studio:.0f}" font-weight="500" letter-spacing="0.34em" opacity="0.78">STUDIO</text>
    <text x="{tx}" y="{y3:.0f}" font-size="{tag:.0f}" font-weight="400" opacity="0.66">{text}</text>
  </g>""")


# ---------------------------------------------------------------- variants

def variant_a(w: int, h: int) -> str:
    """A — plain. What the brandboard's banner example shows."""
    return f'  <rect width="{w}" height="{h}" fill="{DEEP}"/>\n' + lockup(w, h, 32, "Things built to last.")


def variant_b(w: int, h: int) -> str:
    """B — pixel field + Moss accent rule under the wordmark."""
    block = 32
    body = [f'  <rect width="{w}" height="{h}" fill="{DEEP}"/>']
    body.append(pixel_field(w, h, 8, MIST, 0.045, 5))
    body.append(lockup(w, h, block, "Things built to last."))
    # Moss pixel rule, aligned to the mark's grid
    mark_h = HB * block
    rule_y = round(h / 2 + mark_h * 0.30)
    mark_w = WB * block
    total = mark_w + round(mark_h * 0.30) + (mark_h * 0.194) * 3.0
    x0 = round((w - total) / 2)
    tx = x0 + mark_w + round(mark_h * 0.30)
    body.append(f'  <g fill="{MOSS}">')
    for i in range(8):
        body.append(f'    <rect x="{tx + i*12}" y="{rule_y}" width="8" height="8"/>')
    body.append("  </g>")
    return "\n".join(body)


def variant_c(w: int, h: int) -> str:
    """C — the arc bleeding off the right edge at low opacity, for depth."""
    body = [f'  <rect width="{w}" height="{h}" fill="{DEEP}"/>']
    body.append(mark(w * 1.02, h * 0.5, 88, MIST, MIST, op=0.06))
    body.append(lockup(w, h, 32, "Things built to last."))
    return "\n".join(body)


def variant_d(w: int, h: int) -> str:
    """D — pixel field + bleed arc, no accent rule. Texture without the extra colour."""
    body = [f'  <rect width="{w}" height="{h}" fill="{DEEP}"/>']
    body.append(pixel_field(w, h, 8, MIST, 0.035, 5))
    body.append(mark(w * 1.02, h * 0.5, 88, MIST, MIST, op=0.05))
    body.append(lockup(w, h, 32, "Things built to last."))
    return "\n".join(body)


VARIANTS = [("A-plain", variant_a), ("B-field-moss", variant_b),
            ("C-bleed", variant_c), ("D-field-bleed", variant_d)]


def main() -> int:
    if shutil.which("flatpak") is None:
        print("flatpak not found", file=sys.stderr)
        return 1
    OUT.mkdir(parents=True, exist_ok=True)
    w, h = 1500, 500
    made = []
    for name, fn in VARIANTS:
        p = OUT / f"x-{name}.png"
        render(svg(w, h, fn(w, h), f"Bandua Studio banner variant {name}"), p, w)
        made.append((name, p))

    # comparison sheet: halves at 1:1 so texture is judged accurately
    crop_w = 900
    tiles = []
    for name, p in made:
        im = Image.open(p).convert("RGB")
        tiles.append((name, im.crop(((w - crop_w) // 2, 40, (w + crop_w) // 2, h - 40))))
    W = crop_w
    H = sum(t.height + 26 for _, t in tiles)
    sheet = Image.new("RGB", (W, H), "#000000")
    from PIL import ImageDraw
    d = ImageDraw.Draw(sheet)
    y = 0
    for name, t in tiles:
        d.text((8, y + 6), f"Variant {name}", fill="#F2F5EE")
        y += 22
        sheet.paste(t, (0, y))
        y += t.height + 4
    sheet.save(OUT / "comparison.png")
    print(f"variants: {len(made)}")
    for name, p in made:
        print(f"  {p.relative_to(ROOT)}")
    print(f"  {(OUT / 'comparison.png').relative_to(ROOT)}")
    shutil.rmtree(WORK, ignore_errors=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
