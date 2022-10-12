"""Dictionary Functions!"""


__author__ = "730615836"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a dict!"""
    result: dict[str, str] = {}
    for key in a:
        if a[key] in result:
            raise KeyError("Duplicate Values.")
        else:
            result[a[key]] = key
    return result


def favorite_color(b: dict[str, str]) -> str:
    """Returns the most poplular color!"""
    color: dict[str, int] = {}
    fav_color: str = ""
    i: int = 0
    for keys in b:
        if b[keys] in color:
            color[b[keys]] += 1
        else:
            color[b[keys]] = 1
    for item in color:
        if color[item] > i:
            i = color[item]
            fav_color = item
    return fav_color


def count(c: list[str]) -> dict[str, int]:
    """Counts the instances of a string in a list."""
    result: dict[str, int] = {}
    for i in c:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result