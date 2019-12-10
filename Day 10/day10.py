from collections import OrderedDict
from math import atan, degrees


class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.seen_asteroids = {}

    def get_seen_count(self):
        return len(self.seen_asteroids)

    def __str__(self):
        return str(self.x) + ", " + str(self.y) + ": " + str(len(self.seen_asteroids))


def find_asteroids(lines):
    asteroids = []
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                asteroids.append(Asteroid(x, y))
    return asteroids


def find_angle(x, y):
    if x == 0:
        angle = 0
        if y > 0:
            angle = 180
    elif y == 0:
        angle = 90
        if x < 0:
            angle = 270
    else:
        angle = degrees(atan(abs(y) / abs(x))) if y < 0 else degrees(atan(abs(x) / abs(y)))

        if y > 0 and 0 < x:
            angle = 180 - angle
        elif x < 0 < y:
            angle += 180
        elif x < 0 and 0 > y:
            angle += 270

    return angle


def find_seen_asteroids(asteroid, asteroids):
    def add_if_can_see():
        def replace_if_closer():
            seen_rel_x = seen_asteroid.x - asteroid.x
            seen_rel_y = seen_asteroid.y - asteroid.y
            is_closer = abs(other_rel_x) + abs(other_rel_y) < abs(seen_rel_x) + abs(seen_rel_y)
            if is_closer:
                asteroid.seen_asteroids[key] = other_asteroid

        other_rel_x = other_asteroid.x - asteroid.x
        other_rel_y = other_asteroid.y - asteroid.y

        key = find_angle(other_rel_x, other_rel_y)
        seen_asteroid = asteroid.seen_asteroids.get(key)
        if seen_asteroid is not None:
            replace_if_closer()
        else:
            asteroid.seen_asteroids[key] = other_asteroid

    for other_asteroid in asteroids:
        if other_asteroid.x == asteroid.x and other_asteroid.y == asteroid.y:
            continue
        add_if_can_see()
    return OrderedDict(sorted(asteroid.seen_asteroids.items()))


def create_asteroids():
    lines = open("input.txt", "r").read().splitlines()
    asteroids = find_asteroids(lines)
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

    ordered_seen_asteroids = find_seen_asteroids(source_asteroid, asteroids)
    killed_asteroids = []

    while len(killed_asteroids) < 200:
        for asteroid in ordered_seen_asteroids.values():
            asteroids.remove(asteroid)
            killed_asteroids.append(asteroid)

        source_asteroid.seen_asteroids = {}
        ordered_seen_asteroids = find_seen_asteroids(source_asteroid, asteroids)

    return killed_asteroids[199]
