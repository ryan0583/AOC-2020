from Utils import debug_tools


class IntcodeComputer:
    class __Instruction:
        def __init__(self, value):
            self.opcode = value[len(value) - 2:] if len(value) > 1 else "0" + value[len(value) - 1:]
            self.param1_mode = value[len(value) - 3:len(value) - 2] if len(value) > 2 else PARAM_MODE_POSITION
            self.param2_mode = value[len(value) - 4:len(value) - 3] if len(value) > 3 else PARAM_MODE_POSITION
            self.param3_mode = value[len(value) - 5:len(value) - 4] if len(value) > 4 else PARAM_MODE_POSITION

        def is_stop(self):
            return self.opcode == STOP

        def __str__(self):
            return self.opcode + ", " + self.param1_mode + ", " + self.param2_mode + ", " + self.param3_mode

    def __init__(self, inputs, file_name, return_on_output):
        self.ints = list(map(int, open(file_name, "r").read().split(",")))
        self.inputs = list(inputs)
        self.index = 0
        self.return_on_output = return_on_output
        self.opcode = None
        self.last_output = 0
        self.input_count = 0
        self.rel_offset = 0

    def is_running(self):
        return self.opcode != STOP

    def append_input(self, new_input):
        self.inputs.append(new_input)

    def process(self):
        def grow_list(new_size):
            self.ints += [0] * (new_size - len(self.ints) + 1)

        def read_value_at_position(value):
            return self.ints[value] if value < len(self.ints) else 0

        def read_value(param_mode, param):
            param_mode_switcher = {
                PARAM_MODE_DIRECT: lambda: param,
                PARAM_MODE_POSITION: lambda: read_value_at_position(param),
                PARAM_MODE_RELATIVE: lambda: read_value_at_position(param + self.rel_offset)
            }
            return param_mode_switcher.get(param_mode, lambda: debug_tools.raise_("Invalid param mode" + param_mode))()

        def read_values():
            return (read_value(next_instruction.param1_mode, self.ints[self.index + 1]),
                    read_value(next_instruction.param2_mode, self.ints[self.index + 2]))

        def get_write_index(param_mode, index):
            param_mode_switcher = {
                PARAM_MODE_DIRECT: lambda: index,
                PARAM_MODE_POSITION: lambda: self.ints[index],
                PARAM_MODE_RELATIVE: lambda: self.ints[index] + self.rel_offset
            }
            return param_mode_switcher.get(param_mode, lambda: debug_tools.raise_("Invalid param mode" + param_mode))()

        def add(val1, val2):
            return val1 + val2

        def multiply(val1, val2):
            return val1 * val2

        def less_than(val1, val2):
            return 1 if val1 < val2 else 0

        def equals(val1, val2):
            return 1 if val1 == val2 else 0

        def get_write_index_and_grow():
            write_index = get_write_index(next_instruction.param3_mode, self.index + 3)
            grow_list(write_index)
            return write_index

        def perform_logic_and_write(func):
            self.ints[get_write_index_and_grow()] = func(*read_values())
            return self.index + 4

        def perform_input():
            write_index = get_write_index_and_grow()
            self.ints[write_index] = self.inputs[self.input_count]
            self.input_count += 1
            return self.index + 2

        def perform_add():
            return perform_logic_and_write(add)

        def perform_multiply():
            return perform_logic_and_write(multiply)

        def perform_jump_if_true():
            val1, val2 = read_values()
            return val2 if val1 != 0 else self.index + 3

        def perform_jump_if_false():
            val1, val2 = read_values()
            return val2 if val1 == 0 else self.index + 3

        def perform_less_than():
            return perform_logic_and_write(less_than)

        def perform_equals():
            return perform_logic_and_write(equals)

        def perform_output():
            self.last_output = read_value(next_instruction.param1_mode, self.ints[self.index + 1])
            return self.index + 2

        def perform_adjust_rel_offset():
            self.rel_offset += read_value(next_instruction.param1_mode, self.ints[self.index + 1])
            return self.index + 2

        def should_return_output():
            return self.opcode == OUTPUT and self.return_on_output

        def invalid_output():
            return self.opcode == OUTPUT and not next_instruction.is_stop() and self.last_output != 0

        opcode_switcher = {
            ADD: perform_add,
            MULTIPLY: perform_multiply,
            INPUT: perform_input,
            OUTPUT: perform_output,
            JUMP_IF_TRUE: perform_jump_if_true,
            JUMP_IF_FALSE: perform_jump_if_false,
            LESS_THAN: perform_less_than,
            EQUALS: perform_equals,
            ADJUST_REL_OFFSET: perform_adjust_rel_offset
        }

        next_instruction = self.__Instruction(str(self.ints[self.index]))
        self.opcode = next_instruction.opcode
        while self.is_running():
            self.index = opcode_switcher.get(self.opcode,
                                             lambda: debug_tools.raise_(Exception("Invalid opcode" + self.opcode)))()

            next_instruction = self.__Instruction(str(self.ints[self.index]))

            if should_return_output():
                break
            if invalid_output():
                raise Exception("Expected last output to be 0, but was " + str(self.last_output))

            self.opcode = next_instruction.opcode

        return self.last_output


ADD = "01"
MULTIPLY = "02"
INPUT = "03"
OUTPUT = "04"
JUMP_IF_TRUE = "05"
JUMP_IF_FALSE = "06"
LESS_THAN = "07"
EQUALS = "08"
ADJUST_REL_OFFSET = "09"
STOP = "99"

PARAM_MODE_POSITION = "0"
PARAM_MODE_DIRECT = "1"
PARAM_MODE_RELATIVE = "2"
