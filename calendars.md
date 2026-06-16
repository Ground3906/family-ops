# calendars.md — Bayer Family Calendar State (v0)

**Owner:** Foreman
**Schema version:** 1
**Last full rewrite:** 2026-06-01
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
- **17:30-19:00 - Family meal.** HARD. No exceptions without Tim's chat-session override.

### Weekly
- **Sundays - all day.** HARD. Mass 0800. Faith Formation 0900-1015 (school year). Family/rest. No work, no study, no non-essential appointments.

### Annual / Liturgical
- **Lent (Ash Wed to Easter Vigil):**
  - Ash Wednesday - Mass attendance.
  - Fridays - Stations of the Cross. Fish dinner (no meat).
  - Holy Thursday - evening Mass, kids serving.
  - Good Friday - 1200 Stations + 1500 Service. No meat.
  - Holy Saturday - Easter Vigil ~1745.
- **Easter Sunday + Octave.**
- **Confirmation cycle** - 1845-2000 evening sessions; clusters Feb-Apr.
- **Other Holy Days of Obligation** - capture as they come.
- **Christmas / Epiphany Jan 6.**
- **Thanksgiving** - 1000 Mass.

### Family Sacred Dates
- **November 8 - wedding anniversary** (Matt + Kalea, eloped Nov 2013).
- **April 25 - Loretto Chapel day.** Mantel-owned sacred memory. Foreman marks but never schedules over.

### Hunting Blackouts - Matt-only scope
See `mystery-ranch/blackouts.md` - read at session start. Mystery Ranch writes; Foreman protects. **Freezes Matt's calendar only**; Kalea, kids, household continue normally. Re-route drivers per `family.md` backup-adult tier.

### Kalea Drill Travel - Kalea-only scope
Per `prefs.md`. Freezes Kalea's calendar only; household continues normally with routing falling to Matt or backup-adult tier (default Tier 1: Oma & Papa).

### Kalea Canning - Sacred blocks (Kalea-only scope)
Two sessions/year: (1) peaches ~Labor Day, (2) apples/jalapenos/etc ~October. 3 days each. Foreman blocks territory; Chow Hall handles meals + inventory during session.

---

## Weekly Recurring Shape (Academic Year - Aug-May)

Confirm exact times each season; this is the shape, not the truth.

### Monday
- K. apt - weekly, ~1400 or 1515. Location varies; often Salida.
- Pig feed (Punch List).

### Tuesday
- M. Knights of Columbus - monthly, ~2nd Tue 1800.
- Algebra teaching (Tim) - PM during school year. Confirm season.
- Pig feed.

### Wednesday
- Salida runs - common, 1130-1530 window. Disambiguate per event.
- **Winter:** Wrestling 1430-1630 Salida.
- **Spring:** W. Track 1545-1700.
- Pig feed.

### Thursday
- Youth Group 1830-2000 (older kids) - seasonal, not year-round. Confirm window each year.
- Swim practice in season - 09:30-11:30 Florence Pool.
- Some weeks K. apt 1400.
- Lenten Mass 1800 some Thursdays.

### Friday
- Pig feed.
- Chicken feed (Fri or Sat) - 3 bags.
- Stations of the Cross during Lent.

### Saturday
- 4H meetings monthly (~1300-1400).
- Sports: X-country (fall), basketball (winter), track (spring). Bus depart often 0600 / 0645 for away games.
- Pig feed.

### Sunday - SACRED, NO SCHEDULING
- 0800 Mass - St. Joseph's Salida.
- 0900-1015 Faith Formation (school year only - Aug-May).
- Kids serving rotations (W-Serve, M-Serve, Molly-Serve).
- Matt-EM on rotation.

---

## Recurring Medical

- **W. orthodontist** - ~6 week intervals, often Pueblo, often 0830.
- **Kids dentist** - quarterly, often bulk-booked. Matt = Salida Family Dental. Everyone else = Cañon Family Dental, Cañon City.
- **K. apt** - weekly Mon (above).

---

## Notes for Foreman

- **Phase 1 = no Google Calendar writes. No whiteboard writes.** Propose, don't push.
- **Whiteboard is the family's ground truth.** This file is a parallel ledger they choose to consult.
- **One source of truth per fact.** Don't restate `family.md` or `prefs.md` here. Reference.
- **Reminder voice belongs to domain agents (Option C).** You hold the date; the named agent in brackets speaks when the prompt fires.
- **It always makes the calendar.** Unresolved = flag=true. Nothing stays off pending resolution.
- **Travel spans:** `travel=true` on any span where a person is physically away from home. Foreman asks "Are they traveling?" on all multi-day absence entries.
- **No em-dashes in any calendar entry title or notes field. Hyphen (-) only.**
- **Swim meets = ALL-DAY always.** Never assign a time to a swim meet entry.
- **cancel=pending:** Event displays with strikethrough title and ⊘ symbol. Awaiting Matt or Kalea confirmation. Both have equal authority to propose or confirm.
- **cancel=confirmed:** Parser skips the entry entirely. Line stays in this file permanently as audit trail. Never delete a confirmed-cancel line.
- **When in doubt, ask Tim.** Life with 6 kids changes - don't guess at this year's schedule from last year's.

---

## Travel / Extended Absences

Whiteboard regularly marks `Mom Leaves`, `Mom Returns`, `K Hawaii`, `M+K gone`, etc. Capture confirmed travel here as soft blocks; surface conflicts at session start. Kalea USMC drill travel is a sub-category - Kalea-only scope sacred block.

*(Populated as confirmed.)*

---

## Upcoming Events

Foreman appends here only after Tim/Jill confirm proposals. Phase 1: copy to whiteboard after committing.
**Doctrine: It always makes the calendar. Unresolved items get flag=true. Nothing stays off pending resolution.**
Last batch: 2026-06-01. All entries widget-readable [CAL] / [CAL-RECUR] format.

---

### RECURRING - Weekly

[CAL-RECUR weekly start=2026-05-03 day=sun skip=2026-06-07] 08:00 Mass - Eggs for Fr. Joe :: liturgical :: end=09:00 :: location="St. Joseph's, Salida"
[CAL-RECUR weekly start=2026-05-06 day=wed] 10:00 Daily Mass :: liturgical :: optional=true :: end=11:00 :: location="Our Lady of Assumption, Westcliffe"

---

### SWIM PRACTICE - Cañon City Pirates Summer Season 2026
<!-- Mon+Wed 17:30-19:30. Tue+Thu 09:30-12:00. Florence Pool. Kalea drives+coaches. -->
<!-- Exceptions: Jun 16+18 M+R at art camp. Jul 15 W+M at fair (swine show). Jul 16 M at fair (sheep show). -->
[CAL] 2026-06-01 17:30 [W][M][R][C][E] Swim practice :: kids :: end=19:30 :: location="Florence Pool, Florence, CO"
[CAL] 2026-06-02 09:30 [W][M][R][C][E] Swim practice :: kids :: end=12:00 :: location="Florence Pool, Florence, CO"
[CAL] 2026-06-03 17:30 [W][M][R][C][E] Swim practice :: kids :: end=19:30 :: location="Florence Pool, Florence, CO"
[CAL] 2026-06-04 09:30 [W][M][R][C][E] Swim practice :: kids :: end=12:00 :: location="Florence Pool, Florence, CO"
[CAL] 2026-06-08 17:30 [W][M][R][C][E] Swim practice :: kids :: end=19:30 :: location="Florence Pool, Florence, CO"
[CAL] 2026-06-09 09:30 [W][M][R][C][E] Swim practice :: kids :: end=12:00 :: location="Florence Pool, Florence, CO"
[CAL] 2026-06-10 17:30 [W][M][R][C][E] Swim practice :: kids :: end=19:30 :: location="Florence Pool, Florence, CO"
[CAL] 2026-06-11 09:30 [W][M][R][C][E] Swim practice :: kids :: end=12:00 :: location="Florence Pool, Florence, CO"
[CAL] 2026-06-15 17:30 [W][M][R][C][E] Swim practice :: kids :: end=19:30 :: location="Florence Pool, Florence, CO"
[CAL] 2026-06-16 09:30 [W][C][E] Swim practice :: kids :: end=12:00 :: location="Florence Pool, Florence, CO"
[CAL] 2026-06-17 17:30 [W][M][R][C][E] Swim practice :: kids :: end=19:30 :: location="Florence Pool, Florence, CO"
[CAL] 2026-06-18 09:30 [W][C][E] Swim practice :: kids :: end=12:00 :: location="Florence Pool, Florence, CO"
[CAL] 2026-06-22 17:30 [W][M][R][C][E] Swim practice :: kids :: end=19:30 :: location="Florence Pool, Florence, CO"
[CAL] 2026-06-23 09:30 [W][M][R][C][E] Swim practice :: kids :: end=12:00 :: location="Florence Pool, Florence, CO"
[CAL] 2026-06-24 17:30 [W][M][R][C][E] Swim practice :: kids :: end=19:30 :: location="Florence Pool, Florence, CO"
[CAL] 2026-06-25 09:30 [W][M][R][C][E] Swim practice :: kids :: end=12:00 :: location="Florence Pool, Florence, CO"
[CAL] 2026-06-29 17:30 [W][M][R][C][E] Swim practice :: kids :: end=19:30 :: location="Florence Pool, Florence, CO" :: cancel=pending
[CAL] 2026-06-30 09:30 [W][M][R][C][E] Swim practice :: kids :: end=12:00 :: location="Florence Pool, Florence, CO" :: cancel=pending
[CAL] 2026-07-01 17:30 [W][M][R][C][E] Swim practice :: kids :: end=19:30 :: location="Florence Pool, Florence, CO" :: cancel=pending
[CAL] 2026-07-02 09:30 [W][M][R][C][E] Swim practice :: kids :: end=12:00 :: location="Florence Pool, Florence, CO" :: cancel=pending
[CAL] 2026-07-06 17:30 [W][M][R][C][E] Swim practice :: kids :: end=19:30 :: location="Florence Pool, Florence, CO"
[CAL] 2026-07-07 09:30 [W][M][R][C][E] Swim practice :: kids :: end=12:00 :: location="Florence Pool, Florence, CO"
[CAL] 2026-07-08 17:30 [W][M][R][C][E] Swim practice :: kids :: end=19:30 :: location="Florence Pool, Florence, CO"
[CAL] 2026-07-09 09:30 [W][M][R][C][E] Swim practice :: kids :: end=12:00 :: location="Florence Pool, Florence, CO"
[CAL] 2026-07-13 17:30 [W][M][R][C][E] Swim practice :: kids :: end=19:30 :: location="Florence Pool, Florence, CO"
[CAL] 2026-07-14 09:30 [W][M][R][C][E] Swim practice :: kids :: end=12:00 :: location="Florence Pool, Florence, CO"
[CAL] 2026-07-15 17:30 [R][C][E] Swim practice :: kids :: end=19:30 :: location="Florence Pool, Florence, CO"
[CAL] 2026-07-16 09:30 [W][R][C][E] Swim practice :: kids :: end=12:00 :: location="Florence Pool, Florence, CO"
[CAL] 2026-07-20 17:30 [W][M][R][C][E] Swim practice :: kids :: end=19:30 :: location="Florence Pool, Florence, CO"
[CAL] 2026-07-21 09:30 [W][M][R][C][E] Swim practice :: kids :: end=12:00 :: location="Florence Pool, Florence, CO"
[CAL] 2026-07-22 17:30 [W][M][R][C][E] Swim practice :: kids :: end=19:30 :: location="Florence Pool, Florence, CO"
[CAL] 2026-07-23 09:30 [W][M][R][C][E] Swim practice :: kids :: end=12:00 :: location="Florence Pool, Florence, CO"
[CAL] 2026-07-27 17:30 [W][M][R][C][E] Swim practice :: kids :: end=19:30 :: location="Florence Pool, Florence, CO"
[CAL] 2026-07-28 09:30 [W][M][R][C][E] Swim practice :: kids :: end=12:00 :: location="Florence Pool, Florence, CO"
[CAL] 2026-07-29 17:30 [W][M][R][C][E] Swim practice :: kids :: end=19:30 :: location="Florence Pool, Florence, CO"
[CAL] 2026-07-30 09:30 [W][M][R][C][E] Swim practice :: kids :: end=12:00 :: location="Florence Pool, Florence, CO"

---

### KNIGHTS OF COLUMBUS - 2026-27 (2nd Tuesday monthly)
[CAL] 2026-06-09 18:00 [D] Knights of Columbus :: meetings :: end=20:00
[CAL] 2026-07-14 18:00 [D] Knights of Columbus :: meetings :: end=20:00
[CAL] 2026-08-11 18:00 [D] Knights of Columbus :: meetings :: end=20:00
[CAL] 2026-09-08 18:00 [D] Knights of Columbus :: meetings :: end=20:00
[CAL] 2026-10-13 18:00 [D] Knights of Columbus :: meetings :: end=20:00
[CAL] 2026-11-10 18:00 [D] Knights of Columbus :: meetings :: end=20:00
[CAL] 2026-12-08 18:00 [D] Knights of Columbus :: meetings :: end=20:00
[CAL] 2027-01-12 18:00 [D] Knights of Columbus :: meetings :: end=20:00
[CAL] 2027-02-09 18:00 [D] Knights of Columbus :: meetings :: end=20:00
[CAL] 2027-03-09 18:00 [D] Knights of Columbus :: meetings :: end=20:00
[CAL] 2027-04-13 18:00 [D] Knights of Columbus :: meetings :: end=20:00
[CAL] 2027-05-11 18:00 [D] Knights of Columbus :: meetings :: end=20:00

---

### FAIRBOARD MEETING - 2026-27 (2nd Monday monthly)
[CAL] 2026-06-08 16:30 [D] Fairboard meeting :: meetings :: end=17:30
[CAL] 2026-07-06 16:30 [D] Fairboard meeting :: meetings :: end=17:30 :: location="Fairgrounds, Westcliffe, CO"
[CAL] 2026-08-10 16:30 [D] Fairboard meeting :: meetings :: end=17:30
[CAL] 2026-09-14 16:30 [D] Fairboard meeting :: meetings :: end=17:30
[CAL] 2026-10-12 16:30 [D] Fairboard meeting :: meetings :: end=17:30
[CAL] 2026-11-09 16:30 [D] Fairboard meeting :: meetings :: end=17:30
[CAL] 2026-12-14 16:30 [D] Fairboard meeting :: meetings :: end=17:30
[CAL] 2027-01-11 16:30 [D] Fairboard meeting :: meetings :: end=17:30
[CAL] 2027-02-08 16:30 [D] Fairboard meeting :: meetings :: end=17:30
[CAL] 2027-03-08 16:30 [D] Fairboard meeting :: meetings :: end=17:30
[CAL] 2027-04-12 16:30 [D] Fairboard meeting :: meetings :: end=17:30
[CAL] 2027-05-10 16:30 [D] Fairboard meeting :: meetings :: end=17:30

---

### FAITH FORMATION - School Year 2026-27
<!-- Start date TBD - individual entries pending parish confirmation. PQ-20 logged. -->
[CAL] 2026-08-01 ALL-DAY Faith Formation individual entries pending - confirm start date ⏰ :: prompt

---

### YOUTH GROUP - 2026 Season
<!-- Seasonal only - NOT year-round. Season end confirmed May 2026. -->
[CAL] 2026-05-14 18:30 Youth Group :: kids :: end=21:30
[CAL] 2026-05-21 18:30 Youth Group :: kids :: end=21:30
[CAL] 2026-05-28 18:30 Youth Group :: kids :: end=21:30

---

### TRASH PICKUP - Jul 2026 to Jan 2027 (every 4 weeks)

[CAL] 2026-05-06 ALL-DAY trash-day :: misc
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

[CAL] 2026-05-05 10:00 [K][D] Prenatal apt - Pueblo :: appointments :: stripe=appt :: location="Pueblo, CO"
[CAL] 2026-05-14 08:00 [W] Field trip - Sky Zone :: kids :: location="Colorado Springs, CO"
[CAL] 2026-05-14 ALL-DAY [M][R][C][E] PJ Day :: kids
[CAL] 2026-05-16 11:00 [R] Haircut :: kids
[CAL] 2026-05-16 11:00 [W] Art :: kids
[CAL] 2026-05-16 17:00 Mass :: liturgical :: location="St. Joseph's, Salida"
[CAL] 2026-05-18 10:00 [K] Apt - Gina :: appointments :: stripe=appt
[CAL] 2026-05-19 08:00 [M][R] Triathlon - Westcliffe :: kids :: location="Westcliffe, CO"
[CAL] 2026-05-22 ALL-DAY [D] Pick up wood shavings - Ryan Stover :: misc :: notes="In town"
[CAL] 2026-05-23 11:00 [R][M] Apt - Tacey :: appointments :: stripe=appt

---

### JUNE 2026

[CAL] 2026-06-01 ALL-DAY [W] Sweden trip :: kids :: span=2026-06-13 :: travel=true :: flag=true :: notes="🚩 F-05 drop-off pickup chaperone logistics unresolved"
[CAL] 2026-06-03 ALL-DAY [D][K] NV drop - Austin Auto :: misc :: location="Austin Automotive" :: notes="Kalea drives Tahoe, Matt drives NV. Pickup day = Tahoe drop day TBD"
[CAL] 2026-06-04 13:40 [K][D] Prenatal apt :: appointments :: stripe=appt
[CAL] 2026-06-05 ALL-DAY [W][M] Jackpot - Castle Rock :: 4h :: location="Castle Rock, CO"
[CAL] 2026-06-06 16:00 Mass - St. Benedict's, Florence :: liturgical :: end=18:00
[CAL] 2026-06-07 ALL-DAY [FAM] Swim meet - Las Animas :: family :: location="Las Animas, CO" :: notes="Corpus Christi obligation fulfilled via anticipated Mass Jun 6 17:00 St. Joseph's Salida"
[CAL] 2026-06-08 ALL-DAY [D] Kombucha brewed :: misc :: notes="Condition-based check - no time alert. Check when ready."
[CAL] 2026-06-09 09:00 [D] Dodge - tire rotation/balance/alignment :: misc :: location="Les Schwab Tires, Cañon City, CO"
[CAL] 2026-06-10 10:00 [M][R] Apt - Tacey :: appointments :: stripe=appt :: end=12:00
[CAL] 2026-06-15 10:00 [M][R] Art camp :: kids :: end=15:00 :: location="Westcliffe, CO"
[CAL] 2026-06-15 08:00 [D][W] Fairgrounds cleanup :: misc :: end=12:00
[CAL] 2026-06-16 10:00 [M][R] Art camp :: kids :: end=15:00 :: location="Westcliffe, CO"
[CAL] 2026-06-17 10:00 [M][R] Art camp :: kids :: end=15:00 :: location="Westcliffe, CO"
[CAL] 2026-06-18 10:00 [M][R] Art camp :: kids :: end=15:00 :: location="Westcliffe, CO"
[CAL] 2026-06-19 10:00 [M][R] Art camp :: kids :: end=15:00 :: location="Westcliffe, CO"
[CAL] 2026-06-16 12:00 [W] Dentist :: appointments :: stripe=appt :: location="Cañon Family Dental, Cañon City, CO"
[CAL] 2026-06-17 13:30 [K] WIC Recertification :: appointments :: stripe=appt
[CAL] 2026-06-17 10:30 [W][K] School advisory apt :: appointments :: stripe=appt :: end=11:30
[CAL] 2026-06-18 13:00 [K] Apt - Gina :: appointments :: stripe=appt
[CAL] 2026-06-18 15:30 [D] Apt - Wentz Foot and Ankle :: appointments :: stripe=appt :: end=16:15 :: location="Salida, CO"
[CAL] 2026-06-18 10:15 [D] Orthopedic apt :: appointments :: stripe=appt :: end=11:15 :: location="Westcliffe Clinic, Westcliffe, CO"
[CAL] 2026-06-20 ALL-DAY [FAM] Swim meet - Pueblo County :: family :: location="Pueblo, CO"
[CAL] 2026-06-20 08:00 [W][M] Livestock clinic - Florence :: misc :: location="Florence, CO" :: cancel=confirmed
[CAL] 2026-06-25 13:30 [W] Ortho :: appointments :: stripe=appt :: location="Pueblo, CO"
[CAL] 2026-06-25 16:00 [R] Haircut :: kids
[CAL] 2026-06-25 ALL-DAY [D] Scale certification :: misc :: location="Fairgrounds, Westcliffe, CO" :: notes="time TBD"
[CAL] 2026-06-06 08:00 [D] Deworm pigs :: farm :: note="Stockyard reminder - deworming day"
[CAL] 2026-06-11 ALL-DAY [D] Meet up with Tom :: misc :: span=2026-06-12 :: tentative=true
[CAL] 2026-06-13 ALL-DAY Fr. Joe birthday :: misc
[CAL] 2026-06-13 ALL-DAY Uncle Doug birthday :: misc
[CAL] 2026-06-14 08:00 [W][M] Serve at Mass :: liturgical :: end=09:00 :: location="St. Joseph's, Salida"
[CAL] 2026-06-17 14:00 [M][W] 4H volunteer event :: kids :: end=15:00 :: flag=true :: note="Date unconfirmed - June 17 or 24. Jun 17: Molly art camp ends 15:00 - conflict. Jun 24 cleaner."
[CAL] 2026-06-26 14:00 [M] Jackpot prep - Gonzalez :: kids :: end=16:00
[CAL] 2026-06-26 ALL-DAY [K] Gardyn roots check ⏰ :: prompt :: notes="14-day rolling cadence. Last checked 2026-06-08 by Kalea. On confirm, set next check +14 days. Voice: Rootstock."
[CAL] 2026-06-27 ALL-DAY [W][M] Jackpot - Monte Vista :: 4h :: location="Monte Vista, CO"
[CAL] 2026-06-29 08:00 [D] Deworm pigs :: farm :: note="Stockyard reminder - deworming day. Last dewormed 2026-06-08, moved from 06-27 per Matt."
[CAL] 2026-06-28 ALL-DAY [FAM] Mesquite trip - Nevada :: family :: span=2026-07-02 :: travel=true

---

### JULY 2026

[CAL] 2026-07-08 09:30 [D] Optometrist :: appointments :: stripe=appt :: end=10:30 :: location="Westcliffe Clinic, Westcliffe, CO"
[CAL] 2026-07-16 13:30 [K][D] New patient apt :: appointments :: stripe=appt :: end=14:30 :: location="Westcliffe Clinic, Westcliffe, CO"
[CAL] 2026-07-08 10:20 [K] Dentist :: appointments :: stripe=appt :: location="Cañon Family Dental, Cañon City, CO"
[CAL] 2026-07-09 16:00 Fair cleanup :: 4h :: location="Westcliffe, CO"
[CAL] 2026-07-11 ALL-DAY [FAM] Swim meet - Piranhas home meet :: family :: location="Pueblo, CO"
[CAL] 2026-07-14 ALL-DAY [GUEST] Adam and Bethany :: misc :: span=2026-07-17
[CAL] 2026-07-14 15:00 [W][M] Weigh-in / Picnic :: 4h :: location="Westcliffe, CO"
[CAL] 2026-07-15 17:00 [W][M] Swine show + pork meal :: 4h :: location="Westcliffe, CO"
[CAL] 2026-07-16 09:00 [M] Sheep show :: 4h :: location="Westcliffe, CO"
[CAL] 2026-07-17 12:00 [M] Master showmanship - sheep :: 4h :: location="Westcliffe, CO"
[CAL] 2026-07-18 12:00 [W][M] Buckle ceremony + livestock sale :: 4h :: location="Westcliffe, CO"
[CAL] 2026-07-19 08:00 [W][M] Serve at Mass :: liturgical :: end=09:00 :: location="St. Joseph's, Salida"
[CAL] 2026-07-19 ALL-DAY [FAM] Swim meet - Salida :: family :: location="Salida, CO" :: tentative=true
[CAL] 2026-07-19 12:00 [W][M] Fair cleanup :: 4h :: location="Westcliffe, CO" :: notes="W+M at fair cleanup - cannot attend Salida swim meet same day"
[CAL] 2026-07-24 ALL-DAY [FAM] Swim meet - SECAL Championship :: family :: location="Las Animas, CO" :: span=2026-07-26
[CAL] 2026-07-31 ALL-DAY [FAM] Swim meet - State Championship :: family :: location="Alamosa, CO" :: span=2026-08-02

---

### AUGUST 2026

[CAL] 2026-08-16 08:00 [W][M] Serve at Mass :: liturgical :: end=09:00 :: location="St. Joseph's, Salida"
[CAL] 2026-08-31 ALL-DAY [K][D] SNAP recert :: appointments :: flag=true :: tentative=true :: notes="🚩 Time TBD - physical paperwork required. Bring required docs. Prompts fire Jul 15 + Aug 1."

---

### MILESTONES - Punch List / Wyatt / Mantel

[CAL] 2026-06-15 ALL-DAY [K] CAC renewal reminder ⏰ :: prompt
[CAL] 2026-07-15 ALL-DAY [K][D] SNAP recert - gather docs ⏰ :: prompt
[CAL] 2026-08-01 ALL-DAY [K][D] SNAP recert - appt Aug 31 ⏰ :: prompt
[CAL] 2026-08-01 ALL-DAY Wyatt driver-ed research ⏰ :: prompt
[CAL] 2026-08-01 ALL-DAY Jackson trailer registration ⏰ :: prompt
[CAL] 2026-08-01 ALL-DAY Kalea teaching block - confirm fall schedule ⏰ :: prompt
[CAL] 2026-08-01 ALL-DAY Youth Group fall schedule - confirm ⏰ :: prompt
[CAL] 2026-08-01 ALL-DAY Faith Formation fall start - confirm with parish ⏰ :: prompt
[CAL] 2026-09-15 ALL-DAY Enroll Wyatt in driver ed ⏰ :: prompt
[CAL] 2026-11-08 ALL-DAY [D][K] Wedding anniversary :: misc
[CAL] 2026-12-15 ALL-DAY Wyatt driver ed cert check ⏰ :: prompt
[CAL] 2027-01-01 ALL-DAY Wyatt DMV permit appt ⏰ :: prompt
[CAL] 2027-02-27 ALL-DAY [K] CO DL renewal reminder ⏰ :: prompt
[CAL] 2027-04-22 ALL-DAY Wyatt permit checkpoint - 3 mo ⏰ :: prompt
[CAL] 2027-07-22 ALL-DAY Wyatt permit checkpoint - 6 mo ⏰ :: prompt
[CAL] 2027-10-22 ALL-DAY Wyatt permit checkpoint - 9 mo ⏰ :: prompt
[CAL] 2028-01-01 ALL-DAY Wyatt CO road test ⏰ :: prompt
[CAL] 2028-09-07 ALL-DAY [D] CO DL renewal reminder ⏰ :: prompt
[CAL] 2029-01-01 ALL-DAY Wyatt restricted phase ending check ⏰ :: prompt

---

### LITURGICAL - 2026 Calendar Events

[CAL] 2026-02-18 ALL-DAY Ash Wednesday - Mass attendance :: liturgical
[CAL] 2026-02-20 ALL-DAY Lenten Friday - Stations + fish dinner :: liturgical
[CAL] 2026-02-27 ALL-DAY Lenten Friday - Stations + fish dinner :: liturgical
[CAL] 2026-03-06 ALL-DAY Lenten Friday - Stations + fish dinner :: liturgical
[CAL] 2026-03-08 ALL-DAY DST begins - protect Sunday :: misc
[CAL] 2026-03-13 ALL-DAY Lenten Friday - Stations + fish dinner :: liturgical
[CAL] 2026-03-20 ALL-DAY Lenten Friday - Stations + fish dinner :: liturgical
[CAL] 2026-03-27 ALL-DAY Lenten Friday - Stations + fish dinner :: liturgical
[CAL] 2026-04-02 18:00 Holy Thursday Mass - W. serving :: liturgical :: end=19:15
[CAL] 2026-04-03 12:00 Good Friday - Stations 1200 + Service 1500 :: liturgical :: end=13:15
[CAL] 2026-04-04 17:45 Easter Vigil :: liturgical :: end=20:00
[CAL] 2026-04-05 ALL-DAY Easter Sunday :: liturgical
[CAL] 2026-04-25 ALL-DAY Loretto Chapel day - sacred memory :: liturgical
[CAL] 2026-11-01 ALL-DAY DST ends - protect Sunday :: misc
[CAL] 2026-11-26 10:00 Thanksgiving Mass :: liturgical :: end=11:30 :: location="St. Joseph's, Salida"

---

### LITURGICAL - Curated Feasts 2026
<!-- Filter: Holy Days of Obligation + feasts with food tradition or significant family observance. Voice: Mantel. -->

[CAL] 2026-01-01 ALL-DAY Mary, Mother of God :: liturgical
[CAL] 2026-01-06 ALL-DAY Epiphany 🍞 :: liturgical :: notes="king cake"
[CAL] 2026-02-02 ALL-DAY Candlemas 🍞 :: liturgical :: notes="crepes"
[CAL] 2026-02-03 ALL-DAY St. Blaise - throat blessing :: liturgical
[CAL] 2026-02-11 ALL-DAY Our Lady of Lourdes :: liturgical
[CAL] 2026-02-14 ALL-DAY St. Valentine :: liturgical
[CAL] 2026-03-17 ALL-DAY St. Patrick 🍞 :: liturgical :: notes="corned beef, soda bread"
[CAL] 2026-03-19 ALL-DAY St. Joseph 🍞 :: liturgical :: notes="zeppole, pasta"
[CAL] 2026-03-25 ALL-DAY Annunciation :: liturgical
[CAL] 2026-04-23 ALL-DAY St. George :: liturgical
[CAL] 2026-05-01 ALL-DAY St. Joseph the Worker :: liturgical
[CAL] 2026-05-13 ALL-DAY Our Lady of Fatima :: liturgical
[CAL] 2026-05-15 ALL-DAY St. Isidore - patron of Edelweiss :: liturgical
[CAL] 2026-05-31 ALL-DAY Visitation :: liturgical
[CAL] 2026-05-17 ALL-DAY Ascension of the Lord - Holy Day of Obligation :: liturgical :: notes="US transfer to Sunday"
[CAL] 2026-05-24 ALL-DAY Pentecost Sunday - Holy Day :: liturgical
[CAL] 2026-06-07 ALL-DAY Corpus Christi - Holy Day :: liturgical
[CAL] 2026-06-13 ALL-DAY St. Anthony 🍞 :: liturgical :: notes="bread of St. Anthony"
[CAL] 2026-06-24 ALL-DAY Birth of St. John the Baptist 🍞 :: liturgical :: notes="bonfire feast, summer foods"
[CAL] 2026-06-29 ALL-DAY Sts. Peter and Paul 🍞 :: liturgical :: notes="fish"
[CAL] 2026-07-16 ALL-DAY Our Lady of Mount Carmel :: liturgical
[CAL] 2026-07-22 ALL-DAY St. Mary Magdalene :: liturgical
[CAL] 2026-07-26 ALL-DAY Sts. Joachim and Anne :: liturgical
[CAL] 2026-08-06 ALL-DAY Transfiguration 🍞 :: liturgical :: notes="grapes, first fruits"
[CAL] 2026-08-15 ALL-DAY Assumption of Mary - Holy Day of Obligation :: liturgical
[CAL] 2026-08-22 ALL-DAY Queenship of Mary :: liturgical
[CAL] 2026-09-08 ALL-DAY Birth of Mary :: liturgical
[CAL] 2026-09-14 ALL-DAY Exaltation of the Holy Cross :: liturgical
[CAL] 2026-09-29 ALL-DAY Sts. Michael, Gabriel, Raphael :: liturgical
[CAL] 2026-10-01 ALL-DAY St. Therese of Lisieux :: liturgical
[CAL] 2026-10-02 ALL-DAY Guardian Angels :: liturgical
[CAL] 2026-10-04 ALL-DAY St. Francis - animal blessing :: liturgical
[CAL] 2026-10-07 ALL-DAY Our Lady of the Rosary :: liturgical
[CAL] 2026-10-28 ALL-DAY Sts. Simon and Jude :: liturgical
[CAL] 2026-10-31 ALL-DAY All Hallows Eve :: liturgical
[CAL] 2026-11-01 ALL-DAY All Saints Day - Holy Day of Obligation :: liturgical
[CAL] 2026-11-02 ALL-DAY All Souls Day 🍞 :: liturgical :: notes="pan de muerto"
[CAL] 2026-11-11 ALL-DAY St. Martin of Tours 🍞 :: liturgical :: notes="goose, wine"
[CAL] 2026-11-22 ALL-DAY St. Cecilia :: liturgical
[CAL] 2026-11-25 ALL-DAY St. Catherine of Alexandria :: liturgical
[CAL] 2026-12-06 ALL-DAY St. Nicholas 🍞 :: liturgical :: notes="treats in shoes"
[CAL] 2026-12-08 ALL-DAY Immaculate Conception - Holy Day of Obligation :: liturgical
[CAL] 2026-12-12 ALL-DAY Our Lady of Guadalupe 🍞 :: liturgical :: notes="tamales"
[CAL] 2026-12-13 ALL-DAY St. Lucy 🍞 :: liturgical :: notes="saffron buns"
[CAL] 2026-12-25 ALL-DAY Christmas - Nativity of the Lord 🍞 :: liturgical :: notes="Mass attendance"
[CAL] 2026-12-27 ALL-DAY St. John the Apostle :: liturgical
[CAL] 2026-12-28 ALL-DAY Holy Innocents :: liturgical

---

### LITURGICAL - Curated Feasts 2027

[CAL] 2027-01-01 ALL-DAY Mary, Mother of God :: liturgical
[CAL] 2027-01-06 ALL-DAY Epiphany 🍞 :: liturgical :: notes="king cake"
[CAL] 2027-02-02 ALL-DAY Candlemas 🍞 :: liturgical :: notes="crepes"
[CAL] 2027-02-03 ALL-DAY St. Blaise - throat blessing :: liturgical
[CAL] 2027-02-11 ALL-DAY Our Lady of Lourdes :: liturgical
[CAL] 2027-02-14 ALL-DAY St. Valentine :: liturgical
[CAL] 2027-03-17 ALL-DAY St. Patrick 🍞 :: liturgical :: notes="corned beef, soda bread"
[CAL] 2027-03-19 ALL-DAY St. Joseph 🍞 :: liturgical :: notes="zeppole, pasta"
[CAL] 2027-03-25 ALL-DAY Annunciation :: liturgical
[CAL] 2027-04-23 ALL-DAY St. George :: liturgical
[CAL] 2027-05-01 ALL-DAY St. Joseph the Worker :: liturgical
[CAL] 2027-05-13 ALL-DAY Our Lady of Fatima :: liturgical
[CAL] 2027-05-15 ALL-DAY St. Isidore - patron of Edelweiss :: liturgical
[CAL] 2027-05-31 ALL-DAY Visitation :: liturgical
[CAL] 2027-06-06 ALL-DAY Ascension of the Lord - Holy Day of Obligation :: liturgical :: notes="US transfer to Sunday"
[CAL] 2027-06-13 ALL-DAY Pentecost Sunday - Holy Day :: liturgical
[CAL] 2027-06-27 ALL-DAY Corpus Christi - Holy Day :: liturgical
[CAL] 2027-06-13 ALL-DAY St. Anthony 🍞 :: liturgical :: notes="bread of St. Anthony"
[CAL] 2027-06-24 ALL-DAY Birth of St. John the Baptist 🍞 :: liturgical :: notes="bonfire feast, summer foods"
[CAL] 2027-06-29 ALL-DAY Sts. Peter and Paul 🍞 :: liturgical :: notes="fish"
[CAL] 2027-07-16 ALL-DAY Our Lady of Mount Carmel :: liturgical
[CAL] 2027-07-22 ALL-DAY St. Mary Magdalene :: liturgical
[CAL] 2027-07-26 ALL-DAY Sts. Joachim and Anne :: liturgical
[CAL] 2027-08-06 ALL-DAY Transfiguration 🍞 :: liturgical :: notes="grapes, first fruits"
[CAL] 2027-08-15 ALL-DAY Assumption of Mary - Holy Day of Obligation :: liturgical
[CAL] 2027-08-22 ALL-DAY Queenship of Mary :: liturgical
[CAL] 2027-09-08 ALL-DAY Birth of Mary :: liturgical
[CAL] 2027-09-14 ALL-DAY Exaltation of the Holy Cross :: liturgical
[CAL] 2027-09-29 ALL-DAY Sts. Michael, Gabriel, Raphael :: liturgical
[CAL] 2027-10-01 ALL-DAY St. Therese of Lisieux :: liturgical
[CAL] 2027-10-02 ALL-DAY Guardian Angels :: liturgical
[CAL] 2027-10-04 ALL-DAY St. Francis - animal blessing :: liturgical
[CAL] 2027-10-07 ALL-DAY Our Lady of the Rosary :: liturgical
[CAL] 2027-10-28 ALL-DAY Sts. Simon and Jude :: liturgical
[CAL] 2027-10-31 ALL-DAY All Hallows Eve :: liturgical
[CAL] 2027-11-01 ALL-DAY All Saints Day - Holy Day of Obligation :: liturgical
[CAL] 2027-11-02 ALL-DAY All Souls Day 🍞 :: liturgical :: notes="pan de muerto"
[CAL] 2027-11-11 ALL-DAY St. Martin of Tours 🍞 :: liturgical :: notes="goose, wine"
[CAL] 2027-11-22 ALL-DAY St. Cecilia :: liturgical
[CAL] 2027-11-25 ALL-DAY St. Catherine of Alexandria :: liturgical
[CAL] 2027-12-06 ALL-DAY St. Nicholas 🍞 :: liturgical :: notes="treats in shoes"
[CAL] 2027-12-08 ALL-DAY Immaculate Conception - Holy Day of Obligation :: liturgical
[CAL] 2027-12-12 ALL-DAY Our Lady of Guadalupe 🍞 :: liturgical :: notes="tamales"
[CAL] 2027-12-13 ALL-DAY St. Lucy 🍞 :: liturgical :: notes="saffron buns"
[CAL] 2027-12-25 ALL-DAY Christmas - Nativity of the Lord 🍞 :: liturgical :: notes="Mass attendance"
[CAL] 2027-12-27 ALL-DAY St. John the Apostle :: liturgical
[CAL] 2027-12-28 ALL-DAY Holy Innocents :: liturgical

---

### BIRTHDAYS - Immediate Family

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

### FEDERAL HOLIDAYS + OBSERVANCES - 2026

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

---

### FEDERAL HOLIDAYS + OBSERVANCES - 2027

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
