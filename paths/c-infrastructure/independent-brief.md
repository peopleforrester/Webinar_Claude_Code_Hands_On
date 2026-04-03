# Independent Challenge: Service Health Dashboard Config Generator

## The Brief

Build a CLI tool that generates monitoring and observability configuration files for a set of services. You provide a list of services with their ports and health check endpoints — it outputs a complete monitoring stack config (all static files, no running infrastructure required).

## Requirements

### Inputs
- A list of service names (e.g., `api-gateway`, `user-service`, `order-service`)
- Port for each service
- Health check endpoint for each service (e.g., `/healthz`, `/status`)

### Generated Outputs

**1. Monitoring config (Prometheus-style YAML)**
- Scrape targets for each service
- Appropriate scrape intervals
- Labels for service name and environment

**2. Alerting rules file**
- High latency alert (response time > threshold)
- Service down alert (target unreachable)
- Error rate alert (5xx responses above threshold)
- Configurable thresholds with sensible defaults

**3. Grafana dashboard JSON**
- One dashboard with panels for all services
- Panels: uptime, latency (p50/p95/p99), error rate, request rate
- Variables for environment and service filtering

### Constraints
- All output is static files — no running Prometheus, Grafana, or any infrastructure
- Python 3, stdlib only (no PyYAML, no external libraries)
- Include a validation step that checks generated configs for syntax errors
- Output to a `./monitoring-configs/` directory

---

## Workflow Reminders

1. **Check context first** — if above 65%, `/compact` or `/clear`
2. **Start in Plan Mode** — review this brief, have Claude plan the approach
3. **Externalize** — create a `PLAN.md` with your task breakdown before coding
4. **You have about 7 minutes of session time for this** — you won't finish, and that's fine. Practice the workflow, take it home to finish

---

## Hints (if stuck)

1. **Plan the schema first.** Define the YAML and JSON structure before writing any generator code. Knowing the output format makes the generation logic straightforward.

2. **Generate YAML as formatted strings.** Use `json.dumps(indent=2)` for Grafana JSON. For Prometheus YAML, write formatted strings directly — no PyYAML library needed. YAML is a superset of JSON, but hand-crafted string output gives you more control over readability.

3. **Grafana dashboard JSON is well-documented.** Ask Claude to generate a dashboard template — it knows the panel schema. Start with a single `stat` panel and a `timeseries` panel, then expand.

4. **Use `/effort high` for the alerting rules logic.** The PromQL expressions for latency percentiles and error rates benefit from Claude thinking more carefully about the math.
