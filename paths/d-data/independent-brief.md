# Independent Challenge: Guest Flow Simulator

## The Brief

Build a simulation tool that models guest arrivals at theme park attractions and analyzes operational performance. Generate synthetic data, run analysis, and produce a report — all with Python's standard library.

## Requirements

- **Generate synthetic data:** Guest arrivals at 6 attractions over 12 hours
- **Model realistic patterns:** Arrival rate varies by time of day (morning ramp-up, midday peak, evening decline)
- **Calculate per-attraction metrics:**
  - Average wait time
  - Throughput (guests per hour)
  - Utilization percentage
- **Detect bottlenecks:** Flag any attraction with utilization >85%
- **Output:** Markdown report with per-attraction stats and an hourly heatmap rendered in ASCII
- **Bonus:** Suggest optimal staffing levels based on the data

## Workflow Reminders

1. **Check context first** — if you're above 65% context usage, run `/compact` or `/clear` before starting
2. **Start in Plan Mode** — review this brief, have Claude plan the simulation approach before writing code
3. **Externalize your plan** — create a `PLAN.md` with your task breakdown before coding begins
4. **You have about 7 minutes of session time for this** — you won't finish, and that's fine. Focus on practicing the workflow (plan, build, iterate). Take it home to finish the full implementation

## Hints (if stuck)

1. **Use Plan Mode for the simulation model** — get the math right before writing any code. Ask Claude to explain the queuing theory behind wait times.
2. **Use `random.gauss()` for realistic arrival distributions.** A Poisson process is more accurate, but Gaussian is simpler and good enough for a workshop.
3. **Model each attraction with a `capacity_per_hour` attribute.** Utilization = actual arrivals / capacity. When utilization exceeds 1.0, a queue forms.
4. **Use `/effort high` for the bottleneck detection and staffing algorithm.** These are the hardest parts — give Claude room to think through the optimization.
