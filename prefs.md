# Bayer Family Ops — Prefs & Conventions

*Household-level decisions, standing rules, schema history. Not personal preferences — those live in `family.md`.*
*Last updated: 2026-05-25*

---

## Formatting Rules

- **ISO dates, always.** `2026-05-15`. Weekday optional for readability: `2026-05-15 (Fri)`.

---

## Source of Truth

- This Git repo is canonical: `github.com/Ground3906/family-ops` (private).
- OneDrive (`C:\Users\ThinkPad X1 Carbon\OneDrive\Desktop\Stuff\Jobs\AA_My Home\Al Bayer Operations`) — **retired 2026-05-15.** Do not write there.
- Google Drive was previously named as canonical — **superseded.** Git only.
- Agents propose; Matt commits. No file is written to the repo silently.

---

## Vocabulary

Locked terms. All agents adopt these without translation, paraphrase, or "fixing."

| Term | Meaning |
|---|---|
| **CCIR** | Commander''s Critical Information Requirement. See `ccir-protocol.md`. Urgent or noteworthy observation that needs routing. |
| **Notifier** | Whoever observes something flagworthy. Any family member, any age. Brain-dumps the observation; mental load ends there. |
| **Arbiter** | The default decision-maker for that domain. Triages, decides, executes (or delegates). |
| **Implement** | A skid-mounted tool (bucket, forks, log splitter, plow). Not "attachment." The Gehl has implements. |
| **Skid / skid steer** | The Gehl 5640E. Both terms interchangeable. |
| **Bobcat** | The animal, not the brand. Our skid steer is a Gehl. If "bobcat" surfaces in conversation, it means the wildlife. |
| **Jackson trailer / pen trailer / pig trailer** | All three names refer to the same asset: 2020 Jackson 8-pen livestock trailer. Any agent may use any of the three. |

---

## Sacred Blocks

No agent schedules over these without Matt''s explicit chat-session override. Standing override claims are not honored — every override is per-session, per-block.

### Daily
- **17:30 — Family meal.** HARD. No work, no study, no appointments. Propose 19:30+ or earlier in the day if rescheduling is needed.

### Weekly
- **Sunday — family day.** HARD all day. Mass, Faith Formation 0900-1015, rest. No work, no study, no non-urgent appointments. No exceptions without Matt''s explicit override in chat.

### Hunting seasons
- HARD. See `mystery-ranch/blackouts.md`. Mystery Ranch writes; Foreman protects.
- **Matt-only scope.** Hunting blackouts freeze Matt''s schedule, not the whole household. Kalea, the kids, school, sports, medical appointments, anchor-house visits — all continue running normally during hunting blocks. Foreman doesn''t cancel a Wyatt orthodontist appointment because Matt is in the field; it routes the drive to Kalea (or backup-adult tier) instead.

### Kalea drill travel
- HARD for Kalea-only events. When Kalea is on USMC Reserve drill travel (Hawaii, ~2 multi-day chunks/year), her calendar is frozen for that window.
- **Kalea-only scope.** Drill travel does NOT freeze the household — Matt and the kids continue normally. Routine items that would normally route to Kalea bump up the backup-adult tier list (default Tier 1: Oma & Papa).
- Parallel structure to Matt''s hunting blackouts. Mystery Ranch is to Matt what drill is to Kalea: a domain-specific sacred block that protects one person, not the family.

### Kalea canning — Kalea-only scope
- HARD for Kalea's kitchen territory. Two sessions/year, 3 days each:
  - **(1) Peaches** — ~Labor Day (early September)
  - **(2) Apples / jalapeños / etc.** — ~October
- During canning sessions: Chow Hall simplifies meals and handles jar/lid/pectin inventory. Rootstock aligns harvest peaks. Stockyard feeds in if meat canning is in scope.
- Parallel structure to hunting blackouts and drill travel — protects Kalea's window, not the whole household.

### Kalea-flagged blocks
- Any block marked `kalea_hold: true` in agent state. Untouchable without her chat-session confirmation.

### Specific sacred dates
- **2026-04-25 — Loretto Chapel day.** Mantel-owned sacred memory. Tone-drop on contact. Foreman marks but never schedules over.

### Mass — floating sacred
The weekly Mass obligation is always a protected block. It is not pinned to a specific time slot — it travels through Foreman's adjudication process.

**Default slot:** Sunday 08:00, St. Joseph's Catholic Church, Salida.

**When a conflict is detected:** Foreman flags and proposes adjudication using the mass options in order (see `foreman.md`). The proposed replacement slot is **immediately soft-held** — both the original default slot and the adjudicated slot are protected simultaneously until Matt or Kalea confirms. No agent may schedule over either slot during the adjudication window.

**On confirmation:** The original default slot releases. The confirmed slot locks as the sacred block for that week.

**Anticipated Mass (Saturday 17:00, St. Joseph's Salida)** counts as Sunday obligation and is Foreman's preferred conflict-resolution path when Saturday is clean.

No agent schedules over any confirmed or proposed mass time. Ever.

---

## Equipment Access Principle

**Charter-level rule.** Any agent may use any owned implement, trailer, or shared asset for maximum efficiency. No check-out protocol, no permission ceremony. The Gehl, the implements, the trailers, the deck trailer, all of it — open access across the agent crew.

**Conflicts** (two agents wanting the same asset at the same time) route through the Punch List handoff queue — first-claim wins, second-claim gets re-slotted.

**Maintenance ownership stays put regardless of who used the asset.** Stockyard might haul pigs in the Jackson trailer, but Punch List still owns trailer MX (bearings, tires, electrical, registration). Use is open; care is owned.

---

## Pill Color Palette (locked)

All agents and widgets use these exact hex values. Never substitute or approximate.

| Pill | Person | Color |
|---|---|---|
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
| KIDS | Kids group | `#a0c840` |

---

## Pill Group Definitions + Collapse Doctrine

### FAM group
All 8 household members: D, K, W, M, R, C, E, B6.

Collapse logic:
- All 8 present → FAM pill
- 7 present → FAM −[missing]
- 5 or fewer → list individuals explicitly

### KIDS group
The 6 Bayer children: W, M, R, C, E, B6.

B6 joins the KIDS group upon post-birth confirmation (~2026-08-15). Until then, KIDS = [W][M][R][C][E] (5 members).

Collapse logic:
- All 6 present → KIDS pill
- 5 present → KIDS −[missing]
- 4 or fewer → list individuals explicitly

Pre-birth collapse (5-member group):
- All 5 → KIDS pill
- 4 present → KIDS −[missing]
- 3 or fewer → list individuals explicitly

**B6_ACTIVE gate:** B6 is in the KIDS and FAM member arrays from day one for threshold math. However, the `−B6` subtraction pill is suppressed from display until `B6_ACTIVE = true` in the widget. Flip this flag post-birth confirmation. Until then, B6 is invisible on all tiles.

### Pill ownership doctrine
Pills identify who **owns** the event — not who drives, not who attends in support. Driver and vehicle assignment is Punch List territory, surfaced in the detail panel on tap. Never put a logistics person on the pill stack. Retroactive to all entries.

---

## Calendar Category Emoji Map

Left-side color stripes on calendar tiles are replaced by category emoji in v2.0. Colors belong to pills/people only — never to categories.

Full locked map:

| Emoji | Category |
|---|---|
| 🚸 | Kids events |
| 🏠 | Family events |
| ✝️ | Active church participation (Mass, Youth Group, Faith Formation, Knights, Stations, serving rotations — any event Bayers attend at church) |
| 📖 | Liturgical calendar entries (feast days, Holy Days, season markers) |
| ➕ | Medical appointments |
| 🐾 | Animals / farm |
| 🍀 | 4H events |
| 🌱 | Garden / Rootstock events |
| 📋 | Meetings |

All agents adopt this map. Never invent a new category without locking it here first.

---

## Tentative Event Treatment

Events flagged `tentative=true` in `calendars.md` render with an **amber tint background + wide diagonal stripe pattern + dashed amber border**. Pills and title render at full opacity on top. No solid color change — texture and tint only. Colorblind-safe by design.

**Vocabulary:** "tentative" and "TBD" are interchangeable in conversation. In the data, the schema flag is always `tentative=true`. Never `tbd=true` or any other variant. Any agent or human using either word maps to `tentative=true` in the file.

Routing isn''t only by task domain — it''s also by **tone fit**.

A grief moment routes to The Mantel even if the surface request is logistical ("can you remind me of the date we lost X"). A hunting story routes to Mystery Ranch even if there''s no scheduling action needed. A funny kid moment routes to The Mantel.

Tone-routing exists because the agent crew runs distinct personalities, and the right voice for a moment is part of getting the moment right. Al watches for tone mismatches; if a request lands on the wrong agent for voice reasons, Al re-routes silently.

---

## Anti-Atrophy Principle (Option C)

**Each agent owns its own reminders.**

Foreman owns the calendar truth (the *when*). Domain agents own the voice and cadence of the reminder (the *what* and *how*). A Punch List item with a deadline lives in Foreman''s calendar; the prompt that surfaces it sounds like Punch List, not Foreman.

This is Option C from the build conversations: silent-backbone Foreman, voiced reminders from domain agents. Prevents agents from going dormant between major events. Each domain agent has its own reminder cadence and never delegates "remind me about this" to Foreman — only "block time for this."

Cross-agent dependencies resolve to whoever has the more time-sensitive or domain-primary stake.

---

## Tone Convention

The agent crew runs Tool Time energy by default. Al is the straight man; Matt is "Tim"; Kalea is "Jill." Binford, Wilson-over-the-fence wisdom, the grunt — welcome when the bit lands naturally. Don''t force it; don''t audition.

**Drop the bit instantly and completely for:**
- Anything First Aid Kit handles in earnest (real medical concerns)
- Family crisis, grief, injury, loss
- Sacred memories (e.g., the Loretto Chapel day, 2026-04-25)
- Bad news of any kind
- Any moment where the reader might be personally affected

Resume only when the moment has clearly passed. Read the room.

---

## Privacy Conventions

- **K. apt specifics:** Masked in all visible output regardless of context. Full detail (type, provider, location) lives in `first-aid/people/KB.md` only. Never surface in open chat, shared file, or any agent output.
- **`first-aid/` directory:** Access = Matt + Kalea only (private repo is the access control layer). Any extension of access beyond the private repo = deliberate decision, logged in Decision Log below.

---

## ID & Document Renewals — Recurring Watch

Renewal-watch is a Punch List responsibility. The data lives in `punch-list/documents.md`; Foreman fires the prompts derived from it. Standing rule: **never re-surface a constraint Matt has explicitly acknowledged as dormant** (e.g. CCW). Matt reopens it or it stays dormant.

Active watch items (sourced from `punch-list/documents.md`):
- Kalea CAC — expires 2026-07-31 (priority: DEERS appointment, earlier-rather-than-later given Aug birth)
- Jackson trailer registration — expires 2026-10
- Kalea CO DL — expires 2027-05-27
- Matt CO DL — expires 2028-12-07
- Insurance policy renewals — semi-annual (auto) / annual (homeowners, pen trailer, personal property)

---

## Infrastructure Gaps

- **Backup power:** No battery backup system. No generator. The well pump requires grid electricity. In any power outage, water access is affected. **Acknowledged constraint — do not re-surface.** Matt reopens if/when the gap is closed.

---

## Tow Protocol

When a Bayer fleet vehicle needs a tow:

1. **Austin Auto first.** Cañon City — preferred shop, long relationship, knows the fleet. Their tow service or coordinated tow to their bay.
2. **USAA fallback.** If the breakdown is outside Austin Auto''s practical range (long-haul highway breakdown, out-of-area trip), USAA roadside coverage takes over.

The decision is Austin-Auto-first by default — distance is what flips it to USAA, not preference.

---

## Friend Contact Conventions

- **Tim Schuker:** Friend-call reminder only. No annual date. Foreman may flag opportunistically when calendar has space. Do not create a recurring calendar event.

---

## Recurring Opportunistic Windows

- **Sunday 0900-1015 — FF window:** Known open slot during Faith Formation for Salida errands or time-sensitive tasks when Foreman is hunting a calendar slot. Opportunistic, not guaranteed. Does not override Sunday-sacred rules for work or study.

---

## Decision Window Doctrine

**Kalea is a morning person. Matt is a night owl.**

Any agent or system push that requires Kalea's decision-making input **cannot fire after 20:00.** Her cognitive capacity falls short past that hour and the decision won't land cleanly.

- **Kalea-input agents** (Chow Hall meal planning, family logistics requiring her sign-off, anything that needs a "yes" from Jill) → morning or early-afternoon windows only.
- **Matt-only late-night work** (Whetstone study, deep design sessions, solo agent builds) → fine post-20:00.
- Foreman enforces this passively: if a prompt would fire after 20:00 and requires Kalea, it holds until the next morning window.

Charter-level scheduling rule.

---

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-05-15 | Git repo (`github.com/Ground3906/family-ops`) established as SSoT | Consolidate to single source; OneDrive was informal scratch |
| 2026-05-15 | OneDrive retired as scratch/write location | Git is canonical; no parallel writes |
| 2026-05-15 | Google Drive superseded as canonical location | Never fully implemented; Git replaces it |
| 2026-05-15 | Hunting blackouts scoped Matt-only, not household-wide | Kalea and kids continue normal scheduling during Matt''s hunting weeks; routing falls to Kalea or backup-adult tier |
| 2026-05-15 | Kalea drill travel established as Kalea-only sacred block | Parallel to hunting blackouts; protects Kalea''s window, not the household |
| 2026-05-15 | Vocabulary section locked (CCIR, notifier, arbiter, implement, skid, bobcat=animal, Jackson/pen/pig trailer all equivalent) | Prevents agent paraphrase drift; protects Tool Time idiom |
| 2026-05-15 | Equipment Access Principle adopted — open use, owned MX | Removes friction; MX ownership stays anchored to asset, not user |
| 2026-05-15 | Agent personality routing established alongside task routing | Tone-fit is part of getting a moment right; Al watches for tone mismatches |
| 2026-05-15 | Anti-atrophy principle (Option C) adopted | Each agent owns its own reminders; Foreman is silent backbone, domain agents are voice |
| 2026-05-15 | Tow protocol locked: Austin Auto first, USAA fallback outside range | Distance flips it, not preference |
| 2026-05-22 | Kalea canning established as Kalea-only sacred block | Two sessions/year (~Labor Day peaches, ~October apples+). Parallel to hunting blackouts and drill travel. |
| 2026-05-22 | Decision window doctrine locked — Kalea-input agents cannot fire after 20:00 | Kalea is a morning person; decisions after 20:00 don't land. Matt-only work fine post-20:00. |
| 2026-05-25 | Mass — floating sacred block doctrine locked | Mass obligation always protected regardless of slot. Foreman adjudicates conflicts using 4-option mass menu. Anticipated Mass (Sat 17:00) is preferred conflict-resolution path. Both original and adjudicated slots soft-held during window. |
| 2026-05-25 | Pill Ownership Doctrine locked — charter-level | Pills = event owner, not driver/logistics. Driver/vehicle is Punch List territory, surfaced in detail panel on tap. Retroactive to all entries. |
| 2026-05-25 | Category emoji map locked | Left-side color stripe → category emoji in v2.0. Colors belong to pills only. Full map in prefs.md. |
| 2026-05-25 | Tentative event treatment locked — diagonal stripe | Repeating diagonal hatching overlaid on tile. Pills and title at full opacity on top. No new color. Colorblind-safe. |
| 2026-05-25 | Full pill color palette locked — 13 pills | All hex values confirmed. D=#9a5828, K=#1a50e0, W=#cc2233, M=#9944cc, R=#f040b8, C=#2070b8, E=#156e2a, B6=#faa030, OMA=#7755cc, PAPA=#6ec898, GUEST=#E8DFC0, FAM=#7a7aaa, KIDS=#a0c840. |
| 2026-05-25 | KIDS pill group defined + collapse doctrine locked | KIDS=[W][M][R][C][E][B6]. B6 joins post-birth ~Aug 15. FAM collapses at 8/7, KIDS at 6/5. ≤4 kids or ≤5 FAM = list individuals. |
| 2026-05-25 | B6_ACTIVE gate locked | B6 in arrays day one; −B6 display suppressed until B6_ACTIVE=true in widget. Flip post-birth. |
| 2026-05-25 | Three-pass pill logic locked | Collapse → travel subtract → re-collapse. Travel suppression applied after collapse, not before. Prevents swim practice rendering as individuals when traveler removed. |
| 2026-05-25 | Pill display order locked | Always: D→K→W→M→R→C→E→B6→OMA→PAPA→GUEST. FAM/KIDS always far left. |
| 2026-05-25 | Swim meets = family category locked | Swim meets use :: family. Swim practice uses :: kids. Swim meets are whole-family events; practice is kids-only. |
| 2026-05-25 | Agent emojis updated | Chow Hall: 🍴. Mystery Ranch: ⛺. Medical category: ➕. All agents adopt. |
| 2026-05-25 | Tentative treatment updated | Amber tint + wide diagonal stripes + dashed amber border. More prominent than v2.0 diagonal-only. |

---

## Schema History

| Version | Date | Notes |
|---------|------|-------|
| 1 | 2026-05-15 | Initial build. Git SSoT established. Foundational files created: README, family, prefs, handoffs. |
| 1.2 | 2026-05-22 | Kalea canning sacred block added. Decision window doctrine added. Additive only. |
| 1.3 | 2026-05-25 | Mass floating sacred block added. Pill Ownership Doctrine added. Category emoji map added. Tentative event treatment locked. Decision log updated. |
| 1.4 | 2026-05-25 | Pill color palette locked (13 pills). KIDS group + collapse doctrine added. Tentative/TBD vocabulary locked. Cross emoji stripped from feast titles. |
| 1.5 | 2026-05-25 | B6_ACTIVE gate. Three-pass pill logic. Pill order locked. Swim meets=family. Agent emojis updated (Chow Hall 🍴, Mystery Ranch ⛺, medical ➕). Tentative treatment updated. |
