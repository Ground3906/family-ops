# Trip Cost Estimates

Standalone log for economic cost estimates on specific trips — fuel + wear + time. Separate from `punch-list/fuel-log.jsonl`, which is real per-fill receipt data only. This file is estimates/planning math, not receipts.

**Format:** One entry per estimate. Include route terrain split, vehicle, and the assumptions used (MPG by terrain, wear rate, hourly time value) so old estimates stay auditable if rates change later.

---

## 2026-07-07 — Half-Paved / Half-Dirt Round Trip

**Vehicle:** NV3500
**Route:** 14 mi paved + 14 mi rough dirt (one-way), round trip

**Assumptions:**
- Fuel: $3.50/gal. Paved 14 MPG, dirt 10 MPG.
- Wear: $0.30/mi paved, $0.60/mi dirt (rough terrain double rate).
- Time value: $20.00/hr baseline. Paved speed 50 MPH, dirt speed 20 MPH.

**One round trip (drop-off only):**

| Category | Cost |
|---|---|
| Fuel (2.4 gal total) | $8.40 |
| Wear (split-terrain) | $12.60 |
| Time (1.26 hrs) | $25.20 |
| **Total** | **$46.20** |

**Two round trips (drop & pick-up):**

| Category | Cost |
|---|---|
| Fuel | $16.80 |
| Wear | $25.20 |
| Time | $50.40 |
| **Total** | **$92.40** |

