def read_lines():
    return list(map(int, open("Input.txt", "r").readlines()))


def part1():
    lines = read_lines()

    def remainder_in_list(number):
        return (2020 - int(number)) in lines

    match = next(filter(remainder_in_list, lines))
    return match * (2020 - match)


def part2():
    lines = read_lines()

    def sum_less_than_required(number):
        return

    for line1 in lines:
        for line2 in lines:
            sum2 = int(line1) + int(line2)
            if sum2 < 2020:
                for line3 in lines:
                    result = sum2 + int(line3)
                    if result == 2020:
                        return int(line1) * int(line2) * int(line3)


print(part1())
print(part2())
