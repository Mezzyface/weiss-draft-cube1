# Weiss Schwarz Draft Cube

A custom **4-color draft cube** for Weiss Schwarz, built on the "Toyo-club" model: minimal custom changes to real cards, with universal traits and name-references baked in, and one light theme per color. The goal is a balanced, draftable environment using mostly-unmodified real cards.

**[View the card gallery](https://USERNAME.github.io/weiss-draft-cube/)** *(enable GitHub Pages, then update this link)*

## The model

Every card is a real Weiss Schwarz card with three controlled changes only: **traits, color, and card references**. Power levels are kept as printed. Two blanket rules are baked into every card so the format stays simple for a first pass (and can be tightened later):

- **All traits are universal** - every character counts as having every trait.
- **All name references are universal** - "your other <X>" and named combos respond to any card.

This lets combo and synergy cards function without bespoke rewrites, while keeping printed numbers untouched for balance.

## Structure

Each color is **50 cards** on a fixed template, plus **2 shared core cards** given to every color:

| Section | Count |
|---|---|
| Level 0 | 18 |
| Level 1 | 12 |
| Level 2 | 6 |
| Level 3 | 10 |
| Event | 4 |
| **Total** | **50** |

Copy cap is 4, except the Level 1 CX combo at 6. Each color gets one soul-trigger Level 0.

## Color themes

| Color | Light lean |
|---|---|
| Yellow | Events / direct effects |
| Blue | Markers / tempo |
| Red | Memory |
| Green | Stock / ramp |

## Repo contents

- `index.html` - self-contained static site showing every chosen card, grouped by color and level, with copy counts and recolor tags. Card images load from the official ws-tcg.com CDN.
- `data/cube.db` - SQLite database of the committed cube (card no, name, cube color vs printed color, section, role, count, stats, ability text).
- `build_cube.py` - builds `cube.db` from the card list (the source of truth for what's in the cube).
- `plans/` - per-color design docs (`cube_yellow.md`, etc.) and the overall `cube_plan.md`.

## Rebuilding the database

`build_cube.py` reads card details from a local `cards.db` scrape (not included - it's large and contains card text) and writes `cube.db`. The `CUBE` list inside it is the canonical definition of the cube.

## License / disclaimer

Cube design, scripts, and site code: MIT (see `LICENSE`). Weiss Schwarz and all card names, text, and artwork are (c) Bushiroad. This is a non-commercial fan project, not affiliated with or endorsed by Bushiroad. Card images are not redistributed here - the site loads them from official sources.
