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
                _joystick_tilt = JOY_RIGHT
            else:
                _joystick_tilt = JOY_LEFT

        return _joystick_tilt

    intcode_computer = IntcodeComputer([], "input.txt", True)
    intcode_computer.write_mem_addr(0, 2)

    tiles = {}
    score = 0
    last_ball_point = None
    paddle_point = None
    joystick_tilt = JOY_CENTRAL
    has_drawn_block = False
    setup_complete = False
    grid = None

    while intcode_computer.is_running():
        x = intcode_computer.process()
        y = intcode_computer.process()
        output = intcode_computer.process()
        if x == SCORE_X and y == SCORE_Y:
            # print("SCORE: " + str(output))
            # print("BLOCK_COUNT: " + str(sum(map(BLOCK.__eq__, tiles.values()))))
            score = output
            setup_complete = True
            if has_drawn_block:
                if sum(map(BLOCK.__eq__, tiles.values())) == 0:
                    break
        else:
            point = Point(x, y)

            if output == BLOCK:
                # print("BLOCK: " + str(point))
                has_drawn_block = True
            # elif output == WALL:
                # print("WALL: " + str(point))
            # elif output == EMPTY:
                # print("EMPTY: " + str(point))
            elif output == BALL:
                # print("BALL: " + str(point))
                joystick_tilt = get_joystick_tilt(joystick_tilt)
                last_ball_point = point
            elif output == PADDLE:
                paddle_point = point
                # print("PADDLE: " + str(point))

            tiles[point] = output

            if setup_complete:
                if grid is None:
                    x_dim = max(list(map(lambda _point: _point.x, tiles.keys()))) + 1
                    y_dim = max(list(map(lambda _point: _point.y, tiles.keys()))) + 1
                    grid = create_grid(x_dim, y_dim, "  ")

                for point in tiles.keys():
                    tile_type = tiles.get(point)
                    tile_char = None
                    if tile_type == EMPTY:
                        tile_char = " "
                    elif tile_type == WALL:
                        tile_char = "|"
                    elif tile_type == BLOCK:
                        tile_char = "#"
                    elif tile_type == PADDLE:
                        tile_char = "_"
                    elif tile_type == BALL:
                        tile_char = "O"
                    grid[point.y][point.x] = tile_char

        # joystick_tilt = int(input("enter joystick movement:\n"))
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
