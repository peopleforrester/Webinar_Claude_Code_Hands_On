# Decisions

## 2026-11-20 · No E2E command for the heavy gate

Issue #10 asked for an `E2E command:` line in AGENTS.md wherever the repo has
end-to-end, browser or integration tests against real services. It has none.
The tracked files are Markdown docs, JSON sample data, skill examples and the
starter `.claude/settings.json`. The only code is `tests/test_repo_content.py`,
a stdlib content-integrity suite that needs no network, service or data outside
the clone. AGENTS.md's own conventions rule out network requests and any
external runtime for testing.

Decision: AGENTS.md declares no `E2E command:` line and says why, and the heavy
gate runs the light Test command. This follows the standing rule in
peopleforrester/hecaton#103: a repo with no real-service tests gets no E2E
line, with the reason recorded here. `TestGateCommands` in
`tests/test_repo_content.py` fails if an `E2E command:` line is added without
this entry being revisited.

Revisit this if the repo gains tests that need a browser, a network service or
data outside the clone. Declare their command then, and update the test.
