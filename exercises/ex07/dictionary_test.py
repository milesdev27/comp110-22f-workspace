"""Testing Dictionary Functions!"""


__author__ = "730615836"


from dictionary import invert
from dictionary import favorite_color
from dictionary import count


import pytest


def test_invert_1() -> None:
    """Duplicate values!"""
    x: dict[str, str] = {"Hello": "Hi", "Bye": "Hi"}
    with pytest.raises(KeyError):
        invert(x)


def test_invert_2() -> None:
    """Hi and Bye!"""
    x: dict[str, str] = {"Hello": "Hi", "Goodbye": "Bye"}
    assert invert(x) == {'Hi': 'Hello', 'Bye': 'Goodbye'}


def test_invert_3() -> None:
    """First and last names."""
    x: dict[str, str] = {"Kris": "Jordan", "Miles": "Devine"}
    assert invert(x) == {'Jordan': 'Kris', 'Devine': 'Miles'}


def test_favorite_color_1() -> None:
    """Blue."""
    x: dict[str, str] = {"Miles": "Orange", "Laura": "Blue", "Jack": "Blue"}
    assert favorite_color(x) == "Blue"


def test_favorite_color_2() -> None:
    """Tie."""
    x: dict[str, str] = {"Miles": "Orange", "Roman": "Blue"}
    assert favorite_color(x) == "Orange"


def test_favorite_color_3() -> None:
    """One key."""
    x: dict[str, str] = {"Miles": "Orange"}
    assert favorite_color(x) == "Orange"


def test_count_1() -> None:
    """Empty."""
    x: list[str] = []
    assert count(x) == {}


def test_count_2() -> None:
    """Hi, Hello."""
    x: list[str] = ["Hi", "Hi", "Hello"]
    assert count(x) == {"Hi": 2, "Hello": 1}


def test_count_3() -> None:
    """Names."""
    x: list[str] = ["Miles", "Miles", "Laura", "Jack", "Laura"]
    assert count(x) == {"Miles": 2, "Laura": 2, "Jack": 1}