# PROJECT STATE — Disney DXT Workshop Companion Repo

## Current Status: Build Complete — Branches Synced

**Last updated:** 2026-02-25
**Branch:** staging (main synced at f462511)
**Next step:** Add remote origin and push both branches
**Remote:** Not yet configured — no remote origin set

## Task Checklist

### Phase 1: Shared Foundation
- [x] README.md — repo overview, quickstart, path selection guide
- [x] CLAUDE.md — generic workshop CLAUDE.md
- [x] .claude/settings.json — starter security deny list
- [x] command-reference.md — printable cheat sheet
- [x] .gitignore updated — allows .claude/settings.json through

### Phase 2: Path Materials
- [x] paths/a-frontend/README.md — guided build steps
- [x] paths/a-frontend/CLAUDE.md — path-specific conventions
- [x] paths/a-frontend/independent-brief.md — Park Wait Times challenge
- [x] paths/b-backend/README.md — guided build steps
- [x] paths/b-backend/CLAUDE.md — path-specific conventions
- [x] paths/b-backend/independent-brief.md — Dining Preferences challenge
- [x] paths/c-infrastructure/README.md — guided build steps
- [x] paths/c-infrastructure/CLAUDE.md — path-specific conventions
- [x] paths/c-infrastructure/independent-brief.md — Health Dashboard challenge
- [x] paths/d-data/README.md — guided build steps
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
- [x] PROJECT_STATE.md written
- [x] Initial commit to staging (899bb11)

## Decisions Made
- .gitignore updated to allow .claude/settings.json (negation pattern)
- Per-path READMEs with full guided build steps (not combined)
- Skills in skills-examples/ (not .claude/skills/) — attendees copy what they need
- No finished project code — briefs, data, and conventions only
- CLAUDE.md at two levels: root (workshop-wide) + per-path (language-specific)

## Known Issues in Instructor Docs (gitignored, not distributed)
- docs/specfile.md line 76: Path A labeled "(React/HTML)" — should be "(HTML/JS)"
- docs/specfile.md line 338: mentions Express/Flask — contradicts stdlib-only constraint
- These are in the gitignored docs/ directory and do not affect attendees
