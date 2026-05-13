# Bayer Family Ops — Shared State Schema v1

**Location:** Google Drive → `/Family Operations/`
**Access:** Matt + Kalea (full). Agents read via Google Drive MCP or local sync.
**Source-of-truth rule:** Each fact lives in exactly one file. Other agents reference, never duplicate.

---

## Top-Level Layout

```
/Family Operations/
├── README.md                  ← What this is + how agents use it
├── family.md                  ← Roster, ages, allergies, prefs
├── prefs.md                   ← Household decisions, schema versions
├── calendars.md               ← Google Calendar map (for Foreman)
├── handoffs.json              ← Cross-agent inbox
│
├── punch-list/
│   ├── tasks.json             ← Open/in-progress/done tasks
│   └── vehicles.json          ← Service intervals, registration
│
├── whetstone/
│   ├── progress.md            ← Domain coverage, weak clusters
│   └── exam-logs/             ← Per-exam transcripts
│
├── mystery-ranch/
│   ├── seasons.md             ← Rifle seasons, draws by year
│   ├── blackouts.md           ← Sacred blocks for Foreman
│   ├── draws.json             ← Active applications
│   └── scouting.md            ← Recon log
│
├── chow-hall/
│   ├── meal-plan.md           ← Current + upcoming weeks
│   ├── pantry.json
│   └── freezer.json           ← Game meat tracker
│
├── first-aid/                 ← SENSITIVE — see access notes
│   ├── people/<initials>.md
│   ├── medications.json
│   └── appointments.md
│
├── footings/
│   ├── pipeline.json          ← Applications by stage
│   ├── targets.md             ← Employer research
│   ├── certs.md               ← AWS / Azure progress
│   └── resume/                ← Versioned résumés
│
├── square/
│   └── projects/<name>/       ← Plan PDFs + takeoff outputs
│
└── mantel/
    ├── moments.md             ← Day-to-day worth keeping
    ├── stories/               ← Long-form
    └── archive/               ← Photos, mementos
```

---

## File Specs

### `README.md`
Single page describing this directory + the rules below. First file an agent should read on a cold session.

### `family.md`
The roster. Single source of truth for who is in the family. Markdown, one section per person.

```markdown
## Matt
- Age 38, Marine veteran
- Allergies: none
- Notes: AWS cert pursuit; primary planner

## Kalea
- Age 38
- Allergies: TBD
- Notes: teaching schedule M/W 12:20–13:40
```

**Read by:** all agents.
**Written by:** Matt or Kalea via Al, with confirmation. Agents propose roster updates, never commit silently.

### `prefs.md`
Household-level decisions, schema versions, conventions. Not personal preferences (those live in `family.md`). Things like "we use 24h clock," "Sunday is sacred," schema version history, decision log for irreversible choices.

### `calendars.md`
The Google Calendar map. Names, owners, color codes, sacred blocks, event-tagging conventions. Read by Foreman before any calendar write. See Charter §Calendar Strategy for the structure.

### `handoffs.json`
Cross-agent inbox. Append-only by convention; entries marked `status: done` rather than deleted.

```json
{
  "version": 1,
  "entries": [
    {
      "id": "h-2026-05-13-001",
      "from": "punch-list",
      "to": "foreman",
      "created": "2026-05-13T14:22:00",
      "subject": "Truck oil change overdue (1200 mi past)",
      "payload": {
        "task_id": "t-0042",
        "vehicle": "F-250",
        "proposed_blocks": ["Tue 09:00", "Thu 14:00"]
      },
      "status": "open"
    }
  ]
}
```

**Read by:** every agent at session start (filter `to: self, status: open`).
**Written by:** any agent emitting a handoff.
**Closed by:** receiving agent after action — marks `status: done` with `closed_at`.

### `punch-list/tasks.json`
```json
{
  "version": 1,
  "tasks": [
    {
      "id": "t-0042",
      "title": "Truck oil change",
      "owner_agent": "punch-list",
      "owner_human": "Matt",
      "vehicle_ref": "F-250",
      "due": "2026-05-20",
      "status": "open",
      "notes": "Last service 2026-02-15, ~4500 mi ago"
    }
  ]
}
```

### `punch-list/vehicles.json`
```json
{
  "version": 1,
  "vehicles": [
    {
      "id": "F-250",
      "year": 2020,
      "registration_due": "2026-08-31",
      "inspection_due": "2026-08-31",
      "service_interval_mi": 5000,
      "last_service_date": "2026-02-15",
      "last_service_mi": 84200,
      "current_mi_estimate": 88700,
      "notes": "Diesel"
    }
  ]
}
```

### `whetstone/progress.md`
Domain coverage table, weak-cluster list, current exam target, dates, run-log summary. Detail per-exam goes in `exam-logs/<date>-<exam>.md` following Matt's documented protocol.

### `mystery-ranch/blackouts.md`
The sacred date ranges Foreman must protect.

```markdown
## 2026 Season

### 3rd Rifle (CO)
2026-11-07 → 2026-11-13
Block strength: HARD — no work, no study, no appointments

### 4th Rifle (CO)
2026-11-18 → 2026-11-22
Block strength: HARD

### Scouting weekend
2026-08-22 → 2026-08-23
Block strength: SOFT — work avoidable if needed
```

### `chow-hall/freezer.json`
Game meat inventory. Drives meal planning + butcher-trip timing.

```json
{
  "version": 1,
  "items": [
    {
      "kind": "elk",
      "cut": "backstrap",
      "qty_lb": 8,
      "harvested": "2025-11-09",
      "harvested_by": "Matt"
    }
  ]
}
```

### `first-aid/` — SENSITIVE
Sharing access in Google Drive *is* access control. Default to Matt + Kalea only. Extending access to anyone or anything else = deliberate decision logged in `prefs.md`. Tone-drop applies inside this directory.

- `people/<initials>.md` — one file per family member. Med history, immunizations, conditions.
- `medications.json` — current Rx, doses, refills.
- `appointments.md` — upcoming, cross-references Foreman.

### `footings/pipeline.json`
```json
{
  "version": 1,
  "applications": [
    {
      "company": "Coalfire",
      "role": "Cloud Engineer (FedRAMP)",
      "stage": "applied",
      "applied": "2026-05-01",
      "notes": "Referral via X"
    }
  ]
}
```

### `mantel/moments.md`
Append-only. Sacred and everyday. Date-stamped. The Loretto Chapel entry (2026-04-25) is the gold standard for how to treat the sacred ones — tone-drop on contact.

---

## Conventions

- **Times: 24-hour clock, always.** `17:30`, not `5:30 PM`.
- **Dates: ISO format.** `2026-05-13`.
- **Schema version: every JSON file has a `version` field.** Bump it on breaking changes; note the migration in `prefs.md`.
- **Source of truth: one file per fact.** Don't restate roster details outside `family.md`. Reference by ID.
- **Secrets policy: NEVER STORE.** No AWS keys, account IDs, passwords, SSNs. Sensitive medical info lives in `first-aid/` with restricted access.
- **Append-only mindset for logs.** Delete is destructive; status flags are reversible.
- **Confirmation before writes to anything shared.** Agents propose, human commits.

---

## Bootstrap Order

When standing this up from scratch:

1. Create `README.md`, `family.md`, `prefs.md`, `calendars.md`, and an empty `handoffs.json`.
2. Foreman first (v1 deep) → drives `calendars.md` to completeness.
3. Punch List MVP → `tasks.json` + `vehicles.json`.
4. Whetstone MVP → `progress.md`.
5. Remaining agents per Charter §Build Order.
