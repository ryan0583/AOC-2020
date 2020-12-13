from Utils.file_reader import read_lines


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


print(part1())
