"""Content-integrity tests for the workshop repo (stdlib only).

The repo ships docs, sample data, skill examples and starter settings rather
than application code, so these tests check that what attendees copy and rely
on stays well-formed and consistent with the briefs.

Run: python3 -m unittest discover -s tests
"""

import datetime
import json
import os
import re
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Local-only paths from .gitignore that may exist on a maintainer's machine.
SKIP_DIRS = {
    ".git", ".claude", "docs", "transcripts", "claude-ai-context", ".claude-history",
    "node_modules", "output", "__pycache__",
}
SKIP_FILES = {"ACTION_ITEMS.md", "CLAUDE.local.md"}

PATHS = ["a-frontend", "b-backend", "c-infrastructure", "d-data", "e-business"]
PARKS = {"Coral Kingdom", "Skyward Summit", "Harbor Gardens", "Meadow Haven"}

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


def repo_files(suffix):
    found = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            if name.endswith(suffix) and name not in SKIP_FILES:
                found.append(os.path.join(dirpath, name))
    return sorted(found)


def load_json(*parts):
    with open(os.path.join(ROOT, *parts), encoding="utf-8") as f:
        return json.load(f)


def rel(path):
    return os.path.relpath(path, ROOT)


class TestJson(unittest.TestCase):
    def test_all_json_files_parse(self):
        files = repo_files(".json")
        self.assertTrue(files)
        for path in files:
            with self.subTest(file=rel(path)):
                with open(path, encoding="utf-8") as f:
                    json.load(f)


class TestStarterSettings(unittest.TestCase):
    def test_deny_rules_enforce_conventions(self):
        settings = load_json(".claude", "settings.json")
        deny = settings["permissions"]["deny"]
        self.assertIsInstance(deny, list)
        for rule in deny:
            self.assertIsInstance(rule, str)
        # CLAUDE.md conventions: no network requests, no package installs.
        for rule in ["Bash(curl *)", "Bash(wget *)", "Bash(pip *)",
                     "Bash(pip3 *)", "Bash(npm *)"]:
            self.assertIn(rule, deny)


class TestMarkdown(unittest.TestCase):
    def test_relative_links_resolve(self):
        broken = []
        for path in repo_files(".md"):
            with open(path, encoding="utf-8") as f:
                text = f.read()
            for target in LINK_RE.findall(text):
                if re.match(r"^[a-z]+:", target) or target.startswith("#"):
                    continue
                target = target.split("#", 1)[0]
                resolved = os.path.normpath(
                    os.path.join(os.path.dirname(path), target))
                if not os.path.exists(resolved):
                    broken.append(f"{rel(path)} -> {target}")
        self.assertEqual(broken, [])

    def test_claude_md_files_stay_under_200_lines(self):
        files = [p for p in repo_files(".md")
                 if os.path.basename(p) in ("CLAUDE.md", "AGENTS.md")]
        self.assertTrue(files)
        for path in files:
            with self.subTest(file=rel(path)):
                with open(path, encoding="utf-8") as f:
                    self.assertLess(len(f.readlines()), 200)

    def test_root_claude_md_points_at_agents_md(self):
        claude = os.path.join(ROOT, "CLAUDE.md")
        agents = os.path.join(ROOT, "AGENTS.md")
        self.assertTrue(os.path.isfile(agents))
        self.assertTrue(os.path.samefile(claude, agents))


class TestPaths(unittest.TestCase):
    def test_each_path_has_its_core_docs(self):
        for name in PATHS:
            for doc in ["README.md", "CLAUDE.md", "guided-brief.md",
                        "independent-brief.md"]:
                with self.subTest(path=name, doc=doc):
                    self.assertTrue(os.path.isfile(
                        os.path.join(ROOT, "paths", name, doc)))


class TestSkillExamples(unittest.TestCase):
    def test_skills_have_frontmatter_matching_directory(self):
        base = os.path.join(ROOT, "skills-examples")
        skills = sorted(os.listdir(base))
        self.assertTrue(skills)
        for skill in skills:
            with self.subTest(skill=skill):
                with open(os.path.join(base, skill, "SKILL.md"),
                          encoding="utf-8") as f:
                    text = f.read()
                match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
                self.assertIsNotNone(match, "missing frontmatter")
                fields = dict(
                    line.split(":", 1) for line in match.group(1).splitlines()
                    if ":" in line)
                fields = {k.strip(): v.strip() for k, v in fields.items()}
                self.assertEqual(fields.get("name"), skill)
                self.assertTrue(fields.get("description"))
                self.assertTrue(text[match.end():].strip(), "empty body")


class TestGuestFeedbackSample(unittest.TestCase):
    def setUp(self):
        self.entries = load_json(
            "paths", "a-frontend", "sample-data", "guest-feedback.json")

    def test_has_at_least_15_entries_with_unique_ids(self):
        # guided-brief.md asks for at least 15 entries.
        self.assertGreaterEqual(len(self.entries), 15)
        ids = [e["id"] for e in self.entries]
        self.assertEqual(len(ids), len(set(ids)))

    def test_entries_match_dashboard_model(self):
        categories = {"Attractions", "Dining", "Service", "Facilities"}
        sentiments = {"positive", "neutral", "negative"}
        for e in self.entries:
            with self.subTest(id=e.get("id")):
                self.assertIn(e["category"], categories)
                self.assertIn(e["sentiment"], sentiments)
                self.assertIn(e["rating"], range(1, 6))
                self.assertTrue(e["comment"].strip())
                datetime.date.fromisoformat(e["date"])
        self.assertEqual({e["category"] for e in self.entries}, categories)
        self.assertEqual({e["sentiment"] for e in self.entries}, sentiments)


class TestReservationSample(unittest.TestCase):
    def setUp(self):
        self.requests = load_json(
            "paths", "b-backend", "sample-data", "sample-reservations.json")

    def test_has_valid_and_invalid_examples(self):
        notes = [r["_note"] for r in self.requests]
        for note in notes:
            self.assertRegex(note, r"^(Valid|INVALID)\b")
        self.assertTrue(any(n.startswith("Valid") for n in notes))
        self.assertTrue(any(n.startswith("INVALID") for n in notes))

    def test_examples_agree_with_date_independent_rules(self):
        # Date rules are relative to "today", so only park and party size
        # are checked here.
        for r in self.requests:
            with self.subTest(note=r["_note"], guest=r["guestEmail"]):
                self.assertIn("@", r["guestEmail"])
                datetime.date.fromisoformat(r["date"])
                park_ok = r["park"] in PARKS
                size_ok = 1 <= r["partySize"] <= 20
                note = r["_note"]
                if note.startswith("Valid"):
                    self.assertTrue(park_ok and size_ok)
                elif "party size" in note:
                    self.assertFalse(size_ok)
                elif "park" in note:
                    self.assertFalse(park_ok)


class TestOperationsLogSample(unittest.TestCase):
    def test_entries_match_log_format(self):
        logs = load_json(
            "paths", "d-data", "sample-data", "operations-logs.json")
        self.assertGreaterEqual(len(logs), 10)
        for e in logs:
            with self.subTest(entry=e):
                self.assertEqual(set(e), {"timestamp", "operation",
                                          "duration_ms", "status", "location"})
                datetime.datetime.fromisoformat(
                    e["timestamp"].replace("Z", "+00:00"))
                self.assertIsInstance(e["duration_ms"], int)
                self.assertGreaterEqual(e["duration_ms"], 0)
                self.assertIn(e["status"], {"success", "error", "timeout"})
                self.assertIn(e["location"], PARKS)


if __name__ == "__main__":
    unittest.main()
