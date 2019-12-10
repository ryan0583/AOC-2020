from math import atan

class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.seen_asteroids = []

    def get_seen_count(self):
        return len(self.seen_asteroids)

    def __str__(self):
        return str(self.x) + ", " + str(self.y) + ": " + str(len(self.seen_asteroids))

def find_asteroids():
    _asteroids = []
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                _asteroids.append(Asteroid(x, y))
    return _asteroids


def find_seen_asteroids():
    def can_see():
        def find_angle(x, y):
            if y > 0:
                return atan(y/x) if x != 0 else 0
            return atan(x/y) if y != 0 else 0

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


def find_best_asteroid():
    max_seen_count = 0
    best_asteroid = None
    for _asteroid in asteroids:
        seen_count = _asteroid.get_seen_count()
        if seen_count > max_seen_count:
            max_seen_count = seen_count
            best_asteroid = _asteroid
    return best_asteroid


lines = open("input.txt", "r").read().splitlines()
# lines = open("testinput.txt", "r").read().splitlines()
asteroids = find_asteroids()
for asteroid in asteroids:
    find_seen_asteroids()
    # print(asteroid)

print(find_best_asteroid())
