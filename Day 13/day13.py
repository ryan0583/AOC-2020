import time

from Utils.debug_tools import raise_
from Utils.graphics_panel import *
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

    def map_tile(tile_type):
        tile_switcher = {
            EMPTY: lambda: "black",
            WALL: lambda: "white",
            BLOCK: lambda: "red",
            PADDLE: lambda: "blue",
            BALL: lambda: "yellow"
        }

        return tile_switcher.get(tile_type, lambda: raise_("Invalid param mode" + tile_type))()

    intcode_computer = IntcodeComputer([], "input.txt", True)
    intcode_computer.write_mem_addr(0, 2)

    tiles = {}
    score = 0
    last_ball_point = None
    paddle_point = None
    joystick_tilt = JOY_CENTRAL
    setup_complete = False
    graphics_panel = None

    while intcode_computer.is_running():
        x = intcode_computer.process()
        y = intcode_computer.process()
        output = intcode_computer.process()
        if x == SCORE_X and y == SCORE_Y:
            if not setup_complete:
                graphics_panel = GraphicsPanel({k: map_tile(v) for k, v in tiles.items()})
                graphics_panel.init_canvas()
                graphics_panel.add_text("SCORE: " + str(score), "white")
                graphics_panel.paint_canvas()
                setup_complete = True
            else:
                graphics_panel.update_text("SCORE: " + str(score))

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

            if setup_complete:
                graphics_panel.update_canvas(point, map_tile(output))
                if output != EMPTY:
                    # graphics_panel.update_text("SCORE: " + str(score))
                    graphics_panel.paint_canvas()
                    time.sleep(0.01)

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
