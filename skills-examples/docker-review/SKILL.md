---
name: docker-review
description: Reviews Dockerfiles and container configs for security and best practices. Use when reviewing or creating Docker configurations.
---
When reviewing a Dockerfile, check each of these areas:

## Multi-Stage Builds
- Separate build stage from runtime stage
- Build stage installs dev dependencies and compiles; runtime stage copies only artifacts
- Final image should not contain build tools, source code, or dev dependencies

## Non-Root User
- Runtime stage must create and switch to a non-root user
- Use USER directive after installing packages but before COPY/CMD
- Verify file permissions allow the non-root user to run the application

## Minimal Base Image
- Use alpine or slim variants (e.g., python:3.12-slim, node:20-alpine)
- Avoid latest tag — pin to a specific version
- Justify any use of full-size base images

## .dockerignore
- A .dockerignore file must exist alongside the Dockerfile
- Must exclude: .git, node_modules, __pycache__, .env, *.md, tests/
- Verify no secrets or large unnecessary files would be included in the build context

## No Secrets in Build
- No secrets in ENV, ARG, or COPY instructions
- No .env files copied into the image
- No API keys, passwords, or tokens in the Dockerfile

## Health Checks
- HEALTHCHECK instruction must be present
- Use curl or a lightweight check against the application's health endpoint
- Set appropriate interval, timeout, and retries
