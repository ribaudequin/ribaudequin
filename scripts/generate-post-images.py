#!/usr/bin/env python3
"""
Launch post images for Bandua Studio.

Writes into a dated post folder, so regenerating one post can never touch another:

    posts/<date-slug>/images/x-1600x900.png          1600 x 900   16:9
    posts/<date-slug>/images/linkedin-1200x627.png   1200 x 627   1.91:1
    posts/<date-slug>/images/patreon-1500x900.png    1500 x 900   5:3
    posts/<date-slug>/images/kofi-1200x600.png       1200 x 600   2:1

    /usr/bin/python3 scripts/generate-post-images.py 2026-10-10-launch
    /usr/bin/python3 scripts/generate-post-images.py            # list folders

The image carries the brand and the three projects — nothing it cannot back up.
No licence claim, no version numbers, no dates: the projects carry no LICENSE file
yet, and versions move.

A bug this script exists to avoid, fixed below: the first version spaced project
rows by `font_size * 2.0`, which is less than a title plus a description line, so
each description landed on top of the next title. Measured: 3 text blocks instead
of 6. The row pitch is now computed from the two actual line heights plus a gap.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "posts"
WORK = ROOT / "profiles" / ".work-posts"

INKSCAPE = [
    "flatpak", "run", "--command=inkscape", "org.inkscape.Inkscape",
    "--export-type=png",
]

MIST = "#F2F5EE"
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

PROJECTS = [
    ("clavis", "encrypted notes"),
    ("epub-library-manager", "EPUB library organiser"),
    ("ValidadorPT", "offline Portuguese ID validator"),
]

PLATFORMS = [
    ("x", 1600, 900),
    ("linkedin", 1200, 627),
    ("patreon", 1500, 900),
    ("kofi", 1200, 600),
]


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


def build(name: str, w: int, h: int, out_dir: Path) -> Path:
    """Left column: mark, wordmark, tagline. Right column: the three projects.

    A two-column layout because these images are wide; a single centred stack
    leaves the sides dead.
    """
    block = max(UNIT, int(round(h * 0.30 / HB / UNIT)) * UNIT)
    mark_h = HB * block
    mark_w = WB * block

    word = mark_h * WORD_RATIO * 1.15
    studio = mark_h * STUDIO_RATIO * 1.15
    tag = mark_h * TAG_RATIO * 1.2

    pad = h * 0.14
    left_x = pad + mark_w / 2
    top = h * 0.20

    lparts = [mark_svg(left_x, top + mark_h / 2, block, MIST, MIST)]
    y_word = top + mark_h + word * 1.5
    lparts.append(
        f'  <g font-family="Space Grotesk" fill="{MIST}">\n'
        f'    <text x="{pad:.0f}" y="{y_word:.0f}" font-size="{word:.0f}" '
        f'font-weight="700" letter-spacing="-0.02em">bandua</text>\n'
        f'    <text x="{pad:.0f}" y="{y_word + studio * 1.7:.0f}" font-size="{studio:.0f}" '
        f'font-weight="500" letter-spacing="0.34em" opacity="0.72">STUDIO</text>\n'
        f'    <text x="{pad:.0f}" y="{y_word + studio * 1.7 + tag * 2.1:.0f}" '
        f'font-size="{tag:.0f}" font-weight="400" opacity="0.6">Things built to last.</text>\n'
        f"  </g>"
    )

    # Right column. The row pitch must fit a title AND its description: the first
    # version used font*2.0 and the description landed on the next title.
    right_x = w * 0.52
    psize = tag * 0.95
    dsize = psize * 0.82
    line_title = psize * 1.45          # title line height
    line_desc = dsize * 1.55           # description line height
    row_gap = psize * 1.1              # blank space between project rows
    row_pitch = line_title + line_desc + row_gap

    total_h = row_pitch * len(PROJECTS) - row_gap
    ptop = (h - total_h) / 2 + line_title * 0.78

    rparts = [f'  <g font-family="JetBrains Mono" fill="{MIST}">']
    for i, (proj, desc) in enumerate(PROJECTS):
        y = ptop + i * row_pitch
        rparts.append(
            f'    <text x="{right_x:.0f}" y="{y:.0f}" font-size="{psize:.0f}" '
            f'font-weight="500">{proj}</text>'
        )
        rparts.append(
            f'    <text x="{right_x:.0f}" y="{y + line_desc:.0f}" '
            f'font-size="{dsize:.0f}" font-weight="400" opacity="0.62">{desc}</text>'
        )
    rparts.append("  </g>")

    body = [f'  <rect width="{w}" height="{h}" fill="{DEEP}"/>']
    body.append(mark_svg(-mark_h * 0.35, h * 0.5, block * 3, MIST, MIST, opacity=0.06))
    body.append("\n".join(lparts))
    body.append("\n".join(rparts))

    out = out_dir / f"{name}-{w}x{h}.png"
    render(svg(w, h, "\n".join(body), f"Bandua Studio post, {name}"), out, w)
    return out


def list_posts() -> list[Path]:
    if not POSTS.exists():
        return []
    return sorted(p for p in POSTS.iterdir()
                  if p.is_dir() and p.name != "TEMPLATE" and not p.name.startswith("."))


def main() -> int:
    if shutil.which("flatpak") is None:
        print("flatpak not found", file=sys.stderr)
        return 1

    if len(sys.argv) < 2:
        posts = list_posts()
        if not posts:
            print("No post folders yet. Create one:\n"
                  "  cp -r posts/TEMPLATE posts/YYYY-MM-DD-slug")
            return 1
        print("Available posts — pass one as an argument:")
        for p in posts:
            print(f"  {p.name}")
        return 0

    slug = sys.argv[1]
    post_dir = POSTS / slug
    if not post_dir.is_dir():
        print(f"No such post folder: posts/{slug}", file=sys.stderr)
        print("Available:", ", ".join(p.name for p in list_posts()) or "(none)", file=sys.stderr)
        return 1

    img_dir = post_dir / "images"
    img_dir.mkdir(parents=True, exist_ok=True)

    made = [build(n, w, h, img_dir) for n, w, h in PLATFORMS]
    print(f"generated into posts/{slug}/images/:")
    for p in made:
        with Image.open(p) as im:
            print(f"  {p.name:<24} {im.width}x{im.height}  {p.stat().st_size} B")

    shutil.rmtree(WORK, ignore_errors=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
