# Disney DXT — Workshop Project

## Build & Test
- Language: Depends on your chosen path — see your path's CLAUDE.md
- Run: See your path's CLAUDE.md for the correct run command
- Test: See your path's CLAUDE.md for the correct test command

## Conventions
- No external dependencies (stdlib only)
- All output goes to ./output/ directory
- Error handling: log warnings, never crash on bad input
- Include sample/mock data for testing
- Single-responsibility functions — keep them small and focused
- Use descriptive names for variables and functions

## Don't
- Don't make network requests
- Don't access files outside project directory
- Don't use hardcoded absolute paths
- Don't install packages (no pip install, no npm install)
- Don't require Docker or any external runtime to test

## Project Structure Pattern
```
your-project/
├── CLAUDE.md           ← Copy from your path's CLAUDE.md
├── main.py/index.js    ← Entry point
├── output/             ← Generated output goes here
├── tests/              ← Test files
└── .claude/
    ├── settings.json   ← Security settings
    └── skills/         ← Your custom skills
```

## CLAUDE.md Hierarchy
| Level | Location | Scope |
|-------|----------|-------|
| User | `~/.claude/CLAUDE.md` | All your projects |
| Project | `./CLAUDE.md` | Team-shared (commit this) |
| Local | `./CLAUDE.local.md` | Personal (gitignored) |

Keep CLAUDE.md under 4000 words. Every instruction competes for attention.
