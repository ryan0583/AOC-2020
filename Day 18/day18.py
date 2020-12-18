from Utils.file_reader import read_lines


def calc_sum(input):
    def process_brackets(index):
        sub = input[index:]
        close_index = sub.index(")")
        string_in_brackets = sub[0:close_index + 1]
        # print(string_in_brackets)
        bracket_sum = calc_sum(string_in_brackets)
        # print(bracket_sum)
        return [bracket_sum, close_index]

    total = 0
    next_operator = ''

    print('================')
    print(input)

    i = 0
    while i < len(input):
        # print(i)
        char = input[i]

        i += 1

        if char == ')':

            continue

        if char == MULTIPLY or char == ADD:
            next_operator = char
        else:
            if char == '(':
                result = process_brackets(i)
                next_num = result[0]
                i += result[1]
                print("NEW i: " + str(i))
            else:
                next_num = int(char)

            if next_operator == '':
                total = next_num
            elif next_operator == MULTIPLY:
                total *= next_num
            elif next_operator == ADD:
                total += next_num

    print("TOTAL: " + str(total))
    return total


def part1():
    sum_str_lines = read_lines('Input.txt')
    return sum([calc_sum(line.replace(' ', '').replace('\n', '')) for line in sum_str_lines])


MULTIPLY = "*"
ADD = "+"
print(part1())
