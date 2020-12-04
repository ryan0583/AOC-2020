import os


def read_passports():
    file = open("Input.txt", "r")
    lines = list(file.read().split(os.linesep + os.linesep))
    file.close()
    return lines


def part1():
    def is_valid(line):
        for field in REQ_FIELDS:
            if field not in line:
                return False
        return True

    return len(list(filter(lambda valid: valid, list(map(is_valid, read_passports())))))


def part2():
    def get_field_index(line, field_name):
        try:
            return line.index(field_name)
        except ValueError:
            return -1

    def parse_value(line, field_name, total_length):
        field_index = get_field_index(line, field_name)
        if field_index == -1:
            return False
        if len(line) < field_index + total_length:
            return False
        field_and_value = line[field_index: field_index + total_length]
        return field_and_value[field_and_value.index(':') + 1: len(field_and_value)]

    def valid_year(line, field_name, start_year, end_year):
        value = int(parse_value(line, field_name, 8))
        if not value:
            return False
        if start_year <= value <= end_year:
            return True
        return False

    def valid_eye_colour(line):
        valid_colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        value = parse_value(line, 'ecl', 7)
        if value and value in valid_colours:
            return True
        return False

    def valid_hair_colour(line):
        valid_chars = '0123456789abcdef'
        value = parse_value(line, 'hcl', 11)
        if not value:
            return False
        value = value.rstrip()
        if len(value) == 7 \
                and value[0] == '#' \
                and all(c in valid_chars for c in value[1:len(value)]):
            return True
        return False

    def valid_passport_id(line):
        value = parse_value(line, 'pid', 14)
        if not value:
            value = parse_value(line, 'pid', 13)
            if not value:
                return False
        value = value.rstrip()
        if len(value) == 9 and value.isdigit():
            return True
        return False

    def valid_height(line):
        field_index = get_field_index(line, 'hgt')
        if field_index == -1:
            return False

        value = line[field_index + 4:len(line)]
        if 'cm' in value:
            value = int(value[0:value.index('cm')])
            if 150 <= value <= 193:
                return True
        elif 'in' in value:
            value = int(value[0:value.index('in')])
            if 59 <= value <= 76:
                return True
        return False

    def is_valid(passport):
        valid = valid_year(passport, 'byr', 1920, 2002) \
                and valid_year(passport, 'iyr', 2010, 2020) \
                and valid_year(passport, 'eyr', 2020, 2030) \
                and valid_eye_colour(passport) \
                and valid_passport_id(passport) \
                and valid_hair_colour(passport) \
                and valid_height(passport)
        return valid

    return len(list(filter(lambda valid: valid, list(map(is_valid, read_passports())))))


REQ_FIELDS = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
# print(part1())
print(part2())
