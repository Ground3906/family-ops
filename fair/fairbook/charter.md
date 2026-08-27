# Fairbook Charter

The single doctrine file for the Custer County Fair Book rewrite. Mission, architecture, drafting standard, and the source findings and political flags that explain why the book reads the way it does.

**Three files, total.** This one, `draft.md` (the book), and `open-items.md` (the standing list). Session state — what shipped, what is next — lives in the spin-up prompt and nowhere else. Delta tracking was retired 8/12/2026: the book is a full rewrite, so the audit trail is the diff between the old county book and the new one, producible on demand.

---

# PART ONE — MISSION

## What we are building

A revised Custer County Fair Book aligned to the Colorado State Fair rule stack, written finished chapter by chapter as it will print. The working group receives a rulebook, not a menu of proposals.

## The adoption sequence and the clock

**Board adoption by October 1, 2026.** Families begin buying and committing to market beef projects for the 2027 fair in the fall, so the rules must be settled and printed before that buying decision, not after.

Three stages fit inside that date:

1. **Draft complete** — target the week of 8/12/2026. Every chapter written to high finish, print-ready. The working group receives a rulebook, not a partial.
2. **Working group** — Matt, Brittany, and Enjoli, functioning as a subcommittee. They chop, edit, add, and delete. Superintendent input arrives here rather than before drafting; the clock does not allow a cycle of department review ahead of the draft.
3. **Recompile and board vote** — the marked-up draft is rebuilt into a clean book and presented to the full board for formal adoption.

**High finish is a requirement, not a nice-to-have.** The working group needs to react to finished text, not draft a book. A rougher pass would move the drafting burden onto three volunteers and would not survive the clock.

**Superseded 8/16/2026.** The Addendum's first populated instance ships inside the October deliverable, not separately in spring 2027. 2026 facts translate to 2027 using a fixed anchor — the fair closes on the third Saturday in July, giving July 17, 2027 — and the translated values populate the Addendum directly rather than waiting for a second pass. A relative-anchor rule (April 15 llama enrollment, May 1 dog enrollment) does not ride the fair-week shift and carries forward as stated. Values with no source in either direction (sheep and goat maximum weight, official channels) are marked as pending rather than guessed, and populate when the working group or a superintendent supplies them.

## Build order

CC 1 through CC 8 are shipped. CC 1, CC 2, and CC 3 (shared layer plus six species subchapters) shipped 8/12/2026; CC 4 the Livestock Sale and CC 3.1.16 the prior-sale ownership bar, plus CC 5 Horse, shipped 8/13/2026; CC 8 Shooting Sports and CC 7 Showmanship shipped 8/13/2026; CC 6.1 the shared layer and CC 6.2 Rabbit shipped 8/14/2026; CC 6.3 Poultry, CC 6.4 Dog, and CC 6.5 Cat shipped 8/15/2026; CC 6.6 Llama and CC 6.7 Breeding and Dairy shipped 8/15/2026, completing CC 6. CC 7 was pulled forward ahead of CC 6 by explicit call, since CC 6.1's six-species racking pass was judged too long for the session. CC 9, Family and Consumer Sciences and General Projects, shipped complete and standalone 8/16/2026 — the project-sections layer was not built; both source documents were fully consumed by the chapter's single section. CC 10, Open Division, shipped complete 8/16/2026 across three chunks: patches to already-shipped text, the CC 10.1 shared layer plus Baked Goods, Food Preservation, Decorated Baked Goods, Floriculture, Horticulture, and Heritage Arts, then Scrapbooking, Sewing/Clothing, Jewelry, Visual Arts, Photography, and Miscellaneous — completing every chapter, CC 1 through CC 10.

**Draft, front matter, and the full-book conformance screen are complete.** Cover page graphic remains, sourced by Matt outside this project's drafting scope. The conformance screen — reference integrity, abbreviation consistency, no volatile facts in the body, TOC accuracy, Authority naming, adoption lead-ins, single formal register per chapter, and the one full-book renumber — ran to completion 8/17/2026; findings fixed and verified byte-for-byte on push. `draft.md` runs clean from CC 1 through CC 10 with no legacy carry-forward material remaining; the General Rules / Code of Conduct block, the last of three legacy blocks staged since CC 4 shipped, was struck 8/17/2026 once every substantive line was confirmed re-homed into CC 2.

**Table of contents shipped 8/17/2026**, at `fair/fairbook/toc.md`, chapter and subchapter/department depth, kept as a separate file rather than front matter in `draft.md` so the conformance-pass renumber can patch it without touching rule-text diffs. Excludes the Addendum, which publishes separately.

Shared layers build before the projects that lean on them. A reconciliation sweep runs at the end of each chapter to catch commonalities the project passes surface that the chapter's shared layer missed.

**Addendum §1 through §9 shipped 8/16/2026**, at `fair/fairbook/addendum.md`, pre-populated with 2027 facts per the anchor above. §5 carries an index plus seven reproduced forms (§5.1 through §5.7); §5.1 is a proposed Code of Conduct rewrite pending CSU Extension review, §5.2 and §5.3 are marked for collection. §3 (Official Communication Channels) ships as a structure with no channels yet designated, since that is board policy. The same session patched four rules in `draft.md`: CC 2.8 was rewritten to restore the both-sides appeal right (see Part Five), CC 3.3.2 was rewritten into a three-tier swine weight and sale-eligibility structure (see Part Five), CC 3.3.3 and CC 3.3.5 were synced from "hogs" to "animals" to match, and CC 10.1.10 was patched to resolve a self-contradiction (see Part Four). Remaining: cover page graphic, and the pending Addendum values and working-group confirmations tracked in `open-items.md`.

Roughly 700 source paragraphs remain unworked. CC 1 and CC 2 consumed a full session and are the two smallest chapters in the book, so the remaining scope is several working sessions run back to back, not one.

## Political frame

- The book is a communication document as much as a legal one. Primary audience: parents, exhibitors, board members. The lead-in adoption sentence makes the alignment argument on every page — we follow the standard, we are not making things up. Repetition is the feature.
- **Nothing is silently dropped.** Every local mechanism pulled out of rule text is preserved and its home identified, so the old guard can see where their language went rather than discovering it missing.
- **Neutral enforcement.** The disqualifying fact is always generated by an outside authority or an objective instrument — vet, lab, certified scale, brand inspector, Extension signature, national infraction database. The board only executes the printed consequence. The board reads the instrument; it never is the instrument. Every board member has kids in the ring; this is the structural answer to any accusation of self-dealing. Board framing: this extends existing Custer practice (Weights and Measures scale certification, brand inspector notification at beef weigh-in, outside judges), so the pitch is consistency, not novelty.
- Model for the board pitch: county adoption of building and fire codes — model code by reference, local amendments printed as exceptions. Alignment, not novelty.
- **Locked is not adopted.** A decision locked in a working session settles what the book proposes. Only the board adopts. The board can strike or rewrite anything, but it strikes text it can read in place, in the book, rather than choosing from proposals in a log.
- **The working group is a subcommittee, not the board.** Matt, Brittany, and Enjoli mark up the draft. Their edits change what the board sees; they do not constitute adoption. The full board votes.

## Sequencing hazard

The terminal-sale and online-conduct changes both respond to the same 2026 pattern (private resale surfacing on social media). Presenting them separately risks reading as a coordinated crackdown rather than the CSF-alignment argument the whole mission rests on. Decided: one package, presented together, inside the alignment frame. The frame carries everything or it carries nothing.

Board adoption must complete before the sale committee's spring cycle (auctioneer secured January, interest letters end of March, RFP by June) bids the 2027 floor-buyer relationship, since the terminal-sale change alters what that relationship is. The October 1 date clears this with margin. The floor-buyer brief (`fair/sale-committee/floor-buyer-brief.md`) circulates regardless of adoption timing, since the committee's annual cycle does not wait on the board.

## Eligibility carries forward untouched

Matt's direction 8/11/2026: the rewrite does not change or update eligibility scope at all. Every eligibility line carries forward exactly as the county book has it, including where different departments carry different scopes, and is incorporated into the new structure without unification. Where the county book is silent, the rewrite stays silent — a sentence the book never carried is a change to how eligibility reads even where the underlying rule holds.

---

# PART TWO — ARCHITECTURE

**Structure is closed.** Set 8/11/2026. It is not re-argued at the top of a session and not reopened by a drafter mid-pass.

## The five structural rules

1. **Chapter-based.** Every project lives in a chapter. A reader goes to their chapter and stops.
2. **Rack to the top of the chapter.** Commonalities within a chapter rise to that chapter's shared layer. Project specifics stay in the project's subchapter.
3. **Numbering and lettering.** Chapter, subchapter, rule, then letters for subparts.
4. **Addendum for volatile facts. Reference, not reprint.** Dates, times, fees, names, and forms live in the Addendum. Rules are cited by number, not printed twice.
5. **Lean on CSF and IAFE constantly.** The norm is referenced wherever possible. County language rides inside the reference.

## Chapters

| | Chapter | Sections |
|---|---|---|
| **CC 1** | Definitions | abbreviations, every defined term, the Authority |
| **CC 2** | Rules and Regulations | named subchapters, divided by who a rule reaches |
| **CC 3** | Market Livestock | 3.1 all market projects · Beef · Swine · Sheep · Goat · Poultry · Rabbit |
| **CC 4** | The Livestock Sale | sale, terminal delivery, Wholesome Meat Act |
| **CC 5** | Horse | standalone |
| **CC 6** | Non-Market and Small Animal | 6.1 all non-market · Rabbit · Poultry · Dog · Cat · Llama · Breeding and Dairy |
| **CC 7** | Showmanship | 7.1 all showmanship · Livestock · Master · Companion Animal Master |
| **CC 8** | Shooting Sports | standalone |
| **CC 9** | Family and Consumer Sciences and General Projects | 9.1 general · project sections |
| **CC 10** | Open Division | 10.1 general · twelve divisions |

CC 5 and CC 8 are standalone: single-project chapters with no internal commonality layer.

Schedule and roster are gone from the book entirely; they are Addendum content. Book order departs from the current county order, which places Horse and non-market between the market departments and the sale. Reader logic wins over legacy order, and the change is visible rather than silent.

## Front matter

Locked 8/12/2026, order updated 8/17/2026 when the cover-page session split mission and objectives onto their own page: cover page (book title, version number, graphic), mission and objectives page, ADA statement, table of contents, CC 1 through CC 10. All front matter — cover, mission and objectives, and the ADA statement — lives in `fair/fairbook/front-matter.md`, kept separate from `draft.md` for the same renumber-isolation reason as `toc.md`. `draft.md` carries none of it; its own file header points here instead of restating it. The Addendum publishes separately.

The ADA statement adapts CSF's, swapping the Colorado Department of Agriculture for the Custer County Fair Board and the state contact line for a pointer to Addendum §1.

The Fair Book carries a **version number only, never a year**. Its number moves only on an adopted rule change. This book is Version 1.0, the first version under this system; no prior county book was versioned.

## CC 2 and its subchapters

CC 2 is **Rules and Regulations**. It divides into **named subchapters by who the rule reaches**. Three exist so far:

- **All Exhibitors** — true for every exhibitor in the fair, without exception.
- **Animal Exhibitors** — true for every exhibitor with an animal.
- **Open Exhibitors** — true for every Open Division exhibitor.

The set is **not closed**. Subchapters are created as the source requires them.

**The placement test:** a rule belongs in a subchapter only if it is true for every person that subchapter names. A rule true for most but not all does not rise; it stays with its projects. Run the test before proposing, not after locking.

Matt's formulation 8/11/2026: "CC 2 is for everyone. Then the kids can navigate to their projects chapter for more specifics. Forcing a kid to read every chapter means this thing is worthless." A reader's path is CC 1, their CC 2 subchapters, their chapter, and done.

## Racking

Commonalities rack **within a chapter**, to that chapter's top. A rule shared by every market project goes to CC 3.1 and does not climb to CC 2. A rule shared by every animal project goes to Animal Exhibitors. A rule shared by every exhibitor goes to All Exhibitors.

Deviations stay in the project's own subchapter and are not normalized into the shared layer.

**Racking reaches below chapter level too.** Within a single subchapter, a fact repeated verbatim across three or more sibling classes in that subchapter's Class Rules racks into one shared statement rather than printing per class. Precedent: Llama's eight-obstacle minimum, stated once for Pack, Obstacle, and Public Relations rather than three times.

## Numbering

```
CC 3          chapter        MARKET LIVESTOCK
CC 3.3        subchapter     Swine
CC 3.3.2      rule           the citable unit
CC 3.3.2(a)   subpart        a condition inside that rule
      (i)     sub-subpart    rarely, only when (a) itself lists
```

Rules cite three levels deep. **The fourth level is letters, never a fourth decimal.**

The **CC prefix is load-bearing**. This book prints CSF references on nearly every page. Without a county tag, a parent cannot tell whose Rule 4.2 they are reading.

## Reference, not reprint

**A rule prints once.** Everywhere else it is cited by number. Each project section opens with an **applies-to-you index**: every rule reaching that project, by number and title, in about one screen. The index points; it does not restate.

**The index prints as a list, not a rule.** A lead-in sentence states what the section covers, then each pointer runs on its own line as "CC X.X — description." This does not reverse the bullets-banned-in-rule-text prohibition: an index creates no obligation and is never itself cited, so nothing is lost by making it scannable. An index of one or two pointers stays as a single sentence instead; a list that short reads worse as a list than as prose. Locked 8/14/2026, converting CC 3.1.15 and the CC 3.2 through CC 3.7 department indexes; CC 5.12, CC 7.2.1, and CC 7.3.1 stayed as prose under the short-list exception.

Reprinting in full is an exception argued at its pass. Every reprint is a drift risk taken deliberately.

**A by-reference outside document is adopted in parts, not as a block.** DTR and CCR are both CSU Extension contest-rule documents built from a shared template, and that template carries its own protest-and-arbitration provisions layered independently of CC 2.5. Where an adopted document's general-rules block would import a second grievance path, that block is not adopted; only the specific provisions the department needs are cited by number, and CC 2.5 continues to govern grievances in that department like every other. Locked at CC 6.4 and CC 6.5, and extended to the GEFA at CC 10: Custer does not adopt the GEFA as a whole document, only the entry, judging, and display provisions this chapter cites; operational CSF-only provisions (shipping, wristbands, the Pueblo office, CSF-specific check-in cutoffs) are never imported.

## The Addendum

**Superseded 8/26/2026.** The nine-section table locked 8/12/2026, and the "these numbers never renumber" rule that came with it, no longer hold. The working group asked for the IAFE National Code of Show Ring Ethics printed in full as its own section, so every book citation to it points to text a reader can turn to. Placing it first, ahead of the roster, moved every existing section down by one — a deliberate renumber, not a drift. 46 citations across draft.md, addendum.md, toc.md, and front-matter.md were retargeted in the same pass. The lesson carried forward is narrower than the old rule: a section number holds unless a locked working-group decision requires an insert ahead of it, in which case the renumber is done in one clean pass and every citation is verified against the new numbers before the file ships.

Ten sections, ordered by when a family needs them:

| | Section | Holds |
|---|---|---|
| §1 | IAFE National Code of Show Ring Ethics | fixed reference, does not change annually |
| §2 | Fair Board, Staff, Superintendents, and the Sale | roster, contact information, club leaders, processors, floor buyers |
| §3 | Schedule | the fair schedule, cleanup dates |
| §4 | Deadlines and Required Attendance | entry and registration deadlines by project area |
| §5 | Weight Windows and Market Deadlines | per-species weights, ages, and market timing |
| §6 | Fees | grievance, appeal, premiums, any entry fee |
| §7 | Required Forms | every form an exhibitor must complete and sign |
| §8 | Grievance and Appeal | filing windows, the two forms |
| §9 | Locations | every facility named in the book |
| §10 | Official Communication Channels | designated channels, per CC 2.9 |

A section may be empty in a given year; it does not lose its number absent a locked decision like the one above. Structure and current contents live in `fair/rulebooks/volatility-inventory.md`.

**"See the Addendum" is banned language.** Every reference in the book cites a specific section by number. A bare reference makes a family hunt through a document the book itself organized.

**A relative anchor is not a volatile fact.** A rule stated against a moving reference point — "one hour after the conclusion of the beef show" — prints in the chapter body as the rule AND repeats in its cited Addendum section. It is the schedule that is volatile, not the relationship. The relationship is the rule and belongs in the body; the clock time it resolves to in a given year belongs in the Addendum. Precedent: CC 4.3.1, the sale-declaration deadline.

## The Word deliverable

**Locked 8/16/2026.** Markdown in `draft.md` and `addendum.md` is the drafting source throughout the project. The deliverable the working group and the board see is a Word document, generated once at final assembly, after the conformance screen — not built incrementally as chapters ship. Doing it once avoids walking the whole book twice, since the conformance screen already owns that walk.

The Word output is built for a volunteer administrator to edit with basic computer skills: flat tables, a single header row, no merged cells, no hidden or locked cells, no formulas, gridlines visible. A signature line is a bordered table cell, never an underscore run, since underscores shift when a volunteer types near them in Word. A free-text field (a grievance's statement of facts, an appeal's stated outcome) is a fixed-height table cell sized to the content it needs to hold, not a blank paragraph, so it holds its place on the printed page and grows rather than pushing the rest of the form apart.

Every table drafted in markdown from this point forward is checked against these constraints at draft time, not deferred to conversion.

**Hyperlinking.** The Word deliverable is internally hyperlinked. Every citation to a CC rule, an Addendum section, and every table-of-contents entry links to its target, using Word bookmarks and cross-references rather than typed page numbers, so links survive editing and repagination. This is what "see the Addendum is banned" and citation-first exceptions were already built for: a bare reference has nothing to link to, and a book that names its target everywhere is a book that can be wired up mechanically at assembly.

---

# PART THREE — HOW A RULE IS WRITTEN

## Leaning on the norm

**The book should be constantly referencing CSF and IAFE.** The default posture is that a Custer rule sits inside a CSF or IAFE shell. A rule standing outside a shell is the exception that has to justify itself.

**The flow:** reference the adopted rule first, then bring the Custer rule in as an example that helps explain it. Where the county rule deviates or narrows, make the reference, then the county specifics, in one continuous statement.

Pattern: *Custer County adopts and recognizes IAFE Item 5, including the prohibition on ice packs and refrigerants to alter finish, and on altering the color or structure of hair or wool except by trimming and blocking.*

Where the fit is strained, the county rule is drafted inside the shell anyway and **flagged for the working group**. The drafter does not pull a rule out of a shell on their own judgment.

## The examples pattern

State the adopted rule, then print the county's current specifics beneath it as examples. The examples illustrate the rule; they never limit it. This solves the flavor problem structurally: the veterans' own language survives as illustration while the rule above it is the standard. Nothing gets thrown out and nothing drifts.

## Citation

- **CSF cites by heading name.** The GCR carries no section numbers, no rule numbers, and no section symbol anywhere. It runs on named headings. So: "Custer County acknowledges and adopts the GCR, Determination of Violations." A parent can open the state's document, find that heading, and confirm the words match. Verified against source 8/10/2026.
- **IAFE cites by item number.** Its eight guidelines are numbered, so "IAFE National Code of Show Ring Ethics, Item 7" is a real citation. The Code itself is an Addendum instrument, signed, referenced in the book but never restated.
- **HSRB (Horse) cites by specific numbered rule, and by named provision where its provisions carry names but no numbers.** Unlike the GCR, the HSRB numbers its individual rules straight through (Rule 4, Rule 7, Rule 24...), so citations name the number: "HSRB, General Rules and Requirements, Rule 7." A named provision inside the HSRB — "General Rules and Requirements," "Gymkhana Division" — is spelled out in full every time it is cited, the same convention the GCR's named provisions already use (Grievances/Protests, Determination of Violations); it does not get a CC 1 abbreviation of its own. A heading-only citation with no rule number is a defect.
- **Abbreviations are defined once in CC 1 and used everywhere after.** 4-H, APA, CSF, CSU Extension, FFA, GCR, HSRB, IAFE, MQA. Spelling out a defined term after CC 1 is a defect. This applies to the source document names only, never to a named provision or section inside one of those documents — GCR's named provisions and HSRB's named provisions are spelled out in full every citation, per the HSRB citation rule above.
- **Citation-first exceptions.** Any Custer exception that extends, narrows, or applies an adopted rule cites the source first, then states the county's application. Without the citation, an exception carrying a CSF principle reads as Custer inventing liability.
- **The adoption phrase is fixed.** Every adoption lead-in reads "Custer County acknowledges and adopts [source cited by name]," followed by what is being adopted. One phrase, used identically everywhere. A drafter varying it — recognizes, follows, incorporates — reintroduces the vocabulary drift the no-synonyms rule exists to prevent.
- **CSF department requirements cite by named department.** The GCR cites by heading, IAFE by item number, and the CSF department requirements by the name of the department: "the CSF Market Hogs competition requirements." These are numbered lists printed under a department's "Competition Requirements" heading, not GCR headings, so a GCR-style heading citation would send a parent to the wrong document.

## Entity swaps

Mandatory on adoption, not optional. CSF staff titles, CSU Extension nomination machinery, and "the Fair" meaning Pueblo all swap to Custer equivalents. Numbers are never verbatim by default: fees, weights, windows, and deadlines are each a decision in the pass, not a copy.

CSF text built on a standing on-call veterinarian or direct contact with the State Veterinarian's Office swaps to Custer's actual chain: the exhibitor's one call goes to a Fair Board member or the relevant superintendent, who contacts the Authority's veterinarian. The veterinarian's own reporting duties to the state run separately, on her own scope of work, and are never printed as a family's obligation.

Where the base text belongs to another body — the 4-H and FFA Code of Conduct, owned by CSU Extension and FFA, who collect the signatures — the county text is retained as base and **no adoption sentence is printed**. The Fair Board rewriting another organization's instrument in CSF's voice is a harder sell than any rule inside it.

**Superseded 8/26/2026.** The Fair and 4-H office was never actually one place. The Fair Board's office is a fairgrounds structure staffed only during fair week; CSU Extension runs a separate, year-round office. The merged term hid that difference and would have printed a phone number for a building that has none. The book now names two places: the **Fair office**, the fair-week filing point for CC 2.8 grievances and appeals, and the **CSU Extension office**, the contact of record before and after fair week. Routing follows timing — during fair week, the Fair office; the animal care and housing form is the one exception, routed to Extension since §3 and the Code of Conduct already sent it there and only the collection line disagreed. Both offices are listed in Addendum §2 and §9.

**A subchapter may name its own official instrument.** CC 3.1.4 fixes the certified fairgrounds scale as the official instrument, but a livestock scale cannot resolve a three-pound bird. Where the shared-layer instrument physically cannot measure a species, the subchapter names its own as a stated exception, and that instrument carries the same annual Colorado Weights and Measures certification the shared rule requires. The exception is to the instrument, never to the certification. Precedent: CC 3.6.4, the poultry scale.

## Sentence craft

Official-sounding and loophole-resistant pull in the opposite direction from complicated. Loopholes do not live in simple sentences. They live in vocabulary drift.

- Short sentences, active voice, a named actor. "The exhibitor must weigh in on Thursday," never "weigh-in shall be accomplished."
- **Must / must not** is mandatory. **May** is permitted. **Will** is the fair promising something. "Should" never appears.
- Every weight-bearing term is defined once in CC 1 and used identically forever. **No synonyms, ever.**
- Numerals for anything countable, so a kid can scan for the number.
- A rule with a consequence prints the consequence. A rule with a check prints who does the checking.
- Rule text targets a fifth-grade reading level.
- **Bullets are banned in rule text.** A bullet cannot be cited, so anything a family can be held to carries a number or a letter. If it is a bullet, it is not a rule.
- **Book promises print minimal.** Where the book commits the fair to something, promise the least that solves the problem. Operational specificity stays in practice and committee documents.
- **Judging criteria print without point values.** Where CSF states a numeric point breakdown for judging criteria, the book adopts the named criteria and drops the weighting. Applied at CC 3.6.10 and CC 3.7.8.
- Em dashes are permitted here and in the book. These are documents of record, not Matt's authored voice.

## One register

**Locked 8/12/2026, superseding the prior two-register rule.** The book carries a single formal register throughout. Adopted text and Custer exceptions read in the same voice, in CSF's verbose cadence. County language is reworded on adoption rather than carried in its original plain phrasing.

The seam between an adopted rule and a Custer exception is marked by the adoption lead-in sentence and by the phrase introducing the county's reading, never by a shift in register.

Matt's framing: the book is being transformed from a small-county document into an official one that reads consistently from front to back.

Audience is eight through eighteen, with enough weight that the rules sound official, because it is the parents who hunt loopholes. Where formality and comprehension conflict, the sentence gets shorter, not plainer in register.

CC 1 and CC 2 were drafted under the prior rule and converted 8/12/2026.

---

# PART FOUR — SOURCE FINDINGS

Findings from reading the county book, the GCR, and the CSF handbook against each other. These explain why the book reads the way it does and should not be rediscovered.

## The book is downstream of IAFE and never said so

Beyond its four-line ethics rule, the county book is thick with IAFE-derived practice carrying no citation: the tag staying with the animal all fair, the certified scale calibrated yearly, the vet check before sale, MQA required, the signed Wholesome Meat Act Disclosure, no breeding animal in market classes. Ownership integrity, instrument integrity, and food-chain integrity — IAFE Items 1, 2, 4, and 5 in practice with no source printed.

**This is the strongest argument for adoption:** it is recognition of what the fair already does, not importation of something foreign.

IAFE's own text says fairs "may have rules and regulations that they impose on the local, county, state, provincial, and national levels." A Custer layer is not a deviation from the standard. It is the slot the standard leaves open. IAFE also binds "owners, exhibitors, fitters, trainers, and responsible persons," which is how the norm reaches parents without printing a parent-specific rule.

## CSF has no coaching rule

Full-source scan 8/10/2026. The word "coach" appears once in the entire 689-page handbook, in a horse list of who is bound by the GCR. Cueing, cuing, whistling: zero hits. IAFE has none either. The only near-hit in the whole stack is a horse rule, "No deliberate interference with the horse from outside the ring," which addresses spooking the animal.

The state's answer is that the judge handles it, because showmanship scores independence.

Custer's coaching rule prints verbatim eight times in the current book. It is written into CC 2.6 as **examples of interference with other exhibitors**, inside CSF's Prohibition of Interference shell.

**The keystone, Matt's framing:** the injured party is the other exhibitors in the ring, not the coached child. That is what makes it enforceable without proving anything about the coached kid.

## CSF has no show-bar concept

Searched the full handbook and the GCR, 8/12/2026. CSF's sale model has exactly two outcomes: an animal is terminal and goes directly to slaughter, or it is not selected for the sale and is "released to the exhibitor." There is no private-sale path in CSF's architecture, so nothing corresponds to Custer's rule that a privately-sold animal may not be shown again.

CC 1.3 Exhibition Bar is county-original with no shell to sit inside. A genuine structural exception, written as one deliberately.

## The vocabulary collision, and the book's proof case

The county book used "termination" to mean show-ineligibility ("the animal may not be exhibited in any other show or competition") while the sale architecture uses "terminal" to mean the animal goes to slaughter. Same word, two meanings, thirty pages apart.

Resolved 8/12/2026: **terminal** keeps the slaughter meaning, because that is CSF's own word ("The Sale is a terminal sale, and all livestock sold will go to slaughter"). The show-bar concept is renamed **exhibition bar**.

This is the book's proof case for the no-synonyms rule. Loopholes live in vocabulary drift, not in complicated sentences.

## The membership gate is not one rule

It prints four times with three different scopes. General Projects: "bona fide members of Custer County, Colorado 4-H." Market: "Custer County 4-H or Custer County FFA." Non-market: "bona fide members of **Colorado** 4-H & FFA," no county. Sale: "bona fide 4-H **age** youth (no associate member 4-H youth)."

Read plainly, any 4-H member in Colorado may show a rabbit or a dog at Custer while a market steer requires Custer membership. Every line carries forward as written. Do not unify them.

## The county book has no entry rule family

No entry form, no entry deadline, no entry fee, no statement of how a person enters the fair. Indoor and Open Division carry check-in machinery. Llama and Dog carry enrollment dates; nobody else does. Market livestock has nothing — weigh-in and tagging is the de facto registration and the book mentions it only sideways.

CSF carries the full family under Entries and Entry Forms. Matt's direction: county organic inherits, the mechanism stays, this is not a rule change.

**The consent gap this exposed:** CSF's fifth entry rule makes a completed entry the exhibitor's acceptance of all competition requirements. Custer had no analog anywhere. Nothing made an exhibitor agree to the rules by entering. The only consent instrument in the system was the Code of Conduct signature, collected by Extension and running to Extension. CC 2.2 closes this using mechanisms that already exist, without adding a form to anyone's fair week. It is what makes every other rule binding on someone who never signed anything.

## Perpetuity is within the norm

CSF's model separates record permanence from consequence permanence. Its Barred Exhibitors provision reaches anyone barred from any other show for unethical practices, disqualified at any major show, or who has had premiums withheld — no time limit, national reach through the NALS&RMA database. Its Determination of Violations allows a bar "for a determined period, including a lifetime suspension, upon the concurrence" of three named officers.

Permanent exclusion is within the standard, and it arrives with three-way concurrence attached. A three-year ceiling appears only in the interference rule, not in the general violation structure.

## The two three-strike ladders

The county book carried two three-strike ladders thirty lines apart with different triggers and different consequences: the coaching ladder and the own-work ladder. They could not both survive consolidation. Resolved 8/12/2026: the ladder generalizes and moves to CC 2.7(a) as the escalation any rule violation runs through unless that rule states its own consequence. CC 2.6 and CC 2.13 cite it rather than printing their own. IAFE's forfeiture of premiums, awards, and auction proceeds rides on top where the violation also breaches the Code of Show Ring Ethics, because sale money is the only consequence a repeat family actually feels.

## CSF runs a declared weight, Custer runs a weigh-in

Found 8/12/2026. CSF prints, in every market species, that there will be no official weigh-in. Scales are available for exhibitor use, the exhibitor declares a show weight on a weight card, and integrity is enforced afterward by a deviation tolerance: the animal may not vary more than 5 percent from the declared weight when checked on the official scale. Poultry and rabbit run the same way, with band numbers locked to the card at nomination.

Custer runs the opposite machine, a physical weigh-in on a certified scale, and that is the locked direction. The consequence is that Custer imports none of CSF's declaration or deviation-audit machinery, and any CSF weight ceiling adopted into this book is enforced at the scale instead. This also means the post-placement re-weigh finding below reaches the poultry ceiling, not just beef.

## CSF bars market into breeding, Custer bars breeding into market

These are opposite directions, not the same rule stated once. CSF's Junior Livestock Market Competition eligibility list provides that market animals are not eligible for entry in any breeding show, with a printed exception for heifers, which may enter the Junior Breeding Heifer Show. The county book carries only the reverse, that animals shown in breeding classes may not be shown in market classes. Both directions print, with the heifer exception carried and the department name swapped.

Custer's Breeding Beef department exists but carries no defined classes, only a line vesting regulations and classes in the superintendent or Fair Board. Matt's note: the non-market departments are thin because nobody enrolls in them, not because the fair is closed to them.

## The county market section has four departments and promises five

The market section heading reads "MARKET ELIGIBLE LIVESTOCK AND POULTRY RULES AND REGULATIONS" while the section contains only Market Swine, Market Beef, Market Sheep, and Market Goat. No market poultry department and no market rabbit department exist anywhere in the source. Poultry and Rabbit in CC 3 are therefore new construction against locked direction, not consolidation of existing text.

Two defects in the source itself, recorded so they are not mistaken for extraction errors: two general rules are truncated mid-sentence. An XML-level re-extraction 8/12/2026 confirmed Market Swine's project exhibit rules run fully populated, six items straight through, correcting an earlier and incorrect claim that they opened with three textless numbered stubs.

## The CSF handbook carries copy-paste artifacts between departments

Found 8/13/2026. The CSF Market Goat holding-area rule prohibits family members from holding or staging "any lamb-holding pens," inside a section otherwise entirely about goats — the text was written for Market Lambs and pasted across. The CSF Market Chickens classes are divided into "White and Bronze," but Bronze is a turkey variety, and CSF's own turkey classes carry no such split.

Neither artifact was adopted. Before adopting any CSF department requirement, confirm the rule belongs to the department it is printed under. A rule naming a different species than its own department heading is the tell.

## The Wholesome Meat Act does not reach two market species

The Act amends the Federal Meat Inspection Act, which covers cattle, sheep, swine, and goats. Poultry falls under the Poultry Products Inspection Act. Rabbit is a non-amenable species under voluntary fee-for-service inspection. CSF runs Market Chicken, Market Turkey, and Market Rabbit divisions and still names only the Wholesome Meat Act in its sale warranty, so adopting CSF verbatim imports the same gap. Resolved 8/12/2026: both acts print, plus a county-original catch-all warranting any market species not covered by a named act to the same standard, with rabbit named as the current instance. Not legal advice; confirm with the processor or Extension before the book prints.

## The 2026 pattern behind the terminal sale

Multiple families repurchased goats and sheep from the floor buyers after the sale; animals resurfaced on social-media sale pages roughly six months later. The effect was double-dipping: sale check, animal back, private resale. The premium buyer base — the fair's high-priced and deeply supportive buyers — was angered and soured by it.

The current book licensed the leak by assigning trucking, slaughter, and processing to the exhibitor. The fix closes it by custody rather than prohibition, following CSF's own architecture, with an explicit product-not-live-animal clause added since CSF leaves that implicit.

Stated opponent-proof: behavior pattern and buyer-relations stake, no blame on any named person. No names recorded, by design.

## Veteran knowledge captured

**Beef post-sale rest custom.** Never previously written down anywhere: sale steers were commonly taken home for about a week to calm down and restore muscle glycogen before processing, since a stressed slaughter animal risks dark-cutting and docked meat. The terminal custody chain cannot accommodate an at-home rest week, so the purpose — meat quality — is preserved differently: a purchaser-requested rest period arranged inside the designated-facility chain, holding cost withheld from proceeds like any other delivery cost.

**Why a substitute shower is allowed.** The county rule permitting an animal to be shown by its owner or another qualified member exists for the exhibitor who has two animals of the same species drawn into the same class. The book has never stated the reason. Recorded 8/12/2026 so the answer exists when someone asks why the exception is there.

**Sale-day information practice.** The auction runs live on an auction site, deliberately unnamed in the book to avoid lock-in — the veterans' existing instinct is the volatility doctrine already in practice. Sale lots and order are distributed physically ringside. Misprints are hand-scratched on the podium sale sheet and announced during the sale; the podium sheet as annotated is the single source of information.

## Market Rabbit is the sale-integrity case, not a third terminal rationale

Found 8/13/2026, reading the CSF Market Rabbits department (Dept 802.00) against the terminal-rationale question raised building CC 3.6. Only the Grand Champion and Reserve Grand Champion pens qualify for the Livestock Sale, and CSF states plainly that the sale is terminal only for the pens that qualify. The department's own schedule has every non-qualifying pen off the grounds the same weekend rather than routed to slaughter.

This is the beef, hogs, lambs, and goats pattern. Poultry's terminal-by-biosecurity rule, adopted at CC 3.6.3 and explained at the Part Five finding on two terminal rationales, does not extend to rabbit; nothing in CSF's rabbit text carries a disease or commingling rationale. Resolved 8/13/2026: CC 3.7.2 states the distinction explicitly rather than leaving it to inference, since the two departments sit back to back in the book and silence would invite a reader to assume the poultry rule carries over.

## Showmanship timing contradicts the written county rule

Found 8/13/2026 building CC 7. The county book states showmanship classes run "immediately prior to the judging" of their paired class, but actual practice runs the opposite: the market or breed class is judged first, and showmanship for that species runs after. CC 7.1.7 (then numbered 7.1.6, before the CC 7.1.1 index insert) was drafted to match practice rather than the old written rule.

**Superseded 8/26/2026.** The working group asked for judge preference instead of a fixed order. CC 7.1.7 now points to the Addendum schedule, and the Authority sets the order each year in consultation with that year's judge. The finding above is why a fixed order existed at all; it is not the reason a fixed order was kept.

## CSF's Master Showmanship Competition is the state-level feeder event

Found 8/13/2026 building CC 7. CSF runs its own Master Showmanship Competition (Division 001, Department 925) at the state level, open only to one exhibitor per county fair, fed by each county's own "Round Robin" or equivalent qualifying event. Custer's Livestock Master Showmanship Contest at CC 7.2 is that qualifying event, though the book does not currently point to the CSF competition it feeds. Previously unrecorded institutional knowledge.

## Horse carries no pen, stall, or cage assignment rule, and none is planned

Found 8/14/2026 building CC 6.1. CC 3.1.11 (market) and CC 6.1.4 (non-market) are parallel rules, same shape, adapted to species. CC 5 (Horse) has no equivalent and is not getting one. The horse project runs on stalls families arrange directly, outside any Authority-run assignment process the book governs, and none of CC 5's other rules touch space either. Recorded so a future both-directions audit of CC 5 does not re-flag the absence as a silence-gap needing a rule.

## CC 6.3 Poultry has no source in either direction

Found 8/15/2026 building CC 6.3. The county book's only mention of a poultry show anywhere in the non-market section is the old Companion Animal Master Showmanship rule, which names Cat, Poultry, Dog, and Llama as feeder shows without ever creating a Poultry department. CSF carries no junior poultry department to adopt from either — its only poultry departments are Market Chickens and Market Turkeys. CC 6.3 was constructed rather than adapted, the first department in the book built this way.

## Market Goat's Dairy Goat cross-reference points at nothing

Found 8/15/2026 building CC 6.3. CC 3.5.14 sends the reader to "the non-market eligible livestock section" for Dairy Goat. That section has no Dairy Goat department, only a two-line Non-Market Goat entry. The dead cross-reference predates this rewrite and is not caused by anything shipped so far; flagged for the conformance pass rather than fixed now, since Breeding and Dairy has not yet been built and may be where it resolves.

## The county's Dog rules regulate a class that is not offered

Found 8/15/2026 building CC 6.4. The county book's obedience rules reference a "Sub-Novice" class by name in two places, but no class list anywhere in the county book offers it. Resolved by adopting the DTR's own progression, which uses Pre-Beginner Novice in that slot; CC 6.4.5 prints the DTR progression as authority rather than the county's incomplete list.

## DTR and CCR share a template, protest-and-arbitration block included

Found 8/15/2026 building CC 6.4 and CC 6.5. Both are CSU Extension by-reference documents, and both carry near-identical General Contest Rules language, including matching $50 written-protest and arbitration-committee provisions. Neither block was adopted, for the reason at Part Two. Expect the same template, and the same non-adoption, in any future by-reference document this book cites.

## The Cat archive file is a CC 9 source, but not the only one

Found 8/15/2026 building CC 6.5, corrected 8/16/2026 building CC 9.1. `co4h-cat.pdf` is not a Cat-specific document. It is the full CSF 4-H Contest Requirements bundle (CCR), covering Cake Decorating, Cat Show, Creative Cooks, Digital Photo, Fashion Revue, Public Presentations, and Rocket Fly Day. The original plan was for CC 9 to extend the CCR abbreviation rather than define a second one.

That plan didn't survive contact with the source. A second CSU Extension document, `co4h-consumer-science-general.pdf`, governs the exhibit-requirements shared layer CC 9.1 actually adopts from — eligibility, original work and AI-generated content, one-entry-per-class, display board standards — and it is a genuinely different document from the CCR: contest rules for live judged events versus exhibit rules for static displays, despite overlapping category names (Cake Decorating appears in both). It earned its own abbreviation, CCGP, defined at CC 1 and adopted at CC 9.1. Both documents reach CC 9; neither substitutes for the other.

## CC 9.1 silence-gaps closed from the CCGP shared layer

Found 8/16/2026. Three CCGP requirements had no county analog and were adopted into CC 9.1 under the both-directions audit: the AI-generated-content labeling and disqualification rule (an image or passage of text generated by AI and used in a display board, project notebook, or e-record must be captioned with the tool, the developer, the date, and a link), the one-entry-per-class limit, and the display board size and safety standard (4 feet by 3 feet, no sharp items). None of the three carried forward from the county book; all three cite CCGP directly.

## Llama's Costume class and Cat's Costume Contest may be one practice, not two

Found 8/15/2026 building CC 6.5. Both departments carry a Costume class judged with every age division together, the only class in either department not split by age. Neither source explains the shared shape, and it is unconfirmed whether this reflects one real cross-species costume practice at the fair or independent copy-paste between two legacy sections. Worth a direct check when Llama opens, since the answer may mean one rule rather than two.

Checked when Llama opened, 8/15/2026: not the same shape. Llama's Costume class states its all-ages rule three times in the source. Cat's carries no source at all — the sentence naming Cat's Costume Contest as undivided appeared in shipped text with no county or CCR statement behind it, and has been struck. Logged to open-items as a working-group question rather than resolved as fact.

## A session-long citation mislabel went uncaught until the Addendum pass

Found 8/16/2026. CC 10.1.10, the miscellaneous-exhibit-request rule, was referred to as "CC 10.4" throughout an entire Addendum working session — by the drafter, not corrected by Matt — because CC 10.4 (Decorated Baked Goods) sits nearby in the chapter and the number was carried from memory rather than checked. The error surfaced only when the actual rule text was pulled to fix a real defect inside it: the rule pointed at Addendum §4 for a deadline that resolved to check-in, while also stating a request made at check-in is refused. The citation-number error and the substantive defect were unrelated; only pulling the source caught either one. Reinforces the standing rule at Part Six to re-check already-fetched text at the point of use rather than recalling it, extended here to rule numbers carried across an entire session rather than reused from a moment earlier in the same reply.

## A keyword hit-count is not a source

Found 8/15/2026 building CC 6.7. A raw text search for "Breeding Swine" in the CSF handbook returned five hits, read at first as a real department to adopt from. All five were incidental: a Hereford Hog purebred-eligibility note and a litter-registration policy line, both embedded in the Market Swine department rather than naming a standalone Breeding Swine show. Breeding Sheep and Dairy Goat, by contrast, each returned dozens of hits inside a genuine numbered department with its own class list and award structure. A hit count alone does not distinguish these; the entry or class-number list structure does. Check before treating prose mentions as an adoptable source.

## Two postures for the same zero-source pattern, resolved

CC 6.3 Poultry was built from construction — real classes, drafted from general livestock-show convention, with neither source to check against. CC 6.7's five classes with no source on either side (Breeding Beef, Breeding Goat, Breeding Swine, Fiber Goat, Utility Goat) were instead left undefined, delegated whole to the Authority. Same fact pattern, two different drafting postures.

Resolved 8/16/2026: **delegate always.** Where neither source carries rule text, the book prints the Authority-vesting rule and logs the gap to open-items; no department is built from show convention. CC 6.3 Poultry stands as shipped, the pre-default exception — it was fully fleshing out a viable high-participant project, and the default governs drafting decisions made after 8/16/2026, not a retroactive edit to a decision already made and recorded.

## CC 2.3's sanctions list is deliberately open-ended

The legacy General Rules block, struck 8/17/2026 once its conduct material finished re-homing into CC 2, carried an eight-item sanctions enumeration for a conduct violation: verbal warning, notification to parents, immediate removal, premium penalties, behavior contract, law enforcement referral, program suspension, expulsion. CC 2.3 states who may impose discipline and the due-process standard but never lists what the sanction can be, only that the Authority "may impose any sanction."

Confirmed 8/17/2026, kept open-ended rather than pulling the enumeration forward. This is a decision, not a gap: a future conformance pass should not read CC 2.3's silence as unfinished and reopen it.

---

# PART FIVE — POLITICAL FLAGS

Things that will land hard. The working group screens them first; the board should hear them out loud rather than discover them in a barn.

## Superintendent authority

Nine rules in the current book vest a responsibility in a superintendent alone: early release of exhibits, hardship cases, releasing animals from the grounds, checkout before leaving, feeder animal early release, breaking classes by weight, barn space assignment, changing class order, and refusing an exhibit.

All nine rewrite to vest in **the Authority with the superintendent named as lead** — every printing, site by site as each chapter is written, no standalone announcement rule in CC 1. The superintendent's original sentence does not survive alongside; it is rewritten.

**FLAGGED DRAMA-PRONE.** A long-tenured superintendent will hear "we are taking your show away." The answer that works, in Matt's framing: "This isn't to take their responsibility away, it's to formally allow the Authority to do what they need if needed." The rule changes nothing about who runs the show, only about who the show belongs to.

**Rule seven is the live flashpoint:** barn space assignment. Swine stall assignment is a recurring political issue, not a one-time one.

**The rewrite has settled into a fixed formula, confirmed 8/15/2026 against nine live printings:** "[obligation or power], with the superintendent of the department as lead." The verb before the comma tracks whether the Authority must act or may — "shall determine," "may impose," "may change" — and that choice is a real decision each time, not filled in by the formula. Only the trailing clause is fixed.

## Pen allocation changed principle

Locked 8/12/2026 at CC 3.1.11. The county rule gave space priority in the barns to Senior members, full stop. CSF allocates by animal, one pen per head delivered, with no ranking of exhibitors at all. Custer is running out of space, so neither model survives alone: every exhibitor is guaranteed one pen per species entered, seniority sets the order of assignment, and the superintendent runs both the guaranteed pass and the distribution of whatever space is left.

This is a real change in principle from a pure seniority queue to a floor plus a seniority-ordered remainder, and it lands on the most drama-prone rule in the book. CSF's tampering language is adopted alongside it, which gives the assignment a printed consequence it never had.

**The capacity escape valve is a second flag inside the first.** CC 3.1.11 carries a valve: where entries in a species exceed available pen space, the guarantee yields and the Authority may impose limits on the space assigned to each exhibitor, with the superintendent as lead. The trigger is objective — entries exceed pens, a fact anyone can count. The response is open-ended, and that asymmetry is deliberate, because no printed formula survives contact with a barn that is genuinely full. It also means the valve prints discretion into the most drama-prone rule in the book, on the same page as the rule that already changed principle. Working-group walkthrough item: the board should decide with open eyes whether it wants the discretion or a printed formula, rather than meet the valve for the first time in a full barn.

## The coaching rule

Matt is the only board member who questions it and expected to lose a straight repeal vote. The examples structure means **no repeal is needed**: the veterans' language survives in the book, printed as an illustration of an adopted standard rather than as county invention. The alignment argument stays intact.

## Local practices that did not survive

Named here so the veterans hear them from the board rather than discovering them missing.

**First and last call.** The county gave two verbal calls before a show and forfeited the exhibitor's right to show at the second. CSF has no calls at all; the exhibitor is responsible for being at ringside one class ahead, and the gate is held only where the gate steward was told of a conflict. CSF's model was adopted whole at CC 2.18 and the calls end.

**The beef no-waterers line.** Market Beef prohibited leaving feed pans or waterers in pens and stalls, in direct contradiction of Market Swine and of CSF. CSF governs every species now and the beef line dies.

**The swine self-waterer allowance.** Market Swine permitted a self-waterer built from PVC pipe and a pig nipple. Compatible with CSF but more specific than it, and dropped rather than raised, on the judgment that CSF's rule is enough.

**Superintendent-delivered grievance routing.** The county book had grievances in Open Division routed through the division superintendent at check-in. CC 2.8 governs grievances for every chapter in the book, Open Division included, and that routing does not survive — a grievance in any department goes through the standard CC 2.8 channel, not a department-specific one.

## Answerable for the people you bring

CC 2.7(c) records a warning against both the person who earned it and the exhibitor they were acting for. This is CSF's principle, not Custer's, and it will land hard the first time a twelve-year-old loses premiums because her uncle pounded on a rail.

It is also what closes the gaming vector: route coaching through an uncle and the uncle carries a record that follows him to every family he helps, while the exhibitor's record moves anyway. No clean hand to hide behind.

**The board should say this out loud when the book is presented.**

## The accessibility statement and the parking gap

The book now prints an ADA commitment while the grounds still have no designated accessible parking at either entrance. Those two facts should be presented together, not discovered separately.

## Judges' decisions

The current book contradicts itself: the Conduct section says decisions are final while the protest section says a protest may review judging procedures. CC 2.5 resolves it — a judge's placing is final and not protestable, while a grievance reaches rules, eligibility, and procedure. Resolving a contradiction in a direction changes effect, so this is a real decision, not cleanup.

## Testing: "may" is deliberate

The county has no capacity or intent to run mandatory testing every year. CSF prints "will be tested" for champions; Custer prints **may**. This keeps the deterrent and the right on the page without committing the fair to the cost or the logistics. The softening is deliberate and should be named as such rather than discovered.

## Post-placement re-weigh: not adopted, and why

CSF re-weighs the top five finishers in each class after placing, with a greater-than-5% deviation disqualifying. Custer's scale limitations may not support it. **Printing an integrity rule the fair cannot reliably execute is worse than not printing it.** If the board wants it, that conversation needs the scale's actual capability on the table.

## Two different terminal rationales

Market poultry is terminal for biosecurity: birds that have commingled at a fair do not return to a home flock. Every bird is terminal whether or not it sells. The market sale is terminal for sale integrity, and that change carries the 2026 resale history behind it.

These are separate arguments and they must stay separate in board framing. Poultry's rule would stand on its own if the sale had never changed. Folding it into the sale package would hand an opponent the claim that the board is expanding terminality everywhere, and would drag a disease-control rule into the most contested conversation in the book.

## Vet scope of work

The enforced-by assignments accumulating across the chapters convert into a vet-facing engagement document: arrival inspection, age verification where invoked, the sale-ring health gate, on-grounds medication administration, specimen collection if testing is exercised, and illness or injury certification for sale eligibility. This lets the veterinarian scope and fee the work as a professional engagement.

CSF supplies a printable cost-recovery model: arrival inspection charged to the exhibitor when documentation is missing, testing costs deducted from sale proceeds.

Audience lane: professional and vendor-facing. Scope and fee basis only. Board-facing framing is no-blame — formalizing existing practice so expectations and fees are clear for both sides. Nothing about exhibitor behavior trends prints anywhere in it.

## Horse dress narrowings not adopted

The county book's horse dress rules require long-sleeve button-down shirts with collar and cuffs, no "show" shirts, and no chaps or chinks in any class. HSRB permits chaps as optional attire, so the county's chaps prohibition contradicts the adopted source and does not print at CC 5.10. The show-shirt and chaps restrictions are real practices some families may expect to see; their absence should reach the working group before a parent notices a chap-wearing exhibitor and asks why the rule vanished.

## The grievance appeal right was one-sided until this session

Found and fixed 8/16/2026. CC 2.8 as shipped gave the appeal right to the grievant only — "if the grievant is not satisfied... the grievant may appeal." A person sanctioned under CC 2.7, including on a first written warning that CC 2.7(b) makes permanent and never-expiring, had no route to contest it at all, whether or not anyone had filed a grievance against them. The GCR's own Rights of Appeal and Process of Appeal provision, which CC 2.8 already cited as adopted, gives the appeal right to the person a determination went against — the book had cited the source and then narrowed past what it said. CC 2.8 now gives a sanctioned person the same appeal right a grievant has, with its own filing window (Addendum §9) and its own effective date (the sanction itself is not recorded under CC 2.7(b) until the appeal is decided, so an appeal in progress cannot be held against the person while it is pending).

**FLAGGED for the board pitch.** This closes a real gap rather than adding new machinery — the fix restores what the GCR citation already promised — but it is still a new right nobody currently has, and worth naming plainly rather than letting a superintendent discover it the first time a warning gets appealed.

## Underweight market swine now show but cannot sell

Locked 8/16/2026 at CC 3.3.2. Previously, an underweight animal showed under the general feeder-animal rule at CC 3.1.9 with no species-specific bar on selling it. CC 3.3.2 now states explicitly, for swine only, that an animal at or under 219 pounds shows in the lightest weight class but may not sell in the Market Livestock Sale. The three-tier structure (underweight shows-only, in-window shows and sells at actual weight, overweight shows and sells capped at the 290-pound maximum) is Matt's direct instruction, not adopted from CSF or carried from the county book.

**FLAGGED for the board pitch.** This is a real new restriction on a family whose animal comes in under 220 pounds, printed nowhere in either source. It is scoped to swine only; sheep, goat, and beef are unaffected and carry no equivalent bar.

## Board policy, deliberately not in the book

- **Discipline ledger keeper.** The Fair Board secretary holds it, as a standing duty of the office rather than of a person. Families are told warnings are permanent, never who keeps the ledger. Extension was considered and set aside: a ledger the Fair Board does not control is a ledger that can quietly stop existing.
- **Buyer-refund donation destination.** The book prints "the Custer County Fair" with no named recipient. Where that money lands is board policy. The Wet Mountain Valley Community Foundation is the obvious candidate and is deliberately unnamed in rule text.
- **Official channel designation.** Who administers the accounts and how a channel is designated is board policy. The book carries only the pointer to Addendum §10.

---

# PART SIX — WORKING METHOD

- **ONE TOPIC PER RESPONSE — hard rule.** Present one item. Stop. No decision maps, no stacked questions, no "here's everything" preamble, no commentary tail after the decision. If a topic has structure, surface the structure as ONE line and open the first item — do not walk the whole tree. Findings, verification results, and status may batch; decisions and the reasoning around them never do. This holds under every framing, including efficiency. Correcting this drift is not Matt's job.
- **Map the decision surface before opening an item**, so the item's true size is visible at the start. A sub-question discovered mid-item is named as newly discovered when it surfaces.
- **Check the existing lock before building an options menu.** A prior lock, a charter line, or an established default may already answer it. Presenting settled doctrine as an open choice wastes a turn and invites re-litigating something decided.
- **Pull the source before presenting a delta.** CSF first, county second, question only on the difference. Asserting what a source says from memory and being corrected costs more turns than the pull would have.
- **A department pass runs both directions.** County to CSF finds the deltas: where the county rule differs from the standard it sits inside. CSF to county finds the silence-gaps: where CSF's department carries a requirement the county book never had, and the county's silence is an omission rather than a decision. A department is not finished until its CSF department checklist has been walked item by item. Shared layers carry the same exposure — CC 3.1, CC 2, and CC 1 were built before this pass existed and owe a re-audit, tracked in `open-items.md` under Method.
- **A by-reference document's named contents get swept before a whole-document adoption locks.** Before locking a decision to adopt a by-reference document (CCR, DTR, or similar) whole into a chapter, every contest, class, or project area that document names is checked against the county source range first. A document may carry real content the county book never printed a word of; adopting it whole without that sweep imports territory nobody asked for. Locked 8/16/2026 after the CCR's seven named contests were found to have zero county-book presence, discovered only after the whole-document adoption had already locked.
- **Sweep the full county paragraph range before Item 1 opens.** A line sitting in the department's front matter, above the numbered project rules, is easy to miss when work starts from the class list. Llama Races sat undiscovered until late in that department's pass because the sweep ran only over the class-list and class-rules paragraphs. Every line in the department's source range gets a disposition — adopted, racked, delegated, or logged — before the first item is presented.
- **Run the placement test before proposing, not after locking.**
- **Words, not numbers.** Matt-facing presentation quotes the exact rulebook text. Paragraph indices and line numbers live only in repo records.
- **Sources first, never memory.** The county book, the GCR, and the CSF handbook live in `fair/rulebooks/archive/`. Containers reset; re-pull and re-extract each session rather than reconstructing from a prior summary. This reaches within a session too: re-check already-fetched text at the point of use rather than recalling it from earlier in the same conversation, including before asserting what a source does or doesn't say and before assigning a new rule number against a slot that may already be occupied.
- **A resumed session re-verifies before it narrates.** After a conversation compaction, the compaction summary's status claims — what shipped, what is still pending — are not authoritative until checked against the actual files. A session opened by echoing the summary's "open-items.md still needs eight more items" framing before pulling the file; the file was already current, the framing was stale. The verification pull (`open-items.md`, `charter.md`, `draft.md` HEAD) runs at the first message of a resumed session, not deferred to the first write trigger.
- **Build gate.** Nothing ships without a commit word. A correction is never a commit word.
- **Verify content before every write, not just intent.** A session wrote a literal placeholder string to `draft.md` instead of the file's content, live on main for about a minute before the read-back caught it at 8 bytes. Before any `create_or_update_file` call: confirm the actual content is present, not a reference or shorthand, and sanity-check its length against what's expected. The read-back catches a bad push after the fact; this catches it before.
- **A push that requires content the drafter has not directly read in full is not routine.** A small file gets viewed whole before it is retyped for a push. A file large enough that only excerpts have been read carries a real risk of the untouched majority being reconstructed from general shape rather than transcribed — read it complete, in gapless ranges, immediately before the push, and verify the result against a locally computed git blob SHA rather than a character count. Locked 8/26/2026 after `draft.md`, at 140KB, was pushed successfully this way following an initial attempt that would have relied on an incomplete view.
- **A multi-chunk build targeting one file patches every chunk in the container first, then pushes once.** "Large builds chunk by default" chunks the drafting and verification work; it does not require chunking the push itself when every chunk lands in the same file. One push, hash-verified, after all chunks are patched and diffed. Locked 8/26/2026 building `draft.md` across CC 1 through CC 10 in one working-group edit pass.
- **A gap found by reading the old book is checked against the current draft before it is named a defect.** Reading the prior county book surfaces real history, but a rule found there and not immediately visible in `draft.md` is not yet a finding — the current file is checked directly before anything is called missing, dropped, or silently deleted. Three false findings in one working-group session (goat milk teeth, the re-weigh policy, rate of gain) came from skipping this step; two of the three already existed in `draft.md` exactly as needed, and the third had simply never been part of any version. This extends the existing pull-source-before-presenting-a-delta rule to `draft.md` itself, not just the external sources.
- **A hash match on the write tool's own return value is the only accepted proof a push landed correctly — not a re-fetch, not a re-read, the value the tool call itself returns.** A push of this exact file, on the first attempt, returned a blob SHA and size that did not match the locally computed reference, despite the content having been read in full immediately beforehand. A contiguous block from the middle of the file was missing from what actually transmitted, with no error and no visible sign in the response other than the mismatched hash. The cause was not diagnosed; the fix was a second push, checked the same way. This is why the check compares the tool's returned SHA, not just a belief that the right content was sent — a large single-call payload can silently drop a middle section in transit, and the returned hash is the only signal that catches it.

## Source re-extraction

County book (.docx): curl the raw GitHub URL, `pip install python-docx --break-system-packages -q`, iterate `doc.paragraphs`, write a numbered extract. CSF handbook and GCR (.pdf): curl, then `pdftotext -layout`.

Raw fetches (`raw.githubusercontent.com`) need a commit SHA or branch in the URL, never a blob SHA; an invalid ref returns an empty file rather than an error. Sanity-check line count immediately after any raw fetch used as an edit base.

Archive holds: the 2026 county book, the CSF handbook, the GCR, and the Colorado 4-H project guides for cat, dog, shooting sports, and consumer science. The Colorado 4-H Horse Show Rule Book (LA1500K, 2024), named by the county Horse section and pulled from the web 8/13/2026, is not yet in the archive; add the official PDF when convenient.
