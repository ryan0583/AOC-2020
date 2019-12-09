from Utils.intcode_computer import IntcodeComputer


def part1():
    # file = open("testinput.txt", "r")
    file = open("input.txt", "r")
    ints = list(map(int, file.read().split(",")))
    intcode_computer = IntcodeComputer([2], ints, False)
    intcode_computer.process()

part1()
