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
        if y < 0:
            angle = 180
    elif y == 0:
        angle = 90
        if x < 0:
            angle = 270
    else:
        angle = degrees(atan(abs(y) / abs(x))) if y > 0 else degrees(atan(abs(x) / abs(y)))

        if y < 0 < x:
            angle = 180 - angle
        elif y < 0 and x < 0:
            angle += 180
        elif x < 0 < y:
            angle += 270

    return angle


def find_seen_asteroids(asteroid, asteroids):
    def add_if_can_see():
        other_rel_x = other_asteroid.x - asteroid.x
        other_rel_y = other_asteroid.y - asteroid.y

        key = find_angle(other_rel_x, other_rel_y)
        seen_asteroid = asteroid.seen_asteroids.get(key)
        if seen_asteroid is not None:
            # print(str(asteroid) + " can't see " + str(other_asteroid) + ". Blocked by " + str(seen_asteroid))
            seen_rel_x = seen_asteroid.x - asteroid.x
            seen_rel_y = seen_asteroid.y - asteroid.y
            is_closer = other_rel_x + other_rel_y < seen_rel_x + seen_rel_y
            if is_closer:
                asteroid.seen_asteroids[key] = other_asteroid
        else:
            asteroid.seen_asteroids[key] = other_asteroid

    for other_asteroid in asteroids:
        if other_asteroid.x == asteroid.x and other_asteroid.y == asteroid.y:
            continue
        add_if_can_see()

    print(asteroid)


def find_best_asteroid(asteroids):
    max_seen_count = 0
    best_asteroid = None
    for asteroid in asteroids:
        seen_count = asteroid.get_seen_count()
        if seen_count > max_seen_count:
            max_seen_count = seen_count
            best_asteroid = asteroid
    return best_asteroid


def get_rotation_increment(asteroids):
    x_positions = list(map(lambda asteroid: asteroid.x, asteroids))
    y_positions = list(map(lambda asteroid: asteroid.y, asteroids))
    min_x = min(x_positions)
    max_x = max(x_positions)
    min_y = min(y_positions)
    max_y = max(y_positions)

    return degrees(min(atan(1 / (max_x - min_x)), atan(1 / (max_y - min_y))))


def find_asteroids_on_path(asteroids, source_asteroid, up, right, angle):
    on_path = []
    for asteroid in asteroids:
        y_dist = asteroid.y - source_asteroid.y
        x_dist = asteroid.x - source_asteroid.x
        asteroid_up = y_dist > 0
        asteroid_right = x_dist > 0
        asteroid_angle = find_angle(x_dist, y_dist) if x_dist != 0 and y_dist != 0 else 0
        if up == asteroid_up and right == asteroid_right and asteroid_angle == angle:
            on_path.append(asteroid)
    return on_path


def find_closest(source_asteroid, asteroids):
    min_dist = None
    closest_asteroid = None

    for asteroid in asteroids:
        dist = abs(asteroid.x - source_asteroid.x) + abs(asteroid.y - source_asteroid.y)
        if min_dist is None or dist < min_dist:
            min_dist = dist
            closest_asteroid = asteroid

    return closest_asteroid


def add_next_asteroid(source_asteroid, all_asteroids, vapourised, up, right, angle):
    asteroids_on_path = find_asteroids_on_path(list(set(all_asteroids) - set(vapourised)), source_asteroid, up, right,
                                               angle)
    source_asteroid.seen_asteroids.append(find_closest(source_asteroid, asteroids_on_path))


def part1():
    lines = open("input.txt", "r").read().splitlines()
    # lines = open("testinput.txt", "r").read().splitlines()
    asteroids = find_asteroids(lines)
    for asteroid in asteroids:
        find_seen_asteroids(asteroid, asteroids)
    return find_best_asteroid(asteroids)


def part2():
    lines = open("input.txt", "r").read().splitlines()
    source_key = "26, 36"
    # lines = open("part2test.txt", "r").read().splitlines()
    asteroids = find_asteroids(lines)
    asteroid_positions = list(map(lambda asteroid: (str(asteroid.x) + ", " + str(asteroid.y), asteroid), asteroids))
    asteroid_pos_map = {k: v for (k, v) in asteroid_positions}

    source_asteroid = asteroid_pos_map.get(source_key)
    find_seen_asteroids(source_asteroid, asteroids)
    # print(source_asteroid)
    seen_asteroid_angles = list(
        map(lambda asteroid: (find_angle(asteroid.x - source_asteroid.x, asteroid.y - source_asteroid.y), asteroid),
            source_asteroid.seen_asteroids))

    asteroid_angle_map = {k: v for (k, v) in seen_asteroid_angles}
    print(asteroid_angle_map)

    #
    # print(source_asteroid)
    #
    # rotation_increment = get_rotation_increment(asteroids)
    #
    # print(rotation_increment)
    #
    # vapourised = []
    # rotation = 0
    # up = True
    # right = True
    #
    # while len(vapourised) < 200:
    #     angle = rotation % 45
    #     print(up)
    #     print(right)
    #     print(angle)
    #     target_asteroids = find_asteroids_on_path(source_asteroid.seen_asteroids, source_asteroid, up, right, angle)
    #     if len(target_asteroids) > 0:
    #         print("VAPOURISE!!")
    #         vapourised.append(target_asteroids[0])
    #         source_asteroid.seen_asteroids.remove(target_asteroids[0])
    #         add_next_asteroid(source_asteroid, asteroids, vapourised, up, right, angle)
    #
    #     rotation += rotation_increment
    #     if rotation > 360:
    #         rotation = rotation % 360
    #         right = True
    #     elif rotation > 270:
    #         up = True
    #     elif rotation > 180:
    #         right = False
    #     elif rotation > 45:
    #         up = False
    #
    # print(vapourised[len(vapourised)])

# print(part1())
# part2()
