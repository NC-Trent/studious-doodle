# Studious Doodle

Practice flashcards from your terminal. Each card has a question and an answer. The deck lives on your computer and remembers when each card is due.

## First session

From the checkout, run these commands with Python 3.10 or newer.

```sh
python -m app add "Which git command shows unstaged changes?" "git diff"
python -m app review
python -m app status
```

Recall the answer, press Enter to reveal it, then type a rating.

| Key | Effect |
| --- | --- |
| a | Practice the card again the next time you start a review. |
| g | Schedule the card in 1, 2, 4, 8, 16, then 30 days on consecutive successes. |
| q | End the session with the current card still due. Earlier ratings are saved. |

A missed card restarts at the one-day interval on its next success. Review shows each due card once per session. Dates follow your local calendar.

## Keep separate decks

Cards are stored in `~/.studious-doodle.db`. Select another SQLite file with the global `--db` option. Use the same path each time you open that deck.

```sh
python -m app --db spanish.db add "Good morning" "Buenos días"
python -m app --db spanish.db review
```

To use the shorter `study` command from any directory, install the project in an active virtual environment with `python -m pip install -e .`. For development, see the [newcomer guide](docs/ONBOARDING.md).
