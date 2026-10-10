# Ko-fi — @A0383T5

Read from the live page on 2026-10-09.

Page: `ko-fi.com/A0383T5`

---

## Current state

| Field | Now | Target |
|---|---|---|
| Page name | `ribaudequin` → **now `Bandua Studio`** | done |
| About | `Creating Software` | the text below |
| Avatar | uploaded 2026-08-21 | `avatar-teal-400.png` |
| Cover image | **none** | `banners/kofi-1200x400.png` |
| Website link | `github.com/ribaudequin` | keep |
| Category | `Software` | keep |
| Goal | `Claude Pro` — **removed** | done |

**The name is the GitHub username, not the brand.** `ribaudequin` is your GitHub handle; a visitor
arriving from the X or LinkedIn profile has no way to connect it to Bandua Studio. This was the single
most important change here, and it is done — the page now reads "Buy Bandua Studio a Coffee".

**Correction: Ko-fi does have a cover image.** I wrote earlier that it had none. It does — Ko-fi's own
panel offers *Add cover image*, and its help centre gives the specification: **1200 × 400 px, 3:1 ratio,
under 8 MB, JPEG or PNG**.

The asset for it already exists and matches exactly: `profiles/banners/kofi-1200x400.png`, measured at
1200 × 400 with a 3.00:1 ratio.

---

## Files to upload

| Field | File | Size |
|---|---|---|
| Avatar | `profiles/avatars/avatar-teal-400.png` | 400 × 400 |
| Cover image | `profiles/banners/kofi-1200x400.png` | 1200 × 400, 3:1 |

Use **teal** for the avatar. Ko-fi's dark theme surrounds it with a dark surface, where a Deep avatar
would need its rim to read at all.

### The cover survives Ko-fi's mobile crop

Ko-fi crops the cover's sides on mobile. Measured on the actual file:

| Check | Result |
|---|---|
| Lockup position | x 362–839 of 1200 |
| Left / right margin | 362 px / 360 px |
| Survives a 75 % centre crop | **yes** |
| Survives 85 % and 90 % crops | yes |
| Bottom-left zone (x 0–200, lower half) | **0 content pixels** — clear for the avatar overlay |

---

## Page name — copy exactly

```
Bandua Studio
```

13 characters.

---

## About — copy exactly

```
Creating software — small, local, private tools.
```

48 characters. Ko-fi's About field accepts more, but short reads better under the page name.

If you want the projects visible here too, this also fits:

```
Creating software — small, local, private tools.

clavis · epub-library-manager · ValidadorPT

No cloud. No accounts. No compromise.
```

---

## The goal — decided: remove it

The page runs a goal: **"Claude Pro", 0%**.

**Decision: remove the goal entirely.** Not replace it, not change it.

The reasoning, which is sounder than my first recommendation:

A goal is an **implicit promise**. It tells visitors "this money is for X, and when we reach it, X
happens". That creates an obligation the page then has to honour — and the failure mode is worse than
having no goal at all. If the goal sits at 99 % for two years, the page shows a permanently unmet
promise to every visitor. If it is never reached, it is a visible failure.

Without a goal, a donation is simply support for work that already exists. No counterpart to deliver, so
no debt.

| | With a goal | Without a goal |
|---|---|---|
| Promises something | Yes — implicitly | No |
| If it reaches 99 % and stalls | Stranded, publicly visible | Not applicable |
| If it is never reached | A failed goal, permanently on display | Not applicable |
| What a supporter expects | The objective to be met | Nothing beyond the support |

I had suggested switching the goal to code-signing certificates, on the grounds that it gives supporters
something concrete. That reasoning was incomplete: a certificate is a real cost, but a goal turns it
into a commitment, and the commitment is the part that can go wrong.

### The structural reason no goal fits here

It is not that the alternatives are expensive. It is that **every cost this work has is recurring**:

| Cost | Nature |
|---|---|
| Code-signing certificates | per **year** |
| Claude Pro | per **month** |
| Domain and hosting | per **year** |

**A goal is a finish line. A recurring cost never crosses it** — there is no moment at which it is done.
A goal for an annual cost would reach 100 % and reset to 0 % the following year, which is a strange
thing to display to supporters.

So no goal works here, and the reason is structural rather than a matter of choosing a better one.

**When a goal *would* be right:** a single, bounded, one-off cost with a definite end — a specific piece
of equipment, a one-time licence, a migration. Something that can be finished and then closed. None of
the current costs are that.

**How to remove it:** `Your Page` → the Goal → the three dots (⋯) → **Remove Goal**.

Ko-fi documents three options on that menu — *Edit*, *Set New Goal*, *Remove Goal*.

---

## A finding worth acting on

The page has **13 supporters**, and the public feed shows the messages they left. Two are substantive:

> "Thank you for the linux-kernel video. I was having a low wifi speed (75-100) and I was wondering how
> to fix it. After three weeks of looking for an answer, I found your video easy to follow for a beginner
> in Linux like me. Now the wifi speed is over 400... Thank You again!"

> "Thanks for your site! Using your instructions, I was able to install BSDs with a GUI, where I had been
> unsuccessful before - FreeBSD on a laptop and OpenBSD in a VM (for now) on a desktop."

These are people who supported you for **Linux and BSD tutorials**, not for Bandua Studio. The page name
change will not erase that history, but it does mean new visitors see a brand page whose supporters
arrived for something else.

That is not a reason to avoid the change — it is the same situation as the X account's old posts. Worth
knowing, and worth deciding whether the About text should acknowledge it.

---

## Two payment settings worth checking

### Contributor mode — may be taking 5 % of your tips

Ko-fi's own help centre states:

> "Everyone who joins Ko-fi now starts with **Contributor status**... That includes a **5 % service fee on tips**.
> You can opt out anytime and keep tips completely free."

Contributor mode is **on by default** for new accounts. Turning it off is what delivers the 0 % on tips
that Ko-fi advertises. It is a legitimate programme — you are funding Ko-fi — but it is opt-out, not
opt-in.

**Where:** `Settings` → `Payment` → `Contributor` → toggle off.

**Two honest caveats:**

- I cannot see whether it is on for this account. The page has supporters from before, so it may already
  be off. Only the payment panel shows it.
- It does not apply retroactively to one-off donations already made, and Ko-fi notes that memberships or
  recurring tips **started** while Contributor stay at 5 % even after you switch off.

### Currency — USD is fine

A supporter pays in their own currency and Ko-fi converts automatically to the creator's chosen one.
There is no loss from running the page in USD; a Portuguese supporter simply pays in EUR and it
converts. If most supporters turn out to be European, setting the account currency to EUR avoids one
conversion step — but it is a payment setting, not a page setting, and not urgent.

---

## Tip amounts — $3 is right

The single default is **$3**, which is Ko-fi's own default price for one "coffee" and the most-used
value on the platform. Industry data puts **72 % of all tips on preset buttons** and the average tip at
**$4.85**.

So $3 is not too little — it is the standard. Adding more presets creates choice paralysis for no gain,
and the free-amount field already covers anyone who wants to give more.

**If you want one more**, $5 is the only addition worth making — the common middle option. Not necessary.

---

## Order of operations

1. ~~Page name~~ → done: `Bandua Studio`
2. ~~Goal~~ → done: removed
3. **About** → the text above (currently `Creating Software`)
4. **Cover image** → upload `profiles/banners/kofi-1200x400.png`
5. **Avatar** → upload `profiles/avatars/avatar-teal-400.png`
6. **Website** → already `github.com/ribaudequin`; keep
