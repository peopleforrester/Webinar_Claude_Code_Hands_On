# Build with Claude Code: No Pitches, Just Practice

**Disney DXT AI Day — Workshop Companion Repo**

A hands-on workshop focused entirely on Claude Code CLI in a restricted enterprise environment. Attendees learn the three pillars of effectiveness (context management, planning discipline, externalizing decisions), then apply them immediately through a choose-your-own-adventure build exercise.

---

## Environment Prerequisites

| Requirement | Details |
|-------------|---------|
| **Claude Code CLI** | Version 2.1.x or later |
| **Backend** | Amazon Bedrock (configured by your IT team) |
| **Model** | Opus 4.6 via Bedrock |
| **Network** | No internet required — all exercises are self-contained |
| **Dependencies** | None — stdlib only, no package installs |

Verify your setup:
```bash
claude --version    # Should show 2.1.x
claude /status      # Verify backend connection
claude /model       # See available models
```

---

## How to Use This Repo

### 1. Clone the repo
```bash
git clone <repo-url>
cd Disney_Claude_Code_Course
```

### 2. Read the root CLAUDE.md
The `CLAUDE.md` at repo root contains workshop-wide conventions. Skim it before starting.

### 3. Choose your adventure path
Pick the path that matches your role:

| If you are... | Pick Path... | Directory |
|---------------|-------------|-----------|
| A frontend/UI developer | **A: Frontend** — Guest Feedback Dashboard | `paths/a-frontend/` |
| A backend/API developer | **B: Backend** — Reservation Validation API | `paths/b-backend/` |
| DevOps / SRE / platform | **C: Infrastructure** — Deployment Config Generator | `paths/c-infrastructure/` |
| Data engineer / analyst | **D: Data/Analysis** — Operations Log Analyzer | `paths/d-data/` |

### 4. Follow the guided build
Each path has its own `guided-brief.md` with step-by-step build instructions. Open your path's `README.md` for an overview, then follow `guided-brief.md` along with the instructor.

### 5. Try the independent challenge
After the guided build, each path has an `independent-brief.md` with a standalone challenge you can start in session and take home to finish.

---

## Repo Structure

```
Disney_Claude_Code_Course/
├── README.md                     ← You are here
├── CLAUDE.md                     ← Workshop-wide conventions (loaded by Claude Code)
├── command-reference.md          ← Printable cheat sheet of all commands & shortcuts
├── .claude/
│   └── settings.json             ← Starter security settings
├── paths/
│   ├── a-frontend/               ← Path A: Guest Feedback Dashboard
│   │   ├── README.md             ← Path overview & quick start
│   │   ├── guided-brief.md       ← Step-by-step guided build (20 min)
│   │   ├── CLAUDE.md             ← Path-specific project CLAUDE.md
│   │   ├── independent-brief.md  ← Park Wait Times challenge
│   │   └── sample-data/
│   │       └── guest-feedback.json
│   ├── b-backend/                ← Path B: Reservation Validation API
│   │   ├── README.md             ← Path overview & quick start
│   │   ├── guided-brief.md       ← Step-by-step guided build (20 min)
│   │   ├── CLAUDE.md             ← Path-specific project CLAUDE.md
│   │   └── independent-brief.md  ← Dining Preferences challenge
│   ├── c-infrastructure/         ← Path C: Deployment Config Generator
│   │   ├── README.md             ← Path overview & quick start
│   │   ├── guided-brief.md       ← Step-by-step guided build (20 min)
│   │   ├── CLAUDE.md             ← Path-specific project CLAUDE.md
│   │   └── independent-brief.md  ← Health Dashboard Configs challenge
│   └── d-data/                   ← Path D: Operations Log Analyzer
│       ├── README.md             ← Path overview & quick start
│       ├── guided-brief.md       ← Step-by-step guided build (20 min)
│       ├── CLAUDE.md             ← Path-specific project CLAUDE.md
│       ├── independent-brief.md  ← Guest Flow Simulator challenge
│       └── sample-data/
│           └── operations-logs.json
├── reference/                    ← Quick reference handouts
│   ├── command-card.md           ← Compact command & shortcut card
│   ├── three-pillars.md          ← The three pillars of effectiveness
│   └── effort-guide.md           ← /effort level selection guide
├── slides/                       ← Instructor slide deck (added before workshop)
│   └── README.md
└── skills-examples/              ← Example Skills to copy into your project
    ├── explain-code/SKILL.md     ← General purpose: code explanation
    ├── ui-component/SKILL.md     ← Path A: UI component conventions
    ├── api-scaffold/SKILL.md     ← Path B: API scaffold conventions
    ├── docker-review/SKILL.md    ← Path C: Dockerfile review checklist
    └── data-report/SKILL.md      ← Path D: Data report conventions
```

---

## The Three Pillars

Everything in this workshop is built around three effectiveness pillars:

| Pillar | What It Means | Why It Matters |
|--------|---------------|----------------|
| **Manage Context** | Compact at 65-70%, not 90%. One feature per session. | LLM performance degrades as context fills — "context rot" is real |
| **Plan Before Code** | Plan Mode (`Shift+Tab` to cycle modes, or `/plan`) before implementation | Forces architecture thinking, catches dependency issues early |
| **Externalize Decisions** | CLAUDE.md, Skills, files — not just conversation | Files persist across sessions; teams share standards automatically |

---

## Using Skills Examples

The `skills-examples/` directory contains example Skills you can copy into your project during the workshop:

```bash
# From your project directory:
mkdir -p .claude/skills/
cp /path/to/this/repo/skills-examples/explain-code/SKILL.md .claude/skills/explain-code/SKILL.md
```

Skills hot-reload — edit the file and changes apply immediately, no restart needed.

---

## Key Files to Commit to Your Own Repos After the Workshop

- `CLAUDE.md` — Project standards (team-shared)
- `.claude/settings.json` — Permissions and security
- `.claude/skills/` — Shared reusable skills

---

## Quick Reference

See `command-reference.md` for the full printable cheat sheet, or run `claude /help` inside a session.
