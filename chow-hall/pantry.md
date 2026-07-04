# Chow Hall — Pantry

**Owner:** Chow Hall (🍴)
**Last updated:** 2026-07-03
**Data state:** STARTER EXAMPLES — not a real count. Real numbers load when meal planning earns it (Kalea ride-along checks + Costco receipts).

**Naming rule:** Name each item the plain way you'd say it out loud, and keep the name identical here and in `freezer.json` so the shopping list and recipes line up.

Pantry is the shelf-stable food, sorted by how you count it:

- **Canned** — counted by jars/cans, each with a size.
- **Bulk** — tracked by how full the bin is: full / half / low / out.
- **Packaged** — counted by the box, bag, or package.

**"Low at"** is the point where an item counts as low. Blank means Chow Hall hasn't learned that line yet — it asks Kalea once when the item comes up, then remembers. **"Restock to"** is the back-to-normal amount the shopping list buys up to.

Home-canned items (Kalea's jars) refill by re-canning, not a store run — season targets live in `canning-goals.md`.

**Source key:** `Costco` (bulk protein/freezer/paper), `Walmart` (everyday fill-in), `Safeway` (sale-cycle only), `Azure Standard` (monthly drop-point order — bulk dry staples: flour, grains, legumes, oils), `Edelweiss / home` (farm or home-canned).

---

## Canned

| Item | Size | On hand | Source | Low at | Restock to |
|---|---|---|---|---|---|
| Refried beans | 16 oz | 6 | Costco | — | 12 |
| Diced tomatoes | 28 oz | 8 | Costco | — | 12 |
| Black beans | 15 oz | 10 | Costco | — | 12 |
| Tomato sauce | 15 oz | 7 | Costco | — | 12 |
| Peaches | 1 qt | 9 | Edelweiss / home | — | re-can |
| Jalapeños | 1 pt | 14 | Edelweiss / home | — | re-can |
| Chicken stock | 1 qt | 6 | Edelweiss / home | — | re-can |

*Chicken stock also lives frozen in `freezer.json` — same item, two shelves. When the planner asks "do we have stock?" it adds both.*

---

## Bulk

Tracked by how full the bin is, not a count: **full / half / low / out.**

| Item | Status | Source | Restock to |
|---|---|---|---|
| All-purpose flour | full | Azure Standard | back to full |
| Sugar | half | Azure Standard | back to full |
| White rice | full | Azure Standard | back to full |
| Rolled oats | low | Azure Standard | back to full |
| Salt | full | Costco | back to full |
| Dried pinto beans | half | Azure Standard | back to full |

*Bulk-bin restocks route to Azure Standard by default — it's a monthly drop-point order, not an on-demand run. If a bin goes low between drops and can't wait, Costco or Walmart covers the gap.*

---

## Packaged

| Item | On hand | Low at | Restock to |
|---|---|---|---|
| Spaghetti | 6 | — | 8 |
| Cereal | 4 | — | 6 |
| Saltine crackers | 2 | — | 3 |
| Tortilla chips | 3 | — | 4 |
| Peanut butter | 2 | — | 3 |
| Coffee | 3 | — | 4 |
| Eggs (farm fresh) | — | — | — |
| Flour tortillas | — | — | — |
| Active dry yeast | — | — | — |

---

*Canning supplies (jars, lids, rings, pectin) are parked — they come back before peach season as their own tracked thing.*
