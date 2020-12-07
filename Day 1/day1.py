from Utils.file_reader import read_lines

from itertools import combinations


def remainder_in_list(number, lines):
    return (2020 - int(number)) in lines


def part1():
    lines = {int(line) for line in read_lines()}
    match = {number for number in lines if remainder_in_list(number, lines)}.pop()
    return match * (2020 - match)


def part2():
    lines = {int(line) for line in read_lines()}
    combos = list(combinations(lines, 2))
    pair = {pair for pair in combos if remainder_in_list(pair[0] + pair[1], lines)}.pop()
    return pair[0] * pair[1] * (2020 - pair[0] - pair[1])


print(part1())
print(part2())
