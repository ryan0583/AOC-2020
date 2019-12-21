from Utils.debug_tools import raise_
from Utils.graphics_panel import GraphicsPanel
from Utils.point import Point


class Droid:
    def __init__(self, path, point, direction, portals):
        self.path = list(path)
        self.point = point
        self.direction = direction
        self.portals = portals.copy()

    def clone(self, direction, point):
        return Droid(self.path, point, direction, self.portals)

    def attempt_move(self, maze_map, portal_map):
        def teleport():
            key = get_teleport_key(next_char, next_point, maze_map)
            if key is None:
                return
            if key in self.portals:
                return
            self.portals.add(key)
            if key == "ZZ":
                return
            if key == "LN":
                print("FOUND LN")
            portal_points = portal_map.get(key)
            key_point = None
            for portal_point in portal_points:
                if next_point not in portal_point:
                    key_point = next(iter(portal_point))
            if key_point is not None:
                space_point = find_space_point(key_point, maze_map)

                up_clone = self.clone(N, space_point)
                up_clone.path.append(space_point)
                droids_to_add.append(up_clone)
                down_clone = self.clone(S, space_point)
                down_clone.path.append(space_point)
                droids_to_add.append(down_clone)
                right_clone = self.clone(E, space_point)
                right_clone.path.append(space_point)
                droids_to_add.append(right_clone)
                left_clone = self.clone(W, space_point)
                left_clone.path.append(space_point)
                droids_to_add.append(left_clone)

        def can_move_to_space(_next_char):
            return _next_char == SPACE

        def can_teleport_on_next_space(_next_char):
            return _next_char.isupper()

        droids_to_add = []
        droid_to_remove = None

        next_point = get_next_point(self.direction, self.point)
        next_char = maze_map.get(next_point)
        if next_char is None or next_char == EMPTY:
            return droids_to_add, self

        can_move = can_move_to_space(next_char)

        if can_move:
            self.path.append(self.point)
            self.point = next_point
            can_turn_left = can_move_to_space(maze_map.get(get_next_point(turn_left(self.direction), self.point)))
            can_turn_right = can_move_to_space(maze_map.get(get_next_point(turn_right(self.direction), self.point)))

            if can_turn_left:
                droids_to_add.append(self.clone(turn_left(self.direction), self.point))

            if can_turn_right:
                droids_to_add.append(self.clone(turn_right(self.direction), self.point))
        elif can_teleport_on_next_space(next_char):
            droid_to_remove = self
            teleport()
        else:
            droid_to_remove = self

        return droids_to_add, droid_to_remove

    def __eq__(self, other):
        return self.path == other.path \
               and self.point == other.point \
               and self.direction == other.direction

    def __str__(self):
        return str(self.path) + str(self.point) + str(self.direction)

    def __hash__(self):
        return hash(str(self))


def find_space_point(key_point, maze_map):
    space_point = None
    if maze_map.get(move_up(key_point, 1)) == SPACE:
        space_point = move_up(key_point, 1)
    elif maze_map.get(move_up(key_point, 2)) == SPACE:
        space_point = move_up(key_point, 2)
    elif maze_map.get(move_down(key_point, 1)) == SPACE:
        space_point = move_down(key_point, 1)
    elif maze_map.get(move_down(key_point, 2)) == SPACE:
        space_point = move_down(key_point, 2)
    elif maze_map.get(move_left(key_point, 1)) == SPACE:
        space_point = move_left(key_point, 1)
    elif maze_map.get(move_left(key_point, 2)) == SPACE:
        space_point = move_left(key_point, 2)
    elif maze_map.get(move_right(key_point, 1)) == SPACE:
        space_point = move_right(key_point, 1)
    elif maze_map.get(move_right(key_point, 2)) == SPACE:
        space_point = move_right(key_point, 2)
    return space_point


def move_up(point, amount):
    return Point(point.x, point.y - amount)


def move_down(point, amount):
    return Point(point.x, point.y + amount)


def move_left(point, amount):
    return Point(point.x - amount, point.y)


def move_right(point, amount):
    return Point(point.x + amount, point.y)


def get_next_point(direction, current_point):
    direction_switcher = {
        N: lambda: Point(current_point.x, current_point.y - 1),
        S: lambda: Point(current_point.x, current_point.y + 1),
        W: lambda: Point(current_point.x - 1, current_point.y),
        E: lambda: Point(current_point.x + 1, current_point.y)
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


def map_color(char):
    if char == SPACE:
        return "black"
    if char == WALL:
        return "white"
    if char.isupper():
        return "yellow"


def get_teleport_key(char, point, maze_map):
    char2 = None
    point2 = None
    point2 = Point(point.x, point.y + 1)
    char2 = maze_map.get(point2)
    if char2 is None or not char2.isupper():
        point2 = Point(point.x, point.y - 1)
        char2 = maze_map.get(point2)
    if char2 is None or not char2.isupper():
        point2 = Point(point.x + 1, point.y)
        char2 = maze_map.get(point2)
    if char2 is None or not char2.isupper():
        point2 = Point(point.x - 1, point.y)
        char2 = maze_map.get(point2)

    if char2 is None:
        return None
    elif point2.x < point.x or point2.y < point.y:
        return char2 + char
    return char + char2


def part_one():
    def add_to_portal_map():
        point2 = None
        char2 = None
        if y + 1 < len(lines):
            point2 = Point(x, y + 1)
            chars2 = list(lines[y + 1])
            if x < len(chars2):
                if chars2[x].isupper():
                    char2 = chars2[x]
        if char2 is None and x + 1 < len(chars):
            point2 = Point(x + 1, y)
            if chars[x + 1].isupper():
                char2 = chars[x + 1]
        if char2 is not None:
            # print("found " + char + char2 + " at point " + str(point))
            point_list = portal_map.get(char + char2)
            if point_list is None:
                portal_map[char + char2] = [{point, point2}]
            else:
                point_list.append({point, point2})

    lines = open("input.txt", "r").read().splitlines()

    panel = GraphicsPanel.create_empty_panel(300, 300)
    panel.init_canvas()

    maze_map = {}
    portal_map = {}

    for y, line in enumerate(lines):
        chars = list(line)
        for x, char in enumerate(chars):
            point = Point(x, y)
            panel.update_canvas(point, map_color(char))
            maze_map[Point(x, y)] = char
            if char.isupper():
                add_to_portal_map()

    points = portal_map.get("AA")[0]
    for point in points:
        panel.update_canvas(point, "green")

    points = portal_map.get("ZZ")[0]
    for point in points:
        panel.update_canvas(point, "red")

    panel.paint_canvas()

    start_point = find_space_point(next(iter(portal_map.get("AA")[0])), maze_map)

    droids = [Droid([], start_point, N, set("AA")),
              Droid([], start_point, S, set("AA")),
              Droid([], start_point, E, set("AA")),
              Droid([], start_point, W, set("AA"))]

    winning_droid = None

    while winning_droid is None:
        # print("Droid count: " + str(len(droids)))
        droids_to_add = []
        droids_to_remove = set()
        for droid in droids:
            panel.update_canvas(droid.point, "black")
            add, remove = droid.attempt_move(maze_map, portal_map)
            panel.update_canvas(droid.point, "blue")
            panel.paint_canvas()
            if "ZZ" in droid.portals:
                winning_droid = droid
                break
            droids_to_add.extend(add)
            if remove is not None:
                droids_to_remove.add(remove)
        droids.extend(droids_to_add)
        droids = list(filter(lambda this_droid: this_droid not in droids_to_remove, droids))

    for point in winning_droid.path:
        print(point)

    print(len(winning_droid.path))
    input("press any key")


N = "N"
S = "S"
W = "W"
E = "E"

WALL = "#"
SPACE = "."
EMPTY = " "

part_one()
