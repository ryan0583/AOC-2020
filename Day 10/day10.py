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
    print(lines)
    chain = [0]
    one_diff = 0
    three_diff = 0
    while max(chain) != max(lines):
        next_diff = add_next()
        if next_diff == 1:
            one_diff += 1
        if next_diff == 3:
            three_diff += 1
    print(chain)
    print(one_diff)
    print(three_diff + 1)
    return one_diff * (three_diff + 1)


def part2():
    def get_next(number):
        valid_next_list = []
        for line in lines:
            if line >= number:
                break
            if line >= number - 3:
                valid_next_list.append(line)
        return valid_next_list

    def process_next(number):
        valid_next_list = get_next(number)
        for valid_next in valid_next_list:
            if valid_next == min(lines):
                paths.append(1)
            else:
                process_next(valid_next)

    lines = sorted([int(row) for row in file_reader.read_lines('TestInput.txt')])
    paths = []
    process_next(max(lines) + 3)
    return len(paths)


# print(part1())
print(part2())
