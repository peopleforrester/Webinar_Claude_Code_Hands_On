# Path C: Infrastructure — Deployment Config Generator

## Overview

A CLI tool (Python, stdlib only) that generates production-ready deployment configuration files from a simple project description. You provide an app name, language, and port — it outputs a Dockerfile, docker-compose.yml, and a GitHub Actions CI pipeline config.

This is a **file generator**, not a deployment tool. It does not require Docker to be installed. It writes config files to disk — that's it.

**Best for:** DevOps engineers, SREs, platform engineers, backend developers who write their own deployment configs.

**Prerequisites:** Python 3.x installed, plus Claude Code CLI.

---

## What's in This Directory

| File | Purpose |
|------|---------|
| [guided-brief.md](guided-brief.md) | Step-by-step guided build (28 min, instructor-led) |
| [independent-brief.md](independent-brief.md) | Self-directed challenge: Service Health Dashboard Config Generator |
| [CLAUDE.md](CLAUDE.md) | Path-specific project conventions — copy into your build directory |

> **Note:** This path has no sample data directory — input comes from CLI arguments (`--app`, `--lang`, `--port`, `--db`), not from a data file.

## Quick Start

1. Read the [guided-brief.md](guided-brief.md) and follow along with the instructor
2. When done, try the [independent-brief.md](independent-brief.md) challenge on your own
3. See [`skills-examples/docker-review/SKILL.md`](../../skills-examples/docker-review/SKILL.md) for an example skill for this path
