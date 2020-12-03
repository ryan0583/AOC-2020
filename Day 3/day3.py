from Utils.file_parser import FileParser
from Utils.point import Point


parser = FileParser('Input.txt')
tree_map = parser.read_points_map('#')

max_x = max(list(map(lambda key: key.get_x(), tree_map.keys())))
max_y = max(list(map(lambda key: key.get_y(), tree_map.keys())))

print(max_x)
print(max_y)

next_point = Point(0, 0)

tree_count = 0

while next_point.get_y() <= max_y:
    if next_point in tree_map:
        tree_count = tree_count + 1

    next_x = next_point.get_x() + 3
    if next_x > max_x:
        next_x = next_x - max_x - 1
    next_y = next_point.get_y() + 1
    next_point = Point(next_x, next_y)

print(tree_count)




