const R = require('./render.js');
const fs = require('fs');
const { Document, Packer, Paragraph, TextRun, AlignmentType, BorderStyle, PageBreak,
        InternalHyperlink, TabStopType, Bookmark, Header } = R;
const VERSION = R.VERSION, PM = R.PAGEMAP;
const md = fs.readFileSync('addendum.v14.md', 'utf8');

// split into § sections
const secs = []; let cur = null; const preamble = [];
for (const l of md.split('\n')) {
  const m = /^## (§(\d+)) — (.+)$/.exec(l);
  if (m) { cur = { short: m[1], num: +m[2], title: m[3], anchor: 'a' + m[2], raw: [] }; secs.push(cur); continue; }
  if (cur) cur.raw.push(l);
  else if (!/^# Custer County|^---\s*$|^\s*$/.test(l)) preamble.push(l);
}

const toc = [];
for (const s of secs) {
  toc.push({ depth: 0, label: `${s.short} — ${s.title}`, anchor: s.anchor });
  for (const l of s.raw) {
    const m = /^### (§[\d.]+) — (.+)$/.exec(l);
    if (m) toc.push({ depth: 1, label: `${m[1]} — ${m[2]}`, anchor: 'as' + m[1].replace(/[^0-9]/g, '_') });
  }
}

function navbarA(current) {
  const kids = [];
  const push = (label, anchor, active) => active
    ? kids.push(new TextRun({ text: label, bold: true, font: R.FONT, size: 17, color: '000000' }))
    : kids.push(new InternalHyperlink({ anchor, children: [new TextRun({ text: label, font: R.FONT, size: 17, color: '444444' })] }));
  push('Contents', 'atoc', current === 'atoc');
  for (const s of secs) {
    kids.push(new TextRun({ text: '  ·  ', font: R.FONT, size: 17, color: '999999' }));
    push(s.short, s.anchor, s.short === current);
  }
  return new Header({ children: [new Paragraph({
    alignment: AlignmentType.CENTER, spacing: { after: 120 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 4, space: 6, color: 'BBBBBB' } },
    children: kids })] });
}

const front = [];
front.push(new Paragraph({ spacing: { before: 2600, after: 200 }, alignment: AlignmentType.CENTER,
  children: [new TextRun({ text: 'CUSTER COUNTY', bold: true, font: R.FONT, size: 52 })] }));
front.push(new Paragraph({ spacing: { after: 160 }, alignment: AlignmentType.CENTER,
  children: [new TextRun({ text: 'FAIR BOOK', bold: true, font: R.FONT, size: 52 })] }));
front.push(new Paragraph({ spacing: { after: 400 }, alignment: AlignmentType.CENTER,
  children: [new TextRun({ text: 'ADDENDUM', font: R.FONT, size: 40, color: '333333' })] }));
front.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 120 },
  border: { top: { style: BorderStyle.SINGLE, size: 6, space: 10, color: '000000' } },
  children: [new TextRun({ text: ' ', font: R.FONT, size: 20 })] }));
front.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60 },
  children: [new TextRun({ text: `Version ${VERSION}`, font: R.FONT, size: 28 })] }));
front.push(new Paragraph({ alignment: AlignmentType.CENTER,
  children: [new TextRun({ text: 'Westcliffe, Colorado', font: R.FONT, size: 22, color: '444444' })] }));
front.push(new Paragraph({ children: [new PageBreak()] }));
for (const b of R.parseBlocks(preamble.join('\n'))) {
  if (b.t === 'p') front.push(R.para(b.text));
}

const tocKids = [new Paragraph({
  heading: R.HeadingLevel.HEADING_1, outlineLevel: 0, spacing: { after: 200 },
  children: [new Bookmark({ id: 'atoc', children: [new TextRun({ text: 'Contents', bold: true, font: R.FONT, size: 30, color: '000000' })] })],
})];
for (const e of toc) {
  tocKids.push(new Paragraph({
    spacing: { after: 20, line: 240 }, indent: { left: e.depth * 160 },
    tabStops: [{ type: TabStopType.RIGHT, position: 4480, leader: 'dot' }],
    children: [
      new InternalHyperlink({ anchor: e.anchor, children: [new TextRun({ text: e.label, font: R.FONT, size: e.depth ? 18 : 19, bold: !e.depth, color: '000000' })] }),
      new TextRun({ text: '\t' + (PM[e.anchor] || ''), font: R.FONT, size: 18, color: '444444' }),
    ],
  }));
}

function sectionChildren(s) {
  const kids = [R.heading(`${s.short} — ${s.title}`, 0, s.anchor)];
  for (const b of R.parseBlocks(s.raw.join('\n'))) {
    if (b.t === 'hr') continue;
    if (b.t === 'table') { const t = R.buildTable(b.rows); if (t) kids.push(t); continue; }
    if (b.t === 'h3') {
      const m = /^(§[\d.]+) — (.+)$/.exec(b.text);
      kids.push(R.heading(b.text, 1, m ? 'as' + m[1].replace(/[^0-9]/g, '_') : 'ax' + R.slug(b.text)));
      continue;
    }
    if (b.t === 'h2') { kids.push(R.heading(b.text, 1, 'ax' + R.slug(b.text))); continue; }
    const bm = /^\*\*([^*]+)\*\*$/.exec(b.text);
    if (bm) { kids.push(R.heading(bm[1], 2, 'ab' + R.slug(bm[1]) + kids.length)); continue; }
    kids.push(R.para(b.text));
  }
  return kids;
}

const sections = [
  { properties: { page: { size: R.PAGE, margin: R.MARGIN } },
    headers: { default: R.plainHeader() }, footers: { default: R.footerCentered() }, children: front },
  { properties: { page: { size: R.PAGE, margin: R.MARGIN }, column: { count: 2, space: 400, equalWidth: true } },
    headers: { default: R.plainHeader() }, footers: { default: R.footerCentered() }, children: tocKids },
];
for (const s of secs) {
  sections.push({
    properties: { page: { size: R.PAGE, margin: R.MARGIN } },
    headers: { default: navbarA(s.short) },
    footers: { default: R.footerCentered() },
    children: sectionChildren(s),
  });
}

Packer.toBuffer(new Document({
  styles: { default: { document: { run: { font: R.FONT, size: R.BODY } } } }, sections,
})).then(b => {
  fs.writeFileSync('/mnt/user-data/outputs/Custer County Fair Book Addendum v' + VERSION + '.docx', b);
  console.log('addendum written', b.length, 'bytes |', secs.length, 'sections |', toc.length, 'toc entries');
});
