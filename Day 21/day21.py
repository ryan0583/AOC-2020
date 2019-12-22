import time

from Utils.graphics_panel import GraphicsPanel
from Utils.intcode_computer import IntcodeComputer


def convert_to_ascii(string):
    return [ord(c) for c in string]


def add_instruction(string, inputs):
    inputs.extend(convert_to_ascii(string + "\n"))


def part1():
    panel = GraphicsPanel.create_empty_panel(30, 30)
    panel.init_canvas()
    panel.paint_canvas()

    all_inputs = []
    add_instruction("NOT A J", all_inputs)
    add_instruction("NOT B T", all_inputs)
    add_instruction("OR T J", all_inputs)
    add_instruction("NOT C T", all_inputs)
    add_instruction("OR T J", all_inputs)
    add_instruction("AND D J", all_inputs)
    add_instruction("WALK", all_inputs)

    computer = IntcodeComputer(all_inputs, "input.txt", True)

    output = computer.process()
    printstr = chr(output)
    panel.add_text(printstr, "green yellow")
    while output < 130:
        printstr += chr(output)
        if output == 10:
            panel.update_text(printstr)
            panel.paint_canvas()
        output = computer.process()

    input(str(output) + " - press any key")


def part2():
    panel = GraphicsPanel.create_empty_panel(30, 30)
    panel.init_canvas()
    panel.paint_canvas()

    all_inputs = []
    add_instruction("NOT A J", all_inputs)
    add_instruction("NOT B T", all_inputs)
    add_instruction("OR T J", all_inputs)
    add_instruction("NOT C T", all_inputs)
    add_instruction("OR T J", all_inputs)
    add_instruction("AND D J", all_inputs)
    add_instruction("NOT E T", all_inputs)
    add_instruction("NOT T T", all_inputs)
    add_instruction("OR H T", all_inputs)
    add_instruction("AND T J", all_inputs)
    add_instruction("RUN", all_inputs)

    computer = IntcodeComputer(all_inputs, "input.txt", True)

    output = computer.process()
    printstr = chr(output)
    panel.add_text(printstr, "green yellow")
    while output < 130:
        printstr += chr(output)
        if output == 10:
            panel.update_text(printstr)
            panel.paint_canvas()
        output = computer.process()
        time.sleep(0.03)

    input(str(output) + " - press any key")


# part1()
part2()
