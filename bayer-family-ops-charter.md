# Bayer Family Operations — Charter v1.9

The foundational document for the household multi-agent system. Upload this to project knowledge. Updated as decisions are made.

**Last updated:** 2026-06-01 — v1.9: Wave 6.5 complete (Meal Planner + Widget Integration). Widget filename convention updated to `cal-widget-vX.X.html`. calendars.md schema additions: `[MEAL]` tag, `cancel=pending/confirmed`, `skip=` on CAL-RECUR. BUILD GATE and Item vs PQ naming locked in Profile (not restated here — Profile is the source).
**Prior:** 2026-05-27 — v1.8: Interaction Doctrine stripped to project-specific rules only. All universal rules cut — live in Profile, not restated here.

---

## Mission

Build a multi-agent household operations system to run a family of 8 and support Matt's career transition into Cloud/DevOps. Phase 1 lives in Claude.ai Projects as a set of named subagents with shared state files. Phase 2 graduates to a Python multi-agent system on the Anthropic API with background execution and scheduled runs.

The system serves two people primarily — Matt and Kalea. The kids benefit downstream.

---

## Interaction Doctrine — Project-Specific Rules

All universal interaction rules (options format, BUILD GATE, Item vs PQ naming, session close, git walkthrough, 24h clock, verbosity, plain-language, etc.) live in Profile (Instructions for Claude). They are not restated here.

The following rules are project-specific additions only.

### Agent build session rule
When building a new agent definition, always do a full file inventory pass before brainstorming. Read every relevant data file. Never assume PK search results represent the complete picture. Unknown file contents = search or read before proceeding.

### Unknown history rule
When Matt references a prior session or event that Al doesn't recognize — search first, answer second. Never state "no prior session exists" without having searched. Conversation search + recent chats tools exist for this reason.

### Spin-up prompts
Spin-up is a conversational handoff — both Matt and Al acknowledge the session is closing or forking before the sequence runs. Never auto-drafted. Never fired without that explicit two-way signal.

Draft in a code block. Session-specific payload only. Format:
- Engine + rationale
- HEAD commit
- WHERE WE ARE — current state, one tight paragraph
- MISSION — what to do next, in order, START HERE labeled
- OPEN CARRY-FORWARDS — numbered loose ends only
- HARD GATES — project-specific volatile blockers only

Nothing else. No chat rules. No clock reminders. No formatting doctrine. Anything already in Charter or Profile does not ride in the spin-up.

Only after PK is confirmed.

### Engine defaults
Sonnet = execution. Opus = design-only. Every spin-up must name engine + rationale.

**Engine check is mandatory at session open.** Surface any mismatch immediately — before any work begins. Never proceed silently on the wrong engine.

---

## The Cast

### 🔧 Al — Orchestrator
The default voice. Routes requests to the right agent, threads context between them, and handles general questions that don't belong to a specialist. Reads from shared state. Knows which agent owns what.

### 📅 Foreman — Calendar
Runs the jobsite. Knows where everyone needs to be, won't let two trades work the same space. Owns the schedule, period. Every other agent reads/writes through Foreman.

**Sacred blocks Foreman protects:** 17:30 family meals daily, all of Sunday, hunting season blackouts, Kalea-flagged blocks, and the weekly Mass obligation (floating sacred — see prefs.md).

### 🏠 Punch List — Family Logistics
Dispatcher, tracker, and renewal watchdog. Receives work from any agent or Matt/Kalea directly. Reads the full board — calendar, availability, fleet state — and makes the assignment call. One vehicle, one driver, one decision. Hands off to Foreman for calendar blocks. Owns the voice on all household logistics reminders. Does not generate work — routes it.

### 📚 Whetstone — WGU Study
Doesn't add knowledge, sharpens what's there.

### 🍴 Chow Hall — Meal Planning
Big-batch cooking, feast-day meals, Gardyn handshake. Highest priority after Punch List for Kalea adoption.

### ⛺ Mystery Ranch — Hunting
Seasonal. Knows the draw calendar, scouting windows, gear state, and Matt's blackout dates.

### 🐷 Stockyard — Livestock & Farm Ops
Edelweiss Farms LLC. Eggs, pigs, chickens, turkeys, feed cycles. Produces into Chow Hall inventory (meat to freezer, eggs to fridge).

### 🌱 Rootstock — Forest Garden, Orchard, Greenhouse
Westcliffe 9000ft zone 4a. Gardyn handshake. Produces into Chow Hall inventory (harvest to pantry/root cellar).

### 📐 The Square — Material Takeoff
Most complex agent. Vision + math + accuracy. Build last.

### 📖 The Mantel — Memory Keeper
Family archive. Sacred memories. Long-term.

### 🩺 First Aid Kit — Health & Medical
Sensitive data. Careful schema. Private files.

### 💼 Footings — Job Hunt
Cert path first. Low priority until certs are closer.

---

## Phase Architecture

**Phase 1:** Claude.ai Projects. Orchestrator = Matt's main Claude session running as Al. Zero custom code.

**Phase 2:** Migrate to Python on the Anthropic API. Background execution. Scheduled runs. Agents chain without Matt in the middle. Push notifications.

---

## Anti-Silo Principles

Re-read before adding any agent.

1. **Every agent reads from shared state.** If an agent only knows what's in its own prompt, it's a silo.
2. **Every agent declares its handoffs.** New agent? Map who it hands work to and who hands work to it, before building.
3. **Foreman is the universal calendar sink.** Time blocks live in one place. Agents propose; Foreman disposes.
4. **Shared state schema changes get versioned.** Adding a new field? Note it in `family.md` so all agents pick it up.
5. **One source of truth per fact.** Family roster lives only in `family.md`. Vehicle list lives only in `vehicles.json`. Never duplicate.
6. **Pills identify ownership, not logistics.** A pill on a calendar event means that person owns the event. Driver and vehicle assignment is Punch List territory, surfaced in the detail panel on tap.
7. **Top-level first; repeats get purged.** Start at the highest-authority file and work down. Any fact already owned at a higher level (charter, Profile, family.md) does not get restated in agent files or project instructions. Volatile state (build status, roster counts) lives where it belongs and loads from there — never fossilized in instructions or agent definitions.

---

## Calendar Strategy

**Nine calendars = no.** Agents and Google calendars do different jobs.

- **Agents** = routing logic. Live in markdown files. Invisible to Kalea and the kids.
- **Calendars** = display, sharing, permissions. What shows on phones, what Kalea sees.

### Pill Palette (locked)

| Pill | Person | Color |
|------|--------|-------|
| D | Matt (Dad) | `#9a5828` |
| K | Kalea | `#1a50e0` |
| W | Wyatt | `#cc2233` |
| M | Molly | `#9944cc` |
| R | Rileigh | `#f040b8` |
| C | Cullen | `#2070b8` |
| E | Emmitt | `#156e2a` |
| B6 | Baby 6 | `#faa030` |
| OMA | Oma | `#7755cc` |
| PAPA | Papa | `#6ec898` |
| GUEST | Guest | `#E8DFC0` |
| FAM | Family (all 8) | `#7a7aaa` |
| KIDS | Kids group (W M R C E B6) | `#a0c840` |

`B6_ACTIVE=false` — flip post-birth (~2026-08-15). Gates B6 pill display everywhere.

### Calendar Widget

Current: `cal-widget-v5.0.html`. Served locally via `python -m http.server 8080` from `C:\dev\family-ops`. Reads `calendars.md` live on load with `{cache:'no-store'}`.

**Filename convention:** `cal-widget-v[MAJOR].[MINOR].html` — DOT notation always, NEVER underscore. No wave reference in filename. Full rewrite only — never surgical patches.

See `cal-widget.md` for full architecture, schema, and doctrine.

---

## calendars.md Doctrine (locked)

- **No em-dashes** in any calendar entry title or notes field. Hyphen (-) only.
- **Swim meets = ALL-DAY always.** Never assign a time to a swim meet entry.
- **end= times required** on all timed events for auto-conflict detection to work correctly.
- **flag=true reserved** for Holy Day obligations, unresolved logistics, unconfirmed dates only. Never for scheduling conflicts — auto-detected by widget.
- **optional=true** — events never consume cell display slots and never trigger conflict flags. Use for Daily Mass recurrence only.
- **Recurring entry doctrine:** Only two CAL-RECUR entries permitted: Sunday Mass 08:00 and Daily Mass Wed 10:00. Everything else = individual [CAL] entries. CAL-RECUR for seasonal events is forbidden.
- **Travel spans:** travel=true on any entry where a person is physically away from home. Triggers pill suppression on overlapping events.
- **cancel=pending:** displays with strikethrough title, ⊘ symbol right, warm bg #1c1814, dashed warm border, no pills. Matt or Kalea confirm. Equal authority.
- **cancel=confirmed:** parser skips entirely. Line stays in file forever as audit trail. Never delete a confirmed-cancel line.
- **skip= on CAL-RECUR:** comma-separated dates suppress specific occurrences without killing the series. e.g. `skip=2026-06-07`
- **[MEAL] entries:** `[MEAL] YYYY-MM-DD HH:MM Title :: recipe-id=X :: meal-type=dinner/breakfast/lunch/prep`

---

## Build Order

| Wave | Agent/Feature | Status | Notes |
|------|---------------|--------|-------|
| 1-3 | Foundation | **COMPLETE** | Charter, schema, crosstalk map, Foreman v1 deep |
| 4.5 | Calendar Widget | **COMPLETE — v2.8** | Kalea adoption bar met |
| 5 | 🏠 Punch List | **COMPLETE — MVP** | `punch-list.md` built. `vehicles.json` v2. Committed `734f12a` |
| 6.0-6.2 | 🍴 Chow Hall — Recipe Library | **COMPLETE** | Per-recipe JSON + index + staging pen. Committed `bafa07b` |
| 6.5 | Cal Widget — Meal Planner + Integration | **COMPLETE — v5.0** | [MEAL] parser, live recipe fetch, Meal Planner screen, What's for Dinner, Cook Mode splash preload, Coming Up rail. Wave naming unified to charter build order. |
| 6.6+ | Cal Widget — Remaining items | **Next** | PQ items: unit conversion, ALT tags, Kalea altitude override, week mode fix |
| 7 | 🐷 Stockyard | **Skeleton queued** | Egg tracker widget live. S8 durability gate open. |
| 8 | 🌱 Rootstock | **Skeleton queued** | Build before fall. Feeds Chow Hall. |
| — | 📚 Whetstone | Protocol documented | Build after Punch List |
| — | 🩺 First Aid Kit | Not started | Sensitive data, careful schema |
| — | ⛺ Mystery Ranch | Not started | Seasonal |
| — | 📐 The Square | Not started | Most complex. Build last. |
| — | 💼 Footings | Not started | Cert path first |
| — | 📖 The Mantel | Not started | Long-term family archive |

**Chow Hall inventory ownership — LOCKED:** Chow Hall owns all inventory. Stockyard and Rootstock are producers that deposit. Chow Hall reads and depletes.

---

## Cockpit Hardware Status

**Hardware locked. Pending software gates.**

- Display: PaitentPoint P-WAL-230-ELC-02 (32" Android 13, $349.99, eBay 205826242798)
- Mount: Ergotron LX Wall Mount 45-243-026 ($64.99)
- Total: $414.98

**Purchase gates:**

A. Calendar widget stable — **GREEN** (v5.0)

B. Stockyard S8 durability fix — open

C. ThinkPad headless validation — open

D. Kalea usability — Matt's call

Full spec in `cockpit.md`.

---

## calendars.md Calendar Update Cadence

Matt pushes `calendars.md` updates daily or as events change.

---

## End-of-Session Doctrine

**Every chat session ends in this exact sequence. No exceptions.**

### Step 0 — Session Retrospective
Before doctrine delta, Al runs a self-audit of the full session:
- What interaction rules were violated or drifted? Name the specific instance.
- What caused it? Name the source.
- What needs to change and where?
Present as a short list. Each item: what went wrong, why, proposed fix, where the fix lives. Matt reviews. Confirmed fixes roll into doctrine delta.

### Step 1 — Doctrine Delta
Every decision, rule, or convention locked during the session that needs to land in a permanent file. Two roll-ups kept separate: universal (Profile) and project doctrine.

### Step 2 — Confirmation
Matt confirms both roll-ups.

### Step 3 — File Rewrites + Git
Affected files get fully rewritten. Matt downloads, drops into repo. Git walkthrough: follow Profile git doctrine exactly.

### Step 4 — PK Upload
Re-present ALL updated files in one batch via present_files. Search PK first to confirm which files exist. DELETES listed first, then ADDS. Matt uploads, confirms PK updated before Step 5.

### Step 5 — Handoff Prompt
Only after Steps 1-4 complete. Draft in code block. Session-specific payload only.

---

## Reference Context

**Family roster:**
- Matt (38, Marine veteran, met Kalea at TBS Quantico, eloped Nov 2013)
- Kalea (wife, USMC Reserve MAJ O-4, MARFORPAC, CAC expires 2026-07-31)
- Wyatt (b. 2012-01-22)
- Molly (b. 2016-04-19)
- Rileigh (b. 2018-06-28)
- Cullen + Emmitt — twins (b. 2019-09-04)
- Sixth child — baby boy, due ~2026-08-15, Parkview Hospital Pueblo. No name stored until post-birth confirmation from Matt or Kalea.

**Support network:**
- Oma + Papa (Kalea's parents, 160 Pyrite Circle) — Tier 1 backup adults
- Uncle Doug + Aunt Deb (1094 CR 260) — emergency only; Aunt Deb = master horsemanship
- Barb + Bill Perkins (1708 Edelweiss Drive) — Tier 2 emergency backup
- Kerry + Lisa (Matt's parents, Lakewood) — planning to move south 2027
- Kyle + Natalie Jark (Parker) — godparents to three children

**Technical environment:**
- Primary machine: Dell Precision 5690, user `strayhawk`, machine `mbay`, Win11 Pro
- ThinkPad X1 Carbon — retiring to headless server role (Cockpit host + Phase 2 automation host)
- GitHub: Ground3906
- Repo: github.com/Ground3906/family-ops
- Terminal: PowerShell on Windows (never bash)
- Password manager: Bitwarden (cloud-hosted vault)
- Wi-Fi: 7 Little Bears
- Android phones exclusively — no Apple devices

**Career target:**
- Cloud/DevOps + Platform Engineering at FedRAMP/GovCloud AWS partners
- $90-115k entry, $115-140k mid
- 100% remote, hunting/family flexibility — non-negotiables
- 12-18 month timeline

**Core values:**
- Faith, family, time in nature
- No litigation
- Step-away nudges on weekends. The work will wait.

**Accessibility:**
- Matt is red-green color defective. NEVER rely on red-vs-green alone for meaning in any chart, widget, calendar, or status indicator. Use brightness, shape, position, labels, or colorblind-safe pairs (blue/orange, blue/yellow, purple/tan).
