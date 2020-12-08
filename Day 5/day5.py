import time

from Utils.file_reader import read_lines
from Utils.graphics_panel import GraphicsPanel
from Utils.point import Point


def get_seat_id(line: str) -> int:
    return int(line.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2)


def get_seat_ids() -> list:
    return [get_seat_id(line) for line in read_lines('Input.txt')]


def part1() -> int:
    return max(get_seat_ids())


def convert_seat_id_to_point(seat_id: int) -> Point:
    binary_seat_id = str(bin(seat_id))[2:].zfill(10)
    x = int(binary_seat_id[0:7], 2)
    y = int(binary_seat_id[7:len(binary_seat_id)], 2) + 2
    if y > 3:
        y += 1

    if y > 8:
        y += 1
    return Point(x, y)


def visualise(seat_ids: list, your_seat: int):
    def take_seat():
        graphics_panel.update_canvas(point, "blue")
        graphics_panel.paint_canvas()
        time.sleep(0.005)

    points = [convert_seat_id_to_point(seat_id) for seat_id in seat_ids]

    graphics_panel = GraphicsPanel.create_empty_panel(max([point.x for point in points]) + 4,
                                                      max([point.y for point in points]) + 4,
                                                      10)

    graphics_panel.init_canvas()
    graphics_panel.paint_canvas()
    for point in points:
        take_seat()

    graphics_panel.update_canvas(convert_seat_id_to_point(your_seat), "yellow")
    graphics_panel.paint_canvas()


def part2() -> int:
    seat_ids = get_seat_ids()
    your_seat = [seat_id for seat_id in list(range(min(seat_ids), max(seat_ids))) if seat_id not in seat_ids].pop()
    visualise(seat_ids, your_seat)
    return your_seat


print(part1())
print(part2())
