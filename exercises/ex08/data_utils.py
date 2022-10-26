"""Dictionary related utility functions."""

__author__ = "730615836"

# Define your functions below


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Returns a list of the rows of data."""
    lines: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for line in csv_reader:
        lines.append(line)
    file_handle.close()
    return lines


def column_values(table: list[dict[str, str]], key: str) -> list[str]:
    """Returns the values at a specific key."""
    result: list[str] = []
    for i in table:
        result.append(i[key])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Returns a dict of all column names."""
    result: dict[str, list[str]] = {}
    row: dict[str, str] = table[0]
    for i in row:
        result[i] = column_values(table, i)
    return result


def head(table: dict[str, list[str]], number_row: int) -> dict[str, list[str]]:
    """Returns a table of the first N number of rows."""
    result: dict[str, list[str]] = {}
    for key in table:
        i: int = 0
        value: list[str] = []
        if number_row > len(table[key]):
            number_row = len(table[key])
        while i < number_row:
            value.append(table[key][i])
            i += 1
        result[key] = value
    return result


def select(table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Returns a dict of selected columns."""
    result: dict[str, list[str]] = {}
    for name in columns:
        result[name] = table[name] 
    return result


def concat(a_table: dict[str, list[str]], b_table: dict[str, list[str]]) -> dict[str, list[str]]:
    """Returns a table of two combined column-based tables."""
    result: dict[str, list[str]] = {}
    for name in a_table:
        result[name] = a_table[name]
    for name in b_table:
        if name in result:
            result[name] += b_table[name]
        else:
            result[name] = b_table[name]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Counts the instances of a string in a list."""
    result: dict[str, int] = {}
    for i in values:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result