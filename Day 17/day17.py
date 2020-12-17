from Utils.debug_tools import create_grid, print_grid, replace_char_at_positions
from Utils.file_parser import FileParser
from Utils.point3d import Point3d
from Utils.point4d import Point4d


def print_points(points):
    for point in points:
        print(point)


def get_neighbours(point):
    neighbours = set()
    for x in range(point.x - 1, point.x + 2):
        for y in range(point.y - 1, point.y + 2):
            for z in range(point.z - 1, point.z + 2):
                neighbour_point = Point3d(x, y, z)
                if neighbour_point != point:
                    neighbours.add(neighbour_point)
    return neighbours


def get_neighbours_4d(point):
    neighbours = set()
    for x in range(point.x - 1, point.x + 2):
        for y in range(point.y - 1, point.y + 2):
            for z in range(point.z - 1, point.z + 2):
                for w in range(point.w - 1, point.w + 2):
                    neighbour_point = Point4d(x, y, z, w)
                    if neighbour_point != point:
                        neighbours.add(neighbour_point)
    return neighbours


def part1():
    def perform_cycle():
        new_active = []

        min_x = min([point.x for point in current_active]) - 1
        max_x = max([point.x for point in current_active]) + 1
        min_y = min([point.y for point in current_active]) - 1
        max_y = max([point.y for point in current_active]) + 1
        min_z = min([point.z for point in current_active]) - 1
        max_z = max([point.z for point in current_active]) + 1

        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                for z in range(min_z, max_z + 1):
                    point_to_check = Point3d(x, y, z)
                    neighbours = get_neighbours(point_to_check)
                    active_neighbours = set.intersection(neighbours, current_active)
                    if len(active_neighbours) == 3:
                        new_active.append(point_to_check)
                    elif point_to_check in current_active and len(active_neighbours) == 2:
                        new_active.append(point_to_check)

        # print_points(new_active)

        return new_active

    parser = FileParser("Input.txt")
    points_2d = parser.read_points("#")
    grid = create_grid(max([point.x for point in points_2d]) + 1, max([point.y for point in points_2d]) + 1,
                       '.')
    replace_char_at_positions(grid, '#', points_2d)
    print("0 cycles")
    print("==========")
    print("z = 0:")
    print_grid(True, grid)
    print("==========")

    current_active = [Point3d(point.x, point.y, 0) for point in points_2d]

    for i in range(0, 6):
        print("CYCLE: " + str(i))
        current_active = perform_cycle()

    return len(current_active)


def part2():
    def perform_cycle():
        new_active = []

        min_x = min([point.x for point in current_active]) - 1
        max_x = max([point.x for point in current_active]) + 1
        min_y = min([point.y for point in current_active]) - 1
        max_y = max([point.y for point in current_active]) + 1
        min_z = min([point.z for point in current_active]) - 1
        max_z = max([point.z for point in current_active]) + 1
        min_w = min([point.w for point in current_active]) - 1
        max_w = max([point.w for point in current_active]) + 1

        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                for z in range(min_z, max_z + 1):
                    for w in range(min_w, max_w + 1):
                        print(w)
                        point_to_check = Point4d(x, y, z, w)
                        neighbours = get_neighbours_4d(point_to_check)
                        active_neighbours = set.intersection(neighbours, current_active)
                        if len(active_neighbours) == 3:
                            new_active.append(point_to_check)
                        elif point_to_check in current_active and len(active_neighbours) == 2:
                            new_active.append(point_to_check)

        # print_points(new_active)

        return new_active

    parser = FileParser("Input.txt")
    points_2d = parser.read_points("#")
    grid = create_grid(max([point.x for point in points_2d]) + 1, max([point.y for point in points_2d]) + 1,
                       '.')
    replace_char_at_positions(grid, '#', points_2d)
    print("0 cycles")
    print("==========")
    print("z = 0:")
    print_grid(True, grid)
    print("==========")

    current_active = [Point4d(point.x, point.y, 0, 0) for point in points_2d]

    for i in range(0, 6):
        print("CYCLE: " + str(i))
        current_active = perform_cycle()

    return len(current_active)


# print(part1())
print(part2())
