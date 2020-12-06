def read_lines():
    file = open("Input.txt", "r")
    lines = list(file.readlines())
    file.close()
    return lines


def read_chunks():
    file = open("Input.txt", "r")
    lines = list(file.read().split("\n\n"))
    file.close()
    return lines
