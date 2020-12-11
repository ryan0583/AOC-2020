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
    def get_adjacent_map():
        return {seat: get_adjacent(seat, seats) for seat in seats}

    def get_permanent():
        permanent = []
        for seat in seats:
            if len(adjacent_map[seat]) < 4:
                permanent.append(seat)
        return set(permanent)

    def next_round():
        new = []
        for seat in seats:
            if seat in permanently_occupied:
                new.append(seat)

            adjacent_occupied = set.intersection(current_occupied, adjacent_map[seat])
            if seat not in current_occupied and len(adjacent_occupied) == 0:
                new.append(seat)
            elif seat in current_occupied and len(adjacent_occupied) < 4:
                new.append(seat)

        return set(new)

    parser = FileParser("Input.txt")
    seats = set(parser.read_points('L'))

    adjacent_map = get_adjacent_map()
    permanently_occupied = get_permanent()
    current_occupied = set(seats)

    round = 1
    while True:
        print(round)
        new_occupied = next_round()
        if new_occupied == current_occupied:
            break
        else:
            current_occupied = new_occupied
        round += 1

    print("====================")
    return len(current_occupied)


def part2():
    def populate_visibles():
        def process(next_seat, x, y):
            this_point = Point(x, y)
            if this_point in seats:
                if next_seat is None:
                    return this_point
                else:
                    visible[next_seat].add(this_point)
                    visible[this_point].add(next_seat)
                    return this_point
            return next_seat

        def process_vertical():
            for y in range(0, xdim):
                next_seat = None
                for x in range(0, xdim):
                    next_seat = process(next_seat, x, y)

        def process_horizontal():
            for x in range(0, xdim):
                next_seat = None
                for y in range(0, ydim):
                    next_seat = process(next_seat, x, y)

        def process_right_diagonal():
            start_x = xdim - 1
            x = start_x
            y = 0
            next_seat = None
            while start_x != -ydim:
                next_seat = process(next_seat, x, y)
                x += 1
                y += 1
                if x == xdim:
                    next_seat = None
                    start_x -= 1
                    x = start_x
                    y = 0

        def process_left_diagonal():
            start_x = 0
            x = start_x
            y = 0
            next_seat = None
            while start_x != xdim + ydim:
                next_seat = process(next_seat, x, y)
                x -= 1
                y += 1
                if x == -1:
                    next_seat = None
                    start_x += 1
                    x = start_x
                    y = 0

        process_horizontal()
        process_vertical()
        process_left_diagonal()
        process_right_diagonal()

    def next_round():
        new = []
        for seat in seats:
            visible_occupied = set.intersection(current_occupied, visible[seat])
            if seat not in current_occupied and len(visible_occupied) == 0:
                new.append(seat)
            elif seat in current_occupied and len(visible_occupied) < 5:
                new.append(seat)

        return set(new)

    parser = FileParser("Input.txt")
    seats = set(parser.read_points('L'))
    xdim = max([seat.x for seat in seats]) + 1
    ydim = max([seat.y for seat in seats]) + 1

    visible = {seat: set() for seat in seats}
    populate_visibles()
    current_occupied = set(seats)

    round = 1
    while True:
        print(round)
        new_occupied = next_round()
        if new_occupied == current_occupied:
            break
        else:
            current_occupied = new_occupied
        round += 1

    return len(current_occupied)


def test():
    parser = FileParser("TestInput2.txt")
    seats = set(parser.read_points('L'))
    print_points(get_visible(Point(2, 1), seats))


print(part1())
print(part2())
# test()
