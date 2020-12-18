from Utils.file_reader import read_lines


def calc_sum(input, print_total):
    def process_brackets(index):
        sub = input[index:]
        return calc_sum(sub, False)

    total = 0
    next_operator = ''

    # print('================')
    # print(input)

    i = 0
    while i < len(input):
        # print(i)
        char = input[i]
        # print(char)

        i += 1

        if char == ')':
            return [total, i]

        if char == MULTIPLY or char == ADD:
            next_operator = char
        else:
            if char == '(':
                if print_total:
                    print("FOUND BRACKET, RECURSING")
                result = process_brackets(i)
                next_num = result[0]
                i += result[1]
                # print("NEW i: " + str(i))
            else:
                next_num = int(char)

            if next_operator == '':
                total = next_num
            elif next_operator == MULTIPLY:
                total *= next_num
            elif next_operator == ADD:
                total += next_num

            if print_total:
                print(total)

    # print(total)
    return [total, i]


def calc_sum_part2(input, print_total):
    def process_brackets(index):
        sub = input[index:]
        return calc_sum_part2(sub, False)

    total = 1
    plus_total = 0
    next_operator = ''

    # print('================')
    print(input)

    i = 0
    while i < len(input):
        # print(i)
        char = input[i]
        print(char)

        i += 1

        if char == ')':
            print("CLOSING BRACKET FOUND, RETURNING")
            if plus_total > 0:
                total = plus_total * total
            return [total, i]

        if char == MULTIPLY or char == ADD:
            next_operator = char
            if char == MULTIPLY:
                total *= plus_total
                plus_total = 0
        else:
            if char == '(':
                if print_total:
                    print("FOUND BRACKET, RECURSING")
                result = process_brackets(i)
                next_num = result[0]
                i += result[1]
                # print("NEW i: " + str(i))
            else:
                next_num = int(char)

            if next_operator == '':
                plus_total = next_num
            else:
                plus_total += next_num

        if print_total:
            print("PLUS_TOTAL: " + str(plus_total))
            print("TOTAL: " + str(total))
            print('=======')

    # print(total)
    if plus_total > 0:
        total = plus_total * total
    return [total, i]


def part1():
    sum_str_lines = read_lines('Input.txt')
    return sum([calc_sum(line.replace(' ', '').replace('\n', ''), True)[0] for line in sum_str_lines])


def part2():
    sum_str_lines = read_lines('Input.txt')
    return sum([calc_sum_part2(line.replace(' ', '').replace('\n', ''), True)[0] for line in sum_str_lines])


MULTIPLY = "*"
ADD = "+"
# print("sum of all results: " + str(part1()))

print("sum of all results: " + str(part2()))
