from Utils.file_reader import read_lines
import timeit

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


def part2():
    lines = read_lines('Input.txt')
    buses = lines[1].split(',')
    bus_index_map = {int(bus): index for index, bus in enumerate(buses) if bus != 'x'}
    bus_list = [int(bus) for bus in buses if bus != 'x']
    # bus_list.sort()
    # bus_list.reverse()

    jump = 1
    answer = bus_list[0] - bus_index_map[bus_list[0]]
    for bus in bus_list:
        index = bus_index_map[bus]
        while (answer + index) % int(bus) != 0:
            answer += jump
        jump *= int(bus)
        print("BUS: " + str(bus) + " ANS: " + str(answer) + " JUMP: " + str(jump))

    return answer


# print(part1())
timeit.timeit(part2())
