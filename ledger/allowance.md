# Allowance & Payroll -- Ledger

**Status:** Live Payroll screen deployed (`payroll-current.html`, served by ThinkPad at :8080). `payroll/payroll-data.json` in the repo is the live tracker -- this file is the doctrine layer it runs against. `allowance-ledger.xlsx` is now a historical archive (frozen as of 2026-07-09); do not update it going forward.

**Last updated:** 2026-07-22

---

## Fixed Monthly Allowance (locked)

- **Amount:** Age in dollars per month. A kid's monthly allowance = their current age.
- **Split:** Dave Ramsey three-jar method -- Give / Save / Spend. Ratios below are exact to each kid's established rate, not a rounded universal percentage.
- **Cadence:** Monthly, **posts at month's end, not the beginning.** Accrual is a manual action in Payroll ("Add this month"), guarded so it can't fire twice in the same month.
- **Payment method:**
  - **Wyatt & Molly** -- Save and Spend still pay out directly to their bank accounts each month, same as always. The Payroll tracker records Save/Spend for them so their on-screen totals stay accurate once commission money -- which does split three ways for them -- lands in the same jars.
  - **Rileigh, Cullen, Emmitt** -- all three jars cash-tracked, no bank accounts yet.

### Current Rates (by age)

| Kid | Age | Monthly | Give | Save | Spend |
|---|---|---|---|---|---|
| Wyatt | 14 | $14 | $1 | $3 | $10 |
| Molly | 10 | $10 | $1 | $2 | $7 |
| Rileigh | 8 | $8 | $1 | $1 | $6 |
| Cullen | 6 | $6 | $1 | $1 | $4 |
| Emmitt | 6 | $6 | $1 | $1 | $4 |

Rates reset on birthday -- update this table when a kid ages up. The same give/save/spend numbers double as each kid's commission split ratio -- one rate table, two jobs.

### Age-Up Doctrine (locked 2026-07-22)

When a kid's birthday bumps the monthly total, the extra dollar defaults to **Spend** unless Matt or Jill call it differently at the time. This applies to every future age-up. Document the call here when it happens.

- **Rileigh 7 -> 8 (2026-06-28):** Extra dollar to Spend. Effective with July 2026 month-end accrual (7/31). June accrual posted at the old $7 rate and stays.

---

## Running Jar Balances (live)

*Source of truth is `payroll/payroll-data.json`. These numbers reflect the June-end reconstructed seed -- July commission sits as pending entries in the Payroll screen and will post to jars at month-end payout (7/31). July fixed allowance also posts 7/31.*

| Kid | Give | Save | Spend | Total | As of |
|---|---|---|---|---|---|
| Wyatt | $2 | $6 | $15 | $23 | 2026-07-22 (seed) |
| Molly | $2 | $4 | -$11 | -$5 | 2026-07-22 (seed) |
| Rileigh | $2 | $2 | $1 | $5 | 2026-07-22 (seed) |
| Cullen | $2 | $2 | $3 | $7 | 2026-07-22 (seed) |
| Emmitt | $2 | $2 | $8 | $12 | 2026-07-22 (seed) |

After 7/31 payout runs: Rileigh +$4, Molly +$1, Cullen/Emmitt floor to $0 (deductions exceed commission).

---

## Commission -- Extra Work (locked)

Commission is extra, on top of the fixed allowance -- never a substitute for it. **Work is optional. No one is required to take a job.**

### Rate Menu (updated 2026-07-22)

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
- **"Not up to Al's standards? I don't think so, Tim. No stamp, no pay."** -- no ticket gets logged for work that isn't done right. Redo before it's stamped.

### Deductions (locked)

- Logged from the same screen as job entries (Payroll -> Log a Job -> Deduction toggle).
- Deducted for attitude/behavior during chores or Jill's requests.
- Deductions net directly against **that month's commission earnings** before payout -- they don't touch the fixed allowance jars or prior months' already-paid-out totals.

### Payout (locked)

- Runs at month's end, separate action from the fixed-allowance accrual.
- Commission sits as pending entries all month. It does **not** touch jar totals until Payout is run.
- Each kid's net commission for the month (jobs minus deductions, floored at $0) splits into Give/Save/Spend using **that kid's own ratio** -- the same give/save/spend proportions as their fixed allowance rate above.
- Split amounts add into the same jar totals the fixed allowance feeds. One set of totals per kid, two income streams.
- Guarded so a given kid's month can't be paid out twice; "Run all" processes every kid with a pending balance in one action.
- **Floor rule:** net commission cannot go below $0. Deductions that exceed commission for a month are absorbed -- they do not carry forward or touch jar totals.

### Commission Log (July 2026 -- active)

*Entries below are pending 7/31 payout. These are also seeded into `payroll/payroll-data.json` as the July entries. After the Payroll screen ships, all new commission is logged there -- this table is no longer maintained manually.*

| Date | Kid | Job | Amount | Stamped | Payout |
|---|---|---|---|---|---|
| 2026-07-09 | Rileigh | Car unload | $1.00 | Yes | Pending 7/31 |
| 2026-07-09 | Rileigh | Car cleanout | $2.00 | Yes | Pending 7/31 |
| 2026-07-09 | Rileigh | Unload dishes | $1.00 | Yes | Pending 7/31 |
| 2026-07-09 | Molly | Unload car | $1.00 | Yes | Pending 7/31 |
| 2026-07-09 | Cullen | Deduction -- attitude | -$1.00 | -- | Pending 7/31 |
| 2026-07-09 | Emmitt | Deduction -- attitude | -$1.00 | -- | Pending 7/31 |

**July net at 7/31 payout:** Rileigh $4.00, Molly $1.00, Cullen $0 (floored), Emmitt $0 (floored).

---

## Expenditures -- Store Purchases (Spend)

*All entries below are historical reference. After Payroll screen ships, expenditure tracking moves to a future Ledger agent session -- not in Payroll scope. Keep recording purchases here until Ledger builds.*

| Date | Kid | Store | Items | Total (rounded) |
|---|---|---|---|---|
| 2026-07-09 | Molly | Walmart | Tic tacs, Dr Pepper, candy | $11 |
| 2026-07-09 | Molly | Amazon | Dumpling (plush) | $14 |
| 2026-07-09 | Wyatt | Walmart | Slim Jims, Celsius, Dr Pepper | $5 |
| 2026-07-09 | Rileigh | Walmart | Skittles, Tic Tacs | $9 |
| 2026-07-09 | Cullen | Walmart | Handcuffs (toy) | $5 |

---

## Notes

- Update the rate table when a kid has a birthday -- apply the age-up doctrine above, then update commission split ratios automatically since they derive from the same numbers.
- Update the Rate Menu here first if a job is added, removed, or repriced; the Payroll screen's menu must match.
- `allowance-ledger.xlsx` is frozen as a historical archive as of 2026-07-09. Do not update it. The running source of truth is `payroll/payroll-data.json`.
- If Ledger stands up as a full agent later, this file becomes its seed data -- don't rebuild from scratch.
- **Fixed allowance Due posts at month's end (e.g. 7/31), not day one of the month.** Commission entries are logged immediately when earned; jar totals don't move until Payout is run at month's end.
