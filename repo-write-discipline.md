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

## Known failure modes

- **`push_files` accepts placeholder content without error.** Verify every content field is real before firing.
- **`get_file_contents` returns a placeholder for large files (roughly 25KB and up).** Use `web_fetch` on the raw GitHub URL as a fallback for files above that size.
- **Files above roughly 50KB cannot be pushed inline via MCP.** Requires manual git from a local machine. This applies to the Cockpit widget HTML specifically — see `cal-widget.md`'s Hard Gates for the PowerShell-only push rule on that file.
- **Local machine commits race MCP commits.** If two machines pull on a cadence (e.g. a 3-minute pull job), a fresh SHA on fetch can mean a local commit landed between your read and your write. Re-read before writing if there's any chance of that race.
- **Large doctrine batches exceed single-push payload.** A multi-file doctrine batch can be too large for one `push_files` call. When that happens, chunk to proven size (roughly 2 medium files, or one large file, per call) and expect multiple commits. This does not violate the one-commit rule in spirit — the ceiling is a payload limit, not a choice. Group the chunks logically and read back every file after.

---

## JSONL append discipline

Append-only logs (`fuel-log.jsonl`, `feed-log.jsonl`, `income-log.jsonl`, `maintenance-log.jsonl`, and any future one): fetch the full file, append the new line, push the complete file back. Never patch a data file to work around a code bug — log the bug, fix the code, and get Matt's explicit permission for any exception to that rule.

---

## Who cites this file

Every agent file with a state-mutating write path cites this file instead of restating its contents: `foreman.md`, `punch-list.md`, `chow-hall.md`, and any future agent that writes to the repo. This file is the single source; agent files reference it, they don't duplicate it.
