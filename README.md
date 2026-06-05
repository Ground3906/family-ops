# Bayer Family Ops

**Repo:** `github.com/Ground3906/family-ops` (private)
**Local path:** `C:\dev\family-ops\` (Precision = dev, ThinkPad = server + binary archive)
**Maintained by:** Matt & Kalea Bayer
**Schema version:** 2 (see `prefs.md` for history)
**Last updated:** 2026-06-05

---

## What this is

Operational nerve center for the Bayer household. Structured Markdown and JSON/JSONL files read by Al and the agent crew to support scheduling, farm ops, family memory, meals, and household logistics. See the Charter for the Vision and the Three-Layer Architecture.

**This repo is the canonical source of truth for structured data.** Binaries do not live here.

- **Repo (this)** — structured truth: Markdown doctrine, JSON state, JSONL event logs, the widget. Text only.
- **Binary archive** — repair-order PDFs, insurance docs, scanned recipe cards, photos. These live on the ThinkPad 2TB archive, transported there via a shared **OneDrive** folder (M365 Family). OneDrive is the binary-archive transport only; it is not a second source of truth. (This supersedes the earlier "OneDrive retired 2026-05-15" note — that retirement was OneDrive as a *truth* store, which still holds. Binaries that the repo should never carry now ride OneDrive to the archive.)

---

## Doctrine

See [`bayer-family-ops-charter.md`](bayer-family-ops-charter.md). Universal working-style and data-handling rules (the SPINE: layered data, data shape, extract-then-file) live in Profile.

---

## Agent roster

Priority order. Al is the orchestrator, outside the ranking.

| # | Agent | Emoji | Domain |
|---|-------|-------|--------|
| — | Al | 🔧 | Orchestrator — default voice |
| 1 | Chow Hall | 🍴 | Meals — the keystone *(she)* |
| 2 | Punch List | 🏠 | Family logistics, vehicles, maintenance |
| 3 | Foreman | 📅 | Calendar |
| 4 | Stockyard | 🐷 | Livestock & farm ops (Edelweiss Farms LLC) — *durability-gated* |
| 5 | IFAK | 🩺 | Health & medical |
| 6 | Rootstock | 🌱 | Forest garden, orchard, greenhouse |
| 7 | Mystery Ranch | ⛺ | Hunting |
| 8 | Mantle | 📖 | Memory keeper / legacy |
| 9 | Ledger | 💼 | Financial — Edelweiss Farms LLC books *(unbuilt)* |

**Struck (2026-06-05):** Whetstone (own project), The Square (own project if needed for bridge work), Footings (not a household concern).

Agent definition files (`al.md`, `foreman.md`, etc.) live at repo root. Data files follow the directory layout in `shared-state-schema.md`.

---

## Directory layout

See `shared-state-schema.md` for the full directory tree and per-file specs.
