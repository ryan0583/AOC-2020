from Utils.graphics_panel import GraphicsPanel
from Utils.intcode_computer import IntcodeComputer
from Utils.point import Point


def part1():
    panel = GraphicsPanel.create_empty_panel(50, 50)
    panel.init_canvas()

    count = 0

    computer = IntcodeComputer([], None, False)

    filename = "input.txt"
    ints = list(map(int, open(filename, "r").read().split(",")))

    for x in range(0, 50):
        for y in range(0, 50):
            computer.reset(ints)
            computer.inputs = [x, y]
            computer.process()
            computer.append_input(x)
            computer.append_input(y)
            output = computer.process()
            if output == 1:
                count += 1
                panel.update_canvas(Point(x, y), "red")
                panel.paint_canvas()

    panel.paint_canvas()
    print(count)
    input("press any key")


def part2():
    dim = 100

    panel = GraphicsPanel.create_empty_panel(dim, dim)
    panel.init_canvas()
    count = 0

    computer = IntcodeComputer([], None, False)

    filename = "input.txt"
    ints = list(map(int, open(filename, "r").read().split(",")))

    x_next_start = 500
    y_next_start = 300
    y_last_col = []

    while True:
        panel.reset()
        for x in range(x_next_start, x_next_start + dim):
            for y in range(y_next_start, y_next_start + dim):
                computer.reset(ints)
                computer.inputs = [x, y]
                computer.process()
                computer.append_input(x)
                computer.append_input(y)
                output = computer.process()
                if output == 1:
                    count += 1
                    panel.update_canvas_with_offset(Point(x, y), "red", - x_next_start, - y_next_start)
                    panel.paint_canvas()
                    if x == x_next_start + dim - 1:
                        y_last_col.append(y)
        if min(y_last_col) == y_next_start:
            break
        x_next_start += dim
        y_next_start = min(y_last_col)
        y_last_col = []

    print(x_next_start, y_next_start)
    input("press any key")


part2()
