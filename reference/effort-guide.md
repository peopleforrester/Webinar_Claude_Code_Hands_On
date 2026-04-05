# Effort Level Guide — When to Use Each Setting

Control how deeply Claude reasons about your request using the `/effort` command.

---

## Thinking Is On by Default

Claude Code includes extended thinking in every response. The default effort level is **medium** for Opus 4.6 and Sonnet 4.6. Use `/effort` to control reasoning depth — set `/effort high` at the start of a session when you need thorough reasoning.

The keyword `ultrathink` triggers max effort for a single turn. `/effort` is the persistent control; `ultrathink` is the per-turn override.

---

## Effort Levels

| Setting | When to Use | Examples |
|---------|-------------|---------|
| `/effort low` | Simple edits, formatting, typos | Fix a typo, reformat a list, rename a variable |
| `/effort medium` | Standard development tasks | Add a function, update a config, write a test |
| `/effort high` | Complex logic, architecture decisions, hard debugging | Refactor a module, debug a race condition, design a system, plan a migration |
| `/effort auto` | Reset to default reasoning depth | Return to default after manually setting a level |

---

## How to Choose

- **Default is medium** — this is what Claude uses unless you change it.
- **Drop to low** when the task is mechanical and you want faster responses.
- **Raise to high** for complex logic, architecture decisions, and hard debugging. Consider starting workshop sessions at high for better results.
- **Use `/effort auto`** to reset to default (medium) after manually setting a level.
- **Use `ultrathink` in your prompt** to trigger max effort for a single turn without changing the persistent level.

---

## Pro Tip: Model Switching

Sonnet 4.6 is available on Bedrock (Alt+P to switch). Use it for routine tasks — near-Opus quality, faster response times, lower token usage. Switch to Opus for architecture decisions and hard debugging.

The combination of the right model and the right effort level gives you the best balance of speed, quality, and cost.
