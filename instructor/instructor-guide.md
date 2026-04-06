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

**Quick check** — everyone runs:

```bash
claude --version
claude /model
```

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

### 5:00–8:00 — Effort Levels (3 min)

Create a scratch directory and start a Claude session:

```bash
mkdir -p scratch && cd scratch
claude
```

Run the same prompt at two effort levels:

1. `/effort low` — then submit the prompt
2. `/effort high` — then submit the same prompt

**The prompt:**

> Write a Python function that validates a theme park reservation date. Rules: no past dates, maximum 60 days in advance, blackout dates are Dec 24–25, Dec 31, and Jul 4.

**What to observe:**

- **Low effort**: Bare function, minimal validation, no edge cases.
- **High effort**: Thorough implementation with edge cases, docstrings, error messages.

**Instructor note**: Default effort is medium. Mention that `ultrathink` (typed directly in the prompt) gives maximum single-turn reasoning depth.

---

### 8:00–11:00 — Plan Mode (3 min)

Same project, more complex task. Two steps — **order matters**.

**Step 1: WITHOUT Plan Mode.**

Ask Claude:

> Add input validation for date format, comprehensive unit tests with pytest, and a CLI wrapper that accepts a date argument.

Let it run. Watch the output.

**Step 2: WITH Plan Mode.**

Enter Plan Mode (Shift+Tab twice or `/plan`), then submit the same request. Claude will analyze first, show a plan, and only implement after you approve.

**Key**: The without-then-with order is critical. Attendees must feel the contrast. If someone's output looks the same planned vs. unplanned, the task wasn't complex enough — have them add more requirements.

---

### 11:00–14:00 — Externalize (3 min)

**Bootstrap CLAUDE.md:**

```
/init
```

This creates a starter `CLAUDE.md` in the project root.

**Add a persistent rule using `#`:**

Type `#` in the prompt, then:

> Always run python -m pytest after every code change. Never skip tests.

This writes the rule directly into CLAUDE.md so it survives compaction and session restarts.

**Create a skill:**

Create `.claude/skills/explain-code/SKILL.md`:

```markdown
# Explain Code

Read the specified file and produce a plain-language explanation suitable for
a non-technical stakeholder. Include: what the code does, key decisions made,
and any risks or limitations.
```

**One sentence on hierarchy**: CLAUDE.md has 4 levels — org-managed, user, project, and local — each scoped differently. Keep each under 200 lines. Every instruction competes for context window space.

---

### 14:00–15:00 — Verify (1 min)

Ask Claude:

> Refactor validate_date to use a dataclass for configuration.

**Watch what happens.** Because of the CLAUDE.md rule, Claude runs `python -m pytest` after the refactor — automatically.

**Key message**: Advisory instructions (CLAUDE.md rules) land about 80% of the time. Deterministic verification (tests, linters, hooks) lands 100% of the time. Use both.

---

### 15:00–17:00 — Choose Your Adventure (2 min)

| Path | Project | Stack |
|------|---------|-------|
| **A — Frontend** | Guest Feedback Dashboard | HTML + vanilla JS |
| **B — Backend** | Reservation Validation API | Python or Node, stdlib only |
| **C — Infrastructure** | Deployment Config Generator | Python stdlib CLI |
| **D — Data/Analysis** | Operations Log Analyzer | Python stdlib |

30 seconds to pick. Open the `guided-brief.md` for your chosen path.

---

### 17:00–45:00 — Guided Builds (28 min)

> **Note**: This block is 28 minutes — 5 more than previous versions. Let attendees absorb. Don't rush.

All four paths follow the same structure. The four pillars are woven in as explicit callouts during each phase.

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

- **Mostly non-developers**: Steer toward Path D (Data/Analysis). It's the most accessible — JSON parsing and markdown output, no server or HTML knowledge needed.
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
- Test: [python -m pytest / npm test / bash test.sh]
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
