# payroll-widget.md — Payroll Screen Reference

**File:** `payroll-widget.jsx` (repo root). **Status:** working prototype, built and iterated with Jill in a Claude.ai session (React artifact environment). **Not yet ported to the Cockpit's live stack.**

---

## What this is

A standalone screen — commission job logging, deductions, jar balances (Give/Save/Spend), fixed monthly allowance accrual, and month-end payout — that sits alongside the Cockpit in navigation, not inside it. See `foreman.md` → "Screens Doctrine — Payroll" for the navigation/ownership contract.

Doctrine of record (rates, ratios, quality-gate policy) lives in `ledger/allowance.md`. This file and `payroll-widget.jsx` are the implementation; `ledger/allowance.md` is the source of truth if they ever drift.

---

## Tech-stack note for Tim (read before wiring this in)

**This file is not a drop-in for the Cockpit.** `cal-widget-current.html` and the rest of the Cockpit stack are vanilla HTML/JS, single-file, fetched with `{cache:'no-store'}` per `cal-widget.md`. `payroll-widget.jsx` was built in Claude.ai's artifact environment, which means:

- **React + JSX**, not vanilla JS. Needs a build step or a rewrite to plain JS/DOM to match the rest of the Cockpit.
- **`lucide-react`** for icons — swap for inline SVG or whatever icon approach the Cockpit already uses.
- **Tailwind utility classes** (core set only, no arbitrary values — colors are inline `style` for that reason). Cockpit doesn't currently use Tailwind; classes will need converting to the Cockpit's existing CSS approach, or Tailwind gets added as a dependency.
- **`window.storage.get/set(key, value, shared)`** — this is a Claude-artifact-only persistence API, it does not exist outside Claude.ai. Every call needs to be swapped for whatever the Cockpit's real persistence is (a JSON file synced through the repo, a small local server endpoint on the ThinkPad, browser storage, etc. — Tim's call based on how the rest of the Cockpit persists state, since Punch List/Chow Hall write through GitHub MCP to markdown/JSON rather than browser storage).

Bottom line: treat this as a **verified interaction design and business-logic spec**, not production code. The state machine (entries, jar totals, ratios, accrual/payout guards) is correct and tested through iteration with Jill — port the logic, not the storage calls.

---

## Data model summary

- **`entries`** — array of job/deduction tickets: `{ id, kidId, type: 'job'|'deduct', label, rate, unit, hours, amount, date }`. This is the append-heavy commission log.
- **`categories`** — `{ totals: { [kidId]: {give, save, spend} }, log: [...], lastAccrualMonth, lastPayoutMonth: {[kidId]: 'YYYY-MM'} }`. This is the jar state, fed by two actions:
  - **`addThisMonth()`** — fixed allowance accrual, guarded to once per calendar month household-wide.
  - **`runPayout(kidId)`** — splits that kid's net commission for the current month (jobs minus deductions, floored at $0) into the three jars using their own ratio (their give/save/spend rate numbers, normalized). Guarded per kid per month.
- **Deductions** net directly against the current month's commission total before payout — they never touch prior months' totals or the fixed-allowance portion of the jars.

Full rate table, per-kid ratios, and the quality-gate copy are in `ledger/allowance.md` — keep both in sync if either changes.

---

## Known open item — flag for Tim, not yet resolved

While pulling files for this handoff, found a real conflict worth a look before more calendar/chore work ships:

`cal-widget.md`'s `[CHORE]` entry doctrine (locked 2026-07-06) states dish-crew and zone data render as `[CHORE]` lines in `calendars.md`, folded into What's for Dinner — and claims `chow-hall.md` and `punch-list/chore-chart.md` were **already corrected** to match, dropping an earlier competing design that put crew info in `[MEAL]` `notes=`.

As of this session, `chow-hall.md` (Dish Crew Doctrine) and `punch-list/chore-chart.md` (Calendar Display section) both still describe the `[MEAL]` `notes=` approach — the correction described in `cal-widget.md` doesn't appear to have landed, or was overwritten by later work in this same session. Two files are now claiming different designs for the same fact. Per Foreman's Anti-Drift rule ("two agents claiming the same event = stop and surface"), this needs a human call on which design stands before the widget parser work for either gets built. Unrelated to Payroll itself — flagging here since it surfaced during this handoff and Tim will be in the codebase regardless.
