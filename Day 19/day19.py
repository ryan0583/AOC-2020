import math

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

    computer = IntcodeComputer([], None, False)

    filename = "input.txt"
    ints = list(map(int, open(filename, "r").read().split(",")))

    points = []

    # for x in range(0, dim):
    #     for y in range(0, dim):
    #         computer.reset(ints)
    #         computer.inputs = [x, y]
    #         output = computer.process()
    #         if output == 1:
    #             point = Point(x, y)
    #             points.append(point)
    #             panel.update_canvas(Point(x, y), "red")
    #             panel.paint_canvas()
    #
    # last_col_points = list(filter(lambda _point: _point.x == dim - 1, points))
    # drop = min(list(map(lambda _point: _point.y, last_col_points)))
    #
    # print(drop)
    # beam_bottom = max(list(map(lambda _point: _point.y, last_col_points))) + 1
    #
    # print(beam_bottom - drop)
    #
    # angle1 = math.atan(drop / dim)
    # print(math.degrees(angle1))
    # angle2 = math.atan(beam_bottom / dim)
    # print(math.degrees(angle2))
    #
    # print(dim * math.tan(angle1))
    # print(dim * math.tan(angle2))
    #
    # desired_y_height = 100 + drop
    #
    # x = desired_y_height / (math.tan(angle2) - math.tan(angle1))
    # y = x * math.tan(angle1) + drop
    #
    # print(str(x) + ", " + str(y))
    #
    # start_x = math.floor()
    # start_y = math.floor(y) - 3

    start_x = 1355
    start_y = 765

    print(str(start_x) + ", " + str(start_y))

    panel.reset()
    for x in range(start_x, start_x + 1):
        print("col " + str(x - start_x))
        for y in range(start_y, start_y + dim):
            computer.reset(ints)
            computer.inputs = [x, y]
            output = computer.process()
            if output == 1:
                point = Point(x, y)
                # print(point)
                points.append(point)
                panel.update_canvas_with_offset(Point(x, y), "red", -start_x, -start_y)
                panel.paint_canvas()
            else:
                print("Output not 1 for point " + str(x) + ", " + str(y))

    input("press any key")

part2()
