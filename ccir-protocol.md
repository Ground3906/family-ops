# CCIR Protocol — Bayer Household Urgent-Issue Routing

**Schema version:** 1
**Owner:** Household-wide doctrine (read by all agents)
**Origin:** USMC Commander''s Critical Information Requirement, adapted for family ops
**Last updated:** 2026-05-15

---

## What this is

A standing protocol for moving urgent or noteworthy issues from whoever first observes them ("notifier") to whoever decides and executes ("arbiter") — without losing the thought, dropping the ball, or burning notifier''s mental bandwidth.

The protocol exists because the household runs eight people across a farm, a workshop, school, military reserve obligations, and a six-kid logistical surface area. A check-engine light Kalea notices on the Dodge during a Pueblo run cannot live in her head until she sees Matt next. The pig that looks off-feed Wyatt spots during evening chores cannot wait for the next family meeting. The well pump making a new noise the twins hear cannot disappear.

**Goal:** clear notifier''s brain. Get the observation into the system. Arbiter triages on their cadence, not notifier''s.

---

## Vocabulary

| Term | Definition |
|---|---|
| **CCIR** | Commander''s Critical Information Requirement. A category of observation important enough to surface immediately, even when notifier doesn''t know what to do with it. |
| **Notifier** | Whoever observed it. Any family member, any age. Job: brain-dump the observation, then hand it off. |
| **Arbiter** | The default decision-maker for that domain. Triages, decides, executes (or delegates execution). |
| **Drop slot** | Wherever the notifier can dump the observation without ceremony — chat session, repo handoff, sticky note, voice memo, text to Matt. Any of these is valid. |

---

## Notifier''s job

1. **Observe.** Something seems off, new, or worth flagging.
2. **Drop it.** Brain-dump into the nearest available slot. No formatting required. No diagnosis required. "The Tahoe sounds funny" is a complete CCIR.
3. **Walk away.** The mental load is over. Arbiter has it.

Notifier does **not** need to:
- Know what''s wrong
- Know who should fix it
- Know how urgent it is
- Decide whether it''s worth mentioning (if it crossed your mind, drop it)

---

## Arbiter''s job

1. **Triage.** Is this urgent (immediate action), watchable (log and monitor), or noise (acknowledge and close)?
2. **Decide.** Schedule, delegate, or execute.
3. **Close the loop.** Tell notifier what happened — even if the answer is "noted, no action." Notifier needs to know it wasn''t dropped.

---

## CCIR triggers by domain

| Domain | Default arbiter | Routing agent | Examples |
|---|---|---|---|
| Vehicles, equipment, fleet MX | **Matt** | Punch List | Check engine light, new noise, fluid leak, dashboard warning, tire wear, registration expiring |
| Livestock health | **Matt** | Stockyard | Pig off-feed, hen not laying, injury, predator sign, fence breach |
| Garden, orchard, greenhouse | **Matt** | Rootstock | Hail damage, irrigation failure, deer breach, frost surprise, tree damage |
| House infrastructure | **Matt** | Punch List | Well pump noise, propane low, electrical issue, plumbing leak, HVAC behavior |
| Kid medical / health | **Matt + Kalea jointly** | First Aid Kit | Fever, injury, rash, behavior shift, sleep disruption beyond normal |
| Adult medical | **The affected adult** | First Aid Kit | Self-arbitrated. Other spouse is notified, not arbiter. |
| Calendar collision | **Matt** | Foreman | Two events landed on the same window, conflict with sacred block |
| Documents / paperwork / expiry | **Matt** | Punch List | ID/registration/insurance/CAC nearing expiration, unexpected letter, IRS notice |
| Financial anomaly | **Matt** | Punch List | Unexpected charge, account access issue, payment failure |
| Memory-worthy moment | **Whoever was there** | Mantel | Worth keeping. Sacred or everyday. |

When in doubt about which domain something belongs to: drop it on Matt. Re-routing is cheap; losing the observation is not.

---

## Edge cases

### Notifier and arbiter are the same person
Matt notices a Tahoe oil leak. He is both notifier and arbiter for vehicle issues. Action: log it directly into Punch List backlog. No handoff ceremony needed. The protocol''s value is when notifier ≠ arbiter; when they''re the same person, skip to step 3.

### Arbiter is unreachable
Kalea is on drill in Hawaii. Wyatt spots a Dodge issue. Options, in order:
1. If non-urgent: drop into chat session, repo handoff, or text — Matt picks it up async when he''s back online.
2. If urgent and Matt is also unreachable: escalate to nearest reachable adult (Oma & Papa, Uncle Doug, etc. per backup-adult tier).
3. If actively dangerous (smoke, flames, blood, severe injury): bypass the protocol entirely. Call for help. The protocol is for routine routing, not emergencies.

### Multiple notifiers see the same thing
First to drop it wins. Subsequent observations get appended to the same item, not duplicated. If two observations differ in detail, both stay — arbiter reconciles during triage.

### Notifier is a kid
Fully valid. Wyatt, Molly, Rileigh — all old enough to be notifiers. Twins and infant get observed *on* rather than observing. A kid''s drop should be acknowledged with the same seriousness as an adult''s; the protocol works only if notifiers trust the system.

### The observation is mid-task and can''t be written down
Voice memo to self. Text to Matt. Even just saying it out loud to whoever else is present so they can carry it. Anything that gets it out of working memory and onto something durable.

### Notifier doesn''t want to bother the arbiter right now
That''s the whole point of the drop slot. The arbiter triages on their schedule, not the notifier''s. Drop it, walk away.

---

## How agents handle CCIR routing

When a Bayer family member tells an agent about an observation that fits a CCIR domain:

1. Capture the observation verbatim. Don''t paraphrase, don''t reframe, don''t "fix" it.
2. Route to the appropriate agent per the domain table.
3. Confirm with the notifier that it''s been logged: *"Logged. Punch List has the Tahoe noise. Matt''ll triage."*
4. Do not press the notifier for diagnosis details they don''t have. "It sounds funny" is a complete observation.

If the agent is uncertain which domain the observation belongs to: capture it, surface to Al, let Al route. Don''t make the notifier route their own observation.

---

## Decision log

| Date | Decision | Rationale |
|---|---|---|
| 2026-05-15 | CCIR protocol established as household doctrine | Consolidates ad-hoc routing patterns into a single vocabulary all agents adopt. Reduces mental load on notifier. |
| 2026-05-15 | Matt set as default arbiter for vehicles, equipment, fleet, infrastructure, garden, livestock, documents | Reflects current household division of operational responsibility. Kalea arbitrates jointly on kid medical. |

Schema changes: bump version above, log here.
