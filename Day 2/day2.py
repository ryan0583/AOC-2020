from Utils.intcode_computer import IntcodeComputer


def calculate_output(noun, verb):
    intcode_computer = IntcodeComputer([], "input.txt", False)
    intcode_computer.ints[1] = noun
    intcode_computer.ints[2] = verb
    intcode_computer.process()
    return intcode_computer.ints[0]


def part1():
    return calculate_output(12, 2)


def part2():
    exp = 19690720
    output = None
    for noun in range(100):
        for verb in range(100):
            if calculate_output(noun, verb) == exp:
                output = 100 * noun + verb
                break
    return output
