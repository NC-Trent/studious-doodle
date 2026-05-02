# Newcomer Guide

## What this repository currently is

This repository is currently a **very minimal starter** rather than a complete application.

- `README.md` contains a one-line description.
- `Ramcat` currently contains only `{{`, which looks like a placeholder or unfinished artifact.

## Current structure

```text
.
├── README.md
├── Ramcat
└── docs/
    └── ONBOARDING.md
```

## Important things to know first

1. There is no runnable app entrypoint yet.
2. There are no tests, build scripts, or dependency manifests (`package.json`, `pyproject.toml`, etc.) yet.
3. Before adding features, define the stack and project goals so contributors can align on structure.

## Suggested immediate cleanup

- Clarify what `Ramcat` is meant to be (source file? template? notes?).
- Expand `README.md` with:
  - Purpose and scope
  - Setup instructions
  - Development workflow
  - Contribution guidelines
- Add a license and basic repository standards.

## What to learn / decide next

### 1) Product and scope
- What problem does the project solve?
- Who is it for?
- What is the minimal first release?

### 2) Tech stack
Pick one clear stack and commit to conventions:
- Backend (if needed): Python, Node.js, Go, etc.
- Frontend (if needed): React, Vue, plain HTML/CSS/JS.
- Tooling: formatter, linter, test framework.

### 3) Basic engineering scaffolding
After stack selection, add:
- Dependency manifest
- Linting and formatting config
- Test runner and first smoke test
- CI workflow (e.g., GitHub Actions)

### 4) Documentation baseline
Create:
- `docs/ARCHITECTURE.md` for system design and decisions
- `docs/CONTRIBUTING.md` for workflow and coding standards
- `docs/ROADMAP.md` for milestones and priorities

## First practical milestone (recommended)
A useful first milestone is to make the repo "executable" with one command:
- `make test` or equivalent succeeds
- CI runs lint + tests on pull requests
- README setup instructions are reproducible from a fresh environment
