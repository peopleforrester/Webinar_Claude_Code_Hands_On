# PROJECT STATE — Claude Code Workshop Companion Repo

## Current Status: v6.0 — Q3 2026 Quarterly Freshness Review

**Workshop delivered:** 2026-04-09 (Thursday, 12:00–1:00 PM ET) and again in May.
**Repo state:** Public-ready. Maintenance mode.
**Branch:** `staging` (do not merge to `main` without explicit go-ahead).
**Remote:** `git@github.com:peopleforrester/Webinar_Claude_Code_Hands_On.git`

v6.0 is the 2026-07-01 quarterly freshness review. Sonnet 5 launched on Amazon Bedrock on 2026-07-01, superseding Sonnet 4.6. Updated all forward-facing and instructor-facing references. CLI floor (2.1.x, latest 2.1.197), Opus 4.8 GA status, slash commands, and brief dates all verified current — no other changes needed.

## What This Sweep Changed (v6.0)

| Item | Finding | Files |
|---|---|---|
| Sonnet model bump | Sonnet 5 GA on Bedrock (2026-07-01); repo named 4.6. Bumped all forward-facing and instructor-facing docs. | `README.md`, `command-reference.md`, `reference/effort-guide.md`, `instructor/instructor-guide.md`, `instructor/live-card.md` |
| `Alt+P` backtick | Keyboard shortcut in `effort-guide.md` prose was missing backtick formatting — fixed for consistency. | `reference/effort-guide.md` |
| CLI floor | Verified: "2.1.x or later" still accurate (latest 2.1.197). No change. | — |
| Opus floor | Verified: Opus 4.8 still current GA on Bedrock. No change. | — |
| Slash commands | Verified: all documented commands valid in v2.1.197. No change. | — |
| Brief dates | Verified: only date strings are `2026-12-15` (~167 days out). No change. | — |

## What This Sweep Changed (v5.9)

| Item | Finding | Files |
|---|---|---|
| Model bump | Opus 4.8 GA on Bedrock (2026-05-28, 1M context, 128K output); repo named 4.7. Bumped forward-facing docs. Sonnet 4.6 still current — unchanged. | `README.md`, `instructor/instructor-guide.md`, `instructor/live-card.md`, `reference/effort-guide.md` |
| Node floor | Node 18 reached end-of-life 2025-04; prerequisite said "18+". Bumped to "20 LTS+". | `paths/b-backend/README.md` |
| CLI floor | Verified: "2.1.x or later" still accurate (latest ~2.1.18x, locally 2.1.181). No change. | — |
| Python floor | Verified: "3.10+" still reasonable (3.9 EOL 2025-10). No change. | — |
| Banner drift | Instructor-guide version banner was stuck at v5.7 (header + footer), one behind PROJECT_STATE; bumped to v5.9 to match. | `instructor/instructor-guide.md` |

**Open design note:** the named model version has now been bumped four times (4.6 → 4.7 → 4.8). Each bump goes stale within weeks. Consider replacing the hard-pinned version in forward-facing docs with "the latest Opus model available in your Bedrock environment" to end the churn. Not done in v5.9 — flagged for decision.

## Verification Method

- **Direct file edit + grep verification.** No live workshop dry-run was run for these changes — the workshop has already occurred.
- **JSON files** were validated with `python3 -c "import json; json.load(open(...))"` after rebrand.
- **Internal link integrity** verified by spot-check; cross-links between `command-reference.md` and `reference/command-card.md` added in this sweep.
- **What is NOT verified:** None of the changes were exercised in a fresh Claude Code session against the participant flow. If a future workshop re-runs from this repo, redo the dry-run before delivery.

## What This Sweep Changed (v5.8)

| # | Issue (from second senior review) | Files |
|---|---|---|
| C1 | Path A sample data still had Disney IP (Space Mountain, Cast member, Adventureland, Haunted Mansion, Dole Whip, Lightning Lane, Pirates, Cosmic Rays, TRON) — completed the rebrand started in v5.7 | `paths/a-frontend/sample-data/guest-feedback.json` |
| C2 | `docs/` was claimed removed in v5.7 but was sitting untracked on disk with internal contact names and stale pre-workshop planning — added to `.gitignore` so the directory survives locally as instructor-only history but never publishes | `.gitignore` |
| H1 | Opus 4.6 → 4.7 propagation completed (v5.7's commit only touched README) | `instructor/instructor-guide.md`, `instructor/live-card.md`, `reference/effort-guide.md`, `PROJECT_STATE.md` |
| H2 | Instructor guide version banner bumped from v5.6 → v5.7 (header + footer) to match PROJECT_STATE | `instructor/instructor-guide.md` |
| H3 | Path E guided brief had `<repo>` placeholder in two `cp` commands attendees would paste literally — replaced with relative paths from a project directory created one level under the repo root | `paths/e-business/guided-brief.md` |
| M2 | Path E CLAUDE.md was 2× the size of the other path CLAUDE.md files because it duplicated voice rules, output structure, and verification rule that already lived in the skill — trimmed to the build/test header plus a pointer to the skill | `paths/e-business/CLAUDE.md` |

## What This Sweep Changed (v5.7)

| # | Phase | Files |
|---|---|---|
| 1 | Cheat-sheet additions: `/release-notes` + Extensibility/Discovery commands | `command-reference.md`, `reference/command-card.md` |
| 2 | Timing reconciliation: 20 → 28 min across 4 path READMEs + dry-run header | `paths/{a,b,c,d}/README.md`, `instructor/dry-run.md` |
| 3 | Skill hot-reload myth fix; dry-run pre-flight commands | `command-reference.md`, `instructor/dry-run.md` |
| 4 | Instructor-guide v5.4 → v5.6 + `/teleport` row removed | `instructor/instructor-guide.md` |
| 5 | Config hygiene: dead `docs/` removed (incomplete — see C2 above), language-specific local example replaced, Path E layout caveat | `.gitignore`, `CLAUDE.local.md.example`, `CLAUDE.md` |
| 6 | Cross-link command refs, dedupe four-pillars auto-memory, frame explain-code as minimal | `command-reference.md`, `reference/command-card.md`, `reference/four-pillars.md`, `skills-examples/explain-code/SKILL.md` |
| 7 | Removed empty `slides/` placeholder | `slides/`, `README.md` |
| 8 | Park rebrand: Coral Kingdom / Skyward Summit / Harbor Gardens / Meadow Haven, invalid case Shadow Isle (Path B + Path D only — Path A was missed, fixed in v5.8) | Path B + Path D CLAUDE.md, sample data, brief; data-report skill |

## Prior Version Changelog (one-liner each)

- **v5.0** — Initial workshop scaffold: 4 paths, briefs, sample data, skills, reference handouts.
- **v5.1** — Auto-memory qualified as "when enabled"; Path B sample data added.
- **v5.2** — Release-notes reconciliation: `/effort max` removed; Shift+Tab cycles modes.
- **v5.3** — Fact-check pass: Alt+T for thinking toggle; Ctrl+X Ctrl+K to kill agents; ultrathink as per-turn override.
- **v5.4** — Spec reconciliation: 28-min guided builds; pillar callouts in all briefs; instructor + dry-run docs created.
- **v5.5** — Generic warmup; pytest → unittest; instructor live-card added.
- **v5.6** — Path E pivot from Python report generator to zero-code Meeting Prep Kit.
- **v5.7** — Post-workshop ship-ready sweep + Disney-to-fictional park rebrand (Path B + D).
- **v5.8** — Closed v5.7 gaps: Path A rebrand, `docs/` properly gitignored, Opus 4.7 propagated to all references, Path E guided-brief paths fixed, Path E CLAUDE.md trimmed.
- **v5.9** — June 2026 version refresh: Opus 4.7 → 4.8 (Bedrock GA 2026-05-28); Node 18+ → 20 LTS+; CLI/Python floors verified current.
- **v6.0** — Q3 2026 freshness review: Sonnet 4.6 → Sonnet 5 (Bedrock GA 2026-07-01) across all forward-facing and instructor docs; `Alt+P` backtick fix; all other floors verified current.

## Confirmed Workshop Environment (historical)

```bash
CLAUDE_CODE_DISABLE_AUTO_MEMORY=true
CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=true
CLAUDE_CODE_DISABLE_1M_CONTEXT=true
```

- Opus 4.7 + Sonnet 4.6 via Bedrock (200K context).
- No internet/egress.
- No rate limit concerns for ~30 simultaneous users.

## Long-standing Decisions

- `.gitignore` allows `.claude/settings.json` through (negation pattern).
- Per-path READMEs are landing pages pointing to `guided-brief.md`.
- Skills live in `skills-examples/` (not `.claude/skills/`) — attendees copy what they need.
- No finished project code in the repo — briefs, data, and conventions only.
- `reference/` for quick handouts; `instructor/` for instructor-only material.
- `warmup-exercises.md` at repo root — attendees reference during the 5:00–15:00 block.
- Auto-memory mentioned as "exists outside enterprise config," not demoed live.
- Agent Teams ON in the env — mentioned briefly, no exercise built around it.
- All content genericized; sample data uses fictional park names across all paths (post-v5.8 — Path A finished in v5.8).
- `docs/` is gitignored, not deleted: it holds instructor-only planning history (real names, internal pre-workshop notes) that should never publish but is useful to keep locally.

## Next Action

None. Repo is in maintenance mode. If a follow-up workshop is scheduled, run a fresh personal dry-run of warmup + chosen path before delivery.
