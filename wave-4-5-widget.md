# wave-4-5-widget.md — Calendar Widget Reference

**Current version:** v2.5
**Filename convention:** `wave-4-5-widget-v[MAJOR].[MINOR].html` — DOT notation always, NEVER underscore
**Status:** Live on local server. Kalea adoption is the bar. Phase 1 canonical.
**Served from:** `C:\dev\family-ops` via `python -m http.server 8080`
**Data source:** `calendars.md` in same directory — fetched live on load and Home button

---

## Hard Gates

- **Stockyard S8 durability fix** — still open. No real flock data entry until fixed.
- **COCKPIT IS READ-ONLY.** No entry tool, no form, no keyboard on Cockpit. Ever.
- **NEVER patch data files to work around code bugs.** Fix the code. Log as PQ.
- **Full rewrite only** — never surgical patches to widget HTML. Version up, full file.

---

## Version History

| Version | Date | Key Changes |
|---------|------|-------------|
| v2.0 | 2026-05-25 | Phase 1 canonical. Category emoji, KIDS pill, bottom nav, week view, Day Panel v2 |
| v2.1 | 2026-05-25 | PQ-26 through PQ-32. Span color stamp, tentative renderer, FAM/KIDS collapse fixes |
| v2.2 | 2026-05-25 | Emoji flush, view button height, cook mode overlay, month/year align, week view viewport, sep cleanup, span time display |
| v2.3 | 2026-05-25 | Span return time order, flag bleed fix, optional=true field, title parser hardened, feast weight unified, cook mode CSS |
| v2.4 | 2026-05-25 | Auto-conflict detection (pill + time overlap), cook mode z-index/centering, conflict brief detail |
| v2.5 | 2026-05-25 | Brief color doctrine, +N more visible, optional events hidden from cell, Home = location.reload(), nav two-zone layout |

---

## Pill Colors (locked)

```
D=#9a5828  K=#1a50e0  W=#cc2233  M=#9944cc  R=#f040b8
C=#2070b8  E=#156e2a  B6=#faa030  OMA=#7755cc  PAPA=#6ec898
GUEST=#E8DFC0  FAM=#7a7aaa  KIDS=#a0c840
```

`B6_ACTIVE=false` — flip post-birth (~2026-08-15). Gates B6 pill display everywhere.

---

## Category Emoji Map (locked)

| Cat key | Emoji | Use |
|---------|-------|-----|
| liturgical | ✝️ | Feast days, Holy Days, Mass |
| kids | 🚸 | Kids events, swim practice, Faith Formation |
| family | 🏠 | Whole-family events, swim meets |
| animals | 🐾 | Farm/animal events |
| appointments | ➕ | Medical, dental, therapy |
| 4h | 🍀 | 4H events, fair |
| rootstock | 🌱 | Garden, orchard |
| prompt | ⏰ | Reminders, milestone pings |
| misc | (none) | Catch-all |

---

## calendars.md Schema

### Entry formats

```
[CAL] YYYY-MM-DD HH:MM [PILLS] Title :: category :: opt=val :: opt=val
[CAL] YYYY-MM-DD ALL-DAY [PILLS] Title :: category :: opt=val
[CAL-RECUR weekly start=YYYY-MM-DD day=dow] HH:MM [PILLS] Title :: category :: opt=val
[BRIEF] YYYY-MM-DD [AgentName] text
```

### Supported options

| Option | Values | Notes |
|--------|--------|-------|
| end= | HH:MM | Event end time. Required for auto-conflict detection to work correctly |
| flag=true | boolean | Special-case flag only — Holy Days, unresolved logistics, unconfirmed dates. NEVER for scheduling conflicts (auto-detected) |
| optional=true | boolean | Event never consumes cell slot, never triggers conflict flag. Use for Daily Mass recurrence |
| travel=true | boolean | Person physically away from home. Triggers pill suppression on overlapping events |
| span= | YYYY-MM-DD | End date for multi-day span. Expands to start/mid/end events |
| tentative=true | boolean | Renders with diagonal stripe hatching |
| stripe=appt | string | Red-tinted appointment background |
| location= | "string" | Renders in day panel detail |
| notes= | "string" | Renders in day panel detail |
| vehicle= | tahoe/dodge/nv | Punch List vehicle assignment |
| driver= | pill code | Punch List driver assignment |

### Recurring entry doctrine (LOCKED 2026-05-25)

**Only two CAL-RECUR entries permitted:**
- Sunday Mass 08:00 — never changes, never has exceptions
- Daily Mass Wed 10:00 — optional=true, always loses to other events

**Everything else = individual [CAL] entries.** Seasonal events (swim practice, Faith Formation, Knights, Fairboard, Youth Group) all have start/end dates and exceptions. Individual entries give full control. CAL-RECUR for seasonal events is forbidden — it causes exception complexity that breaks conflict detection.

---

## Auto-Conflict Detection (v2.4+)

Widget scans each day for family pill + time window overlap automatically. No manual flag=true needed for scheduling conflicts.

**Logic:**
1. Find all timed (non-all-day) events with core family pills (D,K,W,M,R,C,E,B6)
2. Expand FAM/KIDS group pills to individual members
3. For each pair, check time overlap: `A.start < B.end && B.start < A.end`
4. Default duration = 60 min if no `end=` set — **always set end= times**
5. If overlap + shared family member → fire ⚑ on cell AND render detail row in brief
6. Skip travel events (travel suppression handles those)
7. Skip optional=true events

**Brief conflict row format:** `[pill colors]: EventA 09:30-12:00 conflicts with EventB 10:00-15:00`

**flag=true reserved for:** Holy Day obligations, unresolved logistics, unconfirmed dates, travel chaperone issues.

---

## Brief Color Doctrine (v2.5)

| Row type | Color | CSS class |
|----------|-------|-----------|
| Conflict (auto or manual) | #ff5000 (orange-red) | brief-conflict |
| Vehicle/driver | var(--cb) gold | brief-vehicle |
| Appointment | #c86878 muted rose | brief-appt |
| Travel/departure | #4aa8d4 blue | brief-travel |
| Sacred | var(--cb) gold | brief-sacred |

Red = action required. Everything else = informational.

---

## Nav Layout (v2.5)

Two-zone bottom nav:
- **Left zone (.nav-view-zone):** Rolling, Week, Month — separated by vertical divider
- **Right zone (.nav-action-zone, flex:1, justify-content:center):** ←, Home, Cook Mode, Night, →

---

## Cook Mode (v2.5)

CSS: `position:fixed; top:var(--hh); left:0; right:0; bottom:0; z-index:50; padding:24px 24px 76px`
Nav sits on top at z-index:100. Padding-bottom:76px reserves nav zone for centering.
Mode Sovereignty — calendar hidden. Home button (location.reload) exits cook mode.

---

## Week View Layout

When week view active, JS applies `applyWeekLayout()`:
- `#cal-wrap` becomes `position:fixed` from header to nav bottom
- `#weeks` gets `flex: 0 0 55%`
- `#week-detail` gets `flex: 0 0 45%`
- Cell height fills container (not fixed 180px)

`clearWeekLayout()` restores normal flow when leaving week view.

---

## Parked PQs

| PQ | Description | Wave |
|----|-------------|------|
| PQ-22 | Liturgical data 2028-2035 | Phase 1 closeout |
| PQ-03 | Egg count hardcoded 47 — pull from stockyard:eggs-log | 4.6 |
| PQ-04 | Agent buttons — wire to modules | 4.6 |
| PQ-06 | Saint panel — Mantel stub | 4.6 |
| PQ-08 | Cook mode recipe — Chow Hall | 4.6 |
| PQ-11 | Meal Planner full view — Chow Hall | 4.6 |

---

## Open Items (not resolved in v2.5)

- Cook Mode centering — Matt not satisfied with current fix. Nav two-zone helped nav balance. Cook mode screen centering still under review.
- Phase 2 Foreman hook — Foreman writes [CAL] entries via GitHub MCP. Widget fetches live. Cockpit reflects on refresh.
- Swim practice end date — season ends ~Jul 30. No explicit season-end entry. Add if needed.
- Faith Formation individual entries — pending parish start date confirmation.

---

## Stockyard S8 Hook (HARD GATE)

Auto-export to repo via GitHub MCP. Blocks:
- Real flock data entry in Stockyard widget
- Wave 4.5 calendar integration

Not built. Not bypassed. Surface every session.
