from Utils.intcode_computer import IntcodeComputer


def get_all_phase_sequences(phases):
    def add_all_phase_sequences():
        for phase in phases:
            if phase in phase_sequence:
                continue
            phase_sequence.append(phase)
            if len(phase_sequence) == len(phases):
                _phase_sequences.append(list(phase_sequence))
            else:
                add_all_phase_sequences()
            phase_sequence.remove(phase)

    _phase_sequences = []
    phase_sequence = []
    add_all_phase_sequences()
    return _phase_sequences


def process(phase_sequences):
    def find_result():
        last_output = 0
        amps = []
        for phase in phase_sequence:
            amps.append(IntcodeComputer([phase], ints, True))
        while amps[len(amps) - 1].is_running():
            for amp in amps:
                amp.append_input(last_output)
                last_output = amp.process()

        return last_output

    file = open("input.txt", "r")
    ints = list(map(int, file.read().split(",")))
    max_output = 0
    for phase_sequence in phase_sequences:
        output = find_result()
        if output > max_output:
            max_output = output
    return max_output


def part1():
    return process(get_all_phase_sequences([0, 1, 2, 3, 4]))


def part2():
    return process(get_all_phase_sequences([5, 6, 7, 8, 9]))
