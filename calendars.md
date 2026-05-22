# calendars.md — Bayer Family Calendar State (v0)

**Owner:** Foreman
**Schema version:** 1
**Last full rewrite:** 2026-05-22
**Source-of-truth rule:** This file is the digital plan. The whiteboard on the fridge is authoritative for daily ops. Tim and Jill mirror confirmed events from here to the whiteboard.

Future schema changes: bump `Schema version`, note migration in `prefs.md`.

---

## Active Calendars (Phase 1)

| Calendar | Owner | Status |
|---|---|---|
| Whiteboard (fridge) | Family | **Authoritative for daily ops.** Tim/Jill hand-write. |
| `calendars.md` (this file) | Foreman | Digital plan. Phase 1 = propose-only. |
| Google Calendar — Matt | Matt | TBD — confirm whether in use |
| Google Calendar — Kalea | Kalea | TBD |
| Google Calendar — Family | Shared | TBD |
| Google Calendar — Hunting | Matt | TBD |

**Phase 1 sync model:** Foreman appends confirmed events to `## Upcoming Events` below. Tim/Jill mirror to the whiteboard. No automation, no external writes. Phase 2 revisits.

---

## Sacred Blocks

### Daily
- **17:30-19:00 — Family meal.** HARD. No exceptions without Tim's chat-session override.

### Weekly
- **Sundays — all day.** HARD. Mass 0800. Faith Formation 0900-1015 (school year). Family/rest. No work, no study, no non-essential appointments.

### Annual / Liturgical
- **Lent (Ash Wed → Easter Vigil):**
  - Ash Wednesday — Mass attendance.
  - Fridays — Stations of the Cross. Fish dinner (no meat).
  - Holy Thursday — evening Mass, kids serving.
  - Good Friday — 1200 Stations + 1500 Service. No meat.
  - Holy Saturday — Easter Vigil ~1745.
- **Easter Sunday + Octave.**
- **Confirmation cycle** — 1845-2000 evening sessions; clusters Feb–Apr.
- **Other Holy Days of Obligation** — capture as they come.
- **Christmas / Epiphany Jan 6.**
- **Thanksgiving** — 1000 Mass.

### Family Sacred Dates
- **November 8 — wedding anniversary** (Matt + Kalea, eloped Nov 2013).
- **April 25 — Loretto Chapel day.** Mantel-owned sacred memory. Foreman marks but never schedules over.

### Hunting Blackouts — Matt-only scope
See `mystery-ranch/blackouts.md` — read at session start. Mystery Ranch writes; Foreman protects. **Freezes Matt's calendar only**; Kalea, kids, household continue normally. Re-route drivers per `family.md` backup-adult tier.

### Kalea Drill Travel — Kalea-only scope
Per `prefs.md`. Freezes Kalea's calendar only; household continues normally with routing falling to Matt or backup-adult tier (default Tier 1: Oma & Papa).

### Kalea Canning — Sacred blocks (Kalea-only scope)
Two sessions/year: (1) peaches ~Labor Day, (2) apples/jalapeños/etc ~October. 3 days each. Foreman blocks territory; Chow Hall handles meals + inventory during session.

---

## Weekly Recurring Shape (Academic Year — Aug–May)

Confirm exact times each season; this is the shape, not the truth.

### Monday
- K. apt — weekly, ~1400 or 1515. Location varies; often Salida.
- Pig feed (Punch List).

### Tuesday
- M. Knights of Columbus — monthly, ~2nd Tue 1800.
- Algebra teaching (Tim) — PM during school year. Confirm season.
- Pig feed.

### Wednesday
- Salida runs — common, 1130-1530 window. Disambiguate per event.
- **Winter:** Wrestling 1430-1630 Salida.
- **Spring:** W. Track 1545-1700.
- Pig feed.

### Thursday
- Youth Group 1830-2000 (older kids) — seasonal, not year-round. Confirm window each year.
- Swim lessons in season (~Thu noon block).
- Some weeks K. apt 1400.
- Lenten Mass 1800 some Thursdays.

### Friday
- Pig feed.
- Chicken feed (Fri or Sat) — 3 bags.
- Stations of the Cross during Lent.

### Saturday
- 4H meetings monthly (~1300-1400).
- Sports: X-country (fall), basketball (winter), track (spring). Bus depart often 0600 / 0645 for away games.
- Pig feed.

### Sunday — SACRED, NO SCHEDULING
- 0800 Mass — St. Joseph's Salida.
- 0900-1015 Faith Formation (school year only — Aug–May).
- Kids serving rotations (W-Serve, M-Serve, Molly-Serve).
- Matt-EM on rotation.

---

## Recurring Medical

- **W. orthodontist** — ~6 week intervals, often Pueblo, often 0830.
- **W. swim lessons** — Thu in season.
- **Kids dentist** — quarterly, often bulk-booked. Matt = Salida Family Dental. Everyone else = Canyon Family Dental, Cañon City.
- **K. apt** — weekly Mon (above).

---

## Farm Rhythm (Aware-of, not Foreman-planned)

Owned by Punch List or Tim directly. Foreman doesn't book over an obviously-blocked feed window without asking.

- Pig feed — Mon/Wed/Fri/Sat regular cadence.
- Chicken feed — weekly 3 bags.
- Slaughter / butcher — late fall (Oct/Nov).
- Pig weigh-ins and dewormings — growing cycle.
- Turkey raise → harvest — spring → early April.

---

## Whiteboard Conventions (Reference Only)

Tim's whiteboard legend. Foreman reads, never writes.

- **Red outline around date** = trash pickup (every 4 weeks, not weekly).
- **Orange number, upper-right of cell** = daily egg count (Stockyard data).
- **Red writing** = urgent, liturgical, or repeating reminder.
- **Single-letter prefixes:**
  - `M.` + activity → Matt (`M. Knights 1800`).
  - `M` + name context → Molly (`Molly Bday`).
  - `K.` → Kalea (always).
  - `W.` → Wyatt.
  - `R.` → Rileigh.
  - `C` / `Cullen` → twin.
  - `E` / `Emmitt` → twin.
- **EM** = Eucharistic Minister.
- **Salida** = medical/therapy/sports town.
- **Pueblo** = specialist medical (often W. ortho).
- **`D-EM`** = Matt as Eucharistic Minister. `D` is the legacy "Dad" prefix predating standardized cast naming. `D-` and `M.` are the same person.

---

## Standing Milestones (Derived from Domain Agents)

Foreman holds the date; the originating agent voices the reminder (Option C). When the prompt fires, the named agent surfaces the action.

### Punch List milestones
- **2026-06-15** — Kalea CAC renewal prompt. CAC expires 2026-07-31. Schedule DEERS appt. Earlier-rather-than-later given Aug 2026 birth timing. Voice: Punch List.
- **2026-08-01** — Jackson trailer registration renewal prompt (60 days before Oct expiration). Voice: Punch List.
- **Spring 2027** — Gehl skid steer oil change. Voice: Punch List.
- **2027-02-27** — Kalea CO DL renewal prompt (90 days before 2027-05-27 expiration). Voice: Punch List.
- **2028-09-07** — Matt CO DL renewal prompt (90 days before 2028-12-07 expiration). Voice: Punch List.

### Wyatt licensing milestones
From `punch-list/wyatt-licensing.md`. Voice: Punch List.
- **2026-08-01** — Research CO driver-ed providers for Wyatt
- **2026-09-15** — Enroll Wyatt in driver ed
- **2026-12-15** — Confirm driver ed cert issuance on track
- **2027-01-01** — Schedule DMV appt for Wyatt permit application
- **2027-04-22** — Permit checkpoint — 3 months in
- **2027-07-22** — Permit checkpoint — 6 months in
- **2027-10-22** — Permit checkpoint — 9 months in
- **2028-01-01** — Schedule CO road test for Wyatt license
- **2029-01-01** — Confirm restricted phase ending cleanly

### Mantel milestones
- **Annual November 8** — Wedding anniversary. Voice: Mantel.

---

## Travel / Extended Absences

Whiteboard regularly marks `Mom Leaves`, `Mom Returns`, `K Hawaii`, `M+K gone`, etc. Capture confirmed travel here as soft blocks; surface conflicts at session start. Kalea USMC drill travel is a sub-category — Kalea-only scope sacred block.

*(Populated as confirmed.)*

---

## Upcoming Events

Foreman appends here only after Tim/Jill confirm proposals. Phase 1: copy to whiteboard after committing.
**Doctrine: It always makes the calendar. Unresolved items get flag=true. Nothing stays off pending resolution.**
Last batch: 2026-05-22. All entries widget-readable [CAL] / [CAL-RECUR] format.

---

### RECURRING — Weekly

[CAL-RECUR weekly start=2026-05-03 day=sun] 08:00 Mass — St. Joseph's Salida :: liturgical :: notes="Bring eggs for Fr. Joe"

---

### RECURRING — Monthly
<!-- PQ-17: [CAL-RECUR monthly] support needed in v1.14 for Knights + Fairboard. Individual entries written per occurrence below until then. -->

---

### FAITH FORMATION — School Year 2026-27
<!-- School year Aug–May. Start date TBD. Flagged until confirmed with parish. -->
[CAL-RECUR weekly start=2026-08-01 day=sun] 09:00 [W][M][R] Faith Formation :: kids :: flag=true :: notes="🚩 Fall start date unconfirmed — verify with parish"

---

### YOUTH GROUP — 2026 Season
<!-- Seasonal only — NOT year-round. End date unconfirmed. Flagged. -->
[CAL] 2026-05-14 18:30 Youth Group :: kids :: flag=true :: notes="🚩 Season end date unconfirmed"
[CAL] 2026-05-21 18:30 Youth Group :: kids :: flag=true :: notes="🚩 Season end date unconfirmed"
[CAL] 2026-05-28 18:30 Youth Group :: kids :: flag=true :: notes="🚩 Season end date unconfirmed"

---

### LITURGICAL — 2026

[CAL] 2026-02-18 ALL-DAY Ash Wednesday — Mass attendance :: liturgical
[CAL] 2026-02-20 ALL-DAY Lenten Friday — Stations + fish dinner :: liturgical
[CAL] 2026-02-27 ALL-DAY Lenten Friday — Stations + fish dinner :: liturgical
[CAL] 2026-03-06 ALL-DAY Lenten Friday — Stations + fish dinner :: liturgical
[CAL] 2026-03-08 ALL-DAY DST begins — protect Sunday :: misc
[CAL] 2026-03-13 ALL-DAY Lenten Friday — Stations + fish dinner :: liturgical
[CAL] 2026-03-20 ALL-DAY Lenten Friday — Stations + fish dinner :: liturgical
[CAL] 2026-03-27 ALL-DAY Lenten Friday — Stations + fish dinner :: liturgical
[CAL] 2026-04-02 18:00 Holy Thursday Mass — W. serving :: liturgical
[CAL] 2026-04-03 12:00 Good Friday — Stations 1200 + Service 1500 :: liturgical
[CAL] 2026-04-04 17:45 Easter Vigil :: liturgical
[CAL] 2026-04-05 ALL-DAY Easter Sunday :: liturgical
[CAL] 2026-04-25 ALL-DAY Loretto Chapel day — sacred memory :: liturgical
[CAL] 2026-05-01 ALL-DAY St. Joseph the Worker :: liturgical
[CAL] 2026-05-13 ALL-DAY Our Lady of Fatima :: liturgical
[CAL] 2026-05-15 ALL-DAY St. Isidore the Farmer — patron of Edelweiss :: liturgical
[CAL] 2026-05-31 ALL-DAY Visitation :: liturgical
[CAL] 2026-11-01 ALL-DAY DST ends — protect Sunday :: misc
[CAL] 2026-11-26 10:00 Thanksgiving Mass :: liturgical :: location="St. Joseph's Salida"
[CAL] 2026-12-25 ALL-DAY Christmas :: liturgical
[CAL] 2027-01-06 ALL-DAY Epiphany / Three Kings :: liturgical

---

### MILESTONES — Punch List / Wyatt / Mantel

[CAL] 2026-06-15 ALL-DAY Kalea CAC renewal prompt — DEERS appt :: misc
[CAL] 2026-08-01 ALL-DAY Wyatt driver-ed provider research :: misc
[CAL] 2026-08-01 ALL-DAY Jackson trailer registration prompt :: misc
[CAL] 2026-09-15 ALL-DAY Enroll Wyatt in driver ed :: misc
[CAL] 2026-11-08 ALL-DAY Wedding anniversary — Matt + Kalea :: misc
[CAL] 2026-12-15 ALL-DAY Wyatt driver ed cert issuance check :: misc
[CAL] 2027-01-01 ALL-DAY Schedule Wyatt DMV permit appt :: misc
[CAL] 2027-02-27 ALL-DAY Kalea CO DL renewal prompt :: misc
[CAL] 2027-04-22 ALL-DAY Wyatt permit checkpoint — 3 mo :: misc
[CAL] 2027-07-22 ALL-DAY Wyatt permit checkpoint — 6 mo :: misc
[CAL] 2027-10-22 ALL-DAY Wyatt permit checkpoint — 9 mo :: misc
[CAL] 2028-01-01 ALL-DAY Schedule Wyatt CO road test :: misc
[CAL] 2028-09-07 ALL-DAY Matt CO DL renewal prompt :: misc
[CAL] 2029-01-01 ALL-DAY Wyatt restricted phase ending check :: misc

---

### MAY 2026

[CAL] 2026-05-05 10:00 [K][D] Prenatal apt — Pueblo :: appointments :: stripe=appt :: location="Pueblo, CO"
[CAL] 2026-05-06 ALL-DAY trash-day
[CAL] 2026-05-14 ALL-DAY [W] Field trip — Sky Zone :: kids :: location="Colorado Springs, CO"
[CAL] 2026-05-14 ALL-DAY [M][R][C][E] PJ Day :: kids
[CAL] 2026-05-16 11:00 [R] Haircut :: kids
[CAL] 2026-05-16 11:00 [W] Art :: kids
[CAL] 2026-05-16 17:00 Mass — St. Joseph's Salida :: liturgical
[CAL] 2026-05-18 10:00 [K] Apt — Gina :: appointments :: stripe=appt
[CAL] 2026-05-19 08:00 [M][R] Triathlon — Westcliffe :: kids :: location="Westcliffe, CO"
[CAL] 2026-05-22 ALL-DAY [D] Pick up wood shavings — Ryan Stover :: misc :: notes="In town"
[CAL] 2026-05-23 11:00 [R][M] Apt — Tacey :: appointments :: stripe=appt
[CAL] 2026-05-28 ALL-DAY [W][M][D] Jackpot pig show — Brighton :: animals :: location="Brighton, CO" :: flag=true :: notes="🚩 F-01 swim meet conflict — logistics unresolved"

---

### JUNE 2026

[CAL] 2026-06-01 ALL-DAY [W] Sweden trip :: kids :: span=2026-06-13 :: flag=true :: notes="🚩 F-05 drop-off pickup chaperone logistics unresolved"
[CAL] 2026-06-03 ALL-DAY trash-day
[CAL] 2026-06-03 ALL-DAY [D] NV drop — Austin Automotive :: misc :: location="Austin Automotive" :: notes="Kalea drives Tahoe Matt drives NV. Pickup day = Tahoe drop day TBD"
[CAL] 2026-06-04 13:40 [K][D] Prenatal apt :: appointments :: stripe=appt
[CAL] 2026-06-05 ALL-DAY [W][M][R] Swim meet — Las Animas :: kids :: location="Las Animas, CO" :: flag=true :: notes="🚩 F-01 Castle Rock jackpot same day — logistics unresolved"
[CAL] 2026-06-05 ALL-DAY Jackpot — Castle Rock :: animals :: location="Castle Rock, CO" :: flag=true :: notes="🚩 F-01 swim meet conflict — logistics unresolved"
[CAL] 2026-06-08 16:30 [D] Fairboard meeting :: misc
[CAL] 2026-06-09 18:00 [D] Knights of Columbus :: misc
[CAL] 2026-06-13 ALL-DAY Jackpot — New Raymor CO :: animals :: location="New Raymor, CO"
[CAL] 2026-06-15 10:00 [M][R] Art camp :: kids :: span=2026-06-19 :: location="Westcliffe, CO"
[CAL] 2026-06-16 12:00 [W] Dentist — Canyon Family Dental :: appointments :: stripe=appt :: location="Canyon Family Dental, Cañon City, CO"
[CAL] 2026-06-20 08:00 Livestock clinic — Florence CO :: misc :: location="Florence, CO"
[CAL] 2026-06-20 ALL-DAY Jackpot — Jefferson County Fairgrounds :: animals :: location="Golden, CO"
[CAL] 2026-06-25 13:30 [W] Ortho — Pueblo :: appointments :: stripe=appt :: location="Pueblo, CO"
[CAL] 2026-06-26 ALL-DAY [W][M][R] Swim meet — Rocky Ford :: kids :: location="Rocky Ford, CO" :: flag=true :: notes="🚩 F-02 jackpot same window — logistics unresolved"
[CAL] 2026-06-27 ALL-DAY Jackpot — Monte Vista or Lamar TBD :: animals :: flag=true :: notes="🚩 F-02 Rocky Ford swim meet conflict Jun 26-28"

---

### JULY 2026

[CAL] 2026-07-01 ALL-DAY trash-day
[CAL] 2026-07-08 10:20 [K] Dentist — Canyon Family Dental :: appointments :: stripe=appt :: location="Canyon Family Dental, Cañon City, CO"
[CAL] 2026-07-09 ALL-DAY [W][M][D] Custer County Fair :: kids :: span=2026-07-19 :: location="Westcliffe, CO"
[CAL] 2026-07-13 16:30 [D] Fairboard meeting :: misc
[CAL] 2026-07-14 18:00 [D] Knights of Columbus :: misc
[CAL] 2026-07-14 ALL-DAY [W][M] Weigh-ins + picnic :: kids :: location="Westcliffe, CO" :: flag=true :: notes="🚩 PQ-16 GUEST pill Adam+Bethany Louche Tue-Fri pending"
[CAL] 2026-07-15 ALL-DAY [W][M][D] Swine show + pork meal :: kids :: location="Westcliffe, CO"
[CAL] 2026-07-16 09:00 [M] Sheep show :: kids :: location="Westcliffe, CO"
[CAL] 2026-07-17 ALL-DAY [M] Master showmanship — sheep :: kids :: location="Westcliffe, CO"
[CAL] 2026-07-18 ALL-DAY [D][W][M] Buckle ceremony + livestock sale :: kids :: location="Westcliffe, CO"
[CAL] 2026-07-19 ALL-DAY Fair cleanup :: misc :: location="Westcliffe, CO"

---

## Notes for Foreman

- **Phase 1 = no Google Calendar writes. No whiteboard writes.** Propose, don't push.
- **Whiteboard is the family's ground truth.** This file is a parallel ledger they choose to consult.
- **One source of truth per fact.** Don't restate `family.md` or `prefs.md` here. Reference.
- **Reminder voice belongs to domain agents (Option C).** You hold the date; the named agent in brackets speaks when the prompt fires.
- **It always makes the calendar.** Unresolved = flag=true. Nothing stays off pending resolution.
- **When in doubt, ask Tim.** Life with 6 kids changes — don't guess at this year's schedule from last year's.
