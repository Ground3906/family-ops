# Repo Write Discipline — GitHub MCP

**Owner:** Al (orchestrator doctrine, applies to every writing agent on every account)
**Why this file exists:** every agent that writes to the repo — Foreman writing calendar entries, Punch List writing fleet state, Chow Hall writing a meal plan lock — goes through the same GitHub MCP surface and can make the same mistakes. This is written once and cited everywhere, so the pattern never drifts out of sync across agent files.

---

## The write pattern (mandatory, every write, every agent, every account)

1. **Fetch current content first.** `get_file_contents` with `ref=refs/heads/main`. Never write from memory of what a file "probably" contains.
2. **Reconstruct full content.** Partial writes are not supported. Take the fetched content, apply the change in full, produce the complete new file content.
3. **Fetch the SHA before any `create_or_update_file`.** Required for updating an existing file. A stale SHA means someone else committed between your fetch and your write — re-fetch, don't force it.
4. **Batch multi-file changes into one `push_files` call.** One commit, one message, every touched file in the same array. Never stagger a related set of changes across separate calls.
5. **Read back after every write.** Fetch the file again post-commit and confirm the actual content landed, not just that the API returned success. The API returning a SHA does not mean the content is correct — the tool parameter itself can be wrong and the API will still commit successfully.
6. **Never pass a shell reference as file content.** A tool call parameter is not a shell context. `$(cat file.md)`, backticks, environment variable syntax, none of it executes there. It gets written to the repo as literal text. This happened on this project, 2026-07-06: a `content` parameter was set to a literal bash command instead of the actual file text, and it silently committed roughly ninety seconds of garbage before a read-back caught it. Always inline the real content directly, every time.

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

- **`push_files` accepts placeholder content without error.** Verify every content field is real before firing.
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
