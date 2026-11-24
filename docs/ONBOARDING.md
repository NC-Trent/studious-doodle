# Development

Create a virtual environment from the repository root, then install the development tools.

```sh
python -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
make test
make lint
```

Both `study` and `python -m app` run the CLI in `app/__main__.py`. To experiment with a separate deck, pass `--db` before the subcommand. The database file is created on first use in an existing directory. The review tests use temporary decks.
