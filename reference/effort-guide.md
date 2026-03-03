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
| `/effort high` | Complex logic, multi-file changes | Refactor a module, debug a tricky issue, add a feature touching multiple files |
| `/effort max` | Architecture decisions, hard debugging | Design a system, debug a race condition, plan a migration |

---

## How to Choose

- **Start with medium** — it covers most development work.
- **Drop to low** when the task is mechanical and you want faster responses.
- **Raise to high** when you notice Claude missing details or making mistakes.
- **Use max sparingly** — it produces the deepest reasoning but takes the longest and uses the most tokens.

---

## Pro Tip: Model Switching

If Sonnet 4.6 is available (Alt+P to check), use it for routine tasks — near-Opus quality, faster response times, lower token usage. Switch to Opus for architecture decisions and hard debugging.

The combination of the right model and the right effort level gives you the best balance of speed, quality, and cost.
