import time
from random import randint

from Utils.debug_tools import raise_
from Utils.graphics_panel import GraphicsPanel
from Utils.intcode_computer import IntcodeComputer
from Utils.point import Point


def get_next_point(direction, current_point):
    direction_switcher = {
        N: lambda: Point(current_point.x, current_point.y - 1),
        S: lambda: Point(current_point.x, current_point.y + 1),
        W: lambda: Point(current_point.x - 1, current_point.y),
        E: lambda: Point(current_point.x + 1, current_point.y)
    }
    return direction_switcher.get(direction, lambda: raise_("Invalid direction: " + direction))()


def print_direction(direction):
    direction_switcher = {
        N: lambda: print("N"),
        S: lambda: print("S"),
        W: lambda: print("W"),
        E: lambda: print("E")
    }
    return direction_switcher.get(direction, lambda: raise_("Invalid direction: " + direction))()


def turn_right(direction):
    direction_switcher = {
        N: lambda: E,
        S: lambda: W,
        W: lambda: N,
        E: lambda: S
    }
    return direction_switcher.get(direction, lambda: raise_("Invalid direction: " + direction))()


def turn_left(direction):
    direction_switcher = {
        N: lambda: W,
        S: lambda: E,
        W: lambda: S,
        E: lambda: N
    }
    return direction_switcher.get(direction, lambda: raise_("Invalid direction: " + direction))()


def turn(direction):
    turn_dir = randint(0, 1)
    if turn_dir == RIGHT:
        return turn_right(direction)
    elif turn_dir == LEFT:
        return turn_left(direction)
    return direction


def update_panel(point, color, graphics_panel):
    normalised_point = Point(50 + point.x, 50 + point.y)
    graphics_panel.update_canvas(normalised_point, color)


def do_stuff(computer, direction, current_point, graphics_panel, checked_points, blocked_points):
    next_point = get_next_point(direction, current_point)
    if next_point in checked_points:
        return BLOCKED if next_point in blocked_points else None

    checked_points.add(next_point)
    computer.replace_next_input(direction)
    output = computer.process()
    if output == BLOCKED:
        update_panel(next_point, BLOCKED_COLOR, graphics_panel)
        blocked_points.add(next_point)
    elif output == MOVED:
        update_panel(next_point, DROID_COLOR, graphics_panel)
        color = EMPTY_COLOR
        if current_point == Point(0, 0):
            color = "white"
        update_panel(current_point, color, graphics_panel)
    elif output == FOUND_O2_SYSTEM:
        update_panel(next_point, O2_SYSTEM_COLOR, graphics_panel)
    else:
        raise_("Unknown output: " + output)
    graphics_panel.paint_canvas()
    time.sleep(0.02)
    return output


def part1():
    tile_map = {}
    for x in range(0, 100):
        for y in range(0, 100):
            tile_map[Point(x, y)] = "black"

    graphics_panel = GraphicsPanel(tile_map)
    graphics_panel.init_game()
    graphics_panel.paint_canvas()

    blocked_points = set()
    checked_points = set()
    tried_directions = {}
    current_point = Point(0, 0)
    update_panel(current_point, DROID_COLOR, graphics_panel)
    graphics_panel.paint_canvas()
    # time.sleep(0.1)
    computer = IntcodeComputer([], "input.txt", True)
    direction = N
    o2_system_point = None

    while o2_system_point is None:
        # print(current_point)
        # print_direction(direction)
        direction = turn_right(direction)
        output = do_stuff(computer, direction, current_point, graphics_panel, checked_points, blocked_points)
        if output == MOVED:
            current_point = get_next_point(direction, current_point)
            continue
        elif output == FOUND_O2_SYSTEM:
            o2_system_point = get_next_point(direction, current_point)
            break

        direction = turn_left(turn_left(direction))
        output = do_stuff(computer, direction, current_point, graphics_panel, checked_points, blocked_points)
        if output == MOVED:
            current_point = get_next_point(direction, current_point)
            continue
        elif output == FOUND_O2_SYSTEM:
            o2_system_point = get_next_point(direction, current_point)
            break

        direction = turn_right(direction)
        output = do_stuff(computer, direction, current_point, graphics_panel, checked_points, blocked_points)
        if output == MOVED:
            current_point = get_next_point(direction, current_point)
            continue
        elif output == FOUND_O2_SYSTEM:
            o2_system_point = get_next_point(direction, current_point)
            break
        elif output == BLOCKED:
            while output == BLOCKED:
                direction = turn(direction)
                output = do_stuff(computer, direction, current_point, graphics_panel, set(), set())
                if output == MOVED:
                    current_point = get_next_point(direction, current_point)
        elif output is None:
            tried_directions_for_point = tried_directions.get(Point)
            if tried_directions_for_point is None:
                tried_directions[Point] = set()
                tried_directions_for_point = tried_directions.get(Point)

            count = 0
            while direction in tried_directions_for_point and count < 4:
                direction = turn_right(direction)
                count += 1

            if count < 4:
                tried_directions_for_point.add(direction)
            else:
                direction = turn(direction)

            output = do_stuff(computer, direction, current_point, graphics_panel, set(), set())
            if output == MOVED:
                current_point = get_next_point(direction, current_point)
                continue

        graphics_panel.paint_canvas()
        time.sleep(0.02)

        # time.sleep(0.1)

    graphics_panel.paint_canvas()
    print(o2_system_point)
    input("Press Enter to close...")


N = 1
S = 2
W = 3
E = 4

RIGHT = 0
LEFT = 1
NONE = 3

BLOCKED = 0
MOVED = 1
FOUND_O2_SYSTEM = 2

EMPTY_COLOR = "black"
DROID_COLOR = "red"
BLOCKED_COLOR = "blue"
O2_SYSTEM_COLOR = "green"

part1()
