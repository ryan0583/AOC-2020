from Utils.file_reader import read_lines
import math


def part1():
    lines = read_lines('Input.txt')
    target = int(lines[0])
    buses = [int(bus) for bus in lines[1].replace('x,', '').split(',')]

    bus_time_map = {}
    for bus in buses:
        running_total = 0
        while running_total < target:
            running_total += bus
        bus_time_map[running_total] = bus

    final_time = min(bus_time_map.keys())
    return (final_time - target) * bus_time_map[final_time]


# def part2():
#     lines = read_lines('Input.txt')
#     buses = lines[1].split(',')
#
#     max_bus = max([int(bus) for bus in buses if bus != 'x'])
#
#     print(max_bus)
#
#     max_position = 0
#     for index, bus in enumerate(buses):
#         if bus != 'x' and int(bus) == max_bus:
#             max_position = index
#             break
#
#     print(max_position)
#
#     possibles = [(possible * max_bus) - max_position
#                  for possible in range(int(100000000000000 / max_bus), int(200000000000000 / max_bus))
#                  if (possible * max_bus) - max_position < 200000000000000]
#
#     print(possibles)
#
#     for index, bus in enumerate(buses):
#         print(bus)
#         if bus == 'x':
#             continue
#         possibles = [possible for possible in possibles if (possible + index) % int(bus) == 0]
#
#     return possibles[0]


def part2():
    lines = read_lines('Input.txt')
    buses = lines[1].split(',')

    bus_index_map = {int(bus): index for index, bus in enumerate(buses) if bus != 'x'}

    bus_list = [int(bus) for bus in buses if bus != 'x']
    bus_list.sort()
    bus_list.reverse()

    print(bus_list)
    max_bus = bus_list[0]
    second_max_bus = bus_list[1]

    print(max_bus)
    print(second_max_bus)

    position = bus_index_map[max_bus]

    print(position)

    found = False
    answer = 100052416624471
    while not found:
        if answer % (max_bus * second_max_bus) == 0:
            found = True
        else:
            answer += 1

    answer = answer - position
    correct = False
    while not correct:
        print(answer)
        correct = True
        for bus in bus_list:
            index = bus_index_map[bus]
            correct = (answer + index) % int(bus) == 0
            if not correct:
                break
        if correct:
            return answer
        answer += max_bus


# print(part1())
print(part2())
