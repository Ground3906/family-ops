# Crosstalk & Handoff Map v1

How agents pass work to each other. Designed against Charter §Anti-Silo Principles.

---

## Bedrock Rules

1. **Foreman is the universal calendar sink.** Anything that needs a time block goes through Foreman. No agent writes events directly to Google Calendar.
2. **The originating agent writes the handoff to `handoffs.json`.** Subject + payload + proposed options. The receiving agent reads it on next invocation.
3. **The receiving agent confirms with the human before acting.** Especially for calendar writes, state mutations, or anything irreversible.
4. **Handoffs don''t vanish.** Closed handoffs stay in the file (`status: done`) — they''re the audit trail.
5. **Sacred blocks beat everything.** Family meals 17:30 daily. Sundays. Hunting season blackouts (Matt-only scope). Kalea drill travel (Kalea-only scope). Kalea-flagged blocks. Foreman refuses scheduling violations and bounces back to the originating agent.
6. **Reminder ownership — Option C.** The agent that owns the work owns the reminder. Foreman owns calendar truth (the *when*); domain agents own voice and cadence (the *what* and *how*). Cross-agent dependencies resolve to whoever has the more time-sensitive or domain-primary stake.

---

## Routing Matrix

Read as: ROW agent typically hands work TO COLUMN agent.

|              | Foreman | Punch | Whet | Chow | MR  | Stock | Root | FAK | Foot | Sq | Mantel |
|--------------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **Al**       | route | route | route | route | route | route | route | route | route | route | route |
| **Foreman**  |  —   |  ←  |  ←  |  ←  |  ←  |  ←  |  ←  |  ←  |  ←  |  ←  |  →   |
| **Punch**    |  →   |  —  |     |  ←  |     |  ↔  |  ↔  |  ←  |     |     |      |
| **Whetstone**|  →   |     |  —  |     |     |     |     |     |  ↔  |     |      |
| **Chow Hall**|  →   |  →  |     |  —  |  ←  |  ←  |  ←  |     |     |     |      |
| **Mystery R**|  →   |     |     |  →  |  —  |     |     |     |     |     |  →   |
| **Stockyard**|  →   |  ↔  |     |  →  |     |  —  |     |     |     |     |  →   |
| **Rootstock**|  →   |  ↔  |     |  →  |     |     |  —  |     |     |     |      |
| **FAK**      |  →   |  →  |     |     |     |     |     |  —  |     |     |  →   |
| **Footings** |  →   |     |  →  |     |     |     |     |     |  —  |     |      |
| **Square**   |  →   |     |     |     |     |     |     |     |     |  —  |      |
| **Mantel**   |      |     |     |     |     |     |     |     |     |     |  —   |

`→` sends to. `←` receives from. `↔` bidirectional. **MR = Mystery Ranch. Stock = Stockyard. Root = Rootstock.**

Mantel is mostly a terminal sink: things flow IN (moments worth keeping), little flows out except direct queries.

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
**First Aid Kit → Punch List → Foreman.** Appointment scheduled, needs a driving block + maybe a prescription pickup.

FAK emits one handoff to Foreman (the appointment) and one to Punch List (Rx pickup). Punch List may then hand back to Foreman if the pickup needs its own slot. Reminder voice belongs to FAK for the appointment, Punch List for the Rx pickup.

### Pattern C — Hunting → Calendar Blackout
**Mystery Ranch → Foreman.** Draw results, season dates, scouting trip.

Foreman writes a HARD block — **Matt-only scope** per `prefs.md`. Other agents querying Foreman about Matt''s availability inside those windows get a refusal; queries about Kalea, the kids, or anchor-house support continue normally. Don''t cancel a Wyatt ortho because Matt is in the field — shift the driver.

### Pattern D — Hunting → Meals
**Mystery Ranch → Chow Hall.** Harvest comes in. Headed to processor. Processor done.

Chow Hall updates `freezer.json` and adjusts upcoming meal plans accordingly.

### Pattern E — Study → Schedule
**Whetstone → Foreman.** Exam scheduled. Drill block needed. Weak-cluster session.

Foreman places study blocks on Work/Career calendar. Respects 17:30 meals and Sunday — no exceptions, even for cert crunch. Reminder voice when study block approaches: Whetstone.

### Pattern F — Job Hunt ↔ Study
**Footings ↔ Whetstone.** Bidirectional.

- Footings → Whetstone: interview approaching for a role; ramp drills on relevant domains.
- Whetstone → Footings: cert milestone hit; trigger application push or résumé update.

### Pattern G — Hunting → Memory
**Mystery Ranch → Mantel.** Notable harvest. First hunt with a kid. Season highlight.

Mystery Ranch emits a `mantel` handoff with the moment; Mantel files it with appropriate gravity. If the moment touches grief or sacred ground, tone-drop carries through.

### Pattern J — Farm Ops → Schedule
**Stockyard → Foreman.** Slaughter day, weigh-ins, vet visits, multi-hour farm events that need a calendar block. Daily feed cadence does NOT route through Foreman — it''s a known persistent rhythm Foreman respects from the rhythm table.

```
Stockyard writes:
{
  from: "stockyard", to: "foreman",
  subject: "Pig slaughter day — 6-8 hour block",
  payload: { proposed_dates: ["2026-11-07", "2026-11-14"], conflicts_to_check: ["rifle elk season"] },
  status: open
}
```

### Pattern K — Eggs/Harvest → Meals
**Stockyard → Chow Hall.** Egg counts trending up, glut incoming. Or pig in the freezer, processor done. Or chickens culled, broth stock available.

Chow Hall updates `chow-hall/freezer.json` (proteins) or `chow-hall/produce.md` (eggs, fresh harvest), adjusts meal plans toward use-it-up.

### Pattern L — Garden Harvest → Meals
**Rootstock → Chow Hall.** Fresh harvest ready. Tomatoes coming in heavy. Apples on the tree. Gardyn basil at peak.

Chow Hall pulls into meal planning. Preservation prompts (canning, freezing, drying) handed back to Punch List or Rootstock depending on scale.

### Pattern M — Garden Planting → Schedule
**Rootstock → Foreman.** Spring transplant weekend, fall mulching, greenhouse build phase, irrigation install. Multi-hour outdoor work blocks.

Foreman respects sacred blocks; planting windows are weather-sensitive so flexibility from Tim is sometimes required.

### Pattern N — Farm Maintenance ↔ Logistics
**Stockyard ↔ Punch List.** Bidirectional.

- Stockyard → Punch List: coop repair, feed run, water heater for winter, vet supplies pickup.
- Punch List → Stockyard: equipment failure noticed during chores ("the auger''s binding"), feed inventory low.

### Pattern O — Garden Maintenance ↔ Logistics
**Rootstock ↔ Punch List.** Bidirectional. Same pattern — tools, supplies, infrastructure (drip line repair, greenhouse panels, fence work) flow between the two.

### Pattern P — Gardyn Roster Prompts
**Rootstock → Human.** Gardyn (indoor hydroponics appliance) runs on its own app. Rootstock owns the *prompting cadence* — periodically asks Matt to update `gardyn-roster.md` so Chow Hall knows what''s harvestable. Thin handshake, no operational logic, no sync.

### Pattern Q — Document Renewal → Schedule
**Punch List → Foreman.** A document expiration is approaching (DL, CAC, vehicle registration, insurance policy). Punch List emits a milestone handoff; Foreman blocks a calendar slot for the action (DMV appointment, DEERS appointment, online renewal).

Reminder voice belongs to Punch List throughout. Option C.

### Pattern R — CCIR Routing
**Any agent → arbiter''s domain agent.** A family member drops a CCIR observation into a chat session (see `ccir-protocol.md`). The receiving agent routes per the CCIR domain table to the correct agent; that agent logs and confirms back to the notifier.

Cross-agent CCIRs (e.g. an observation that spans vehicle + medical) route to Al for triage. Al never makes the notifier route their own observation.

### Pattern H — Calendar Echo Back
**Foreman → Originating Agent.** Foreman couldn''t fit the request, or there''s a sacred-block conflict.

Foreman writes a return handoff: *"Couldn''t slot oil change Tue 09:00 — Wyatt''s appointment. Try Tue 14:00 or Wed 08:30."*

### Pattern I — Family-Care Echo
**Any → Al → Human.** Session has run long on a weekend. Kids are around.

Al (orchestrator) holds final authority on when to push back on the human. Other agents don''t moralize directly — they flag to Al via handoff, Al decides whether to nudge.

---

## Confirmation Protocol

Before any agent writes to Google Calendar, `handoffs.json`, or any shared state file:

1. **Propose** in chat: *"Here''s what I''m about to write — [diff]. Confirm?"*
2. **Wait for explicit confirmation.** "Yes," "ship it," "do it" — explicit affirmation. Not a thumbs-up emoji, not silence.
3. **Commit** the change.
4. **Report** back: *"Done. [path]."*

No silent writes. Ever. Phase 2 may relax this for trusted patterns, but Phase 1 is propose-then-commit, no exceptions.

---

## Sacred Block Refusals

Foreman is the gatekeeper. When asked to schedule in a sacred block:

- **17:30–19:00 daily (family meal):** REFUSE. Propose 19:00+ or earlier in day.
- **Sunday (any time):** REFUSE work, study, appointments. Mass, family, rest. Override only on Matt''s explicit say-so for a single block, captured in chat for that session — not stored as standing permission.
- **Hunting blackouts (Matt-only):** REFUSE Matt events. Re-route household items to Kalea or backup-adult tier. Bounce to Mystery Ranch for the dates.
- **Kalea drill travel (Kalea-only):** REFUSE Kalea events. Re-route household items to Matt or backup-adult tier.
- **Kalea-flagged blocks:** REFUSE. Never schedule over without Kalea''s confirmation in chat.

Receiving agent (the one that asked) gets a return handoff with the refusal reason + the suggested alternative.

---

## Anti-Loop Discipline

A handoff that bounces back unprocessed twice = stop and surface to the human via Al. Don''t let agents ping-pong. Two strikes, raise the hand.

---

## Quick Reference — Who Owns What

| Domain | Owner Agent | State File |
|---|---|---|
| Calendar | Foreman | Google Calendar + `calendars.md` |
| Tasks | Punch List | `punch-list/tasks.json` |
| Vehicles | Punch List | `punch-list/vehicles.json` + `fleet-state-v1.md` |
| Documents / renewals | Punch List | `punch-list/documents.md` |
| Wyatt licensing | Punch List | `punch-list/wyatt-licensing.md` |
| CCIR routing doctrine | Household-wide | `ccir-protocol.md` |
| Study | Whetstone | `whetstone/progress.md` |
| Meals | Chow Hall | `chow-hall/meal-plan.md` |
| Game meat | Chow Hall | `chow-hall/freezer.json` |
| Hunting seasons | Mystery Ranch | `mystery-ranch/seasons.md` |
| Livestock, eggs, feed | Stockyard | `stockyard/` (eggs-log, flock-config, pigs, turkeys) |
| Plants, orchard, greenhouse | Rootstock | `rootstock/` (plantings.md, garden-plan.md, gardyn-roster.md) |
| Health | First Aid Kit | `first-aid/` |
| Career | Footings | `footings/pipeline.json` |
| Takeoff | The Square | `square/projects/` |
| Memory | The Mantel | `mantel/` |

If two agents seem to want the same fact: re-read this table. One owner only. The other agent references.
