from Utils.file_reader import read_lines


def parse_line(lines, current_instruction, accumulator, processed_lines):
    line = lines[current_instruction]
    command_and_number = line.split(' ')
    command = command_and_number[0].replace(' ', '')
    number = int(command_and_number[1].replace(' ', ''))
    next_instruction = current_instruction
    if command == 'acc':
        next_instruction += 1
        accumulator += number
    elif command == 'jmp':
        next_instruction += number
    elif command == 'nop':
        next_instruction += 1

    if next_instruction in processed_lines:
        return [1, accumulator]

    if next_instruction >= len(lines):
        return [0, accumulator]

    processed_lines.add(next_instruction)
    return parse_line(lines, next_instruction, accumulator, processed_lines)


def part1():
    lines = read_lines()
    return parse_line(lines, 0, 0, {0}).pop()


def replace(lines, thing_to_replace, find, replace):
    found = 0
    for i, line in enumerate(lines):
        command_and_number = line.split(' ')
        command = command_and_number[0].replace(' ', '')
        if command == find:
            found += 1
        if found == thing_to_replace:
            lines[i] = line.replace(find, replace)
            return True
    return False


def part2():
    jmp_to_replace = 1
    replaced_jmp = True
    while replaced_jmp:
        lines = read_lines()
        replaced_jmp = replace(lines, jmp_to_replace, 'jmp', 'nop')
        if replaced_jmp:
            result = parse_line(lines, 0, 0, {0})
            if result[0] == 0:
                return result[1]
        jmp_to_replace += 1

    nop_to_replace = 1
    replaced_nop = True
    while replaced_nop:
        lines = read_lines()
        replaced_nop = replace(lines, nop_to_replace, 'jmp', 'nop')
        if replaced_jmp:
            result = parse_line(lines, 0, 0, {0})
            if result[0] == 0:
                return result[1]
        nop_to_replace += 1


print(part1())
print(part2())
