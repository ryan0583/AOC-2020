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

    def __str__(self):
        return self.opcode + ", " + self.param1_mode + ", " + self.param2_mode


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


def perform_input_instruction(index):
    ints[ints[index + 1]] = input
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
    print(ints[index:index + 2])
    if instruction.get_param1_mode() == "1":
        output = ints[index + 1]
    else:
        output = ints[ints[index + 1]]
    global last_output
    last_output = output
    return index + 2


def process():
    index = 0
    val = str(ints[index])
    instruction = process_instruction(str(val))
    opcode = instruction.get_opcode()
    while opcode != "99":
        print(instruction)

        if last_output != 0:
             raise Exception("Oh dear, output should be 0!!, but was " + str(last_output))

        if opcode == "1" or opcode == "2":
            index = perform_calculation(instruction, index)
        elif opcode == "3":
            index = perform_input_instruction(index)
        elif opcode == "4":
            index = perform_ouput_instruction(instruction, index)

        val = str(ints[index])
        instruction = process_instruction(str(val))
        opcode = instruction.get_opcode()


file = open("input.txt", "r")
ints = list(map(int, file.read().split(",")))
input = 1
last_output = 0
process()
print(last_output)
