from Utils.file_reader import read_lines


def part1():
    subject_number = 7

    lines = read_lines('Input.txt')
    card_pub_key = int(lines[0])
    door_pub_key = int(lines[1])

    value = 1
    card_loop_size = 0
    while value != card_pub_key:
        value *= subject_number
        value = value % 20201227
        card_loop_size += 1

    subject_number = door_pub_key
    enc_key = 1
    for i in range(0, card_loop_size):
        enc_key *= subject_number
        enc_key = enc_key % 20201227

    print(enc_key)


part1()
