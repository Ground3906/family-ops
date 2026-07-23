# Custer County Fair — Project Charter

## What This Is
Fair Board operational support for Matt Bayer, Custer County Fair Board member. Covers show ring setup, barn mapping, exhibitor management, sale day logistics, and board proposals.

## Repo Pattern
- Repo: `Ground3906/family-ops`, path: `/fair/`
- SSI: repo is truth; PK stays starved
- Binary assets (barn maps, PDFs): referenced below; add manually to `/fair/maps/` — cannot push via MCP text tool
- Session state: spin-up prompt only — never in markdown files

## Directory Structure
```
fair/
  charter.md                          ← this file
  notes.md                            ← running open items and board proposals
  2026/
    beef-showmanship-split.md         ← private exhibitor list (contact info included)
    beef-showmanship-split-public.md  ← public exhibitor list (no contact info)
    hotwash-leave-behind.html         ← 2026 board hot wash leave-behind (printable, notes boxes)
  show-ring/
    setup-instructions.md             ← Show Ring Setup Instructions (livestock sale building)
  swine-show/
    handoff.md                        ← 2026 Swine Show fairboard handoff doc (cadence, stall policy, capital asks)
  sheep-goat-barn/
    optimization-brief.md             ← layout optimization design brief for Cowork handoff (constraints, phases, deliverable spec)
  maps/                               ← binary assets, add manually
    Sheep_Goat_Barn_Map_REV6.png      ← sheep/goat barn map, REV6 (BASELINE for optimization brief)
    CusterCountyFairgroundsBriefing.pdf ← fairgrounds briefing
```

## Known Gaps
- `maps/Sheep_Goat_Barn_Map_REV6.png` — referenced by `sheep-goat-barn/optimization-brief.md` but **not yet uploaded to repo**. Binary, manual upload required. Cowork cannot work from source until this lands.
- Fair schedule (2026 Fair Events, July 13-18) — used to build the phase sequence in the optimization brief, not yet in repo.

## Session Spine
At session open: `get_file_contents` repo HEAD before any build work. Pull `charter.md` and `notes.md` first. Spin-up baton is the only session state carrier between sessions.
