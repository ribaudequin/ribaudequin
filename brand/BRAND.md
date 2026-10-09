# Bandua Studio — Brand Guidelines

Complete brand identity reference. This document is the authority on what the brand is, how it looks, and how it is written.

---

## 1. The Name

**Bandua Studio** — short form **Bandua**.

### Origin

*Bandua* (also attested as *Bandue*, *Bandi*, *Banduae*) is the name of a deity worshipped in western Iberia before the Roman period — by the Gallaeci and the Lusitanians, in the territory that is now northern Portugal and Galicia. It is one of the best-documented indigenous deities of the region, alongside Cosus, Nabia and Reo, with around thirty surviving votive inscriptions found mostly in Ourense and Cáceres.

Two readings of the name have scholarly support, and both matter here:

- From the Proto-Indo-European root **\*bhendh-** — "to bind, to tie". This gives a deity of bonds and connections: the ties between people, and by extension order, rule and protection.
- As a deity of **passages and paths** — a protector of travellers, of the roads, and of goods in transit.

In the *interpretatio romana* the deity was associated with **Mars**, and in one dedication is named as a god of the *vexillum* — the standard. Above all, Bandua was a **tutelary deity**: a protector of a specific community, which is why the inscriptions so often attach a local epithet (*Bandua Roudaeco*, *Bandua Etobrico*, *Bandua Brealiacui*).

The name is pre-Roman, Iberian, and tied to the geography of Sines and the Atlantic west. It is short, accent-free, and pronounceable in English.

### What the name means for the brand

The brand inherits three ideas from the name, and they are the values below: **protection** (tools that keep your data yours), **bonds** (tools built for people, not for engagement metrics), and **passages** (tools that travel with you — local, portable, no accounts).

### Naming rules

- Full form on first mention or formal contexts: **Bandua Studio**.
- Short form thereafter, and where space is tight: **Bandua**.
- The wordmark is always lowercase: `bandua`.
- The brand is a personal studio and stays associated with its author: **Bandua Studio by Marcelo Salvador**.
- Do not translate, transliterate or abbreviate the name. No "BS", no "Bandua Tech", no "Bandua Labs".

---

## 2. Positioning

**What it is.** A one-person software studio making small, local, private tools.

**What it makes.** Desktop and mobile applications that do one job well, run on the user's own machine, and ask for nothing — no account, no cloud, no telemetry.

**What it is not.** Not a SaaS company, not an agency, not a startup. There is no growth target, no funding, no roadmap dictated by a market. Tools are built when there is a real problem to solve and released when they are ready.

**The promise.** Things built to last.

---

## 3. Values

| Value | What it means in practice |
|---|---|
| **Local** | Data stays on the device. Offline-first is the default, not a feature toggle. |
| **Private** | No accounts, no tracking, no telemetry. Privacy is structural, not a setting. |
| **Simple** | One tool, one job. No feature bloat, no settings maze. |
| **Made with care** | Craft over speed. Details are measured, not guessed. |
| **Built to last** | Tools that still work in five years without a subscription or a server. |

---

## 4. Logo

### 4.1 The symbol — Pixel Arc

Two concentric arcs drawn in pixel art, rendered on an 8 px grid.

| Property | Value |
|---|---|
| Name | **Pixel Arc** |
| Grid | 8 px |
| Total pixels | 36 (22 in the outer arc, 14 in the inner arc) |
| Outer arc | 6 blocks across the top, then a 3-step shoulder (offsets 28, 36), then 6 rows down each side at offset 40 |
| Inner arc | 4 blocks across the top, then 2 rows down each side at offset 20, then 4 rows at offset 24 |
| Bounding box | 88 × 72 units — width/height ratio **1.222** |
| Canvas | 120 × 120 viewBox, mark centred at (60, 60) |
| Format | SVG, hand-placed rectangles — no strokes, no curves |

The pixel construction is deliberate. An arc alone is a generic mark — it appears in architecture, heritage and hospitality branding. Rendered as discrete square blocks, the same arc reads as *built* rather than drawn: assembled from units, like code. The twist that makes the mark specific is the grid, not the shape.

The two arcs also carry the name's meaning: an outer shelter and an inner one — protection, and the passage between them.

> **Geometry is authoritative in `brandboard.svg`.** This mark was drawn twice in separate passes — the
> brandboard first, then the standalone icons — and the two drifted. The standalone icons had 25 outer
> blocks, a flat 11-block top row and a 90° corner, giving a boxy 104 × 64 silhouette at ratio 1.625.
> They were rebuilt on 2026-10-09 to match the brandboard exactly: 22 + 14 blocks, an 11 × 9 occupancy
> grid, ratio 1.222. Verified block-by-block against the brandboard geometry, all 9 rows identical.
> **Any future redraw must be checked against `brandboard.svg`, not against a rendered PNG.**

### 4.2 The wordmark

`bandua` in **Space Grotesk**, lowercase, with `STUDIO` and `by Marcelo Salvador` set beneath in the supporting stack.

The lowercase wordmark is intentional and is not capitalised, even at the start of a sentence or in a title.

### 4.3 Logo variations

| File | Arc colours | Use on |
|---|---|---|
| `brand/bandua-icon.svg` | Teal `#1F5F66` + Deep `#0F2A2E` | Light backgrounds |
| `brand/bandua-icon-dark.svg` | Deep `#0F2A2E` + Teal `#1F5F66` | Light backgrounds (deep-dominant) |
| `brand/bandua-icon-light.svg` | Teal `#1F5F66` + Mist `#F2F5EE` | Dark backgrounds |
| `assets/bandua-dark.svg` | Canonical copy of `bandua-icon-dark.svg` | Light backgrounds |
| `assets/bandua-light.svg` | Canonical copy of `bandua-icon-light.svg` | Dark backgrounds |

The `assets/` copies exist so that README headers can reference a stable path. They are byte-identical
to their `brand/` counterparts and must be re-copied if the icons change — they are not a second source.

> **Correction, 2026-10-09.** These two files previously held the *old* logo: two smooth stroked
> arcs (`stroke-width="8"`, `fill="none"`), not the Pixel Arc. The dark variant used `#7FC4CC`, a
> colour outside the palette. Each file was also 96% dead weight — 7 736 of 8 094 bytes were
> embedded C2PA metadata — and both were 120 × 120 icons despite being described as a "full lockup".
> All four defects are fixed; the files are now canonical copies of the Pixel Arc icons.

### 4.4 Clear space and minimum size

- **Clear space:** one block width (8 px at nominal scale) on all sides. Nothing enters this margin — no text, no border, no other logo.
- **Minimum size:** 32 px for the symbol. Below that the 8 px grid stops resolving; use a simplified two-block form or omit the symbol entirely.

### 4.5 Don'ts

- Do not rotate, skew or apply perspective to the symbol.
- Do not re-colour the arcs outside the palette in section 5.
- Do not add gradients, shadows, glows or bevels.
- Do not redraw the arcs as smooth curves or strokes — the grid is the identity.
- Do not place the symbol on a busy photographic background without a solid panel behind it.
- Do not capitalise the wordmark.
- Do not add a tagline inside the logo lockup.

---

## 5. Colour

### Palette

| Name | Hex | Role |
|---|---|---|
| **Mist** | `#F2F5EE` | Background / light |
| **Teal** | `#1F5F66` | Primary / brand |
| **Moss** | `#5B7B3A` | Accent / secondary |
| **Deep** | `#0F2A2E` | Text / dark |

### Measured contrast ratios

All values below are computed with the WCAG 2.x relative-luminance formula.

| Foreground | Background | Ratio | AA text (4.5:1) | AA large / UI (3:1) |
|---|---|---|---|---|
| Deep | Mist | 13.71:1 | Pass | Pass |
| Deep | White | 15.10:1 | Pass | Pass |
| Teal | White | 7.27:1 | Pass | Pass |
| Teal | Mist | 6.61:1 | Pass | Pass |
| Mist | Deep | 13.71:1 | Pass | Pass |
| Mist | Teal | 6.61:1 | Pass | Pass |
| Moss | White | 4.84:1 | Pass | Pass |
| **Moss** | **Mist** | **4.40:1** | **Fail** | Pass |
| **Moss** | **Deep** | **3.12:1** | **Fail** | Pass |
| **Deep** | **Moss** | **3.12:1** | **Fail** | Pass |
| **Mist** | **Moss** | **4.40:1** | **Fail** | Pass |
| **Teal** | **Deep** | **2.08:1** | **Fail** | **Fail** |

### Rules that follow from the measurements

1. **Body text is Deep on Mist, or Mist on Deep.** Both give 13.71:1. There is no reason to use anything else.
2. **Moss is an accent only.** At 4.40:1 on Mist it misses the 4.5:1 threshold for body text. Use it for icons, rules, small marks and large display type — never for paragraph text on Mist, and never for text on Deep.
3. **Teal and Deep must not touch.** At 2.08:1 they fail both thresholds. This is why `bandua-icon.svg` pairs Teal with Deep only as *adjacent blocks of a shape*, never as text on a background — and why the dark-background variant swaps Deep for Mist.
4. **Never encode meaning in colour alone.** Pair any colour-coded state with a label, icon or position.

### Surfaces must never be a palette colour

**A palette colour may never be used as the background of a document that displays the palette.** This
is not a style preference — it is a correctness rule, and the brandboard broke it.

The brandboard's page background was `#0F2A2E`, which *is* **Deep**. Everything drawn in Deep on that
page became invisible, and three things were:

| Section | Element | Effect |
|---|---|---|
| 02 · Colors | the **DEEP swatch** itself | vanished completely — the palette appeared to have only three colours |
| 05 · Logo Variations | the "Dark background" demo card | no visible panel |
| 06 · Usage | the "Banner" demo card | no visible panel |

The background is now **`#1A464C`** — a **lightened Deep**, not a neutral grey. It keeps Deep's exact hue
(188°) and saturation and only raises the lightness, so the page stays inside the brand's colour family
instead of introducing a fifth, foreign grey into a document whose subject is the palette.

It was chosen because it measures *identically* to a neutral `#404040` while belonging to the brand:

| Background vs | `#404040` neutral | `#1A464C` lightened Deep |
|---|---|---|
| Deep `#0F2A2E` | 1.46:1 | **1.46:1** |
| Teal `#1F5F66` (nearest palette colour) | 1.43:1 | **1.43:1** |
| Moss `#5B7B3A` | 2.14:1 | **2.14:1** |
| Mist `#F2F5EE` labels *on* the background | 9.42:1 | **9.42:1** |

Same luminance, so the same legibility — but the hue is the brand's. Recorded because it is a general
principle: **a surface that is not itself a brand colour can still be derived from one.** Prefer a
lightness variation of the palette over an unrelated neutral.

Four rules, so this cannot recur:

- **Swatches carry a hairline border** (`#F2F5EE` at `stroke-opacity` 0.45). With a soft background the
  DEEP swatch is held apart mainly by that border, not by its fill — so the border is load-bearing, not
  decorative. Removing it would put the defect back.
- **Do not darken the background towards Deep.** Below roughly L=18% the separation drops under 1.30:1
  and the DEEP swatch starts to disappear again.
- **Prefer a derived tint over a foreign neutral.** `#1A464C` beats `#404040` on every count here.
- **Any future change to the background must be checked against all four swatches and all demo cards** —
  not just against the text.

> **Trade-off, stated plainly.** A soft background means lower separation from the darkest palette
> colour. At 1.46:1 the DEEP swatch is legible but not emphatic — it is held apart mainly by its border,
> and on a badly calibrated or dim display that border is doing the work. That is the cost of a gentler
> surface. Note also that `#1A464C` gives *more* separation from Deep (1.46:1) than pure black would
> (1.39:1), so the softer choice is also the more correct one. If the brandboard is ever reproduced in
> print or on unknown displays, re-check this pair first.

---

## 6. Typography

| Role | Typeface | Weights | Use |
|---|---|---|---|
| **Primary** | Space Grotesk | 400, 500, 700 | Wordmark, headings, UI, body |
| **Monospace** | JetBrains Mono | 400, 500 | Code, terminals, version numbers, technical labels |

### Rules

- **Space Grotesk is the default.** If only one typeface can be used, use this one.
- **JetBrains Mono is for machine text**, never for prose. Version numbers, file paths, commands, code, cryptographic addresses.
- **No third typeface.** Do not introduce Inter, Helvetica, Arial or a system fallback as a design choice — a fallback is a failure mode, not a style.
- **Lowercase for the wordmark.** Titles and headings may use sentence case. Avoid all-caps except for short technical labels (`STUDIO`, `MIT`).
- Body copy: 16 px minimum, line height 1.5.
- Letter-spacing is left at the typeface default, except the wordmark.

---

## 7. Voice and Tone

**Mixed register** — technical when talking about code, personal when talking about the work.

| Principle | Meaning |
|---|---|
| **Clear** | Simple, direct language. No unnecessary jargon. |
| **Precise** | Concrete facts. No exaggeration, no vague promises. |
| **Personal** | Approachable and warm. Like talking to a friend you trust. |
| **Trustworthy** | Transparent about what is made, how, and why. |

### Register by context

| Context | Register | Example |
|---|---|---|
| Code / documentation | Technical | "Offline validator for Portuguese identifiers." |
| Social media | Personal | "Things I make with care, built to last." |
| READMEs | Mixed | "Simple tools, made with care. Things that last." |
| Support | Personal | "Thanks for the support. I'll look into that." |

### Words to use, words to avoid

| ✅ Use | ❌ Avoid |
|---|---|
| Simple | Simplistic |
| Local | Offline-only |
| Private | Secure |
| Built to last | High-quality |
| Made with care | Handcrafted |
| Tools | Solutions |
| Things | Products |

### Rules

- Short sentences. No fluff.
- No emojis in technical contexts.
- No excessive exclamation marks.
- **English only** for everything public — posts, READMEs, bios, documentation.
- No hype, no superlatives, no marketing language. State what the tool does and stop.
- Never claim a feature the code does not have.

---

## 8. Taglines

| Tagline | Use |
|---|---|
| **Things built to last.** | Primary. The default signature. |
| Simple things, made with care. Flowing wherever you need them. | Secondary — the full form, as it appears on the brandboard. |
| Simple things, made with care. | Secondary, short form, where space is tight. |
| Local. Private. Yours. | Feature-led, for privacy-focused tools. |
| No cloud. No accounts. No compromise. | Product-specific (clavis). |
| Built to protect what matters. | Product-specific, security contexts. |

---

## 9. Usage by Platform

| Platform | Handle / URL | Bio or headline |
|---|---|---|
| GitHub | [ribaudequin](https://github.com/ribaudequin/) | Bandua Studio · things built to last. Small, local, private tools. |
| X | [@banduastudio](https://x.com/banduastudio) | Bandua Studio · things built to last. / Small, local, private tools. / No cloud. No accounts. No compromise. |
| LinkedIn | [bandua-marcelo-salvador](https://www.linkedin.com/in/bandua-marcelo-salvador) | Bandua Studio · Software Developer |
| Patreon | [ribalinux](https://www.patreon.com/c/ribalinux) | Support my work on Patreon |
| Ko-fi | [A0383T5](https://ko-fi.com/A0383T5) | Buy me a coffee |

The X bio runs to three lines, with a blank line before the last. Full post and bio copy lives in
`COMMUNICATION.md`.

---

## 10. Signature

```
Marcelo Salvador
Bandua Studio
```

---

## 11. Assets

| Path | Contents |
|---|---|
| `brand/BRAND.md` | This document — complete brand guidelines |
| `brand/brandboard.svg` | Complete identity board |
| `brand/bandua-icon.svg` | Pixel Arc — Teal + Deep, light backgrounds |
| `brand/bandua-icon-dark.svg` | Pixel Arc — Deep + Teal, light backgrounds |
| `brand/bandua-icon-light.svg` | Pixel Arc — Teal + Mist, dark backgrounds |
| `brand/AGENTS.md` | Rules for AI agents creating brand content |
| `brand/COMMUNICATION.md` | Communication guidelines and copy examples |
| `assets/bandua-light.svg`, `assets/bandua-dark.svg` | Canonical copies of the Pixel Arc icons for README paths |
| `assets/PROJECT_HEADER.md` | README header template for projects |
| `assets/README.md` | GitHub profile page source |
| `assets/redes.png` | Social profile mockups, all five platforms |
| `mockups/` | Review artefacts — see below |
| `TODO.md` | Task list for the brand |

### `mockups/`

Working artefacts kept out of `brand/` so the brand folder holds only canonical assets. All HTML here
uses **relative paths** and is self-contained — fonts load from `mockups/fonts/`, not from the network,
so the pages render offline.

| Path | Contents |
|---|---|
| `mockups/arc-compare.html` | Side-by-side of the brandboard geometry vs the standalone icon |
| `mockups/brand-verify.html` | Icon renders + the measured contrast table |
| `mockups/bandua-typography-mockup.html` | Typeface comparison |
| `mockups/bb-icon.png` | Brandboard icon geometry, rendered in isolation for comparison |
| `mockups/brandboard-icon-extracted.svg` | The same geometry as an SVG, extracted from `brandboard.svg` |
| `mockups/bandua-social-mockup.{png,svg}` | Profile mockups, all five platforms |
| `mockups/brandboard-preview.png` | Full identity board, rendered |
| `mockups/icons-preview*.{png,svg}` | Icon iterations from the design pass |
| `mockups/fonts/` | Space Grotesk, Outfit, Sora, Fraunces — woff2, for offline rendering |

> **Why this folder exists.** These files were originally written to the agent scratch directory, which
> is pruned after 24 hours — so review artefacts kept disappearing. They now live with the project.

---

## Notes

- This is a living document. It updates as the brand evolves.
- Where this document and any other brand file disagree, **this document wins**.
- The brand is associated with the name Marcelo Salvador but is not limited to him.
- All public-facing documentation and communication is in English only.
- Communication with the author is in PT-PT.
