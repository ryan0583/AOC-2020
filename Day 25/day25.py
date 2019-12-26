import sys
sys.path.append('../')
from Utils.intcode_computer import IntcodeComputer


def convert_to_ascii(string):
    return [ord(c) for c in string]


def add_instruction(string, inputs):
    inputs.extend(convert_to_ascii(string + "\n"))


def part1():
    computer = IntcodeComputer([], "input.txt", True)

    while computer.is_running():
        last_output = ""
        output = ""
        while output != "\n":
            output = chr(computer.process())
            last_output += str(output)
        print(last_output.strip())
        if last_output == "Command?\n":
            command = input("")
            add_instruction(command, computer.inputs)


part1()
