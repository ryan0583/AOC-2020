from Utils.file_reader import read_lines


def remainder_in_list(number, lines):
    return (2020 - int(number)) in lines


def part1():
    lines = list(map(int, read_lines()))
    match = next(filter(lambda number: remainder_in_list(number, lines), lines))
    return match * (2020 - match)


def part2():
    lines = list(map(int, read_lines()))

    for line1 in lines:
        for line2 in lines:
            sum2 = int(line1) + int(line2)
            if remainder_in_list(sum2, lines):
                return line1 * line2 * (2020 - sum2)


print(part1())
print(part2())
