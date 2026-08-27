# Repo Write Discipline — GitHub MCP

**Owner:** Al (orchestrator doctrine, applies to every writing agent on every account)
**Why this file exists:** every agent that writes to the repo — Foreman writing calendar entries, Punch List writing fleet state, Chow Hall writing a meal plan lock — goes through the same GitHub MCP surface and can make the same mistakes. This is written once and cited everywhere, so the pattern never drifts out of sync across agent files.

---

## The write pattern (mandatory, every write, every agent, every account)

1. **Fetch current content first.** `get_file_contents` with `ref=refs/heads/main`. Never write from memory of what a file "probably" contains.
2. **Reconstruct full content.** Partial writes are not supported. Take the fetched content, apply the change in full, produce the complete new file content.
3. **Fetch the SHA before any `create_or_update_file`.** Required for updating an existing file. A stale SHA means someone else committed between your fetch and your write — re-fetch, don't force it.
4. **Batch multi-file changes into one `push_files` call.** One commit, one message, every touched file in the same array. Never stagger a related set of changes across separate calls.
5. **Read back after every write, and compare the byte size.** Fetch the file again post-commit and confirm the actual content landed, not just that the API returned success. The API returning a SHA does not mean the content is correct — the tool parameter itself can be wrong and the API will still commit successfully. **The check is numeric, not visual: the `size` in the API response must equal the known byte count of the source. A stated intention to write real content is not verification.**
6. **Never pass any reference, placeholder, or token as file content.** A tool call parameter is not a shell context and not a variable scope. `$(cat file.md)`, backticks, environment variable syntax, `__FILE__`, a path, a filename — none of it resolves. It gets written to the repo as literal text. **Every `content` field must contain the complete literal file text, inlined, every time.**

---

## Placeholder content is the highest-frequency MCP failure on this repo

**It has happened twice, and the second time the doctrine forbidding it was already written in this file.**

- **2026-07-06:** a `content` parameter was set to a literal bash command instead of file text. Caught by read-back after roughly ninety seconds of garbage in the repo.
- **2026-08-27:** a `push_files` call sent the literal string `__FILE__` in the `content` field of all twelve files in a greenhouse drawing-renumber batch. Every one committed successfully and became 8 bytes. The API reported success twelve times. Recovery took the larger part of a working session, one file at a time. Nothing was lost only because the batch was a rename — every original still existed under its old name, untouched. **A batch that had overwritten files in place would have destroyed them.**

**Why knowing the rule was not enough:** both incidents passed a preflight that consisted of *intending* to send real content. The intention is not the check. The check is the byte count on the way back out.

**Mechanical rule, no exceptions:**

- Before firing a multi-file `push_files`, print the byte size of every file being sent and confirm each is non-trivial.
- After the call returns, compare the returned `size` for every file against that number.
- A returned size in the single or double digits on a file that should be kilobytes means placeholder content landed. Stop and repair immediately — do not continue the session's work on top of a corrupted tree.
- **Never delete the superseded version of a file until the replacement has been read back and size-verified.** In the 2026-08-27 incident this ordering is the only reason recovery was possible.

---

## Check `.gitignore` before writing any script that stages a repo path

**Before writing or modifying any script that runs `git add` on a repo path, check `.gitignore` for that path first.**

Why: `git add` on an ignored path is a silent no-op. It does not error. The subsequent `git diff --cached` comes back empty, a well-written script interprets that as "nothing to commit," logs a benign message, and exits 0. The task reports success. Nothing is ever pushed. A loud failure gets fixed in a day; this gets trusted indefinitely.

This bit on 2026-08-19. A git push block was added to `inbox-watcher.ps1` staging `archive/receipts-log.jsonl` — a path explicitly ignored at `.gitignore` line 23, under a comment block stating that machine-local runtime state must never be committed because it fights the running scheduled tasks. The code was pushed to `main` and cannot work as written. The check that would have caught it costs one command:

```
git -C <repo> check-ignore -v <path>
```

Note the corollary: if a machine-written file genuinely must reach the repo, it needs a `!` negation in `.gitignore` (as `logs/night-watch.jsonl` and `ops/system-health.json` already have). Adding the negation is a deliberate decision about whether that data belongs in version control at all — not a formality to clear on the way to making a script work.

---

## The Filesystem connector is a local, per-session tool — not an account-wide one

**The Filesystem connector (rooted at `C:\Users\ThinkPad X1 Carbon`) only exists in a Claude session actually running on the ThinkPad itself.** It is not a cloud connector reachable from any device on the account — it is a local stdio server, alive only for the process that spawned it. A session opened on the phone or on Precision will never see it, no matter how many times the tool is retried, and no amount of reconnecting in Claude's connector settings fixes it from the wrong machine.

This cost three dead retries on 2026-08-21 before the actual cause surfaced: the tool had worked earlier in that same session (reading `inbox-watcher.ps1` cleanly), then appeared to vanish mid-conversation. It hadn't dropped — the person had switched from asking on the ThinkPad to asking from the phone, and the tool was never available there to begin with. The fix was opening the request on the ThinkPad, not troubleshooting the connector.

**The tell:** if the Filesystem connector worked earlier in a session and then stops responding with no error, check which device the current request is actually coming from before assuming the connector itself failed.

---

## ThinkPad SYSTEM git authentication

Scheduled tasks on the ThinkPad (`BayerFamilyOps-WeeklyPush`, `BayerFamilyOps-InboxWatcher`, `BayerFamilyOps-PayrollWrite`) run as SYSTEM. SYSTEM has no user profile, no desktop session, and no inherited credentials — every assumption that holds for an interactive git session fails there.

**Configuration as of 2026-08-19 (all machine-wide, verified working):**

- **Auth model:** SSH deploy key, keypair at `C:\Windows\System32\config\systemprofile\.ssh\id_ed25519`, public half registered on `Ground3906/family-ops` as a deploy key **with write access enabled**. Scoped to this one repo; cannot reach any other repo or the account itself. Deploy keys do not expire.
- **Remote:** SSH, `git@github.com:Ground3906/family-ops.git`. Not HTTPS.
- **SSH binary:** `core.sshCommand` points at Git's bundled OpenSSH (`C:/Program Files/Git/usr/bin/ssh.exe`, 10.3p1). **Windows' built-in OpenSSH 9.5 cannot complete a handshake with GitHub** — it advertises a KEX method it does not implement, and the connection dies with `choose_kex: unsupported KEX method`. It is first on PATH, so it wins unless explicitly overridden.
- **`known_hosts`:** GitHub's host key pre-seeded at `C:\Windows\System32\config\systemprofile\.ssh\known_hosts`. Without it, SSH stops to ask for host verification and waits forever, because SYSTEM has nobody to ask.
- **`safe.directory`:** repo path registered `--system`. Without it, git refuses every operation with `detected dubious ownership`.
- **Identity:** `user.name` and `user.email` set `--system`. Without them, `git commit` fails with `Author identity unknown`.

**The failure signature to recognize:** a task that hangs rather than fails. Anything prompting for input — credential manager, host verification — blocks forever under SYSTEM instead of erroring, because there is no session to render the prompt. `Get-ScheduledTaskInfo` shows `LastTaskResult: 267009` (`SCHED_S_TASK_RUNNING`), and `Get-Process -Name git` shows live processes whose `StartTime` matches the task's `LastRunTime`. Kill those by PID, then check for a stranded `.git\index.lock`, which blocks every other git operation against the repo including the 3-minute pull job.

**Testing SYSTEM's git path without risking a hang:** register a temporary task running `git ls-remote origin` as SYSTEM, redirect output to a file, run it, read the file, delete the task. `ls-remote` only reads, so there is nothing to hang on. Never verify SYSTEM auth by running the command as yourself — an interactive session has credentials SYSTEM does not.

**Incident, 2026-08-21 — two compounding failures, found live during an arrivals-hook end-to-end test:**

1. **`origin` had reverted to HTTPS.** Read operations (`pull`, `ls-remote`) still succeeded off a cached Windows Credential Manager entry, which masked the problem completely — only `push` under SYSTEM hung, because push triggers a fresh permission check with no session to satisfy it. A hang, not an error, and the heartbeat log stayed silent because the script's `Log()` calls only fire after a git command returns. Diagnosed by isolating each operation individually as a temporary SYSTEM task — `ls-remote` clean, `pull` clean, `push` hung every time — which narrowed it to exactly the operation this doc already names as the risk. Fixed with `git remote set-url origin git@github.com:Ground3906/family-ops.git`, confirmed against the same isolated-push test.

2. **`FamilyOps-PullJob` was not running as SYSTEM at all.** Its principal was `LogonType: Interactive, UserId: mbay` — Matt's own account, not SYSTEM, unlike every other repo-writing task on this machine. It had been working for months on a cached HTTPS credential belonging to that account. The moment fix #1 changed `origin` to SSH — a single `.git/config` setting shared by every process touching this clone — PullJob broke instantly, since Matt's account had no SSH key registered anywhere. One fix silently broke an unrelated task that had never been unified onto the documented SYSTEM auth model in the first place.

**The lesson, not just the fix:** `origin`'s URL and the SSH deploy key are shared, repo-level state. Changing either affects every task touching that clone, not just the one being debugged. Before changing the remote or the auth model for one task, check the principal of every other scheduled task that touches the same repo:

```
Get-ScheduledTask | Where-Object { (Get-ScheduledTask $_.TaskName).Actions.Arguments -match 'family-ops' } | ForEach-Object { $_.TaskName; (Get-ScheduledTask $_.TaskName).Principal.UserId }
```

A task silently running under the wrong identity can work for months before a shared-config change exposes it — a clean `LastTaskResult` history proves nothing about which identity actually produced it.

---

## PowerShell scripts are ASCII-only

**Any `.ps1` file written to this repo must contain pure ASCII. No em-dashes, no en-dashes, no smart quotes, no Unicode of any kind — in code OR in comments.**

Why: content is written through a UTF-8 MCP pipe, but the ThinkPad runs Windows PowerShell 5.1, which reads script files as Windows-1252 by default. A UTF-8 em-dash becomes multi-byte mojibake (`â€"`), and when that garbage lands inside a string literal or comment, the 5.1 parser derails with "string is missing the terminator" and "missing closing brace" errors far from the real cause. The script will not run at all.

This bit on 2026-07-12 building NightWatch: em-dashes in comments and one in a `Write-Host` string killed the whole file. It bit again on 2026-08-19, when four em-dashes in `weekly-push.ps1` — three in the header comment, one in a `Log` string — silently failed that task every Sunday for five weeks. **The signature of a parse failure is total silence:** the script's own logging never runs, not even from its `catch` block, because a parse error happens before the first line executes. A script whose scheduled task returns a failure code while its log file does not exist at all is a parse failure, not a runtime one.

The fix is stripping every non-ASCII byte:
```
(Get-Content $p -Raw) -replace '[^\x00-\x7F]', '-' | Set-Content $p -Encoding ASCII
```

Rules:
- Use `-` (hyphen) instead of any dash. Use straight `'` and `"` only.
- When writing a `.ps1` through MCP, do not use Unicode punctuation even where it would read nicely.
- If a `.ps1` throws a parser error near a comment or string, suspect mojibake first: `Select-String -Path $file -Pattern '[^\x00-\x7F]'` finds it, and the one-liner above strips it.
- `Set-Content -Encoding ASCII` is the safe write encoding for these files.

This applies to `.ps1` specifically. Markdown files are read by tools that handle UTF-8, so em-dashes are fine there — the ban is PowerShell-only. (Note: em-dashes remain banned in any content Matt authors under his name — emails, papers, documents — for a separate reason: they read as AI, not Matt. That rule lives in Profile.)

---

## Native commands do not throw — check `$LASTEXITCODE`

**A failing external command (git, or any executable) never raises a PowerShell exception. It sets `$LASTEXITCODE` and execution continues.** `$ErrorActionPreference = 'Stop'` does not change this — that setting governs cmdlets, not native executables. A try/catch wrapped around bare `git add` / `git commit` / `git push` calls catches nothing when git fails; the script sails straight into its success path.

This bit for a full month. `payroll-write.ps1` piped all three git commands to `$null` with no exit-code checks and logged `Saved and pushed` unconditionally after them. Diagnosed 2026-08-20: eight "Saved and pushed" entries in the log, zero commits ever landed — the file-scoped `git log` on `payroll/payroll-data.json` showed only the original seed commit. The catch block had never fired once, so no failure was ever recorded anywhere, and there was no diagnostic trail at all. Fixed in commit `efc36caa`; six weeks of unprotected entries were rescued by manual commit `2ae91e0` first.

Rules for any script that runs git:
- Check `$LASTEXITCODE` after **each** git command individually — add, commit, and push each get their own check. A single check at the end cannot tell you which step failed.
- Distinguish a harmless no-op (staged diff empty, nothing to commit) from a real failure. They are different log lines.
- On failure, capture and log git's actual output (`2>&1` into a variable), not just the fact of failure.
- Log success only after every step is confirmed. A success line the code cannot prove is a lie waiting to be trusted.

**The signature:** a log full of successes over a repo whose commit history shows nothing. Verify the repo side — file-scoped commit history — never the script's own log.

---

## Multi-line PowerShell patches must tolerate line endings

Any patch to `cal-widget-current.html` (or any other large file patched locally via PowerShell rather than MCP) spanning more than one line must not rely on a literal here-string match. The ThinkPad's working copy line endings don't reliably match whatever line breaks land in a here-string typed into the console, and a literal multi-line match will silently return zero even when the content is correct on every line.

Fix: build the match as a regex — split the target text on `\r?\n`, escape each line with `[regex]::Escape()`, rejoin with `\r?\n`. Match with `[regex]::Matches()`, not `.Replace()`. Detect the file's actual line ending once (`$content -match "\r\n"`) and normalize inserted text to match before splicing, so the file doesn't end up mixed.

Single-line patches are unaffected and can still use literal matching — this only applies once a target spans more than one line.

This bit on 2026-08-19 patching the span-stacking and night-mode fixes: two separate multi-line patches both silently matched zero on the first attempt against a file confirmed present with a clean read. Root cause was CRLF in the working copy against LF-only here-strings. The abort-on-mismatch check caught it cleanly, no file was written on the failed attempt. The tolerant-regex approach above should be the default for any future multi-line patch, not a reactive fix reached for after a first failure.

---

## Known failure modes

- **`push_files` accepts placeholder content without error.** Verify every content field is real before firing, and verify the returned byte size after. See the dedicated section above — this has happened twice.
- **`get_file_contents` returns a placeholder for large files (roughly 25KB and up).** Use `web_fetch` on the raw GitHub URL as a fallback for files above that size.
- **Files above roughly 50KB cannot be pushed inline via MCP.** Requires manual git from a local machine. This applies to the Cockpit widget HTML specifically — see `cal-widget.md`'s Hard Gates for the PowerShell-only push rule on that file.
- **Local machine commits race MCP commits.** If two machines pull on a cadence (e.g. a 3-minute pull job), a fresh SHA on fetch can mean a local commit landed between your read and your write. Re-read before writing if there's any chance of that race.
- **Large doctrine batches exceed single-push payload.** A multi-file doctrine batch can be too large for one `push_files` call. When that happens, chunk to proven size (roughly 2 medium files, or one large file, per call) and expect multiple commits. This does not violate the one-commit rule in spirit — the ceiling is a payload limit, not a choice. Group the chunks logically and read back every file after.
- **A scheduled task reporting success proves nothing about whether data moved.** `LastTaskResult: 0` means the script exited cleanly, which includes every early-exit path it was written to take. Verify the repo side independently — commit history on the target file — not the exit code.
- **`create_or_update_file` can fail with `No approval received` where `push_files` succeeds on identical content.** Observed 2026-08-20. `push_files` is the default write tool for this repo; reach for `create_or_update_file` only when a SHA-guarded single-file update is specifically required, and expect the approval gate.

---

## JSONL append discipline

Append-only logs (`fuel-log.jsonl`, `feed-log.jsonl`, `income-log.jsonl`, `maintenance-log.jsonl`, `night-watch.jsonl`, and any future one): fetch the full file, append the new line, push the complete file back. Never patch a data file to work around a code bug — log the bug, fix the code, and get Matt's explicit permission for any exception to that rule.

Note on machine-written logs: `night-watch.jsonl` and `ops/system-health.json` are written on the ThinkPad and pushed by WeeklyPush, not through MCP. They are `!`-negated in `.gitignore` so that push works. Do not remove those negations, and do not hand-edit these files through MCP — they are machine-owned. See `ops/watcher-layer.md`.

---

## Who cites this file

Every agent file with a state-mutating write path cites this file instead of restating its contents: `foreman.md`, `punch-list.md`, `chow-hall.md`, and any future agent that writes to the repo. This file is the single source; agent files reference it, they don't duplicate it.
