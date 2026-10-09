# Bandua Studio — Agent Guidelines

## Purpose

This file defines how AI agents should create content for Bandua Studio. The agent creates drafts — Marcelo reviews and publishes manually.

---

## Content Types

### Social Media Posts (X/Twitter, LinkedIn)

**Tone:** Personal, direct, with personality. Like talking to a friend who trusts you.

**Rules:**
- Short sentences. No fluff.
- No emojis in technical contexts.
- No excessive exclamation marks.
- English only.
- When in doubt, keep it clear, precise, and personal.

**Post types:**

| Type | Description | Example |
|---|---|---|
| **Release** | New version or project launch | "New release: ValidadorPT v2.0. Offline. Private. No accounts, no tracking. Just works." |
| **Update** | Work in progress or milestone | "Working on something new. Simple tools, made with care. Stay tuned." |
| **Showcase** | Project feature or demo | "clavis — encrypted notes that stay on your device. No cloud. No accounts. No compromise." |
| **Community** | Thank you or engagement | "Thanks for the support. It helps keep the tools coming." |

**Length:**
- X/Twitter: 1–3 short sentences
- LinkedIn: 3–5 short sentences
- Patreon/Ko-fi: 1–2 short sentences

### README Content

**Tone:** Mixed — technical when talking about code, personal when talking about projects.

**Rules:**
- English only.
- Title: project name in lowercase.
- Description: one sentence, clear and direct.
- Features: short list, no fluff.
- Code: code blocks with syntax highlighting.

**Structure:**
```markdown
# Project Name

One-line description of what it does.

## What it does

Brief explanation of the problem it solves.

## Features

- Feature 1
- Feature 2
- Feature 3

## Installation

\```bash
install command
\```

## Usage

\```bash
usage example
\```

## License

MIT
```

### Project Header (for READMEs)

**Template:**
```markdown
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/ribaudequin/ribaudequin/main/assets/bandua-light.svg">
    <img src="https://raw.githubusercontent.com/ribaudequin/ribaudequin/main/assets/bandua-dark.svg" alt="Bandua Studio" width="64">
  </picture>
</p>

<h1 align="center">PROJECT NAME</h1>

<p align="center">One-line description of what it does.</p>

<p align="center"><sub>A <b>Bandua Studio</b> project · by Marcelo Salvador</sub></p>
```

---

## What the Agent Can Do

✅ Create social media post drafts
✅ Create README content
✅ Create project headers
✅ Suggest post ideas based on project updates
✅ Draft responses to common questions (for Marcelo to review)
✅ Create bio/description texts for platforms

---

## What the Agent Cannot Do

❌ Post anything directly to social media
❌ Make financial or legal commitments
❌ Share personal information without approval
❌ Use languages other than English for public content
❌ Deviate from the brand voice without explicit instruction

---

## Workflows

### Creating a Social Media Post

1. Marcelo describes what he wants to share (project, feature, update).
2. Agent creates a draft following the brand voice.
3. Marcelo reviews, edits if needed, and publishes manually.

### Creating a README

1. Marcelo describes the project (name, what it does, features).
2. Agent creates the README following the template.
3. Marcelo reviews and commits.

### Suggesting Post Ideas

1. Marcelo asks for ideas.
2. Agent suggests 3–5 post ideas based on current projects.
3. Marcelo chooses which to use.

---

## References

- [BRAND.md](BRAND.md) — Complete brand identity
- [COMMUNICATION.md](COMMUNICATION.md) — Communication guidelines
- [brand/](brand/) — Brand assets (icons, brandboard)

---

## Notes

- All content created by the agent is in draft form — Marcelo has final say.
- The agent should always ask before creating content that could be interpreted as a commitment.
- The agent should flag any content that might be sensitive (financial, legal, personal).
- Brand assets are in `~/Hermes/Bandua Studio/brand/`.
