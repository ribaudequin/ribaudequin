# Banner candidates — C and D

**DECIDED 2026-10-09: C.** The banners in `banners/` are variant C. D is archived at `_archive/d/`.

Both were generated at all five platform sizes and compared as full-resolution PNGs — which is what
settled it. The comparison sheet is at `../mockups/banner-cd-comparison.png`.

```bash
python3 scripts/banner-candidates.py   # regenerates both, into banners/c/ and banners/d/
```

Note: re-running that script writes back into `banners/c/` and `banners/d/`. To change the shipped
banners, promote the chosen folder's files up to `banners/` as was done for C.

---

## What the two variants share

Both use the mark's **own geometry** as the only decoration: the arc, scaled up 3×, positioned so it
bleeds off the right edge at 7 % opacity. No new shapes, no colours outside the palette.

Everything else follows the main generator's rules — integer block sizes on the `UNIT=8` grid,
measured centring, rendered 1:1.

| Property | Value |
|---|---|
| Bleed opacity | 7 % — measures **1.20:1** against Deep |
| Field opacity (D only) | 4.5 % — measures **1.13:1** against Deep |
| Lockup centre offset | **±0.5 px** on all ten files |
| Text contrast, worst case (D) | **11.46:1** — Mist on the brightest field pixel |

The decoration is deliberately far below the 3:1 threshold for a meaningful element. It reads as depth,
not as content, and it cannot compete with the wordmark.

---

## Why C won

At full resolution, D's block field read as **texture rather than structure**, and it filled the
negative space that gives C its composure. C also holds up better in the short, wide formats
(LinkedIn, Patreon, Ko-fi), where D's field had the least room to breathe.

C's weakness, recorded honestly: it can read as **empty** in the wide formats. That is accepted — the
negative space is the treatment.

---

## A note on measuring these

The decoration must be **excluded from the centring measurement**. An earlier version measured the full
canvas including the bleed, so the measured width came out larger than the banner itself and the lockup
was positioned off the left edge — a negative offset. Measure the lockup alone; position the decoration
around it.

To check centring, threshold the ink strongly (a delta above ~200 against Deep) so the low-opacity
decoration drops out, then compare the bounding-box centre to the canvas centre.
