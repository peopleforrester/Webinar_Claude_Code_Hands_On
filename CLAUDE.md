# Disney DXT Workshop

Workshop project for Disney DXT team demonstrating Claude Code capabilities.

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

## CLAUDE.md Hierarchy (Teaching Reference)

| Level | Location | Scope |
|-------|----------|-------|
| User | `~/.claude/CLAUDE.md` | All your projects |
| Project | `./CLAUDE.md` | Team-shared (commit this) |
| Local | `./CLAUDE.local.md` | Personal (gitignored) |

Keep CLAUDE.md under 4000 words. Every instruction competes for attention.
