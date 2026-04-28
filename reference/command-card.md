# Claude Code Quick Reference Card

Printable command and shortcut reference for the Claude Code hands-on workshop.

> Need full detail and prose explanations? See [`command-reference.md`](../command-reference.md).

---

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| Shift+Tab | Cycle modes: Default → Accept Edits → Plan |
| Alt+T (Option+T on Mac) | Toggle extended thinking display |
| Shift+Enter | New line in input |
| Ctrl+B | Background a task |
| Ctrl+X then Ctrl+K | Terminate all background agents |
| Alt+P (Option+P on Mac) | Quick model switch |
| # | Add a context note (Claude incorporates into CLAUDE.md) |

---

## Slash Commands

### Context Management

| Command | What It Does |
|---------|-------------|
| `/context` | See what's loaded and context usage |
| `/compact` | Compress conversation, keep critical details |
| `/clear` | Full conversation reset |
| `/btw` | Side question — doesn't enter context |
| `/memory` | View auto-memory (when enabled) |

### Planning & Reasoning

| Command | What It Does |
|---------|-------------|
| `/plan` | Enter Plan Mode |
| `/effort low` | Simple edits, formatting, typos |
| `/effort medium` | Standard development tasks |
| `/effort high` | Complex logic, architecture decisions, hard debugging |
| `/effort auto` | Reset to default reasoning depth |

### Project Setup

| Command | What It Does |
|---------|-------------|
| `/init` | Bootstrap a CLAUDE.md |

### Utilities

| Command | What It Does |
|---------|-------------|
| `/debug` | Troubleshoot session issues |
| `/insights` | Usage analytics |
| `/copy` | Copy code blocks from last response to clipboard |
| `/simplify` | Review changed code for reuse, quality, and efficiency |
| `/batch` | Run a prompt across multiple files |
| `/powerup` | Interactive lessons on Claude Code features |
| `/release-notes` | Show what's new in this Claude Code version |

### Extensibility & Discovery *(honorable mentions)*

| Command | What It Does |
|---------|-------------|
| `/plugins` | Manage installed plugins |
| `/skills` | List skills available in the current session |
| `/agents` | Browse and manage subagents |
| `/mcp` | View MCP server status, tools, and auth |

*Not part of the walkthrough — run each one just to see what your environment exposes.*

---

## Tips & Tricks

| What | How |
|------|-----|
| Max reasoning for one turn | Type `ultrathink` in your prompt |
| Toggle Plan Mode quickly | `Shift+Tab` twice |
| Quick model switch | `Alt+P` (`Option+P` on Mac) |

---

*Tip: Print this page and keep it next to your terminal during the workshop.*
