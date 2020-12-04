import os


def part1():
    def is_valid(line):
        for field in REQ_FIELDS:
            if field not in line:
                return False
        return True

    file = open("Input.txt", "r")
    lines = list(file.read().split(os.linesep + os.linesep))
    file.close()
    return len(list(filter(lambda valid: valid, list(map(is_valid, lines)))))


REQ_FIELDS = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
print(part1())
