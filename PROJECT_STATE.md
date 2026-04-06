# PROJECT STATE — Claude Code Workshop Companion Repo

## Current Status: v5.4 Full Spec Reconciliation Complete

**Last updated:** 2026-04-07
**Branch:** staging
**Workshop date:** Wednesday, April 8, 2026 (12:00-1:00 PM ET)
**Next step:** Dry-run exercises in Bedrock-like config, then grant attendees repo access
**Remote:** git@github.com:peopleforrester/Disney_Claude_Code_Course.git

## Confirmed Environment (from IT team, pre-workshop)

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
- [x] README.md, config hierarchy doc, settings.json, command-reference.md, .gitignore
- [x] All 4 path directories: README, guided-brief, project config, independent-brief
- [x] Sample data: guest-feedback.json (Path A), operations-logs.json (Path D)
- [x] Skills examples: explain-code, ui-component, api-scaffold, docker-review, data-report
- [x] Reference handouts: command-card, four-pillars, effort-guide
- [x] slides/README.md placeholder

### Phase 5: v5.1 Environment Alignment (Complete)
- [x] Auto-memory references qualified as "when enabled" across all files
- [x] Path B sample data added (sample-reservations.json)
- [x] All shortcuts clarified and corrected

### Phase 6: v5.2 Release Notes Reconciliation (Complete)
- [x] `/effort max` removed — levels are now low/medium/high/auto
- [x] Shift+Tab updated to "cycle modes" (Default → Accept Edits → Plan → Auto)
- [x] All guided briefs updated for mode cycling
- [x] effort-guide.md rewritten for 3 levels + auto
- [x] settings.json deny list expanded

### Phase 7: v5.3 Fact-Check Reconciliation (Complete)
- [x] Alt+T for thinking toggle (not Tab)
- [x] Ctrl+X then Ctrl+K for kill agents (not Ctrl+F)
- [x] Default effort documented as medium
- [x] Ultrathink re-introduced as per-turn override
- [x] 4-level config hierarchy with Managed policy
- [x] /btw and /compact focus hints documented

### Phase 8: v5.4 Full Spec Reconciliation (Complete)
- [x] Guided brief timing updated: 20 min → 28 min across all 4 paths
- [x] Step names aligned with spec: "Set Up + Externalize", "Build + Verify", "Iterate + Verify"
- [x] Pillar callouts added to all 4 guided briefs
- [x] Missing # context notes added (test-after-change for B/C/D, list-files for A)
- [x] /powerup added to command-card.md and command-reference.md
- [x] ultrathink added to command-card.md
- [x] warmup-exercises.md created (4 rapid exercises for 5:00-15:00 block)
- [x] instructor/instructor-guide.md created (genericized full workshop spec)
- [x] instructor/dry-run.md created (genericized pre-workshop testing script)
- [x] README.md updated with new files, corrected timings, warmup reference
- [x] All content genericized (no client-specific references)

### Remaining Before Workshop
- [ ] Dry-run exercises in Bedrock-like environment
- [ ] Grant attendees access to GitHub repo
- [ ] Add presentation deck to slides/ directory (separate project)

## Decisions Made
- .gitignore allows .claude/settings.json through (negation pattern)
- Per-path READMEs: landing pages pointing to guided-brief.md
- Skills in skills-examples/ (not .claude/skills/) — attendees copy what they need
- No finished project code — briefs, data, and conventions only
- reference/ directory for quick reference handouts
- instructor/ directory for instructor-only materials (guide + dry run)
- warmup-exercises.md at repo root — attendees reference during 5:00-15:00 block
- Auto-memory: mentioned as "exists outside enterprise config" — not demoed live
- Agent Teams: ON in their env — mention briefly, don't build instruction around it
- Observers: acknowledged in instructor docs — repo content is self-explanatory
- All content genericized for public use — no client-specific branding
