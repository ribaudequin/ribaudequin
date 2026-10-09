# X (Twitter) — @sinesdigital → Bandua Studio

Everything below is ready. **You apply it** — the X API needs OAuth and there are no credentials
configured, and I will not drive an authenticated session on your behalf.

Account: **@sinesdigital**, created February 2011, 667 posts, 20 followers, 120 following.
Last post: **June 2015**.

---

## Decisions taken

| # | Decision |
|---|---|
| 1 | **Use the existing account** — its age is worth keeping |
| 2 | **Leave the 667 old posts as they are** — nothing is deleted |
| 3 | **Replace the avatar** and **change the handle** |

---

## What changes

| Field | Before | After |
|---|---|---|
| Display name | `sinesdigital` | **Bandua Studio** |
| Handle | `@sinesdigital` | **@banduastudio** |
| Avatar | Genialevasion logo | **Bandua Pixel Arc** |
| Banner | 2013 image, unrelated | **Bandua banner, 1500 × 500** |
| Bio | SinesDigital services, in Portuguese | **English, brand voice** |
| Location | `Sines` | **Sines, Portugal** |
| Website | *(none)* | **https://github.com/ribaudequin** |

---

## Files to upload

| Field | File | Size |
|---|---|---|
| Avatar | `profiles/avatars/avatar-teal-400.png` | 400 × 400 |
| Banner | `profiles/banners/x-1500x500.png` | 1500 × 500 |

Both are inside `~/Hermes/Bandua Studio/`. Use **teal** for the avatar here, not deep — X's dark theme
surrounds the avatar with `#000000`, where Teal holds at 2.89:1 and the deep variant would need its rim
to read at all.

> **The banner is safe with the avatar on top.** X overlays the profile picture on the banner's
> bottom-left (roughly x 0–400, y 150–500 at 1500 × 500). That region was measured: **zero** non-background
> pixels, so nothing is hidden. The old Genialevasion banner *did* have its logo covered there.

---

## Bio — copy exactly

```
Bandua Studio · things built to last.
Small, local, private tools.

No cloud. No accounts. No compromise.
```

**105 characters.** X's limit is 160 — plenty of room.

Language note: English only. The current bio is in Portuguese, which breaks the brand's public-content
rule.

---

## Order of operations

Do the handle **last**, after everything else is in place — if the handle change fails validation you do
not want it half-applied.

1. **Profile** → `x.com/settings/profile`
   - Upload the banner
   - Upload the avatar
   - Display name → `Bandua Studio`
   - Bio → the text above
   - Location → `Sines, Portugal`
   - Website → `https://github.com/ribaudequin`
   - Save

2. **Username** → same page, *Username* field
   - Change to `banduastudio`
   - X will ask for your password to confirm

3. **Verify** — open `x.com/banduastudio` and check every field landed.

---

## Availability, checked

| Handle | Status |
|---|---|
| `@bandua` | **taken** |
| `@banduastudio` | **appears free** |
| `@bandua_studio` | appears free |
| `@banduastudios` | appears free |

Availability was probed by HTTP status only. **Confirm in the X interface before committing** — a 404
can also mean a suspended or protected account.

---

## Two warnings

1. **Changing the handle frees `@sinesdigital`.** Someone else can register it. There is no redirect on
   X, so every existing link to `x.com/sinesdigital` breaks — including the `twitter_username` already
   set on the GitHub profile, which will need updating to `banduastudio`.

2. **The old posts stay and are visible.** 667 posts from 2011–2015 about web design, 2015-era
   cryptocurrencies and two closed businesses. A visitor arriving from the new bio will scroll into
   them. That was a deliberate choice; revisit it if the mismatch becomes awkward.

---

## After this

Once the handle changes, two things elsewhere need the new value:

- GitHub profile `twitter_username` — currently `sinesdigital`
- `brand/BRAND.md` §9 and `brand/COMMUNICATION.md` — both document `@sinesdigital`

Say the word and I will update both.
