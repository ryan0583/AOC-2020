import math

from Utils.debug_tools import create_grid, print_grid, replace_char_at_positions
from Utils.file_parser import FileParser
from Utils.point import Point


def create_next_point(current_point, x_step, y_step):
    next_x = current_point.get_x() + x_step
    if next_x >= max_x:
        next_x = next_x - max_x
    next_y = current_point.get_y() + y_step
    return Point(next_x, next_y)


def calculate_trees(x_step, y_step, grid):
    next_point = Point(0, 0)
    tree_count = 0
    new_grid = []

    while next_point.get_y() < max_y:
        new_char = 'X'
        if next_point in tree_points:
            tree_count = tree_count + 1
            new_char = 'O'
        new_grid = replace_char_at_positions(grid, new_char, [next_point])

        next_point = create_next_point(next_point, x_step, y_step)

    print_grid(DEBUG, new_grid)
    return tree_count


def part1():
    grid = replace_char_at_positions(create_grid(max_x, max_y, '.'), TREE_CHAR, tree_points)
    return calculate_trees(3, 1, grid)


def part2():
    grid = replace_char_at_positions(create_grid(max_x, max_y, '.'), TREE_CHAR, tree_points)
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    results = []
    for slope in slopes:
        results.append(calculate_trees(slope[0], slope[1], grid))
    return math.prod(results)


TREE_CHAR = '#'
DEBUG = False
parser = FileParser('Input.txt')
tree_points = parser.read_points(TREE_CHAR)

max_x = max([point.x for point in tree_points]) + 1
max_y = max([point.y for point in tree_points]) + 1

print(part1())
print(part2())
