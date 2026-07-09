# Allowance & Payroll — Ledger

**Status:** Ledger agent is unbuilt. This file is a standalone placeholder until Ledger stands up. No agent definition, no automation — just doctrine + a running ledger that Al maintains on request. The interactive **Payroll** screen (React artifact, persistent storage) implements everything below; this file is its doctrine of record.

**Last updated:** 2026-07-09

---

## Fixed Monthly Allowance (locked)

- **Amount:** Age in dollars per month. A kid's monthly allowance = their current age.
- **Split:** Dave Ramsey three-jar method — Give / Save / Spend. Ratios below are exact to each kid's established rate, not a rounded universal percentage.
- **Cadence:** Monthly. Accrual is a manual action in Payroll ("Add this month"), guarded so it can't fire twice in the same month.
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

### Outstanding as of 2026-07-04 (seed balance in Payroll)

| Kid | Give | Save | Spend |
|---|---|---|---|
| Wyatt | $2 | $0 | $0 |
| Molly | $2 | $0 | $0 |
| Rileigh | $2 | $2 | $10 |
| Cullen | $2 | $2 | $8 |
| Emmitt | $2 | $2 | $8 |

Reflects May + June owed as of 2026-07-04. July onward runs through Payroll's "Add this month" action. **Superseded going forward by Running Jar Balances below** — this table stays as the historical seed point.

---

## Running Jar Balances (live)

*Al updates this table by hand after every Commission Log entry, every Expenditures Log entry, and every monthly accrual — until Payroll widget or Ledger agent is live and doing it automatically. This is the current-truth balance; the "Outstanding" table above is the fixed starting point it was built from.*

*Wyatt and Molly's Spend runs through their bank accounts, not a cash jar — a negative here means money owed against that account, not a jar shortfall. Pending Commission is stamped work sitting in the Commission Log below, not yet folded into Spend/Save/Give — it moves into those jars only when month-end Payout runs.*

| Kid | Give | Save | Spend | Pending Commission (unpaid) | As of |
|---|---|---|---|---|---|
| Wyatt | $2 | $0 | **-$5** (owed via bank) | $0 | 2026-07-09 |
| Molly | $2 | $0 | **-$11** (owed via bank) | $0 | 2026-07-09 |
| Rileigh | $2 | $2 | $1.00 | **$3.00** | 2026-07-09 |
| Cullen | $2 | $2 | $3.00 | $0 | 2026-07-09 |
| Emmitt | $2 | $2 | $8 | $0 | 2026-07-09 |

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

*Append-only, mirrors the `entries` data model from `payroll-widget.md` (kid, type job/deduct, label, rate, amount, date) so this manual log can port straight into Payroll once it's wired into the Cockpit. Stamped = cleared the Quality Gate. Sits here unpaid — feeding the "Pending Commission" column in Running Jar Balances above — until month-end Payout is run by hand; once paid, mark Payout column with the month and it drops out of Pending.*

| Date | Kid | Job | Rate | Qty/Hrs | Amount | Stamped | Payout |
|---|---|---|---|---|---|---|---|
| 2026-07-09 | Rileigh | Car unload | — | 1 | $1.00 | Yes | Pending |
| 2026-07-09 | Rileigh | Car cleanout | — | 1 | $2.00 | Yes | Pending |

**Rileigh unpaid commission total: $3.00** — this is the source of the $3.00 in Pending Commission above. It isn't in her Spend/Save/Give balances yet; it moves there only when Payout runs for her.

---

## Expenditures — Store Purchases (Spend)

*Tracks money kids actually spend so Spend balances stay accurate against real life. Entries are tagged by store and consolidated per kid per trip — total and item list, not itemized per purchase. Amounts round to the nearest dollar.*

| Date | Kid | Store | Items | Total (rounded) | Spend Balance After |
|---|---|---|---|---|---|
| 2026-07-09 | Molly | Walmart | Tic tacs, Dr Pepper, candy | $11 | **-$11** (owed via bank) |
| 2026-07-09 | Wyatt | Walmart | Slim Jims, Celsius, Dr Pepper | $5 | **-$5** (owed via bank) |
| 2026-07-09 | Rileigh | Walmart | Skittles, Tic Tacs | $9 | $1.00 |
| 2026-07-09 | Cullen | Walmart | Handcuffs (toy) | $5 | $3.00 |

**Total expenditures this trip: $30** (Molly $11 + Wyatt $5 + Rileigh $9 + Cullen $5) — all Spend money.

**How this works:**
- Al logs a row per kid per trip — store tag, item list, total rounded to the nearest dollar. Doesn't need to reconcile to the penny against individual items.
- Rileigh and Cullen's totals come straight out of their tracked cash Spend jar in Running Jar Balances.
- Wyatt and Molly have no cash Spend jar — their Spend money lives in the bank, so a purchase shows as a **negative balance** (money owed against that account) rather than a jar debit. Still flagged: give Al a starting bank balance for either of them and this can track a real running total instead of resetting to $0/-purchase each time.
- If a purchase would take Rileigh, Cullen, or Emmitt's tracked cash Spend jar negative, flag it to Jill rather than logging it — that rule doesn't apply to Wyatt/Molly since bank-based Spend is expected to run negative between deposits.

---

## Notes

- Update the rate table when a kid has a birthday — commission split ratios move with it automatically since they're derived from the same numbers.
- Update the Rate Menu here first if a job is added, removed, or repriced; Payroll's menu should match this table.
- If Ledger stands up as a full agent later, this file becomes its seed data — don't rebuild from scratch.
- Commission Log and Expenditures Log are both manual/append-only until Payroll widget or Ledger agent goes live — Al maintains both on request, same pattern as everything else in this file.
