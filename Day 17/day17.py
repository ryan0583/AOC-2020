from Utils.graphics_panel import GraphicsPanel
from Utils.intcode_computer import IntcodeComputer
from Utils.point import Point


def part1():
    graphics_panel = GraphicsPanel.create_empty_panel(100, 100)
    graphics_panel.init_canvas()
    graphics_panel.paint_canvas()

    camera = IntcodeComputer([], "input.txt", True)

    tile_colors = {}
    scaffold_count = 0
    x = 0
    y = 0

    while scaffold_count < 304:
        output = camera.process()
        color = None
        if output == SCAFFOLD:
            color = SCAFFOLD_COLOR
            scaffold_count += 1
        elif output == ROBOT_UP or output == ROBOT_RIGHT or output == ROBOT_LEFT or output == ROBOT_DOWN or output == ROBOT_DEAD:
            color = ROBOT_COLOR
        elif output == SPACE:
            color = SPACE_COLOR
        elif output == NEW_LINE:
            y += 1
            x = 0

        if color is not None:
            point = Point(x, y)
            graphics_panel.update_canvas(point, color)
            tile_colors[point] = color
            x += 1

    intersections = []
    intersect_count = 0

    for key in tile_colors.keys():
        color = tile_colors.get(key)
        if color == SCAFFOLD_COLOR:
            left_color = tile_colors.get(Point(key.x - 1, key.y))
            right_color = tile_colors.get(Point(key.x + 1, key.y))
            up_color = tile_colors.get(Point(key.x, key.y - 1))
            down_color = tile_colors.get(Point(key.x, key.y - 1))

            if color == left_color and color == right_color and color == up_color and color == down_color:
                intersections.append(key)
                intersect_count += key.x * key.y

    print(len(intersections))
    print(intersect_count)
    graphics_panel.paint_canvas()
    input("Press any key...")


SCAFFOLD = 35
SPACE = 46
NEW_LINE = 10
ROBOT_UP = 94
ROBOT_DOWN = 118
ROBOT_RIGHT = 62
ROBOT_LEFT = 60
ROBOT_DEAD = 88

SCAFFOLD_COLOR = "yellow"
SPACE_COLOR = "black"
ROBOT_COLOR = "red"

part1()
