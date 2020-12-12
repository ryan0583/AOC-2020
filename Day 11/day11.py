from Utils.file_parser import FileParser
from Utils.point import Point


def process(seats, related_seats, max_occupied):
    def next_round():
        def occupied(seat):
            return seat in current_occupied

        def get_occupied_adjacent_length(seat):
            return len(current_occupied.intersection(related_seats[seat]))

        return [seat
                for seat in seats
                if (not occupied(seat) and get_occupied_adjacent_length(seat) == 0)
                or (occupied(seat) and get_occupied_adjacent_length(seat) < max_occupied)]

    current_occupied = set(seats)

    while True:
        new_occupied = set(next_round())
        if new_occupied == current_occupied:
            break
        else:
            current_occupied = new_occupied

    return len(current_occupied)


def part1():
    def get_adjacent(point, other_points):
        adjacent = []
        for x in range(point.x - 1, point.x + 2):
            for y in range(point.y - 1, point.y + 2):
                point_to_check = Point(x, y)
                if point_to_check == point:
                    continue
                if point_to_check in other_points:
                    adjacent.append(point_to_check)
        return set(adjacent)

    seats = set(FileParser("Input.txt").read_points('L'))

    adjacent_map = {seat: get_adjacent(seat, seats) for seat in seats}
    return process(seats, adjacent_map, 4)


def part2():
    def populate_visibles():
        def process_point(next_seat, x, y):
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
                    next_seat = process_point(next_seat, x, y)

        def process_horizontal():
            for x in range(0, xdim):
                next_seat = None
                for y in range(0, ydim):
                    next_seat = process_point(next_seat, x, y)

        def process_right_diagonal():
            start_x = xdim - 1
            x = start_x
            y = 0
            next_seat = None
            while start_x != -ydim:
                next_seat = process_point(next_seat, x, y)
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
                next_seat = process_point(next_seat, x, y)
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

    seats = set(FileParser("Input.txt").read_points('L'))
    xdim = max([seat.x for seat in seats]) + 1
    ydim = max([seat.y for seat in seats]) + 1

    visible = {seat: set() for seat in seats}
    populate_visibles()
    return process(seats, visible, 5)


print(part1())
print(part2())
