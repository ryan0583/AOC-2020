from Utils.intcode_computer import IntcodeComputer


def get_all_phase_sequences(phases):
    def add_all_phase_sequences():
        for phase in phases:
            if phase in phase_sequence:
                continue
            phase_sequence.append(phase)
            _phase_sequences.append(list(phase_sequence)) if len(phase_sequence) == 5 else add_all_phase_sequences()
            phase_sequence.remove(phase)

    _phase_sequences = []
    phase_sequence = []
    add_all_phase_sequences()
    return _phase_sequences


def find_part1_result(phase_sequence, ints):
    last_output = 0

    for phase in phase_sequence:
        last_amp = IntcodeComputer([phase, last_output], ints, True)
        last_output = last_amp.process()

    return last_output


def find_part2_result(phase_sequence, ints):
    last_output = 0
    amps = [IntcodeComputer([phase_sequence[0]], ints, True),
            IntcodeComputer([phase_sequence[1]], ints, True),
            IntcodeComputer([phase_sequence[2]], ints, True),
            IntcodeComputer([phase_sequence[3]], ints, True),
            IntcodeComputer([phase_sequence[4]], ints, True)]
    while not amps[4].is_stopped():
        for amp in amps:
            amp.append_input_val(last_output)
            last_output = amp.process()

    return last_output


def process(find_result, phases):
    file = open("input.txt", "r")
    ints = list(map(int, file.read().split(",")))
    phase_sequences = get_all_phase_sequences(phases)
    max_output = 0
    for phase_sequence in phase_sequences:
        output = find_result(phase_sequence, ints)
        if output > max_output:
            max_output = output
    return max_output


def part1():
    return process(find_part1_result, [0, 1, 2, 3, 4])


def part2():
    return process(find_part2_result, [5, 6, 7, 8, 9])
