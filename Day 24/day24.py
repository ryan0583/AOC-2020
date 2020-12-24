from Utils.file_reader import read_lines
from Utils.point import Point


def get_initial_state():
    black_tiles = set()
    lines = read_lines('Input.txt')

    for line in lines:
        char_index = 0
        x = 0
        y = 0
        while char_index < len(line):
            char = line[char_index]
            char_index += 1
            direction = char
            if char == 'n' or char == 's':
                direction += line[char_index]
                char_index += 1

            if direction == 'e':
                x += 2
            elif direction == 'se':
                x += 1
                y -= 1
            elif direction == 'sw':
                x -= 1
                y -= 1
            elif direction == 'w':
                x -= 2
            elif direction == 'nw':
                x -= 1
                y += 1
            elif direction == 'ne':
                x += 1
                y += 1

        point = Point(x, y)
        if point in black_tiles:
            black_tiles.remove(point)
        else:
            black_tiles.add(point)

    return black_tiles


def part1():
    print(len(get_initial_state()))


def get_neighbour_tiles(tile):
    return {
        Point(tile.x + 2, tile.y),
        Point(tile.x + 1, tile.y - 1),
        Point(tile.x - 1, tile.y - 1),
        Point(tile.x - 2, tile.y),
        Point(tile.x - 1, tile.y + 1),
        Point(tile.x + 1, tile.y + 1)}


def perform_day_flip(black_tiles):
    new_black_tiles = []

    min_x = min([point.x for point in black_tiles]) - 2
    max_x = max([point.x for point in black_tiles]) + 2
    min_y = min([point.y for point in black_tiles]) - 2
    max_y = max([point.y for point in black_tiles]) + 2

    points = [Point(x, y)
              for x in range(min_x, max_x + 1)
              for y in range(min_y, max_y + 1)
              if (abs(x) + abs(y)) % 2 == 0]

    for point_to_check in points:
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

    print(len(black_tiles))


part1()
part2()
