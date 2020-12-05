from Utils.file_reader import read_lines
import math


def parse_row(char, existing_rows):
    existing_length = len(existing_rows)
    halfway = math.ceil(len(existing_rows) / 2)
    if char == 'F':
        return existing_rows[0:halfway]
    elif char == 'B':
        return existing_rows[halfway: existing_length]


def parse_col(char, existing_cols):
    existing_length = len(existing_cols)
    halfway = math.ceil(len(existing_cols) / 2)
    if char == 'L':
        return existing_cols[0:halfway]
    elif char == 'R':
        return existing_cols[halfway: existing_length]


def part1():
    seat_ids = []
    lines = read_lines()
    for line in lines:
        rows = list(range(128))
        cols = list(range(8))
        for char in line:
            if char == 'F' or char == 'B':
                rows = parse_row(char, rows)
            elif char == 'R' or char == 'L':
                cols = parse_col(char, cols)
        seat_ids.append(rows[0] * 8 + cols[0])
    return max(seat_ids)


print(part1())
