class IntcodeComputer:
    class __Instruction:
        def __init__(self, value):
            self.opcode = value[len(value) - 2:] if len(value) > 1 else "0" + value[len(value) - 1:]
            self.param1_mode = value[len(value) - 3:len(value) - 2] if len(value) > 2 else PARAM_MODE_LOOKUP
            self.param2_mode = value[len(value) - 4:len(value) - 3] if len(value) > 3 else PARAM_MODE_LOOKUP
            self.param3_mode = value[len(value) - 5:len(value) - 4] if len(value) > 4 else PARAM_MODE_DIRECT

        def is_stop(self):
            return self.opcode == STOP

        def __str__(self):
            return self.opcode + ", " + self.param1_mode + ", " + self.param2_mode + ", " + self.param3_mode

    def __init__(self, inputs, ints, return_on_output):
        self.ints = list(ints)
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

        def get_val_lookup(value):
            return self.ints[value] if value < len(self.ints) else 0

        def get_val(param_mode, value):
            def get_val_relative():
                return get_val_lookup(value + self.rel_offset)

            param_mode_switcher = {
                PARAM_MODE_LOOKUP: lambda: get_val_lookup(value),
                PARAM_MODE_DIRECT: lambda: value,
                PARAM_MODE_RELATIVE: get_val_relative
            }
            return param_mode_switcher.get(param_mode, lambda: "Invalid param mode" + param_mode)()

        def get_values():
            return (get_val(next_instruction.param1_mode, self.ints[self.index + 1]),
                    get_val(next_instruction.param2_mode, self.ints[self.index + 2]))

        def perform_input():
            lookup_index = self.ints[self.index + 1]
            if next_instruction.param1_mode == PARAM_MODE_RELATIVE:
                lookup_index += self.rel_offset

            grow_list(lookup_index)
            self.ints[lookup_index] = self.inputs[self.input_count]
            self.input_count += 1
            return self.index + 2

        def perform_add():
            values = get_values()
            lookup_index = self.ints[self.index + 3]
            if next_instruction.param3_mode == PARAM_MODE_RELATIVE:
                lookup_index += self.rel_offset
            grow_list(lookup_index)
            self.ints[lookup_index] = values[0] + values[1]
            return self.index + 4

        def perform_multiply():
            values = get_values()
            lookup_index = self.ints[self.index + 3]
            if next_instruction.param3_mode == PARAM_MODE_RELATIVE:
                lookup_index += self.rel_offset
            grow_list(lookup_index)
            self.ints[lookup_index] = values[0] * values[1]
            return self.index + 4

        def perform_jump_if_true():
            val1 = get_val(next_instruction.param1_mode, self.ints[self.index + 1])
            return get_val(next_instruction.param2_mode, self.ints[self.index + 2]) if val1 != 0 else self.index + 3

        def perform_jump_if_false():
            val1 = get_val(next_instruction.param1_mode, self.ints[self.index + 1])
            return get_val(next_instruction.param2_mode, self.ints[self.index + 2]) if val1 == 0 else self.index + 3

        def perform_less_than():
            values = get_values()
            lookup_index = self.ints[self.index + 3]
            if next_instruction.param3_mode == PARAM_MODE_RELATIVE:
                lookup_index += self.rel_offset
            grow_list(lookup_index)
            self.ints[lookup_index] = 1 if values[0] < values[1] else 0
            return self.index + 4

        def perform_equals():
            values = get_values()
            lookup_index = self.ints[self.index + 3]
            if next_instruction.param3_mode == PARAM_MODE_RELATIVE:
                lookup_index += self.rel_offset
            grow_list(lookup_index)
            self.ints[lookup_index] = 1 if values[0] == values[1] else 0
            return self.index + 4

        def perform_output():
            self.last_output = get_val(next_instruction.param1_mode, self.ints[self.index + 1])
            print(self.last_output)
            return self.index + 2

        def perform_adjust_rel_offset():
            self.rel_offset += get_val(next_instruction.param1_mode, self.ints[self.index + 1])
            # print(self.rel_offset)
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
            # print(self.index)
            # print(self.ints)
            self.index = opcode_switcher.get(self.opcode, lambda: print("Invalid opcode" + self.opcode))()

            # print(self.opcode)
            # print(self.last_output)

            next_instruction = self.__Instruction(str(self.ints[self.index]))

            if should_return_output():
                break
            # if invalid_output():
            # raise Exception("Expected last output to be 0, but was " + str(self.last_output))

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

PARAM_MODE_LOOKUP = "0"
PARAM_MODE_DIRECT = "1"
PARAM_MODE_RELATIVE = "2"
