class Instruction:
    def __init__(self, opcode, param1_mode, param2_mode):
        self.opcode = opcode
        self.param1_mode = param1_mode
        self.param2_mode = param2_mode

    def get_opcode(self):
        return self.opcode

    def get_param1_mode(self):
        return self.param1_mode

    def get_param2_mode(self):
        return self.param2_mode


def process_instruction(value):
    opcode = value[len(value) - 1:]
    param1_mode = "0"
    param2_mode = "0"

    if len(value) > 2:
        param1_mode = value[len(value) - 3:len(value) - 2]

    if len(value) > 3:
        param2_mode = value[len(value) - 4:len(value) - 3]

    return Instruction(opcode, param1_mode, param2_mode)


def get_val(param_mode, list, value):
    if param_mode == "1":
        return value
    return list[value]


def perform_input_instruction(index, value):
    ints[ints[index + 1]] = value
    return index + 2


def perform_calculation(instruction, index):
    val1 = get_val(instruction.get_param1_mode(), ints, ints[index + 1])
    val2 = get_val(instruction.get_param2_mode(), ints, ints[index + 2])
    if instruction.get_opcode() == "1":
        val = val1 + val2
    else:
        val = val1 * val2
    ints[ints[index + 3]] = val
    return index + 4


def perform_ouput_instruction(instruction, index):
    if instruction.get_param1_mode == "1":
        output = ints[index + 1]
    else:
        output = ints[ints[index + 1]]
    if output != 0:
        raise Exception("Oh dear, output should be 0!!")
    return index + 2


# def calculate_output(noun, verb):
#     local_ints = list(ints)
#     local_ints[1] = noun
#     local_ints[2] = verb
#     index = 0
#     opcode = local_ints[index]
#     while opcode != 99:
#         index1 = local_ints[index + 1]
#         index2 = local_ints[index + 2]
#         index3 = local_ints[index + 3]
#         val1 = local_ints[index1]
#         val2 = local_ints[index2]
#         if opcode == 1:
#             val = val1 + val2
#         else:
#             val = val1 * val2
#         local_ints[index3] = val
#         index = index + 4
#         opcode = local_ints[index]
#     return local_ints[0]


# def part_one():
#     print(calculate_output(12, 2))


file = open("input.txt", "r")
ints = list(map(int, file.read().split(",")))
# part_one()
