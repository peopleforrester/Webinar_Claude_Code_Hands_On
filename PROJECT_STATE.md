# PROJECT STATE — Disney DXT Workshop Companion Repo

## Current Status: v5.3 Fact-Check Reconciliation Complete

**Last updated:** 2026-04-05
**Branch:** staging
**Workshop date:** Wednesday, April 8, 2026 (12:00-1:00 PM ET)
**Next step:** Dry-run exercises in Bedrock-like config, then grant attendees repo access
**Remote:** git@github.com:peopleforrester/Disney_Claude_Code_Course.git

## Confirmed Environment (from Greg, March 2026)

```bash
CLAUDE_CODE_DISABLE_AUTO_MEMORY=true      # Auto-memory is OFF
CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=true  # Agent Teams is ON
CLAUDE_CODE_DISABLE_1M_CONTEXT=true        # Context capped at 200K
```

- Opus 4.6 + Sonnet 4.6 via Bedrock (200K context)
- No internet/egress — all exercises self-contained
- No rate limit concerns for 30 simultaneous users
- Some observers expected without CLI access

## Task Checklist

### Phase 1-4: v5 Content (Complete)
- [x] README.md, CLAUDE.md, settings.json, command-reference.md, .gitignore
- [x] All 4 path directories: README, guided-brief, CLAUDE.md, independent-brief
- [x] Sample data: guest-feedback.json (Path A), operations-logs.json (Path D)
- [x] Skills examples: explain-code, ui-component, api-scaffold, docker-review, data-report
- [x] Reference handouts: command-card, three-pillars, effort-guide
- [x] slides/README.md placeholder

### Phase 5: v5.1 Environment Alignment
- [x] Auto-memory references qualified as "when enabled" across all files
- [x] README.md Pillar 3 row — removed auto-memory as assumed-working feature
- [x] command-reference.md — auto-memory section adds enterprise caveat
- [x] reference/three-pillars.md — auto-memory note rewritten for enterprise awareness
- [x] reference/command-card.md — /memory qualified, Ctrl+F clarified
- [x] Path B guided-brief — normalized Plan Mode instructions (removed `plan`/`code` keywords)
- [x] Path B sample data added (sample-reservations.json — 10 entries, valid + invalid)
- [x] Path B README updated with sample data file reference
- [x] Ctrl+F shortcut clarified as destructive action in command-reference.md and command-card.md
- [x] `#` shortcut description clarified in command-reference.md
- [x] Independent briefs (all 4 paths) — timing context added ("about 7 minutes")

### Phase 6: v5.2 Release Notes Reconciliation
- [x] `/effort max` removed — levels are now low/medium/high/auto (max was removed from CLI)
- [x] Shift+Tab updated from "toggle Plan Mode" to "cycle modes" (Default → Accept Edits → Plan → Auto)
- [x] Auto Mode noted as unavailable on Bedrock in command-reference.md
- [x] All guided briefs updated: "press Shift+Tab twice" → "use Shift+Tab to cycle to Plan Mode"
- [x] Exit Plan Mode instructions updated to "cycle back to Default"
- [x] Path D independent-brief: `/effort max` → `/effort high`
- [x] effort-guide.md rewritten for 3 levels + auto
- [x] Path B curl example dates updated (2026-03-15 → 2026-04-20)
- [x] `/copy` description standardized across command-reference.md and command-card.md
- [x] settings.json deny list expanded (pip, npm, git clone)
- [x] output/.gitkeep added to all 4 paths, .gitignore updated
- [x] Path C README: note about CLI args vs sample data
- [x] CLAUDE.local.md.example added as teaching reference

### Phase 7: v5.3 Fact-Check Reconciliation
- [x] Tab shortcut corrected: was "toggle thinking" → now Alt+T / Option+T (Tab is autocomplete)
- [x] Ctrl+F corrected: was "kill agents" → now Ctrl+X then Ctrl+K
- [x] Default effort documented as medium (not max) — added /effort high recommendation
- [x] Ultrathink re-introduced: removed "deprecated" claim, added as per-turn override
- [x] CLAUDE.md hierarchy expanded to 4 levels (added Managed policy for enterprise)
- [x] "Under 4000 words" → "under 200 lines" (official guidance) across all files
- [x] Context rot "20-40%" removed — real phenomenon but unverified threshold
- [x] /btw added to command-reference.md and command-card.md
- [x] /compact focus hints documented
- [x] Skills described as "loaded on-demand" not "auto-invoked"

### Remaining Before April 8
- [ ] Dry-run exercises in Bedrock-like environment
- [ ] Grant attendees access to GitHub repo (coordinate with Derek)
- [ ] Add presentation deck to slides/ directory (separate Remotion project)

## Decisions Made
- .gitignore allows .claude/settings.json through (negation pattern)
- Per-path READMEs: landing pages pointing to guided-brief.md
- Skills in skills-examples/ (not .claude/skills/) — attendees copy what they need
- No finished project code — briefs, data, and conventions only
- CLAUDE.md at two levels: root (workshop-wide) + per-path (language-specific)
- Hybrid approach: both README.md AND guided-brief.md per path
- reference/ directory for quick reference handouts
- Auto-memory: mentioned as "exists outside enterprise config" — not demoed live
- Agent Teams: ON in their env — mention briefly, don't build instruction around it
- Observers: acknowledged in instructor docs — repo content is self-explanatory

## Known Issues in Instructor Docs (gitignored, not distributed)
- docs/specfile.md line 76: Path A labeled "(React/HTML)" — should be "(HTML/JS)"
- docs/specfile.md line 338: mentions Express/Flask — contradicts stdlib-only constraint
- These are in the gitignored docs/ directory and do not affect attendees
