# PROJECT STATE — Disney DXT Workshop Companion Repo

## Current Status: v5 Content Update Complete — Branches Synced

**Last updated:** 2026-03-03
**Branch:** staging (main synced at 26b1919)
**Next step:** Dry-run exercises in Bedrock-like environment before April 1
**Remote:** git@github.com:peopleforrester/Disney_Claude_Code_Course.git (both branches pushed)

## Task Checklist

### Phase 1: Shared Foundation
- [x] README.md — repo overview, quickstart, path selection guide
- [x] CLAUDE.md — generic workshop CLAUDE.md
- [x] .claude/settings.json — starter security deny list
- [x] command-reference.md — printable cheat sheet
- [x] .gitignore updated — allows .claude/settings.json through

### Phase 2: Path Materials
- [x] paths/a-frontend/README.md — path overview landing page
- [x] paths/a-frontend/guided-brief.md — step-by-step guided build (20 min)
- [x] paths/a-frontend/CLAUDE.md — path-specific conventions
- [x] paths/a-frontend/independent-brief.md — Park Wait Times challenge
- [x] paths/b-backend/README.md — path overview landing page
- [x] paths/b-backend/guided-brief.md — step-by-step guided build (20 min)
- [x] paths/b-backend/CLAUDE.md — path-specific conventions
- [x] paths/b-backend/independent-brief.md — Dining Preferences challenge
- [x] paths/c-infrastructure/README.md — path overview landing page
- [x] paths/c-infrastructure/guided-brief.md — step-by-step guided build (20 min)
- [x] paths/c-infrastructure/CLAUDE.md — path-specific conventions
- [x] paths/c-infrastructure/independent-brief.md — Health Dashboard challenge
- [x] paths/d-data/README.md — path overview landing page
- [x] paths/d-data/guided-brief.md — step-by-step guided build (20 min)
- [x] paths/d-data/CLAUDE.md — path-specific conventions
- [x] paths/d-data/independent-brief.md — Guest Flow Simulator challenge

### Phase 3: Sample Data
- [x] paths/a-frontend/sample-data/guest-feedback.json — 15 entries, validated
- [x] paths/d-data/sample-data/operations-logs.json — 10 entries, validated

### Phase 4: Skills Examples
- [x] skills-examples/explain-code/SKILL.md — general purpose demo
- [x] skills-examples/ui-component/SKILL.md — Path A skill
- [x] skills-examples/api-scaffold/SKILL.md — Path B skill
- [x] skills-examples/docker-review/SKILL.md — Path C skill
- [x] skills-examples/data-report/SKILL.md — Path D skill

### Phase 5: Validation
- [x] JSON files parse with python -m json.tool
- [x] Markdown reviewed for broken tables, orphan references
- [x] Relative links in path READMEs corrected (../../ prefix)
- [x] No instructor-only content in attendee-facing files
- [x] docs/ directory confirmed gitignored
- [x] Initial commit to staging (899bb11)

### v5 Content Update
- [x] guided-brief.md created for all 4 paths (extracted from original READMEs)
- [x] Path READMEs trimmed to landing pages with file directory tables
- [x] reference/command-card.md — compact command & shortcut card
- [x] reference/three-pillars.md — pillar summary with auto-memory
- [x] reference/effort-guide.md — /effort level selection guide
- [x] slides/README.md — placeholder for instructor deck
- [x] command-reference.md updated — /memory, /copy, /simplify, /batch, Ctrl+F, Sonnet confirmed
- [x] README.md updated — structure diagram, guided-brief references, auto-memory in Pillar 3
- [x] Commit v5 changes to staging (26b1919)
- [x] Push staging to remote
- [x] Sync main with staging

## Decisions Made
- .gitignore updated to allow .claude/settings.json (negation pattern)
- Per-path READMEs refactored: landing pages pointing to guided-brief.md
- Skills in skills-examples/ (not .claude/skills/) — attendees copy what they need
- No finished project code — briefs, data, and conventions only
- CLAUDE.md at two levels: root (workshop-wide) + per-path (language-specific)
- Hybrid approach for v5: both README.md AND guided-brief.md per path
- reference/ directory for quick reference handouts (3 files)
- slides/ directory with placeholder README

## Known Issues in Instructor Docs (gitignored, not distributed)
- docs/specfile.md line 76: Path A labeled "(React/HTML)" — should be "(HTML/JS)"
- docs/specfile.md line 338: mentions Express/Flask — contradicts stdlib-only constraint
- These are in the gitignored docs/ directory and do not affect attendees

## Verification Method
- Research-based content derived from v5 spec reconciliation
- File structure verified via git status
- JSON sample data validated with python -m json.tool
- All relative links manually verified in prior session
