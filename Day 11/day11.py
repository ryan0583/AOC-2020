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


def get_visible(point, other_points):
    def append(distance_point_map):
        if len(distance_point_map) > 0:
            visible.append(distance_point_map[min(distance_point_map.keys())])

    visible = []
    other_points = [other_point for other_point in other_points if other_point != point]

    horizontal = [horiz for horiz in other_points if horiz.y == point.y]
    vertical = [vert for vert in other_points if vert.x == point.x]
    diagonal_r = [diag_r for diag_r in other_points if
                  (diag_r.x - point.x) != 0 and float(float(diag_r.y - point.y) / float(diag_r.x - point.x)) == 1]
    diagonal_l = [diag_l for diag_l in other_points if
                  (diag_l.x - point.x) != 0 and float(float(diag_l.y - point.y) / float(diag_l.x - point.x)) == -1]

    append({next_point.x - point.x: next_point for next_point in horizontal if next_point.x - point.x > 0})
    append({point.x - next_point.x: next_point for next_point in horizontal if point.x - next_point.x > 0})

    append({next_point.y - point.y: next_point for next_point in vertical if next_point.y - point.y > 0})
    append({point.y - next_point.y: next_point for next_point in vertical if point.y - next_point.y > 0})

    append({(next_point.x - point.x) + (next_point.y - point.y): next_point
            for next_point in diagonal_r
            if next_point.x - point.x > 0
            and next_point.y - point.y > 0})

    append({(point.x - next_point.x) + (point.y - next_point.y): next_point
            for next_point in diagonal_r
            if point.x - next_point.x > 0
            and point.y - next_point.y > 0})

    append({(point.x - next_point.x) + (next_point.y - point.y): next_point
            for next_point in diagonal_l
            if point.x - next_point.x > 0
            and next_point.y - point.y > 0})

    append({(next_point.x - point.x) + (point.y - next_point.y): next_point
            for next_point in diagonal_l
            if next_point.x - point.x > 0
            and point.y - next_point.y > 0})

    return set(visible)


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


def part2():
    def get_visible_map():
        return {seat: get_visible(seat, seats) for seat in seats}

    def next_round():
        new = []
        for seat in seats:
            visible_occupied = set.intersection(visible[seat], current_occupied)
            if seat not in current_occupied and len(visible_occupied) == 0:
                new.append(seat)
            elif seat in current_occupied and len(visible_occupied) < 5:
                new.append(seat)

        return set(new)

    parser = FileParser("Input.txt")
    seats = set(parser.read_points('L'))

    visible = get_visible_map()
    current_occupied = set(seats)

    while True:
        new_occupied = next_round()
        if new_occupied == current_occupied:
            break
        else:
            current_occupied = new_occupied

    return len(current_occupied)


print(part1())
print(part2())
