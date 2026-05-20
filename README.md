# Bayer Family Ops

**Repo:** `github.com/Ground3906/family-ops` (private)
**Local path:** `$env:BAYER_OPS_ROOT` -> `C:\dev\family-ops\`
**Maintained by:** Matt & Kalea Bayer
**Schema version:** 1 (see `prefs.md` for history)
**Last updated:** 2026-05-15

---

## What this is

Operational nerve center for the Bayer household. Structured Markdown and JSON files read by Al and the agent crew to support scheduling, farm ops, job hunt, family memory, and household logistics.

**This repo is the canonical source of truth.** Not Google Drive. Not OneDrive (retired 2026-05-15).

---

## Cold-session read order

1. This file (`README.md`)
2. `family.md` — who is in the family
3. `prefs.md` — conventions, sacred rules, standing decisions
4. `calendars.md` — Foreman reads this; any agent scheduling an event reads it too
5. `handoffs.json` — filter to `to: self`, `status: open`
6. `ccir-protocol.md` — household urgent-issue routing doctrine (notifier/arbiter pattern)

Then load agent-specific data files for the session domain.

---

## Rules

- **Agents propose; Matt commits.** Nothing is written to the repo silently.
- **One fact, one file.** Don''t restate roster data outside `family.md`. Reference by name or ID.
- **Secrets policy: NEVER STORE.** No passwords, API keys, SSNs, AWS account IDs.
- **Append-only for logs.** Status flags over deletes. Destructive actions are logged in `prefs.md`.
- **Confirm before shared calendar or state writes.** Same as the repo: propose, then commit.
- **24-hour clock, always.** `17:30`, not `5:30 PM`.
- **ISO dates, always.** `2026-05-15`.

---

## Agent roster

| Agent | Emoji | Domain |
|-------|-------|--------|
| Al | ?? | Orchestrator — default voice |
| Foreman | ?? | Calendar |
| Punch List | ?? | Family logistics, vehicles, maintenance |
| Whetstone | ?? | WGU study |
| Chow Hall | ?? | Meal planning |
| Mystery Ranch | ?? | Hunting |
| Stockyard | ?? | Livestock & farm ops (Edelweiss Farms LLC) |
| Rootstock | ?? | Forest garden, orchard, greenhouse |
| The Square | ?? | Material takeoff |
| The Mantel | ?? | Memory keeper |
| First Aid Kit | ?? | Health & medical |
| Footings | ?? | Job hunt |

Agent definition files (`al.md`, `foreman.md`, etc.) live at repo root. Data files follow the directory layout in `shared-state-schema.md`.

---

## Directory layout

See `shared-state-schema.md` for the full directory tree and per-file specs.
---

## Build status

| Wave | Status | Notes |
|------|--------|-------|
| Wave 1 | ? Complete | Charter, shared-state schema, crosstalk map |
| Wave 2 | ? Complete | Foreman v1 deep — 12/12 stress test passed |
| Wave 3 | ? Complete | Agent skeletons, foundational files |
| Wave 4 | ? Complete | Punch List MVP — deployed as Claude Code subagent, 7/7 stress test passed (2026-05-15) |
| Wave 4.1 | ?? Queued | Punch List tightening — 9 cosmetic/verbosity fixes |
| Wave 4.5 | ?? DIRE | Calendar visual widget — Kalea adoption is the bar. Slots before Whetstone. |
| Wave 5 | ? Pending | Whetstone (WGU study) + Stockyard/Rootstock v3 |
