from Utils.intcode_computer import process


def part1():
    file = open("input.txt", "r")
    ints = list(map(int, file.read().split(",")))
    result = process([1], ints)
    print(result)
    return result


def part2():
    file = open("input.txt", "r")
    ints = list(map(int, file.read().split(",")))
    result = process([5], ints)
    print(result)
    return result
