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
    def parse_value(line, field_name, total_length):
        try:
            field_index = line.index(field_name)
        except ValueError:
            return False
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
        if value < start_year or value > end_year:
            return False
        return True

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
        value = parse_value(line, 'pid', 13)
        if not value:
            return False
        value = value.rstrip()
        if len(value) == 9 and value.isdigit():
            return True
        return False

    def valid_height(line):
        value = parse_value(line, 'hgt', 9)
        if not value:
            return False
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
        print(valid)
        return valid

    return len(list(filter(lambda valid: valid, list(map(is_valid, read_passports())))))


REQ_FIELDS = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
# print(part1())
print(part2())
