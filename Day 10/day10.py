from collections import OrderedDict
from math import atan, degrees

from Utils.file_parser import FileParser
from Utils.debug_tools import raise_


class Asteroid:
    def __init__(self, point):
        self.point = point
        self.seen_asteroids = {}

    def get_x(self):
        return self.point.x

    def get_y(self):
        return self.point.y

    def get_seen_count(self):
        return len(self.seen_asteroids)

    def __str__(self):
        return str(self.point) + ": " + str(len(self.seen_asteroids))


def find_asteroids():
    file_parser = FileParser("input.txt")
    return list(map(Asteroid, file_parser.read_points("#")))


def find_angle(x, y):
    def find_vertical_angle():
        return 180 if y > 0 else 0

    def find_horiz_angle():
        return 90 if x > 0 else 270

    def get_up_angle():
        return degrees(atan(abs(y) / abs(x)))

    def get_down_angle():
        return degrees(atan(abs(x) / abs(y)))

    def get_quadrant():
        if y < 0 < x:
            return TOP_RIGHT
        if y > 0 and 0 < x:
            return BOTTOM_RIGHT
        if y > 0 > x:
            return BOTTOM_LEFT
        if y < 0 and 0 > x:
            return TOP_LEFT

    if x == 0:
        return find_vertical_angle()
    elif y == 0:
        return find_horiz_angle()
    else:
        angle = get_up_angle() if y < 0 else get_down_angle()

        quadrant_switcher = {
            TOP_RIGHT: lambda: angle,
            BOTTOM_RIGHT: lambda: 180 - angle,
            BOTTOM_LEFT: lambda: angle + 180,
            TOP_LEFT: lambda: angle + 270
        }

        return quadrant_switcher.get(get_quadrant(), lambda: raise_(Exception("Invalid quadrant")))()


def find_seen_asteroids(asteroid, asteroids):
    def add_if_can_see():
        def replace_if_closer():
            seen_rel_x = seen_asteroid.get_x() - x
            seen_rel_y = seen_asteroid.get_y() - y
            is_closer = abs(other_rel_x) + abs(other_rel_y) < abs(seen_rel_x) + abs(seen_rel_y)
            if is_closer:
                asteroid.seen_asteroids[key] = other_asteroid

        other_rel_x = other_x - x
        other_rel_y = other_y - y

        key = find_angle(other_rel_x, other_rel_y)
        seen_asteroid = asteroid.seen_asteroids.get(key)
        if seen_asteroid is None:
            asteroid.seen_asteroids[key] = other_asteroid
        else:
            replace_if_closer()

    x = asteroid.get_x()
    y = asteroid.get_y()

    for other_asteroid in asteroids:
        other_x = other_asteroid.get_x()
        other_y = other_asteroid.get_y()
        if other_x != x or other_y != y:
            add_if_can_see()

    return OrderedDict(sorted(asteroid.seen_asteroids.items()))


def create_asteroids():
    asteroids = find_asteroids()
    for asteroid in asteroids:
        find_seen_asteroids(asteroid, asteroids)
    return asteroids


def find_best_asteroid(asteroids):
    max_seen_count = 0
    best_asteroid = None
    for asteroid in asteroids:
        seen_count = asteroid.get_seen_count()
        if seen_count > max_seen_count:
            max_seen_count = seen_count
            best_asteroid = asteroid
    return best_asteroid


def part1():
    return find_best_asteroid(create_asteroids())


def part2():
    asteroids = create_asteroids()
    source_asteroid = find_best_asteroid(asteroids)

    ordered_seen_asteroids = OrderedDict(sorted(source_asteroid.seen_asteroids.items()))
    killed_asteroids = []

    while len(killed_asteroids) < 200:
        for asteroid in ordered_seen_asteroids.values():
            asteroids.remove(asteroid)
            killed_asteroids.append(asteroid)

        source_asteroid.seen_asteroids = {}
        ordered_seen_asteroids = find_seen_asteroids(source_asteroid, asteroids)

    return killed_asteroids[199]


TOP_RIGHT = "TR"
BOTTOM_RIGHT = "BR"
BOTTOM_LEFT = "BL"
TOP_LEFT = "TL"
