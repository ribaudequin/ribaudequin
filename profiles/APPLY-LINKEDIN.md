# LinkedIn — personal profile

**Scope: personal profile only.** A Company Page was considered and set aside — it would solve the
`sinesdigital` URL problem, but it is a new public entity and the decision was to tidy the personal
profile first.

Profile: `linkedin.com/in/bandua-marcelo-salvador`

---

## Current state — read from the profile 2026-10-09

The profile is nearly empty. This is mostly **creation**, not replacement.

| Field | Now | Target |
|---|---|---|
| Name | `Sinesdigital Marcelo Salvador` | `Marcelo Salvador` |
| Headline | `Proprietário(a), Marcelo Salvador - Sinesdigital` (Portuguese) | `Bandua Studio · Software Developer` |
| Location | `Setúbal, Portugal` | `Sines, Portugal` |
| About | **empty — no section exists** | the text below |
| Photo | old logo | `avatar-teal-400.png` |
| Banner | **none** | `linkedin-1584x396.png` |
| Activity | "You haven't posted yet" | — |
| Connections / followers | 3 / 3 | — |
| Profile language | Portuguese | — |

There is **no old About text in Portuguese to undo** — the section does not exist. The only Portuguese
content to replace is the headline.

**Note on the name field:** LinkedIn requires a real name (§2.1 of the User Agreement). `Marcelo
Salvador` goes there; the brand belongs in the headline. This is the opposite of X, where the display
name is free text.

---

## The URL — corrected

**My earlier claim was wrong.** I stated that LinkedIn fixes the profile slug at creation and that it
could not be changed. It can. The slug is now `bandua-marcelo-salvador`, changed on 2026-10-09 from
`sinesdigital-marcelo-salvador-97705a2b`.

Where the confusion came from: LinkedIn lets you **edit** the public profile URL, but only to a
**custom** value of your choosing — not to arbitrary free text, and it is rate-limited (roughly five
changes per six months). What is *not* possible is two personal accounts, which is a separate rule.

**One account per person** still holds. LinkedIn's User Agreement, §2.1:

> "you will only have one LinkedIn account, which must be in your real name"

That rule is about *people*, not email addresses, and it is why a second profile is not a route to a
cleaner URL — editing the existing one is.

**Links to the old slug break.** There is no redirect. Anything pointing at
`sinesdigital-marcelo-salvador-97705a2b` now 404s, and that includes the GitHub profile, which has been
updated.

---

## Files to upload

| Field | File | Size |
|---|---|---|
| Profile photo | `profiles/avatars/avatar-teal-400.png` | 400 × 400 |
| Background banner | `profiles/banners/linkedin-1584x396.png` | 1584 × 396 |

Both match LinkedIn's current specification. Use **teal** for the photo: LinkedIn's dark theme
surrounds the avatar with a very dark surface, where a Deep avatar would lose its edge.

### The banner is safe on every crop

LinkedIn trims the far edges on smaller screens and overlays the profile photo on the bottom-left.
Measured on the actual file:

| Check | Result |
|---|---|
| Lockup position | x 554–1031, y 90–305 — centred vertically (centre 198 of 396) |
| Left / right margin | 554 px / 552 px |
| Survives a 60 % centre crop (aggressive mobile) | **yes** |
| Survives 70 % and 80 % crops | yes |
| Bottom-left overlay zone (x 0–260, y 100–396) | **0 content pixels** |

Nothing important sits near an edge or under the photo.

---

## Headline — copy exactly

```
Bandua Studio · Software Developer
```

45 characters. LinkedIn's limit is 220, so there is room — but this matches `BRAND.md` §9 and the
existing guideline, and shorter reads better in search results.

If you want the projects visible without expanding, this variant also fits:

```
Bandua Studio · building simple, local, private tools
```

---

## About section — copy exactly

```
I build small, local, private tools — software that does one job well and keeps
your data on your own machine.

Currently working on:

· clavis — encrypted notes for passwords, PINs and bank details
· epub-library-manager — organise your EPUB library by series
· ValidadorPT — offline validator for Portuguese NIF, IBAN and NIB

No cloud. No accounts. No compromise.

Things built to last.
```

English only — the brand's public-content rule. If the profile is currently in Portuguese, this is a
change of language, not just of wording.

---

## Other fields

| Field | Value |
|---|---|
| Name | Marcelo Salvador *(real name — required by the User Agreement)* |
| Location | Sines, Portugal |
| Website | `https://github.com/ribaudequin` |
| Industry | Software Development |

**Do not put "Bandua Studio" in the Name field.** LinkedIn requires a real name there, and the brand
belongs in the headline. This is the opposite of X, where the display name is free text.

---

## Known limitation

I can **read** the profile through the desktop preview pane, but not **act** on it: the pane only
takes actions in the session the user is looking at, and the automated browser has a separate, logged-out
session. So the state above is observed, but the changes are yours to apply.

I will not drive an authenticated session on your behalf in any case.

---

## Order of operations

1. **Name** — pencil on the intro card → `Marcelo Salvador` → Save
2. **Headline** — same card → `Bandua Studio · Software Developer` → Save
3. **Location** — same card → `Sines, Portugal` → Save
4. **Photo** — pencil on the photo → upload `profiles/avatars/avatar-teal-400.png`
5. **Banner** — pencil on the cover → upload `profiles/banners/linkedin-1584x396.png`
6. **About** — *Add profile section* → *About* → paste → Save
7. **Contact info** — add `https://github.com/ribaudequin` and the industry *Software Development*
