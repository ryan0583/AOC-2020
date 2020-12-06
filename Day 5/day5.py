from Utils.file_reader import read_lines


def get_seat_id(line: str) -> int:
    return int(line.replace('F', '0').replace('L', '0').replace('B', '1').replace('R', '1'), 2)


def get_seat_ids() -> list:
    return list(map(lambda line: get_seat_id(line), read_lines()))


def part1() -> int:
    return max(get_seat_ids())


def part2() -> int:
    seat_ids = get_seat_ids()
    return list(filter(lambda seat_id: seat_id not in seat_ids, list(range(min(seat_ids), max(seat_ids))))).pop()


if __name__ == '__main__':
    print(part1())
    print(part2())
