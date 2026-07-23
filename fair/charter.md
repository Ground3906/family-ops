# Custer County Fair — Project Charter

## What This Is
Fair Board operational support for Matt Bayer, Custer County Fair Board member. Covers show ring setup, barn mapping, exhibitor management, sale day logistics, and board proposals.

## Repo Pattern
- Repo: `Ground3906/family-ops`, path: `/fair/`
- SSI: repo is truth; PK stays starved
- Binary assets (maps, schedules, PDFs) live in `/fair/maps/` — cannot push via MCP text tool, upload manually through the GitHub web UI
- GitHub cannot hold an empty directory: a folder exists only once a file is committed into it
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
  rulebooks/                          ← rulebooks subsystem (parallel workstream)
  maps/                               ← binary visual assets, manual upload
    README.md                         ← asset index, update when assets are added or revised
    Sheep_Goat_Barn_Map_REV6.png      ← sheep/goat barn, REV6. BASELINE for optimization-brief.md
    Fair_Events_Schedule_2026.png     ← 2026 Fair Events schedule, July 13-18
    CusterCountyFairgroundsBriefing.pdf ← fairgrounds briefing (not yet uploaded)
```

## Known Gaps
- `maps/CusterCountyFairgroundsBriefing.pdf` — referenced in the maps index but not yet uploaded to the repo. Binary, manual upload required.

## Session Spine
At session open: `get_file_contents` repo HEAD before any build work. Pull `charter.md` and `notes.md` first. Spin-up baton is the only session state carrier between sessions.
