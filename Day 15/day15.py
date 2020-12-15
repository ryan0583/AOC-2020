from Utils.file_reader import read_lines


def process(max):
    def take_turn():
        print("TURN: " + str(turn))
        # print("LAST: " + str(last_num))

        if turn < len(start_nums):
            next_num = start_nums[turn]
        elif last_num in num_turn_map.keys() and len(num_turn_map[last_num]) > 1:
            turns_seen = num_turn_map[last_num]
            next_num = turns_seen[-1] - turns_seen[-2]
        else:
            next_num = 0

        if next_num not in num_turn_map.keys():
            num_turn_map[next_num] = []
        num_turn_map[next_num].append(turn)

        # print("=============")
        return next_num

    start_nums = [int(num) for num in read_lines("Input.txt")[0].split(",")]

    last_num = -1
    num_turn_map = {}
    for turn in range(0, max):
        last_num = take_turn()

    return last_num


def part1():
    return process(2020)


def part2():
    return process(30000000)


print(part1())
# print(part2())
