from Utils.debug_tools import create_grid
from Utils.debug_tools import print_grid
from Utils.debug_tools import raise_
from Utils.intcode_computer import IntcodeComputer
from Utils.point import Point


class Robot:
    def __init__(self, filename):
        self.brain = IntcodeComputer([], filename, True)
        self.position = Point(0, 0)
        self.direction = UP

    def turn(self, rotation):
        if rotation == ROTATE_RIGHT:
            self.direction = self.direction + 1
            if self.direction > LEFT:
                self.direction = UP
        else:
            self.direction = self.direction - 1
            if self.direction < UP:
                self.direction = LEFT

    def move(self):
        if self.direction == UP:
            self.position = Point(self.position.x, self.position.y - 1)
        elif self.direction == RIGHT:
            self.position = Point(self.position.x + 1, self.position.y)
        elif self.direction == DOWN:
            self.position = Point(self.position.x, self.position.y + 1)
        elif self.direction == LEFT:
            self.position = Point(self.position.x - 1, self.position.y)
        else:
            raise_(Exception("Unrecognised direction " + str(self.direction)))


class Panel:
    def __init__(self):
        self.colours = {}

    def paint(self, color, position):
        self.colours[position.x, position.y] = color

    def get_colour(self, position):
        colour = self.colours.get((position.x, position.y))
        return colour if colour is not None else BLACK

    def print(self):
        min_x = min(list(map(lambda key: key[0], self.colours.keys())))
        max_x = max(list(map(lambda key: key[0], self.colours.keys())))
        min_y = min(list(map(lambda key: key[1], self.colours.keys())))
        max_y = max(list(map(lambda key: key[1], self.colours.keys())))

        x_dim = max_x - min_x + 1
        y_dim = max_y - min_y + 1

        grid = create_grid(x_dim, y_dim)

        for position, colour in self.colours.items():
            x_pos = position[0] - min_x
            y_pos = position[1] - min_y
            grid[y_pos][x_pos] = ".." if colour == BLACK else "##"

        print_grid(True, grid)


def part1():
    robot = Robot("input.txt")
    panel = Panel()

    while robot.brain.is_running():
        next_input = panel.get_colour(robot.position)
        robot.brain.append_input(next_input)
        next_colour = robot.brain.process()
        next_rotation = robot.brain.process()
        panel.paint(next_colour, robot.position)
        robot.turn(next_rotation)
        robot.move()

    print(len(panel.colours))


def main_loop(robot, panel):
    while robot.brain.is_running():
        next_input = panel.get_colour(robot.position)
        robot.brain.append_input(next_input)
        next_colour = robot.brain.process()
        next_rotation = robot.brain.process()
        panel.paint(next_colour, robot.position)
        robot.turn(next_rotation)
        robot.move()


def part1():
    robot = Robot("input.txt")
    panel = Panel()
    main_loop(robot, panel)
    print(len(panel.colours))


def part2():
    robot = Robot("input.txt")
    panel = Panel()
    panel.paint(WHITE, robot.position)
    main_loop(robot, panel)
    panel.print()


BLACK = 0
WHITE = 1

ROTATE_LEFT = 0
ROTATE_RIGHT = 1

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

part1()
# part2()
