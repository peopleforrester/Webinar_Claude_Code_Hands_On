# Claude Code — Command Reference Card

A printable cheat sheet for the Disney DXT AI Day workshop.

---

## Starting a Session

| Action | Command |
|--------|---------|
| Start Claude Code | `claude` (in any project directory) |
| Check version | `claude --version` |
| Check backend status | `claude /status` |
| See available models | `claude /model` |
| Get help | `claude /help` |

---

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Shift+Tab` x2 | Toggle Plan Mode |
| `Tab` | Toggle thinking display |
| `Shift+Enter` | New line in input |
| `Ctrl+B` | Background a task |
| `Ctrl+F` | Terminate all background agents |
| `Alt+P` (or `Option+P` on Mac) | Quick model switch |
| `#` | Add a context note (Claude incorporates into CLAUDE.md) |

---

## Slash Commands

### Context Management
| Command | Purpose |
|---------|---------|
| `/context` | See what's loaded and context usage |
| `/compact` | Compress conversation, keep critical details |
| `/clear` | Full conversation reset |

### Planning & Reasoning
| Command | Purpose |
|---------|---------|
| `/plan` | Enter Plan Mode (read everything, modify nothing) |
| `/effort low` | Simple edits, formatting, typos |
| `/effort medium` | Standard development tasks |
| `/effort high` | Complex logic, multi-file changes |
| `/effort max` | Architecture decisions, hard debugging |

### Memory & Output
| Command | Purpose |
|---------|---------|
| `/memory` | View auto-memory (when enabled — may be disabled in enterprise environments) |
| `/copy` | Copy code blocks from last response to clipboard |

### Project Setup
| Command | Purpose |
|---------|---------|
| `/init` | Bootstrap a CLAUDE.md for the current project |

### Code Quality
| Command | Purpose |
|---------|---------|
| `/simplify` | Review changed code for reuse, quality, and efficiency |
| `/batch` | Run a prompt across multiple files |

### Diagnostics
| Command | Purpose |
|---------|---------|
| `/debug` | Troubleshoot session issues |
| `/insights` | Usage analytics (run monthly) |

---

## Context Management Rules of Thumb

| Context Level | What To Do |
|---------------|------------|
| 0-65% | Work normally |
| 65-70% | Compact or start fresh |
| 70-80% | `/compact` NOW — quality is already degrading |
| 80%+ | You've waited too long |

**Rule:** One feature per session. If Claude starts giving worse answers, it's likely context rot, not the model.

---

## Auto-Memory

When enabled, Claude Code automatically remembers learnings across sessions. It stores these in `~/.claude/projects/<project>/memory/MEMORY.md`.

| Action | How |
|--------|-----|
| View what Claude remembers | `/memory` |
| Add a memory manually | Tell Claude: "Remember that we use snake_case" |
| Remove a memory | `/memory`, then ask Claude to remove the entry |

Auto-memory is part of Pillar 3 (Externalize Decisions) — Claude learns your project conventions over time without you repeating them.

**Note:** Auto-memory may be disabled in some enterprise environments. Run `/memory` to check whether it's active in your setup. Even when disabled, CLAUDE.md and Skills provide the same externalization benefits — you control those directly.

---

## CLAUDE.md Hierarchy

| Level | Location | Scope |
|-------|----------|-------|
| User | `~/.claude/CLAUDE.md` | All your projects |
| Project | `./CLAUDE.md` | Team-shared (commit this) |
| Local | `./CLAUDE.local.md` | Personal (gitignored) |

---

## Skills

Skills are reusable workflow definitions stored in `.claude/skills/*/SKILL.md`.

```bash
# Create a skill directory
mkdir -p .claude/skills/my-skill

# Create the skill file
# (use Claude Code to help write it!)
```

A skill file uses YAML frontmatter to declare its name and description:

```markdown
---
name: my-skill
description: What this skill does (shown in /help output)
---

Your skill instructions here...
```

Skills hot-reload — edit the file and changes apply immediately, no restart needed.

---

## Plan Mode Workflow

```
1. Enter Plan Mode (Shift+Tab x2 or /plan)
2. Ask Claude to analyze the project and plan the approach
3. Review the plan — ask questions, request changes
4. Exit Plan Mode (Shift+Tab x2)
5. Tell Claude to implement the approved plan
```

In Plan Mode, Claude can **read everything** but **modify nothing**. It becomes a strategic advisor.

---

## Effort Levels

> For detailed guidance on choosing effort levels, see [reference/effort-guide.md](reference/effort-guide.md).

| Setting | When to Use |
|---------|-------------|
| `/effort low` | Simple edits, formatting, typos |
| `/effort medium` | Standard development tasks |
| `/effort high` | Complex logic, multi-file changes |
| `/effort max` | Architecture decisions, debugging hard problems |

Thinking is on by default with max budget. Use `/effort` to control reasoning depth.

**Pro tip:** Sonnet 4.6 is available on Bedrock (`Alt+P` to switch). Use it for routine tasks — near-Opus quality, faster response times, and lower token usage. Switch to Opus for architecture decisions and hard debugging.

---

## Files to Commit to Your Repos

- `CLAUDE.md` — Project standards
- `.claude/settings.json` — Permissions and security
- `.claude/skills/` — Shared skills

---

## Common Workflow Pattern

```
1. /plan          → Think before coding
2. /effort high   → Set appropriate reasoning depth
3. Build          → Let Claude implement
4. /context       → Check context health
5. /compact       → Compress if needed
6. Iterate        → Refine and improve
```
