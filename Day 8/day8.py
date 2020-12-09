from Utils.file_parser import FileParser, JUMP, NO_OP


def part1():
    return FileParser('Input.txt').parse_boot_code().pop()


def try_replacements(find_str, replace_str):
    occurrence_to_replace = 1
    replaced = True
    while replaced:
        file_parser = FileParser('Input.txt')
        replaced = file_parser.replace(find_str, replace_str, occurrence_to_replace)
        if replaced:
            result = file_parser.parse_boot_code()
            if result[0] == 0:
                return result[1]
        occurrence_to_replace += 1
    return False


def part2():
    result = try_replacements(JUMP, NO_OP)
    if not result:
        result = try_replacements(NO_OP, JUMP)
    return result


print(part1())
print(part2())
