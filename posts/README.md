# Posts

One folder per publication, named by its date. Everything for that post lives together — the copy for
every platform and the images that go with it.

```
posts/
  README.md                        this file — the index
  TEMPLATE/                        copy this to start a new post
  2026-10-10-launch/
    post.md                        copy for all four platforms
    images/
      x-1600x900.png
      linkedin-1200x627.png
      patreon-1500x900.png
      kofi-1200x600.png
```

## Why by date

- **Nothing overwrites.** Each post gets its own folder, so regenerating images for a new post cannot
  touch an old one. (This project has already lost work once to two scripts writing to the same path.)
- **The archive is chronological.** Old posts stay readable as a record of what was said and when.
- **One post, one folder.** The copy and the images for a publication stay together.

## Naming

`YYYY-MM-DD-slug` — the date the post is **published**, not the date it was drafted. ISO order so the
folder list sorts itself chronologically.

## Index

| Date | Slug | Platforms | Status |
|---|---|---|---|
| 2026-10-10 | `launch` | X · LinkedIn · Patreon · Ko-fi | **published** |

## Starting a new post

```bash
cp -r posts/TEMPLATE posts/2026-11-01-something
```

Then fill in `post.md` and generate images:

```bash
/usr/bin/python3 scripts/generate-post-images.py 2026-11-01-something
```

The generator reads the platform list and writes into that folder's `images/`. Run it with no argument
to see the available posts.
