from Utils.intcode_computer import IntcodeComputer


def get_all_phase_sequences(phases):
    def process_phase(phase):
        if phase in phase_sequence:
            return
        phase_sequence.append(phase)
        if len(phase_sequence) == len(phases):
            phase_sequences.append(list(phase_sequence))
        else:
            add_all_phase_sequences()
        phase_sequence.remove(phase)

    def add_all_phase_sequences():
        return list(map(process_phase, phases))

    phase_sequences = []
    phase_sequence = []
    add_all_phase_sequences()
    return phase_sequences


def process(phase_sequences):
    def find_result(phase_sequence):
        last_output = 0
        amps = list(map(lambda phase: IntcodeComputer([phase], "input.txt", True), phase_sequence))

        while amps[len(amps) - 1].is_running():
            for amp in amps:
                amp.append_input(last_output)
                last_output = amp.process()

        return last_output

    return max(map(find_result, phase_sequences))


def part1():
    return process(get_all_phase_sequences([0, 1, 2, 3, 4]))


def part2():
    return process(get_all_phase_sequences([5, 6, 7, 8, 9]))
