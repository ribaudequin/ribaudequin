#!/usr/bin/env python3
"""
Verify that the shipped assets are the ones that were chosen.

Run after any regeneration. Exits non-zero on failure, so it can gate a commit.

    python3 scripts/verify-shipped-assets.py

Why this exists: re-running the avatar generator once silently overwrote the
chosen banner variant with the plain version, because both scripts wrote to
profiles/banners/. The loss was only caught by eye. A file that gets checked
mechanically cannot regress quietly.
"""

from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
BANNERS = ROOT / "profiles" / "banners"
AVATARS = ROOT / "profiles" / "avatars"

DEEP = (0x0F, 0x2A, 0x2E)
MIST = (0xF2, 0xF5, 0xEE)
TEAL = (0x1F, 0x5F, 0x66)

# Variant C is the chosen banner treatment: the arc bleeding off the right edge
# at 7% opacity. Against Deep that composites to #1E373B.
BLEED = (0x1E, 0x37, 0x3B)
BLEED_MIN = 1000            # pixels; a plain banner has ~0

EXPECTED_BANNERS = {
    "github-1280x640.png": (1280, 640),
    "x-1500x500.png": (1500, 500),
    "linkedin-1584x396.png": (1584, 396),
    "patreon-1600x400.png": (1600, 400),
    "kofi-1200x400.png": (1200, 400),
}

EXPECTED_AVATARS = {
    "avatar-teal-512.png": (TEAL, False),
    "avatar-teal-460.png": (TEAL, False),
    "avatar-teal-400.png": (TEAL, False),
    "avatar-deep-512.png": (DEEP, True),
    "avatar-deep-460.png": (DEEP, True),
    "avatar-deep-400.png": (DEEP, True),
    "avatar-mist-512.png": (MIST, False),
    "avatar-mist-460.png": (MIST, False),
    "avatar-mist-400.png": (MIST, False),
}

failures: list[str] = []


def check_banners() -> None:
    found = {p.name for p in BANNERS.glob("*.png")}
    missing = set(EXPECTED_BANNERS) - found
    extra = found - set(EXPECTED_BANNERS)
    if missing:
        failures.append(f"banners missing: {sorted(missing)}")
    if extra:
        failures.append(f"unexpected files in banners/: {sorted(extra)}")

    for name, size in EXPECTED_BANNERS.items():
        p = BANNERS / name
        if not p.exists():
            continue
        with Image.open(p).convert("RGB") as im:
            if im.size != size:
                failures.append(f"{name}: size {im.size}, expected {size}")
            c = Counter(im.get_flattened_data())
        bleed = c.get(BLEED, 0)
        if bleed < BLEED_MIN:
            failures.append(
                f"{name}: {bleed} bleed pixels — this is the PLAIN banner, not variant C. "
                f"Run scripts/banner-candidates.py and promote banners/c/."
            )
        print(f"  {name:<24} {size[0]}x{size[1]}  bleed={bleed:>7}  variant C")


def check_avatars() -> None:
    found = {p.name for p in AVATARS.glob("*.png")}
    missing = set(EXPECTED_AVATARS) - found
    if missing:
        failures.append(f"avatars missing: {sorted(missing)}")

    for name, (field, wants_rim) in EXPECTED_AVATARS.items():
        p = AVATARS / name
        if not p.exists():
            continue
        with Image.open(p).convert("RGB") as im:
            w, h = im.size
            px = im.load()
            row = [px[x, h // 2] for x in range(w)]
        # Sample the FIELD at the centre, not near the edge: a rimmed avatar's
        # first pixels are the rim itself, not the field.
        centre = row[w // 2]
        if centre != field:
            failures.append(f"{name}: field is #{centre[0]:02X}{centre[1]:02X}{centre[2]:02X}, "
                            f"expected #{field[0]:02X}{field[1]:02X}{field[2]:02X}")
        # A rim only counts when it differs from the field. The Mist avatar's
        # field IS Mist, so edge pixels there are just the field, not a rim.
        has_rim = field != MIST and any(row[i] == MIST for i in range(0, 14))
        if wants_rim and not has_rim:
            failures.append(f"{name}: missing the Mist rim — a Deep avatar has no edge on dark surfaces")
        if not wants_rim and has_rim:
            failures.append(f"{name}: has an unexpected rim")
        print(f"  {name:<24} {w}x{h}  field=#{centre[0]:02X}{centre[1]:02X}{centre[2]:02X}"
              f"  rim={'yes' if has_rim else 'no'}")


def main() -> int:
    print("banners:")
    check_banners()
    print("avatars:")
    check_avatars()
    print()
    if failures:
        print(f"FAILED — {len(failures)} problem(s):")
        for f in failures:
            print(f"  - {f}")
        return 1
    print("All shipped assets match the chosen variants.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
