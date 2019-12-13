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
    intcode_computer = IntcodeComputer([JOY_CENTRAL], "input.txt", True)
    intcode_computer.write_mem_addr(0, 2)

    tiles = {}
    score = 0
    last_ball_point = None
    joystick_tilt = JOY_CENTRAL
    has_drawn_block = False

    while intcode_computer.is_running():
        x = intcode_computer.process()
        y = intcode_computer.process()
        output = intcode_computer.process()
        if x == SCORE_X and y == SCORE_Y:
            score = output
        else:
            point = Point(x, y)

            if output == BLOCK:
                has_drawn_block = True
            elif output == BALL:
                if last_ball_point is not None:
                    moving_right = last_ball_point.x < point.x
                    if moving_right:
                        joystick_tilt = JOY_RIGHT
                    else:
                        joystick_tilt = JOY_LEFT
                last_ball_point = point

            tiles[str(point)] = output

            if has_drawn_block:
                if sum(map(BLOCK.__eq__, tiles.values())) == 0:
                    break

        # joystick_tilt = int(input("enter joystick movement:\n"))
        intcode_computer.append_input(joystick_tilt)

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
