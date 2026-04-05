# Effort Level Guide — When to Use Each Setting

Control how deeply Claude reasons about your request using the `/effort` command.

---

## Thinking Is On by Default

Claude Code includes extended thinking in every response. The old keywords (`think`, `think hard`, `ultrathink`) are deprecated and non-functional. Use `/effort` to control reasoning depth instead.

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

- **Start with medium** — it covers most development work.
- **Drop to low** when the task is mechanical and you want faster responses.
- **Raise to high** when you notice Claude missing details or making mistakes, or for architecture and hard debugging.
- **Use `/effort auto`** to reset to default behavior after manually setting a level.

---

## Pro Tip: Model Switching

Sonnet 4.6 is available on Bedrock (Alt+P to switch). Use it for routine tasks — near-Opus quality, faster response times, lower token usage. Switch to Opus for architecture decisions and hard debugging.

The combination of the right model and the right effort level gives you the best balance of speed, quality, and cost.
