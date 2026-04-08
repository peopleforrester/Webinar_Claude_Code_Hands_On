# Live Teaching Card — Workshop 2026-04-09, 12:00 ET

Your at-podium reference. Keep this open alongside your terminal and
`warmup-exercises.md`. Scroll top-to-bottom in sync with the clock.

Preparation detail lives in `instructor-guide.md`. This card is purely
operational — what to say, what to paste, what to point at, in order.

---

## T-5 min — Pre-flight Checklist

- [ ] Claude CLI version: `claude --version` → 2.1.x
- [ ] Model set to Opus 4.6: `claude /model`
- [ ] Backend connected: `claude /status`
- [ ] Terminal font size cranked up (20pt+ for share-readability)
- [ ] Scratch directory ready: `mkdir -p ~/workshop-live && cd ~/workshop-live`
- [ ] **`~/.claude/CLAUDE.md` skill installation policy temporarily commented out** — otherwise Ex3 skill creation will refuse on your machine. (Attendees don't have this, only you.)
- [ ] Second window: `warmup-exercises.md` open (you'll paste from it)
- [ ] Third window: this file
- [ ] `claude` session NOT yet started — you'll do it live so they see it
- [ ] Mic check, screen-share check, slack/notifications silenced
- [ ] Water within reach

---

## 0:00–5:00 — Orientation

**Say (30 sec):**

> Welcome. This is a hands-on session, not a pitch. In 60 minutes you'll feel every pattern that makes Claude Code reliable in production. Observers are welcome — follow along or just watch, whichever works. If you hit a setup issue, drop it in chat and our team will help you offline while we keep moving.

**Say (30 sec — what Claude Code is):**

> Claude Code is an agentic coding tool that runs in your terminal. It reads files, writes code, runs commands, and iterates — through natural language. It's not autocomplete. It executes multi-step tasks autonomously. Today you'll control that autonomy with four patterns we'll name at the end.

**Do — everyone runs together:**

```bash
claude --version
claude /model
```

**Say:**

> If you see 2.1.x and Opus 4.6 in that list, you're in. If not, chat us and we'll fix it after.

**30-second tour — put this table on screen or call it out verbally:**

| Control | What it does |
|---|---|
| `Shift+Tab` | Cycle modes (Default → Accept Edits → Plan) |
| `/effort low\|medium\|high` | Set reasoning depth |
| `/context` | Show what's in the context window |
| `#` as first char | Save a rule to CLAUDE.md |
| `!` prefix | Run a shell command inside Claude |

---

## 5:00–15:00 — Warmup Block (ONE session, ONE directory)

> **Flow rule for you:** Do not exit the session, do not `cd`, do not restart. All four warmup exercises run inside one Claude session. If you find yourself reaching for a new terminal tab, stop.

**Start the session live** so attendees see it:

```bash
mkdir -p ~/workshop-live && cd ~/workshop-live
claude
```

### 5:00–8:00 — Exercise 1: Effort Levels (3 min)

**Say:**

> Claude has a reasoning dial. You control it. Same prompt, two dials, watch the difference.

**Paste (low):**

```
/effort low
```

**Paste (prompt 1 of 2):**

```
Write a short retrospective document for a 1-hour hands-on workshop.
Cover what went well, what didn't, and what to change next time.
```

Let it finish. Read the output aloud briefly.

**Paste (high):**

```
/effort high
```

**Paste (same prompt):**

```
Write a short retrospective document for a 1-hour hands-on workshop.
Cover what went well, what didn't, and what to change next time.
```

**Point out:**
- Wall time: high is ~2x longer
- Low: bare bullet list, 3 short sections
- High: executive framing, nuanced observations, specific concrete suggestions

**Say:**

> Default is medium. You control the dial per-command. If you want max reasoning on a single turn, type `ultrathink` in your prompt and it burns extra thinking for that one turn.

**Reset:**

```
/effort medium
```

---

### 8:00–11:00 — Exercise 2: Plan Mode (3 min)

**Say:**

> Now we need a baseline file Claude can read and modify. Watch.

**Paste (baseline creation):**

```
Create a file retro.md in the current directory with these four sections
and two or three bullet points in each: "## What Went Well",
"## What Didn't", "## Action Items", "## Metrics". Treat it as a
retrospective for a 1-hour hands-on Claude Code workshop.
```

Wait for `retro.md` to be created. Confirm in the chat pane.

**Say:**

> First we'll do it WITHOUT Plan Mode. Just dive in.

**Paste (unplanned ask):**

```
Rewrite retro.md: add an executive summary at the top, fill in the
Action Items with realistic owners and deadlines, populate the Metrics
section with sensible numbers, and tighten the language everywhere.
Do not remove or rename any of the existing section headers.
```

Let it run ~30 seconds. **Then press `Esc`** to interrupt.

**Say:**

> Notice Claude dove straight in. No reading, no thinking, just writing. Now let's do the same thing WITH Plan Mode.

**Do — enter Plan Mode by pressing `Shift+Tab` until the input bar shows `plan mode`.**

> If `plan mode` doesn't appear after one Shift+Tab, keep pressing — in this build it cycles through multiple modes.

**Paste (same ask):**

```
Rewrite retro.md: add an executive summary at the top, fill in the
Action Items with realistic owners and deadlines, populate the Metrics
section with sensible numbers, and tighten the language everywhere.
Do not remove or rename any of the existing section headers.
```

Read the plan aloud for ~20 seconds. Point out: it read the file, identified sections, proposed order, **and did not touch the file**.

**Do — exit Plan Mode by pressing `Shift+Tab` until `plan mode` disappears.**

**Paste (implement):**

```
Implement the plan you just described.
```

**Point out:**
- Without planning → chaos / half-finished
- With planning → coordinated coherent pass
- The plan is free — you get it before touching files

---

### 11:00–14:00 — Exercise 3: Externalize (3 min)

**Say:**

> Everything that stays only in the conversation is ephemeral. Anything you want to survive `/compact`, `/clear`, or a new session has to go in a file. Three things get written here: a CLAUDE.md, a verification script, and a skill.

**Paste (bootstrap):**

```
/init
```

Wait for `CLAUDE.md` to generate.

**Say:**

> Now we need a deterministic check that our rule can run.

**Paste (check.sh creation):**

```
Create a shell script check.sh in the current directory. It should
grep retro.md for these required sections: "## What Went Well",
"## What Didn't", "## Action Items", "## Metrics". Print "OK" if all
four are present. For each missing section, print "FAIL: missing
<section name>" on its own line and exit non-zero. Make the script
executable.
```

**Sanity check from bash mode — paste:**

```
!./check.sh
```

Should print `OK`. If it doesn't, the baseline is broken — re-create `retro.md`.

**Say:**

> Now the magic: we're going to save a rule to a file using the `#` shortcut. Type `#` as the first character of a brand-new prompt, then the rule. Claude will ask where to save it.

**Paste — literally start with `#`:**

```
# After any change to retro.md, always run ./check.sh and confirm it passes before responding.
```

Claude opens the memory-target picker. **Pick the project-level CLAUDE.md.**

**Say:**

> That rule now lives in a file. It will still be there after compact, after clear, after a fresh session tomorrow. The conversation is temporary. The file is permanent.

**Paste (skill creation):**

```
Create a skill file at .claude/skills/explain-doc/SKILL.md. It must
start with YAML front matter between --- fences, with two fields:
  name: explain-doc
  description: Summarizes a document by identifying the thesis, key decisions, and open questions
After the closing ---, add markdown instructions: identify the main
thesis in one sentence, list up to three key decisions the document
makes, flag any unanswered questions, and suggest one concrete
improvement.
```

**If Claude refuses with a skill-policy message**, say:

> That's a policy in my user CLAUDE.md blocking Write to the skills directory — it won't affect your fresh setup. In a restricted enterprise build you might see the same thing and the workaround is a heredoc in your terminal, which your IT team would provide.

Then use bash mode yourself:

```
!mkdir -p .claude/skills/explain-doc && cat > .claude/skills/explain-doc/SKILL.md <<'MD'
---
name: explain-doc
description: Summarizes a document by identifying the thesis, key decisions, and open questions
---
Identify the main thesis in one sentence, list up to three key decisions the document makes, flag any unanswered questions, and suggest one concrete improvement.
MD
```

**Say:**

> Skills are scanned at session start — this one will be available the next time you launch Claude in this directory. No hot-reload in this build. We wrote it to demonstrate externalization, not to use it right now.

---

### 14:00–15:00 — Exercise 4: Verify — THE PAYOFF (1 min)

**Say:**

> Watch what happens when I deliberately break the rule.

**Paste:**

```
Reorganize retro.md: move "Action Items" to the top of the document,
and rename the "What Didn't" section to "Pain Points".
```

**Point out, as it happens:**
1. Claude makes the edit
2. Because of the CLAUDE.md rule, Claude runs `./check.sh`
3. The check **fails** because `## What Didn't` was renamed
4. Claude sees the failure in the script output and self-corrects

**Say (emphatic):**

> This is the whole point of the workshop. Advisory instructions — "please do X" — work about 80% of the time. Deterministic verification — a command that exits 0 or 1 — works 100% of the time. And when it fails, Claude can *see* the failure and fix it. Rule plus check plus auto-run is the core pattern of reliable automation.

---

## 15:00–17:00 — Choose Your Adventure (2 min)

**Say:**

> 30 seconds. No deliberation. Pick what's closest to your day job.

| Pick | Path | Project |
|---|---|---|
| **A** | Frontend | Guest Feedback Dashboard (HTML + vanilla JS) |
| **B** | Backend | Reservation Validation API (Python/Node stdlib) |
| **C** | Infrastructure | Deployment Config Generator (Python stdlib) |
| **D** | Data/Analysis | Operations Log Analyzer (Python stdlib) |

**Tell them:**

> Open `paths/<your-path>/guided-brief.md`. The brief has step-by-step instructions you'll follow along with me. We start the guided build in 30 seconds.

**For mostly non-developers in the room**, steer explicitly to Path D. It's the most accessible — JSON parsing and markdown output, no server or HTML knowledge needed.

---

## 17:00–45:00 — Guided Build (28 min)

**You walk the room through their chosen path.** Everyone is in a different project but the *structure* is identical across all four:

| Phase | Time | What attendees do |
|---|---|---|
| Set Up + Externalize | 3 min | `mkdir`, `cd`, `/init`, `#` rules |
| Plan First | 4 min | Plan Mode, review plan, adjust |
| Build + Verify | 12 min | Exit plan, implement, tests run automatically |
| Iterate + Verify | 5 min | Add features, tests re-run |
| Create Skill | 2 min | Path-specific skill in `.claude/skills/` |
| Check Context | 2 min | `/context`, `/compact` if above 65% |

**Your job during this block:**
- Stay visible but don't lecture. They're working. Let them work.
- Drop in and help individuals on Slack/chat as issues come up.
- Every 5 min call out the time so they know where we are.
- **If you see someone stuck**, suggest they use `/plan` on whatever they're doing — most friction comes from skipping the plan.
- **If you see someone's context above 65%**, tell them to `/compact` immediately.

**Common issues and fixes:**

| Symptom | Fix |
|---|---|
| Claude dove in without reading | Have them enter Plan Mode and ask it to re-analyze |
| Tests aren't running automatically | Check their CLAUDE.md has the test command explicitly |
| "Claude keeps forgetting X" | Put X in CLAUDE.md with `#` — stop relying on prompt memory |
| Context above 65% | `/compact` now |
| Plan looks shallow | `/effort high` then re-enter Plan Mode |

---

## 45:00–52:00 — Independent Build (7 min)

**Say:**

> You will not finish this. That is by design. The independent challenge is sized to take 20–30 minutes. You have 7 here to start, feel the workflow, and have something to continue at home.

**Tell them the checklist before they dive in:**

- Enter Plan Mode before building
- Run `/context` to check your window
- Externalize your plan to `PLAN.md`
- Set up verification (tests or a validation script)

**At the 50-minute mark, say:**

> Two minutes. Save your state. Write down where you are.

---

## 52:00–55:00 — Name the Framework (3 min) — THE REVEAL

**Say exactly this:**

> You just used four patterns. I deliberately didn't name them until now because adults don't internalize frameworks from descriptions — they internalize from experience. You already have the reps. Here are the names.

**Show this on screen or call it out:**

| Pillar | What you did | Why it matters |
|---|---|---|
| **Manage Context** | Ran `/context`, compacted | Context window is finite. Monitor it. One feature per session. |
| **Plan Before Code** | Used Plan Mode | Read first, think second, implement third. |
| **Externalize Decisions** | Created CLAUDE.md, check.sh, Skills | Conversations get compacted. Files persist. |
| **Verify Output** | Ran tests / check.sh and saw self-correction | Advisory ~80%. Deterministic 100%. |

**Say:**

> Those four, together, are the difference between a demo that impresses you in a keynote and a tool you ship with on Monday. If you take one thing from today, take the rule-plus-check pattern — a rule in CLAUDE.md paired with a command that verifies it. That one pattern alone changes the reliability curve.

**Take-home commands** (throw on screen):

| Command | What it does |
|---|---|
| `/plan` or `Shift+Tab` | Enter/exit Plan Mode |
| `/effort low\|medium\|high` | Reasoning dial |
| `ultrathink` (in prompt) | Max reasoning for one turn |
| `/context` | Show context window |
| `/compact` | Compress history |
| `#` (as first char) | Save a rule to CLAUDE.md |
| `/init` | Bootstrap CLAUDE.md |
| `!<cmd>` | Run a shell command inside Claude |

**Files to commit after the workshop:** `CLAUDE.md`, `.claude/settings.json`, `.claude/skills/`.

---

## 55:00–60:00 — Q&A (5 min)

**Seed questions if the room is quiet:**
- "What happens when the context window fills up?"
- "Can I use this with my existing IDE?"
- "How is this different from Copilot?"

**Cached answers — don't improvise on these:**

| Question | Answer |
|---|---|
| "Does Claude see my whole codebase?" | It reads files on demand, not all at once. Run `/context` to see what's currently loaded. |
| "Is my code sent to Anthropic?" | In this setup, Bedrock traffic goes to AWS — not to Anthropic. Set `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` for full isolation. |
| "What model are we using?" | Opus 4.6. Sonnet 4.6 is also available — switch with Alt+P. |
| "How is this different from Copilot?" | Copilot autocompletes lines. Claude Code executes multi-step tasks autonomously — it reads, plans, writes, runs commands, and iterates. |
| "What about Agent Teams?" | Enabled in this environment (experimental). Allows spawning sub-agents for parallel work. Worth exploring after you're comfortable with the four pillars. |
| "Does it remember between sessions?" | Auto-memory is disabled in this environment. It's on by default elsewhere. That's why we externalize to CLAUDE.md and Skills — files persist, conversations don't. |
| "What about ultrathink?" | Back after a brief deprecation. Type `ultrathink` directly in your prompt for max reasoning depth on a single turn. |
| "Can I use it without internet?" | Within a restricted enterprise setup like this one, yes — all traffic routes through Bedrock in your own AWS account. No public internet required. |
| "How much does it cost?" | Depends on your enterprise contract. For individuals, Claude Max includes it. Ask your procurement team. |

**Close (at 59:30):**

> Thanks for spending your hour with me. Your projects and skills are in your own directories — take them home. The companion repo link is in the chat. Any follow-up questions, drop them in chat now and I'll answer async.

---

## If Something Breaks — Recovery Paths

| What broke | Do this |
|---|---|
| `claude` command not found | Skip setup, use your own screen-share as the demo surface |
| Model returns empty / hangs | `Ctrl+C` to interrupt, re-paste the prompt |
| Plan Mode toggle not working | Type `/plan` and `/plan` to enter/exit explicitly |
| `#` shortcut doesn't show picker | Type the rule into an open prompt asking Claude to append it to `./CLAUDE.md` manually |
| `check.sh` permission denied | `!chmod +x check.sh` |
| Attendees stuck on Bedrock auth | Defer to IT team in chat, keep the group moving |
| Entire session crashes | Restart `claude` in the same directory — files persist, conversation is gone |
| You lose your place in this card | Look at the wall clock, jump to the time marker |

---

## Emergency Prompts — Copy-Paste Ready

**Ex1 effort prompt:**
```
Write a short retrospective document for a 1-hour hands-on workshop. Cover what went well, what didn't, and what to change next time.
```

**Ex2 baseline:**
```
Create a file retro.md in the current directory with these four sections and two or three bullet points in each: "## What Went Well", "## What Didn't", "## Action Items", "## Metrics". Treat it as a retrospective for a 1-hour hands-on Claude Code workshop.
```

**Ex2 rewrite ask (use for both unplanned and planned):**
```
Rewrite retro.md: add an executive summary at the top, fill in the Action Items with realistic owners and deadlines, populate the Metrics section with sensible numbers, and tighten the language everywhere. Do not remove or rename any of the existing section headers.
```

**Ex3 check.sh:**
```
Create a shell script check.sh in the current directory. It should grep retro.md for these required sections: "## What Went Well", "## What Didn't", "## Action Items", "## Metrics". Print "OK" if all four are present. For each missing section, print "FAIL: missing <section name>" on its own line and exit non-zero. Make the script executable.
```

**Ex3 rule (starts with `#`):**
```
# After any change to retro.md, always run ./check.sh and confirm it passes before responding.
```

**Ex3 skill:**
```
Create a skill file at .claude/skills/explain-doc/SKILL.md. It must start with YAML front matter between --- fences, with two fields: name: explain-doc and description: Summarizes a document by identifying the thesis, key decisions, and open questions. After the closing ---, add markdown instructions: identify the main thesis in one sentence, list up to three key decisions the document makes, flag any unanswered questions, and suggest one concrete improvement.
```

**Ex4 payoff:**
```
Reorganize retro.md: move "Action Items" to the top of the document, and rename the "What Didn't" section to "Pain Points".
```

---

*One session. One directory. Four exercises. One reveal. Good luck, Michael.*
