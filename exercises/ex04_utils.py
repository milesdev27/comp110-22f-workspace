"""Utility functions!"""

__author__ = "730615836"


def all(a: list[int], b: int) -> bool:
    """Generates a boolean value of either true or false."""
    i: int = 0
    contain: bool = True
    if len(a) == 0:
        contain = False
    else:
        while i < len(a):
            if a[i] == b:
                i += 1
            else:
                contain = False
                i += 1
    return contain


def max(c: list[int]) -> int:
    """Generates the maximum value in a list of integer values!"""
    if len(c) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        value: int = c[0]
        i: int = 1
        while i != len(c):
            if int(c[i]) > value:
                value = c[i]
                i += 1
            else:
                i += 1
        
    return value


def is_equal(d: list[int], e: list[int]) -> bool:
    """Determines if two lists of integers are equal!"""
    if len(d) != len(e):
        return False
    i: int = 0
    equal: bool = True
    while i < len(d):
        if d[i] == e[i]:
            i += 1
        else:
            equal = False
            i += 1
    return equal