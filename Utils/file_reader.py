def read_lines(filename):
    file = open(filename, "r")
    lines = [*file.readlines()]
    file.close()
    return lines


def read_chunks(filename):
    file = open(filename, "r")
    lines = [*file.read().split("\n\n")]
    file.close()
    return lines
