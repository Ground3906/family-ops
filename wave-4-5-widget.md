# wave-4-5-widget.md — Calendar Widget Reference

**Current version:** v2.8
**Filename convention:** `wave-4-5-widget-v[MAJOR].[MINOR].html` — DOT notation always, NEVER underscore
**Status:** Wave 4.5 CLOSED. v2.8 canonical. PQ-29 parked.
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
| v2.6 | 2026-05-26 | meetings category added (📋) to CAT_EMOJI/CAT_MAP/CAT_CLS. KoC + Fairboard entries updated in calendars.md. syncNavH() + --nh var added. |
| v2.7 | 2026-05-26 | Cook mode inset:0 attempt — centers at true 50vh but visual perception off |
| v2.8 | 2026-05-26 | Cook mode padding:var(--hh) 24px var(--nh) — reserves header+nav zones. PQ-29 still open. |

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
| meetings | 📋 | KoC, Fairboard, any recurring meeting |
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

**Everything else = individual [CAL] entries.**

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

## Cook Mode (v2.8)

CSS: `position:fixed; inset:0; z-index:50; padding:var(--hh) 24px var(--nh)`
Header + nav sit at z-index:100 on top. Padding reserves header and nav zones so flexbox centers in visible space.
**PQ-29: Centering still not resolved.** Requires devtools on live server to diagnose. Do not guess-fix.
Mode Sovereignty — calendar hidden. Home button (location.reload) exits cook mode.

---

## CSS Variables (v2.6+)

- `--hh` — header height. Set by `syncHdrH()` on init + resize.
- `--nh` — nav height. Set by `syncNavH()` on init + resize.
- `--cell-hdr-h` — cell header height (54px fixed).

---

## Week View Layout

When week view active, JS applies `applyWeekLayout()`:
- `#cal-wrap` becomes `position:fixed` from header to nav bottom
- `#weeks` gets `flex: 0 0 55%`
- `#week-detail` gets `flex: 0 0 45%`
- Cell height fills container (not fixed 180px)

`clearWeekLayout()` restores normal flow when leaving week view.

---

## Open Items (not resolved — carry forward)

- **PQ-29: Cook Mode vertical centering** — persistent across v2.5-v2.8. Requires devtools session on live server. Do not guess-fix again.
- **Faith Formation 2026-27 entries** — parish publishes schedule in August. Add individual entries, remove placeholder prompt at that time.

---

## Parked PQs

| PQ | Description | Wave |
|----|-------------|------|
| PQ-22 | Liturgical data 2028-2035 | Phase 1 closeout |
| PQ-29 | Cook Mode vertical centering — devtools required | 4.6 |
| PQ-03 | Egg count hardcoded 47 — pull from stockyard:eggs-log | 4.6 |
| PQ-04 | Agent buttons — wire to modules | 4.6 |
| PQ-06 | Saint panel — Mantel stub | 4.6 |
| PQ-08 | Cook mode recipe — Chow Hall | 4.6 |
| PQ-11 | Meal Planner full view — Chow Hall | 4.6 |

---

## Stockyard S8 Hook (HARD GATE)

Auto-export to repo via GitHub MCP. Blocks:
- Real flock data entry in Stockyard widget
- Wave 4.5 calendar integration

Not built. Not bypassed. Surface every session.
