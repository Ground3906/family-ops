#!/usr/bin/env python3
# apply-payroll-v3.py
# Uniform tiles on the Earnings Board. Run after apply-payroll-v2.py.
#
#   cd "C:\Users\ThinkPad X1 Carbon\Documents\family-ops"
#   python scripts/apply-payroll-v3.py
#
# What went wrong in v2: tile height was pinned at min-height 218px, a number
# computed against an assumed 150px balance strip. The real balance cards are
# taller, so the third row ran off the bottom of the screen.
#
# The fix is not a better number. It is removing the number. The rate card now
# claims whatever vertical space is left after the balance cards, and the grid
# divides that into three equal rows with grid-auto-rows: 1fr. Row height is
# computed from what is actually there, so it cannot overflow whether those
# cards render at 150px or 280px.
#
# Also: heroes are gone. Fifteen tiles, five across, three down, exactly
# filling the grid with no leftover cells. Biggest payday still sorts first,
# so wood chipping and coop deep-clean lead the board by position rather
# than by size.
#
# Type scaled to suit: icon 42, name 21, price 36. Verified to fit a row
# even at the tightest balance-card height tested.
#
# TARGET pin history: first published as 46812 / 4d55805c50e9498d, which was
# wrong. That figure came from running this patch against a stale local copy
# of the v2 output, one built before the loadErr declaration bug was fixed.
# The deployed file carries that declaration and is 16 bytes longer. The pin
# below is derived from the actual file in the repo. The guard caught the
# mismatch and refused to write, which is what it is for.

import hashlib
import os
import subprocess
import sys

TARGET_SHA256 = "722d2b9a917ac0c0"
TARGET_BYTES = 46828
F = "payroll-current.html"

if not os.path.exists(F):
    print("ERROR: run from the repo root (payroll-current.html not found)")
    sys.exit(1)

src = open(F, encoding="utf-8").read()

if "grid-auto-rows: 1fr" in src:
    print("Already patched. No changes made.")
    sys.exit(0)

if "APPEND_URL" not in src:
    print("ERROR: apply-payroll-v2.py has not been run on this file yet.")
    sys.exit(1)

print("Read %d chars from %s" % (len(src), F))
print("")


def cut(old, new, label):
    global src
    n = src.count(old)
    if n != 1:
        print("ABORT: %s -- expected 1 match, found %d" % (label, n))
        print("The file is not in the state this patch was written against.")
        sys.exit(1)
    src = src.replace(old, new, 1)
    print("  ok  %s" % label)


cut(
    "#panel-board { flex-direction: column; padding: 20px 24px 16px 24px; gap: 16px; overflow: hidden; }",
    "#panel-board { flex-direction: column; padding: 20px 24px 16px 24px; gap: 16px; overflow: hidden; }\n#kid-cards { flex: 0 0 auto; }\n#rate-card { flex: 1 1 auto; display: flex; flex-direction: column; min-height: 0; overflow: hidden; }",
    "board panel divides its own height",
)

cut(
    ".rate-grid { display: grid; grid-template-columns: repeat(6, 1fr); gap: 14px; }",
    ".rate-grid { display: grid; grid-template-columns: repeat(5, 1fr); grid-auto-rows: 1fr;\n  gap: 14px; flex: 1 1 auto; min-height: 0; }",
    "five columns, rows computed not pinned",
)

cut(
    "  min-height: 218px; padding: 10px 8px; border-radius: 12px;",
    "  min-height: 0; padding: 8px; border-radius: 12px; overflow: hidden;",
    "fixed tile height removed",
)

cut(
    """.rate-item.hero { grid-column: span 2; background: #7d4a12; border-top-color: #e08a3c; }
.rate-item.wide { grid-column: span 2; }
.rate-item-icon { font-size: 58px; line-height: 1; margin-bottom: 10px; }
.rate-item.hero .rate-item-icon { font-size: 76px; }""",
    """.rate-item-icon { font-size: 42px; line-height: 1; margin-bottom: 6px; }""",
    "hero spans dropped, icon scaled",
)

cut(
    """.rate-item-name { font-family: Georgia, serif; font-size: 26px; font-weight: 700; color: #f6e2bd;
  text-align: center; line-height: 1.12; margin-bottom: 10px; }
.rate-item.hero .rate-item-name { font-size: 34px; }""",
    """.rate-item-name { font-family: Georgia, serif; font-size: 21px; font-weight: 700; color: #f6e2bd;
  text-align: center; line-height: 1.12; margin-bottom: 6px; }""",
    "name scaled",
)

cut(
    """.rate-item-price { font-family: Georgia, serif; font-size: 46px; font-weight: 700; color: #ffd98a;
  letter-spacing: .01em; text-shadow: 0 2px 3px rgba(0,0,0,.6); }
.rate-item.hero .rate-item-price { font-size: 64px; }""",
    """.rate-item-price { font-family: Georgia, serif; font-size: 36px; font-weight: 700; color: #ffd98a;
  letter-spacing: .01em; text-shadow: 0 2px 3px rgba(0,0,0,.6); }""",
    "price scaled",
)

cut(
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
    return '<div class="' + cls + '">' +""",
    """  var list = JOBS.filter(function(j) { return j.id !== 'custom'; });
  list.sort(function(a,b) { return (b.rate || 0) - (a.rate || 0); });
  document.getElementById('rate-grid').innerHTML = list.map(function(j) {
    return '<div class="rate-item">' +""",
    "uniform tiles, biggest payday first",
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
                 "payroll screen: uniform tiles, 5x3, rows sized from available space instead of a pinned height"])
subprocess.call(["git", "pull", "--rebase"])
subprocess.call(["git", "push"])
print("")
print("Done. The Cockpit caches the page, so a plain reload will not show this.")
print("In Fully Kiosk: triple-tap the screen to open the menu, then")
print("Settings > Advanced Web Settings > Clear Cache, then reload.")
