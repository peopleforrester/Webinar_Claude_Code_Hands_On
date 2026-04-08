# Build with Claude Code: No Pitches, Just Practice
## v5.4 — Workshop Instructor Guide

---

## ENVIRONMENT NOTES FOR INSTRUCTOR

**Target**: Restricted enterprise environment, Bedrock-backed.

**Environment flags** (set before the session):

| Flag | Value |
|------|-------|
| `CLAUDE_CODE_DISABLE_AUTO_MEMORY` | `true` |
| `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` | `true` |
| `CLAUDE_CODE_DISABLE_1M_CONTEXT` | `true` |

**Feature availability**:

| Available | Not Available |
|-----------|---------------|
| Claude Code CLI full feature set | claude.ai web |
| Plan Mode (Shift+Tab twice or `/plan`) | Claude Code web |
| `/effort` (low / medium / high / ultrathink) | `/teleport` |
| `/debug`, `/insights` | Internet MCP servers |
| CLAUDE.md — all 4 levels | 1M context window |
| Skills, hooks, subagents | Auto-Memory (disabled for workshop) |
| Local filesystem access | Web search |
| Opus 4.6 + Sonnet 4.6 via Bedrock (200K context) | |

**Confirmed capacity**: Both Opus 4.6 and Sonnet 4.6 available via Bedrock with 200K context. No rate limit for 30 concurrent users.

**Setup wizard**: v2.1.92 added an interactive Bedrock setup wizard (`/setup-bedrock`). Use this if anyone needs to reconfigure auth during the session.

**Pedagogical approach**: Experience-first. The four pillars are not lectured upfront — they are felt through exercises and named afterward (at minute 52).

---

## PART 1: SESSION OVERVIEW

| Time | Block | What Happens |
|------|-------|-------------|
| 0:00–5:00 | Orientation | Verify setup, run first command |
| 5:00–8:00 | Effort Levels | Same prompt at low / medium / high |
| 8:00–11:00 | Plan Mode | Build without planning vs. with planning |
| 11:00–14:00 | Externalize | Set up CLAUDE.md and Skills |
| 14:00–15:00 | Verify | Run tests, see Claude self-correct |
| 15:00–17:00 | Choose Your Adventure | Pick a path |
| 17:00–45:00 | Guided Build | Build real project with all four patterns |
| 45:00–52:00 | Independent Build | Start solo challenge |
| 52:00–55:00 | Name the Framework | Four Pillars cheat sheet |
| 55:00–60:00 | Q&A | Open discussion |

---

## PART 2: DETAILED WORKSHOP OUTLINE

### 0:00–5:00 — Orientation (5 min)

**Acknowledge the room.** This is a hands-on session. Observers are welcome — they can follow along or just watch.

**Quick check** — everyone runs these on the **command line**, not inside a Claude session:

```bash
claude --version              # CLI version — 2.1.x expected
claude -p "reply with OK"     # End-to-end ping — confirms auth, backend, and model
```

Both are one-shot commands that print and exit. Do **not** tell them to run `claude /model` or `claude /status` on the shell — those drop you into the interactive REPL with the slash command queued, which breaks flow. The model and backend will also appear in the startup banner when they launch `claude` for the warmup.

If anyone fails here, defer to the IT team while continuing with the rest of the group.

**30-second context**: Claude Code is an agentic coding tool that runs in your terminal. It reads files, writes code, runs commands, and iterates — all through natural language. It is not autocomplete. It executes multi-step tasks autonomously.

**30-second tour** of key controls:

| Control | What It Does |
|---------|-------------|
| Shift+Tab (twice) or `/plan` | Enter Plan Mode |
| `/effort low\|medium\|high` | Set reasoning effort |
| `/context` | Show what's in the context window |
| `#` in prompt | Add a note/rule to CLAUDE.md |
| Alt+P | Switch model (Opus ↔ Sonnet) |

---

### 5:00–15:00 — Warmup Block (10 min, one Claude session)

**Critical flow rule:** The entire warmup runs inside **one Claude session** and **one directory**. No exits, no restarts, no `cd`. The exercises are deliberately non-code so both developers and non-developers in the room can follow along and feel the same contrasts.

Attendees open `warmup-exercises.md` and start the shared session:

```bash
mkdir -p ~/workshop-warmup && cd ~/workshop-warmup
claude
```

The shared task across all four exercises is drafting a short workshop retrospective document (`retro.md`) — everyone in the room is literally living a workshop, so they can all relate to the content.

---

#### 5:00–8:00 — Effort Levels (3 min)

Run the same prompt at two effort levels:

1. `/effort low` — then submit the prompt
2. `/effort high` — then submit the same prompt

**The prompt:**

> Write a short retrospective document for a 1-hour hands-on workshop. Cover what went well, what didn't, and what to change next time.

**What to observe:**

- **Low effort**: Bare bullet list, three short sections, no nuance.
- **High effort**: Structured sections with an executive framing, nuanced observations, and concrete suggestions.

No files are written in this exercise — the contrast lives entirely in the chat window.

**Instructor note**: Default effort is medium. Mention that `ultrathink` (typed directly in the prompt) gives maximum single-turn reasoning depth. Reset the dial with `/effort medium` before Exercise 2.

---

#### 8:00–11:00 — Plan Mode (3 min)

Same session, same directory. First, seed the baseline — ask Claude to create `retro.md` with four specific section headers:

> Create a file retro.md in the current directory with these four sections and two or three bullet points in each: "## What Went Well", "## What Didn't", "## Action Items", "## Metrics". Treat it as a retrospective for a 1-hour hands-on Claude Code workshop.

Those exact headers matter — the `check.sh` script in Exercise 3 greps for them.

**Step 1: WITHOUT Plan Mode.** Ask Claude:

> Rewrite retro.md: add an executive summary at the top, fill in the Action Items with realistic owners and deadlines, populate the Metrics section with sensible numbers, and tighten the language everywhere. Do not remove or rename any of the existing section headers.

Watch for ~30 seconds, then `Esc` to interrupt. The point is seeing Claude dive in without a plan, not the final output.

**Step 2: WITH Plan Mode.** Press `Shift+Tab` until `plan mode` shows (or type `/plan`). Submit the same request. Claude reads the file, produces a coordinated plan, and modifies nothing. Exit Plan Mode (Shift+Tab again until `plan mode` disappears), then tell Claude "Implement the plan you just described."

**Key**: The without-then-with order is critical. Attendees must feel the contrast. If someone's output looks the same planned vs. unplanned, the task wasn't complex enough — have them add more requirements to the rewrite ask.

---

#### 11:00–14:00 — Externalize (3 min)

Still in the same session, same directory. Three things get written to disk here: a CLAUDE.md, a verification script, and a skill.

**Step 1 — Bootstrap CLAUDE.md:**

```
/init
```

This creates a starter `CLAUDE.md` in the project root.

**Step 2 — Create the verification script first** (the rule in Step 3 will point at it):

> Create a shell script check.sh in the current directory. It should grep retro.md for these required sections: "## What Went Well", "## What Didn't", "## Action Items", "## Metrics". Print "OK" if all four are present. For each missing section, print "FAIL: missing <section name>" on its own line and exit non-zero. Make the script executable.

Attendees can sanity-check it by typing `!./check.sh` in the prompt (bash mode) — should print `OK`.

**Step 3 — Add a persistent rule using `#`:**

Type `#` as the first character of a brand-new prompt, then:

> After any change to retro.md, always run ./check.sh and confirm it passes before responding.

Claude will ask which CLAUDE.md to save it to — choose the **project-level** one. This writes the rule directly into CLAUDE.md so it survives compaction and session restarts.

**Step 4 — Create a skill:**

> Create a skill file at .claude/skills/explain-doc/SKILL.md. It must start with YAML front matter between --- fences, with two fields: name: explain-doc and description: Summarizes a document by identifying the thesis, key decisions, and open questions. After the closing ---, add markdown instructions: identify the main thesis in one sentence, list up to three key decisions the document makes, flag any unanswered questions, and suggest one concrete improvement.

Claude handles the `mkdir` for `.claude/skills/explain-doc/` itself.

> **Do not restart Claude to "prove" the skill loaded.** Skills are scanned at session start only — there is no hot-reload in this build. The pedagogical point is that the skill is now on disk and will be available the next time attendees launch `claude`. Mention this as a footnote and keep moving.

**One sentence on hierarchy**: CLAUDE.md has 4 levels — org-managed, user, project, and local — each scoped differently. Keep each under 200 lines. Every instruction competes for context window space.

---

#### 14:00–15:00 — Verify (1 min)

Ask Claude:

> Reorganize retro.md: move "Action Items" to the top of the document, and rename the "What Didn't" section to "Pain Points".

**Watch what happens.** Because of the CLAUDE.md rule, Claude runs `./check.sh` after the edit. The check **fails** — renaming `## What Didn't` to `## Pain Points` triggers `FAIL: missing ## What Didn't`. Claude sees the failure in the script output and self-corrects: renames the section back, updates `check.sh`, or asks which the user meant.

**Key message**: Advisory instructions (CLAUDE.md rules) land about 80% of the time. Deterministic verification (tests, linters, hooks, scripts) lands 100% of the time — and when it fails, Claude can *see* the failure and fix it. That visceral self-correction moment is the payoff of the entire warmup.

---

### 15:00–17:00 — Choose Your Adventure (2 min)

| Path | Project | Stack |
|------|---------|-------|
| **A — Frontend** | Guest Feedback Dashboard | HTML + vanilla JS |
| **B — Backend** | Reservation Validation API | Python or Node, stdlib only |
| **C — Infrastructure** | Deployment Config Generator | Python stdlib CLI |
| **D — Data/Analysis** | Operations Log Analyzer | Python stdlib |
| **E — Business** | Meeting Prep Kit (no code — Claude IS the tool) | Markdown + shell verify only |

30 seconds to pick. Open the `guided-brief.md` for your chosen path.

**For non-developers in the room:** steer to Path E. **Path E is deliberately zero-code** — the attendee does not write Python, JavaScript, or anything else. They copy a Skill file into their project, point Claude at a meeting transcript, and Claude generates five stakeholder artifacts (summary, decisions, action items CSV, follow-up email, timeline). The model is the tool. Say this out loud when they pick paths, or PMs will assume Path E is "too technical" and default to sitting it out.

---

### 17:00–45:00 — Guided Builds (28 min)

> **Note**: This block is 28 minutes — 5 more than previous versions. Let attendees absorb. Don't rush.

All five paths follow the same structure. The four pillars are woven in as explicit callouts during each phase.

**Common structure for every path:**

| Phase | Time | Pillar |
|-------|------|--------|
| Set Up + Externalize | 3 min | Externalize Decisions |
| Plan First | 4 min | Plan Before Code |
| Build + Verify | 12 min | Verify Output |
| Iterate + Verify | 5 min | Manage Context + Verify Output |
| Create Skill | 2 min | Externalize Decisions |
| Check Context | — | Manage Context |

---

#### Path A: Frontend — Guest Feedback Dashboard

Single-page HTML+JS dashboard displaying guest feedback with filtering, sorting, and summary statistics. Vanilla JS only — no frameworks, no build tools. All rendering in the browser. Sample data embedded in a JS file. Output: `output/dashboard.html` that opens directly in a browser.

**Guided build** walks through layout, data binding, and filter logic.
**Independent challenge**: Add a trend visualization or export feature.

---

#### Path B: Backend — Reservation Validation API

REST-style API handling reservation create/read/validate operations. Python `http.server` or Node `http` module only — no Express, no Flask. JSON request/response. Validates dates, capacity, and conflicts against in-memory data. Output: running server + test results.

**Guided build** walks through route handling, validation logic, and test coverage.
**Independent challenge**: Add capacity management or waitlist logic.

---

#### Path C: Infrastructure — Deployment Config Generator

CLI tool that generates Dockerfile, docker-compose.yml, and CI pipeline configs from a simple project descriptor. Python stdlib only — uses `argparse`, `json`, `os`, `pathlib`. Templates are string-based, no Jinja. Output: generated configs in `output/`.

**Guided build** walks through template generation, CLI argument parsing, and multi-format output.
**Independent challenge**: Add environment-specific overrides or a validation mode.

---

#### Path D: Data/Analysis — Operations Log Analyzer

Log file analyzer that parses JSON-formatted operations logs, computes summary statistics, detects anomalies (e.g., unusually long wait times), and produces markdown reports. Python stdlib only — `json`, `datetime`, `statistics`, `pathlib`. Output: markdown report in `output/`.

**Guided build** walks through parsing, aggregation, and report formatting.
**Independent challenge**: Add time-window analysis or comparative reporting.

---

#### Path E: Business — Meeting Prep Kit

**The zero-code path.** Attendee copies a Skill file into their project, points Claude at a messy meeting transcript, and Claude generates five stakeholder-ready artifacts: executive summary, decisions log, action items CSV (with source-quote audit trail), draft follow-up email, and a topic-by-topic timeline with sentiment. No Python, no JavaScript, no extraction library. The model IS the tool. Sample data is a realistic 47-minute Q2 planning meeting with decisions, slippage, tangents, a late joiner, parked items, and one unresolved launch-date question.

**The key framing for non-developer attendees:** they write no code at all. Their job is judgment — what should a good meeting prep kit contain, how should action items be attributed, what's the right tone for a follow-up email. Claude handles the reasoning and writing. Sell this explicitly when attendees pick paths.

**Why this path exists:** Most Claude Code demos show code generation. That's real but it undersells the tool. Path E demonstrates that Claude Code is equally useful for skilled knowledge work where the bottleneck is judgment, not syntax. For the PM / chief of staff / business lead in the room, this is the path they can take directly to Monday morning.

**Verification story** mirrors the warmup's `check.sh` pattern: a `verify.sh` script checks all five output files exist, CSV header is correct, every action row has an owner and date, summary is under 300 words, and no weasel words appear anywhere. CLAUDE.md rule auto-runs it after every output change. When a rule is violated, Claude sees the failure and self-corrects — same visceral moment as the warmup, applied to document work.

**Guided build** walks through: copying the Skill, Plan Mode review of the extraction approach, running the Skill, iterating with per-audience variants (exec 100-word version, Slack version, per-person commitments, risk radar), and creating a personal org-specific skill.
**Independent challenge**: multi-meeting changelog — compare two transcripts of the same project a week apart, surface what changed, what slipped, and what should have changed but didn't.

---

### 45:00–52:00 — Independent Build (7 min)

**Checklist before starting:**

- [ ] Enter Plan Mode before building
- [ ] Run `/context` to check your window
- [ ] Externalize your plan to `PLAN.md`
- [ ] Set up verification (tests or validation script)

**They will not finish.** That is by design. The independent challenge is sized to take 20–30 minutes. The 7-minute window is enough to start, feel the workflow, and have something to continue at home.

Tell them: "Take this home. You have the full brief, the CLAUDE.md, and the skills. Everything you need to finish is in your project directory."

---

### 52:00–55:00 — Name the Framework (3 min)

Now — and only now — name the four pillars.

| Pillar | What You Did | Why It Matters |
|--------|-------------|----------------|
| **Manage Context** | Ran `/context`, compacted | Context window is finite. Monitor it. One feature per session. |
| **Plan Before Code** | Used Plan Mode | Read first, think second, implement third. |
| **Externalize Decisions** | Created CLAUDE.md, Skills | Conversations get compacted. Files persist. |
| **Verify Output** | Ran tests, watched self-correct | Advisory instructions ~80%. Deterministic verification 100%. |

**Take-home reference card** — key commands and shortcuts:

| Command / Shortcut | What It Does |
|--------------------|-------------|
| `/plan` or Shift+Tab (×2) | Enter/exit Plan Mode |
| `/effort low\|medium\|high` | Set reasoning effort |
| `ultrathink` (in prompt) | Maximum single-turn reasoning |
| `/context` | Show context window contents |
| `/compact` | Compress conversation history |
| `#` (in prompt) | Add rule to CLAUDE.md |
| `/init` | Bootstrap CLAUDE.md |
| `/powerup` | Show all available power features |
| Alt+P | Switch model |
| `/debug` | Debug mode |
| `/insights` | Session insights |

**Files to commit** after the workshop:

- `CLAUDE.md`
- `.claude/settings.json`
- `.claude/skills/`

**Resources:**

- `claude /help` — in-CLI help
- [code.claude.com/docs](https://code.claude.com/docs) — official documentation
- `/powerup` — discover features you haven't tried

---

### 55:00–60:00 — Q&A (5 min)

**Seed questions** (use if the room is quiet):

- "What happens when the context window fills up?"
- "Can I use this with my existing IDE?"
- "How is this different from Copilot?"

**Common Q&A:**

| Question | Answer |
|----------|--------|
| "Does Claude see my whole codebase?" | It reads files on demand, not all at once. Run `/context` to see what's currently loaded. |
| "Is my code sent to Anthropic?" | In this setup, Bedrock traffic goes to AWS — not to Anthropic. Set `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` for full isolation. |
| "What model are we using?" | Opus 4.6. Sonnet 4.6 is also available — switch with Alt+P. |
| "How is this different from Copilot?" | Copilot autocompletes lines. Claude Code executes multi-step tasks autonomously — it reads, plans, writes, tests, and iterates. |
| "What about Agent Teams?" | Enabled in this environment (experimental). Allows spawning sub-agents for parallel work. Worth exploring after you're comfortable with the basics. |
| "Does it remember between sessions?" | Auto-memory is disabled in this environment. It's on by default elsewhere (since v2.1.59). That's why we externalize to CLAUDE.md and Skills — files persist, conversations don't. |
| "What about ultrathink?" | Back after a brief deprecation. Type `ultrathink` directly in your prompt for maximum reasoning depth on a single turn. |

---

## PART 3: INSTRUCTOR NOTES

### Why This Structure

Previous versions front-loaded lectures. Adults don't internalize frameworks from descriptions — they internalize from experience. In this version, attendees are doing from minute 5. The framework is named at minute 52, after they've already used every pillar without knowing the labels.

### Pacing Guide

| Block | Time | Duration | Notes |
|-------|------|----------|-------|
| Warmup | 5:00–15:00 | 10 min | 4 micro-exercises, fast and punchy |
| Path selection | 15:00–17:00 | 2 min | 30 seconds to decide, no deliberation |
| Guided build | 17:00–45:00 | 28 min | Let them absorb. Don't rush. |
| Independent build | 45:00–52:00 | 7 min | Won't finish — by design |
| Name framework | 52:00–55:00 | 3 min | Label the experience |
| Q&A | 55:00–60:00 | 5 min | Let it run long if engaged |

### The Warmup Exercises — Critical Notes

- **Effort levels exercise is the hook.** If it lands, you have the room. The visible difference between low and high effort on the same prompt is immediately compelling.
- **Plan Mode exercise is the "aha moment"** for most people. The contrast between chaotic unplanned output and structured planned output is visceral. Order matters — WITHOUT planning first, THEN with planning.
- If someone's output looks the same planned vs. unplanned, **the task wasn't complex enough**. Have them add more requirements (e.g., "also add logging, error codes, and a config file").

### Handling the Environment

| Topic | Guidance |
|-------|----------|
| Default effort | Medium. Don't change the global default. |
| Agent Teams | ON in this environment. Mention in Q&A, not during instruction. It adds complexity that distracts from the four pillars. |
| Auto-Memory | OFF for this workshop. Mention during the externalization exercise as "this feature exists in normal environments — that's why we're teaching you the manual version first." |
| Observers | Acknowledge at the top of the session. Don't slow down for them. |
| Auth issues | Defer to the IT team (pre-workshop confirmation should have caught these). Don't debug Bedrock auth live. |

### Adapting to Your Audience

- **Mostly non-developers**: Steer hard toward Path E (Business — Meeting Prep Kit). It is genuinely zero-code — attendees don't write or even read Python. They copy a Skill file, point Claude at a transcript, and get five stakeholder-ready artifacts. Path D (Data/Analysis) is a strong second for analysts comfortable reading code but not writing it.
- **All senior devs**: Move faster through the warmup, allocate more time for the independent build, and point them toward hooks (`.claude/hooks/`) as a post-workshop exploration topic.
- **Mixed audience**: Let people self-select paths. The path structure handles the skill spread naturally.

---

## PART 4: STARTER FILES

### Starter CLAUDE.md (for all paths)

```markdown
# Workshop Project

## Build & Test
- Language: [Python/Node.js/Bash]
- Run: [python main.py / node index.js / bash generate.sh]
- Test: [python3 -m unittest discover -s tests / npm test / bash test.sh]
- Run tests after every code change. Never skip.

## Conventions
- No external dependencies (stdlib only)
- All output goes to ./output/ directory
- Error handling: log warnings, never crash on bad input
- Include sample/mock data for testing

## Don't
- Don't make network requests
- Don't access files outside project directory
- Don't use hardcoded absolute paths
```

### Starter settings.json (for all paths)

```json
{
  "permissions": {
    "deny": [
      "Read(~/.ssh/**)",
      "Read(~/.aws/**)",
      "Read(~/.env)",
      "Bash(curl *)",
      "Bash(wget *)"
    ]
  }
}
```

> **Note**: The companion repo has expanded deny rules including `pip`, `npm`, `git clone`, and other network-capable commands.

---

*v5.4 | Claude Code Hands-On Workshop*
*Experience-first structure. Four pillars revealed through exercises, named at the end.*
