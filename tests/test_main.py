from app.main import greet


def test_greet() -> None:
    assert greet("friend") == "Hello, friend!"
