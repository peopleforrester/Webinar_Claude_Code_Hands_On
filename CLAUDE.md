# Claude Code Hands-On Workshop

Workshop project demonstrating Claude Code capabilities in a restricted enterprise environment.

**Stack**: Depends on participant's chosen path (Python or JavaScript, stdlib only)

## Conventions

- No external dependencies (stdlib only)
- All output goes to `./output/` directory
- No network requests, no files outside project directory, no hardcoded absolute paths
- No package installs (no pip, no npm)
- No Docker or external runtime required to test
- Error handling: log warnings, never crash on bad input

## Project Structure

```
your-project/
├── CLAUDE.md
├── main.py/index.js    ← Entry point
├── output/             ← Generated output
├── tests/
└── .claude/
    ├── settings.json
    └── skills/
```

> Layout shown is illustrative for code-producing paths (A–D). Path E is a zero-code prep kit and diverges — see `paths/e-business/README.md` for its structure.

## CLAUDE.md Hierarchy (Teaching Reference)

| Level | Location | Scope |
|-------|----------|-------|
| Managed policy | `/etc/claude-code/CLAUDE.md` (Linux) | Organization-wide, cannot be overridden |
| User | `~/.claude/CLAUDE.md` | All your projects |
| Project | `./CLAUDE.md` | Team-shared (commit this) |
| Local | `./CLAUDE.local.md` | Personal (gitignored) |

Keep each CLAUDE.md under 200 lines. Every instruction competes for attention.
