# studious-doodle

A tiny beginner-friendly Python project scaffold.

## What this gives you

- A simple Python package (`app/`) with one function.
- A test suite (`tests/`) using `pytest`.
- A `Makefile` with common commands.
- Basic linting/formatting setup (`ruff`).

## Quick start

1. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -e .[dev]
   ```

3. Run checks:

   ```bash
   make test
   make lint
   make format
   ```

## Project layout

```text
.
├── app/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_main.py
├── docs/
│   └── ONBOARDING.md
├── Makefile
├── pyproject.toml
└── README.md
```

## Next learning steps

- Add a second function in `app/main.py` and write tests first.
- Learn basic Git workflow: branch, commit, push, pull request.
- Add GitHub Actions CI once you're comfortable with local tooling.
