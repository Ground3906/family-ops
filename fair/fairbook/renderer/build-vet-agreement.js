const { Document, Packer, Paragraph, TextRun, HeadingLevel, BorderStyle,
        Table, TableRow, TableCell, WidthType, ShadingType,
        Footer, PageNumber, TabStopType, TabStopPosition } = require('docx');
const fs = require('fs');
const FONT = 'Cambria';
const FULL = 9360;

const P = (parts, opts = {}) => new Paragraph({
  children: (Array.isArray(parts) ? parts : [parts]).map(p => typeof p === 'string'
    ? new TextRun({ text: p, font: FONT, size: 22 })
    : new TextRun({ text: p.t, bold: !!p.b, font: FONT, size: 22 })),
  spacing: { after: 150, line: 276 }, ...opts,
});
const H2 = t => new Paragraph({
  heading: HeadingLevel.HEADING_2, outlineLevel: 1, spacing: { before: 300, after: 130 }, keepNext: true,
  children: [new TextRun({ text: t, bold: true, font: FONT, size: 25, color: '000000' })],
});

const cell = (parts, w, opts = {}) => new TableCell({
  width: { size: w, type: WidthType.DXA },
  margins: { top: 90, bottom: 90, left: 110, right: 110 },
  children: [P(parts, { spacing: { after: 0 } })],
  ...opts,
});
const hcell = (t, w) => cell([{ t, b: true }], w, { shading: { type: ShadingType.CLEAR, fill: 'E8E8E8' } });

function table(cols, rows) {
  const widths = cols.map(c => c.w);
  return new Table({
    columnWidths: widths,
    width: { size: FULL, type: WidthType.DXA },
    rows: [
      new TableRow({ tableHeader: true, children: cols.map(c => hcell(c.h, c.w)) }),
      ...rows.map(r => new TableRow({ children: r.map((v, i) => cell([v], widths[i])) })),
    ],
  });
}

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

c.push(new Paragraph({ spacing: { after: 60 }, children: [new TextRun({ text: 'Custer County Fair', bold: true, font: FONT, size: 40 })] }));
c.push(new Paragraph({
  spacing: { after: 300 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 8, space: 8, color: '000000' } },
  children: [new TextRun({ text: 'Veterinary Services Agreement', font: FONT, size: 28 })],
}));

c.push(H2('1. Parties and term'));
c.push(P(['This Agreement is entered into by the Custer County Fair Board, referred to as the Fair, and the licensed veterinarian named below, referred to as the Veterinarian.']));
c.push(table(
  [{ h: 'Field', w: 3200 }, { h: 'Entry', w: 6160 }],
  [
    ['Veterinarian, printed name', ''],
    ['Practice name', ''],
    ['Colorado license number', ''],
    ['Fair year covered by this Agreement', ''],
  ]
));
c.push(P(['This Agreement takes effect when it is signed by both parties and remains in effect through the close of the fair year named above.'], { spacing: { before: 150 } }));

c.push(H2('2. Purpose and precedence'));
c.push(P(['The Custer County Fair Book assigns a licensed veterinarian a defined set of duties and a defined authority to act on them. This Agreement states those duties in one place so that the Veterinarian can scope the work, price it, and accept it before the fair year begins.']));
c.push(P(['This Agreement creates no duty beyond what the Fair Book states. Where this Agreement and the Fair Book disagree, the Fair Book governs, and the Fair shall provide the Veterinarian written notice of any amendment to the Fair Book that changes a duty listed in Section 4.']));

c.push(H2('3. Authority'));
c.push(P(['The Fair Book names the licensed veterinarian as the Authority in animal health, fitness, and slaughter readiness, under CC 1.12.1(d). Within that role the Veterinarian may refuse entry to, excuse, or disqualify any animal.']));
c.push(P(['A determination made by the Veterinarian within that role is the determination of the Fair. It shall not be overridden by an exhibitor, a superintendent, or a member of the Fair Board.']));

c.push(H2('4. Duties'));
c.push(P(['The Veterinarian shall perform the duties listed below. Each duty is stated with the Fair Book rule that creates it. No duty outside this list is required of the Veterinarian under this Agreement.']));

c.push(P([{ t: 'On arrival at the fairgrounds, before unloading', b: true }], { spacing: { before: 120, after: 100 } }));
c.push(table(
  [{ h: 'Duty', w: 6100 }, { h: 'Fair Book rule', w: 3260 }],
  [
    ['Examine every market livestock animal on arrival at the fairgrounds, before it is unloaded, including its body condition. Refuse entry to, excuse, or disqualify any animal that does not meet a health or qualification standard. An animal refused entry shall not be unloaded or exhibited.', 'CC 2.14'],
    ['Inspect every bird entered in a market poultry division on arrival, before unloading. Refuse entry to a bird showing signs of illness.', 'CC 3.6.2'],
    ['Perform a dental check to verify the age of a market beef animal where age is in question. Market beef carries a maximum age of 20 months at fair time.', 'CC 3.2.2'],
    ['Perform a dental check to verify that a market lamb has its milk teeth.', 'CC 3.4.8a'],
    ['Perform a dental check to verify that a market goat has its milk teeth.', 'CC 3.5.8'],
    ['Examine a market lamb for a testicle contained in the body cavity. An animal in that condition is not eligible to show.', 'CC 3.4.9'],
  ]
));

c.push(P([{ t: 'During the fair', b: true }], { spacing: { before: 220, after: 100 } }));
c.push(table(
  [{ h: 'Duty', w: 6100 }, { h: 'Fair Book rule', w: 3260 }],
  [
    ['Examine a non-market or small animal on the grounds on request, and refuse or excuse an animal showing evidence of poor health or presenting a risk to other animals or to any person.', 'CC 6.1.7'],
    ['Advise the Fair on request whether water should be given to an animal.', 'CC 2.17'],
    ['Collect specimens where the Fair exercises its right to test a market animal for an illegal or banned substance.', 'CC 3.1.17'],
  ]
));

c.push(P([{ t: 'Before and after the sale', b: true }], { spacing: { before: 220, after: 100 } }));
c.push(table(
  [{ h: 'Duty', w: 6100 }, { h: 'Fair Book rule', w: 3260 }],
  [
    ['Examine each market livestock animal before the sale to determine slaughter readiness.', 'CC 2.14'],
    ['Certify when a consigned animal cannot be sold because of illness, injury, death, or an unlapsed drug withdrawal period.', 'CC 4.4.6'],
  ]
));

c.push(H2('5. Contingency'));
c.push(P(['Health requirements may change before the fair in the event of a disease outbreak in Colorado or a neighboring state. Where that occurs, the Fair shall follow the direction of the Colorado State Veterinarian\'s Office under CC 3.1.18, and the Veterinarian shall advise the Fair on carrying out that direction on the grounds.']));
c.push(P(['Reporting obligations owed to the State under the Veterinarian\'s license are not duties under this Agreement.']));

c.push(H2('6. Fee basis'));
c.push(P(['The Fair shall pay the Veterinarian on the basis and at the rates entered below. A line left blank is not a service required under this Agreement.']));
c.push(table(
  [{ h: 'Item', w: 4700 }, { h: 'Basis', w: 2330 }, { h: 'Rate', w: 2330 }],
  [
    ['Arrival examination, market livestock', '', ''],
    ['Arrival inspection, market poultry', '', ''],
    ['Age and eligibility verification', '', ''],
    ['Pre-sale readiness examination', '', ''],
    ['On-call during fair week', '', ''],
    ['Specimen collection and testing', '', ''],
    ['Certification under CC 4.4.6', '', ''],
    ['Mileage or travel', '', ''],
  ]
));
c.push(P(['Where a cost is recovered rather than borne by the Fair, it shall be stated here. Testing costs may be deducted from sale proceeds. An arrival examination required because an exhibitor presented an animal without required documentation may be charged to that exhibitor.'], { spacing: { before: 150 } }));

c.push(H2('7. Terms to be completed by the Fair Board'));
c.push(P(['Insurance, liability, term of termination, and payment schedule are not stated in this Agreement. They shall be completed and reviewed before either party signs.']));

c.push(H2('8. Acceptance'));
c.push(P(['By signing below, the Veterinarian accepts the duties stated in Section 4 and the authority stated in Section 3, and agrees to perform those duties for the fair year named in Section 1. By signing below, the Fair agrees to the fee basis stated in Section 6.']));

c.push(new Table({
  columnWidths: [4680, 4680],
  width: { size: FULL, type: WidthType.DXA },
  rows: [
    new TableRow({ children: [hcell('Veterinarian', 4680), hcell('Custer County Fair Board', 4680)] }),
    new TableRow({ children: [cell([{ t: 'Printed name and title', b: true }], 4680), cell([{ t: 'Printed name and title', b: true }], 4680)] }),
    new TableRow({ height: { value: 700, rule: 'atLeast' }, children: [cell([''], 4680), cell([''], 4680)] }),
    new TableRow({ children: [cell([{ t: 'Signature', b: true }], 4680), cell([{ t: 'Signature', b: true }], 4680)] }),
    new TableRow({ height: { value: 700, rule: 'atLeast' }, children: [cell([''], 4680), cell([''], 4680)] }),
    new TableRow({ children: [cell([{ t: 'Date', b: true }], 4680), cell([{ t: 'Date', b: true }], 4680)] }),
    new TableRow({ height: { value: 560, rule: 'atLeast' }, children: [cell([''], 4680), cell([''], 4680)] }),
  ],
}));

const doc = new Document({
  styles: { default: { document: { run: { font: FONT, size: 22 } } } },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1440, right: 1440, bottom: 1180, left: 1440 } } },
    footers: { default: footer('Custer County Fair: Veterinary Services Agreement') },
    children: c,
  }],
});

Packer.toBuffer(doc).then(b => {
  fs.writeFileSync('/mnt/user-data/outputs/Custer County Fair - Veterinary Services Agreement.docx', b);
  console.log('written', b.length);
});
