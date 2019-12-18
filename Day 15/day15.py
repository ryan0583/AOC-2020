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

    def move(self):
        self.brain.replace_next_input(self.direction)
        self.last_output = self.brain.process()
        if self.last_output == MOVED:
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


def run():
    def add_right_droid(_droids, droid):
        next_right_position = get_next_point(turn_right(droid.direction), droid.point)
        if next_right_position not in checked_points and next_right_position not in blocked_points:
            _droids.append(
                Droid(IntcodeComputer.copy(droid.brain), droid.point, turn_right(droid.direction), droid.path))

    def add_left_droid(_droids, droid):
        next_left_position = get_next_point(turn_left(droid.direction), droid.point)
        if next_left_position not in checked_points and next_left_position not in blocked_points:
            _droids.append(
                Droid(IntcodeComputer.copy(droid.brain), droid.point, turn_left(droid.direction), droid.path))

    def move_droids(_droids, move_color):
        _o2_tank_point = None
        _path = None
        _final_droid = None
        _droids_to_add = []

        for droid in _droids:
            checked_points.add(droid.point)
            droid.move()
            if droid.last_output == MOVED:
                graphics_panel.update_canvas_with_offset(droid.point, move_color, 22, 22)
            elif droid.last_output == BLOCKED:
                blocked_points.add(get_next_point(droid.direction, droid.point))
                graphics_panel.update_canvas_with_offset(get_next_point(droid.direction, droid.point), BLOCKED_COLOR, 22, 22)
            elif droid.last_output == FOUND_O2_SYSTEM:
                _o2_tank_point = get_next_point(droid.direction, droid.point)
                graphics_panel.update_canvas_with_offset(_o2_tank_point, O2_COLOR, 22, 22)
                _path = droid.path
                _final_droid = droid

            add_right_droid(_droids_to_add, droid)

            add_left_droid(_droids_to_add, droid)

        _droids.extend(_droids_to_add)
        _droids = list(filter(lambda _droid: _droid.point not in checked_points and _droid.point not in blocked_points,
                              _droids))

        graphics_panel.paint_canvas()
        return _droids, _o2_tank_point, _path, _final_droid

    graphics_panel = GraphicsPanel.create_empty_panel(43, 43)
    graphics_panel.init_canvas()
    graphics_panel.paint_canvas()

    current_point = Point(0, 0)
    checked_points = set()
    blocked_points = set()

    graphics_panel.update_canvas_with_offset(current_point, DROID_COLOR, 22, 22)
    graphics_panel.paint_canvas()

    filename = "input.txt"

    droids = [Droid(IntcodeComputer([], filename, True), current_point, N, [current_point]),
              Droid(IntcodeComputer([], filename, True), current_point, S, [current_point]),
              Droid(IntcodeComputer([], filename, True), current_point, E, [current_point]),
              Droid(IntcodeComputer([], filename, True), current_point, W, [current_point])]

    path = None
    o2_tank_point = None
    final_droid = None

    while path is None:
        droids, o2_tank_point, path, final_droid = move_droids(droids, DROID_COLOR)
        # time.sleep(.1)

    graphics_panel.paint_canvas()
    print("Path to O2 system is " + str(len(path)) + " steps")
    print("O2 tank is at " + str(o2_tank_point))

    checked_points = set()
    current_droid_position = get_next_point(final_droid.direction, final_droid.point)
    droids = [Droid(IntcodeComputer.copy(final_droid.brain), current_droid_position, N, [o2_tank_point]),
              Droid(IntcodeComputer.copy(final_droid.brain), current_droid_position, S, [o2_tank_point]),
              Droid(IntcodeComputer.copy(final_droid.brain), current_droid_position, E, [o2_tank_point]),
              Droid(IntcodeComputer.copy(final_droid.brain), current_droid_position, W, [o2_tank_point])]

    minutes = -1
    while len(droids) > 0:
        minutes += 1
        droids, o2_tank_point, path, final_droid = move_droids(droids, O2_COLOR)

    print("Filled with O2 after: " + str(minutes) + " minutes")
    input("Press any key...")


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
BLOCKED_COLOR = "yellow"
O2_COLOR = "blue"

run()
