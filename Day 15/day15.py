from Utils.file_reader import read_lines


def process(upper):
    def take_turn():
        if turn < len(start_nums):
            next_num = start_nums[turn]
        else:
            next_num = turn - 1 - num_turn_map[last_num] if last_num in num_turn_map else 0

        num_turn_map[last_num] = turn - 1

        return next_num

    start_nums = [int(num) for num in read_lines("Input.txt")[0].split(",")]

    last_num = ""
    num_turn_map = {}
    for turn in range(0, upper):
        last_num = take_turn()

    return last_num


def part1():
    return process(2020)


def part2():
    return process(30000000)


print(part1())
print(part2())
