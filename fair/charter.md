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
  show-ring/
    setup-instructions.md             ← Show Ring Setup Instructions (livestock sale building)
  maps/                               ← binary assets, add manually
    Sheep_Goat_Barn_Map_REV6.png      ← sheep/goat barn map, REV6
    CusterCountyFairgroundsBriefing.pdf ← fairgrounds briefing
```

## Session Spine
At session open: `get_file_contents` repo HEAD before any build work. Pull `charter.md` and `notes.md` first. Spin-up baton is the only session state carrier between sessions.
