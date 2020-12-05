import math

from Utils.file_reader import read_lines


def find_new_range(char, existing_range, front_char):
    existing_length = len(existing_range)
    halfway = math.ceil(existing_length / 2)
    return existing_range[0:halfway] if char == front_char else existing_range[halfway: existing_length]


def is_matching_char(char, front_char, back_char):
    return char == front_char or char == back_char


def process_line(line, front_char, back_char, initial_range):
    ranges = [initial_range]
    matching_chars = filter(lambda line_char: is_matching_char(line_char, front_char, back_char), line)
    for char in matching_chars:
        ranges.append(find_new_range(char, ranges[-1], front_char))
    return ranges[-1][0]


def get_seat_id(line):
    row = process_line(line, 'F', 'B', list(range(128)))
    col = process_line(line, 'L', 'R', list(range(8)))
    return row * 8 + col


def get_seat_ids():
    return list(map(lambda line: get_seat_id(line), read_lines()))


def part1():
    return max(get_seat_ids())


def is_missing_seat_number(seat_id, seat_ids):
    return seat_id not in seat_ids and seat_id - 1 in seat_ids and seat_id + 1


def part2():
    seat_ids = get_seat_ids()
    return list(filter(
        lambda seat_id: is_missing_seat_number(seat_id, seat_ids),
        list(range(min(seat_ids), max(seat_ids)))))[0]


print(part1())
print(part2())
