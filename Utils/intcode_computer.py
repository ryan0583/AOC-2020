class Instruction:
    def __init__(self, opcode, param1_mode, param2_mode):
        self.opcode = opcode
        self.param1_mode = param1_mode
        self.param2_mode = param2_mode

    @staticmethod
    def get_instruction(value):
        if len(value) > 1:
            opcode = value[len(value) - 2:]
        else:
            opcode = "0" + value[len(value) - 1:]

        param1_mode = PARAM_MODE_LOOKUP
        param2_mode = PARAM_MODE_LOOKUP

        if len(value) > 2:
            param1_mode = value[len(value) - 3:len(value) - 2]

        if len(value) > 3:
            param2_mode = value[len(value) - 4:len(value) - 3]

        return Instruction(opcode, param1_mode, param2_mode)

    def get_opcode(self):
        return self.opcode

    def get_param1_mode(self):
        return self.param1_mode

    def get_param2_mode(self):
        return self.param2_mode

    def __str__(self):
        return self.opcode + ", " + self.param1_mode + ", " + self.param2_mode


class InputCounter:
    def __init__(self, input_count):
        self.input_count = input_count

    def increment_count(self):
        self.input_count += 1

    def get_input_count(self):
        return self.input_count

def process(input_vals, ints):
    def get_val(param_mode, value):
        param_mode_switcher = {
            PARAM_MODE_LOOKUP: lambda: _ints[value],
            PARAM_MODE_DIRECT: lambda: value
        }
        return param_mode_switcher.get(param_mode, lambda: "Invalid param mode" + param_mode)()

    def get_values():
        return (get_val(instruction.get_param1_mode(), _ints[index + 1]),
                get_val(instruction.get_param2_mode(), _ints[index + 2]))

    def perform_input_instruction():
        _ints[_ints[index + 1]] = input_vals[input_counter.get_input_count()]
        input_counter.increment_count()
        return index + 2,

    def perform_add():
        values = get_values()
        _ints[_ints[index + 3]] = values[0] + values[1]
        return index + 4,

    def perform_multiply():
        values = get_values()
        _ints[_ints[index + 3]] = values[0] * values[1]
        return index + 4,

    def perform_jump_if_true():
        val1 = get_val(instruction.param1_mode, _ints[index + 1])
        return get_val(instruction.param2_mode, _ints[index + 2]) if val1 != 0 else index + 3,

    def perform_jump_if_false():
        val1 = get_val(instruction.param1_mode, _ints[index + 1])
        return get_val(instruction.param2_mode, _ints[index + 2]) if val1 == 0 else index + 3,

    def perform_less_than():
        values = get_values()
        _ints[_ints[index + 3]] = 1 if values[0] < values[1] else 0
        return index + 4,

    def perform_equals():
        values = get_values()
        _ints[_ints[index + 3]] = 1 if values[0] == values[1] else 0
        return index + 4,

    def perform_output_instruction():
        return index + 2, get_val(instruction.get_param1_mode(), _ints[index + 1])

    _ints = list(ints)

    opcode_switcher = {
        ADD: perform_add,
        MULTIPLY: perform_multiply,
        INPUT: perform_input_instruction,
        OUTPUT: perform_output_instruction,
        JUMP_IF_TRUE: perform_jump_if_true,
        JUMP_IF_FALSE: perform_jump_if_false,
        LESS_THAN: perform_less_than,
        EQUALS: perform_equals
    }

    index = 0
    last_output = 0
    input_counter = InputCounter(0)
    instruction = Instruction.get_instruction(str(_ints[index]))
    opcode = instruction.get_opcode()
    while opcode != STOP:
        if last_output != 0:
            raise Exception("Output should be 0, but was " + str(last_output))

        result = opcode_switcher.get(opcode, lambda: "Invalid opcode" + opcode)()
        index = result[0]
        if len(result) == 2:
            last_output = result[1]

        instruction = Instruction.get_instruction(str(_ints[index]))
        opcode = instruction.get_opcode()
    return last_output


ADD = "01"
MULTIPLY = "02"
INPUT = "03"
OUTPUT = "04"
JUMP_IF_TRUE = "05"
JUMP_IF_FALSE = "06"
LESS_THAN = "07"
EQUALS = "08"
STOP = "99"

PARAM_MODE_LOOKUP = "0"
PARAM_MODE_DIRECT = "1"
