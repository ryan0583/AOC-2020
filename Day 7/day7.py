from Utils.intcode_computer import process


def get_all_phase_sequences():
    phases = [0, 1, 2, 3, 4]
    _phase_sequences = []

    for phase1 in phases:
        for phase2 in phases:
            if phase2 == phase1:
                continue
            for phase3 in phases:
                if phase3 == phase2 or phase3 == phase1:
                    continue
                for phase4 in phases:
                    if phase4 == phase3 or phase4 == phase2 or phase4 == phase1:
                        continue
                    for phase5 in phases:
                        if phase5 == phase4 or phase5 == phase3 or phase5 == phase2 or phase5 == phase1:
                            continue
                        _phase_sequences.append([phase1, phase2, phase3, phase4, phase5])

    return _phase_sequences


def find_max_ouput():
    def find_result():
        last_output = 0
        for phase in phase_sequence:
            last_output = process([phase, last_output], ints)
        return last_output

    file = open("input.txt", "r")
    ints = list(map(int, file.read().split(",")))
    phase_sequences = get_all_phase_sequences()
    max_output = 0
    for phase_sequence in phase_sequences:
        output = find_result()
        if output > max_output:
            max_output = output
    return max_output


# file = open("testinput.txt", "r")
# ints = list(map(int, file.read().split(",")))
# print(find_result([4, 3, 2, 1, 0]))

# file = open("testinput2.txt", "r")
# ints = list(map(int, file.read().split(",")))
# print(find_result([0, 1, 2, 3, 4]))

# print(get_all_phase_sequences())

print(find_max_ouput())
