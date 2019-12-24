from Utils.point import Point


class FileParser:
    def __init__(self, filename):
        self.lines = open(filename, "r").read().splitlines()

    def read_points(self, char):
        points = []
        for y, line in enumerate(self.lines):
            for x, this_char in enumerate(line):
                if this_char == char:
                    points.append(Point(x, y))
        return points

    def read_points_map(self, char):
        points = {}
        for y, line in enumerate(self.lines):
            for x, this_char in enumerate(line):
                if this_char == char:
                    points[Point(x, y)] = char
        return points
