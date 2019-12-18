from Utils.debug_tools import raise_
from Utils.graphics_panel import GraphicsPanel
from Utils.point import Point


class Droid:
    def __init__(self, path, point, direction, keys, doors):
        self.path = list(path)
        self.point = point
        self.direction = direction
        self.keys = keys.copy()
        self.mykeys = set()
        self.doors = doors.copy()
        self.mypath = []
        self.color = droid_color

    def clone(self, direction):
        return Droid(self.path, self.point, direction, self.keys, self.doors)

    def clone_reverse(self):
        return self.clone(turn_right(turn_right(self.direction)))

    def attempt_move(self, maze_map):
        def can_move_to_space(_next_char):
            return _next_char == SPACE or _next_char.islower() or found_door_with_key

        droids_to_add = []
        droid_to_remove = None

        next_point = get_next_point(self.direction, self.point)
        next_char = maze_map[next_point]
        found_door_with_key = next_char.isupper() and next_char.lower() in self.keys
        can_move = can_move_to_space(next_char)

        global droid_color

        if can_move:
            self.point = next_point
            self.path.append(self.point)
            self.mypath.append(self.point)
            can_turn_left = can_move_to_space(maze_map[get_next_point(turn_left(self.direction), self.point)])
            can_turn_right = can_move_to_space(maze_map[get_next_point(turn_right(self.direction), self.point)])


            if can_turn_left:
                droids_to_add.append(self.clone(turn_left(self.direction)))


            if can_turn_right:
                droids_to_add.append(self.clone(turn_right(self.direction)))

            if found_door_with_key and next_char not in self.doors:
                self.doors.add(next_char)
                if self.color == "green":
                    droid_color = "blue"
                else:
                    droid_color = "green"
                if len(self.mykeys) > 0:
                    droids_to_add.append(self.clone_reverse())
            elif next_char.islower() and next_char not in self.keys:
                self.keys.add(next_char)
                self.mykeys.add(next_char)
                if self.color == "green":
                    droid_color = "blue"
                else:
                    droid_color = "green"
                if len(self.mykeys) > 0:
                    droids_to_add.append(self.clone_reverse())
        else:
            droid_to_remove = self
            if not next_char.isupper():
                can_turn_left = can_move_to_space(maze_map[get_next_point(turn_left(self.direction), self.point)])
                can_turn_right = can_move_to_space(maze_map[get_next_point(turn_right(self.direction), self.point)])
                if not can_turn_left and not can_turn_right and len(self.mypath) > 0 and len(self.mykeys) > 0:
                    if self.color == "green":
                        droid_color = "blue"
                    else:
                        droid_color = "green"

                    droids_to_add.append(self.clone_reverse())

        return droids_to_add, droid_to_remove

    def __eq__(self, other):
        return self.path == other.path \
               and self.point == other.point \
               and self.direction == other.direction \
               and self.keys == other.keys \
               and self.doors == other.doors \
               and self.mypath == other.mypath

    def __str__(self):
        return str(self.path) + str(self.point) + str(self.direction) + str(self.keys) + str(self.doors) + str(
            self.mypath)

    def __hash__(self):
        return hash(str(self))


class DroidMapKey:
    def __init__(self, droid, point):
        self.direction = droid.direction
        self.keys = droid.keys
        self.point = point

    def __eq__(self, other):
        return self.point == other.point \
               and self.direction == other.direction \
               and self.keys == other.keys

    def __str__(self):
        return str(self.point) + str(self.direction) + str(self.keys)

    def __hash__(self):
        return hash(str(self))


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
    if char == ENTRY:
        return "blue"
    if char.islower():
        return "yellow"
    if char.isupper():
        return "red"


def all_keys_found(droids, key_count):
    droids_found_all_keys = []
    for droid in droids:
        if len(droid.keys) >= key_count:
            droids_found_all_keys.append(droid)
    return droids_found_all_keys


def hash_droids(droids):
    droid_map = {}
    for droid in droids:
        key = DroidMapKey(droid, droid.point)
        droid_map[key] = droid

    return droid_map


def part1():
    lines = open("testinput.txt", "r").read().splitlines()

    panel = GraphicsPanel.create_empty_panel(100, 100)
    panel.init_canvas()

    maze_map = {}
    start_point = None
    key_count = 0

    for y, line in enumerate(lines):
        chars = list(line)
        for x, char in enumerate(chars):
            point = Point(x, y)
            if char == ENTRY:
                start_point = point
                char = SPACE
            if char.islower():
                key_count += 1
            panel.update_canvas(point, map_color(char))
            maze_map[Point(x, y)] = char

    panel.paint_canvas()

    droids = [Droid([], start_point, N, set(), set()),
              Droid([], start_point, S, set(), set()),
              Droid([], start_point, E, set(), set()),
              Droid([], start_point, W, set(), set())]

    droid_map = hash_droids(droids)

    while len(all_keys_found(droids, key_count)) == 0:
        print(len(droids))
        droids_to_add = []
        droids_to_remove = set()
        for droid in droids:
            add, remove = droid.attempt_move(maze_map)
            panel.update_canvas(droid.point, droid.color)
            panel.paint_canvas()
            droids_to_add.extend(add)
            if remove is not None:
                droids_to_remove.add(remove)
        droids.extend(droids_to_add)
        droids = list(filter(lambda this_droid: this_droid not in droids_to_remove, droids))
        droids = list(filter(
            lambda this_droid: droid_map.get(
                DroidMapKey(this_droid, get_next_point(this_droid.direction, this_droid.point))) is None,
            droids))
        droid_map.update(hash_droids(droids))

    panel.paint_canvas()
    droids_found_keys = all_keys_found(droids, key_count)
    min_path = min(list(map(lambda this_droid: len(this_droid.path), droids_found_keys)))
    print(min_path)
    # input("press any key")


N = "N"
S = "S"
W = "W"
E = "E"

WALL = "#"
SPACE = "."
ENTRY = "@"

droid_color = "green"

part1()
