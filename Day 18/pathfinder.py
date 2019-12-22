from Utils.graphics_panel import GraphicsPanel
from Utils.point import Point


class Explorer:
    def __init__(self, path, doors, keys):
        self.path = path
        self.doors = doors
        self.keys = keys


def find_path(pointA, pointB, maze_map):
    path = []
    doors = []


def map_color(char):
    if char == SPACE:
        return "black"
    if char == WALL:
        return "white"
    if char == ENTRY:
        return "blue"
    if char.islower():
        return "yellow"
    if char.isupper():
        return "red"


def test():
    lines = open("testinput.txt", "r").read().splitlines()

    panel = GraphicsPanel.create_empty_panel(100, 100)
    panel.init_canvas()

    maze_map = {}
    start_point = None
    keys = []
    doors = []

    for y, line in enumerate(lines):
        chars = list(line)
        for x, char in enumerate(chars):
            point = Point(x, y)
            if char == ENTRY:
                start_point = point
            if char.islower():
                keys.append(point)
            if char.isupper():
                doors.append(point)
            panel.update_canvas(point, map_color(char))
            maze_map[Point(x, y)] = char

    panel.paint_canvas()
    input("press any key...")


WALL = "#"
SPACE = "."
ENTRY = "@"

test()
