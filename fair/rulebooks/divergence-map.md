# Divergence Map — Custer County Fair Book vs. Colorado State Fair

Deliverable 1 of the Fair Rulebooks Charter (`fair/rulebooks/charter.md`). v1 audience is Matt's own parse — this is the staging artifact for a board conversation, not the board-facing document itself. The line-by-line board version is a later conversion pass generated from this master with no re-research.

**Sources compared:** county — `fair/rulebooks/extracts/2026-custer-county-fair-book.md` (2026 Custer County Fair Book, the source of truth). State — `fair/rulebooks/extracts/csf-2026-general-competition-requirements.md`, `csf-2026-exhibitor-handbook.md` (689-page complete handbook, not a TOC), and the Colorado 4-H documents under `fair/rulebooks/extracts/co4h-*.md` for the departments the county book itself sources from 4-H directly (Shooting Sports, Dog).

**Classification vocabulary:** DIVERGED (state has a rule, county has a different one) · CONFLICT (the two actively contradict) · SILENT (state has a rule, county doesn't address it) · LOCAL-ONLY (county has a rule/mechanism with no state analog) · ALIGNED (county correctly mirrors state).

**Disposition lanes (tee-up only — board decides):** ADOPT-STATE · KEEP-LOCAL · DISCUSS.

## Triage Index

| Department | DIVERGED | CONFLICT | SILENT | LOCAL-ONLY | ALIGNED | Total |
|---|---|---|---|---|---|---|
| General / cross-cutting | — | — | 1 | — | — | 1 |
| Shooting Sports | 1 | — | — | — | — | 1 |
| Market Livestock (species-specific) | 4 | — | — | — | — | 4 |
| Market Livestock (cross-species) | — | — | 2 | — | — | 2 |
| Companion Animal (Dog) | — | — | 1 | — | — | 1 |
| Show Ethics | 1 | — | — | — | — | 1 |
| Livestock Sale | — | — | 2 | — | — | 2 |
| Protest & Appeals (Admin) | 2 | — | — | — | — | 2 |
| Poultry | — | — | 1 | — | — | 1 |
| Open Division | — | 1 | — | 1 | — | 2 |
| Judging Systems | — | — | — | — | 1 | 1 |
| **Total** | **8** | **0** | **8** | **1** | **1** | **18** |

No CONFLICT-classified item in this pass beyond the one Open Division nuance noted below — the two books diverge mainly by silence and local addition, not active contradiction. Read that as good news about the starting position, not a clean bill of health: several SILENT items sit on real stakes (health certs, sale-forfeiture consequences).

## Mechanics flag: citation integrity (not a classification-vocabulary item, tracked separately)

All four direct Colorado 4-H URLs cited by name in the county book (`co4h.colostate.edu/ss/ss-rulebook.pdf`, `.../statefair/StateFairExhibitReq.pdf`, `.../statefair/StateFairContestReq-Dog.pdf`, `.../statefair/StateFairContestReq.pdf`) are dead — co4h.colostate.edu rebuilt on a new CMS and every one of them now 302-redirects to a generic resources landing page (HTTP 200, not a 404, so nobody notices until they actually read the destination). Live replacements were located and archived for all but the Poultry/Turkey document, which does not currently exist at the state level at all (see POULTRY-01). This needs fixing in the county book regardless of anything else in this mission: adopt-by-reference only works if the reference resolves. Rule-mechanics.md carries the drafting lesson (link to stable hub pages, not deep PDF paths).

---

## Part 1: Heavy Hitters

Posture-level comparison of load-bearing rule areas. Final list derives from what actually surfaced in both books.

| Area | State posture | County posture | Gap size | Disposition |
|---|---|---|---|---|
| Eligibility & residency | Age 8–18 (Dec 31 cutoff) + full-time CO resident + ≤2 consecutive weeks outside CO between nomination and Fair's end (market livestock); CO residency required for Creative Arts entries | Matches age bands throughout; silent on the residency-continuity rule for livestock; Open Division explicitly allows cross-county residents (single-fair-in-state restriction instead) | Small–medium | DISCUSS |
| Ownership / possession deadlines | CVI (health cert) dated ≤7 days pre-arrival, all species; per-species CSU Extension nomination/tagging deadlines | "Majority of care from official weigh-in forward" framing; species tagging at-or-before weigh-in; no CVI-style dated health-cert deadline anywhere | Medium | DISCUSS |
| Weigh-in & weight-class construction | Bounded windows per species (beef 1,050+ lbs no max; swine 235–300; sheep 110–165; goat 55–115) plus a post-placement audit: top-5 finishers re-weighed, **>5% deviation = disqualified** | Bounded on swine only (220–290); beef/sheep/goat state a floor with no ceiling; goat adds a **local-only "must gain ≥5 lbs" rule** with no state counterpart; pre-declaration accommodation re-weigh only (2 tries before weigh-in closes), no post-placement audit at all | **Large** — richest single area | DISCUSS |
| Health & vet requirements | CVI ≤7 days all species; pseudorabies test for swine unless CO-origin + current health cert; Scrapie Flock ID mandatory sheep ≥18 months; CSU Avian Health Team inspects poultry on arrival | Scrapie tags required sheep **and** goats (matches/exceeds federal baseline); no general dated health-certificate requirement stated for market livestock | Medium–large | DISCUSS |
| Drug residue & show ethics | Zero-tolerance carcass drug-residue standard; ractopamine is the only FDA-approved beta-agonist (0-day withdrawal); 13-item enumerated closed list of "Unethically Fitted Livestock" practices | 4-item general unethical-practices list (doctoring/doping, ice packs/refrigerants, altering hair/wool structure, random drug testing); USDA Wholesome Meat Act incorporated by reference for the sale specifically | Medium (completeness gap, not philosophy) | ADOPT-STATE (lean) |
| Sale rules | Terminal sale, 7% commission on gross; Grand/Reserve/Division Champions **must** sell (3 tiers); 30-minute withdrawal window; no-show = forfeit **all** awards + **3-year exhibition ban**; explicit per-species sale quotas | "Grand and Reserve Grand Champions will sell" (2 tiers, no separate Division-Champion tier named); 2-species-plus-1-meat-pen exhibitor cap; no stated commission %; no-show consequence falls to the general disciplinary ladder rather than a sale-specific rule | Large | DISCUSS |
| Judging systems | Danish used in exhibit-standard contexts, American in competitive-placing contexts (standard national 4-H convention); CSF's own General Competition Requirements is silent on ribbon methodology entirely, deferring to division documents | Danish for Consumer Science/General projects and Dog obedience; American for livestock, showmanship, Cat, Rabbit, Llama, Horse, and Open Division — correctly mirrors the standard dual-system convention | None | N/A — ALIGNED |
| Protest & appeals | $300 bond; 24-hour deadline for livestock; chain of six sequential 15-day clocks running to a 4-person hearing panel | $50 protest / $100 appeal; 24-hour protest deadline (matches state's 24-hour framing exactly); only an **8-hour** appeal window; single-tier Fair Board executive panel as final authority, no multi-stage hearing-panel process | Large — mainly fee-scale and appeal-window length | DISCUSS |

---

## Part 2: Findings

### General / Cross-Cutting

**GEN-01 · SILENT · DISCUSS**
County text: general market-livestock eligibility rules require 4-H/FFA membership and age bands, with no residency-continuity clause.
State text: exhibitors must be "full-time Colorado residents" with no more than two consecutive weeks outside the state between nomination and the Fair's end (CSF Exhibitor Handbook, Market Livestock cross-species rules).
Archaeology note: this rule matters more to a state fair drawing from the whole state than a single-county fair where residency is close to self-evident locally, which may be exactly why it was never written down. Worth confirming that's the actual reason rather than an oversight.
Mechanics tag: none.

### Shooting Sports

**SHOOT-01 · DIVERGED · KEEP-LOCAL (suggested)**
County text: "Custer County does not use the Orion scorecards, the county scorecards will be provided on the day of the contest."
State text: Colorado 4-H Shooting Sports Rulebook specifies the Orion Scoring System for rifle, air rifle, pistol, shotgun, and archery, with discipline-specific tie-breaker hierarchies.
Archaeology note: this is a self-declared, deliberate local opt-out already documented in the county's own book, not a discovered gap — almost certainly a small-range logistics choice (Orion requires software/hardware overhead disproportionate to a one-day county contest). Only DIVERGED item where the county book states its own reasoning implicitly through the phrasing.
Mechanics tag: none.

### Market Livestock — species-specific

**BEEF-01 · DIVERGED · DISCUSS**
County text: "Steers and heifers will weigh a minimum of 1,000 lbs. in order to sell."
State text: CSF Market Beef minimum is 1,050 lbs, no stated maximum.
Archaeology note: a 50 lb gap at the floor. Could reflect Custer's smaller/younger exhibitor base producing lighter finished animals, or could simply be an unreviewed legacy number.
Mechanics tag: none.

**SWINE-01 · DIVERGED · DISCUSS**
County text: hogs "must weigh a minimum of 220 lbs. and a maximum of 290 lbs."
State text: CSF Market Hogs window is 235–300 lbs.
Archaeology note: both floor and ceiling shifted, not just one end — suggests a deliberately different target weight range for the county show rather than a single stale number.
Mechanics tag: none.

**SHEEP-01 · DIVERGED · DISCUSS**
County text: "Lambs must weigh a minimum of 105 lbs" — no maximum stated anywhere in the section.
State text: CSF Market Lambs window is 110–165 lbs (bounded both ends).
Archaeology note: county's unbounded ceiling is the more consequential half of this gap — a lamb well above 165 lbs would be barred from CSF competition but currently has no stated barrier at the Custer show.
Mechanics tag: none.

**GOAT-01 · DIVERGED · DISCUSS**
County text: "Must weigh a minimum of 55 lbs" plus a local-only clause: "all market goat weights must increase at least 5 pounds from the beginning weigh-in weight to the end weight established at county fair."
State text: CSF Market Goats window is 55–115 lbs (bounded); no gain-rate requirement anywhere in the CSF material reviewed.
Archaeology note: the floor matches exactly (55 lbs) — this reads as CSF's number adopted at some point, then the county layered its own gain-rate integrity check on top rather than diverging on the base number. The state's ceiling (115 lbs) was apparently not carried over.
Mechanics tag: none.

### Market Livestock — cross-species

**LIVESTOCK-01 · SILENT · DISCUSS**
County text: re-weigh policy allows animals under/over the class weight to "re-weigh two additional times prior to the end of weigh in" — a pre-declaration accommodation.
State text: CSF re-weighs the top 5 finishers in each class **after** placing; **>5% deviation from declared weight = disqualification**, no second chance.
Archaeology note: these are two different mechanisms serving two different purposes — the county's is exhibitor-friendly (helps hit make-weight before it counts), the state's is an anti-fraud integrity check (catches misrepresented weight after the fact). The county has the first but not the second; adopting the second wouldn't require removing the first.
Mechanics tag: none.

**LIVESTOCK-02 · SILENT · DISCUSS**
County text: no general dated health-certificate requirement for market livestock (Scrapie tags for sheep/goats are the only stated animal-health documentation).
State text: CVI (Certificate of Veterinary Inspection) dated ≤7 days before arrival, required for all species.
Archaeology note: plausible for a single-day-drive-in county fair where animals arrive from known local premises, but this is exactly the kind of rule a disease event (see POULTRY-01's HPAI context) would make the board wish it had in writing beforehand rather than after.
Mechanics tag: none.

### Companion Animal — Dog

**DOG-01 · SILENT · DISCUSS**
County text: "Proof of approved effective vaccination for rabies must be available for inspection on show date" — silent on whether titer-based immunity proof satisfies this.
State text: the current Colorado 4-H Dog document requires a rabies certificate and does not accept titers as substitute proof.
Archaeology note: low-frequency but real exposure — a vet-recommended titer test (increasingly common for dogs with vaccine-reaction history) could read as compliant locally while failing the state standard outright. Worth a one-line clarification either way.
Mechanics tag: county wording is permissive-by-omission where state wording is exclusionary-by-name; the gap is entirely in what's *not* said.

### Show Ethics

**ETHICS-01 · DIVERGED · ADOPT-STATE (lean)**
County text: four enumerated unethical practices (doctoring/doping/injections for fill, ice packs/refrigerants, altering hair/wool structure beyond trimming/blocking, random drug testing).
State text: CSF's "Unethically Fitted Livestock" is a 13-item enumerated closed list (adds, among others: hide cutting, artificial tail-heads, and other named cosmetic-alteration practices not covered by the county's shorter list).
Archaeology note: same philosophy, different completeness. The gap is enumeration, not disagreement — a case where adopting the fuller list closes real loopholes at low local cost, which is why this is the one lean-ADOPT-STATE call in this pass rather than a flat DISCUSS.
Mechanics tag: closed-list vs. shorter closed-list — the wording itself (specific enumerated practices) is the entire gap here.

### Livestock Sale

**SALE-01 · SILENT · DISCUSS**
County text: no sale-specific consequence stated for an animal that qualifies for sale but isn't presented; general disciplinary ladder (warning → parent notice → removal → premium penalty → behavior contract → law enforcement referral → suspension/expulsion) is the only applicable mechanism.
State text: CSF states a specific consequence — forfeiture of **all** awards/premiums/buybacks earned at the Fair, plus a **3-year exhibition ban**, for failing to show a qualified sale animal.
Archaeology note: the county's general ladder can reach a similar outcome case-by-case, but there's no printed floor the way CSF has one — a board wanting predictable, evenly-applied consequences here would need to write one.
Mechanics tag: none.

**SALE-02 · SILENT · DISCUSS**
County text: no stated sale commission percentage anywhere in the Livestock Sale section.
State text: CSF states a flat 7% commission on gross sale proceeds.
Archaeology note: plausibly intentional — a locally-run sale committee may set commission by year by whatever agreement covers costs, rather than printing a fixed number in the book. Worth confirming that's the actual reason (source-before-seed: don't assume, ask).
Mechanics tag: none.

### Protest & Appeals (Admin)

**ADMIN-01 · DIVERGED · DISCUSS**
County text: $50 protest fee / $100 appeal fee; protest window 24 hours; **appeal window 8 hours** after protest resolution is announced; single-tier Fair Board executive panel decision is final.
State text: $300 grievance bond (refundable if upheld); protest window 24 hours for livestock (matches county exactly); appeal process runs a chain of **six sequential 15-day clocks** to a 4-person hearing panel (Board member presiding, subject-matter expert, public member, senior staffer).
Archaeology note: the 24-hour protest window is identical in both books, likely not a coincidence — this may be the one place the county already anchored to a state-style number. The 8-hour appeal window is the standout figure: CSF gives roughly **45x longer** to prepare an appeal than Custer does. This could be a defensible speed trade-off for a fair that runs half as long and closes with same-day sale logistics, or it could be a real due-process gap, especially given a meaningful share of appellants will be minors or their parents mid-fair-week. This is a strong candidate for direct board attention rather than a quiet fix.
Mechanics tag: county's fee/window figures scale down roughly proportionally to fair length and stakes, except the appeal window, which scales down far more steeply than everything else around it.

**ADMIN-02 · SILENT · DISCUSS**
County text: no per-class entry fee stated anywhere in the book for county competition.
State text: CSF charges $10–25 per class throughout (beef $25, swine/sheep/goat $20 each, horse $10/class plus $10 written test plus $10 office fee, most Open Division classes $2–15/item).
Archaeology note: could be a deliberate free-entry policy (defensible, arguably a feature for a small county fair) or simply out of scope for what the book documents (fees handled through 4-H enrollment or a separate entry system). Flagged in `volatility-inventory.md` §3 as well since if this changes it's a volatile line, not a rule change.
Mechanics tag: none.

### Poultry

**POULTRY-01 · SILENT · DISCUSS**
County text: the Market Eligible Livestock **and Poultry** department is named for poultry in its own title, but no dedicated poultry ruleset, class list, or schedule slot exists anywhere in the book. Poultry surfaces exactly once, as an eligibility mention under Companion Animal Master Showmanship ("Champion and Reserve Champion ... Showmen from the Cat, Poultry, Dog, and Llama shows").
State text: CSF runs exactly two junior terminal market classes for poultry — Market Chickens (fryer/broiler pens, CSU-Extension nomination required) and Market Turkeys — and **no** open/exhibition/breed/bantam/egg show at all. Colorado 4-H currently has **no** State Fair contest-requirements document for poultry or turkey at any level; the only state-level poultry event found (a separate July 2026 Gunnison County show) lists "Event details TBA."
Archaeology note: this confirms the charter's own "revival program" framing rather than surprising it — and the research turned up a probable reason both sides are thin at once: recent, recurring Highly Pathogenic Avian Influenza (HPAI) disruption has caused real cancellations of poultry shows at the Colorado State Fair in past years, a plausible explanation for why the state-level contest-requirements document doesn't currently exist either. The revival isn't just a county gap to fill from a ready state template — the template itself needs to be rebuilt or requested fresh from CSU Extension, and the board should decide up front whether Custer's revival aims at CSF's terminal-market-only model or a broader open/exhibition model that has no current state analog at all.
Mechanics tag: none.

### Open Division

**OPEN-01 · LOCAL-ONLY · KEEP-LOCAL (suggested)**
County text: "Exhibitors can reside in a county other than Custer, but entry can only be entered in one county fair in the state, this is excluding the Colorado State Fair."
State text: CSF's Fine Arts Exhibition requires all-Colorado residency but has no comparable "choose one county fair" mechanism (it isn't a county-level competition, so the concept doesn't map directly).
Archaeology note: sensible accommodation for a small rural county where neighboring-county residents are realistically part of the community the fair serves — this looks like a deliberate, defensible local policy rather than a gap.
Mechanics tag: none.

**OPEN-02 · CONFLICT (soft) · DISCUSS**
County text: Decorated Baked Goods is its own numbered division (Division 300, judged specifically "on decoration," entries "not tasted").
State text: CSF's Pantry Dept has no standalone cake-decorating or skill-based decoration division — cakes are judged on taste/crumb only, with the sole decoration-adjacent provision being "Decorated Cookies may be larger than 3 inches."
Archaeology note: marked CONFLICT (soft) rather than SILENT because the two books don't just differ in completeness, they judge the *same physical object* — a decorated cake — on opposite criteria (decoration vs. taste). An exhibitor moving between the two systems would need to know which contest they're actually in. Not a rule violation in either direction, but a real category mismatch, which is why it's flagged more sharply than a typical SILENT.
Mechanics tag: none.

### Judging Systems

**JUDGE-01 · ALIGNED · N/A**
County text: Danish System for 4-H Consumer Science/General Projects and Dog obedience; American System for FFA/4-H livestock, showmanship, Cat, Rabbit, Llama, Horse, and Open Division.
State text: same dual-system convention, standard across 4-H nationally and reflected piecemeal across the CSF/4-H materials reviewed.
Archaeology note: no action needed — recorded because the Triage Index should show what's working, not just what isn't.
Mechanics tag: none.

---

## Propagation note

This map ends at the three deliverables per the charter's propagation gate. The disposition tags above are tee-up only — the board conversation and any resulting county book rewrite are separate future missions, gated on this map and not started here.
