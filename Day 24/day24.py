from Utils.file_parser import FileParser
from Utils.graphics_panel import GraphicsPanel
from Utils.point import Point


class Layer:
    def __init__(self):
        self.child = None
        self.parent = None
        self.bug_point_map = {}
        self.new_child = None
        self.new_parent = None
        self.new_bug_point_map = {}
        self.layer_number = 0

    def get_total_bug_count(self):
        return len(self.bug_point_map.keys())

    def get_bug_count(self, points):
        count = 0
        for point in points:
            bug = self.bug_point_map.get(point)
            if bug is not None:
                count += 1
        return count

    def get_adjacent_count(self, point):
        up_char = self.bug_point_map.get(Point(point.x, point.y - 1))
        down_char = self.bug_point_map.get(Point(point.x, point.y + 1))
        right_char = self.bug_point_map.get(Point(point.x + 1, point.y))
        left_char = self.bug_point_map.get(Point(point.x - 1, point.y))

        return len(list(filter(lambda _char: _char is not None, [up_char, down_char, right_char, left_char])))

    def get_right_inner_adjacent_count(self, point):
        up_char = self.bug_point_map.get(Point(point.x, point.y - 1))
        down_char = self.bug_point_map.get(Point(point.x, point.y + 1))
        right_char = self.bug_point_map.get(Point(point.x + 1, point.y))

        chars = [up_char, down_char, right_char]

        left_chars = []
        if self.child is not None:
            left_chars.append(self.child.bug_point_map.get(Point(4, 0)))
            left_chars.append(self.child.bug_point_map.get(Point(4, 1)))
            left_chars.append(self.child.bug_point_map.get(Point(4, 2)))
            left_chars.append(self.child.bug_point_map.get(Point(4, 3)))
            left_chars.append(self.child.bug_point_map.get(Point(4, 4)))
        chars.extend(left_chars)

        return len(list(filter(lambda _char: _char is not None, chars)))

    def get_left_inner_adjacent_count(self, point):
        up_char = self.bug_point_map.get(Point(point.x, point.y - 1))
        down_char = self.bug_point_map.get(Point(point.x, point.y + 1))
        left_char = self.bug_point_map.get(Point(point.x - 1, point.y))

        chars = [up_char, down_char, left_char]

        right_chars = []
        if self.child is not None:
            right_chars.append(self.child.bug_point_map.get(Point(0, 0)))
            right_chars.append(self.child.bug_point_map.get(Point(0, 1)))
            right_chars.append(self.child.bug_point_map.get(Point(0, 2)))
            right_chars.append(self.child.bug_point_map.get(Point(0, 3)))
            right_chars.append(self.child.bug_point_map.get(Point(0, 4)))
        chars.extend(right_chars)

        return len(list(filter(lambda _char: _char is not None, chars)))

    def get_top_inner_adjacent_count(self, point):
        up_char = self.bug_point_map.get(Point(point.x, point.y - 1))
        right_char = self.bug_point_map.get(Point(point.x + 1, point.y))
        left_char = self.bug_point_map.get(Point(point.x - 1, point.y))

        chars = [up_char, right_char, left_char]

        down_chars = []
        if self.child is not None:
            down_chars.append(self.child.bug_point_map.get(Point(0, 0)))
            down_chars.append(self.child.bug_point_map.get(Point(1, 0)))
            down_chars.append(self.child.bug_point_map.get(Point(2, 0)))
            down_chars.append(self.child.bug_point_map.get(Point(3, 0)))
            down_chars.append(self.child.bug_point_map.get(Point(4, 0)))
        chars.extend(down_chars)

        return len(list(filter(lambda _char: _char is not None, chars)))

    def get_bottom_inner_adjacent_count(self, point):
        down_char = self.bug_point_map.get(Point(point.x, point.y + 1))
        right_char = self.bug_point_map.get(Point(point.x + 1, point.y))
        left_char = self.bug_point_map.get(Point(point.x - 1, point.y))

        chars = [down_char, right_char, left_char]

        up_chars = []
        if self.child is not None:
            up_chars.append(self.child.bug_point_map.get(Point(0, 4)))
            up_chars.append(self.child.bug_point_map.get(Point(1, 4)))
            up_chars.append(self.child.bug_point_map.get(Point(2, 4)))
            up_chars.append(self.child.bug_point_map.get(Point(3, 4)))
            up_chars.append(self.child.bug_point_map.get(Point(4, 4)))
        chars.extend(up_chars)

        return len(list(filter(lambda _char: _char is not None, chars)))

    def process_inner_edge(self):
        top_inner_point = Point(2, 1)
        top_inner_count = self.get_top_inner_adjacent_count(top_inner_point)
        if top_inner_count == 1 or top_inner_count == 2:
            self.new_bug_point_map[top_inner_point] = BUG

        left_inner_point = Point(1, 2)
        left_inner_count = self.get_left_inner_adjacent_count(left_inner_point)
        if left_inner_count == 1 or left_inner_count == 2:
            self.new_bug_point_map[left_inner_point] = BUG

        bottom_inner_point = Point(2, 3)
        bottom_inner_count = self.get_bottom_inner_adjacent_count(bottom_inner_point)
        if bottom_inner_count == 1 or bottom_inner_count == 2:
            self.new_bug_point_map[bottom_inner_point] = BUG

        right_inner_point = Point(3, 2)
        right_inner_count = self.get_right_inner_adjacent_count(right_inner_point)
        if right_inner_count == 1 or right_inner_count == 2:
            self.new_bug_point_map[right_inner_point] = BUG

    def get_top_outer_adjacent_count(self, point):
        down_char = self.bug_point_map.get(Point(point.x, point.y + 1))
        chars = [down_char]

        right_edge = True
        if point.x + 1 < 5:
            right_edge = False
            right_char = self.bug_point_map.get(Point(point.x + 1, point.y))
            chars.append(right_char)

        left_edge = True
        if point.x - 1 >= 0:
            left_edge = False
            left_char = self.bug_point_map.get(Point(point.x - 1, point.y))
            chars.append(left_char)

        parent_chars = []
        if self.parent is not None:
            parent_chars.append(self.parent.bug_point_map.get(Point(2, 1)))
            if right_edge:
                parent_chars.append(self.parent.bug_point_map.get(Point(3, 2)))
            if left_edge:
                parent_chars.append(self.parent.bug_point_map.get(Point(1, 2)))

        chars.extend(parent_chars)

        return len(list(filter(lambda _char: _char is not None, chars)))

    def get_bottom_outer_adjacent_count(self, point):
        up_char = self.bug_point_map.get(Point(point.x, point.y - 1))
        chars = [up_char]

        right_edge = True
        if point.x + 1 < 5:
            right_edge = False
            right_char = self.bug_point_map.get(Point(point.x + 1, point.y))
            chars.append(right_char)

        left_edge = True
        if point.x - 1 >= 0:
            left_edge = False
            left_char = self.bug_point_map.get(Point(point.x - 1, point.y))
            chars.append(left_char)

        parent_chars = []
        if self.parent is not None:
            parent_chars.append(self.parent.bug_point_map.get(Point(2, 3)))
            if right_edge:
                parent_chars.append(self.parent.bug_point_map.get(Point(3, 2)))
            if left_edge:
                parent_chars.append(self.parent.bug_point_map.get(Point(1, 2)))

        chars.extend(parent_chars)

        return len(list(filter(lambda _char: _char is not None, chars)))

    def get_left_outer_adjacent_count(self, point):
        right_char = self.bug_point_map.get(Point(point.x + 1, point.y))
        chars = [right_char]

        bottom_edge = True
        if point.y + 1 < 5:
            bottom_edge = False
            bottom_char = self.bug_point_map.get(Point(point.x, point.y + 1))
            chars.append(bottom_char)

        top_edge = True
        if point.y - 1 >= 0:
            top_edge = False
            top_char = self.bug_point_map.get(Point(point.x, point.y - 1))
            chars.append(top_char)

        parent_chars = []
        if self.parent is not None:
            parent_chars.append(self.parent.bug_point_map.get(Point(1, 2)))
            if bottom_edge:
                parent_chars.append(self.parent.bug_point_map.get(Point(2, 3)))
            if top_edge:
                parent_chars.append(self.parent.bug_point_map.get(Point(2, 1)))

        chars.extend(parent_chars)

        return len(list(filter(lambda _char: _char is not None, chars)))

    def get_right_outer_adjacent_count(self, point):
        left_char = self.bug_point_map.get(Point(point.x - 1, point.y))
        chars = [left_char]

        bottom_edge = True
        if point.y + 1 < 5:
            bottom_edge = False
            bottom_char = self.bug_point_map.get(Point(point.x, point.y + 1))
            chars.append(bottom_char)

        top_edge = True
        if point.y - 1 >= 0:
            top_edge = False
            top_char = self.bug_point_map.get(Point(point.x, point.y - 1))
            chars.append(top_char)

        parent_chars = []
        if self.parent is not None:
            parent_chars.append(self.parent.bug_point_map.get(Point(3, 2)))
            if bottom_edge:
                parent_chars.append(self.parent.bug_point_map.get(Point(2, 3)))
            if top_edge:
                parent_chars.append(self.parent.bug_point_map.get(Point(2, 1)))

        chars.extend(parent_chars)

        return len(list(filter(lambda _char: _char is not None, chars)))

    def process_outer_edge(self):
        top_edge_points = get_top_edge_points()
        for point in top_edge_points:
            adjacent_count = self.get_top_outer_adjacent_count(point)
            if adjacent_count == 1 or adjacent_count == 2:
                self.new_bug_point_map[point] = BUG

        bottom_edge_points = get_bottom_edge_points()
        for point in bottom_edge_points:
            adjacent_count = self.get_bottom_outer_adjacent_count(point)
            if adjacent_count == 1 or adjacent_count == 2:
                self.new_bug_point_map[point] = BUG

        left_edge_points = get_left_edge_points()
        for point in left_edge_points:
            adjacent_count = self.get_left_outer_adjacent_count(point)
            if adjacent_count == 1 or adjacent_count == 2:
                self.new_bug_point_map[point] = BUG

        right_edge_points = get_right_edge_points()
        for point in right_edge_points:
            adjacent_count = self.get_right_outer_adjacent_count(point)
            if adjacent_count == 1 or adjacent_count == 2:
                self.new_bug_point_map[point] = BUG

    def spawn_child(self):
        if self.child is not None:
            return

        bug_count = self.get_bug_count([Point(2, 1), Point(1, 2), Point(2, 3), Point(3, 2)])
        if bug_count > 0:
            print("spawned child")
            self.new_child = Layer()
            self.new_child.parent = self
            self.new_child.layer_number = self.layer_number + 1

            if self.bug_point_map.get(Point(2, 1)) is not None:
                self.new_child.bug_point_map[Point(0, 0)] = BUG
                self.new_child.bug_point_map[Point(1, 0)] = BUG
                self.new_child.bug_point_map[Point(2, 0)] = BUG
                self.new_child.bug_point_map[Point(3, 0)] = BUG
                self.new_child.bug_point_map[Point(4, 0)] = BUG

            if self.bug_point_map.get(Point(1, 2)) is not None:
                self.new_child.bug_point_map[Point(0, 0)] = BUG
                self.new_child.bug_point_map[Point(0, 1)] = BUG
                self.new_child.bug_point_map[Point(0, 2)] = BUG
                self.new_child.bug_point_map[Point(0, 3)] = BUG
                self.new_child.bug_point_map[Point(0, 4)] = BUG

            if self.bug_point_map.get(Point(2, 3)) is not None:
                self.new_child.bug_point_map[Point(0, 4)] = BUG
                self.new_child.bug_point_map[Point(1, 4)] = BUG
                self.new_child.bug_point_map[Point(2, 4)] = BUG
                self.new_child.bug_point_map[Point(3, 4)] = BUG
                self.new_child.bug_point_map[Point(4, 4)] = BUG

            if self.bug_point_map.get(Point(3, 2)) is not None:
                self.new_child.bug_point_map[Point(4, 0)] = BUG
                self.new_child.bug_point_map[Point(4, 1)] = BUG
                self.new_child.bug_point_map[Point(4, 2)] = BUG
                self.new_child.bug_point_map[Point(4, 3)] = BUG
                self.new_child.bug_point_map[Point(4, 4)] = BUG

    def spawn_parent(self):
        if self.parent is not None:
            return

        top_edge_bug_count = self.get_bug_count(get_top_edge_points())
        bottom_edge_bug_count = self.get_bug_count(get_bottom_edge_points())
        left_edge_bug_count = self.get_bug_count(get_left_edge_points())
        right_edge_bug_count = self.get_bug_count(get_right_edge_points())

        if top_edge_bug_count == 1 or top_edge_bug_count == 2 \
                or bottom_edge_bug_count == 1 or bottom_edge_bug_count == 2 \
                or left_edge_bug_count == 1 or left_edge_bug_count == 2 \
                or right_edge_bug_count == 1 or right_edge_bug_count == 2:
            print("spawned parent")
            self.new_parent = Layer()
            self.new_parent.child = self
            self.new_parent.layer_number = self.layer_number - 1

            if top_edge_bug_count == 1 or top_edge_bug_count == 2:
                self.new_parent.bug_point_map[Point(2, 1)] = BUG

            if bottom_edge_bug_count == 1 or bottom_edge_bug_count == 2:
                self.new_parent.bug_point_map[Point(2, 3)] = BUG

            if left_edge_bug_count == 1 or left_edge_bug_count == 2:
                self.new_parent.bug_point_map[Point(1, 2)] = BUG

            if right_edge_bug_count == 1 or right_edge_bug_count == 2:
                self.new_parent.bug_point_map[Point(3, 2)] = BUG

    def part_2_process(self):
        simple_points = [Point(1, 1), Point(3, 1), Point(1, 3), Point(3, 3)]
        for point in simple_points:
            adjacent_count = self.get_adjacent_count(point)
            if adjacent_count == 1 or adjacent_count == 2:
                self.new_bug_point_map[point] = BUG

        self.process_inner_edge()

        self.process_outer_edge()

        self.spawn_child()

        self.spawn_parent()

    def update_bug_point_map(self):
        self.bug_point_map = self.new_bug_point_map.copy()
        self.new_bug_point_map = {}

    def update_parent_and_child(self):
        if self.new_parent is not None:
            self.parent = self.new_parent
            self.new_parent = None
        if self.new_child is not None:
            self.child = self.new_child
            self.new_child = None

    def calculate_biodiversity(self):
        _biodiversity = 0
        power = 1
        for _y in range(0, 5):
            for _x in range(0, 5):
                if self.bug_point_map.get(Point(_x, _y)) == BUG:
                    _biodiversity += power
                power = power * 2
        return _biodiversity


def get_top_edge_points():
    return [Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0), Point(4, 0)]


def get_bottom_edge_points():
    return [Point(0, 4), Point(1, 4), Point(2, 4), Point(3, 4), Point(4, 4)]


def get_left_edge_points():
    return [Point(0, 0), Point(0, 1), Point(0, 2), Point(0, 3), Point(0, 4)]


def get_right_edge_points():
    return [Point(4, 0), Point(4, 1), Point(4, 2), Point(4, 3), Point(4, 4)]


def part1():
    def update_canvas():
        for _point in layer.bug_point_map.keys():
            graphics_panel.update_canvas(_point, "red")

    graphics_panel = GraphicsPanel.create_empty_panel(30, 30)
    graphics_panel.init_canvas()
    graphics_panel.paint_canvas()

    file_parser = FileParser("input.txt")

    layer = Layer()
    layer.bug_point_map = file_parser.read_points_map(BUG)
    seen_layouts = set()

    update_canvas()
    graphics_panel.paint_canvas()
    # time.sleep(2)

    while True:
        for y in range(0, 5):
            for x in range(0, 5):
                point = Point(x, y)
                adjacent_count = layer.get_adjacent_count(point)
                char = layer.bug_point_map.get(point)
                if char is not None:
                    if adjacent_count == 1:
                        layer.new_bug_point_map[point] = BUG
                else:
                    if adjacent_count == 1 or adjacent_count == 2:
                        layer.new_bug_point_map[point] = BUG

        layer.update_bug_point_map()

        graphics_panel.reset()
        update_canvas()
        graphics_panel.paint_canvas()

        biodiversity = layer.calculate_biodiversity()
        if biodiversity in seen_layouts:
            print(biodiversity)
            break
        seen_layouts.add(biodiversity)
        # time.sleep(2)

    input("press any key")


def part2():
    file_parser = FileParser("testinput.txt")

    top_layer = Layer()
    top_layer.bug_point_map = file_parser.read_points_map(BUG)
    minutes = 0

    while minutes < 10:
        layer = top_layer
        while layer is not None:
            layer.part_2_process()
            layer = layer.child

        layer = top_layer
        while layer is not None:
            old_child = layer.child
            layer.update_bug_point_map()
            layer.update_parent_and_child()
            layer = old_child

        if top_layer.parent is not None:
            top_layer = top_layer.parent
        minutes += 1
        print(minutes)

    bug_count = 0
    layer = top_layer
    while layer is not None:
        print(str(layer.layer_number) + ": " + str(layer.get_total_bug_count()))
        bug_count += layer.get_total_bug_count()
        layer = layer.child

    print(bug_count)


BUG = "#"

# part1()
part2()
