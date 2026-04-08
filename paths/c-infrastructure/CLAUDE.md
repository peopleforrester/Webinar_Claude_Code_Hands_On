# Deployment Config Generator

## Build & Test
- Language: Python 3 (stdlib only)
- Run: python generate.py --app myapp --lang python --port 8080 --db postgres
- Test: python3 -m unittest discover -s tests
- Output: ./generated/ directory

## Conventions
- No external dependencies — stdlib only (no Jinja2, no Click, no PyYAML)
- Use Python string.Template or f-strings for templating
- CLI arguments via argparse
- Generated files go to ./generated/ directory (create if missing)
- Each generator is a separate function: generate_dockerfile(), generate_compose(), generate_ci()
- Validate all inputs before generating

## Supported Options
- Languages: node, python, java
- Databases: postgres, redis, none
- CI format: GitHub Actions YAML

## Dockerfile Best Practices (enforce these in generated output)
- Multi-stage builds (build + runtime stages)
- Non-root user in runtime stage
- Minimal base image (alpine or slim variants)
- .dockerignore generated alongside Dockerfile
- No secrets in build args
- HEALTHCHECK instruction included

## Don't
- Don't actually run Docker or deploy anything
- Don't install any packages
- Don't make network requests
- Don't use hardcoded absolute paths
- Don't require Docker to be installed to run this tool
