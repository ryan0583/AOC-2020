from math import atan, degrees


class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.seen_asteroids = []

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
    return degrees(atan(y / x)) if y > 0 else degrees(atan(x / y))


def find_seen_asteroids(asteroid, asteroids):
    def can_see():
        other_rel_x = other_asteroid.x - asteroid.x
        other_rel_y = other_asteroid.y - asteroid.y

        blocked = False
        for seen_asteroid in asteroid.seen_asteroids:
            seen_rel_x = seen_asteroid.x - asteroid.x
            seen_rel_y = seen_asteroid.y - asteroid.y

            same_row = other_rel_y == 0 and seen_rel_y == 0
            same_col = other_rel_x == 0 and seen_rel_x == 0
            same_x_dir = (other_rel_x > 0) == (seen_rel_x > 0)
            same_y_dir = (other_rel_y > 0) == (seen_rel_y > 0)

            if (same_row and same_x_dir) or (same_col and same_y_dir):
                blocked = True
            elif other_rel_y != 0 and other_rel_x != 0 and seen_rel_y != 0 and seen_rel_x != 0:
                same_angle = find_angle(other_rel_x, other_rel_y) == find_angle(seen_rel_x, seen_rel_y)
                if same_x_dir and same_y_dir and same_angle:
                    blocked = True

            if blocked:
                # print(str(asteroid) + " can't see " + str(other_asteroid) + ". Blocked by " + str(seen_asteroid))

                is_closer = other_rel_x + other_rel_y < seen_rel_x + seen_rel_y
                if is_closer:
                    asteroid.seen_asteroids.remove(seen_asteroid)
                    asteroid.seen_asteroids.append(other_asteroid)
                break

        return not blocked

    for other_asteroid in asteroids:
        if other_asteroid.x == asteroid.x and other_asteroid.y == asteroid.y:
            continue
        if can_see():
            asteroid.seen_asteroids.append(other_asteroid)


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
    # lines = open("part2test.txt", "r").read().splitlines()
    asteroids = find_asteroids(lines)
    for i, asteroid in enumerate(asteroids):
        find_seen_asteroids(asteroid, asteroids)
        print("done asteroid " + str(i))

    source_asteroid = find_best_asteroid(asteroids)

    print(source_asteroid)

    rotation_increment = get_rotation_increment(asteroids)

    print(rotation_increment)

    vapourised = []
    rotation = 0
    up = True
    right = True

    while len(vapourised) < 200:
        angle = rotation % 45
        print(up)
        print(right)
        print(angle)
        target_asteroids = find_asteroids_on_path(source_asteroid.seen_asteroids, source_asteroid, up, right, angle)
        if len(target_asteroids) > 0:
            print("VAPOURISE!!")
            vapourised.append(target_asteroids[0])
            source_asteroid.seen_asteroids.remove(target_asteroids[0])
            add_next_asteroid(source_asteroid, asteroids, vapourised, up, right, angle)

        rotation += rotation_increment
        if rotation > 360:
            rotation = rotation % 360
            right = True
        elif rotation > 270:
            up = True
        elif rotation > 180:
            right = False
        elif rotation > 45:
            up = False

    print(vapourised[len(vapourised)])


# print(part1())
part2()
