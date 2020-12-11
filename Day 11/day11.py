from Utils.file_parser import FileParser
from Utils.point import Point


def print_points(points):
    for point in points:
        print(point)


def get_adjacent(point, other_points):
    adjacent = []
    for x in range(point.x - 1, point.x + 2):
        for y in range(point.y - 1, point.y + 2):
            point_to_check = Point(x, y)
            if point_to_check == point:
                continue
            if point_to_check in other_points:
                adjacent.append(point_to_check)
    return adjacent


def part1():
    def get_permanent():
        permanent = []
        for seat in seats:
            if len(get_adjacent(seat, seats)) < 4:
                permanent.append(seat)
        return set(permanent)

    def next_round():
        new = []
        for seat in seats:
            if seat in permanently_occupied:
                new.append(seat)

            adjacent = get_adjacent(seat, current_occupied)
            if seat not in current_occupied and len(adjacent) == 0:
                new.append(seat)
            elif seat in current_occupied and len(adjacent) < 4:
                new.append(seat)

        return set(new)

    parser = FileParser("Input.txt")
    seats = set(parser.read_points('L'))

    permanently_occupied = get_permanent()
    current_occupied = set(seats)

    while True:
        print('...................')
        new_occupied = next_round()
        if new_occupied == current_occupied:
            break
        else:
            current_occupied = new_occupied

    return len(current_occupied)


print(part1())
