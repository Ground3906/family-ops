#!/usr/bin/env python3
# apply-payroll-v2.py
# Applies the 2026-09-08 Payroll screen changes to payroll-current.html.
#
# Run from the repo root on the ThinkPad:
#   python scripts/apply-payroll-v2.py
#
# What it changes:
#   1. The title bar and Home button move from the top of the screen to the
#      bottom, so Home lands on the same pixel as the Payroll button in the
#      calendar's nav bar. Both bars are 96px, both flush left.
#   2. The rate card becomes the payday board: emoji, chore, price, as tiles
#      on a 6-column grid. Wood chipping and coop deep-clean run double-wide.
#      Old layout was 12px text with prices right-justified into the next
#      column, which read as though the price belonged to the wrong chore.
#   3. Writes become append operations instead of whole-file overwrites, and
#      the July seed fallback is deleted so a failed fetch can no longer
#      arm the screen to overwrite the ledger with four-month-old data.
#
# Every edit asserts its target exists exactly once before touching anything.
# Nothing is written unless all edits land and the result matches the hash
# verified when this was built. Safe to abort; safe to re-run (it detects
# an already-patched file and exits without changes).

import hashlib
import os
import subprocess
import sys

TARGET_SHA256 = "1c387c10692c835c"
TARGET_BYTES = 47408
F = "payroll-current.html"

if not os.path.exists(F):
    print("ERROR: run from the repo root (payroll-current.html not found)")
    sys.exit(1)

src = open(F, encoding="utf-8").read()

if "APPEND_URL" in src and "rate-item-icon" in src:
    print("Already patched. No changes made.")
    sys.exit(0)

start_len = len(src)


def cut(old, new, label):
    global src
    n = src.count(old)
    if n != 1:
        print("ABORT: %s -- expected 1 match, found %d" % (label, n))
        print("The file is not in the state this patch was written against.")
        sys.exit(1)
    src = src.replace(old, new, 1)
    print("  ok  %s" % label)


print("Read %d chars from %s" % (start_len, F))
print("")
print("-- 1. Home button to the bottom --")

h0 = src.index('<div id="header">')
h1 = src.index('</div>\n<div id="tab-bar">') + len("</div>\n")
header = src[h0:h1]
if "btn-home" not in header or "hdr-title" not in header:
    print("ABORT: header block did not capture cleanly")
    sys.exit(1)
src = src[:h0] + src[h1:]
body_end = src.index("</body>")
src = src[:body_end] + header + src[body_end:]
if not (src.index('<div id="content">') < src.index('<div id="header">')):
    print("ABORT: header did not land below content")
    sys.exit(1)
print("  ok  header block relocated below content")

cut(
    "#header {\n  display: flex; height: var(--hdr);\n  background: var(--bg); border-bottom: 2px solid #502e0c; flex-shrink: 0;\n}",
    "#header {\n  display: flex; height: var(--hdr);\n  background: var(--bg); border-top: 2px solid #502e0c; flex-shrink: 0;\n}",
    "border moved to the top edge",
)

print("")
print("-- 2. Rate card becomes the payday board --")

cut(
    """.rate-grid { display: flex; flex-wrap: wrap; gap: 4px 0; }
.rate-item { display: flex; justify-content: space-between; width: 25%; padding-right: 20px; font-size: 12px; font-family: system-ui, sans-serif; }
.rate-item-name { color: var(--ink); opacity: .85; }
.rate-item-price { color: var(--ink-soft); font-weight: 700; }""",
    """.rate-grid { display: grid; grid-template-columns: repeat(6, 1fr); gap: 14px; }
.rate-item { display: flex; flex-direction: column; align-items: center; justify-content: center;
  min-height: 218px; padding: 10px 8px; border-radius: 12px;
  background: #6a3e10; border-top: 2px solid #c07030; border-left: 2px solid #a05a20;
  border-bottom: 2px solid #180800; border-right: 2px solid #2e1004;
  box-shadow: 0 4px 10px rgba(0,0,0,.55), inset 0 0 18px rgba(0,0,0,.28); }
.rate-item.hero { grid-column: span 2; background: #7d4a12; border-top-color: #e08a3c; }
.rate-item.wide { grid-column: span 2; }
.rate-item-icon { font-size: 58px; line-height: 1; margin-bottom: 10px; }
.rate-item.hero .rate-item-icon { font-size: 76px; }
.rate-item-name { font-family: Georgia, serif; font-size: 26px; font-weight: 700; color: #f6e2bd;
  text-align: center; line-height: 1.12; margin-bottom: 10px; }
.rate-item.hero .rate-item-name { font-size: 34px; }
.rate-item-price { font-family: Georgia, serif; font-size: 46px; font-weight: 700; color: #ffd98a;
  letter-spacing: .01em; text-shadow: 0 2px 3px rgba(0,0,0,.6); }
.rate-item.hero .rate-item-price { font-size: 64px; }""",
    "tile styling",
)

cut(
    """  document.getElementById('rate-grid').innerHTML = JOBS.filter(function(j) { return j.id !== 'custom'; }).map(function(j) {
    return '<div class="rate-item"><span class="rate-item-name">' + j.label + (j.only ? ' *' : '') + '</span>' +
           '<span class="rate-item-price">$' + j.rate + (j.unit === 'hour' ? '/hr' : '') + '</span></div>';
  }).join('');""",
    """  var HERO = ['chip','coop'];
  var list = JOBS.filter(function(j) { return j.id !== 'custom'; });
  list.sort(function(a,b) {
    var ah = HERO.indexOf(a.id) > -1, bh = HERO.indexOf(b.id) > -1;
    if (ah !== bh) return ah ? -1 : 1;
    return (b.rate || 0) - (a.rate || 0);
  });
  var cells = 0;
  list.forEach(function(j) { cells += (HERO.indexOf(j.id) > -1) ? 2 : 1; });
  var cols = 6, slack = (Math.ceil(cells / cols) * cols) - cells;
  document.getElementById('rate-grid').innerHTML = list.map(function(j, i) {
    var hero = HERO.indexOf(j.id) > -1;
    var wide = (!hero && slack > 0 && i === list.length - 1);
    var cls = 'rate-item' + (hero ? ' hero' : '') + (wide ? ' wide' : '');
    return '<div class="' + cls + '">' +
           '<div class="rate-item-icon">' + (j.icon || '') + '</div>' +
           '<div class="rate-item-name">' + j.label + (j.only ? ' *' : '') + '</div>' +
           '<div class="rate-item-price">$' + j.rate + (j.unit === 'hour' ? '/hr' : '') + '</div></div>';
  }).join('');""",
    "tile rendering with emoji and payday sizing",
)

print("")
print("-- 3. Append-only writes, seed fallback removed --")

cut(
    """async function persist() {
  if (!gData) return;
  saving = true; updateSaveStatus();
  try {
    var res = await fetch(WRITE_URL, {method:'POST', headers:{'Content-Type':'application/json','Accept':'*/*'}, body:JSON.stringify(gData)});
    if (!res.ok) throw new Error('HTTP ' + res.status);
    saveErr = null;
  } catch(e) { saveErr = 'Save failed - check ThinkPad'; }
  finally { saving = false; updateSaveStatus(); }
}""",
    """async function persist(op) {
  if (!gData || !op) return;
  saving = true; updateSaveStatus();
  try {
    var res = await fetch(APPEND_URL, {method:'POST', headers:{'Content-Type':'application/json','Accept':'*/*'}, body:JSON.stringify(op)});
    if (!res.ok) throw new Error('HTTP ' + res.status);
    saveErr = null;
  } catch(e) { saveErr = 'Save failed - check ThinkPad'; }
  finally { saving = false; updateSaveStatus(); }
}""",
    "persist sends an operation, not the whole ledger",
)

cut(
    "var WRITE_URL = 'http://192.168.1.60:8081/save';",
    "var WRITE_URL  = 'http://192.168.1.60:8081/save';\nvar APPEND_URL = 'http://192.168.1.60:8081/append';",
    "append endpoint",
)

cut(
    "renderJobGrid(); renderCondFields(); updateAmountDisplay(); updateActionBtn(); renderRecentTickets(); persist();",
    "renderJobGrid(); renderCondFields(); updateAmountDisplay(); updateActionBtn(); renderRecentTickets();\n  persist({addEntries:[entry]});",
    "job stamp sends its ticket",
)

cut(
    "renderDeductPanel(); updateAmountDisplay(); updateActionBtn(); renderRecentTickets(); persist();",
    "renderDeductPanel(); updateAmountDisplay(); updateActionBtn(); renderRecentTickets();\n  persist({addEntries:[entry]});",
    "deduction sends its ticket",
)

cut(
    "  renderRecentTickets(); persist();\n}",
    "  renderRecentTickets(); persist({removeEntryIds:[id]});\n}",
    "ticket delete sends the id",
)

cut(
    """  KIDS.forEach(function(k) {
    var r = RATES[k.id], bal = cats.totals[k.id];
    bal.give  = parseFloat((bal.give  + r.give).toFixed(2));
    bal.save  = parseFloat((bal.save  + r.save).toFixed(2));
    bal.spend = parseFloat((bal.spend + r.spend).toFixed(2));
    cats.log.unshift({id:uid(),kidId:k.id,type:'accrue',note:monthLabel(mk)+' allowance added',date:todayStr()});
  });""",
    """  var accrDelta = {}, accrLog = [];
  KIDS.forEach(function(k) {
    var r = RATES[k.id], bal = cats.totals[k.id];
    bal.give  = parseFloat((bal.give  + r.give).toFixed(2));
    bal.save  = parseFloat((bal.save  + r.save).toFixed(2));
    bal.spend = parseFloat((bal.spend + r.spend).toFixed(2));
    accrDelta[k.id] = {give:r.give, save:r.save, spend:r.spend};
    var lg = {id:uid(),kidId:k.id,type:'accrue',note:monthLabel(mk)+' allowance added',date:todayStr()};
    cats.log.unshift(lg); accrLog.push(lg);
  });""",
    "accrual records what it moved",
)

cut(
    "cats.lastAccrualMonth = mk; renderPayout(); persist();",
    "cats.lastAccrualMonth = mk; renderPayout();\n  persist({addLog:accrLog, totalsDelta:accrDelta, setAccrualMonth:mk});",
    "accrual sends its delta",
)

cut(
    """  cats.log.unshift({id:uid(),kidId:kidId,type:'payout',
    note:monthLabel(mk)+' commission - Give $'+give.toFixed(2)+', Save $'+save.toFixed(2)+', Spend $'+spend.toFixed(2),
    date:todayStr()});""",
    """  var payDelta = {}; payDelta[kidId] = {give:give, save:save, spend:spend};
  var payLog = {id:uid(),kidId:kidId,type:'payout',
    note:monthLabel(mk)+' commission - Give $'+give.toFixed(2)+', Save $'+save.toFixed(2)+', Spend $'+spend.toFixed(2),
    date:todayStr()};
  cats.log.unshift(payLog);""",
    "payout records what it moved",
)

cut(
    "cats.lastPayoutMonth[kidId] = mk; renderPayout(); persist();",
    "cats.lastPayoutMonth[kidId] = mk; renderPayout();\n  persist({addLog:[payLog], totalsDelta:payDelta, setPayoutMonth:{kid:kidId, month:mk}});",
    "payout sends its delta",
)

cut(
    """    if (res.ok) { gData = await res.json(); } else { gData = seedData(); }
  } catch(e) { gData = seedData(); }""",
    """    if (!res.ok) throw new Error('HTTP ' + res.status);
    gData = await res.json();
    loadErr = null;
  } catch(e) { gData = null; loadErr = 'Cannot reach the ledger. Nothing can be logged until this clears.'; }""",
    "failed load no longer falls back to the July seed",
)

cut(
    "var gData = null, saving = false, saveErr = null;",
    "var gData = null, saving = false, saveErr = null, loadErr = null;",
    "load error state declared",
)

# Brace-count to the real end of seedData. A naive scan for the first lone
# closing brace lands inside the function body and leaves a dangling tail.
anchor = "function seedData() {"
if src.count(anchor) != 1:
    print("ABORT: seedData block not found exactly once")
    sys.exit(1)
s0 = src.index(anchor)
depth = 0
s1 = None
for k in range(s0 + len(anchor) - 1, len(src)):
    if src[k] == "{":
        depth += 1
    elif src[k] == "}":
        depth -= 1
        if depth == 0:
            s1 = k
            break
if s1 is None:
    print("ABORT: seedData braces never closed")
    sys.exit(1)
tail = s1 + 1
while tail < len(src) and src[tail] == "\n":
    tail += 1
src = src[:s0] + src[tail:]
if "seedData" in src:
    print("ABORT: seedData still referenced after removal")
    sys.exit(1)
print("  ok  dead seed block deleted")

cut(
    """(async function init() {
  document.getElementById('log-date').value = todayStr();
  await loadData();
  renderBoard();
  renderRecentTickets();
  switchTab('board');
})();""",
    """(async function init() {
  document.getElementById('log-date').value = todayStr();
  await loadData();
  if (!gData) {
    document.getElementById('content').innerHTML =
      '<div id="load-error"><div class="load-error-title">Ledger unavailable</div>' +
      '<div class="load-error-body">' + loadErr + '</div>' +
      '<div class="load-error-hint">Nothing has been lost. Reload once the ThinkPad is reachable.</div></div>';
    updateSaveStatus();
    return;
  }
  renderBoard();
  renderRecentTickets();
  switchTab('board');
})();""",
    "boot refuses to render a ledger it could not load",
)

cut(
    ".rate-note {",
    """#load-error { display:flex; flex-direction:column; align-items:center; justify-content:center;
  height:100%; gap:14px; padding:0 80px; text-align:center; }
.load-error-title { font-family:Georgia,serif; font-size:52px; font-weight:700; color:#ffd98a; }
.load-error-body { font-family:Georgia,serif; font-size:28px; color:#f6e2bd; line-height:1.35; }
.load-error-hint { font-family:system-ui,sans-serif; font-size:18px; color:rgba(240,200,128,.6); }
.rate-note {""",
    "error screen styling",
)

print("")
got_bytes = len(src.encode("utf-8"))
got_sha = hashlib.sha256(src.encode("utf-8")).hexdigest()[:16]
print("result: %d bytes, sha256 %s" % (got_bytes, got_sha))

if got_sha != TARGET_SHA256 or got_bytes != TARGET_BYTES:
    print("")
    print("ABORT: result does not match the build that was verified.")
    print("  expected %d bytes / %s" % (TARGET_BYTES, TARGET_SHA256))
    print("  got      %d bytes / %s" % (got_bytes, got_sha))
    print("Nothing written. Paste this output to Al.")
    sys.exit(1)

print("matches the verified build. Writing.")
open(F, "w", encoding="utf-8", newline="").write(src)

print("")
print("Committing...")
subprocess.call(["git", "add", F])
subprocess.call(["git", "commit", "-m",
                 "payroll screen: Home to the bottom bar, rate card becomes the payday board, append-only writes, seed fallback removed"])
subprocess.call(["git", "pull", "--rebase"])
subprocess.call(["git", "push"])
print("")
print("Done. Restart the write listener so it picks up /append:")
print("  Restart-ScheduledTask -TaskName BayerFamilyOps-PayrollWrite")
print("Then force-reload the Cockpit, or wait for the 00:01 reload.")
