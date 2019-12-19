from Utils.graphics_panel import GraphicsPanel
from Utils.intcode_computer import IntcodeComputer
from Utils.point import Point


def part1():
    panel = GraphicsPanel.create_empty_panel(50, 50)
    panel.init_canvas()

    count = 0

    for x in range(0, 50):
        for y in range(0, 50):
            computer = IntcodeComputer([], "input.txt", True)
            computer.append_input(x)
            computer.append_input(y)
            output = computer.process()
            if output == 1:
                count += 1
                panel.update_canvas(Point(x, y), "red")

    panel.paint_canvas()
    print(count)
    input("press any key")


part1()
