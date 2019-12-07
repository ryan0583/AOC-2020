class IntcodeComputer:
    class Instruction:
        def __init__(self, value):
            self.opcode = value[len(value) - 2:] if len(value) > 1 else "0" + value[len(value) - 1:]
            self.param1_mode = value[len(value) - 3:len(value) - 2] if len(value) > 2 else PARAM_MODE_LOOKUP
            self.param2_mode = value[len(value) - 4:len(value) - 3] if len(value) > 3 else PARAM_MODE_LOOKUP

        def is_stop(self):
            return self.opcode == STOP

        def __str__(self):
            return self.opcode + ", " + self.param1_mode + ", " + self.param2_mode

    def __init__(self, inputs, ints, return_on_output):
        self.ints = list(ints)
        self.inputs = list(inputs)
        self.index = 0
        self.return_on_output = return_on_output
        self.opcode = None
        self.last_output = 0
        self.input_count = 0

    def is_running(self):
        return self.opcode != STOP

    def append_input(self, new_input):
        self.inputs.append(new_input)

    def process(self):
        def get_val(param_mode, value):
            param_mode_switcher = {
                PARAM_MODE_LOOKUP: lambda: self.ints[value],
                PARAM_MODE_DIRECT: lambda: value
            }
            return param_mode_switcher.get(param_mode, lambda: "Invalid param mode" + param_mode)()

        def get_values():
            return (get_val(next_instruction.param1_mode, self.ints[self.index + 1]),
                    get_val(next_instruction.param2_mode, self.ints[self.index + 2]))

        def perform_input():
            self.ints[self.ints[self.index + 1]] = self.inputs[self.input_count]
            self.input_count += 1
            return self.index + 2

        def perform_add():
            values = get_values()
            self.ints[self.ints[self.index + 3]] = values[0] + values[1]
            return self.index + 4

        def perform_multiply():
            values = get_values()
            self.ints[self.ints[self.index + 3]] = values[0] * values[1]
            return self.index + 4

        def perform_jump_if_true():
            val1 = get_val(next_instruction.param1_mode, self.ints[self.index + 1])
            return get_val(next_instruction.param2_mode, self.ints[self.index + 2]) if val1 != 0 else self.index + 3

        def perform_jump_if_false():
            val1 = get_val(next_instruction.param1_mode, self.ints[self.index + 1])
            return get_val(next_instruction.param2_mode, self.ints[self.index + 2]) if val1 == 0 else self.index + 3

        def perform_less_than():
            values = get_values()
            self.ints[self.ints[self.index + 3]] = 1 if values[0] < values[1] else 0
            return self.index + 4

        def perform_equals():
            values = get_values()
            self.ints[self.ints[self.index + 3]] = 1 if values[0] == values[1] else 0
            return self.index + 4

        def perform_output():
            self.last_output = get_val(next_instruction.param1_mode, self.ints[self.index + 1])
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
            EQUALS: perform_equals
        }

        next_instruction = self.Instruction(str(self.ints[self.index]))
        self.opcode = next_instruction.opcode
        while self.is_running():
            self.index = opcode_switcher.get(self.opcode, lambda: "Invalid opcode" + self.opcode)()

            next_instruction = self.Instruction(str(self.ints[self.index]))

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
STOP = "99"

PARAM_MODE_LOOKUP = "0"
PARAM_MODE_DIRECT = "1"
