def read_lines():
    file = open("Input.txt", "r")
    lines = list(file.readlines())
    file.close()
    return lines
