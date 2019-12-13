from Utils.debug_tools import create_grid, render_grid
from Utils.intcode_computer import IntcodeComputer
from Utils.point import Point


def part1():
    intcode_computer = IntcodeComputer([], "input.txt", True)
    tiles = {}

    while intcode_computer.is_running():
        x = intcode_computer.process()
        y = intcode_computer.process()
        output = intcode_computer.process()
        point = Point(x, y)
        tiles[str(point)] = output

    print(sum(map(BLOCK.__eq__, tiles.values())))


def part2():
    def get_joystick_tilt(_joystick_tilt):
        if paddle_point is not None:
            if point.x > paddle_point.x:
                return JOY_RIGHT
            elif point.x < paddle_point.x:
                return JOY_LEFT

        if last_ball_point is not None:
            moving_right = last_ball_point.x < point.x
            if moving_right:
                return JOY_RIGHT
            else:
                return JOY_LEFT

        return _joystick_tilt

    intcode_computer = IntcodeComputer([], "input.txt", True)
    intcode_computer.write_mem_addr(0, 2)

    tiles = {}
    score = 0
    last_ball_point = None
    paddle_point = None
    joystick_tilt = JOY_CENTRAL

    while intcode_computer.is_running():
        x = intcode_computer.process()
        y = intcode_computer.process()
        output = intcode_computer.process()
        if x == SCORE_X and y == SCORE_Y:
            score = output
            if sum(map(BLOCK.__eq__, tiles.values())) == 0:
                break
        else:
            point = Point(x, y)

            if output == BALL:
                joystick_tilt = get_joystick_tilt(joystick_tilt)
                last_ball_point = point
            elif output == PADDLE:
                paddle_point = point

            tiles[point] = output

        intcode_computer.replace_next_input(joystick_tilt)

    print(score)


SCORE_X = -1
SCORE_Y = 0

EMPTY = 0
WALL = 1
BLOCK = 2
PADDLE = 3
BALL = 4

JOY_LEFT = -1
JOY_CENTRAL = 0
JOY_RIGHT = 1

# part1()
part2()
