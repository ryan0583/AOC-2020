from Utils.file_parser import FileParser
from Utils.graphics_panel import GraphicsPanel
from Utils.point import Point


def part1():
    def get_adjacent_count():
        up_char = bug_point_map.get(Point(point.x, point.y - 1))
        down_char = bug_point_map.get(Point(point.x, point.y + 1))
        right_char = bug_point_map.get(Point(point.x + 1, point.y))
        left_char = bug_point_map.get(Point(point.x - 1, point.y))

        return len(list(filter(lambda _char: _char is not None, [up_char, down_char, right_char, left_char])))

    def update_canvas():
        for _point in bug_point_map.keys():
            graphics_panel.update_canvas(_point, "red")

    def calculate_biodiversity():
        _biodiversity = 0
        power = 1
        for _y in range(0, 5):
            for _x in range(0, 5):
                if bug_point_map.get(Point(_x, _y)) == BUG:
                    _biodiversity += power
                power = power * 2
        return _biodiversity

    graphics_panel = GraphicsPanel.create_empty_panel(30, 30)
    graphics_panel.init_canvas()
    graphics_panel.paint_canvas()

    file_parser = FileParser("input.txt")

    bug_point_map = file_parser.read_points_map(BUG)
    new_bug_point_map = {}
    seen_layouts = set()

    update_canvas()
    graphics_panel.paint_canvas()
    # time.sleep(2)

    while True:
        for y in range(0, 5):
            for x in range(0, 5):
                point = Point(x, y)
                adjacent_count = get_adjacent_count()
                char = bug_point_map.get(point)
                if char is not None:
                    if adjacent_count == 1:
                        new_bug_point_map[point] = BUG
                else:
                    if adjacent_count == 1 or adjacent_count == 2:
                        new_bug_point_map[point] = BUG

        bug_point_map = new_bug_point_map.copy()
        graphics_panel.reset()
        update_canvas()
        graphics_panel.paint_canvas()
        biodiversity = calculate_biodiversity()
        if biodiversity in seen_layouts:
            print(biodiversity)
            break
        seen_layouts.add(biodiversity)
        new_bug_point_map = {}
        # time.sleep(2)

    input("press any key")


BUG = "#"

part1()
