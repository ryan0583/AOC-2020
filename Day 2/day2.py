def calculate_output(noun, verb):
    local_ints = list(ints)
    local_ints[1] = noun
    local_ints[2] = verb
    index = 0
    opcode = local_ints[index]
    while opcode != 99:
        index1 = local_ints[index + 1]
        index2 = local_ints[index + 2]
        index3 = local_ints[index + 3]
        val1 = local_ints[index1]
        val2 = local_ints[index2]
        if opcode == 1:
            val = val1 + val2
        else:
            val = val1 * val2
        local_ints[index3] = val
        index = index + 4
        opcode = local_ints[index]
    return local_ints[0]


def part_one():
    print(calculate_output(12, 2))


def part_two():
    exp = 19690720
    for noun in range(100):
        for verb in range(100):
            if calculate_output(noun, verb) == exp:
                print(100 * noun + verb)
                break


file = open("input.txt", "r")
ints = list(map(int, file.read().split(",")))
part_one()
part_two()
