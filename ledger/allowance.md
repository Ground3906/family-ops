# Allowance & Payroll — Ledger

**Status:** Ledger agent is unbuilt. This file is a standalone placeholder until Ledger stands up. No agent definition, no automation — just doctrine + a running ledger that Al maintains on request. The interactive **Payroll** screen (React artifact, persistent storage) implements everything below; this file is its doctrine of record. Live day-to-day tracking (color-coded, per-kid tabs, rolling Give/Save/Spend balances) now lives in `allowance-ledger.xlsx` — this file stays the doctrine layer the two are kept in sync against.

**Last updated:** 2026-07-09

---

## Fixed Monthly Allowance (locked)

- **Amount:** Age in dollars per month. A kid's monthly allowance = their current age.
- **Split:** Dave Ramsey three-jar method — Give / Save / Spend. Ratios below are exact to each kid's established rate, not a rounded universal percentage.
- **Cadence:** Monthly, **posts at month's end, not the beginning.** Accrual is a manual action in Payroll ("Add this month"), guarded so it can't fire twice in the same month.
- **Payment method:**
  - **Wyatt & Molly** — Save and Spend still pay out directly to their bank accounts each month, same as always. **The Payroll tracker now also records Save/Spend for them** (previously Give-only) so their on-screen totals stay accurate once commission money — which does split three ways for them — lands in the same jars.
  - **Rileigh, Cullen, Emmitt** — all three jars cash-tracked, no bank accounts yet.

### Current Rates (by age)

| Kid | Age | Monthly | Give | Save | Spend |
|---|---|---|---|---|---|
| Wyatt | 14 | $14 | $1 | $3 | $10 |
| Molly | 10 | $10 | $1 | $2 | $7 |
| Rileigh | 7 | $7 | $1 | $1 | $5 |
| Cullen | 6 | $6 | $1 | $1 | $4 |
| Emmitt | 6 | $6 | $1 | $1 | $4 |

Rates reset automatically on birthday — update this table when a kid ages up. The same give/save/spend numbers double as each kid's commission split ratio (see below) — one rate table, two jobs.

### Outstanding as of 2026-07-04 (seed balance)

| Kid | Give | Save | Spend |
|---|---|---|---|
| Wyatt | $2 | $0 | $0 |
| Molly | $2 | $0 | $0 |
| Rileigh | $2 | $2 | $10 |
| Cullen | $2 | $2 | $8 |
| Emmitt | $2 | $2 | $8 |

Reflects May + June owed as of 2026-07-04. Historical seed point only — superseded by Running Jar Balances below.

---

## Running Jar Balances (live, rounded to nearest dollar)

*Mirrors the rolling Give/Save/Spend balances in `allowance-ledger.xlsx`. Wyatt and Molly's Save/Spend are real bank-jar totals now (deposits accumulate monthly, purchases and commission shares move against them) — not a "not tracked" placeholder anymore.*

| Kid | Give | Save | Spend | Total | As of |
|---|---|---|---|---|---|
| Wyatt | $3 | $9 | $25 | $37 | 2026-07-09 |
| Molly | $3 | $6 | **-$3** | $6 | 2026-07-09 |
| Rileigh | $4 | $4 | $9 | $16 | 2026-07-09 |
| Cullen | $3 | $3 | $6 | $12 | 2026-07-09 |
| Emmitt | $3 | $3 | $11 | $17 | 2026-07-09 |

---

## Commission — Extra Work (locked)

Commission is extra, on top of the fixed allowance — never a substitute for it. **Work is optional. No one is required to take a job.**

### Rate Menu (updated 2026-07-08)

| Job | Rate | Notes |
|---|---|---|
| Coop deep-clean | $5 | |
| Garden bed weeded | $2 | |
| Yard cleanup | $1 | |
| Take out diaper trash | $1 | |
| Snow shovel | $1 | |
| Wood chipping | $15/hr | Wyatt only |
| Clean the car | $2 | |
| Windows, per room | $1 | |
| Kitchen drawers organized | $1 | |
| Zone: Books & art table | $1 | |
| Zone: Downstairs | $1 | |
| Zone: Common room | $1 | |
| Mud room reset | $2 | |
| Unload dishes | $1 | |
| Unload car | $1 | |
| Flex / "Something else" | Set by Jill at log time | Off-menu job, custom amount |

### Quality Gate (locked)

- **"A job worth doing is worth doing right."** Posted rate pays out only when the job clears inspection.
- **"Not up to Al's standards? I don't think so, Tim. No stamp, no pay."** — no ticket gets logged for work that isn't done right. Redo before it's stamped.

### Deductions (locked)

- Logged from the same screen as job entries (Payroll → Log a Job → Deduction toggle), not a separate tool.
- Deducted for attitude/behavior during chores or Jill's requests. Amount + optional reason, both logged.
- Deductions net directly against **that month's commission earnings** before payout — they don't touch the fixed allowance jars or prior months' already-paid-out totals.

### Payout (locked)

- Runs at month's end, separate action from the fixed-allowance accrual.
- Each kid's net commission for the month (jobs minus deductions, floored at $0) splits into Give/Save/Spend using **that kid's own ratio** — the same give/save/spend proportions as their fixed allowance rate above.
- Split amounts add into the same jar totals the fixed allowance feeds. One set of totals per kid, two income streams.
- Guarded so a given kid's month can't be paid out twice; "Run all" processes every kid with a pending balance in one action.

### Commission Log

*Append-only, mirrors the `entries` data model from `payroll-widget.md` (kid, type job/deduct, label, rate, amount, date). Stamped = cleared the Quality Gate. Sits unpaid until month-end Payout is run by hand; once paid, mark Payout column with the month.*

| Date | Kid | Job | Amount | Stamped | Payout |
|---|---|---|---|---|---|
| 2026-07-09 | Rileigh | Car unload | $1.00 | Yes | Pending |
| 2026-07-09 | Rileigh | Car cleanout | $2.00 | Yes | Pending |
| 2026-07-09 | Rileigh | Unload dishes | $1.00 | Yes | Pending |
| 2026-07-09 | Molly | Unload car | $1.00 | Yes | Pending |
| 2026-07-09 | Cullen | Deduction — attitude | **-$1.00** | — | Pending |
| 2026-07-09 | Emmitt | Deduction — attitude | **-$1.00** | — | Pending |

**Unpaid commission totals this month:** Rileigh $4.00, Molly $1.00, Cullen -$1.00, Emmitt -$1.00. None of this is in Spend/Save/Give balances yet — it moves there only when Payout runs.

---

## Expenditures — Store Purchases (Spend)

*Tracks money kids actually spend so Spend balances stay accurate against real life. Entries are tagged by store and consolidated per kid per trip — total and item list, not itemized per purchase. Amounts round to the nearest dollar. Comes out of Spend only, unless noted otherwise.*

| Date | Kid | Store | Items | Total (rounded) |
|---|---|---|---|---|
| 2026-07-09 | Molly | Walmart | Tic tacs, Dr Pepper, candy | $11 |
| 2026-07-09 | Molly | Amazon | Dumpling (plush) | $14 |
| 2026-07-09 | Wyatt | Walmart | Slim Jims, Celsius, Dr Pepper | $5 |
| 2026-07-09 | Rileigh | Walmart | Skittles, Tic Tacs | $9 |
| 2026-07-09 | Cullen | Walmart | Handcuffs (toy) | $5 |

**Total expenditures logged: $44** — all Spend money.

**How this works:**
- Al logs a row per kid per trip/order — store tag, item list, total rounded to the nearest dollar. Doesn't need to reconcile to the penny against individual items.
- Comes out of Spend only, unless Jill says otherwise for a specific purchase.
- Wyatt and Molly's Spend is a real running bank-jar total now (see Running Jar Balances) — a purchase can and does take it negative, same as the cash-tracked kids. Molly's two July purchases ($11 + $14) put her Spend at -$3.
- If a purchase would take any kid's Spend balance negative, that's expected and gets logged as-is — flag to Jill only if it looks like a mistake, not because it's negative.

---

## Notes

- Update the rate table when a kid has a birthday — commission split ratios move with it automatically since they're derived from the same numbers.
- Update the Rate Menu here first if a job is added, removed, or repriced; Payroll's menu should match this table.
- If Ledger stands up as a full agent later, this file becomes its seed data — don't rebuild from scratch.
- Commission Log and Expenditures Log are both manual/append-only until Payroll widget or Ledger agent goes live — Al maintains both on request, same pattern as everything else in this file.
- `allowance-ledger.xlsx` is now the live day-to-day tracker (color-coded by kid, five individual kid tabs, rolling Give/Save/Spend balances). Al keeps this file's tables in sync with it after each xlsx update.
