"""Command-line study sessions backed by a local SQLite deck."""

import argparse
import sqlite3
import sys
from contextlib import closing
from datetime import date, timedelta
from pathlib import Path


def card_text(value: str) -> str:
    if not value.strip():
        raise argparse.ArgumentTypeError("card text cannot be blank")
    return value.strip()


def review(db: sqlite3.Connection, today: date) -> None:
    cards = db.execute(
        "SELECT id, question, answer, streak FROM cards WHERE due <= ? ORDER BY due, id",
        (today.isoformat(),),
    ).fetchall()
    if not cards:
        print("No cards due. Add a card with 'study add' or check 'study status'.")
        return

    reviewed = 0
    for card_id, question, answer, streak in cards:
        print(f"\n{question}")
        try:
            input("Press Enter to reveal the answer. ")
            print(answer)
            while True:
                rating = input("[a]gain, [g]ot it, or [q]uit? ").strip().lower()
                if rating in {"a", "g", "q"}:
                    break
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if rating == "q":
            break
        streak = min(streak + 1, 6) if rating == "g" else 0
        days = min(2 ** (streak - 1), 30) if streak else 0
        due = (today + timedelta(days=days)).isoformat()
        with db:
            db.execute("UPDATE cards SET streak=?, due=? WHERE id=?", (streak, due, card_id))
        reviewed += 1
    print(f"Reviewed {reviewed} of {len(cards)} due cards.")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="study", description="Practice your local flashcards.")
    parser.add_argument("--db", type=Path, help="deck database (default: ~/.studious-doodle.db)")
    commands = parser.add_subparsers(dest="command", required=True)
    add = commands.add_parser("add", help="add a question and its answer")
    add.add_argument("question", type=card_text)
    add.add_argument("answer", type=card_text)
    commands.add_parser("review", help="practice cards due today")
    commands.add_parser("status", help="show deck size and review schedule")
    args = parser.parse_args(argv)
    today = date.today()
    path = args.db or Path.home() / ".studious-doodle.db"
    try:
        with closing(sqlite3.connect(path)) as db:
            db.execute(
                "CREATE TABLE IF NOT EXISTS cards (id INTEGER PRIMARY KEY, question TEXT NOT NULL,"
                " answer TEXT NOT NULL, streak INTEGER NOT NULL DEFAULT 0, due TEXT NOT NULL)"
            )
            if args.command == "add":
                with db:
                    db.execute(
                        "INSERT INTO cards(question, answer, due) VALUES (?, ?, ?)",
                        (args.question, args.answer, today.isoformat()),
                    )
                print("Card added. It is ready for review.")
            elif args.command == "review":
                review(db, today)
            else:
                total, due, upcoming = db.execute(
                    "SELECT count(*), count(CASE WHEN due <= ? THEN 1 END),"
                    " min(CASE WHEN due > ? THEN due END) FROM cards",
                    (today.isoformat(), today.isoformat()),
                ).fetchone()
                print(f"{due} due today / {total} total")
                if upcoming:
                    print(f"Next scheduled date after today: {upcoming}")
    except sqlite3.Error as exc:
        print(f"Could not use deck {path}: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
