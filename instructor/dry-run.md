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

> **This phase mirrors `warmup-exercises.md` Exercise 1 verbatim.** Run the canonical script — do not improvise prompts.

```bash
mkdir -p ~/workshop-dryrun/warmup && cd ~/workshop-dryrun/warmup
claude
```

**Step 1.1 — Low effort:**
```
/effort low
```
Paste this prompt (the exact one from `warmup-exercises.md`):
> Write a Python function that validates a theme park reservation date. Rules: no past dates, no more than 60 days out, no blackout dates (Dec 24-25, Dec 31, Jul 4). Return a tuple of (bool, error_message).

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

## PHASE 2: Plan Mode Exercise (4 min)

> **CRITICAL — start in a fresh directory.** If you stay in the Phase 1 directory and Claude's high-effort run already produced tests + CLI, this exercise becomes a no-op and the contrast disappears. **Exit your Phase 1 session first** (`Ctrl+D` or `/exit`).

```bash
mkdir -p ~/workshop-dryrun/warmup-plan && cd ~/workshop-dryrun/warmup-plan
```

Seed the baseline with one paste (matches `warmup-exercises.md` Exercise 2):

```bash
cat > validate.py <<'PY'
from datetime import date, timedelta

BLACKOUT = {(12, 24), (12, 25), (12, 31), (7, 4)}

def validate_date(d):
    today = date.today()
    if d < today:
        return False, "past date"
    if (d - today).days > 60:
        return False, "more than 60 days out"
    if (d.month, d.day) in BLACKOUT:
        return False, "blackout date"
    return True, ""
PY

cat > test_validate.py <<'PY'
import unittest
from datetime import date, timedelta
from validate import validate_date

class TestValidateDate(unittest.TestCase):
    def test_future_date_valid(self):
        ok, _ = validate_date(date.today() + timedelta(days=10))
        self.assertTrue(ok)

    def test_past_date_rejected(self):
        ok, _ = validate_date(date.today() - timedelta(days=1))
        self.assertFalse(ok)

if __name__ == "__main__":
    unittest.main()
PY

claude
```

- [ ] **VERIFY:** `validate.py` and `test_validate.py` exist before continuing

**Step 2.1 — WITHOUT Plan Mode:**

Ask Claude:
> Add error handling for malformed input, more thorough unit tests covering every rule, and a CLI wrapper to the reservation validator. The CLI should accept a date string as an argument and print whether it's valid.

Watch it for ~30 seconds — **do not let it finish**. Press `Esc` to interrupt. The point is to see Claude diving in, not the final output.

- [ ] **VERIFY:** Claude started writing files immediately, without reading first
- [ ] Notes: _________________________________

**Step 2.2 — WITH Plan Mode:**

Press `Shift+Tab` until `plan mode` shows in the input bar (or type `/plan`). Ask:
> Before making any changes, analyze what's here. What files exist? What would need to change to add malformed-input handling, more thorough unit tests covering every rule, and a CLI wrapper? What's the right order of operations? What could go wrong?

- [ ] **VERIFY:** Claude read the file but did **NOT** modify it
- [ ] **VERIFY:** Plan includes file breakdown and implementation order

Press `Shift+Tab` again until `plan mode` disappears from the input bar, then tell Claude:
> Implement the plan you just described.

- [ ] **VERIFY:** **CRITICAL** — Is the planned output noticeably better than the half-finished unplanned attempt? (yes / no)
- [ ] Quality comparison notes: _________________________________

### Issue Log — Phase 2
- [ ] _________________________________
- [ ] _________________________________

---

## PHASE 3: Externalize Exercise (3 min)

> Stay in `~/workshop-dryrun/warmup-plan` from Phase 2. Do not change directories.

**Step 3.1 — /init:**
```
/init
```
- [ ] **VERIFY:** `CLAUDE.md` file generated in current directory

**Step 3.2 — # shortcut to add a rule:**

Type `#` as the **first character of a brand-new prompt**, then paste the canonical warmup rule:
> # Always run python -m pytest after every code change. Never skip tests.

Claude will ask which CLAUDE.md to save it to — choose the **project-level** one.

- [ ] **VERIFY:** Memory-target picker appeared (not just inline text)
- [ ] **VERIFY:** Rule added to `CLAUDE.md`

**Step 3.3 — Create a skill:**

Skills must live in their own named subdirectory under `.claude/skills/`. A bare `.claude/skills/SKILL.md` is **not** loaded by the registry.

```bash
mkdir -p .claude/skills/explain-code
```
Then ask Claude to create the skill file:
> Create a skill file at .claude/skills/explain-code/SKILL.md. It must start with YAML front matter between --- fences, with two fields: name: explain-code and description: Explains code with diagrams and analogies. After the closing ---, add markdown instructions: start with an everyday analogy, draw an ASCII diagram, walk through step-by-step, highlight one common gotcha.

- [ ] **VERIFY:** File exists at `.claude/skills/explain-code/SKILL.md` (note the subdirectory)
- [ ] **VERIFY:** File begins with `---` and has both `name:` and `description:` inside the front matter block
- [ ] **VERIFY:** After exiting and restarting `claude`, the skill is in the available list (skills are scanned at session start — there is no hot-reload in this build)

### Issue Log — Phase 3
- [ ] _________________________________
- [ ] _________________________________

---

## PHASE 4: Verify Exercise (2 min)

> Stay in `~/workshop-dryrun/warmup-plan` — that's where the validator + tests + the new CLAUDE.md rule live. After the Phase 3 restart, you should be back in this directory with a fresh `claude` session.

**Sanity check first:**
```bash
ls test_*.py
```
- [ ] **VERIFY:** At least one test file exists. If not, paste Phase 2's "Implement the plan" prompt again before continuing — Phase 4's whole point collapses without tests on disk.

Ask Claude:
> Refactor the validator function to return a dataclass instead of a tuple. Update the tests to match.

- [ ] **VERIFY:** **CRITICAL** — Did Claude run `python -m pytest` (or equivalent) after making the change, *because of the CLAUDE.md rule*?
- [ ] Tests pass? (yes / no)
- [ ] If tests failed, did Claude attempt to fix them and re-run? (yes / no)

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
| Tests run automatically (per CLAUDE.md rule) | [ ] | [ ] |
| Skill loaded after restart (in correct subdir) | [ ] | [ ] |
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
| Effort levels | 5 min | ______ | ______ |
| Plan Mode | 4 min | ______ | ______ |
| Externalize | 3 min | ______ | ______ |
| Verify | 2 min | ______ | ______ |
| Guided build | 28 min | ______ | ______ |
| **Total** | **~42 min** | ______ | ______ |

### Adjustments Needed

- _________________________________
- _________________________________
- _________________________________

---

*Dry run script for Claude Code Hands-On Workshop*
*Run on Bedrock if possible. Run on direct API if not.*
*Log every issue. Fix before workshop day.*
