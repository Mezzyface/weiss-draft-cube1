#!/usr/bin/env python3
"""Export data/cube.db into one Markdown file per card for Synthadoc ingest.

Each card becomes a self-contained source document with YAML-ish frontmatter (so
cube_color/role/section/level are queryable) and a prose body describing the card and
its ability. Synthadoc reads these, synthesizes a cross-linked wiki, and auto-links
cards that share mechanics/roles.

Usage:
    python3 tools/cube_to_synthadoc.py            # -> synthadoc_sources/
    python3 tools/cube_to_synthadoc.py OUTDIR     # custom output dir
"""
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "data" / "cube.db"
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "synthadoc_sources"


def slug(cardno: str, name: str) -> str:
    base = f"{cardno}-{name}".lower()
    base = re.sub(r"[^a-z0-9]+", "-", base).strip("-")
    return base[:80] or "card"


def card_doc(r: sqlite3.Row) -> str:
    relabel = (r["relabel_notes"] or "").strip()
    cube_c, printed_c = r["cube_color"], r["printed_color"]
    recolor = f" (recolored from {printed_c})" if printed_c and printed_c != cube_c else ""
    lines = [
        "---",
        f"cardno: {r['cardno']}",
        f"name: {r['name']}",
        f"cube_color: {cube_c}",
        f"printed_color: {printed_c}",
        f"section: {r['section']}",
        f"role: {r['role']}",
        f"level: {r['level']}",
        f"cost: {r['cost']}",
        f"power: {r['power']}",
        f"soul: {r['soul']}",
        f"trigger: {r['trigger']}",
        f"count: {r['bundle_count']}",
        "---",
        "",
        f"# {r['name']} ({r['cardno']})",
        "",
        f"A **{cube_c}** {r['section']} card in the draft cube{recolor}, "
        f"filling the **{r['role']}** role. "
        f"Level {r['level']}, cost {r['cost']}, power {r['power']}, soul {r['soul']}, "
        f"trigger {r['trigger']}. Included at {r['bundle_count']} cop"
        f"{'y' if str(r['bundle_count']) == '1' else 'ies'}.",
        "",
        "## Ability",
        "",
        (r["ability"] or "(no ability text)").strip(),
    ]
    if relabel:
        lines += ["", "## Cube changes", "", relabel]
    # Universal-trait/name rule applies to every card in this cube model:
    lines += [
        "",
        "## Format note",
        "",
        "Per the cube's Toyo model, all traits and all name references are treated as "
        "universal: every character counts as having every trait, and 'your other <X>' / "
        "named combos respond to any card.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    if not DB.exists():
        sys.exit(f"cube.db not found at {DB} — run build_cube.py first.")
    OUT.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    rows = con.execute("SELECT * FROM cube ORDER BY cube_color, section, level, name").fetchall()
    written = 0
    for r in rows:
        path = OUT / f"{slug(r['cardno'], r['name'])}.md"
        path.write_text(card_doc(r), encoding="utf-8", newline="\n")
        written += 1
    print(f"Wrote {written} card source files to {OUT}")
    print(f"Next: synthadoc ingest --batch {OUT} -w weiss-cube")


if __name__ == "__main__":
    main()
