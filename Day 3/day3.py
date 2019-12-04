import sys

from Utils.utils import create_grid, debug_print, print_grid

sys.path.append('../')


class WirePart:
    def __init__(self, char, step_num):
        self.char = char
        self.step_num = step_num

    def get_step_num(self):
        return self.step_num

    def get_char(self):
        return self.char

    def __str__(self):
        return self.char


class Crossing:
    def __init__(self, x, y, total_steps):
        self.x = x
        self.y = y
        self.total_steps = total_steps

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_total_steps(self):
        return self.total_steps

    def __str__(self):
        return "X"


def max_range(instructions, posChar, negChar):
    max_dist = 0
    min_dist = 0
    running_total = 0
    for instruction in instructions:
        direction = instruction[0:1]
        distance = int(instruction[1:])
        if direction == posChar:
            running_total = running_total + distance
        elif direction == negChar:
            running_total = running_total - distance

        if running_total > max_dist:
            max_dist = running_total
        if running_total < min_dist:
            min_dist = running_total
    return min_dist, max_dist


def draw_wire1():
    def place_wire(x, y, wire_char):
        new_step_num = step_num + 1
        grid[y][x] = WirePart(wire_char, new_step_num)
        return new_step_num

    step_num = 0
    x_pos = port_x
    y_pos = port_y

    for instruction in wire1_instructions:
        direction = instruction[0:1]
        distance = int(instruction[1:])
        if direction == "R":
            for x in range(x_pos + 1, x_pos + 1 + distance):
                step_num = place_wire(x, y_pos, "-")
            x_pos = x_pos + distance
        elif direction == "L":
            for x in range(x_pos - 1, x_pos - 1 - distance, -1):
                step_num = place_wire(x, y_pos, "-")
            x_pos = x_pos - distance
        elif direction == "D":
            for y in range(y_pos + 1, y_pos + 1 + distance):
                step_num = place_wire(x_pos, y, "|")
            y_pos = y_pos + distance
        elif direction == "U":
            for y in range(y_pos - 1, y_pos - 1 - distance, -1):
                step_num = place_wire(x_pos, y, "|")
            y_pos = y_pos - distance


def draw_wire2_and_determine_crossings():
    def place_wire_and_add_crossing(wire_char, x, y):
        new_step_num = step_num + 1
        grid_space = grid[y][x]
        if isinstance(grid_space, WirePart):
            crossing = Crossing(x, y, new_step_num + grid_space.get_step_num())
            grid[y][x] = crossing
            crossings.append(crossing)
        else:
            grid[y][x] = wire_char
        return new_step_num

    crossings = list()
    step_num = 0
    x_pos = port_x
    y_pos = port_y

    for instruction in wire2_instructions:
        direction = instruction[0:1]
        distance = int(instruction[1:])
        if direction == "R":
            for x in range(x_pos + 1, x_pos + 1 + distance):
                step_num = place_wire_and_add_crossing("-", x, y_pos)
            x_pos = x_pos + distance
        elif direction == "L":
            for x in range(x_pos - 1, x_pos - 1 - distance, -1):
                step_num = place_wire_and_add_crossing("-", x, y_pos)
            x_pos = x_pos - distance
        elif direction == "D":
            for y in range(y_pos + 1, y_pos + 1 + distance):
                step_num = place_wire_and_add_crossing("|", x_pos, y)
            y_pos = y_pos + distance
        elif direction == "U":
            for y in range(y_pos - 1, y_pos - 1 - distance, -1):
                step_num = place_wire_and_add_crossing("|", x_pos, y)
            y_pos = y_pos - distance
    return crossings


def find_min_crossing_position():
    min_crossing = -1
    for crossing in crossings:
        dist = abs(crossing.get_y() - port_y) + abs(crossing.get_x() - port_x)
        if min_crossing == -1 or dist < min_crossing:
            min_crossing = dist
    return min_crossing


def find_min_crossing_steps():
    min_steps = -1
    for crossing in crossings:
        if min_steps == -1 or crossing.get_total_steps() < min_steps:
            min_steps = crossing.get_total_steps()
    return min_steps


debug = False

debug_print(debug, "reading file")
file = open("Input.txt", "r")
instruction_list = file.read().splitlines()
wire1_instructions = instruction_list[0].split(",")
wire2_instructions = instruction_list[1].split(",")

debug_print(debug, "finding range")
wire1_x_range = max_range(wire1_instructions, "R", "L")
wire1_y_range = max_range(wire1_instructions, "U", "D")
wire2_x_range = max_range(wire2_instructions, "R", "L")
wire2_y_range = max_range(wire2_instructions, "U", "D")

maxRight = max(wire1_x_range[1], wire2_x_range[1])
maxLeft = abs(min(wire1_x_range[0], wire2_x_range[0]))
xDimension = maxRight + maxLeft + 3

maxUp = max(wire1_y_range[1], wire2_y_range[1])
maxDown = abs(min(wire1_y_range[0], wire2_y_range[0]))
yDimension = maxUp + maxDown + 3

debug_print(debug, "creating grid")
grid = create_grid(xDimension, yDimension)
port_x = maxLeft + 1
port_y = maxUp + 1
grid[port_y][port_x] = "o"

debug_print(debug, "drawing wire 1")
draw_wire1()

debug_print(debug, "drawing wire 2")
crossings = draw_wire2_and_determine_crossings()

debug_print(debug, "finding answers")
print_grid(debug, grid)
print(find_min_crossing_position())
print(find_min_crossing_steps())
