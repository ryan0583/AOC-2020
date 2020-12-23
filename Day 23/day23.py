from Utils.file_reader import read_lines


def part1():
    def move(current_line):
        print(current_line)
        print(current_cup)

        new_line = current_line

        current_index = line.index(current_cup)
        removed_cups = ''

        for times in range(0, 3):
            next_index = (current_index + 1) % len(new_line)

            num = new_line[next_index]
            new_line = new_line[:next_index] + new_line[next_index + 1:]
            print(new_line)

            removed_cups += num

            current_index = new_line.index(current_cup)

        print(removed_cups)

        dest_cup = int(current_cup) - 1
        min_cup = min([int(c) for c in current_line])
        max_cup = max([int(c) for c in current_line])
        while str(dest_cup) not in new_line:
            dest_cup -= 1
            if dest_cup < min_cup:
                dest_cup = max_cup

        print(dest_cup)
        dest_index = new_line.index(str(dest_cup))
        new_line = new_line[:dest_index + 1] + removed_cups + new_line[dest_index + 1:]

        print(new_line)
        print('================')

        return new_line

    line = read_lines('Input.txt')[0]

    current_cup = line[0]

    for i in range(0, 100):
        print('MOVE: ' + str(i + 1))
        line = move(line)
        next_cup_index = (line.index(str(current_cup)) + 1) % len(line)
        current_cup = line[next_cup_index]

    print(line)


part1()
