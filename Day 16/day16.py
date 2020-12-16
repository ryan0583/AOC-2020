from Utils.file_reader import read_chunks

def find_completely_invalid():
    def check_valid(num_to_check):
        for range in valid_ranges:
            # print(range)
            if int(range[0]) <= int(num_to_check) <= int(range[1]):
                return True
        return False

    chunks = read_chunks('Input.txt')
    # print(chunks)
    valids = chunks[0].split('\n')
    # print(valids)
    valid_ranges = []
    for valid in valids:
        class_index = valid.index(': ')
        numeric_part = valid[class_index + 2:]
        ranges = numeric_part.split(' or ')
        for range in ranges:
            range = [int(number) for number in range.split('-')]
            valid_ranges.append(range)

    # print(valid_ranges)
    invalids = []
    # print(chunks[2])
    number_rows = chunks[2].split('\n')[1:]
    # print(number_rows)
    for number_row in number_rows:
        for number in [int(num) for num in number_row.split(',')]:
            # print(number)
            if not check_valid(number):
                # print('VALID: FALSE')
                invalids.append(number)
            # print('=====================')

    return invalids

def part1():
    return sum(find_completely_invalid())


print(part1())
