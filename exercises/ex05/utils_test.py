""""""

__author__ = "730615836"

from utils import only_evens
from utils import concat
from utils import sub

def test_only_evens_1() -> None:
    x: list[int] = [1, 2, 6, 7, 9]
    assert only_evens(x) == [2, 6]

def test_only_evens_2() -> None:
    x: list[int] = []
    assert only_evens(x) == []

def test_only_evens_3() -> None:
    x: list[int] = [4, 4, 4, 4, 4]
    assert only_evens(x) == [4, 4, 4, 4, 4]

def test_concat_1() -> None:
    x: list[int] = [1, 2, 3]
    y: list[int] = [4, 5, 6]
    assert concat(x, y) == [1, 2, 3, 4, 5, 6]

def test_concat_2() -> None:
    x: list[int] = []
    y: list[int] = [4, 6, 5]
    assert concat(x, y) == [4, 6, 5]

def test_concat_3() -> None:
    x: list[int] = [2, 3]
    y: list[int] = [6, 8, 10]
    assert concat(x, y) == [2, 3, 6, 8, 10]

def test_sub_1() -> None:
    a_list: list[int] = [5, 4, 6, 3, 7]
    x: int = 1
    y: int = 4
    assert sub(a_list, x, y) == [4, 6, 3]

def test_sub_2() -> None:
    a_list: list[int] = [1, 2, 3, 4, 5]
    x: int = -3
    y: int = 6
    assert sub(a_list, x, y) == [1, 2, 3, 4]

def test_sub_3() -> None:
    a_list: list[int] = [1, 2, 3, 4, 5]
    x: int = 1
    y: int = 1
    assert sub(a_list, x, y) == [2, 3, 4]