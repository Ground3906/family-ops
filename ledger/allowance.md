# Allowance & Payroll — Ledger

**Status:** Ledger agent is unbuilt. This file is a standalone placeholder until Ledger stands up. No agent definition, no automation — just doctrine + a running ledger that Al maintains on request. The interactive **Payroll** screen (React artifact, persistent storage) implements everything below; this file is its doctrine of record.

**Last updated:** 2026-07-08

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

Reflects May + June owed as of 2026-07-04. July onward runs through Payroll's "Add this month" action.

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

---

## Notes

- Update the rate table when a kid has a birthday — commission split ratios move with it automatically since they're derived from the same numbers.
- Update the Rate Menu here first if a job is added, removed, or repriced; Payroll's menu should match this table.
- If Ledger stands up as a full agent later, this file becomes its seed data — don't rebuild from scratch.
