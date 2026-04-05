# The Three Pillars of Effectiveness

A concise reference for the workshop's three pillars framework.

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
| Current task state | `PLAN.md` | Survives `/clear` and context resets |
| Decisions made | `DECISIONS.md` or commit messages | Permanent record |
| Claude's learnings | `~/.claude/projects/<project>/memory/` | Auto-saved, loaded next session (when enabled) |
| Org-wide policy | `/etc/claude-code/CLAUDE.md` | Managed, cannot be overridden |

### A Note on Auto-Memory

When enabled, Claude Code automatically writes notes to itself as it works — build commands, debugging patterns, architecture insights. These are saved to `~/.claude/projects/<project>/memory/MEMORY.md` and loaded at the start of every session. Run `/memory` to see what Claude has learned.

**Note:** Auto-memory may be disabled in some enterprise environments. Even when disabled, the other externalization tools (CLAUDE.md, Skills, PLAN.md) work the same way — those are the tools you control directly.

---

*These three pillars are not sequential steps — they are habits. Practice them together and they compound.*
