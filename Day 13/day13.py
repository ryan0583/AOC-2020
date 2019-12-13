import tkinter as tk

from Utils.debug_tools import raise_
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

    def update_canvas(_canvas, _point, tile_type):
        tile_switcher = {
            EMPTY: lambda: "white",
            WALL: lambda: "black",
            BLOCK: lambda: "blue",
            PADDLE: lambda: "green",
            BALL: lambda: "red"
        }

        color = tile_switcher.get(tile_type, lambda: raise_("Invalid param mode" + tile_type))()
        rect = rects.get(_point)
        if rect is None:
            rect = _canvas.create_rectangle(_point.x * GAME_SCALE, _point.y * GAME_SCALE,
                                                _point.x * GAME_SCALE + GAME_SCALE,
                                                _point.y * GAME_SCALE + GAME_SCALE, fill=color)
            rects[_point] = rect
        else:
            _canvas.itemconfigure(rect, fill=color)
        _canvas.itemconfigure(text, text="SCORE: " + str(score))

    def paint_canvas():
        root.update_idletasks()
        root.update()

    def init_game():
        def init_canvas():
            for _point in tiles.keys():
                tile_type = tiles.get(_point)
                update_canvas(_canvas, _point, tile_type)
            paint_canvas()
            return _canvas.create_text(GAME_SCALE * 2, GAME_SCALE * 2, fill="black",
                                       font="Arial " + str(GAME_SCALE - GAME_SCALE // 2), anchor="w",
                                       text="SCORE: " + str(score))

        x_dimension = (max(list(map(lambda position: position.x, tiles.keys()))) + 1) * GAME_SCALE
        y_dimension = (max(list(map(lambda position: position.y, tiles.keys()))) + 1) * GAME_SCALE

        _canvas = tk.Canvas(root, width=x_dimension, height=y_dimension)
        _canvas.pack()

        return _canvas, init_canvas(), True

    intcode_computer = IntcodeComputer([], "input.txt", True)
    intcode_computer.write_mem_addr(0, 2)
    root = tk.Tk()

    tiles = {}
    rects = {}
    score = 0
    last_ball_point = None
    paddle_point = None
    joystick_tilt = JOY_CENTRAL
    setup_complete = False
    canvas = None
    text = None

    while intcode_computer.is_running():
        x = intcode_computer.process()
        y = intcode_computer.process()
        output = intcode_computer.process()
        if x == SCORE_X and y == SCORE_Y:
            if not setup_complete:
                canvas, text, setup_complete = init_game()

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
                update_canvas(canvas, point, output)
                if output != EMPTY:
                    paint_canvas()

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

GAME_SCALE = 50

# part1()
part2()
