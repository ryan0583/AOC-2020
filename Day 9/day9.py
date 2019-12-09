from Utils.intcode_computer import IntcodeComputer


def part1():
    intcode_computer = IntcodeComputer([1], "input.txt", False)
    return intcode_computer.process()


def part2():
    intcode_computer = IntcodeComputer([2], "input.txt", False)
    return intcode_computer.process()
