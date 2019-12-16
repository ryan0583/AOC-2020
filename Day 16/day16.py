def get_repeating_pattern(length, element_count):
    pattern_list = [0, 1, 0, -1]
    pattern = []
    count = 0

    while len(pattern) < length + 1:
        pattern_item = pattern_list[count % 4]
        for i in range(0, element_count):
            pattern.append(pattern_item)
        count += 1

    return pattern[1:length + 1]


def process(input_list, pattern):
    output = 0
    for i, input_item in enumerate(input_list):
        pattern_item = pattern[i]
        output += int(input_item) * pattern_item
    output_str = str(output)
    return output_str[len(output_str) - 1: len(output_str)]


def part1():
    input_list = list(open("input.txt", "r").read())
    output = []

    phase_count = 0
    while phase_count < 100:
        phase_count += 1
        for i in range(0, len(input_list)):
            pattern = get_repeating_pattern(len(input_list), i + 1)
            output.append(process(input_list, pattern))
        input_list = output
        output = []
        print(input_list)

    print("".join(input_list[0:8]))


def part2():
    input_list = list(open("input.txt", "r").read())
    full_input_list = []
    for i in range(0, 10000):
        full_input_list.extend(input_list)

    message_offset = int("".join(input_list[0:7]))
    output = []

    phase_count = 0
    while phase_count < 100:
        phase_count += 1
        print(phase_count)
        for i in range(0, len(full_input_list)):
            pattern = get_repeating_pattern(len(full_input_list), i + 1)
            output.append(process(full_input_list, pattern))
            print(len(output))
        full_input_list = output
        output = []
        print(input_list)

    print(input_list[message_offset: message_offset + 8])


# part1()
part2()
