import time

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


def choose_direction(direction, current_point, checked_points, blocked_points):
    should_continue = get_next_point(direction, current_point) not in checked_points
    if should_continue:
        return can_continue(direction, current_point, blocked_points)
    return None


def can_continue(direction, current_point, blocked_points):
    if get_next_point(direction, current_point) not in blocked_points:
        return direction
    return None


def find_unblocked(current_point, blocked_points):
    directions = [N, S, E, W]
    for direction in directions:
        if get_next_point(direction, current_point) not in blocked_points:
            return direction


def get_next_direction(direction, current_point, checked_points, blocked_points):
    #should continue
    new_direction = choose_direction(direction, current_point, checked_points, blocked_points)
    if new_direction is not None:
        return new_direction

    if direction == N:
        new_direction = choose_direction(W, current_point, checked_points, blocked_points)
        if new_direction is not None:
            return new_direction
        new_direction = choose_direction(E, current_point, checked_points, blocked_points)
        if new_direction is not None:
            return new_direction

    if direction == S:
        new_direction = choose_direction(E, current_point, checked_points, blocked_points)
        if new_direction is not None:
            return new_direction
        new_direction = choose_direction(W, current_point, checked_points, blocked_points)
        if new_direction is not None:
            return new_direction

    if direction == W:
        new_direction = choose_direction(N, current_point, checked_points, blocked_points)
        if new_direction is not None:
            return new_direction
        new_direction = choose_direction(S, current_point, checked_points, blocked_points)
        if new_direction is not None:
            return new_direction

    if direction == E:
        new_direction = choose_direction(S, current_point, checked_points, blocked_points)
        if new_direction is not None:
            return new_direction
        new_direction = choose_direction(N, current_point, checked_points, blocked_points)
        if new_direction is not None:
            return new_direction

    #can continue
    new_direction = can_continue(direction, current_point, blocked_points)
    if new_direction is not None:
        return new_direction

    if direction == N:
        new_direction = can_continue(W, current_point, blocked_points)
        if new_direction is not None:
            return new_direction
        new_direction = can_continue(E, current_point, blocked_points)
        if new_direction is not None:
            return new_direction

    if direction == S:
        new_direction = can_continue(E, current_point, blocked_points)
        if new_direction is not None:
            return new_direction
        new_direction = can_continue(W, current_point, blocked_points)
        if new_direction is not None:
            return new_direction

    if direction == W:
        new_direction = can_continue(N, current_point, blocked_points)
        if new_direction is not None:
            return new_direction
        new_direction = can_continue(S, current_point, blocked_points)
        if new_direction is not None:
            return new_direction

    if direction == E:
        new_direction = can_continue(S, current_point, blocked_points)
        if new_direction is not None:
            return new_direction
        new_direction = can_continue(N, current_point, blocked_points)
        if new_direction is not None:
            return new_direction

    #go in opposite direction, or go in any unblocked direction
    direction_switcher = {
        N: lambda: S,
        S: lambda: N,
        W: lambda: E,
        E: lambda: W
    }
    opposite_direction = direction_switcher.get(direction, lambda: raise_("Invalid direction: " + direction))()
    if get_next_point(opposite_direction, current_point) in blocked_points:
        return find_unblocked(current_point, blocked_points)
    return opposite_direction


def print_direction(direction):
    direction_switcher = {
        N: lambda: print("N"),
        S: lambda: print("S"),
        W: lambda: print("W"),
        E: lambda: print("E")
    }
    return direction_switcher.get(direction, lambda: raise_("Invalid direction: " + direction))()


def update_panel(point, color, graphics_panel):
    normalised_point = Point(50 + point.x, 50 + point.y)
    graphics_panel.update_canvas(normalised_point, color)


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
    current_point = Point(0, 0)
    update_panel(current_point, DROID_COLOR, graphics_panel)
    graphics_panel.paint_canvas()
    # time.sleep(0.1)
    computer = IntcodeComputer([], "input.txt", True)
    direction = N
    o2_system_point = None

    while o2_system_point is None:
        print(current_point)
        print_direction(direction)
        computer.replace_next_input(direction)
        output = computer.process()
        if output == BLOCKED:
            print("blocked")
            next_point = get_next_point(direction, current_point)
            update_panel(next_point, BLOCKED_COLOR, graphics_panel)
            blocked_points.add(next_point)
        elif output == MOVED:
            print("moved")
            next_point = get_next_point(direction, current_point)
            update_panel(next_point, DROID_COLOR, graphics_panel)
            update_panel(current_point, EMPTY_COLOR, graphics_panel)
            checked_points.add(current_point)
            current_point = next_point
        elif output == FOUND_O2_SYSTEM:
            o2_system_point = get_next_point(direction, current_point)
        else:
            raise_("Unknown output: " + output)
        graphics_panel.paint_canvas()
        # time.sleep(0.1)
        direction = get_next_direction(direction, current_point, checked_points, blocked_points)

    print(o2_system_point)


N = 1
S = 2
W = 3
E = 4

BLOCKED = 0
MOVED = 1
FOUND_O2_SYSTEM = 2

EMPTY_COLOR = "black"
DROID_COLOR = "red"
BLOCKED_COLOR = "blue"

part1()
