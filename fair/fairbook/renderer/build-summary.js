const { Document, Packer, Paragraph, TextRun, HeadingLevel, PageBreak, BorderStyle, LevelFormat,
        AlignmentType, Footer, PageNumber, TabStopType, TabStopPosition } = require('docx');
const fs = require('fs');
const FONT = 'Cambria';

const P = (parts, opts = {}) => new Paragraph({
  children: (Array.isArray(parts) ? parts : [parts]).map(p => typeof p === 'string'
    ? new TextRun({ text: p, font: FONT, size: 22 })
    : new TextRun({ text: p.t, bold: !!p.b, font: FONT, size: 22 })),
  spacing: { after: 150, line: 276 }, ...opts,
});
const BUL = parts => new Paragraph({
  children: (Array.isArray(parts) ? parts : [parts]).map(p => typeof p === 'string'
    ? new TextRun({ text: p, font: FONT, size: 22 })
    : new TextRun({ text: p.t, bold: !!p.b, font: FONT, size: 22 })),
  numbering: { reference: 'bul', level: 0 }, spacing: { after: 110, line: 276 },
});
const H2 = t => new Paragraph({
  heading: HeadingLevel.HEADING_2, outlineLevel: 1, spacing: { before: 300, after: 130 }, keepNext: true,
  children: [new TextRun({ text: t, bold: true, font: FONT, size: 25, color: '000000' })],
});
const H1 = t => new Paragraph({
  heading: HeadingLevel.HEADING_1, outlineLevel: 0, spacing: { before: 120, after: 200 },
  children: [new TextRun({ text: t, bold: true, font: FONT, size: 32, color: '000000' })],
});
const OLD = q => P([{ t: 'The old Custer County book said: ', b: true }, q], { keepNext: true, keepLines: true });
const DID = s => P([{ t: 'What we did: ', b: true }, s], { keepNext: true, keepLines: true });
const REF = r => P([{ t: 'Read it at: ', b: true }, r], { keepLines: true });

const footer = title => new Footer({
  children: [new Paragraph({
    tabStops: [{ type: TabStopType.RIGHT, position: TabStopPosition.MAX }],
    border: { top: { style: BorderStyle.SINGLE, size: 4, space: 6, color: '999999' } },
    children: [
      new TextRun({ text: title, font: FONT, size: 18, color: '444444' }),
      new TextRun({ text: '\t', font: FONT, size: 18 }),
      new TextRun({ text: 'Page ', font: FONT, size: 18, color: '444444' }),
      new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 18, color: '444444' }),
      new TextRun({ text: ' of ', font: FONT, size: 18, color: '444444' }),
      new TextRun({ children: [PageNumber.TOTAL_PAGES], font: FONT, size: 18, color: '444444' }),
    ],
  })],
});

const c = [];

c.push(new Paragraph({ spacing: { after: 60 }, children: [new TextRun({ text: 'Custer County Fair Book', bold: true, font: FONT, size: 40 })] }));
c.push(new Paragraph({
  spacing: { after: 320 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 8, space: 8, color: '000000' } },
  children: [new TextRun({ text: 'Summary of Major Changes', font: FONT, size: 28 })],
}));

c.push(H2('Rewrite Goals'));
c.push(P(['Wherever it was possible, this book was aligned to the Colorado State Fair book. That is why the look, the feel, and the references all run off the state book.']));
c.push(P(['The reason for aligning is to establish the norm. When a parent asks why a rule exists, the answer is that this is the standard every fair in Colorado competes under, not that the Custer County Fair Board decided it. That takes the heat off this board and puts it where it belongs.']));
c.push(P(['The rules were also tightened into something a person can actually follow in the heat of the moment, in a barn, with a line of exhibitors waiting.']));
c.push(P(['And the Fair Board was pulled out of the vast majority of the book and replaced with a defined term, the Authority. The Authority is whoever is competent to make that particular call: the Fair Board, the superintendent in their own department, the judge in the ring, the veterinarian on animal health, Extension on eligibility, the sale committee on the sale. It flexes to the situation instead of routing everything through one body.']));

c.push(H2('The Addendum'));
c.push(P(['The information that changes from one year to the next was pulled out of the book and put into the Addendum. Dates, times, fees, weights, deadlines, the roster, the schedule, the forms. The rule points at the Addendum section that carries it.']));
c.push(P(['That is what makes this maintainable. The Addendum is one document and it is the only thing that has to be updated every year. It is our one stop shop as a board. Look at what actually came up during the fair. If a rule needs to change because of it, change that rule. If nothing came up, the book stays exactly as it is and the only work is refreshing the Addendum with next year’s dates, weights, and names.']));

c.push(H2('1. The sale is now terminal'));
c.push(OLD('"Market animals do not have to be sold. However, if sold, the project is terminated." And separately: "Arrangements for the payment, trucking, slaughter, and processing of private sale animals must be taken care of by the exhibitor."'));
c.push(DID('Every animal sold in the sale goes to slaughter. Custody moves from the exhibitor to the Fair at the sale ring and stays there until the animal is loaded. A buyer gets the processed product, never a live animal.'));
c.push(REF('CC 4.1.1, CC 4.3.2, CC 4.4.1, CC 4.4.3'));

c.push(H2('2. Managing barn space and growth'));
c.push(OLD('"Space priority in the livestock and small animal barns will be given to Senior 4-H and FFA members." The old book set no limit at all on how many market animals of a species one exhibitor could bring.'));
c.push(DID('The barn is a fixed size and we are running out of it. Every exhibitor is now guaranteed one pen, stall, or cage in each species they enter. Seniority still sets the order of assignment, it just no longer decides who gets space at all. Exhibitors may combine their assigned spaces by agreement. And for the first time there is one entry limit, the same number for every species, so the fair can plan the barn against a known ceiling instead of guessing.'));
c.push(REF('CC 3.1.15, CC 6.1.4, CC 3.1.4, and Addendum Section 5 for the number'));

c.push(H2('3. A structured disciplinary system'));
c.push(OLD('"Coaching / cueing / whistling / calling by parents from outside the show ring during the show is not allowed. Written warnings will be issued to the parent. After the third warning the 4-H or FFA member will be disqualified from the competition. Warnings are cumulative between species."'));
c.push(DID('The old book ran two separate three-strike ladders in two places with different triggers and different consequences. There is now one ladder that every rule runs through unless that rule states its own consequence.'));
c.push(BUL([{ t: 'Carried forward: adults are covered. ', b: true }, 'The old book already issued warnings to the parent and disqualified the member on the third. The new book states the whole set: parents, grandparents, siblings, leaders, volunteers, fitters, trainers.']));
c.push(BUL([{ t: 'New: anyone sanctioned can appeal. ', b: true }, 'Including on a first written warning. A parent may file for a member under 18. A sanction under appeal is not recorded until the appeal is decided, and one overturned is never recorded.']));
c.push(REF('CC 2.7 for the ladder, CC 2.8 for the appeal'));

c.push(H2('4. The show ring dress code'));
c.push(OLD('"4-H & FFA members must wear appropriate clothing while exhibiting their projects and during the sale. (Long sleeve shirts/blouses, nice jeans or trousers, and closed toe shoes. No sandals. No hats. No gum or tobacco.)"'));
c.push(DID('The general dress code is now generic and matches the state standard. Our old one was stricter than the state requires of its own exhibitors. Where a department needs something different, that lives in that department, which puts the call in the superintendent’s hands. The general rule also finally carries a consequence: an improperly dressed exhibitor can be refused entry to the ring until they change.'));
c.push(REF('CC 2.22, plus each department for its own deviation'));

c.push(H2('5. The Authority replaces the superintendent standing alone'));
c.push(OLD('"Superintendents have the authority to deal with hardship cases." "All animals must remain on the fairgrounds until released by the superintendents." "Any exhibit, record book or ribbon may be released at the discretion of the superintendent." Nine rules in the old book vested a responsibility in a superintendent alone.'));
c.push(DID('Those responsibilities now read as a decision of the Authority with the superintendent of the department as lead. The superintendent still runs the show and is still named first. What changes is that the Fair Board can act when it has to, and a superintendent is not standing alone on a call that turns into a grievance. The formula now appears eighteen times in the book, because it was also applied to rules that did not exist before.'));
c.push(REF('CC 1.12 for the definition, then look for the phrase "with the superintendent of the department as lead" throughout'));

c.push(H2('6. What happens to an animal after the sale'));
c.push(OLD('Nothing. The old book named no processors, no floor buyers, and no chain of custody after the sale. It said only that the exhibitor arranged trucking, slaughter, and processing.'));
c.push(DID('This whole mechanic is new. The Fair now designates the processing facilities and separately designates the floor buyer for each market species, and both get published in the Addendum. Custody runs from the exhibitor to the Fair at the sale ring, then to the processor’s truck. A buyer may ask for the animal to be rested before slaughter and the Fair arranges it inside that chain, with the buyer paying the holding cost rather than it coming out of the exhibitor’s check.'));
c.push(P([{ t: 'The part to discuss: ', b: true }, 'a floor buyer approved by the Fair Board may take live delivery of a floored animal that has not reached market finish and feed it out. That buyer has three months to produce a certified receipt from a licensed auction or a slaughter facility for every animal taken, identified by its fair weigh-in tag. A buyer who does not produce it can be barred from the fair in any capacity.']));
c.push(REF('CC 4.4.1 through CC 4.4.5, and CC 4.6.2 for who pays'));

c.push(H2('7. The veterinarian now decides'));
c.push(OLD('"All exhibits are to display good health. Any animal showing evidence of poor health that renders the animal unfit for human consumption may be excused from the grounds immediately following a decision from the review committee." The vet’s only named jobs were a slaughter readiness check, the heifer pregnancy certificate, and a call on a bitch in heat.'));
c.push(DID('The licensed veterinarian is now named in the book as the Authority on animal health, fitness, and slaughter readiness, and may refuse or excuse any animal. The book also hands the veterinarian a concrete list of expected duties.'));
c.push(P([{ t: 'Why it matters here: ', b: true }, 'the disqualifying fact now comes from a licensed outside professional, not from this board. This is the structural answer to anyone who says the board plays favorites.']));
c.push(REF('CC 1.12.1(d), CC 2.14, CC 3.2.2, CC 3.2.3, CC 3.4.8a, CC 3.4.9, CC 3.5.8, CC 3.6.2, CC 4.4.6 or rolled up in the Veterinary Services Agreement.'));

c.push(H2('8. A written exam in Master Showmanship'));
c.push(OLD('"The Champion Senior, Intermediate, and Junior Showmen from the Horse, Beef, Swine, Sheep, and Goat shows will compete in the Master Showmanship Contest." Nothing in that section mentions a written test. The fair\'s only written test was in the horse project, where it already counts toward Grand Champion and the buckle.'));
c.push(DID('Master Showmanship now includes a written exam covering Market Beef, Market Goat, Market Lamb, Market Swine, and Horse, counting thirty percent of the overall score. This is what the state contest requires of the exhibitor who goes on to represent Custer County.'));
c.push(REF('CC 7.2.3a'));

c.push(new Paragraph({ children: [new PageBreak()] }));
c.push(H1('Decision Points for the Fair Board'));

c.push(H2('A. How indoor projects are judged'));
c.push(P(['Two ways exist to award ribbons. One ranks the exhibits against each other, so in a class of twelve there is one blue, one red, one white, and nine kids with nothing. The other rates each project against what that project should be, so every kid who did good work goes home with a good ribbon.']));
c.push(P(['Everything at the fair uses the first, except indoor projects and the dog project, which use the second. That split is not new. It came straight out of the old book.']));
c.push(P(['Both of those departments follow Colorado 4-H documents the county does not control, and a member taking a project to state would be judged one way here and another way there.']));
c.push(P([{ t: 'The question: ', b: true }, 'does the board want to change it anyway.']));
c.push(REF('CC 9.11, CC 6.4.7'));

c.push(H2('B. Who decides when the barn is full'));
c.push(P(['Every exhibitor is guaranteed one space. When a species has more entries than there are spaces, that guarantee gives way and the Fair Board and superintendent may limit how much space each exhibitor gets.']));
c.push(P(['That is open ended on purpose, because no printed formula survives contact with a barn that is genuinely full.']));
c.push(P([{ t: 'The question: ', b: true }, 'does the board want that room to move, or a printed formula it has to live with.']));
c.push(REF('CC 3.1.15'));

c.push(H2('C. The accessibility gap'));
c.push(P(['The book now prints a commitment that the fair is accessible to people with disabilities.']));
c.push(P(['The grounds have no designated accessible parking at either entrance.']));
c.push(P([{ t: 'The question: ', b: true }, 'these two facts need to be true at the same time. What is the plan.']));
c.push(REF('The ADA statement in the front matter'));

c.push(H2('D. Three things the book points at and leaves to the board'));
c.push(P([{ t: 'Who holds the discipline record. ', b: true }, 'The book tells families that warnings are permanent. It never says who keeps the ledger.']));
c.push(P([{ t: 'Where a buyer’s refunded money goes. ', b: true }, 'The book says a refund may be donated to the Custer County Fair. It names no recipient.']));
c.push(P([{ t: 'How an official fair communication channel gets designated. ', b: true }, 'The book points families at a list of official channels. The list is empty.']));
c.push(REF('CC 2.7, CC 2.9, and Addendum Section 10'));

c.push(new Paragraph({ children: [new PageBreak()] }));
c.push(H1('The Way Ahead'));

c.push(H2('The department chapters have not been deep dived'));
c.push(P(['This rewrite took each project chapter largely as it was written and brought it up to the new standard. It did not re-examine the rules inside each department. That work is still owed.']));
c.push(P(['Each chapter routes to its superintendent or project leader. They screen their own department, mark it up, and their changes come back to the Fair Board for adoption or rejection. Same loop we are running now, pushed out to the people who know each department best.']));

c.push(H2('Still open'));
c.push(BUL(['Four Addendum tables are still blank and need the board and the sale committee to fill them: phone numbers for the board and superintendents, the 4-H club leader roster, the designated processors, and the floor buyers by species.']));

const doc = new Document({
  numbering: { config: [{ reference: 'bul', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•',
    alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 460, hanging: 260 } } } }] }] },
  styles: { default: { document: { run: { font: FONT, size: 22 } } } },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1440, right: 1440, bottom: 1180, left: 1440 } } },
    footers: { default: footer('Fair Book: Summary of Major Changes') },
    children: c,
  }],
});

Packer.toBuffer(doc).then(b => {
  fs.writeFileSync('/mnt/user-data/outputs/Fair Book - Summary of Major Changes.docx', b);
  console.log('summary written', b.length);
});
