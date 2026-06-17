# Using Synthadoc as the cube's knowledge layer

[Synthadoc](https://github.com/axoviq-ai/synthadoc) is an LLM "wiki compiler": it reads source
documents and synthesizes them into a cross-linked, queryable Markdown wiki where every claim
cites its source. For this cube it acts as the **research/reference layer** — it helps you find,
organize, and reason about cards. It is **not** a balancer, evaluator, or draft simulator
(those stay in `build_cube.py` / a spreadsheet over the JSON export).

> **Scope, in one line:** Synthadoc answers *"what cards do this and how do they connect"*;
> `build_cube.py` + queries over `cube.db` answer *"is the curve and ratio balanced."*
> The bridge between the two is Synthadoc's JSON export.

---

## What it lets us do

1. **Query the pool in plain language.** "List Green cards that gain stock on attack",
   "what removal exists below level 1", "cards that punish refresh" — instead of scrolling
   `index.html`. Answers cite the card.
2. **Archetype depth via the wikilink graph.** Cards sharing a mechanic auto-link into clusters.
   Export to GraphML, open in Gephi/yEd: dense clusters = draftable archetypes, thin/isolated
   nodes = lanes that need more enablers or payoffs before they're consistent.
3. **Knowledge-gap flagging = under-supported archetypes.** Ask about an archetype and a thin
   answer tells you the lane isn't deep enough yet.
4. **Orphan detection = dead cards.** A card that links to nothing (no shared mechanic, no
   archetype page) is a cut candidate.
5. **Design rationale lives next to the cards.** Author archetype briefs / power-tier notes as
   wiki pages; they cross-link to the card pages, with citations, so six months later you know
   *why* a card made the cut.
6. **Errata/version safety.** Contradiction detection flags a card whose current ruling differs
   from its printed text, so you don't design around an interaction that got errata'd away.
7. **Export as LLM context.** `export --format llms-full.txt` produces a clean, citation-threaded
   dump you can paste into any LLM (or a Discord rules bot) as a cube-aware assistant.

### Where it stops — use the existing tooling instead
- **No curve / ratio math.** Level-cost-color counts, "too many Lv3 finishers" → query `cube.db`
  directly or analyze the JSON export. (The cube template lives in `README.md`: Lv0 18 / Lv1 12 /
  Lv2 6 / Lv3 10 / Event 4 per color.)
- **No power evaluation or card ranking.** It organizes and explains; it doesn't judge balance.
- **No draft simulation / legality checking.**
- **Vision needs a paid key.** Card *images* require an Anthropic/OpenAI key. We don't need that —
  `cube.db` already holds ability text, so we ingest text and skip vision entirely.

---

## One-time setup

Synthadoc is already installed on this machine at `~/synthadoc` (editable install in
`~/synthadoc/.venv`). If setting up fresh elsewhere:

```bash
# PyPI is firewalled here — pip must go through the corporate proxy.
export HTTPS_PROXY=http://p1.riptidewsa1.nterprise.net:80
python3 -m venv ~/synthadoc/.venv
~/synthadoc/.venv/bin/pip install --proxy "$HTTPS_PROXY" -e ~/synthadoc
```

We use the **`claude-code` provider** (no API key — uses the Claude Code subscription).

---

## Build the cube wiki

From this repo:

```bash
SD=~/synthadoc/.venv/bin/synthadoc
export NO_PROXY=localhost,127.0.0.1          # keep loopback off the proxy

# 1. Turn cube.db into one Markdown source file per card
python3 tools/cube_to_synthadoc.py           # writes to synthadoc_sources/

# 2. Create a fresh (non-demo) wiki, then point it at the claude-code provider
$SD install weiss-cube --target ~/wikis --domain "Weiss Schwarz Draft Cube"
#   the install writes a default Gemini config; edit ~/wikis/weiss-cube/.synthadoc/config.toml:
#     default = { provider = "claude-code", model = "claude-sonnet-4-6" }
#   (scaffold during install is skipped without an API key — harmless, static templates are used)

# 3. Start the server (leave running in its own terminal)
$SD serve -w weiss-cube

# 4. Ingest the card source files (new terminal)
$SD ingest --batch synthadoc_sources/ -w weiss-cube

# 5. Lint — builds cross-links, flags orphans (dead cards) and gaps
$SD lint run -w weiss-cube
$SD lint report -w weiss-cube
```

> Tip: also ingest the per-color design docs (`plans/cube_*.md`) and the comprehensive WS rules
> so jargon and rulings cross-link to the cards.

---

## Daily use

```bash
SD=~/synthadoc/.venv/bin/synthadoc; export NO_PROXY=localhost,127.0.0.1

$SD query "Which Green cards generate or refund stock?" -w weiss-cube
$SD query "What punishes the opponent for refreshing?" -w weiss-cube
$SD web -w weiss-cube                                   # browser chat UI

# Archetype-depth graph (open in Gephi / yEd)
$SD export --format graphml --output exports/cube.graphml -w weiss-cube

# Structured data for curve/ratio analysis or feeding another LLM
$SD export --format json       --output exports/cube.json    -w weiss-cube
$SD export --format llms-full.txt --output exports/cube.txt   -w weiss-cube
```

---

## Notes / gotchas
- Re-run `tools/cube_to_synthadoc.py` + `ingest --batch` whenever `cube.db` changes; ingest
  dedups by content hash, so unchanged cards are skipped (cheap).
- `build_cube.py` remains the source of truth for *what's in the cube*. Synthadoc is a derived,
  read-mostly view for research — don't hand-edit card facts in the wiki.
- Server binds localhost only. From WSL, reach it from the Windows browser via `http://localhost:7070/app`.
