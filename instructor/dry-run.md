# Claude Code Workshop — Dry Run Script
## Run this to simulate the attendee experience before the workshop

**Purpose:** Walk through every exercise step by step to verify:
1. All commands work in a Bedrock-backed environment
2. Effort level differences are visible and meaningful
3. Plan Mode produces noticeably better output than unplanned
4. CLAUDE.md rules are picked up (especially the "run check.sh" rule)
5. Guided build can complete in allotted time
6. Context usage stays manageable

**How to use:** Open a terminal. Run each step in order. Check the **VERIFY** note after each. Log issues in the checkboxes provided.

**Flow rule:** The warmup lives inside **one Claude session** and **one directory**. No exits, no restarts, no `cd` until Phase 5. If you find yourself reaching for a new terminal, stop — you are off script.

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

## PHASE 1: Effort Levels Exercise (3 min)

> **This phase mirrors `warmup-exercises.md` Exercise 1 verbatim.** Run the canonical script — do not improvise prompts. Start the session you'll use for the rest of the warmup here and **do not exit it** until after Phase 4.

```bash
mkdir -p ~/workshop-dryrun/warmup && cd ~/workshop-dryrun/warmup
claude
```

**Step 1.1 — Low effort:**
```
/effort low
```
Paste this prompt (the exact one from `warmup-exercises.md`):
> Write a short retrospective document for a 1-hour hands-on workshop. Cover what went well, what didn't, and what to change next time.

- [ ] **VERIFY:** Minimal output — short bullets, no structure beyond the three sections
- [ ] Note response time: ______ seconds
- [ ] Note response length: ______ lines

**Step 1.2 — High effort:**
```
/effort high
```
Paste the **same** prompt again.

- [ ] **VERIFY:** More thorough output — executive framing, nuanced observations, concrete suggestions
- [ ] Note response time: ______ seconds
- [ ] Note response length: ______ lines
- [ ] **CRITICAL:** Is the difference visible enough to use in a live demo? (yes / no)

**Step 1.3 — Reset the dial:**
```
/effort medium
```

### Issue Log — Phase 1
- [ ] _________________________________
- [ ] _________________________________

---

## PHASE 2: Plan Mode Exercise (3 min)

> Stay in the same Claude session from Phase 1. No new directory, no restart.

Ask Claude to create the baseline retrospective file:
> Create a file retro.md in the current directory with these four sections and two or three bullet points in each: "## What Went Well", "## What Didn't", "## Action Items", "## Metrics". Treat it as a retrospective for a 1-hour hands-on Claude Code workshop.

- [ ] **VERIFY:** `retro.md` exists in the current directory
- [ ] **VERIFY:** All four section headers are present in the file

**Step 2.1 — WITHOUT Plan Mode:**

Ask Claude:
> Rewrite retro.md: add an executive summary at the top, fill in the Action Items with realistic owners and deadlines, populate the Metrics section with sensible numbers, and tighten the language everywhere. Do not remove or rename any of the existing section headers.

Watch it for ~30 seconds — **do not let it finish**. Press `Esc` to interrupt. The point is to see Claude diving in, not the final output.

- [ ] **VERIFY:** Claude started editing the file immediately, without a plan
- [ ] Notes: _________________________________

**Step 2.2 — WITH Plan Mode:**

Press `Shift+Tab` until `plan mode` shows in the input bar (or type `/plan`). Ask the **same** thing:
> Rewrite retro.md: add an executive summary at the top, fill in the Action Items with realistic owners and deadlines, populate the Metrics section with sensible numbers, and tighten the language everywhere. Do not remove or rename any of the existing section headers.

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

> Still in the same session, same directory. Do not exit Claude.

**Step 3.1 — /init:**
```
/init
```
- [ ] **VERIFY:** `CLAUDE.md` file generated in current directory

**Step 3.2 — Create the verification script first** so the CLAUDE.md rule in Step 3.3 has something to point at:

Ask Claude:
> Create a shell script check.sh in the current directory. It should grep retro.md for these required sections: "## What Went Well", "## What Didn't", "## Action Items", "## Metrics". Print "OK" if all four are present. For each missing section, print "FAIL: missing <section name>" on its own line and exit non-zero. Make the script executable.

- [ ] **VERIFY:** `check.sh` exists and is executable
- [ ] Test it from bash mode by typing `!./check.sh` in the prompt — it should print `OK`

**Step 3.3 — `#` shortcut to add the rule:**

Type `#` as the **first character of a brand-new prompt**, then paste the canonical warmup rule:
> # After any change to retro.md, always run ./check.sh and confirm it passes before responding.

Claude will ask which CLAUDE.md to save it to — choose the **project-level** one.

- [ ] **VERIFY:** Memory-target picker appeared (not just inline text)
- [ ] **VERIFY:** Rule added to `CLAUDE.md`

**Step 3.4 — Create a skill:**

Ask Claude to create the skill file (Claude handles the directory):
> Create a skill file at .claude/skills/explain-doc/SKILL.md. It must start with YAML front matter between --- fences, with two fields: name: explain-doc and description: Summarizes a document by identifying the thesis, key decisions, and open questions. After the closing ---, add markdown instructions: identify the main thesis in one sentence, list up to three key decisions the document makes, flag any unanswered questions, and suggest one concrete improvement.

- [ ] **VERIFY:** File exists at `.claude/skills/explain-doc/SKILL.md` (note the subdirectory)
- [ ] **VERIFY:** File begins with `---` and has both `name:` and `description:` inside the front matter block
- [ ] **Do not** restart Claude to "prove" the skill loaded — skills are scanned at session start only. The demonstration point is that we wrote it to a file, not that the current session is using it. Mention this to attendees as a footnote.

### Issue Log — Phase 3
- [ ] _________________________________
- [ ] _________________________________

---

## PHASE 4: Verify Exercise (1 min)

> Still in the same session, same directory. Do not exit Claude. All of `retro.md`, `check.sh`, and the CLAUDE.md rule were created above and live on disk.

**Sanity check first** from bash mode — type this in the prompt:
```
!ls retro.md check.sh && ./check.sh
```
- [ ] **VERIFY:** Both files exist and `check.sh` prints `OK` against the current `retro.md`. If not, fix the baseline before continuing.

Ask Claude:
> Reorganize retro.md: move "Action Items" to the top of the document, and rename the "What Didn't" section to "Pain Points".

- [ ] **VERIFY:** **CRITICAL** — Did Claude run `./check.sh` after making the change, *because of the CLAUDE.md rule*?
- [ ] **VERIFY:** Did the check fail with "FAIL: missing ## What Didn't" (or similar)?
- [ ] **VERIFY:** Did Claude then self-correct — rename the section back, update `check.sh`, or ask for clarification?

### Issue Log — Phase 4
- [ ] _________________________________
- [ ] _________________________________

---

## PHASE 5: Guided Build — Pick ONE Path (28 min)

> **Recommended:** Path B (Backend API) — it has the most verification steps. This phase is a **separate, fresh Claude session** in a new directory. Exit the warmup session (`/exit` or `Ctrl+D`) and start over here.

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
- Always run `python3 -m unittest discover -s tests` after changes
- Use stdlib only — no external dependencies
- All output goes to `./output/`

- [ ] **VERIFY:** Rules present in `CLAUDE.md`

**Step 5.2 — Plan Mode — paste the full API spec:**

Enter Plan Mode (Shift+Tab until `plan mode` shows), then paste:
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
- [ ] **VERIFY:** Tests pass (via `python3 -m unittest discover -s tests`)
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
| CLAUDE.md rule picked up (check.sh fired) | [ ] | [ ] |
| check.sh failure triggered self-correction | [ ] | [ ] |
| Skill file created in correct subdir | [ ] | [ ] |
| Warmup stayed in one session start-to-finish | [ ] | [ ] |
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
| **Total** | **~39 min** | ______ | ______ |

### Adjustments Needed

- _________________________________
- _________________________________
- _________________________________

---

*Dry run script for Claude Code Hands-On Workshop*
*Run on Bedrock if possible. Run on direct API if not.*
*Log every issue. Fix before workshop day.*
