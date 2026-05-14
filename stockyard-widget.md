# stockyard-widget.md — Egg & Ledger Reference (v2)

**Status:** Live as a Claude artifact in a pinned chat. Predates the Stockyard agent.
**Owner (future):** Stockyard
**Owner (now):** Standalone widget. Matt enters counts daily; Kalea cross-checks against the whiteboard.
**Widget version:** v2 (transaction-based flock model, breed-aware, vacuum projections, tiered alerts)

This file exists so the future Stockyard agent build doesn't have to re-derive the schema, constants, or operational context from the widget code. Read this before designing Stockyard's egg-tracking module.

---

## What it is

An interactive widget — HTML/JS, runs inline in a Claude chat — that tracks daily egg counts, flock composition over time, and breed-level performance for Edelweiss Farms, LLC. Features:

- **Today:** daily count entry, expected band (±15%), in-range/over/under pill, MTD and YTD running totals with dozen breakdown, 60-day production chart (daily bars + 7-day rolling average + shaded expected band)
- **Back-fill:** month-grid calendar, tap-a-day entry, blank = uncollected (never zero)
- **Records:** lifetime eggs, avg eggs per day (twin: per logged day vs per calendar day), avg eggs per hen (twin: same split, walks effective flock count daily), biggest/smallest day, best/slowest month, monthly breakdown table, collection consistency stats
- **Vacuum projections:** sealed-lab projection from advertised breed data × cohort age factor × seasonal modifier × count. Reality-factor compares actual YTD against projected YTD. Color-coded against a configurable floor.
- **Flock:** three-panel layout. (a) Current flock — computed live from transaction log, broken down by category and by cohort. (b) Record-a-change form — date, category, breed, cohort year, sign (+/−), count, reason, notes. (c) History — full transaction list with edit/delete per row.
- **Breeds:** ~25 seeded breeds (user's current order plus common varieties), breed autocomplete on category fields, click any breed name anywhere in the app to open a data card (advertised eggs/year, color, size, weight, lay onset, productive years, temperament, origin — or for meat breeds: mature weight, days-to-process, FCR, dressing %). User override field for advertised eggs/year. User notes per breed.
- **Pullet auto-promotion:** pullet cohorts age into layer cohorts at breed-specific lay onset (or 5-month fallback). Auto-generated as paired -pullet/+layer transactions on the promotion date, tagged `auto`.
- **Alerts:** tiered shortfall detection on the dashboard — Tier 1 (25–40% under expected), Tier 2 (40–60%, half-flock molt suspected), Tier 3 (60%+, non-molt cause likely).
- **Import / Export:** CSV in for eggs (`YYYY-MM-DD,count`), CSV out for eggs, for full flock transaction log, for breeds with user overrides and notes.

## Where it lives

- **The widget itself:** pinned chat in this project. Not in project knowledge — widgets render in the chat that built them; loading the source as a knowledge file doesn't make it reusable.
- **Per-conversation storage:** `window.storage` in its own chat. Data does not cross chats.
- **Bridges to the family-ops repo:**
  - `stockyard/eggs-log.csv` — daily counts. Format `date,count`.
  - `stockyard/flock-log.csv` — transaction log. Format `date,sign,count,category,breed,cohort_year,is_pet_layer,reason,notes,auto_generated,edited`.
  - `stockyard/breeds.csv` — user breed list with overrides and notes. Format `breed,last_used,eggs_per_year_override,notes`.

  These are the durable records the Stockyard agent will eventually read.

## Storage schema

The widget's `window.storage` keys are deliberately namespaced to match what Stockyard will own when the agent ships. Carry these names forward without changes.

**Path separator note:** keys use **colons**, not slashes. Slashes break the storage API. The v1 of this document used slashes — that was wrong; the actual code has always used colons.

```
stockyard:eggs-log         → { "YYYY-MM-DD": <int count>, ... }   // unchanged from v1
stockyard:flock-log        → [ <transaction>, ... ]                // v2 — live flock data
stockyard:flock-config     → { y1Count, y2Count }                  // v1 LEGACY — archive only
stockyard:breeds           → { "<breed name>": { lastUsed, overrides, userNotes } }
stockyard:reasons          → [ { text, lastUsed }, ... ]
stockyard:settings         → { showBandOnChart, showCards, supplementLighting,
                               realityFactorFloor, cohortRetirementAge, pruneYears }
```

**Transaction shape (`stockyard:flock-log` entries):**

```
{
  id: "tx_<timestamp>_<rand>",
  date: "YYYY-MM-DD",
  sign: 1 | -1,
  count: <int, always positive>,
  category: "layer" | "pullet" | "cockerel" | "rooster" | "meat" | "pet" | "other",
  breed: "<breed name>" | "",
  cohortYear: <int year> | null,    // null for non-cohort categories (meat, other)
  isPetLayer: <bool>,               // only meaningful for category="pet"
  reason: "<free text>",
  notes: "<free text>",             // meat-bird post-processing data goes here in v2
  edited: <bool>,
  autoGenerated: <bool>,            // true for pullet-promotion entries
  parentTxId: "<tx id>"             // set when autoGenerated=true, links to source pullet tx
}
```

**Current state is always computed**, never stored. `flockStateOn(date)` walks the transaction log up to and including `date`, groups by cohort key `category|breed|cohortYear|isPetLayer`, and sums signed counts. Empty cohorts drop out. This is the source of truth — there is no live "flock count" stored anywhere.

**Rule from family.md:** A blank entry in the egg log means "uncollected / unrecorded," NOT a real zero. The Bayer flock never has zero-egg days. Stockyard's analysis must treat missing dates as null, not zero, when computing averages and trend lines. The widget enforces this at entry time (confirm prompt on 0).

## Production model constants

Used for "expected today" calculations, vacuum projections, and tiered alerts. Refine after a full year of real data.

### Cohort production rates (eggs/hen/day at peak season)

| Year of lay | Rate |
|---|---|
| Y1 (first year laying) | 0.80 |
| Y2 | 0.65 |
| Y3 | 0.50 |
| Y4+ | 0.35 |

Year of lay = `current_year - cohort_year + 1`, clamped to 4. Cohort year is the year the bird arrived at the farm or was hatched on the farm.

### Seasonal modifiers (multiplier on cohort rate)

Two tables. Toggle exposed in Settings.

**Supplement lighting ON** (heat lamp keeps waterers from freezing, lights keep birds laying through winter — default state for Edelweiss):

| Month | Modifier |
|---|---|
| Jan | 0.80 |
| Feb | 0.80 |
| Mar | 0.85 |
| Apr | 0.95 |
| May | 0.95 |
| Jun | 1.00 |
| Jul | 1.00 |
| Aug | 0.95 |
| Sep | 0.85 |
| Oct | 0.70 |
| Nov | 0.80 |
| Dec | 0.80 |

**Supplement lighting OFF** (natural light only):

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

### Expected eggs for a date

```
expected_raw  = Σ over all active layer cohorts: count × cohortRate(cohort, date)
expected_day  = expected_raw × seasonal[month]
```

A "layer cohort" is any cohort with `category="layer"`, OR `category="pet"` with `isPetLayer=true`. Pullets, cockerels, roosters, meat birds, and non-laying pets do not contribute to expected.

### Year-over-year fallback (preferred when available)

Once 5+ logged days exist in the prior-year ±7-day window of the target date, the widget switches from the industry baseline above to the actual mean of those prior-year counts. YoY trumps industry. This kicks in automatically as the egg log accumulates a full year of data.

### Lay onset (pullet → layer promotion)

Per-breed in seeded data when known (e.g., Marans 24 weeks, Combless Leghorn 18 weeks, Brahma 28 weeks). Fallback is 5 months (≈21.5 weeks). Computed in months from arrival date for the auto-promotion calculation.

### Altitude caveat

Edelweiss Farms is at 9000 ft, Westcliffe CO, zone 4a. High altitude likely depresses winter production further than the seasonal modifier alone captures. Track Nov–Feb actuals carefully; if winter consistently underruns expected by >15% across a full year, Stockyard should add an altitude factor and surface it as a setting. The reality-factor on the Vacuum Projections card is the first place this will show up — if it's below the configured floor (default 70%) and the cause isn't molt or refresh timing, suspect altitude.

## Anomaly detection logic

Tiered alerts on the dashboard. Computed over a trailing 7-day window with at least 4 logged days. Compares actual average against the average of `expectedFor()` over the same window (which uses YoY when available, industry baseline otherwise).

| Shortfall | Tier | Label | Interpretation |
|---|---|---|---|
| < 25% | — | (no alert) | Seasonal noise. |
| 25–40% | 1 | Production dip — watch it | Weather, stress, or early molt onset. |
| 40–60% | 2 | Molt suspected | Half-flock molt fits this range. 6–8 week recovery typical. The Bayer operation refreshes ~50% of layers annually, so partial-flock molts are expected each fall. |
| > 60% | 3 | Bigger than a molt | Non-molt cause likely — water issue, predator, illness, feed quality, extreme weather. |

Tier 3 surfaces with red accent and an urgent label. Tier 1 and 2 are softer.

## Breed system

### Seeded library

~25 breeds carried in the widget code (`BREED_DATA` object). Included as of v2:

**User's current order:** Ginger Brown, Marans, Whiting True Blue, Whiting True Green, Combless Leghorn, Mille Fleur, Colorado Gold (meat), Jumbo Naked Neck (dual)

**Common varieties seeded for autocomplete:** Buff Orpington, Rhode Island Red, Barred Rock, Australorp, Wyandotte, Easter Egger, Olive Egger, Welsummer, Speckled Sussex, Brahma, Silkie, Cornish Cross, Red Ranger, Sapphire Gem, Black Star, Red Star, Cochin, Polish

Sources: Murray McMurray Hatchery, Whiting Farms, breed standards. Stockyard should treat seeded data as authoritative starting points but allow user overrides to take precedence.

### Per-breed schema

```
"<Breed Name>": {
  altNames: "<comma-separated alternates>",
  type: "layer" | "meat" | "dual",
  layerStats: { eggsPerYear, eggColor, eggSize } | null,
  meatStats: { matureWeightLb, daysToProcess, fcr, dressingPct } | null,
  matureWeightLb: { hen, rooster },
  layOnsetWeeks: <int> | null,
  productiveYears: <int> | null,
  coldHardy: <bool>,
  heatHardy: <bool>,
  temperament: "<free text>",
  origin: "<free text>"
}
```

### Fuzzy matching

Levenshtein similarity. Hardcoded threshold: **85%**. Used in autocomplete suggestions (typo recovery) and when a new breed is entered (surfaces possible-match suggestions in the confirm prompt). Revisit the threshold at the 2-year mark — flagged as a Stockyard hook.

### User overrides

```
stockyard:breeds → {
  "Marans": {
    lastUsed: "2026-10-15",
    overrides: { eggsPerYear: 175 },   // user's observed, replaces advertised in math
    userNotes: "Ours lay closer to 175. Heavy molt year 2."
  }
}
```

The override field replaces the advertised value in vacuum projection math. Original advertised data is preserved in `BREED_DATA` and shown alongside (struck through) in the breed data card UI. User notes are free text — Stockyard should preserve them verbatim, never paraphrase.

### Auto-prune

Breeds the user hasn't recorded a transaction with in N years drop off autocomplete suggestions (still searchable by exact name). Configurable: 1 / 2 / 5 / never. Default 2.

### New-breed handling

When a breed entered on a transaction doesn't match anything in the seeded library or user library, the widget surfaces possible fuzzy matches in a confirm prompt and asks the user to either pick a match or proceed adding the new breed. Stockyard should keep this as prompt-and-confirm initially; flagged as a hook to potentially go silent-add once the user's breed library has stabilized.

## Vacuum projections

What advertised breed data says *should* happen — sealed lab, no weather, no losses. Reality factor compares actual against this.

### Methodology

For each layer cohort active today:
- `advertised_per_bird` = breed's advertised eggs/year (or user override if set)
- `age_factor` = COHORT_RATES[year_of_lay] / COHORT_RATES[1] (ratio to Y1 best)
- `annual_per_cohort` = advertised_per_bird × age_factor × cohort_count

**Annual projection** = sum across cohorts. Naive, ignores season.

**YTD projection** = walk every day from Jan 1 to today, sum per-day expected using `(advertised / 365) × age_factor × seasonal[month] × count` for each cohort active on that day. Season-aware.

**Reality factor** = `(actual_YTD / projected_YTD) × 100`. Displayed as a percentage with color coding:
- ≥ floor: green
- floor × 0.7 to floor: yellow
- < floor × 0.7: red

Floor configurable (default 70%). Cohorts with no breed data don't contribute to projection but appear in the breakdown table with a `(no data)` flag.

### What this exposes

Discrepancies between marketing claims and farm reality. Over time, the reality factor surfaces:
- Altitude depression (consistent under-performance in winter)
- Breed-specific underperformance (Marans claim 200 but yours do 175 — record as override)
- Operational issues (predator pressure, feed quality) that wouldn't otherwise stand out

When Stockyard ships, the reality factor becomes a primary trend metric for ordering decisions.

## Transaction model & cohort math

### Why transactions, not snapshots

v1 used a snapshot model (one config: Y1 count, Y2 count). That worked for daily expected-eggs math but it lost history. Add 5 birds in March, lose 2 to a fox in May, sell 3 in September — the snapshot only ever shows "current count." No audit trail, no per-event recall, no breed-level granularity.

v2 records every change as a transaction. Current state is computed live by walking the log. Every change has a date, a reason, an optional note, and can be edited or deleted (edits tagged `(edited)` in the history).

### Cohort key

Cohorts are grouped by the tuple `category | breed | cohortYear | isPetLayer`. Two transactions with the same key sum together. Two transactions that differ on any one of those fields produce two separate cohorts.

This means: 5 Ginger Browns added in 2026 and 5 more Ginger Browns added in 2027 are *two cohorts* (different cohortYear), each on its own age track. Buying 3 Marans and 3 Easter Eggers in 2026 is two cohorts (different breeds). This is intentional — production rates and projections key off cohort year.

### Pullet auto-promotion

When a pullet cohort reaches its breed-specific lay onset (or 5-month fallback) measured from the transaction date, the widget writes two paired transactions on the promotion date:
- `-N pullets` of the same breed/cohortYear, reason "Auto-promoted (pullet → layer)"
- `+N layers` of the same breed/cohortYear, reason "Auto-promoted (pullet → layer)"

Both tagged `autoGenerated: true`, linked to the parent pullet transaction via `parentTxId`. Deleting the parent cascades the auto-generated children.

Stockyard should preserve this semantics. If structured pullet weigh-in / health data is added later, hang it off the auto-promotion event.

### Pet-layer flag

`category="pet"` with `isPetLayer=true` counts in production math (uses cohort-year rate, contributes to expected and to layer count), but stays categorized as "pet" for inventory purposes. Useful for Mille Fleur and similar ornamentals that lay sporadically but consistently.

## Stockyard hooks (the agent's inheritance)

Things the widget acknowledges it doesn't do. Documented in `Settings` with `[Stockyard hook]` flags where they're surfaced to the user, and listed in code with `// S1`, `// S2`, etc. comments.

| ID | Hook | Status in widget | Stockyard's job |
|---|---|---|---|
| S1 | Production curve auto-tuning | Hardcoded 0.80/0.65/0.50/0.35 | Compute actual cohort rates from historical egg log + flock log, replace constants per-cohort or per-farm |
| S2 | Post-butcher meat data capture | Free-text in transaction `notes` field | Structured fields: live weight, dressed weight, mortality count, days to process, computed FCR. Hangs off a `processing` event type. Powers user-override of advertised meat-bird data. |
| S3 | Feed math integration | Not tracked in widget | Owns feed cadence, intake records, feed totals. FCR computation requires this. |
| S4 | Silent breed adds | Prompt-and-confirm in v2 | Once user library is stable (2+ years), Stockyard may move new-breed adds to silent (skip the confirm prompt) and only surface unrecognized names that fuzzy-fail. |
| S5 | Fuzzy threshold | Hardcoded 85% | Revisit at 2-year mark. If catching too many false positives or too many misses, tune. May need per-context thresholds (breeds vs reasons). |
| S6 | Multi-species ops | Chicken-only | Pigs (feed cadence, weigh-ins, dewormings, slaughter timing). Turkeys (April raise tracking). Future additions. |
| S7 | Altitude factor | Not modeled | If winter under-performance is consistent across full year, derive altitude depression factor from Nov–Feb actuals vs expected, expose as setting. |

## Operational context

- **The whiteboard on the family fridge is the family's primary record.** Orange numbers in the upper-right of each cell = daily egg count. Started late 2025 when the layers came online. Photos of older months are in project knowledge.
- **Matt and Kalea both update the whiteboard.** The widget is the digital ledger; the whiteboard is the wall ledger. They should stay in sync. The whiteboard wins for daily ops; the widget wins for analytics.
- **Flock refresh cycle:** Roughly half the layers are replaced annually. At any given time, Y1 and Y2 cohorts are present in roughly equal numbers, with smaller Y3 and Y4+ holdovers and pets. Refresh timing typically tied to spring chick orders.
- **Edelweiss Farms, LLC** is the legal entity. Current operations: chickens (layers, meat, pets), pigs (seasonal), turkeys (spring raise). 98% operational tracking at this stage; 2% business hooks reserved for revenue/expense/depreciation when the LLC scales toward profitability.
- **Pet birds are real birds.** Mille Fleur ornamentals are counted as pets but lay enough eggs to matter. The `isPetLayer` flag exists for this case.

## When Stockyard ships

The agent inherits:

1. **The three CSV exports** at `stockyard/eggs-log.csv`, `stockyard/flock-log.csv`, `stockyard/breeds.csv` as the durable record
2. **This file's schema and constants** as the v2 starting design
3. **The seven hooks above** as its build queue
4. **Responsibility for the rest of the barn** — pigs, turkeys, slaughter records, feed math
5. **Responsibility for displacing the widget — or keeping it as the daily-entry UI** while the agent owns analytics and multi-species ops. Matt's call at that point. Most likely path: widget stays as the entry UI (it works, Kalea uses it), Stockyard owns everything else and reads the CSV exports plus runs its own data files.

Until then, the widget is the system.
