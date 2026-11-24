import sqlite3
from datetime import date, timedelta
from unittest.mock import patch

from app.__main__ import main, review


def test_review_schedule_and_partial_session(tmp_path):
    deck = tmp_path / "deck.db"
    args = ["--db", str(deck)]
    for question in ["First?", "Second?"]:
        assert main([*args, "add", question, "Answer"]) == 0
    with sqlite3.connect(deck) as db:
        today = date.today()
        with patch("builtins.input", side_effect=["", "a", "", "q"]):
            review(db, today)
        assert db.execute("SELECT streak FROM cards ORDER BY id").fetchall() == [(0,), (0,)]
        for days in [1, 2, 4, 8, 16, 30, 30]:
            with patch("builtins.input", side_effect=["", "g", "", "g"]):
                review(db, today)
            today += timedelta(days=days)
            dates = db.execute("SELECT DISTINCT due FROM cards").fetchall()
            assert dates == [(today.isoformat(),)]
        with patch("builtins.input", side_effect=["", "a", EOFError]):
            review(db, today)
        assert db.execute("SELECT streak FROM cards ORDER BY id").fetchall() == [(0,), (6,)]
