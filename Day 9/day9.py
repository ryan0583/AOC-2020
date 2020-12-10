from itertools import combinations

from Utils.file_reader import read_lines


def check_next(next_index, countback, lines):
    next_number = lines[next_index]
    sub_lines = lines[next_index - countback: next_index]
    combos = list(combinations(sub_lines, 2))
    sums = {sum(combo) for combo in combos}
    if next_number in sums:
        return -1
    return next_number


def find_invalid():
    lines = [int(line) for line in read_lines('Input.txt')]
    invalid = -1
    countback = 25
    next_index = countback
    while invalid == -1:
        invalid = check_next(next_index, countback, lines)
        next_index += 1
    return invalid


def part1():
    return find_invalid()


def find_contiguous_set(lines, number_to_find):
    start_index = 0
    end_index = 0
    while True:
        sub_list = lines[start_index:end_index]
        number_to_check = sum(sub_list)
        if number_to_check == number_to_find:
            return sub_list
        end_index += 1
        if number_to_check > number_to_find or end_index > len(lines) - 1:
            start_index += 1
            end_index = start_index
        if start_index > len(lines) - 1:
            raise Exception('No contiguous set found which sums to ' + number_to_find)


def part2():
    lines = [int(line) for line in read_lines('Input.txt')]
    number_to_find = find_invalid()
    contiguous_set = find_contiguous_set(lines, number_to_find)
    return min(contiguous_set) + max(contiguous_set)


print(part1())
print(part2())
