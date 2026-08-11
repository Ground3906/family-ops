// Fairbook-Complete.docx generator — assembled walkthrough book, 8/10/2026 state.
// See section-line-map.md in this directory for source extraction (uw/*.txt) and regeneration.
// WORKED sections are hardcoded at their 8/10 state; regenerate from draft.md + delta-log as passes lock.
const { Document, Packer, Paragraph, TextRun, HeadingLevel, BorderStyle, ShadingType } = require("docx");
const fs = require("fs");

const US_LETTER = { width: 12240, height: 15840 };
const OLDFILL = "F1F1F1";
const OLDBAR = "999999";

function title(t) { return new Paragraph({ heading: HeadingLevel.TITLE, spacing: { after: 80 }, children: [new TextRun({ text: t })] }); }
function h1(t) { return new Paragraph({ heading: HeadingLevel.HEADING_1, spacing: { before: 440, after: 160 }, children: [new TextRun({ text: t, bold: true })] }); }
function usedToSay() { return new Paragraph({ spacing: { before: 100, after: 100 }, children: [new TextRun({ text: "WHAT IT USED TO SAY", bold: true, size: 19, color: "777777" })] }); }
function saysNow() { return new Paragraph({ spacing: { before: 300, after: 120 }, children: [new TextRun({ text: "WHAT IT SAYS NOW", bold: true, size: 20, color: "1F3A5F" })] }); }
function newOnly() { return new Paragraph({ spacing: { before: 100, after: 120 }, children: [new TextRun({ text: "NEW — no earlier version exists", bold: true, size: 19, color: "777777" })] }); }
function unchangedBanner() {
  return new Paragraph({ spacing: { before: 100, after: 140 },
    children: [new TextRun({ text: "UNCHANGED — current book text, not yet reworked. Queued for its department pass.", bold: true, size: 19, color: "777777" })] });
}
function old(t) {
  return new Paragraph({ spacing: { after: 120 }, shading: { type: ShadingType.CLEAR, fill: OLDFILL },
    border: { left: { style: BorderStyle.SINGLE, size: 16, color: OLDBAR, space: 8 } }, indent: { left: 200 },
    children: [new TextRun({ text: t, color: "555555" })] });
}
function body(t) { return new Paragraph({ spacing: { after: 140 }, children: [new TextRun({ text: t })] }); }
function boldLead(l, r) { return new Paragraph({ spacing: { after: 140 }, children: [new TextRun({ text: l, bold: true }), new TextRun({ text: r })] }); }
function subsubhead(t) { return new Paragraph({ spacing: { before: 140, after: 60 }, children: [new TextRun({ text: t, bold: true })] }); }
function bullet(t) { return new Paragraph({ spacing: { after: 100 }, indent: { left: 300 }, children: [new TextRun({ text: "•  " + t })] }); }
function subbullet(t) { return new Paragraph({ spacing: { after: 100 }, indent: { left: 560 }, children: [new TextRun({ text: "-  " + t })] }); }

function renderUnworked(children, filePath) {
  const lines = fs.readFileSync(filePath, "utf8").split("\n");
  for (const raw of lines) {
    const t = raw.trim();
    if (!t) continue;
    const letters = t.replace(/[^A-Za-z]/g, "");
    const isCapsHeader = letters.length > 3 && letters === letters.toUpperCase();
    if (isCapsHeader) children.push(subsubhead(t));
    else children.push(body(t));
  }
}

const children = [];

children.push(title("Custer County Fair Book"));
children.push(new Paragraph({ spacing: { after: 200 }, children: [new TextRun({ text: "Complete — As Written", bold: true, size: 30 })] }));
children.push(new Paragraph({ spacing: { after: 160 }, children: [new TextRun({ text: "The entire book, in book order. Assembled 8/10/2026.", italics: true, color: "555555" })] }));
children.push(new Paragraph({ spacing: { after: 300 }, children: [
  new TextRun({ text: "Grey blocks: ", bold: true }), new TextRun({ text: "what a reworked section used to say, kept for comparison. " }),
  new TextRun({ text: "Plain text: ", bold: true }), new TextRun({ text: "the book as it now reads. Sections marked UNCHANGED carry today's book text verbatim, awaiting their department pass — present, not omitted." }),
]}));

children.push(h1("Front Matter"));
children.push(newOnly());
children.push(subsubhead("Definitions"));
children.push(body("In this book, \"the Authority\" means the governance of the Custer County Fair, acting through the Custer County Fair Board, its committees, superintendents, 4-H leaders, FFA advisors and advisory board members, and county or CSU Extension personnel, each within the limits of their own assigned duties. Where a specific role is meant, this book names that role directly (the sale committee, a superintendent, the Fair Board President)."));
children.push(subsubhead("Versioning"));
children.push(body("This Fair Book carries a version number only: \"Custer County Fair Book — Version [N].\" No year is printed. The version number changes only when the Authority adopts a change to a printed rule."));
children.push(body("A companion document, the Addendum, carries every volatile fact this book refers to: the current schedule, roster and contacts, fees and premiums, current-year animal health requirements, enrollment and entry dates, grounds and locations, and forms. Its cover carries a year and revision number: \"[Year] Addendum, Revision [N].\" The current version of each document is posted at the Authority's designated official channel; the posted version controls."));
children.push(body("The Addendum is organized into seven numbered sections that never renumber across years: 1. Schedule. 2. Roster and Contacts. 3. Fees and Premiums. 4. Current-Year Animal Health Requirements. 5. Enrollment and Entry Dates. 6. Grounds and Locations. 7. Forms. Every form this book references is printed in Addendum Section 7, never in this book."));

children.push(h1("Fair Schedule"));
children.push(unchangedBanner());
children.push(body("Under the versioning system above, this entire section moves to Addendum Section 1 when the schedule rework runs; it prints here unchanged until then."));
renderUnworked(children, "uw/A-schedule.txt");

children.push(h1("General Rules"));
children.push(usedToSay());
children.push(old("Code of Conduct: purpose paragraph narrower than the code's own title (\"4-H, FFA, and Open Fair\") — spoke only of 4-H/FFA members and program goals. Judge-contact rule reached judges only, before/after the fair only. Sanctions: a flat nine-item list with no ordering, no offense-to-sanction link, no treatment of repeat incidents, imposable by a five-way actor list spelled out in full each time it appeared. Protest and Appeals: two conflicting processes in one book, $50/$100 fees printed inline, an 8-hour appeal window to an undefined \"Fair Board executive panel,\" and no review route at all for a sanctioned participant."));
children.push(saysNow());
children.push(body("Custer County 4-H, FFA, and Open Fair Code of Conduct and Disciplinary Procedures"));
children.push(body("Prior to participating, the Extension office must have the Code of Conduct signed by the participant, parent/guardian, and volunteers. For applicable participants, MQA certifications and animal care/housing forms are needed as well."));
children.push(body("By participating in the Custer County Fair as a participant, volunteer, or spectator you agree to the Code of Conduct."));
children.push(subsubhead("A. Purpose and application"));
children.push(body("The Code of Conduct is intended to foster a safe environment that is conducive to optimal learning and growth. All fair participants — 4-H and FFA members, Open Division exhibitors, leaders, parents, volunteers, and spectators — are expected to behave in a way that respects the rights and property of others and that will not disrupt or interfere with the fair or with 4-H or FFA program goals."));
children.push(body("This Code of Conduct and Disciplinary Procedure is a condition of participation in the Custer County Fair."));
children.push(subsubhead("B. Behaviors prohibited at the County Fair that warrant removal from fairgrounds:"));
children.push(bullet("Possession, selling, and/or use of marijuana, alcoholic beverages, tobacco products to include vapes/e-cigarettes, and/or illegal drugs, or being present where individuals are using alcohol, tobacco products, and/or any illegal substances."));
children.push(bullet("Abuse (physical and/or verbal) and harassment."));
children.push(bullet("Any kind of excessive public display of affection."));
children.push(bullet("Possession of weapons or firearms (except while participating in a shooting sports event)."));
children.push(bullet("Behavior that violates state or local laws."));
children.push(bullet("Damage to, theft of, or misuse or abuse of public or personal property."));
children.push(bullet("Conduct that jeopardizes the safety of self or others."));
children.push(bullet("Conduct that disrupts or interferes with the 4-H or FFA programming."));
children.push(bullet("Tampering with ribbons or state fair qualifier stickers by anyone except official fair staff."));
children.push(subsubhead("C. Behaviors that will be subject to Disciplinary Procedures:"));
children.push(bullet("Unsolicited contact with, or interference with, county fair judges, fair staff, or show officials in the performance of their duties, whether before, during, or after the Custer County Fair, is prohibited, other than contact with judges for learning opportunities. Judges' decisions are final."));
children.push(bullet("Participants in the Custer County Fair will be held to the 4-H and FFA Codes of Conduct, and the overall spirit within which they were established. Any 4-H or FFA member that has been reported to law enforcement because of a violation on the Custer County Fairgrounds or Rodeo grounds during fair week will be subject to disciplinary actions including but not limited to: disqualification from show, and/or sale, and/or loss of sale premiums, or other consequences as deemed appropriate by the Authority. Anyone banned from the Rodeo grounds will also be banned from the Fairgrounds and will forfeit all rights to participate in any show or sale."));
children.push(bullet("Inappropriate dress. Clothing should meet the standards expected in Custer County public schools. The following Colorado State 4-H dress code has been developed to provide participants and spectators with the best experience and will be enforced for all individuals attending 4-H events and activities, including chaperones. If you choose to dress inappropriately, you will be required to change."));
children.push(subbullet("All clothing shall be neat, clean, acceptable in repair and appearance, and shall be worn within the bounds of decency and good taste as appropriate for 4-H events and activities."));
children.push(subbullet("Articles of clothing which display profanity, products, or slogans which promote tobacco, alcohol, drugs, or sex, or are in any other way distracting, are prohibited."));
children.push(subbullet("Excessively baggy or tight clothing which advertises gang symbols or affiliation is prohibited."));
children.push(subbullet("Items of clothing which expose bare midriffs, bare chests, undergarments, or that are transparent (see-through) are prohibited."));
children.push(subbullet("Tank tops with straps wider than one inch are permitted. Shirts which expose a bare back, halter tops, and tube tops are prohibited."));
children.push(subbullet("Shorts must be mid-thigh length; cut-off shorts or short-shorts are not allowed."));
children.push(subbullet("Hats need to be removed for meetings, workshops, meals, and at other times when asked to remove them."));
children.push(subbullet("Shoes must be worn at all times."));
children.push(subsubhead("D."));
children.push(body("The Authority may impose discipline as set out below in cases of misconduct by current, former, or prospective 4-H participants if, in the judgement of the personnel involved, the misconduct poses a potential risk to the 4-H or FFA program or is in violation of the 4-H and FFA Codes of Conduct. This includes risks to the safety or well-being of others and risks to the effective functioning or integrity of 4-H and FFA."));
children.push(subsubhead("E. Disciplinary Procedures"));
children.push(body("Discipline may be imposed by any part of the Authority with oversight responsibility at the Custer County Fair."));
children.push(body("Unless otherwise outlined in this fair book, or in cases where immediate action is required, the following procedures must take place before there is a finding or conclusion of guilt: the accused participant shall be told which prohibited behavior he or she is accused of violating; the factual evidence will be shared with the accused participant; and the accused participant will be given a chance to tell his or her side of the story."));
children.push(body("The Authority must be satisfied that the participant, more likely than not, engaged in the prohibited behavior before imposing a sanction. Sanctions follow two tiers."));
children.push(boldLead("First-response tier. ", "Any single actor within the Authority may impose: a verbal warning; notification to parents; immediate removal from the fair; premium penalties or withholdings; a behavior contract; or another sanction of equivalent weight."));
children.push(boldLead("Severe tier. ", "Program suspension or expulsion, referral to local law enforcement, or another sanction of equivalent weight, requires the concurrence of the Fair Board President, the Extension Director (or the FFA Advisor where the matter is FFA-specific), and the relevant department Superintendent. Concurrence need not be in person or simultaneous. A suspension or expulsion's duration is set by the concurring three at the time of imposition and may run from the current fair through a stated multi-year period."));
children.push(body("A third first-response sanction against the same participant in the same fair triggers severe-tier review. Other sanctions appropriate to the circumstances may be imposed within whichever tier is acting, as determined by the Authority."));
children.push(subsubhead("Protest and Appeals"));
children.push(boldLead("Scope. ", "A protest may be filed by any person to report an alleged violation of fair rules or unethical activity. Judges' decisions on placings are final and are not subject to protest. A judging procedure conducted contrary to the printed rules may be protested as a rule violation."));
children.push(boldLead("Filing. ", "The protest must be in writing on the protest form printed in the current Addendum, Section 7 (Forms), accompanied by the protest fee stated in the current Addendum, Section 3 (Fees and Premiums), in cash or certified check, and delivered to the fair office. The protest must include the name and contact information of the person filing, the name of the exhibitor or entry in question, the specific allegations and supporting facts, and the specific rule provisions alleged to have been violated, with a signed certification that the contents are true to the best of the filer's knowledge. The protest fee will be refunded if the matter is resolved in favor of the person bringing the protest."));
children.push(boldLead("Deadline. ", "For livestock activities, protests must be delivered no later than 24 hours after the alleged infraction. For all other activities, protests must be delivered before the official close of the fair. Judging will not be interrupted by a protest."));
children.push(boldLead("Review. ", "Upon receipt, the Fair Board President or designee will determine the same day whether the protest is timely, complete, and states a specific rule violation; a protest denied at this step is denied in writing with reasons stated. A valid protest is referred to a committee of three disinterested, qualified persons appointed by the Fair Board President and the Extension Director. A person is disinterested if he or she has no entry and no immediate-family entry in the affected department and is not the subject of, a witness to, or a participant in the events protested. The committee issues a written resolution within 24 hours of appointment; the President may grant one extension for good cause, stated in writing."));
children.push(boldLead("Appeals. ", "A protest resolution may be appealed by the person who filed the protest. A sanction imposed under the Disciplinary Procedures may be appealed by the sanctioned participant if the sanction includes removal from the fair, premium penalties or withholdings, program suspension, or expulsion; a verbal warning, notification to parents, or placement on a behavior contract is final when imposed."));
children.push(boldLead("Appeal filing. ", "An appeal must be in writing on the Appeal Form printed in the current Addendum, Section 7 (Forms), and delivered no later than 24 hours after delivery of the written protest resolution or written sanction. An appeal of a protest resolution must be accompanied by the appeal fee stated in the current Addendum, Section 3 (Fees and Premiums), in cash or certified check, refunded if resolved in favor of the person bringing the appeal; no fee is charged for a participant's appeal of a sanction."));
children.push(boldLead("Appeal panel. ", "The appeal is decided by a panel of three: a Fair Board member presiding (the President, or where the President is conflicted or unavailable, another Board member selected by the Board), one person qualified in the subject matter of the competition, and one member of the public or Extension or FFA personnel. A person who imposed or concurred in the sanction under appeal may not serve. The panel's decision is final."));
children.push(body("At any time before the appeal panel issues its decision, the review committee or the sanctioning authority may vacate its resolution or sanction in full in favor of the appealing party; any fees paid are refunded."));
children.push(body("Premiums and sale proceeds attributable to an entry or exhibitor that is the subject of a pending protest, appeal, or unresolved sanction will be held until final resolution."));
children.push(body("Compliance with this protest and appeal process is mandatory prior to seeking review in any other forum."));
children.push(subsubhead("F. Immediate action situations"));
children.push(body("The Authority may take immediate action to remove a participant from the fairgrounds and other action as needed, where there is an emergency or significant risk of continuing misconduct. In those cases, the immediate action is temporary discipline and the procedures set out under Disciplinary Procedures above must be arranged as soon as possible but in no event longer than seven days from the temporary discipline."));
children.push(subsubhead("Application to online conduct"));
children.push(body("This Code of Conduct applies regardless of medium. It applies when a person is targeted because of their role in the Custer County Fair, including judges, superintendents, Fair Board members, buyers, volunteers, Extension and FFA personnel, exhibitors, and exhibitors' families. The person need not be named if they are reasonably identifiable."));
children.push(body("This provision reaches harassment, threats, and abuse directed at a person. It does not reach criticism, and it does not restrict what exhibitors, families, or the public may say about the Fair, their own animals or projects, the Fair Board, its rules, or its decisions, or what they may say to prospective buyers."));
children.push(subsubhead("Official Fair Communications"));
children.push(body("Official communication channels of the Custer County Fair are those designated by the Fair Board and listed in the current Addendum. Channels not designated by the Fair Board are not official communications of the Fair."));
children.push(body("Only persons designated by the Fair Board may publish to official channels. Statements on behalf of the Fair are made by the Fair Board President or the President's designee. Committees and superintendents acting within their assigned duties are designated for those duties."));
children.push(body("No person may represent a personal account, post, or statement as an official communication of the Fair. Violations of this provision by fair participants are subject to the disciplinary procedures of the Code of Conduct."));
children.push(subsubhead("Reservation of Authority"));
children.push(body("Custer County acknowledges and adopts the Colorado State Fair General Competition Requirements reservation of authority: \"The Authority reserves to itself the final and absolute right to interpret these competition requirements and to fairly and impartially settle and determine all matters, questions, and differences in regard thereto.\""));
children.push(body("Where these rules prescribe a maximum penalty or consequence, the Authority may reduce, suspend, or waive that penalty or consequence where circumstances warrant. The Authority may never impose a penalty or consequence greater than these rules prescribe."));

children.push(h1("Fair Board, Staff, and Superintendents"));
children.push(unchangedBanner());
children.push(body("Under the versioning system above, this roster moves to Addendum Section 2 when its pass runs; it prints here unchanged until then."));
renderUnworked(children, "uw/B-roster.txt");

children.push(h1("County Shooting Sports"));
children.push(unchangedBanner());
renderUnworked(children, "uw/C-shooting.txt");

children.push(h1("4-H Family Consumer Science & General Projects"));
children.push(unchangedBanner());
renderUnworked(children, "uw/D-fcs.txt");

children.push(h1("4-H & FFA Market Eligible Livestock and Poultry"));
children.push(unchangedBanner());
children.push(body("This section — the market livestock general rules and the Beef, Swine, Sheep, and Goat department rules — carries today's book text verbatim. The drug-testing direction (consent-to-testing; champions may be tested) is adopted in principle; its final wording lands when this section's pass runs."));
renderUnworked(children, "uw/E-market.txt");

children.push(h1("4-H & FFA Horse"));
children.push(unchangedBanner());
renderUnworked(children, "uw/F-horse.txt");

children.push(h1("4-H & FFA Non-Market Livestock and Small Animal"));
children.push(unchangedBanner());
renderUnworked(children, "uw/G-nonmarket.txt");

children.push(h1("Companion Animal Master Showmanship"));
children.push(unchangedBanner());
renderUnworked(children, "uw/H-camaster.txt");

children.push(h1("Showmanship and Master Showmanship"));
children.push(unchangedBanner());
renderUnworked(children, "uw/I-showmanship.txt");

children.push(h1("Livestock Sale"));
children.push(usedToSay());
children.push(old("Sale: Saturday, July 18, 2026, 12:00 pm printed in the book itself; remove unsold exhibits before 9:00 am Saturday. Notify the sale committee one hour after the beef show; a miss may default to selling the lightest animal. Animals do not have to be sold, but a sold project is \"terminated\" — defined as exhibition-only, so the animal itself was never restricted. Animals cannot be withdrawn after entering the sale ring. \"Arrangements for the payment, trucking, slaughter, and processing of private sale animals must be taken care of by the exhibitor.\" No sale-specific consequence for a no-show. Wholesome Meat Act: on a residue finding, \"exhibitor forfeits all rights to the sale price\" — automatic and mandatory. No poultry ruleset anywhere in the book."));
children.push(saysNow());
children.push(subsubhead("4-H & FFA Livestock Sale"));
children.push(body("The sale is held on the date and at the time stated in the current Addendum, Section 1 (Schedule)."));
children.push(body("All livestock exhibits not being sold must be removed from the fairgrounds by the time stated in the current Addendum, Section 1 (Schedule)."));
children.push(subsubhead("General rules"));
children.push(body("Market livestock sale rules will be reviewed on an annual basis with changes made as needed."));
children.push(body("An exhibitor may sell no more than two market animals at the Market Livestock Sale, and they must be of different species. In addition, an exhibitor may sell one meat pen of rabbits."));
children.push(body("All Grand Champion and Reserve Grand Champion market animals will sell. This applies in every market species and is not limited by the sale limit above. An exhibitor who wins championships in more than two species will sell all of those champions."));
children.push(body("The only case in which one exhibitor sells two market animals of the same species is when that exhibitor owns both the Grand Champion and the Reserve Grand Champion of that species. Both animals will sell."));
children.push(body("The sale order will be determined by the sale committee or Fair Board."));
children.push(body("Official sale information will be available on the day of the sale at the sale ring and the posted sale information board at the fairgrounds, and on any official channels designated by the Fair Board. Any corrections or changes to sale information will be posted to the same locations and channels. Sale information published at these locations and channels controls over information from any other source. Among official postings, the sale sheet maintained at the auction podium, including any hand-marked corrections announced during the sale, is the controlling record."));
children.push(body("In order to sell market beef animals, each exhibitor must present a bill of sale to the brand inspector prior to the sale."));
children.push(body("The sale weight will be the weight established at the weigh-in."));
children.push(body("Market goats (wethers or does) must weigh a minimum of 55 lbs. and must be a milk-tooth goat to be eligible to sell."));
children.push(body("Market swine must weigh a minimum of 220 lbs. and a maximum of 290 lbs. If swine is over 290 lbs, it can still be sold, but is not eligible for competition."));
children.push(body("Market sheep must weigh a minimum of 105 lbs. and no maximum."));
children.push(body("Market beef must weigh a minimum of 1,000 lbs. and no maximum."));
children.push(subsubhead("Exit election, terminal sale, and custody"));
children.push(body("An exhibitor who does not wish to sell a declared market animal must notify the sale committee by one hour after the conclusion of the beef show. An animal not withdrawn by this deadline is consigned to the sale. Consignment is absolutely terminal: ownership transfers at the close of bidding for that animal and does not reverse for any reason. Grand Champion and Reserve Grand Champion market animals may not be withdrawn under this election."));
children.push(body("The notification described above is the sale committee's paperwork instrument for building the sale lot list. Failure to notify by the deadline may result in the undeclared animal being consigned to the sale at floor market price, as set annually by the sale committee with the floor buyer, rather than through the auction ring. The Authority may reduce this consequence where circumstances warrant."));
children.push(body("From the close of the exit election until delivery, a consigned sale animal may not leave the fairgrounds except by delivery to the slaughter-processing facility designated below. The exhibitor remains responsible for the animal's care, feeding, and daily custody through the night before delivery."));
children.push(body("The Authority is responsible for the delivery of every sale animal to the slaughter-processing facility designated for that animal. Delivery takes place the morning after the sale. The exhibitor's care and custody of the animal end when the animal is loaded for delivery; the exhibitor is not part of the delivery. Where a purchaser requests that an animal be held before slaughter to allow the animal to rest, that holding is arranged by the Authority within the facilities designated below, never by the exhibitor, and any cost of holding is withheld from the sale proceeds like any other delivery cost."));
children.push(body("A sale animal will not be released to the exhibitor, the exhibitor's family, or any other person at any time after consignment. The only way a consigned sale animal leaves the fairgrounds is delivery to the designated slaughter-processing facility."));
children.push(boldLead("Sale custody and destination. ", "Custer County acknowledges and adopts the following from the CSF Junior Livestock Sale Participation Requirements: \"The Sale is a terminal sale, and all livestock sold will go to slaughter.\" \"Animals going to custom slaughter will be sent to a slaughtering facility designated by the Authority.\" \"No animal will be sent to any other individual packer or slaughterhouse.\" \"The Authority is responsible for the delivery of sale animals to the slaughter-processing facility.\""));
children.push(body("Purchase of a sale animal conveys the right to the processed product only, including the buyer's processing instructions at the designated facility. No purchase conveys any right to possession of a live animal. Possession of a live sale animal does not transfer to any buyer at any time. No sale animal may be returned, gifted, resold, or released as a live animal to the exhibitor, the exhibitor's family, or any other person, for any reason."));
children.push(body("The Authority designates, for each sale year, one or more facilities holding a valid USDA inspection for animals intended for resale, and may additionally designate one or more custom-exempt facilities for purchasers taking product for their own use."));
children.push(body("If a veterinarian certifies that a consigned sale animal cannot be sold because of illness, injury, death, or because a medication's withdrawal period has not lapsed by delivery, the sale committee will purchase the animal at floor market price. The exhibitor's animal is credited to the sale at that price, and the exhibitor is not subject to the consequences for failure to show in the sale for that animal. Disposition of the animal follows the veterinarian's direction."));
children.push(subsubhead("Failure to show in sale"));
children.push(body("Custer County acknowledges and adopts the following from the CSF Junior Livestock Sale Participation Requirements, Failure to Show in Sale: failure to show a consigned animal in the Market Livestock Sale, other than an animal excused under the illness, injury, or death provision above, will result in the exhibitor forfeiting all awards, recognitions, and premiums earned at the Custer County Fair that year, and being barred from showing any exhibit on the Custer County fairgrounds for three years."));
children.push(body("Only bona fide 4-H age youth (no associate member 4-H youth) and FFA youth are eligible to sell at the market livestock sale."));
children.push(subsubhead("United States Department of Agriculture Wholesome Meat Act"));
children.push(body("All members participating in the Livestock Sale must sign and return a copy of this act to the fair office with their sale slip. The Wholesome Meat Act Disclosure is printed in the current Addendum, Section 7 (Forms)."));
children.push(body("The United States Department of Agriculture Wholesome Meat Act applies to the sale of market livestock sold during the Custer County Fair as follows:"));
children.push(bullet("Animals must be in good health and carcasses free of drug or chemical residues."));
children.push(bullet("Antibiotics and sulfonamides have required withdrawal periods."));
children.push(bullet("Drug label directions for use and withdrawal periods apply."));
children.push(body("If drug or other chemical residues are found in the tissue of carcasses, the entire carcass may be condemned. Custer County acknowledges and adopts the following from the CSF Junior Livestock Sale Participation Requirements: \"Payment to the exhibitor will not be made until all testing results have been received and declared negative or non-suspect.\" \"If for any reason any animal is condemned at slaughter, whether by testing results or by any USDA-inspector condemnation, the Authority may withhold any payment due the exhibitor.\" \"The Authority is not liable for any breaches of contracts between the seller and buyer as a result of any condemnation or any other matter.\" Before administering antibiotics and/or sulfonamides, consult a licensed and practicing veterinarian, or label directions of the drug."));
children.push(body("To be eligible to sell market animals, all exhibitors and parents are required to sign a copy of the Wholesome Meat Act Disclosure. This is to be turned into the sale committee no later than one hour after the market beef show."));

children.push(h1("Market Poultry"));
children.push(newOnly());
children.push(body("Market Chickens are sold as a pen of three birds; an exhibitor may enter up to four Market Chicken pens. Each bird in a pen must carry an individual numbered leg or wing band. Market Turkeys are sold as single birds."));
children.push(body("Market poultry sells at the Market Livestock Sale on the same terms as other market animals. A declared Market Chicken pen or Market Turkey counts toward an exhibitor's two-species sale limit under the sale limits rule above, except that one pen of Market Chickens or one meat pen of rabbits, exhibitor's choice, may be sold in addition to that limit. All Grand Champion and Reserve Grand Champion Market Chicken pens and Market Turkeys will sell, on the same terms as the required champion sales rule above."));
children.push(body("Market poultry follows the same exit election, deadlines, and terminal-sale provisions as every other market species under this section."));
children.push(body("Only birds and pens consigned to the Market Livestock Sale are terminal. A market bird or pen an exhibitor elects not to sell goes home with the exhibitor, the same as any other market species."));
children.push(body("Every Market Chicken and Market Turkey must be inspected on arrival during the Authority's scheduled arrival window. A bird showing signs of illness will not be allowed on the fairgrounds. If a bird becomes ill or dies while on the fairgrounds, the exhibitor must report it immediately to a Fair Board member or the poultry superintendent, who will contact the Authority's veterinarian. Every bird must carry a premises identification (PID) number at the time of entry and an individual numbered leg or wing band. Exhibitors and their poultry must comply with current Colorado Department of Agriculture exhibition health requirements for poultry, as summarized in the current Addendum, Section 4 (Current-Year Animal Health Requirements)."));

children.push(h1("Open Division and Indoor Divisions"));
children.push(unchangedBanner());
renderUnworked(children, "uw/J-open.txt");

const doc = new Document({ sections: [{ properties: { page: { size: US_LETTER, margin: { top: 1440, bottom: 1440, left: 1440, right: 1440 } } }, children }] });
Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync("Fairbook-Complete.docx", buf);
  console.log("Written:", buf.length, "bytes,", children.length, "blocks");
});
