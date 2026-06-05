# Crosstalk & Handoff Map v2

How agents pass work to each other. Designed against Charter §Anti-Silo Principles.

**v2 (2026-06-05):** Roster reduced to 9 agents. Struck Whetstone, The Square, Footings (patterns E and F removed). First Aid Kit renamed IFAK (path `first-aid/` unchanged); The Mantel renamed Mantle (path `mantle/`). Ledger (financial) added — fed by the JSONL cost/revenue logs; handoff patterns designed at build. "Phase 2 may relax" language replaced with the Automation layer.

---

## Bedrock Rules

1. **Foreman is the universal calendar sink.** Anything that needs a time block goes through Foreman. No agent writes events directly to Google Calendar.
2. **The originating agent writes the handoff to `handoffs.json`.** Subject + payload + proposed options. The receiving agent reads it on next invocation.
3. **The receiving agent confirms with the human before acting.** Especially for calendar writes, state mutations, or anything irreversible.
4. **Handoffs don't vanish.** Closed handoffs stay in the file (`status: done`) — they're the audit trail.
5. **Sacred blocks beat everything.** Family meals 17:30 daily. Sundays. Mass obligation (floating sacred — travels through adjudication, always protected). Hunting season blackouts (Matt-only scope). Kalea drill travel (Kalea-only scope). Kalea-flagged blocks. Foreman refuses scheduling violations and bounces back to the originating agent.
6. **Reminder ownership — Option C.** The agent that owns the work owns the reminder. Foreman owns calendar truth (the *when*); domain agents own voice and cadence (the *what* and *how*). Cross-agent dependencies resolve to whoever has the more time-sensitive or domain-primary stake.
7. **Pills = ownership, not logistics.** A pill on a calendar event means that person owns the event. Driver and vehicle assignment is Punch List territory — surfaced in the day/week detail panel on tap, never on the pill stack.

---

## Routing Matrix

Read as: ROW agent typically hands work TO COLUMN agent.

|              | Foreman | Punch | Chow | MR  | Stock | Root | IFAK | Mantle |
|--------------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **Al**       | route | route | route | route | route | route | route | route |
| **Foreman**  |  —   |  ←  |  ←  |  ←  |  ←  |  ←  |  ←  |  →   |
| **Punch**    |  →   |  —  |  ←  |     |  ↔  |  ↔  |  ←  |      |
| **Chow Hall**|  →   |  →  |  —  |  ←  |  ←  |  ←  |     |      |
| **Mystery R**|  →   |     |  →  |  —  |     |     |     |  →   |
| **Stockyard**|  →   |  ↔  |  →  |     |  —  |     |     |  →   |
| **Rootstock**|  →   |  ↔  |  →  |     |     |  —  |     |      |
| **IFAK**     |  →   |  →  |     |     |     |     |  —  |  →   |
| **Mantle**   |      |     |     |     |     |     |     |  —   |

`→` sends to. `←` receives from. `↔` bidirectional. **MR = Mystery Ranch. Stock = Stockyard. Root = Rootstock.**

Mantle is mostly a terminal sink: things flow IN (moments worth keeping), little flows out except direct queries.

**Ledger (financial, unbuilt)** is not yet in the grid. It receives cost and revenue feeds from `fuel-log.jsonl`, `feed-log.jsonl`, and `income-log.jsonl`. Its handoff patterns get designed when it is built.

---

## Canonical Patterns

### Pattern A — Logistics → Schedule
**Punch List → Foreman.** A task needs a time block.

```
Punch List writes:
{
  from: "punch-list", to: "foreman",
  subject: "Truck oil change — 1200 mi past due",
  payload: { task_id, proposed_blocks: ["Tue 09:00", "Thu 14:00"] },
  status: open
}
```

Foreman next invocation: *"Punch List flagged the truck oil change. Tuesday 09:00 or Thursday 14:00? Or pick another."*
Reminder voice when the date approaches: **Punch List speaks**, not Foreman. Option C.

### Pattern B — Health → Logistics → Schedule
**IFAK → Punch List → Foreman.** Appointment scheduled, needs a driving block + maybe a prescription pickup.

IFAK emits one handoff to Foreman (the appointment) and one to Punch List (Rx pickup). Punch List may then hand back to Foreman if the pickup needs its own slot. Reminder voice belongs to IFAK for the appointment, Punch List for the Rx pickup. **Drop the bit** on anything IFAK touches in earnest.

### Pattern C — Hunting → Calendar Blackout
**Mystery Ranch → Foreman.** Draw results, season dates, scouting trip.

Foreman writes a HARD block — **Matt-only scope** per `prefs.md`. Other agents querying Foreman about Matt's availability inside those windows get a refusal; queries about Kalea, the kids, or anchor-house support continue normally. Don't cancel a Wyatt ortho because Matt is in the field — shift the driver.

### Pattern D — Hunting → Meals
**Mystery Ranch → Chow Hall.** Harvest comes in. Headed to processor. Processor done.

Chow Hall updates `freezer.json` and adjusts upcoming meal plans accordingly.

### Pattern G — Hunting → Memory
**Mystery Ranch → Mantle.** Notable harvest. First hunt with a kid. Season highlight.

Mystery Ranch emits a `mantle` handoff with the moment; Mantle files it with appropriate gravity. If the moment touches grief or sacred ground, tone-drop carries through.

### Pattern J — Farm Ops → Schedule
**Stockyard → Foreman.** Slaughter day, weigh-ins, vet visits, multi-hour farm events that need a calendar block. Daily feed cadence does NOT route through Foreman — it's a known persistent rhythm Foreman respects from the rhythm table.

```
Stockyard writes:
{
  from: "stockyard", to: "foreman",
  subject: "Pig slaughter day — 6-8 hour block",
  payload: { proposed_dates: ["2026-11-07", "2026-11-14"], conflicts_to_check: ["rifle elk season"] },
  status: open
}
```

### Pattern K — Eggs/Harvest → Meals  *(producer → Chow Hall; Stockyard leg GATED)*
**Stockyard → Chow Hall.** Egg counts trending up, glut incoming. Or pig in the freezer, processor done. Or chickens culled, broth stock available.

Chow Hall updates `chow-hall/freezer.json` (proteins) or produce tracking (eggs, fresh harvest), adjusts meal plans toward use-it-up. **This is the producer → Chow Hall end-state handoff and is blocked by the Stockyard durability gate** — no real flock-driven feed into Chow Hall until that fix is verified (see Charter §Hard Gates).

### Pattern L — Garden Harvest → Meals  *(producer → Chow Hall)*
**Rootstock → Chow Hall.** Fresh harvest ready. Tomatoes coming in heavy. Apples on the tree. Gardyn basil at peak.

Chow Hall pulls into meal planning. Preservation prompts (canning, freezing, drying) handed back to Punch List or Rootstock depending on scale. The Rootstock leg of the producer handoff is clear when Rootstock comes online (not gated).

### Pattern M — Garden Planting → Schedule
**Rootstock → Foreman.** Spring transplant weekend, fall mulching, greenhouse build phase, irrigation install. Multi-hour outdoor work blocks.

Foreman respects sacred blocks; planting windows are weather-sensitive, so flexibility from Tim is sometimes required.

### Pattern N — Farm Maintenance ↔ Logistics
**Stockyard ↔ Punch List.** Bidirectional.

- Stockyard → Punch List: coop repair, feed run, water heater for winter, vet supplies pickup.
- Punch List → Stockyard: equipment failure noticed during chores ("the auger's binding"), feed inventory low.

### Pattern O — Garden Maintenance ↔ Logistics
**Rootstock ↔ Punch List.** Bidirectional. Same pattern — tools, supplies, infrastructure (drip line repair, greenhouse panels, fence work) flow between the two.

### Pattern P — Gardyn Roster Prompts
**Rootstock → Human.** Gardyn (indoor hydroponics appliance) runs on its own app. Rootstock owns the *prompting cadence* — periodically asks Matt to update `gardyn-roster.md` so Chow Hall knows what's harvestable. Thin handshake, no operational logic, no sync.

### Pattern Q — Document Renewal → Schedule
**Punch List → Foreman.** A document expiration is approaching (DL, CAC, vehicle registration, insurance policy). Punch List emits a milestone handoff; Foreman blocks a calendar slot for the action (DMV appointment, DEERS appointment, online renewal).

Reminder voice belongs to Punch List throughout. Option C.

### Pattern R — CCIR Routing
**Any agent → arbiter's domain agent.** A family member drops a CCIR observation into a chat session (see `ccir-protocol.md`). The receiving agent routes per the CCIR domain table to the correct agent; that agent logs and confirms back to the notifier.

Cross-agent CCIRs (e.g. an observation that spans vehicle + medical) route to Al for triage. Al never makes the notifier route their own observation.

### Pattern H — Calendar Echo Back
**Foreman → Originating Agent.** Foreman couldn't fit the request, or there's a sacred-block conflict.

Foreman writes a return handoff: *"Couldn't slot oil change Tue 09:00 — Wyatt's appointment. Try Tue 14:00 or Wed 08:30."*

### Pattern I — Family-Care Echo
**Any → Al → Human.** Session has run long on a weekend. Kids are around.

Al (orchestrator) holds final authority on when to push back on the human. Other agents don't moralize directly — they flag to Al via handoff, Al decides whether to nudge.

**Struck patterns (2026-06-05):** Pattern E (Study → Schedule, Whetstone) and Pattern F (Job Hunt ↔ Study, Footings ↔ Whetstone) removed with their agents. WGU study lives in its own project.

---

## Confirmation Protocol

Before any agent writes to Google Calendar, `handoffs.json`, or any shared state file:

1. **Propose** in chat: *"Here's what I'm about to write — [diff]. Confirm?"*
2. **Wait for explicit confirmation.** "Yes," "ship it," "do it" — explicit affirmation. Not a thumbs-up emoji, not silence.
3. **Commit** the change.
4. **Report** back: *"Done. [path]."*

No silent writes in the Interactive layer. Ever. The **Automation layer** may relax propose-then-commit for trusted, self-contained jobs — but only with a heartbeat and a review ping (e.g. the receipt watcher writes, then pings Matt "logged — review when you can"). A silent failure can never be allowed; that's the lesson of the durability gate.

---

## Sacred Block Refusals

Foreman is the gatekeeper. When asked to schedule in a sacred block:

- **17:30–19:00 daily (family meal):** REFUSE. Propose 19:00+ or earlier in day.
- **Sunday (any time):** REFUSE work, study, appointments. Mass, family, rest. Override only on Matt's explicit say-so for a single block, captured in chat for that session — not stored as standing permission.
- **Mass — floating sacred:** REFUSE both the original default mass slot AND any currently proposed adjudication slot. Both protected simultaneously during adjudication window. On confirmation original releases; confirmed slot becomes the new protected block.
- **Hunting blackouts (Matt-only):** REFUSE Matt events. Re-route household items to Kalea or backup-adult tier. Bounce to Mystery Ranch for the dates.
- **Kalea drill travel (Kalea-only):** REFUSE Kalea events. Re-route household items to Matt or backup-adult tier.
- **Kalea-flagged blocks:** REFUSE. Never schedule over without Kalea's confirmation in chat.

Receiving agent (the one that asked) gets a return handoff with the refusal reason + the suggested alternative.

---

## Anti-Loop Discipline

A handoff that bounces back unprocessed twice = stop and surface to the human via Al. Don't let agents ping-pong. Two strikes, raise the hand.

---

## Quick Reference — Who Owns What

| Domain | Owner Agent | State File |
|---|---|---|
| Calendar | Foreman | Google Calendar + `calendars.md` |
| Driver assignment | Punch List | Surfaced in day/week detail panel on tap — never on pill stack |
| Tasks | Punch List | `punch-list/tasks.json` |
| Vehicles | Punch List | `punch-list/vehicles.json` + `fleet-state-v1.md` |
| Documents / renewals | Punch List | `punch-list/documents.md` |
| Wyatt licensing | Punch List | `punch-list/wyatt-licensing.md` |
| CCIR routing doctrine | Household-wide | `ccir-protocol.md` |
| Meals | Chow Hall | `chow-hall/meal-plan.md` |
| Game meat | Chow Hall | `chow-hall/freezer.json` |
| Hunting seasons | Mystery Ranch | `mystery-ranch/seasons.md` |
| Livestock, eggs, feed | Stockyard | `stockyard/` (eggs-log, flock-config, pigs, turkeys) — *durability-gated* |
| Plants, orchard, greenhouse | Rootstock | `rootstock/` (plantings.md, garden-plan.md, gardyn-roster.md) |
| Health | IFAK | `first-aid/` |
| Memory / legacy | Mantle | `mantle/` |
| Farm finances | Ledger | *(unbuilt — fed by `fuel-log.jsonl`, `feed-log.jsonl`, `income-log.jsonl`)* |

If two agents seem to want the same fact: re-read this table. One owner only. The other agent references.
