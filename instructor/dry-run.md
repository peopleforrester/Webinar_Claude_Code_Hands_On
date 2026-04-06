# Claude Code Workshop — Dry Run Script
## Run this to simulate the attendee experience before the workshop

**Purpose:** Walk through every exercise step by step to verify:
1. All commands work in a Bedrock-backed environment
2. Effort level differences are visible and meaningful
3. Plan Mode produces noticeably better output than unplanned
4. CLAUDE.md rules are picked up (especially the "run tests" rule)
5. Guided build can complete in allotted time
6. Context usage stays manageable

**How to use:** Open a terminal. Run each step in order. Check the **VERIFY** note after each. Log issues in the checkboxes provided.

**Estimated time:** 45–60 minutes for a full dry run.

---

## PHASE 0: Environment Verification (2 min)

```bash
claude --version
```
- [ ] Version shows **2.1.x**

```bash
claude /model
```
- [ ] Model list includes **Opus 4.6** and **Sonnet 4.6**

```bash
claude /status
```
- [ ] Shows connected backend (Bedrock or direct API)

### Issue Log — Phase 0
- [ ] _________________________________
- [ ] _________________________________

---

## PHASE 1: Effort Levels Exercise (5 min)

```bash
mkdir -p ~/workshop-dryrun/warmup && cd ~/workshop-dryrun/warmup
claude
```

**Step 1.1 — Low effort:**
```
/effort low
```
Paste this prompt:
> Write a theme park reservation validator in Python. It should check date format, party size (1-20), and park name against a known list.

- [ ] **VERIFY:** Minimal output — short function, few comments, no extras
- [ ] Note response time: ______ seconds
- [ ] Note response length: ______ lines

**Step 1.2 — High effort:**
```
/effort high
```
Paste the same prompt again.

- [ ] **VERIFY:** More thorough output — docstrings, edge case handling, better structure
- [ ] Note response time: ______ seconds
- [ ] Note response length: ______ lines
- [ ] **CRITICAL:** Is the difference visible enough to use in a live demo? (yes / no)

**Step 1.3 — Reset:**
```
/effort medium
```

### Issue Log — Phase 1
- [ ] _________________________________
- [ ] _________________________________

---

## PHASE 2: Plan Mode Exercise (5 min)

**Step 2.1 — WITHOUT Plan Mode:**

Ask Claude:
> Add input validation with clear error messages, a full test suite, and a CLI wrapper to the reservation validator.

Let it run to completion.

- [ ] **VERIFY:** Note output quality — did it produce everything? Was it well-structured?
- [ ] Quality notes: _________________________________

**Step 2.2 — WITH Plan Mode:**

Press **Shift+Tab** twice to enter Plan Mode. Ask:
> Analyze the current code and plan how you would add input validation, a test suite, and a CLI wrapper. Do not make changes yet — just plan.

- [ ] **VERIFY:** Claude read the file but did **NOT** modify it
- [ ] **VERIFY:** Plan includes file breakdown and implementation order

Exit Plan Mode (Shift+Tab), then tell Claude:
> Implement the plan you just created.

- [ ] **VERIFY:** **CRITICAL** — Is the planned output noticeably better than the unplanned version? (yes / no)
- [ ] Quality comparison notes: _________________________________

### Issue Log — Phase 2
- [ ] _________________________________
- [ ] _________________________________

---

## PHASE 3: Externalize Exercise (3 min)

**Step 3.1 — /init:**
```
/init
```
- [ ] **VERIFY:** `CLAUDE.md` file generated in current directory

**Step 3.2 — # shortcut to add a rule:**

Type `#` then add a rule like:
> Always run tests after making changes

- [ ] **VERIFY:** Rule added to `CLAUDE.md`

**Step 3.3 — Create a skill:**
```bash
mkdir -p .claude/skills
```
Create `.claude/skills/SKILL.md` with a simple skill definition (e.g., a code review checklist).

- [ ] **VERIFY:** Skill is picked up when referenced
- [ ] **VERIFY:** Hot-reload works — edit the skill file and confirm Claude sees the update without restart

### Issue Log — Phase 3
- [ ] _________________________________
- [ ] _________________________________

---

## PHASE 4: Verify Exercise (2 min)

Ask Claude:
> Refactor the reservation validator to use a Python dataclass instead of a plain dict. Update the tests to match.

- [ ] **VERIFY:** **CRITICAL** — Did Claude run `pytest` (or equivalent) after making the change?
- [ ] Tests pass? (yes / no)
- [ ] If tests failed, did Claude attempt to fix them? (yes / no)

### Issue Log — Phase 4
- [ ] _________________________________
- [ ] _________________________________

---

## PHASE 5: Guided Build — Pick ONE Path (20 min)

> **Recommended:** Path B (Backend API) — it has the most verification steps.

### Setup
```bash
mkdir -p ~/workshop-dryrun/reservation-api && cd ~/workshop-dryrun/reservation-api
claude
```

**Step 5.1 — Initialize and configure:**
```
/init
```
Use `#` to add context rules:
- Always run tests after changes
- Use stdlib only — no external dependencies
- All output goes to `./output/`

- [ ] **VERIFY:** Rules present in `CLAUDE.md`

**Step 5.2 — Plan Mode — paste the full API spec:**

Enter Plan Mode (Shift+Tab twice), then paste:
> Build a reservation API with these endpoints:
> - POST /reservations — create a reservation (name, date, party_size, park)
> - GET /reservations/{id} — retrieve a reservation
> - DELETE /reservations/{id} — cancel a reservation
>
> Business rules: party size 1-20, date must be in the future, park must be in the allowed list, no duplicate reservations for the same name+date+park.

- [ ] **VERIFY:** Plan is coherent — lists files, order, and approach
- [ ] Plan time: ______ seconds

**Step 5.3 — Implement:**

Exit Plan Mode, tell Claude to implement the plan.

- [ ] **VERIFY:** All expected files created (server, models, tests, etc.)
- [ ] **VERIFY:** Tests pass
- [ ] **VERIFY:** Tests ran automatically (not manually triggered)
- [ ] Implementation time: ______ seconds

**Step 5.4 — Iterate:**

Ask Claude:
> Add rate limiting (max 10 requests per minute per IP), a /health endpoint, and request logging to a file.

- [ ] **VERIFY:** Features added correctly
- [ ] **VERIFY:** Tests pass (including new test coverage)
- [ ] Iteration time: ______ seconds

**Step 5.5 — Check context:**
```
/context
```
- [ ] **VERIFY:** Context usage below **65%**

**Step 5.6 — Total timing:**
- [ ] Total guided build time: ______ minutes
- [ ] **CRITICAL:** Does the build fit within **28 minutes**? (yes / no)

### Issue Log — Phase 5
- [ ] _________________________________
- [ ] _________________________________
- [ ] _________________________________

---

## PHASE 6: Spot-Check Commands (3 min)

**`/btw`** — Ask a quick question using `/btw`:
```
/btw what is the default port for http.server in Python?
```
- [ ] **VERIFY:** Answers without entering full conversation context

**`/compact`** — Compact the conversation:
```
/compact
```
- [ ] **VERIFY:** Conversation compacted successfully

**`/context`** — Check usage after compact:
```
/context
```
- [ ] **VERIFY:** Context usage dropped after compact

**`/insights`** — View session analytics:
```
/insights
```
- [ ] **VERIFY:** Shows analytics summary

**`ultrathink`** — Test deep reasoning:

Ask Claude:
> ultrathink — What are the race conditions in this reservation system and how would you prevent them?

- [ ] **VERIFY:** Deeper reasoning visible — longer think time, more thorough analysis

### Issue Log — Phase 6
- [ ] _________________________________
- [ ] _________________________________

---

## PHASE 7: Dry Run Summary

### Overall Assessment

| Check | Pass | Fail |
|-------|------|------|
| Effort level differences visible | [ ] | [ ] |
| Plan Mode quality improvement clear | [ ] | [ ] |
| CLAUDE.md rules picked up | [ ] | [ ] |
| Tests run automatically | [ ] | [ ] |
| Skills hot-reload works | [ ] | [ ] |
| Guided build fits in 28 min | [ ] | [ ] |
| Context usage below 65% | [ ] | [ ] |
| Keyboard shortcuts work (Shift+Tab) | [ ] | [ ] |
| /btw works without context load | [ ] | [ ] |
| ultrathink shows deeper reasoning | [ ] | [ ] |

### Issues to Fix Before Workshop

1. _________________________________
2. _________________________________
3. _________________________________
4. _________________________________
5. _________________________________

### Timing Notes

| Section | Target | Actual | Verdict |
|---------|--------|--------|---------|
| Effort levels | 3 min | ______ | ______ |
| Plan Mode | 3 min | ______ | ______ |
| Externalize | 3 min | ______ | ______ |
| Verify | 1 min | ______ | ______ |
| Guided build | 28 min | ______ | ______ |
| **Total** | **~38 min** | ______ | ______ |

### Adjustments Needed

- _________________________________
- _________________________________
- _________________________________

---

*Dry run script for Claude Code Hands-On Workshop*
*Run on Bedrock if possible. Run on direct API if not.*
*Log every issue. Fix before workshop day.*
