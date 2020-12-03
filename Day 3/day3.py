import math
from Utils.file_parser import FileParser
from Utils.point import Point


def create_next_point(current_point, x_step, y_step):
    next_x = current_point.get_x() + x_step
    if next_x > max_x:
        next_x = next_x - max_x - 1
    next_y = current_point.get_y() + y_step
    return Point(next_x, next_y)


def calculate_trees(x_step, y_step):
    next_point = Point(0, 0)
    tree_count = 0

    while next_point.get_y() <= max_y:
        if next_point in tree_map:
            tree_count = tree_count + 1

        next_point = create_next_point(next_point, x_step, y_step)

    return tree_count


def part1():
    return calculate_trees(3, 1)


def part2():
    return math.prod([calculate_trees(1, 1), calculate_trees(3, 1), calculate_trees(5, 1), calculate_trees(7, 1),
                      calculate_trees(1, 2)])


parser = FileParser('Input.txt')
tree_map = parser.read_points_map('#')

max_x = max(list(map(lambda key: key.get_x(), tree_map.keys())))
max_y = max(list(map(lambda key: key.get_y(), tree_map.keys())))

print(part1())
print(part2())
