from Utils.file_reader import read_lines
from Utils.point import Point


def rotate(current_direction, rotate_direction, amount):
    new_direction = current_direction
    change_amount = (amount / 90) % 4
    if rotate_direction == RIGHT:
        new_direction += change_amount
    else:
        new_direction -= change_amount
    new_direction = new_direction % 4
    return new_direction


def rotate_waypoint(waypoint_position, ship_position, rotate_direction, amount):
    change_amount = (amount / 90) % 4
    relative = Point(waypoint_position.x - ship_position.x, waypoint_position.y - ship_position.y)

    if change_amount == 2:
        relative.x = -relative.x
        relative.y = -relative.y
    else:
        if rotate_direction == RIGHT:
            if change_amount == 1:
                relative = Point(relative.y, -relative.x)
            else:
                relative = Point(-relative.y, relative.x)
        else:
            if change_amount == 1:
                relative = Point(-relative.y, relative.x)
            else:
                relative = Point(relative.y, -relative.x)

    return Point(ship_position.x + relative.x, ship_position.y + relative.y)


def move(current_position, direction, amount):
    new_position = Point(current_position.x, current_position.y)
    if direction == NORTH:
        new_position.y += amount
    elif direction == SOUTH:
        new_position.y -= amount
    if direction == EAST:
        new_position.x += amount
    if direction == WEST:
        new_position.x -= amount
    return new_position


def part1():
    direction = EAST
    position = Point(START_POSITION.x, START_POSITION.y)
    lines = read_lines("Input.txt")
    for line in lines:
        instruction = line[0]
        amount = int(line[1:])
        if instruction in ["R", "L"]:
            direction = rotate(direction, instruction, amount)
        elif instruction in DIRECTIONS:
            position = move(position, DIRECTIONS.index(instruction), amount)
        else:
            position = move(position, direction, amount)

    return abs(position.x) + abs(position.y)


def part2():
    waypoint_relative = Point(10, 1)
    ship_position = Point(START_POSITION.x, START_POSITION.y)
    waypoint_position = Point(START_POSITION.x + waypoint_relative.x, START_POSITION.y + waypoint_relative.y)
    lines = read_lines("Input.txt")
    print(f'SHIP: {ship_position}')
    print(f'WAYPOINT: {waypoint_position}')
    print('====================')
    for line in lines:
        instruction = line[0]
        amount = int(line[1:])

        if instruction in ["R", "L"]:
            waypoint_position = rotate_waypoint(waypoint_position, ship_position, instruction, amount)
            waypoint_relative = Point(waypoint_position.x - ship_position.x, waypoint_position.y - ship_position.y)

        elif instruction in DIRECTIONS:
            waypoint_position = move(waypoint_position, DIRECTIONS.index(instruction), amount)
            waypoint_relative = Point(waypoint_position.x - ship_position.x, waypoint_position.y - ship_position.y)
        else:

            for i in range(0, amount):
                ship_position = Point(waypoint_position.x, waypoint_position.y)
                waypoint_position = Point(ship_position.x + waypoint_relative.x, ship_position.y + waypoint_relative.y)

        print(f'SHIP: {ship_position}')
        print(f'WAYPOINT: {waypoint_position}')
        print('====================')

    return abs(ship_position.x) + abs(ship_position.y)


NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

RIGHT = 'R'
LEFT = 'L'

DIRECTIONS = ["N", "E", "S", "W"]

START_POSITION = Point(0, 0)

# print(part1())
print(part2())
