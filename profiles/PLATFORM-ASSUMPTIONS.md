# Platform assumptions — verify, never assume

A record of three claims I made about platform behaviour that were **wrong**, all in one session. They
share one cause, and it is worth naming so it does not repeat.

---

## The three errors

| Platform | What I claimed | What is true |
|---|---|---|
| **LinkedIn** | The profile slug is fixed at creation and cannot be changed | **It can be edited** to a custom value, rate-limited to roughly five changes per six months |
| **Ko-fi** | Ko-fi has no cover image | **It does** — 1200 × 400, 3:1, under 8 MB |
| **Patreon** | The handle is fixed and cannot be changed | **It can be changed**, and Patreon redirects the old vanity URL |

In every case the owner corrected me. In every case I had stated it as fact.

---

## The cause

**I generalised from one platform's rule to another.** Specifically:

- LinkedIn's rule is *one account per person*. That is a rule about **people**. I applied it to the
  profile **URL**, which is a different thing with a different rule.
- I assumed "profile URL" behaved the same way everywhere, and that the platform with the most
  restrictive-sounding rule set the pattern.
- For Ko-fi and Patreon I assumed absence of a feature rather than checking the panel, which the owner
  could see and I could not.

None of these were reading failures. They were **assumptions about product behaviour presented as
verified fact.**

---

## The rule that follows

**Platform capabilities must be checked, not inferred.** Before stating that a platform cannot do
something:

1. Search the platform's **own help centre** for the specific field or feature.
2. If the panel is visible to the owner but not to me, **ask them to look** rather than assume.
3. Distinguish clearly between *"the documentation says"* and *"I believe"*. If it is the second, say so.

A related trap: **do not transfer a rule from one platform to another.** X, LinkedIn, Ko-fi and Patreon
each have different policies on handles, URLs, redirects and covers. X does not redirect a changed
handle; Patreon does. LinkedIn allows a URL edit; X allows it once per some period. None of this is
guessable.

---

## What each platform actually does with a changed handle

Verified where possible:

| Platform | Old handle after a change |
|---|---|
| **X** | `x.com/sinesdigital` → **404**. No redirect. |
| **LinkedIn** | Old slug → 404. No redirect. |
| **Patreon** | `patreon.com/ribalinux` → **redirects** to the new one. Links keep working. |

So the cost of changing a handle is **not** uniform, and it cannot be assumed in either direction.
