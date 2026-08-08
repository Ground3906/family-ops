# Fairbook Delta Log

The walkthrough document. Every change from the old Custer book to the new draft lands here, one entry per change, populated by the section passes in book order. Two entries below are pre-staged: decided ahead of the passes so the decisions ride in the repo, not in session batons.

**Schema per entry:** stable ID · status · exact old Custer text · new text · CSF cite · reason · enforced-by (where the rule carries a check) · divergence-map cross-ref where one exists.

**Status vocabulary:** ADOPTED (in the draft) · FLAVOR-CANDIDATE (local mechanism held for working-group sponsorship) · DISCUSS-AT-WALKTHROUGH (undecided, prints greyed in the walkthrough copy). Filtering DISCUSS-AT-WALKTHROUGH produces the working-group docket. Filtering enforced-by produces the vet scope of work.

---

## Pre-staged entries

### FB-TEST-01 · ADOPTED (direction locked; final wording lands in the Market Livestock pass)

- **Old Custer text:** "random drug testing" appears as an item within the county book's four-item unethical-practices list; no consent mechanism, no collection procedure, no champion-testing provision stated.
- **New text (staged direction):** adopt CSF's consent-to-testing structure — entry constitutes consent to collection of urine, saliva, blood, or other specimens, and the fair reserves the right to administer testing on any animal at any time on the grounds. Champion-testing clause adopted with CSF's mandatory language deliberately softened: Grand and Reserve Grand Champion animals of each species MAY be tested (CSF prints "will be tested"). Testing costs, where testing is exercised on sale animals, deducted from sale proceeds per the CSF model.
- **CSF cite:** 2026 Exhibitor Handbook — Testing and Fees ("The Authority reserves the right to administer random testing, including DNA, urine, tissue, blood..."); champion-testing clause ("All Grand Champion or Reserve Grand Champion animals of each species in the Market divisions will be tested"); IAFE National Code of Show Ring Ethics consent language (entry = consent to specimen collection, lab report = prima facie evidence).
- **Reason:** the county has no capacity or intent to run mandatory testing every year. "May" keeps the deterrent and the right on the page without committing the fair to the cost or the logistics. Deliberate ambiguity is the design, logged as REWORDED.
- **Enforced-by:** independent laboratory, specimens collected under veterinary supervision.
- **Cross-ref:** divergence map — Heavy Hitters "Drug residue & show ethics" row; ETHICS-01.

### FB-REWEIGH-01 · DISCUSS-AT-WALKTHROUGH (entire rule prints greyed)

- **Old Custer text:** none. The county book carries only the pre-declaration accommodation re-weigh ("re-weigh two additional times prior to the end of weigh in"); no post-placement audit exists.
- **Proposed text (greyed, not in draft):** CSF's post-placement integrity audit — top 5 finishers in each class re-weighed after placing; deviation greater than 5% from declared weight disqualifies, no re-weigh, not eligible for any other class.
- **CSF cite:** 2026 Exhibitor Handbook, cross-species re-weigh rule (identical wording for beef, goats, hogs, lambs).
- **Reason for DISCUSS:** county scale limitations may not support post-placement audit enforcement. Printing an integrity rule the fair cannot reliably execute is worse than not printing it; the working group decides with the scale's actual capability on the table.
- **Enforced-by (if adopted):** certified scale (Colorado Weights and Measures certification), administered by superintendents.
- **Cross-ref:** divergence map — LIVESTOCK-01.

---

## Pass entries

### Pass one — General Rules (committed 8/8/2026)

#### FB-CONDUCT-01 · ADOPTED

- **Old Custer text:** six defects across the Code of Conduct's disciplinary sections (parts D, E, F of the front-matter list). (1) "the following procedures **should** take place before there is a finding or conclusion of guilt" — the only place in the section where a binding step is softened; everything else binding uses shall or must. (2) "The 4-H, FFA, Fair Board, or CSU Extension staff **The 4-H or FFA** must be satisfied that the participant, more likely than not, engaged in the prohibited behavior" — duplicated sentence fragment, reads as an edit that added the longer list without deleting the phrase it replaced. (3) "must arrange for the procedures in **part B above**" — part B is "Behaviors prohibited at the County Fair that warrant removal from fairgrounds." The procedures are in part E. (4) The law-enforcement paragraph printed twice, near-verbatim, once under part C and again under part F. (5) "...is in violation of the 4-H and FFA Codes of Conduct**..**" — double period. (6) "may impose discipline **pursuant below**".
- **New text:** "should" to "must"; duplicated fragment removed; "part B above" to "the procedures set out under Disciplinary Procedures above"; the part F duplicate deleted and the part C instance retained; double period corrected; "pursuant below" to "as set out below". Full cleaned text in `draft.md`.
- **CSF cite:** none. No CSF rule is adopted on this paragraph.
- **Reason:** cleanup only, no change in meaning or effect. The part B reference is broken in the source, not in extraction. The Word list (numId 57) letters its top-level items A through F: A Purpose and application, B Behaviors prohibited, C Behaviors subject to Disciplinary Procedures, D authority paragraph, E Disciplinary Procedures, F Immediate action situations. Procedures fall at E. This reads as template inheritance: the standard 4-H model runs Purpose, Disciplinary Procedures, Immediate Action, where procedures genuinely are part B. Custer inserted its two behavior lists and the authority paragraph between them, pushing procedures from B to E, and the cross-reference never moved. Good-faith drafting artifact. Fixed by section name rather than letter so it cannot break again on the next insertion.
- **Enforced-by:** not applicable. No compliance check in this paragraph.
- **Base-text note:** the Code of Conduct is owned by CSU Extension, 4-H, and FFA, who collect the signatures from participant, parent or guardian, and volunteers. Rewriting it in CSF's voice would be the Fair Board editing another body's instrument, a harder sell to the working group than any rule inside it. Custer's text is retained as base; no CSF adoption sentence is printed here.
- **Cross-ref:** none. The divergence map does not reach Code of Conduct or Disciplinary Procedures at any finding ID.

#### FB-DISCIPLINE-01 · DISCUSS-AT-WALKTHROUGH (prints greyed beneath part E)

- **Old Custer text:** authority stated three different ways across four paragraphs, and a flat nine-item sanctions list with no ordering, no link between offense type and sanction, and no treatment of priors: "Sanctions may include some or all the following: Verbal warning / Notification to parents / Immediate removal from the fair / Premium penalties or withholdings / Being placed on a behavior contract / Referral to local law enforcement / Program suspension and/or / Expulsion from the fair / Other sanctions appropriate to the circumstances, as determined by the Fair Board, 4-H staff, FFA personnel".
- **Proposed text (greyed, not in draft):** two tiers.
  - *First-response tier.* Any single actor from the existing broad list (Fair Board, 4-H leaders, FFA advisor and advisory board members, superintendents, county or CSU Extension personnel) may impose: verbal warning; notification to parents; immediate removal from the fair; premium penalties or withholdings; behavior contract; or another sanction of equivalent weight.
  - *Severe tier.* Requires the concurrence of the Fair Board President, the Extension Director (or the FFA Advisor where the matter is FFA-specific), and the relevant department Superintendent. Concurrence need not be in person or simultaneous; phone or text counts. Sanctions: program suspension or expulsion, treated as a single severe-removal sanction whose duration is set by the concurring three at the time of imposition and may run from the current fair through a stated multi-year period; referral to local law enforcement; or another sanction of equivalent weight.
  - *Auto-escalation.* A third first-response sanction against the same participant in the same fair triggers severe-tier review. Review, not automatic imposition of a severe sanction.
  - *Catch-all.* The existing "other sanctions appropriate to the circumstances" survives but is scoped inside whichever tier is acting, rather than sitting open outside the structure.
- **CSF cite:** General Competition Requirements §5, Determination of Violations, as structural model only, not adopted. CSF tiers penalties from division-level forfeiture, to fair-wide clawback, to a bar for a determined period including lifetime, and requires concurrence of the General Manager, Director, and Program Manager for the top tier. CSF's org chart has no Custer equivalent, so the roles are mapped rather than copied.
- **Reason for DISCUSS:** none of this exists in the current book and none of it is a direct CSF adoption. It is a hybrid built to answer a real gap, namely that the current list gives a board member standing in a barn no way to know which sanction fits which offense, who may impose it, or how prior incidents count. Three-strikes was chosen because the book already trains people on that pattern twice over (coaching interference and non-active participation, both cumulative), so it reads as consistency rather than new philosophy. The three-way concurrence is the structural answer to any accusation of self-dealing, given that every board member has children in the ring: three independent institutional bases, governance, county 4-H and FFA administration, and show-level expertise. This goes to the working group as a proposal carrying its reasoning, not as settled drafting.
- **Enforced-by:** not applicable to the tier structure itself. Referral to local law enforcement invokes the Custer County Sheriff's Office as the outside authority.
- **Cross-ref:** none.

#### FB-SOCIAL-01 · DISCUSS-AT-WALKTHROUGH (prints greyed beneath the Code of Conduct)

- **Old Custer text:** none. The book contains no social media or digital conduct language of any kind. Verified by full-text search of the source .docx. The Code of Conduct predates the medium.
- **Proposed text (greyed, not in draft):**

  > **Application to online conduct.** This Code of Conduct applies regardless of medium. Prohibited behavior counts the same online as it does on the fairgrounds.
  >
  > It applies when a person is targeted because of their role in the Custer County Fair, including judges, superintendents, Fair Board members, buyers, volunteers, Extension and FFA personnel, exhibitors, and exhibitors' families. The person need not be named if they are reasonably identifiable.
  >
  > This provision reaches harassment, threats, and abuse directed at a person. It does not reach criticism, and it does not restrict what exhibitors, families, or the public may say about the Fair, their own animals or projects, the Fair Board, its rules, or its decisions, or what they may say to prospective buyers.

- **CSF cite:** none directly. CSF reaches online conduct through the IAFE National Code of Show Ring Ethics, which CSF incorporates. Custer does not incorporate IAFE (zero occurrences in the county book), so IAFE cannot serve as the anchor here without first being adopted, which would be its own separate item. The clause therefore hangs on Custer's own Code of Conduct, which already binds by signature collected at the Extension office.
- **Reason:** the clause adds no new prohibited behavior. It states that the existing prohibitions are medium-neutral, which is why it can attach to a code participants already signed. The existing judge-contact rule already reaches contact "prior to or after" the Fair, so the clause substantially makes explicit what is arguably already present. The nexus is causal rather than proximity-based ("targeted because of their role"), so the question is why a person was targeted, answerable from the conduct itself, rather than how closely the conduct ties to the Fair, which is a judgment call. Coverage reaches exhibitors' families so a targeted minor who is not showing is not left out, and "reasonably identifiable" closes the unnamed-but-obvious case. The third paragraph is load-bearing rather than decorative: the limit on a county-appointed board's authority over criticism exists whether or not the book prints it, and printing it both proves the board never claimed that power and prevents the chilling effect of a bare prohibition that leaves a parent unable to tell whether posting about a bad call is sanctionable. The operating line is person versus decision. Abuse aimed at people is reachable; criticism of a decision is not.
- **Enforced-by:** the Code of Conduct's own disciplinary procedures. If FB-DISCIPLINE-01 is adopted this clause inherits the tier structure automatically; if not, it points at the existing nine-item sanctions list. No outside instrument or authority generates the compliance fact here, which is a departure from the neutral-enforcement pattern and should be named as such at the walkthrough.
- **Counsel review flag:** this is the paragraph in the book most needing county counsel review before adoption. Speech-adjacent rules imposed by a county-appointed body, applying to minors and their families, carry live legal exposure that careful drafting alone does not resolve.
- **Related, not drafted:** a photo and likeness consent provision was considered and closed as a verification item rather than a drafting item. No second consent document will be written. The open question is what release CSU Extension already collects and whether it covers Fair publication. See `fair/notes.md`.
- **Cross-ref:** none.
