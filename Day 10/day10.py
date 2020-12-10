from Utils import file_reader


def part1():
    def add_next():
        prev = chain[-1]
        diff = 1
        while True:
            for line in lines:
                if prev + diff == line:
                    chain.append(line)
                    return diff
            diff += 1

    lines = [int(row) for row in file_reader.read_lines('Input.txt')]
    chain = [0]
    one_diff = 0
    three_diff = 0
    while max(chain) != max(lines):
        next_diff = add_next()
        if next_diff == 1:
            one_diff += 1
        if next_diff == 3:
            three_diff += 1
    return one_diff * (three_diff + 1)


def part2():
    def get_prev(number):
        prev_list = []
        for line in lines:
            if line >= number:
                return prev_list
            if line >= number - 3:
                prev_list.append(line)
        return prev_list

    def process_next(number):
        valid_prev_list = get_prev(number)
        for valid_prev in valid_prev_list:
            path_counts[number] += path_counts[valid_prev]

    lines = [int(row) for row in file_reader.read_lines('Input.txt')]
    lines.append(0)
    lines.sort()
    path_counts = {0: 1}
    index = 1
    while index < len(lines):
        next_number = lines[index]
        path_counts[next_number] = 0
        process_next(next_number)
        index += 1
    return path_counts[max(lines)]


print(part1())
print(part2())
