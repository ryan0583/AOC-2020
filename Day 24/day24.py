from Utils.file_reader import read_lines
from Utils.point3d import Point3d


def get_initial_state():
    black_tiles = set()
    lines = read_lines('Input.txt')

    for line in lines:
        char_index = 0
        x = 0
        y = 0
        z = 0
        while char_index < len(line):
            char = line[char_index]
            char_index += 1
            direction = char
            if char == 'n' or char == 's':
                direction += line[char_index]
                char_index += 1

            if direction == 'e':
                x += 1
                y -= 1
            elif direction == 'se':
                z += 1
                y -= 1
            elif direction == 'sw':
                z += 1
                x -= 1
            elif direction == 'w':
                y += 1
                x -= 1
            elif direction == 'nw':
                y += 1
                z -= 1
            elif direction == 'ne':
                x += 1
                z -= 1

        point = Point3d(x, y, z)
        if point in black_tiles:
            black_tiles.remove(point)
        else:
            black_tiles.add(point)

    return black_tiles


def part1():
    print(len(get_initial_state()))


def get_neighbour_tiles(tile):
    return {
        Point3d(tile.x + 1, tile.y - 1, tile.z),
        Point3d(tile.x, tile.y - 1, tile.z + 1),
        Point3d(tile.x - 1, tile.y, tile.z + 1),
        Point3d(tile.x - 1, tile.y + 1, tile.z),
        Point3d(tile.x, tile.y + 1, tile.z - 1),
        Point3d(tile.x + 1, tile.y, tile.z - 1)}


def perform_day_flip(black_tiles):
    new_black_tiles = []

    min_x = min([point.x for point in black_tiles]) - 1
    max_x = max([point.x for point in black_tiles]) + 1
    min_y = min([point.y for point in black_tiles]) - 1
    max_y = max([point.y for point in black_tiles]) + 1
    min_z = min([point.z for point in black_tiles]) - 1
    max_z = max([point.z for point in black_tiles]) + 1

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            for z in range(min_z, max_z + 1):
                if x + y + z != 0:
                    continue

                point_to_check = Point3d(x, y, z)
                neighbours = get_neighbour_tiles(point_to_check)
                black_neighbours = black_tiles.intersection(neighbours)
                if len(black_neighbours) == 2:
                    new_black_tiles.append(point_to_check)
                elif point_to_check in black_tiles and len(black_neighbours) == 1:
                    new_black_tiles.append(point_to_check)

    return set(new_black_tiles)


def part2():
    black_tiles = get_initial_state()

    for i in range(0, 100):
        print('DAY: ' + str(i + 1))
        black_tiles = perform_day_flip(black_tiles)

    print(len(black_tiles))


part1()
part2()
