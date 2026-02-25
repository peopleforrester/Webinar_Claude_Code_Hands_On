# Path C: Infrastructure — Deployment Config Generator

## What You'll Build

A CLI tool (Python, stdlib only) that generates production-ready deployment configuration files from a simple project description. You provide an app name, language, and port — it outputs a Dockerfile, docker-compose.yml, and a GitHub Actions CI pipeline config.

This is a **file generator**, not a deployment tool. It does not require Docker to be installed. It does not run containers or make network requests. It writes config files to disk — that's it.

## Best For

- DevOps engineers
- SREs and platform engineers
- Backend developers who write their own deployment configs
- Anyone who wants to automate boilerplate infrastructure files

## Prerequisites

- Python 3.x installed
- Claude Code CLI installed and authenticated

---

## Guided Build (20 minutes)

### Step 1: Set Up (2 min)

Create your project and initialize Claude Code:

```bash
mkdir config-generator && cd config-generator
claude /init
```

Add context by pressing `#` in Claude Code and entering these details:

- This is a CLI tool that generates deployment configs
- It outputs files — it does NOT run Docker or deploy anything
- Support: Dockerfile, docker-compose.yml, and a basic CI pipeline config
- Use Python with no external dependencies (stdlib only)

This gives Claude the constraints it needs to stay on track.

### Step 2: Plan First (3 min)

Enter Plan Mode by pressing **Shift+Tab twice**. Then describe what you want to build:

> Build a config generator CLI that:
>
> - Accepts inputs: app name, language (node/python/java), port, needs database (y/n)
> - Generates a Dockerfile following best practices (multi-stage build, non-root user, .dockerignore)
> - Generates a docker-compose.yml (app service + optional postgres/redis)
> - Generates a basic CI pipeline config (GitHub Actions format)
> - Outputs all files to a `./generated/` directory
>
> Plan the CLI interface, template structure, and output format. Don't write any code yet.

Review Claude's plan. Does it cover input validation? Does it separate each generator into its own function? Adjust before moving on.

### Step 3: Build (10 min)

Exit Plan Mode (Shift+Tab). Tell Claude to implement the plan.

Key points to watch for during the build:

- **Templating**: Python `string.Template` or f-strings — no Jinja2
- **CLI**: `argparse` for argument parsing — no Click or Typer
- **Structure**: Each generator should be a separate function (`generate_dockerfile()`, `generate_compose()`, `generate_ci()`)
- **Tests**: After each generator is built, ask Claude to write a test that verifies the output contains expected sections

Example test prompt after the Dockerfile generator is done:

> Write a test that verifies generate_dockerfile() output includes a multi-stage build, non-root USER instruction, and HEALTHCHECK.

Run tests after each generator:

```bash
python -m pytest tests/ -v
```

### Step 4: Iterate (3 min)

Ask Claude to add these features:

- A `--dry-run` flag that prints configs to stdout instead of writing files
- A `--security-scan` step added to the CI pipeline config
- A generated `README.md` that explains how to use the output configs

Example prompt:

> Add a --dry-run flag that prints all generated configs to stdout instead of writing to disk. Also add a security scanning step to the GitHub Actions pipeline. Then generate a README.md alongside the configs that documents usage.

### Step 5: Create a Skill (2 min)

Create a reusable Claude Code skill that reviews Dockerfiles for best practices:

> Create a skill at `.claude/skills/docker-review/SKILL.md` that reviews Dockerfiles for:
> - Multi-stage builds
> - Non-root user
> - Minimal base image (alpine or slim)
> - .dockerignore present
> - No secrets in build args
> - Health checks defined

Once created, you can invoke it from any project with `/docker-review`.

---

## What's Next

- **Independent challenge**: See [`independent-brief.md`](independent-brief.md) for a Service Health Dashboard Config Generator you can build on your own.
- **Skill reference**: See [`skills-examples/docker-review/SKILL.md`](../../skills-examples/docker-review/SKILL.md) for a complete example of the Dockerfile review skill.
