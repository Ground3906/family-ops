# Allowance — Ledger (placeholder)

**Status:** Ledger agent is unbuilt. This file is a standalone placeholder until Ledger stands up. No agent definition, no automation — just doctrine + a running ledger that Al maintains on request.

**Last updated:** 2026-07-04

---

## Doctrine (locked)

- **Amount:** Age in dollars per month. A kid's monthly allowance = their current age.
- **Split:** Dave Ramsey three-jar method — Give / Save / Spend, roughly 10% / 20% / 70%, rounded to whole dollars (Give jar floors at $1). Totals hold exact to the age amount.
- **Cadence:** Monthly.
- **Payment method:**
  - **Wyatt & Molly** — Save and Spend paid directly to their bank accounts. **Give jar is cash-tracked here**, not banked.
  - **Rileigh, Cullen, Emmitt** — all three jars (Give/Save/Spend) cash-tracked here. No bank accounts yet.

## Current Rates (by age)

| Kid | Age | Monthly | Give | Save | Spend |
|---|---|---|---|---|---|
| Wyatt | 14 | $14 | $1 | $3 | $10 |
| Molly | 10 | $10 | $1 | $2 | $7 |
| Rileigh | 7 | $7 | $1 | $1 | $5 |
| Cullen | 6 | $6 | $1 | $1 | $4 |
| Emmitt | 6 | $6 | $1 | $1 | $4 |

Rates reset automatically on birthday — update this table when a kid ages up.

---

## Running Ledger

Status per kid per month. `paid` = settled in full for that month (bank + cash jars, whichever apply). `owed` = still outstanding.

### 2026

| Month | Wyatt (Give) | Molly (Give) | Rileigh (all 3) | Cullen (all 3) | Emmitt (all 3) |
|---|---|---|---|---|---|
| May | owed — $1 | owed — $1 | owed — $7 | owed — $6 | owed — $6 |
| June | owed — $1 | owed — $1 | owed — $7 | owed — $6 | owed — $6 |
| July | — | — | — | — | — |

**Wyatt & Molly Save/Spend:** paid current via bank as of 2026-07-04, no cash tracking needed.

### Outstanding as of 2026-07-04

| Kid | Owed |
|---|---|
| Rileigh | $14 |
| Cullen | $12 |
| Emmitt | $12 |
| Wyatt (Give only) | $2 |
| Molly (Give only) | $2 |
| **Total cash owed** | **$42** |

---

## Notes

- Update this file when a payout is made — move month from `owed` to `paid`, zero out the outstanding table.
- Update the rate table when a kid has a birthday.
- If Ledger stands up as a full agent later, this file becomes its seed data — don't rebuild from scratch.
