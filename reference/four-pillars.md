# The Four Pillars of Effectiveness

A concise reference for the workshop's four pillars framework.

---

## Pillar 1: Manage Context

**Problem:** LLM performance degrades as the context window fills — a phenomenon called "context rot." Well before the window is full, the model starts losing track of earlier instructions and decisions.

**Rule:** Compact at 65-70%, not 90%. One feature per session.

**Commands:** `/context`, `/compact`, `/clear`, `/btw`, `/effort low`

### Context Level Guide

| Context Usage | Action |
|---------------|--------|
| 0-65% | Work normally |
| 65-70% | Compact or start a fresh session |
| 70-80% | Compact NOW — you are in the danger zone |
| 80%+ | Too late — quality is already degraded |

---

## Pillar 2: Plan Before Code

Use Plan Mode (`Shift+Tab` to cycle modes, or `/plan`) before implementation.

**In Plan Mode:** Claude reads everything but modifies nothing. It can explore the codebase, analyze files, and reason about architecture — without touching a single line of code.

### Workflow

1. **Enter Plan Mode** — `Shift+Tab` to cycle modes, or `/plan`
2. **Describe what you want** — be specific about the outcome
3. **Review the plan** — Claude proposes an approach; you refine it
4. **Exit Plan Mode** — `Shift+Tab` to cycle back, or `/plan` again
5. **Implement** — Claude executes the agreed plan

Use `/effort` to control reasoning depth. Default is medium — set `/effort high` for complex work. Use `ultrathink` in your prompt for max effort on a single turn.

---

## Pillar 3: Externalize Decisions

**If it matters, get it out of the conversation and into a file.**

Conversations are ephemeral. Files are permanent. Every decision that stays only in chat is a decision you will lose.

| What | Where | Why |
|------|-------|-----|
| Project standards | `CLAUDE.md` (under 200 lines) | Loaded every session automatically |
| Reusable workflows | `.claude/skills/*/SKILL.md` | Loaded on-demand when invoked |
| Current task state | `PROJECT_STATE.md` | Survives `/clear` and context resets |
| Decisions made | `DECISIONS.md` or commit messages | Permanent record |
| Claude's learnings | `~/.claude/projects/<project>/memory/` | Auto-saved, loaded next session (when enabled) |
| Org-wide policy | `/etc/claude-code/CLAUDE.md` | Managed, cannot be overridden |

### A Note on Auto-Memory

When enabled, auto-memory captures build commands, debugging patterns, and architecture insights as Claude works, then loads them at the start of every session. Run `/memory` to see what has been learned. This is the row in the table above — called out separately because it may be disabled in enterprise environments. When disabled, the other externalization tools (CLAUDE.md, Skills, PROJECT_STATE.md) still work the same way; those are the tools you control directly.

---

## Pillar 4: Verify Output

**Give Claude feedback loops so it catches its own mistakes.**

Advisory instructions (CLAUDE.md rules, prompt guidance) work about 80% of the time. Deterministic verification (tests, linting, type-checking, hooks) works 100%. The single highest-leverage thing you can do is give Claude a way to verify its work.

### Verification Methods

| Method | What It Does | When to Use |
|--------|-------------|-------------|
| **Tests** | Run after every implementation step | Always — write tests first, then implement |
| **Type checking** | Catch type errors before runtime | Any typed language (Python with mypy, TypeScript) |
| **Linting** | Enforce style and catch common bugs | Every commit — configure as a pre-commit hook |
| **Build commands** | Verify the project compiles/runs | After any structural change |
| **Manual review** | Read the diff before accepting | Complex logic, security-sensitive code |

### Workshop Workflow

The build exercises in this workshop follow this pattern:

1. **Plan** — Plan Mode, review the approach
2. **Implement** — Claude writes the code
3. **Verify** — Run the tests, check the output, fix failures
4. **Iterate** — Repeat from step 2 with enhancements

Tell Claude your test command in CLAUDE.md (e.g., `python3 -m unittest discover -s tests`) and it will run tests automatically after implementation steps.

### Why This Matters

Without verification, Claude has no signal about whether its output is correct. It is working from language patterns, not executing logic. Tests and type-checks provide the ground truth that closes the loop.

**The key insight:** Don't just tell Claude what to do — give it a way to confirm it did it right.

---

*These four pillars are not sequential steps — they are habits. Practice them together and they compound.*
