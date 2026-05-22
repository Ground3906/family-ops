# Bayer Family Ops — Shared State Schema v1

**Location:** Git repo → `C:\Users\ThinkPad X1 Carbon\Documents\family-ops\` (remote: `github.com/Ground3906/family-ops`, private)
**Access:** Matt + Kalea (full). Agents read from local repo clone. OneDrive scratch location retired 2026-05-15. Google Drive previously named as canonical — superseded; Git only.
**Source-of-truth rule:** Each fact lives in exactly one file. Other agents reference, never duplicate.

---

## Top-Level Layout

```
/family-ops/
├── README.md                  ← What this is + how agents use it (cold-session read first)
├── al.md                      ← Al orchestrator definition
├── foreman.md                 ← Foreman calendar agent definition
├── [other agent .md files]    ← Agent definitions live at repo root
│
├── ccir-protocol.md           ← Household urgent-issue routing doctrine
├── crosstalk-handoff-map.md   ← Inter-agent routing patterns
├── fleet-state-v1.md          ← Rolling stock & equipment master record
│
├── family.md                  ← Roster, ages, allergies, prefs
├── prefs.md                   ← Household decisions, schema versions
├── calendars.md               ← Google Calendar map (for Foreman)
├── handoffs.json              ← Cross-agent inbox
│
├── docs/
│   └── manuals/               ← Vehicle/equipment maintenance PDFs (untracked → tracked 2026-05-15)
│
├── punch-list/
│   ├── tasks.json             ← Open/in-progress/done tasks
│   ├── vehicles.json          ← Service intervals, registration
│   ├── documents.md           ← ID/registration/insurance/military/farm/property/financial tracker
│   └── wyatt-licensing.md     ← CO GDL timeline + Foreman prompt schedule for Wyatt
│
├── whetstone/
│   ├── progress.md            ← Domain coverage, weak clusters
│   └── exam-logs/             ← Per-exam transcripts
│
├── mystery-ranch/
│   ├── seasons.md             ← Rifle seasons, draws by year
│   ├── blackouts.md           ← Sacred blocks for Foreman (Matt-only scope)
│   ├── draws.json             ← Active applications
│   └── scouting.md            ← Recon log
│
├── stockyard/                 ← Edelweiss Farms livestock ops
│   ├── eggs-log.csv           ← Daily egg counts (exported from widget)
│   ├── flock-config.md        ← Y1/Y2 hen split, breeds, refresh dates
│   ├── pigs.md                ← Current pigs, feed schedule, weigh-ins
│   ├── turkeys.md             ← Spring raise tracking
│   └── slaughter-log.md       ← Historical processing records
│
├── rootstock/                 ← Edelweiss Farms growing ops
│   ├── plantings.md           ← Trees, shrubs, perennials with dates planted
│   ├── garden-plan.md         ← Annual veg succession, frost windows
│   ├── greenhouse.md          ← Build status, then operation log
│   ├── gardyn-roster.md       ← Indoor hydroponic inventory (Matt-updated)
│   └── harvest-log.md         ← What''s coming in, when, how much
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
Single page describing this repo + the rules. First file an agent reads on a cold session.

### `ccir-protocol.md`
Household-wide urgent-issue routing doctrine. Notifier/arbiter pattern, CCIR triggers by domain, edge cases, decision log. Read by **all agents** at session start. Vocabulary (CCIR, notifier, arbiter) is locked in `prefs.md`.

### `family.md`
The roster. Single source of truth for who is in the family and the extended-network operational map (anchor houses, backup-adult tier hierarchy). Markdown, one section per person/household.

```markdown
## Matt
- DOB: 1987-12-07 (age 38)
- Background: Marine veteran
- Notes: AWS cert pursuit; primary planner

## Kalea
- DOB: 1988-05-27
- Notes: teaching schedule M/W 12:20–13:40; USMC Reserve IMA MAJ MARFORPAC
```

**Read by:** all agents.
**Written by:** Matt or Kalea via Al, with confirmation. Agents propose roster updates, never commit silently.

### `prefs.md`
Household-level decisions, schema versions, conventions. Not personal preferences (those live in `family.md`). Vocabulary lock, sacred blocks, Equipment Access Principle, Agent Personality Routing, Anti-Atrophy (Option C), Renewal Watch, Tow Protocol, Decision Log, Schema History.

### `calendars.md`
The Google Calendar map. Names, owners, color codes, sacred blocks, event-tagging conventions. Read by Foreman before any calendar write. See Charter §Calendar Strategy for the structure.

### `crosstalk-handoff-map.md`
Inter-agent routing patterns, Bedrock Rules (including Option C reminder ownership), routing matrix, canonical patterns, sacred-block refusal protocol, owner-table.

### `fleet-state-v1.md`
Master record for rolling stock and equipment. Asset summary, per-asset detail (NV3500, Ford F-250, Dodge Ram, Chevy Tahoe, Gehl skid steer, deck trailer, Jackson trailer, ATV), service histories, open items, registration cycles, preferred shops. Owned by Punch List.

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

### `punch-list/documents.md`
Tracker skeleton for IDs, registrations, insurance, military, hunting, farm/LLC, property, financial. Opportunistic capture model — populated as documents surface, not by hunting. Foreman derives renewal-prompt milestones from this file. Sensitive numbers (SSN, account #, passwords) excluded permanently.

### `punch-list/wyatt-licensing.md`
Full CO GDL timeline for Wyatt: phases 0-6, HB24-1021 reference, course-start window (2026-10-22 to 2026-12-22), Foreman prompt schedule. Voice belongs to Punch List under Option C.

### `whetstone/progress.md`
Domain coverage table, weak-cluster list, current exam target, dates, run-log summary. Detail per-exam goes in `exam-logs/<date>-<exam>.md` following Matt''s documented protocol.

### `mystery-ranch/blackouts.md`
The sacred date ranges Foreman must protect — **Matt-only scope** per `prefs.md`. Kalea, kids, household continue normally during these windows.

```markdown
## 2026 Season

### 3rd Rifle (CO)
2026-11-07 → 2026-11-13
Block strength: HARD — Matt-only

### 4th Rifle (CO)
2026-11-18 → 2026-11-22
Block strength: HARD — Matt-only

### Scouting weekend
2026-08-22 → 2026-08-23
Block strength: SOFT — work avoidable if needed
```

### `stockyard/eggs-log.csv`
Daily egg count history. Exported from the egg tracker widget. The Bayer flock never has zero-egg days — blank entries = uncollected/unrecorded, not real zeros. Stockyard analytics treat missing dates as null, not zero.

```csv
date,count,notes
2026-05-10,11,
2026-05-11,12,
2026-05-12,,uncollected
2026-05-13,13,
```

### `stockyard/flock-config.md`
Hen roster + breed + age cohorts. Default operating model: 50/50 Y1/Y2 split, half the flock refreshed annually.

```markdown
## Current Flock — as of 2026-05-13

- Total layers: TBD
- Year 1 cohort: TBD (hatched ~Mar 2026)
- Year 2 cohort: TBD (hatched ~Mar 2025)
- Last refresh date: TBD
- Next refresh planned: ~Mar 2027

## Production Model Constants
(See `stockyard-widget.md` for full reference)
- Y1 hens: 0.80 eggs/day at peak
- Y2 hens: 0.65 eggs/day at peak
- Seasonal modifier table maintained in widget
- Altitude factor: TBD after first full year of data
```

### `rootstock/plantings.md`
Trees, shrubs, perennials. Dates planted, current zone classification, microclimate notes. Stockyard-style historical record for the orchard and forest garden.

```markdown
## 2026 Plantings (year planted)

### Fruit trees
- Honeycrisp apple — 7-8ft — planted 2026-05
- McIntosh apple — 7-8ft — planted 2026-05
- Loring peach — 7-8ft — planted 2026-05 (zone 5-8 — stretch at 4a)
- Arctic Honey jujube — 7-8ft — planted 2026-05 (zone 6+ — biggest gamble)
- Dwarf North Star cherry — planted 2026-05
- 2x mulberry — planted 2026-05

### Shrubs / bushes
- Pink Lemonade blueberry — 3gal — planted 2026-05 (needs pH amendment)
- 2x Regent serviceberry — small 3ft — planted 2026-05

### Brambles
- Black Hawk black raspberry — 3yr — planted 2026-05
- Fall Gold raspberry — 3yr — planted 2026-05
- Latham raspberry — 3yr — planted 2026-05
- Brandywine purple raspberry — 3yr — planted 2026-05

### Vines
- Issai kiwi — 1gal — planted 2026-05

## Site
- 1722 Edelweiss Dr, Westcliffe CO
- Elevation: 9000 ft exact
- Zone: 4a (effective 5a in south-facing HC container microclimate)
- Last frost: mid-to-late May
- First frost: early September
- ~100 days unprotected growing season
```

### `rootstock/gardyn-roster.md`
Indoor hydroponic inventory. Matt-updated when planting or harvesting. Gardyn appliance owns its own app and operational logic; this file is read-only awareness for Chow Hall.

```markdown
## Current Gardyn (as of YYYY-MM-DD)
- Position 1: basil — planted 2026-05-01 — harvestable ~2026-06
- Position 2: ...

## Harvested
- 2026-04-15 basil — used for pesto batch
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
The private repo *is* the access control layer for this directory. Default: Matt + Kalea only. Extending read/write access to anyone or anything beyond the private repo = deliberate decision logged in `prefs.md`. Tone-drop applies inside this directory — no Tool Time, no jokes, straight information.

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
- **Source of truth: one file per fact.** Don''t restate roster details outside `family.md`. Reference by ID.
- **Reminder ownership — Option C.** The agent that owns the work owns the reminder. Foreman owns calendar truth (the *when*); domain agents own voice and cadence (the *what* and *how*). See `prefs.md` and `crosstalk-handoff-map.md` Bedrock Rule #6.
- **Secrets policy: NEVER STORE.** No AWS keys, account IDs, passwords, SSNs. Sensitive medical info lives in `first-aid/` with restricted access. Document tracker (`punch-list/documents.md`) excludes high-sensitivity numbers by policy.
- **Append-only mindset for logs.** Delete is destructive; status flags are reversible.
- **Confirmation before writes to anything shared.** Agents propose, human commits.

---

## Bootstrap Order

When standing this up from scratch:

1. Create `README.md`, `family.md`, `prefs.md`, `calendars.md`, `ccir-protocol.md`, `crosstalk-handoff-map.md`, and an empty `handoffs.json`.
2. Foreman first (v1 deep) → drives `calendars.md` to completeness.
3. Punch List MVP → `tasks.json` + `vehicles.json` + `documents.md` + `wyatt-licensing.md`. References `fleet-state-v1.md`.
4. Whetstone MVP → `progress.md`.
5. Remaining agents per Charter §Build Order.

---

## Calendar Widget Schema (Wave 4.5+)

### `[CAL]` entry format
```
[CAL] YYYY-MM-DD TIME TITLE :: CATEGORY :: [optional attributes]
```

**Pill tokens** (who is involved):
- Individual: `[D]` Matt, `[K]` Kalea, `[W]` Wyatt, `[M]` Molly, `[R]` Rileigh, `[C]` Cullen, `[E]` Emmitt, `[B6]` baby boy
- Collective: `[FAM]` = all family members. Widget auto-generates minus pills for absent members.
- Extended: `[OMA]`, `[PAPA]`, `[GUEST]`

**Pill colors (locked):**
```
D=#CFB87C, K=#2a5fb8, W=#cc2233, M=#9944cc, R=#f040b8
C=#2a8a9a, E=#228844, B6=#faa030, OMA=#7755cc, PAPA=#58a080
GUEST=#E8DFC0, FAM=#7a7aaa
```

**Categories:**
- `:: liturgical` — Mass, feast days, sacred observances
- `:: kids` — children's activities
- `:: animals` — farm/livestock events
- `:: appointments` — medical, therapy, professional appointments
- `:: birthdays` — renders in header slot
- `:: holidays` — renders in header slot
- `:: misc` — general household
- `:: prompt` — reminders and milestone triggers. Pattern: `Title ⏰ :: prompt`. NOT an appointment. Never add `stripe=appt`.

**Optional attributes:**
- `span=YYYY-MM-DD` — event spans multiple days (end date)
- `travel=true` — person is physically away from home during span. Suppresses traveler's pill on overlapping events. Foreman always asks "Are they traveling?" when proposing multi-day absences.
- `flag=true` — unresolved conflict or logistics pending
- `location="..."` — renders in day detail panel only, EXCEPT for travel sports (swim meets, track, XC) where location renders on the tile
- `notes="..."` — day detail only, never on tile
- `stripe=appt` — colored appointment stripe

### Feast day format
```
[CAL] YYYY-MM-DD ALL-DAY ✝️ Saint Name 🍞 :: liturgical :: notes="food description"
```
Cross leads, bread closes. Food name in `notes=` only — never in title. Holy Days of Obligation always included regardless of food association.

### Prompt entry format
```
[CAL] YYYY-MM-DD ALL-DAY [PILL] Title ⏰ :: prompt
```

### Recurring entries
```
[CAL-RECUR weekly start=YYYY-MM-DD day=DOW] TIME TITLE :: CATEGORY
[CAL-RECUR monthly start=YYYY-MM-DD day=DOW week=N] TIME TITLE :: CATEGORY
```
