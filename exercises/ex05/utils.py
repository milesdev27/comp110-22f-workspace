""""""

__author__ = "730615836"

def only_evens(xs: list[int]) -> list:
    """Generates a list of even integer values!"""
    i: int = 0
    output: list[int] = []
    while i < len(xs):
        if xs[i]%2 == 0:
            output.append(xs[i])
            i += 1
        else:
            i += 1
    return output

def concat(a: list[int], b: list[int]) -> list:
    """Generates a combined list!"""
    combine: list[int] = []
    for x in a:
        combine.append(x)
    for y in b:
        combine.append(y)
    return combine

def sub(a_list: list[int], start: int, end: int) -> list:
    """Generates a list!"""
    xs: list[int] = []
    i: int = start
    while i < 0:
        i += 1
    while i > len(a_list):
        i -= 1
    while i < len(a_list) - 1:
        xs.append(a_list[i])
        i += 1
    return xs