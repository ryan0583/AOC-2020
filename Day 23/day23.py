from Utils.file_reader import read_lines


class Entry:
    def __init__(self, value):
        self.value = value
        self.next_cup = None

    def set_next_cup(self, next_cup):
        self.next_cup = next_cup

    def get_value(self):
        return self.value


def move(current_cup, max_cup_value, cup_map):
    pickup_cups = [current_cup.next_cup.value, current_cup.next_cup.next_cup.value,
                   current_cup.next_cup.next_cup.next_cup.value]

    dest_cup_value = current_cup.value - 1
    while dest_cup_value in pickup_cups or dest_cup_value <= 0:
        dest_cup_value -= 1
        if dest_cup_value < 1:
            dest_cup_value = max_cup_value

    dest_cup = cup_map[dest_cup_value]

    removed_cup = current_cup.next_cup

    current_cup.set_next_cup(current_cup.next_cup.next_cup.next_cup.next_cup)

    removed_cup.next_cup.next_cup.set_next_cup(dest_cup.next_cup)
    dest_cup.set_next_cup(removed_cup)

    return current_cup.next_cup


def populate_links(line):
    for index, entry in enumerate(line):
        entry.set_next_cup(line[(index + 1) % len(line)])


def play_game(line, rounds):
    current_cup = line[0]
    max_cup_value = max([e.value for e in line])
    cup_map = {e.value: e for e in line}

    for i in range(0, rounds):
        # print('MOVE: ' + str(i + 1))
        current_cup = move(current_cup, max_cup_value, cup_map)


def part1():
    line = [Entry(int(c)) for c in read_lines('Input.txt')[0]]

    populate_links(line)

    play_game(line, 100)

    cup_one = [cup for cup in line if cup.value == 1][0]
    next_cup = cup_one.next_cup
    result = ''
    while next_cup.value != 1:
        result += str(next_cup.value)
        next_cup = next_cup.next_cup

    print(result)


def part2():
    line = [Entry(int(c)) for c in read_lines('Input.txt')[0]]

    max_num = max([int(e.value) for e in line])

    for i in range(max_num + 1, 1000001):
        line.append(Entry(i))

    populate_links(line)

    play_game(line, 10000000)

    cup_one = [cup for cup in line if cup.value == 1][0]
    result = cup_one.next_cup.value * cup_one.next_cup.next_cup.value
    # print(cup_one.next_cup.value)
    # print(cup_one.next_cup.next_cup.value)
    print(result)


part1()
part2()
