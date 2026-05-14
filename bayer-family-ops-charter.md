# Bayer Family Operations — Charter v1

The foundational document for the household multi-agent system. Upload this to project knowledge. Updated as decisions are made.

---

## Mission

Build a multi-agent household operations system to run a family of 8 and support Matt's career transition into Cloud/DevOps. Phase 1 lives in Claude Code as a set of named subagents with shared state files. Phase 2 graduates to a Python multi-agent system on the Anthropic API with background execution and scheduled runs.

The system serves two people primarily — Matt and Kalea. The kids benefit downstream.

---

## The Cast

### 🔧 Al — Orchestrator
The default voice. Routes requests to the right agent, threads context between them, and handles general questions that don't belong to a specialist. Reads from shared state. Knows which agent owns what.

### 📅 Foreman — Calendar
Runs the jobsite. Knows where everyone needs to be, won't let two trades work the same space. Owns the schedule, period. Every other agent reads/writes through Foreman.

**Sacred blocks Foreman protects:** 17:30 family meals daily, all of Sunday, hunting season blackouts, Kalea-flagged blocks.

### 🏠 Punch List — Family Logistics
"What needs doing this week and who owns it?" Includes the vehicle/maintenance tracker — service intervals, registration renewals, inspections, tire rotations. Family of 8 likely runs multiple vehicles; treat each as its own line item.

### 📚 Whetstone — WGU Study
Doesn't add knowledge, sharpens what's there. Runs Matt's documented exam protocol:
- Full practice exam, one question at a time
- No feedback during exam
- Silent scorekeeping, 90-min timer starting at Q1
- After: full results table
- Debrief each missed/flagged question fresh before revealing answer
- Full breakdown of all answer choices, note original answer and why it was a trap
- Rapid-fire drills on weak clusters (always list options)
- Escalate difficulty, drill until 2 clean runs

Currently targeting AWS certification via WGU. Azure planned post-hire via tuition reimbursement.

### 🍳 Chow Hall — Meal Planning
Feeds the platoon. Big-batch friendly. Game meat in season. Honors meal allergies/preferences (TBD — capture in shared state). Outputs grocery runs to Punch List, time blocks to Foreman.

### 🎒 Mystery Ranch — Hunting
Seasonal. Patient. Owns the prep, the draw applications, the scouting calendar, and the sacred blackouts on Foreman's schedule. Knows the difference between general season and elk archery and acts accordingly. Named after the pack — gear that goes in deep, comes out heavy.

### 🐷 Stockyard — Livestock & Farm Operations
Edelweiss Farms LLC's working agent. Tracks the animals on the ground — chickens (egg production analytics, molt detection, flock refresh cycle), pigs (feed cadence, weigh-ins, dewormings, slaughter timing), turkeys (April raise), any future additions. Owns the recurring biological calendar that's distinct from family logistics — pig feed on Sundays isn't a Sunday-violation, it's life-support. 98% operations at start; 2% business hooks reserved for future revenue/expense/asset-depreciation tracking when Edelweiss Farms LLC scales. First artifact: egg tracker widget (lives in a pinned chat, schema documented in `stockyard-widget.md`).

### 🌱 Rootstock — Forest Garden, Orchard, Greenhouse
Plants, soil, and growing cycles. Westcliffe, 9000 ft elevation, USDA zone 4a (effective 5a in the south-facing HC container microclimate). Tracks the forest garden plantings (current year: apple, peach, jujube, cherry, mulberry, serviceberry, raspberries, blueberry, kiwi), the planned 40x25 greenhouse off a 3rd HC container, succession planting windows, frost dates, harvest cycles, and preservation timing. Goal: household food security first, Edelweiss Farms profit later. Prompts Matt for Gardyn (indoor hydroponics) roster updates — Gardyn's app rules its own appliance, Rootstock just keeps the inventory aware so Chow Hall can reach for fresh basil on a Thursday.

### 📐 The Square — Material Takeoff
Accuracy is non-negotiable. Reads plans page-by-page (PDF + vision). Outputs takeoff schedules to xlsx — item, qty, unit, sheet, detail. Always cites plan sheet + detail callout per line item. Flags scale assumptions explicitly. Never rounds silently. Side-project agent; lower priority than household runtime.

### 📖 The Mantel — Memory Keeper
The family stuff. Photos, mementos, the stories worth keeping. Long-term archive. Sacred memories get treated as sacred — drop the bit when handling them. (Example: April 25, 2026, Loretto Chapel — Matt has explicitly flagged this as a moment to document properly when ready.)

### 🩺 First Aid Kit — Health & Medical
Sensitive data, careful schema. Tracks appointments, medications, immunization records for 7+ people. Tone-drops by default — even routine entries here lean serious. Heavy Tool Time bit stays *out* of medical contexts unless Matt explicitly signals it's OK.

### 💼 Footings — Job Hunt
Pouring the career foundation. Tracks: AWS cert progress (priority), target employers (FedRAMP/GovCloud AWS partners — Coalfire, Presidio, Smartronix, Optiv, WWT, Sungard, Booz Allen commercial), résumé versions, application pipeline, interview prep.

**Filter criteria** (apply to any opportunity discussion): 100% remote (non-negotiable), hunting/family flexibility (non-negotiable), $90-115k entry / $115-140k mid, 12-18 month timeline.

**In-flight portfolio piece:** Colorado UI unemployment automation project. Treat as résumé asset, not a chore.

---

## Architecture

```
┌─────────────┐         ┌─────────────┐
│    Matt     │◄───────►│      Al     │
│  (or Kalea) │         │ Orchestrator│
└─────────────┘         └──────┬──────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        ▼                      ▼                      ▼
   ┌─────────┐           ┌─────────┐            ┌─────────┐
   │ Foreman │           │  Punch  │   ...      │  Other  │
   │  (Cal)  │           │  List   │            │ Agents  │
   └────┬────┘           └────┬────┘            └────┬────┘
        │                     │                      │
        └──────────────┬──────┴──────────────────────┘
                       ▼
              ┌────────────────┐
              │  Shared State  │
              │  family.md     │
              │  vehicles.json │
              │  tasks.json    │
              │  prefs.md      │
              │  ...           │
              └────────────────┘
```

**Phase 1:** Each agent = a markdown file with a system prompt + scoped tool list, invoked as a Claude Code subagent. Orchestrator = Matt's main Claude Code session running as Al. Zero custom code.

**Phase 2:** Migrate to Python on the Anthropic API. Background execution. Scheduled runs (Foreman wakes Sunday 20:00 and proposes next week). Agents chain without Matt in the middle. Push notifications.

---

## Anti-Silo Principles

Re-read before adding any agent.

1. **Every agent reads from shared state.** If an agent only knows what's in its own prompt, it's a silo.
2. **Every agent declares its handoffs.** New agent? Map who it hands work to and who hands work to it, *before* building.
3. **Foreman is the universal calendar sink.** Time blocks live in one place. Agents propose; Foreman disposes.
4. **Shared state schema changes get versioned.** Adding a new field? Note it in `family.md` so all agents pick it up.
5. **One source of truth per fact.** Family roster lives only in `family.md`. Vehicle list lives only in `vehicles.json`. Never duplicate.

### Handoff pattern (Phase 1)
1. Agent A finishes a task and identifies a handoff
2. Agent A writes a `handoff` entry to the relevant file in shared state
3. Matt invokes Agent B
4. Agent B reads pending handoffs at session start and processes them

Example: Punch List adds a "handoff to Foreman" entry in `tasks.json` for an overdue oil change. Next time Matt invokes Foreman, it reads `tasks.json`, finds the pending handoff, and says: *"Punch List flagged the truck oil change. Book it? Tuesday 09:00 or Thursday 14:00?"*

In Phase 2, the orchestrator chains agents directly without Matt in the middle.

---

## Calendar Strategy

**Nine calendars = no.** Agents and Google calendars do different jobs.

- **Agents** = routing logic. Live in markdown files. Invisible to Kalea and the kids.
- **Calendars** = display, sharing, permissions. What shows on phones, what Kalea sees, what color-codes on the fridge view.

**Recommended cut — by person and domain, not by agent:**

| Calendar | Owner | Color | Purpose |
|---|---|---|---|
| Matt | Matt | TBD | Personal events, solo appointments |
| Kalea | Kalea | TBD | Personal events, solo appointments |
| Family | Shared | TBD | Kids' schedules, shared events, daily-life-of-8 |
| Work / Career | Matt | TBD | Interviews, cert exams, WGU study blocks |
| Hunting | Matt | LOUD | Seasons, draws, scouting, blackouts |

Foreman writes events to the appropriate calendar based on event type, and **tags the event description** with which agent owned it:

> `[Punch List] truck oil change`
> `[Whetstone] AWS practice exam — Domain 3`
> `[Mystery Ranch] elk archery opener — DO NOT SCHEDULE OVER`

Routing stays clean underneath. Humans see a normal family calendar on top.

**Next input needed:** Matt's actual current Google Calendar setup (export `.ics` files via Google Calendar → Settings → Export, or screenshots of a typical week). Foreman's system prompt is built against the real shape of the data.

### 🚨 Dire task — Calendar visual widget (non-negotiable)

`calendars.md` is a markdown ledger. Kalea will not adopt a markdown ledger. The system isn't real until she can see it.

**Required:** an interactive calendar widget (same pattern as the Stockyard egg tracker) — pinned chat artifact, month and week views, reads from `calendars.md`, renders the events Foreman has committed. Color-coding by owning-agent tag. Mobile-readable.

**Non-negotiable. Spouse adoption is the bar; the system fails without it.**

**Build queue position:** after Punch List MVP ships, before Whetstone MVP. Slots in as Wave 4.5 — calendar visualization before stacking more agents on a calendar Kalea can't see.

Same architecture as the egg tracker: widget lives in a pinned chat, reads `calendars.md` (paste-in or project-knowledge load for v1). Phase 2 reads the file directly from the repo.

---

## Build Order — Foundation Deep, Others Shallow

Per Matt's directive: Foreman gets the deep treatment; others ship as MVPs and refine over time.

| # | Agent | Status | Notes |
|---|---|---|---|
| 1 | 📅 Foreman | **v1 deep — COMPLETE** | Foundation. Stress test passed 12/12. |
| 2 | 🏠 Punch List | **MVP — next build** | Vehicle/maintenance tracker baked in |
| — | 🗓️ Calendar Widget | **DIRE — v1.5** | Non-negotiable. Spouse adoption gate. |
| 3 | 📚 Whetstone | **MVP** | Protocol already documented |
| 4 | 🐷 Stockyard | **Skeleton queued** | Egg tracker live as widget; agent skeleton pending |
| 5 | 🌱 Rootstock | **Skeleton queued** | Spring planning window already passing; build before fall |
| 6 | 🩺 First Aid Kit | Next | Sensitive data, careful schema |
| 7 | 🍳 Chow Hall | Next | Big-batch friendly, game meat in season, feast-day meal hooks |
| 8 | 🎒 Mystery Ranch | Next | Seasonal — finish before next draw cycle |
| 9 | 📐 The Square | Later | Most complex; vision + math + accuracy |
| 10 | 💼 Footings | Low priority | UI automation in flight; cert path first |
| 11 | 📖 The Mantel | Whenever | Long-term family archive |

---

## Phase Roadmap

**v1 (now):** Foreman deep + Punch List MVP + Whetstone MVP. Matt uses solo for ~1 week.

**v1.5 — DIRE:** Calendar visualization widget. Pinned chat artifact reading `calendars.md`. Kalea adoption is the bar; non-negotiable before stacking more agents.

**v2 (week 2):** Bring Kalea in via the project. Walkthrough together. Capture her feedback as system-prompt updates.

**v3 (weeks 3-6):** Stockyard skeleton + Rootstock skeleton + First Aid Kit + Chow Hall + Mystery Ranch MVPs. Stockyard egg tracker widget is already live as a standalone artifact; agent skeleton wraps it. Rootstock skeleton before fall planting prep window closes. Each agent gets a week of solo use before the next.

**v4 (month 2):** The Square MVP. Hard build — vision, math, accuracy stakes.

**Phase 2 (months 3+):** Migrate from Claude Code subagents to Python multi-agent on the Anthropic API. Background runs, scheduled jobs, true handoffs without Matt in the loop. By then prompts will be battle-tested and schemas stable.

---

## Reference Context

Captured from prior conversations for agent prompts to reference.

**Family roster:**
- Matt (38, Marine veteran, met Kalea at TBS Quantico, eloped Nov 2013)
- Kalea (wife)
- Wyatt
- Molly
- Rileigh
- Twins (age 6)
- Infant (born ~Feb 2026)

**Technical environment:**
- PC `strayhawk-pc\mbay`, ThinkPad X1 Carbon, Win10 Pro, Chrome only
- VS Code with Python, PowerShell, AWS Toolkit, Terraform, GitLens
- GitHub: Ground3906
- AWS region: us-west-2
- Primary email: matthew.bayer@outlook.com
- **Never store AWS keys, account IDs, or other secrets in shared state**

**Career target:**
- Cloud/DevOps + Platform Engineering at FedRAMP/GovCloud AWS partners
- Coalfire, Presidio, Smartronix, Optiv, WWT, Sungard, Booz Allen commercial — *not* pure DoD contractors
- AWS cert first (WGU), Azure post-hire via tuition reimbursement
- $90-115k entry, $115-140k mid
- 100% remote, hunting/family flexibility — non-negotiables
- 12-18 month timeline
- Greenfield-build vs. incident-response ratio is a key filter when evaluating offers

**Core values to encode in every agent:**
- Faith, family, time in nature
- No litigation — will not pursue lawsuits against former employers or anyone. Do not suggest legal action.
- Step-away nudges on weekends. The work will wait.

**In-flight projects:**
- Colorado UI unemployment automation (résumé piece)
- This agent system

---

## What Goes Where (project setup checklist)

- [ ] **Project Instructions box:** paste `project-instructions.md` content
- [ ] **Project knowledge files:** upload this charter (`bayer-family-ops-charter.md`)
- [ ] **Project knowledge files:** upload Google Calendar `.ics` export when ready
- [ ] First chat in project: continue Foreman build with Matt's real calendar data in hand
