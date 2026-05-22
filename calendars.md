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
- Swim practice in season — 09:30-11:30 Florence Pool.
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
- **Kids dentist** — quarterly, often bulk-booked. Matt = Salida Family Dental. Everyone else = Canyon Family Dental, Cañon City.
- **K. apt** — weekly Mon (above).

---

## School Day Doctrine
All school-day events (field trips, school activities, etc.) = 08:00–15:00 for all children, unless a specific time is stated otherwise.

---

## Sports Location Doctrine
For travel sports (swim meets, track meets, cross country meets, and similar away competitions), the location renders on the calendar tile. Explicit exception to the location-in-detail-only rule — every meet is a different venue and the location is essential at-a-glance information.

---

## Prompt Entry Doctrine
Reminders and milestone triggers use `:: prompt` category + ⏰ at end of title. These are not appointments — no `stripe=appt`, no location unless confirmed. Pattern: `[PILL] Title ⏰ :: prompt`

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
- **2026-06-15** — Kalea CAC renewal prompt. CAC expires 2026-07-31. Schedule DEERS appt.
- **2026-08-01** — Jackson trailer registration renewal prompt (60 days before Oct expiration).
- **Spring 2027** — Gehl skid steer oil change.
- **2027-02-27** — Kalea CO DL renewal prompt (90 days before 2027-05-27 expiration).
- **2028-09-07** — Matt CO DL renewal prompt (90 days before 2028-12-07 expiration).

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

[CAL-RECUR weekly start=2026-05-03 day=sun] 08:00 Mass — Eggs for Fr. Joe :: liturgical :: location="St. Joseph's, Salida"
[CAL-RECUR weekly start=2026-05-06 day=wed] 10:00 [D][K] Daily Mass :: liturgical :: location="Our Lady of Assumption, Westcliffe"

---

### RECURRING — Swim Practice (Canon City Pirates — Summer Season)
<!-- Regular: Mon+Wed 17:30-19:30, Tue+Thu 09:30-11:30. Florence Pool. Kalea drives+coaches. -->
[CAL-RECUR weekly start=2026-06-01 day=mon] 17:30 [K][W][M][R][C][E] Swim practice :: kids :: location="Florence Pool, Florence, CO"
[CAL-RECUR weekly start=2026-06-01 day=wed] 17:30 [K][W][M][R][C][E] Swim practice :: kids :: location="Florence Pool, Florence, CO"
[CAL-RECUR weekly start=2026-06-01 day=tue] 09:30 [K][W][M][R][C][E] Swim practice :: kids :: location="Florence Pool, Florence, CO"
[CAL-RECUR weekly start=2026-06-01 day=thu] 09:30 [K][W][M][R][C][E] Swim practice :: kids :: location="Florence Pool, Florence, CO"

---

### RECURRING — Monthly
[CAL-RECUR monthly start=2026-06-09 day=tue week=2] 18:00 [D] Knights of Columbus :: misc
[CAL-RECUR monthly start=2026-06-08 day=mon week=2] 16:30 [D] Fairboard meeting :: misc

---

### FAITH FORMATION — School Year 2026-27
<!-- School year Aug–May. Start date TBD. Sequential with Mass — not a conflict. PQ-20 logged. -->
[CAL-RECUR weekly start=2026-08-01 day=sun] 09:00 [M][R][C][E] Faith Formation :: kids :: flag=true :: notes="🚩 Fall start date unconfirmed — verify with parish"

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
[CAL] 2026-11-26 10:00 Thanksgiving Mass :: liturgical :: location="St. Joseph's, Salida"
[CAL] 2026-12-25 ALL-DAY Christmas :: liturgical
[CAL] 2027-01-06 ALL-DAY Epiphany / Three Kings :: liturgical

---

### MILESTONES — Punch List / Wyatt / Mantel

[CAL] 2026-06-15 ALL-DAY [K] CAC renewal reminder ⏰ :: prompt
[CAL] 2026-08-01 ALL-DAY Wyatt driver-ed research ⏰ :: prompt
[CAL] 2026-08-01 ALL-DAY Jackson trailer registration ⏰ :: prompt
[CAL] 2026-09-15 ALL-DAY Enroll Wyatt in driver ed ⏰ :: prompt
[CAL] 2026-11-08 ALL-DAY [D][K] Wedding anniversary :: misc
[CAL] 2026-12-15 ALL-DAY Wyatt driver ed cert check ⏰ :: prompt
[CAL] 2027-01-01 ALL-DAY Wyatt DMV permit appt ⏰ :: prompt
[CAL] 2027-02-27 ALL-DAY [K] CO DL renewal reminder ⏰ :: prompt
[CAL] 2027-04-22 ALL-DAY Wyatt permit checkpoint — 3 mo ⏰ :: prompt
[CAL] 2027-07-22 ALL-DAY Wyatt permit checkpoint — 6 mo ⏰ :: prompt
[CAL] 2027-10-22 ALL-DAY Wyatt permit checkpoint — 9 mo ⏰ :: prompt
[CAL] 2028-01-01 ALL-DAY Wyatt CO road test ⏰ :: prompt
[CAL] 2028-09-07 ALL-DAY [D] CO DL renewal reminder ⏰ :: prompt
[CAL] 2029-01-01 ALL-DAY Wyatt restricted phase ending check ⏰ :: prompt

---

### TRASH PICKUP — Jul 2026 → Jan 2027 (every 4 weeks from Jul 1)

[CAL] 2026-07-01 ALL-DAY trash-day :: misc
[CAL] 2026-07-29 ALL-DAY trash-day :: misc
[CAL] 2026-08-26 ALL-DAY trash-day :: misc
[CAL] 2026-09-23 ALL-DAY trash-day :: misc
[CAL] 2026-10-21 ALL-DAY trash-day :: misc
[CAL] 2026-11-18 ALL-DAY trash-day :: misc
[CAL] 2026-12-16 ALL-DAY trash-day :: misc
[CAL] 2027-01-13 ALL-DAY trash-day :: misc

---

### MAY 2026

[CAL] 2026-05-06 ALL-DAY trash-day :: misc
[CAL] 2026-05-05 10:00 [K][D] Prenatal apt — Pueblo :: appointments :: stripe=appt :: location="Pueblo, CO"
[CAL] 2026-05-14 08:00 [W] Field trip — Sky Zone :: kids :: location="Colorado Springs, CO"
[CAL] 2026-05-14 ALL-DAY [M][R][C][E] PJ Day :: kids
[CAL] 2026-05-16 11:00 [R] Haircut :: kids
[CAL] 2026-05-16 11:00 [W] Art :: kids
[CAL] 2026-05-16 17:00 Mass :: liturgical :: location="St. Joseph's, Salida"
[CAL] 2026-05-18 10:00 [K] Apt — Gina :: appointments :: stripe=appt
[CAL] 2026-05-19 08:00 [M][R] Triathlon — Westcliffe :: kids :: location="Westcliffe, CO"
[CAL] 2026-05-22 ALL-DAY [D] Pick up wood shavings — Ryan Stover :: misc :: notes="In town"
[CAL] 2026-05-23 11:00 [R][M] Apt — Tacey :: appointments :: stripe=appt
[CAL] 2026-05-28 ALL-DAY [W][M][D] Jackpot — Brighton :: animals :: location="Brighton, CO" :: flag=true :: notes="🚩 F-01 swim meet conflict — logistics unresolved"

---

### JUNE 2026

[CAL] 2026-06-01 ALL-DAY [W] Sweden trip :: kids :: span=2026-06-13 :: travel=true :: flag=true :: notes="🚩 F-05 drop-off pickup chaperone logistics unresolved"
[CAL] 2026-06-03 ALL-DAY [D][K] NV drop — Austin Auto :: misc :: location="Austin Automotive" :: notes="Kalea drives Tahoe, Matt drives NV. Pickup day = Tahoe drop day TBD"
[CAL] 2026-06-04 13:40 [K][D] Prenatal apt :: appointments :: stripe=appt
[CAL] 2026-06-05 ALL-DAY [FAM] Swim meet — Las Animas :: kids :: location="Las Animas, CO" :: span=2026-06-07 :: flag=true :: notes="🚩 F-01 Castle Rock jackpot same day — logistics unresolved"
[CAL] 2026-06-05 ALL-DAY Jackpot — Castle Rock :: animals :: location="Castle Rock, CO" :: flag=true :: notes="🚩 F-01 swim meet conflict — logistics unresolved"
[CAL] 2026-06-12 ALL-DAY [FAM] Swim meet — Lamar :: kids :: location="Lamar, CO" :: span=2026-06-14
[CAL] 2026-06-15 10:00 [M][R] Art camp :: kids :: span=2026-06-19 :: location="Westcliffe, CO"
[CAL] 2026-06-16 12:00 [W] Dentist :: appointments :: stripe=appt :: location="Canyon Family Dental, Cañon City, CO"
[CAL] 2026-06-19 ALL-DAY [FAM] Swim meet — Pueblo County :: kids :: location="Pueblo, CO" :: span=2026-06-21
[CAL] 2026-06-20 08:00 Livestock clinic — Florence :: misc :: location="Florence, CO"
[CAL] 2026-06-20 ALL-DAY Jackpot — Jefferson County Fairgrounds :: animals :: location="Golden, CO"
[CAL] 2026-06-25 13:30 [W] Ortho — Pueblo :: appointments :: stripe=appt :: location="Pueblo, CO"
[CAL] 2026-06-26 ALL-DAY [FAM] Swim meet — Rocky Ford :: kids :: location="Rocky Ford, CO" :: span=2026-06-28 :: flag=true :: notes="🚩 F-02 jackpot same window — logistics unresolved"
[CAL] 2026-06-27 ALL-DAY Jackpot — Monte Vista or Lamar TBD :: animals :: flag=true :: notes="🚩 F-02 Rocky Ford swim meet conflict Jun 26-28"

---

### JULY 2026

[CAL] 2026-07-08 10:20 [K] Dentist :: appointments :: stripe=appt :: location="Canyon Family Dental, Cañon City, CO"
[CAL] 2026-07-09 16:00 Fair cleanup :: misc :: location="Westcliffe, CO"
[CAL] 2026-07-11 ALL-DAY [FAM] Swim meet — Piranhas home meet :: kids :: location="Pueblo, CO"
[CAL] 2026-07-14 ALL-DAY [GUEST] Louche visit — Adam+Bethany :: misc :: span=2026-07-17
[CAL] 2026-07-14 15:00 [W][M] Weigh-ins + picnic :: kids :: location="Westcliffe, CO"
[CAL] 2026-07-15 17:00 [W][M][D] Swine show + pork meal :: kids :: location="Westcliffe, CO"
[CAL] 2026-07-16 09:00 [M] Sheep show :: kids :: location="Westcliffe, CO"
[CAL] 2026-07-17 12:00 [M] Master showmanship — sheep :: kids :: location="Westcliffe, CO"
[CAL] 2026-07-17 ALL-DAY [FAM] Swim meet — Salida :: kids :: location="Salida, CO" :: span=2026-07-19
[CAL] 2026-07-18 12:00 [D][W][M] Buckle ceremony + livestock sale :: kids :: location="Westcliffe, CO"
[CAL] 2026-07-19 12:00 Fair cleanup :: misc :: location="Westcliffe, CO"
[CAL] 2026-07-24 ALL-DAY [FAM] Swim meet — SECAL Championship :: kids :: location="Las Animas, CO" :: span=2026-07-26
[CAL] 2026-07-31 ALL-DAY [FAM] Swim meet — State Championship :: kids :: location="Alamosa, CO" :: span=2026-08-02

---

## Notes for Foreman

- **Phase 1 = no Google Calendar writes. No whiteboard writes.** Propose, don't push.
- **Whiteboard is the family's ground truth.** This file is a parallel ledger they choose to consult.
- **One source of truth per fact.** Don't restate `family.md` or `prefs.md` here. Reference.
- **Reminder voice belongs to domain agents (Option C).** You hold the date; the named agent in brackets speaks when the prompt fires.
- **It always makes the calendar.** Unresolved = flag=true. Nothing stays off pending resolution.
- **Travel spans:** `travel=true` on any span where a person is physically away from home. Foreman asks "Are they traveling?" on all multi-day absence entries.
- **When in doubt, ask Tim.** Life with 6 kids changes — don't guess at this year's schedule from last year's.

---

### BIRTHDAYS — Immediate Family

[CAL] 2026-01-22 ALL-DAY Wyatt birthday :: birthdays
[CAL] 2026-04-19 ALL-DAY Molly birthday :: birthdays
[CAL] 2026-05-27 ALL-DAY Kalea birthday :: birthdays
[CAL] 2026-06-28 ALL-DAY Rileigh birthday :: birthdays
[CAL] 2026-09-04 ALL-DAY Cullen + Emmitt birthday :: birthdays
[CAL] 2026-12-07 ALL-DAY Matt birthday :: birthdays
[CAL] 2027-01-22 ALL-DAY Wyatt birthday :: birthdays
[CAL] 2027-04-19 ALL-DAY Molly birthday :: birthdays
[CAL] 2027-05-27 ALL-DAY Kalea birthday :: birthdays
[CAL] 2027-06-28 ALL-DAY Rileigh birthday :: birthdays
[CAL] 2027-09-04 ALL-DAY Cullen + Emmitt birthday :: birthdays
[CAL] 2027-12-07 ALL-DAY Matt birthday :: birthdays

---

### FEDERAL HOLIDAYS + OBSERVANCES — 2026

[CAL] 2026-01-01 ALL-DAY New Year's Day :: holidays
[CAL] 2026-01-19 ALL-DAY MLK Day :: holidays
[CAL] 2026-02-16 ALL-DAY Presidents Day :: holidays
[CAL] 2026-05-10 ALL-DAY Mother's Day :: holidays
[CAL] 2026-05-25 ALL-DAY Memorial Day :: holidays
[CAL] 2026-06-21 ALL-DAY Father's Day :: holidays
[CAL] 2026-07-04 ALL-DAY Independence Day :: holidays
[CAL] 2026-09-07 ALL-DAY Labor Day :: holidays
[CAL] 2026-10-12 ALL-DAY Columbus Day :: holidays
[CAL] 2026-11-11 ALL-DAY Veterans Day :: holidays
[CAL] 2026-11-26 ALL-DAY Thanksgiving :: holidays
[CAL] 2026-12-25 ALL-DAY Christmas :: holidays

---

### FEDERAL HOLIDAYS + OBSERVANCES — 2027

[CAL] 2027-01-01 ALL-DAY New Year's Day :: holidays
[CAL] 2027-01-18 ALL-DAY MLK Day :: holidays
[CAL] 2027-02-15 ALL-DAY Presidents Day :: holidays
[CAL] 2027-05-09 ALL-DAY Mother's Day :: holidays
[CAL] 2027-05-31 ALL-DAY Memorial Day :: holidays
[CAL] 2027-06-20 ALL-DAY Father's Day :: holidays
[CAL] 2027-07-04 ALL-DAY Independence Day :: holidays
[CAL] 2027-09-06 ALL-DAY Labor Day :: holidays
[CAL] 2027-10-11 ALL-DAY Columbus Day :: holidays
[CAL] 2027-11-11 ALL-DAY Veterans Day :: holidays
[CAL] 2027-11-25 ALL-DAY Thanksgiving :: holidays
[CAL] 2027-12-25 ALL-DAY Christmas :: holidays

---

### AUG 1 PING STACK — additions

[CAL] 2026-08-01 ALL-DAY Kalea teaching block — confirm fall schedule ⏰ :: prompt
[CAL] 2026-08-01 ALL-DAY Youth Group fall schedule — confirm ⏰ :: prompt
[CAL] 2026-08-01 ALL-DAY Faith Formation fall start — confirm with parish ⏰ :: prompt

---

### LITURGICAL — Curated Feasts 2026
<!-- Filter: Holy Days of Obligation + feasts with food tradition or significant family observance. -->
<!-- Full auto-render of all saint days = PQ-22 widget build. -->

[CAL] 2026-01-01 ALL-DAY Mary, Mother of God :: liturgical
[CAL] 2026-01-06 ALL-DAY Epiphany — king cake :: liturgical
[CAL] 2026-02-02 ALL-DAY Candlemas — crêpes :: liturgical
[CAL] 2026-02-03 ALL-DAY St. Blaise — throat blessing :: liturgical
[CAL] 2026-02-11 ALL-DAY Our Lady of Lourdes :: liturgical
[CAL] 2026-02-14 ALL-DAY St. Valentine :: liturgical
[CAL] 2026-03-17 ALL-DAY St. Patrick — corned beef :: liturgical
[CAL] 2026-03-19 ALL-DAY St. Joseph — zeppole :: liturgical
[CAL] 2026-03-25 ALL-DAY Annunciation :: liturgical
[CAL] 2026-04-23 ALL-DAY St. George :: liturgical
[CAL] 2026-05-01 ALL-DAY St. Joseph the Worker :: liturgical
[CAL] 2026-05-13 ALL-DAY Our Lady of Fatima :: liturgical
[CAL] 2026-05-15 ALL-DAY St. Isidore — patron of Edelweiss :: liturgical
[CAL] 2026-05-31 ALL-DAY Visitation :: liturgical
[CAL] 2026-06-13 ALL-DAY St. Anthony — bread of St. Anthony :: liturgical
[CAL] 2026-06-24 ALL-DAY Birth of St. John the Baptist — bonfire :: liturgical
[CAL] 2026-06-29 ALL-DAY Sts. Peter and Paul — fish :: liturgical
[CAL] 2026-07-16 ALL-DAY Our Lady of Mount Carmel :: liturgical
[CAL] 2026-07-22 ALL-DAY St. Mary Magdalene :: liturgical
[CAL] 2026-07-26 ALL-DAY Sts. Joachim and Anne :: liturgical
[CAL] 2026-08-06 ALL-DAY Transfiguration — first fruits :: liturgical
[CAL] 2026-08-15 ALL-DAY Assumption of Mary — Holy Day of Obligation :: liturgical
[CAL] 2026-08-22 ALL-DAY Queenship of Mary :: liturgical
[CAL] 2026-09-08 ALL-DAY Birth of Mary :: liturgical
[CAL] 2026-09-14 ALL-DAY Exaltation of the Holy Cross :: liturgical
[CAL] 2026-09-29 ALL-DAY Sts. Michael, Gabriel, Raphael :: liturgical
[CAL] 2026-10-01 ALL-DAY St. Thérèse of Lisieux :: liturgical
[CAL] 2026-10-02 ALL-DAY Guardian Angels :: liturgical
[CAL] 2026-10-04 ALL-DAY St. Francis — animal blessing :: liturgical
[CAL] 2026-10-07 ALL-DAY Our Lady of the Rosary :: liturgical
[CAL] 2026-10-28 ALL-DAY Sts. Simon and Jude :: liturgical
[CAL] 2026-10-31 ALL-DAY All Hallows Eve :: liturgical
[CAL] 2026-11-01 ALL-DAY All Saints Day — Holy Day of Obligation :: liturgical
[CAL] 2026-11-02 ALL-DAY All Souls Day — pan de muerto :: liturgical
[CAL] 2026-11-11 ALL-DAY St. Martin of Tours — goose :: liturgical
[CAL] 2026-11-22 ALL-DAY St. Cecilia :: liturgical
[CAL] 2026-11-25 ALL-DAY St. Catherine of Alexandria :: liturgical
[CAL] 2026-12-06 ALL-DAY St. Nicholas — treats :: liturgical
[CAL] 2026-12-08 ALL-DAY Immaculate Conception — Holy Day of Obligation :: liturgical
[CAL] 2026-12-12 ALL-DAY Our Lady of Guadalupe — tamales :: liturgical
[CAL] 2026-12-13 ALL-DAY St. Lucy — saffron buns :: liturgical
[CAL] 2026-12-26 ALL-DAY St. Stephen :: liturgical
[CAL] 2026-12-27 ALL-DAY St. John the Apostle :: liturgical
[CAL] 2026-12-28 ALL-DAY Holy Innocents :: liturgical

---

### LITURGICAL — Curated Feasts 2027

[CAL] 2027-01-01 ALL-DAY Mary, Mother of God :: liturgical
[CAL] 2027-01-06 ALL-DAY Epiphany — king cake :: liturgical
[CAL] 2027-02-02 ALL-DAY Candlemas — crêpes :: liturgical
[CAL] 2027-02-03 ALL-DAY St. Blaise — throat blessing :: liturgical
[CAL] 2027-02-11 ALL-DAY Our Lady of Lourdes :: liturgical
[CAL] 2027-02-14 ALL-DAY St. Valentine :: liturgical
[CAL] 2027-03-17 ALL-DAY St. Patrick — corned beef :: liturgical
[CAL] 2027-03-19 ALL-DAY St. Joseph — zeppole :: liturgical
[CAL] 2027-03-25 ALL-DAY Annunciation :: liturgical
[CAL] 2027-04-23 ALL-DAY St. George :: liturgical
[CAL] 2027-05-01 ALL-DAY St. Joseph the Worker :: liturgical
[CAL] 2027-05-13 ALL-DAY Our Lady of Fatima :: liturgical
[CAL] 2027-05-15 ALL-DAY St. Isidore — patron of Edelweiss :: liturgical
[CAL] 2027-05-31 ALL-DAY Visitation :: liturgical
[CAL] 2027-06-13 ALL-DAY St. Anthony — bread of St. Anthony :: liturgical
[CAL] 2027-06-24 ALL-DAY Birth of St. John the Baptist — bonfire :: liturgical
[CAL] 2027-06-29 ALL-DAY Sts. Peter and Paul — fish :: liturgical
[CAL] 2027-07-16 ALL-DAY Our Lady of Mount Carmel :: liturgical
[CAL] 2027-07-22 ALL-DAY St. Mary Magdalene :: liturgical
[CAL] 2027-07-26 ALL-DAY Sts. Joachim and Anne :: liturgical
[CAL] 2027-08-06 ALL-DAY Transfiguration — first fruits :: liturgical
[CAL] 2027-08-15 ALL-DAY Assumption of Mary — Holy Day of Obligation :: liturgical
[CAL] 2027-08-22 ALL-DAY Queenship of Mary :: liturgical
[CAL] 2027-09-08 ALL-DAY Birth of Mary :: liturgical
[CAL] 2027-09-14 ALL-DAY Exaltation of the Holy Cross :: liturgical
[CAL] 2027-09-29 ALL-DAY Sts. Michael, Gabriel, Raphael :: liturgical
[CAL] 2027-10-01 ALL-DAY St. Thérèse of Lisieux :: liturgical
[CAL] 2027-10-02 ALL-DAY Guardian Angels :: liturgical
[CAL] 2027-10-04 ALL-DAY St. Francis — animal blessing :: liturgical
[CAL] 2027-10-07 ALL-DAY Our Lady of the Rosary :: liturgical
[CAL] 2027-10-28 ALL-DAY Sts. Simon and Jude :: liturgical
[CAL] 2027-10-31 ALL-DAY All Hallows Eve :: liturgical
[CAL] 2027-11-01 ALL-DAY All Saints Day — Holy Day of Obligation :: liturgical
[CAL] 2027-11-02 ALL-DAY All Souls Day — pan de muerto :: liturgical
[CAL] 2027-11-11 ALL-DAY St. Martin of Tours — goose :: liturgical
[CAL] 2027-11-22 ALL-DAY St. Cecilia :: liturgical
[CAL] 2027-11-25 ALL-DAY St. Catherine of Alexandria :: liturgical
[CAL] 2027-12-06 ALL-DAY St. Nicholas — treats :: liturgical
[CAL] 2027-12-08 ALL-DAY Immaculate Conception — Holy Day of Obligation :: liturgical
[CAL] 2027-12-12 ALL-DAY Our Lady of Guadalupe — tamales :: liturgical
[CAL] 2027-12-13 ALL-DAY St. Lucy — saffron buns :: liturgical
[CAL] 2027-12-26 ALL-DAY St. Stephen :: liturgical
[CAL] 2027-12-27 ALL-DAY St. John the Apostle :: liturgical
[CAL] 2027-12-28 ALL-DAY Holy Innocents :: liturgical