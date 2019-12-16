from random import randint

from Utils.debug_tools import raise_
from Utils.graphics_panel import GraphicsPanel
from Utils.intcode_computer import IntcodeComputer
from Utils.point import Point


class Droid:
    def __init__(self, brain, point, direction, path):
        self.brain = brain
        self.point = point
        self.direction = direction
        self.path = list(path)
        self.last_output = None
        self.is_blocked = False

    def move(self):
        self.brain.replace_next_input(self.direction)
        self.last_output = self.brain.process()
        if self.last_output == BLOCKED:
            self.is_blocked = True
        elif self.last_output == MOVED:
            self.path.append(self.point)
            self.point = get_next_point(self.direction, self.point)


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


def part1():
    def add_right_droid():
        next_right_position = get_next_point(turn_right(droid.direction), droid.point)
        if next_right_position not in checked_points and next_right_position not in blocked_points:
            droids.append(
                Droid(IntcodeComputer.copy(droid.brain), droid.point, turn_right(droid.direction), droid.path))

    def add_left_droid():
        next_left_position = get_next_point(turn_left(droid.direction), droid.point)
        if next_left_position not in checked_points and next_left_position not in blocked_points:
            droids.append(
                Droid(IntcodeComputer.copy(droid.brain), droid.point, turn_left(droid.direction), droid.path))

    tile_map = {}
    for x in range(0, 100):
        for y in range(0, 100):
            tile_map[Point(x, y)] = "black"

    graphics_panel = GraphicsPanel(tile_map)
    graphics_panel.init_game()
    graphics_panel.paint_canvas()

    current_point = Point(0, 0)
    checked_points = set()
    blocked_points = set()

    update_panel(current_point, DROID_COLOR, graphics_panel)
    graphics_panel.paint_canvas()

    droids = [Droid(IntcodeComputer([], "input.txt", True), current_point, N, [current_point]),
              Droid(IntcodeComputer([], "input.txt", True), current_point, S, [current_point]),
              Droid(IntcodeComputer([], "input.txt", True), current_point, E, [current_point]),
              Droid(IntcodeComputer([], "input.txt", True), current_point, W, [current_point])]

    path = None

    while path is None:
        for droid in droids:
            checked_points.add(droid.point)
            droid.move()
            if droid.last_output == MOVED:
                update_panel(droid.point, DROID_COLOR, graphics_panel)
                graphics_panel.paint_canvas()
                # time.sleep(.1)
            elif droid.last_output == BLOCKED:
                blocked_points.add(get_next_point(droid.direction, droid.point))
                update_panel(get_next_point(droid.direction, droid.point), BLOCKED_COLOR, graphics_panel)
                graphics_panel.paint_canvas()
                # time.sleep(.1)
                droids.remove(droid)
            elif droid.last_output == FOUND_O2_SYSTEM:
                update_panel(get_next_point(droid.direction, droid.point), O2_SYSTEM_COLOR, graphics_panel)
                path = droid.path

            add_right_droid()

            add_left_droid()

        graphics_panel.paint_canvas()
        # time.sleep(.1)

    graphics_panel.paint_canvas()
    print(len(path))
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
