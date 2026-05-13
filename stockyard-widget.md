# stockyard-widget.md — Egg Tracker Reference

**Status:** Live as a Claude artifact in a pinned chat. Predates the Stockyard agent.
**Owner (future):** Stockyard
**Owner (now):** Standalone widget, Matt enters counts daily.

This file exists so the future Stockyard agent build doesn't have to re-derive the schema, constants, or operational context. Read this before designing Stockyard's egg-tracking module.

---

## What it is

An interactive widget — HTML/JS, runs inline in a Claude chat — that tracks daily egg counts for the Edelweiss Farms layer flock. Features:

- Daily count entry with today's expected vs. actual
- 7-day rolling avg, 30-day rolling avg, MTD total, YTD total
- Flock config: total hens with year-1 / year-2 split (default 50/50)
- Molt detection: trailing 7-day vs. prior 7-day drop analysis
- 60-day production chart, daily + 7-day rolling overlay
- Bulk import (back-data from the whiteboard)
- CSV export

## Where it lives

- **The widget itself:** pinned chat in this project. Not in project knowledge — widgets render in the chat that built them; loading the source as a knowledge file doesn't make it reusable.
- **Per-conversation storage:** the widget writes to `window.storage` in its own chat. Data does not cross chats.
- **Bridge to the repo:** CSV export → `stockyard/eggs-log.csv` in the family-ops repo, once Matt starts exporting. That's the durable record the Stockyard agent will eventually read.

## Storage schema

The widget's `window.storage` keys are deliberately namespaced to match what Stockyard will own when the agent ships. Carry these names forward without changes.

```
stockyard/eggs-log      → { "YYYY-MM-DD": <int count>, ... }
stockyard/flock-config  → { y1Count: <int>, y2Count: <int> }
```

**Rule from family.md (recent update):** A blank entry in the egg log means "uncollected / unrecorded," NOT a real zero. The Bayer flock never has zero-egg days. Stockyard's analysis must treat missing dates as null, not zero, when computing averages and trend lines.

## Production model constants

Used for "expected today" calculations and molt detection. These are starting assumptions — refine after a full year of real data.

**Per-hen daily lay rate at peak:**
- Year 1 hens: 0.80 eggs/day
- Year 2 hens: 0.65 eggs/day

**Seasonal modifier (multiplier on peak):**

| Month | Modifier |
|---|---|
| Jan | 0.65 |
| Feb | 0.65 |
| Mar | 0.80 |
| Apr | 0.95 |
| May | 0.95 |
| Jun | 1.00 |
| Jul | 1.00 |
| Aug | 0.95 |
| Sep | 0.85 |
| Oct | 0.70 |
| Nov | 0.55 |
| Dec | 0.55 |

**Expected daily count** = `(y1Count × 0.80 + y2Count × 0.65) × seasonalModifier[month]`

**Altitude caveat:** Edelweiss Farms is at 9000 ft, Westcliffe CO, zone 4a. High altitude likely depresses winter production further than the seasonal modifier alone captures. Track Nov-Feb actuals carefully and add an altitude factor in v2 if winter consistently underruns expected by >15%.

## Molt detection logic

Trailing 7-day average vs. prior 7-day average:

- **40-60% drop:** half-flock molt suspected. The Bayer operation refreshes ~50% of layers annually, so partial-flock molts are expected each fall. Recovery estimate: 6-8 weeks.
- **>60% drop:** non-molt cause likely — water issue, predator, illness, extreme weather. Surface as a flag, not a recovery estimate.
- **<40% drop:** seasonal noise, no alert.

## Operational context (for the future Stockyard agent)

- The whiteboard on the family fridge is the family's primary record. Orange numbers in the upper-right of each cell = daily egg count. Started late 2025 when the layers came online.
- Matt and Kalea both update the whiteboard. The widget is the digital ledger; the whiteboard is the wall ledger. They should stay in sync, but the whiteboard wins for daily ops.
- Flock refresh cycle: half the layers are replaced annually. At any given time, y1 and y2 hens are present in roughly equal numbers. Refresh timing TBD — capture when Matt confirms.

## When Stockyard ships

The agent inherits:
1. The CSV export at `stockyard/eggs-log.csv` as the durable record
2. This file's schema and constants as the starting design
3. Responsibility for displacing the widget — or keeping it as the daily-entry UI while the agent owns analysis. Matt's call at that point.

Until then, the widget is the system.
