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


def process(input_list, pattern, input_item_number):
    def process_chunk():
        _output = 0
        for i, input_item in enumerate(input_list_chunk):
            pattern_item = pattern_chunk[i]
            if pattern_item == 0:
                continue
            _output += int(input_item) * pattern_item
        return _output

    output = 0
    start_pos = input_item_number
    end_pos = start_pos + input_item_number + 1
    while start_pos < len(input_list):
        input_list_chunk = input_list[start_pos:end_pos if end_pos < len(input_list) else len(input_list)]
        pattern_chunk = pattern[start_pos:end_pos if end_pos < len(pattern) else len(pattern)]
        output += process_chunk()
        start_pos = end_pos + input_item_number + 1
        end_pos = start_pos + input_item_number + 1

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
            output.append(process(input_list, pattern, i))
        input_list = output
        output = []
        print(input_list)

    print("".join(input_list[0:8]))


def part2():
    input_list = [int(x) for x in list(open("input.txt", "r").read())]
    full_input_list = []
    for i in range(0, 10000):
        full_input_list.extend(input_list)

    message_offset = int("".join(str(x) for x in input_list[0:7]))
    full_input_list = full_input_list[message_offset:len(full_input_list)]
    output = []

    phase_count = 0
    while phase_count < 100:
        phase_count += 1
        list_sum = sum(full_input_list)
        print(phase_count)
        count_to_subtract = 0
        for item in full_input_list:
            output_str = str(list_sum - count_to_subtract)
            output.append(int(output_str[len(output_str) - 1: len(output_str)]))
            count_to_subtract += item
        full_input_list = output
        output = []
        print(full_input_list)

    print("".join(str(x) for x in full_input_list[0:8]))


part1()
# part2()
