from Utils.intcode_computer import IntcodeComputer


def part1():
    file = open("input.txt", "r")
    ints = list(map(int, file.read().split(",")))
    intcode_computer = IntcodeComputer([1], ints)
    result = intcode_computer.process()
    print(result)
    return result


def part2():
    file = open("input.txt", "r")
    ints = list(map(int, file.read().split(",")))
    intcode_computer = IntcodeComputer([5], ints)
    result = intcode_computer.process()
    print(result)
    return result
