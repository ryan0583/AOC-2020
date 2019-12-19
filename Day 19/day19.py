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


def print_stuff(start_x, start_y):
    dim = 100

    panel = GraphicsPanel.create_empty_panel(dim, dim)
    panel.init_canvas()

    computer = IntcodeComputer([], None, False)

    filename = "input.txt"
    ints = list(map(int, open(filename, "r").read().split(",")))

    panel.reset()
    for x in range(start_x, start_x + dim):
        print("col " + str(x - start_x))
        for y in range(start_y, start_y + dim):
            computer.reset(ints)
            computer.inputs = [x, y]
            output = computer.process()
            if output == 1:
                panel.update_canvas_with_offset(Point(x, y), "red", -start_x, -start_y)
                panel.paint_canvas()
            else:
                print("Output not 1 for point " + str(x) + ", " + str(y))

    input("press any key")


def part2():
    def count_beam_squares(_x, _y_start, _y_end):
        _count = 0
        y = _y_start
        _first_y = None
        _last_y = None
        found_beam = False
        while True:
            computer.reset(ints)
            computer.inputs = [_x, y]
            output = computer.process()
            if output == 1:
                _count += 1
                found_beam = True
                _first_y = y
            elif found_beam:
                _last_y = y - 1
                break
            y += 1
            if _y_end is not None and y > _y_end:
                break

        return _count, _first_y, _last_y

    computer = IntcodeComputer([], None, False)

    filename = "input.txt"
    ints = list(map(int, open(filename, "r").read().split(",")))

    x = 1330
    y_start = 400

    while True:
        count1, first_y1, last_y1 = count_beam_squares(x, y_start, None)
        count2, first_y2, last_y2 = count_beam_squares(x + 99, last_y1 - 99, last_y1)
        print("col = " + str(x))
        print(count1)
        print(last_y1 - 99)
        print(count2)
        print(first_y2)
        if count2 == 100:
            print("FOUND!!!")
            break
        x += 1


# part1()
# part2()
print_stuff(1353, 764)

