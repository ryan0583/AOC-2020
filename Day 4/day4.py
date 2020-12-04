import os


def is_valid(line):
    for field in required_fields:
        if field not in line:
            return False
    return True


file = open("Input.txt", "r")
lines = list(file.read().split(os.linesep + os.linesep))
required_fields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
print(len(lines))
# print(lines[0])
# print('==========')
# print(lines[1])
# print('==========')
# print(lines[2])
valid_count = 0
for line in lines:
    if is_valid(line):
        valid_count = valid_count + 1

print(valid_count)
file.close()
