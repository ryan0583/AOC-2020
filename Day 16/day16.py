from Utils.file_reader import read_chunks


def get_valid_range(valid_row):
    # print(valid_row)
    colon_index = valid_row.index(': ')
    numeric_part = valid_row[colon_index + 2:]
    ranges = numeric_part.split(' or ')
    valid_ranges = []
    for range in ranges:
        range = [int(number) for number in range.split('-')]
        valid_ranges.append(range)
    # print(valid_ranges)
    return [valid_row[:colon_index], valid_ranges]


def find_completely_invalid(valids, number_rows):
    def check_valid(num_to_check):
        for range in valid_ranges:
            # print(range)
            if int(range[0]) <= int(num_to_check) <= int(range[1]):
                return True
        return False

    # print(valids)
    valid_ranges = []
    for valid in valids:
        range = get_valid_range(valid)[1]
        valid_ranges.append(range[0])
        valid_ranges.append(range[1])

    # print(valid_ranges)

    # print(valid_ranges)
    invalids = []
    # print(chunks[2])
    # print(number_rows)
    for index, number_row in enumerate(number_rows):
        for number in [int(num) for num in number_row.split(',')]:
            # print(number)
            if not check_valid(number):
                # print('VALID: FALSE')
                invalids.append([index, number])
            # print('=====================')

    return invalids


def part1():
    chunks = read_chunks('Input.txt')
    # print(chunks)
    valids = chunks[0].split('\n')
    number_rows = chunks[2].split('\n')[1:]
    return sum([result[1] for result in find_completely_invalid(valids, number_rows)])


def part2():
    chunks = read_chunks('TestInput2.txt')
    # print(chunks)
    valids = chunks[0].split('\n')
    # print(valids)
    number_rows = chunks[2].split('\n')[1:]
    # print(number_rows)
    completely_invalid = find_completely_invalid(valids, number_rows)
    # print(completely_invalid)
    remaining_number_rows = [number_row
                             for i, number_row in enumerate(number_rows)
                             if i not in [valid[0]
                                          for valid in completely_invalid]]

    number_rows_ints = [row.split(',') for row in number_rows]
    # print(number_rows_ints)

    position_to_field_names = {}

    for position in range(0, len(number_rows_ints[0])):
        print("POSITION: " + str(position))
        print("|||||||||||||||||||||")
        all_possible_fields = set()
        for number in [number_row[position] for number_row in number_rows_ints]:
            print("NUMBER: " + str(number))
            this_number_fields = []
            for valid_row in valids:
                field_name_and_ranges = get_valid_range(valid_row)
                print('FIELD NAME: ' + field_name_and_ranges[0])
                print('RANGES: ' + str(field_name_and_ranges[1]))
                ranges = field_name_and_ranges[1]
                # print(ranges)
                for this_range in ranges:
                    # print(this_range)
                    # print(number)
                    if int(this_range[0]) <= int(number) <= int(this_range[1]):
                        print('IS VALID')
                        this_number_fields.append(field_name_and_ranges[0])

            print('FOUND VALIDS: ' + str(this_number_fields))

            if len(all_possible_fields) == 0:
                all_possible_fields = set(this_number_fields)
            else:
                all_possible_fields = set.intersection(all_possible_fields, this_number_fields)

            #Get positions found so far where we definitely know the field.
            definite_fields = [definite
                               for definite in [entry[0]
                                                for entry in position_to_field_names.values()
                                                if len(entry) == 1]]

            print('DEFINITE FIELDS: ' + str(definite_fields))

            #remove from the possible list all the fields we already definitely know
            all_possible_fields = set(
                [poss for poss in all_possible_fields if poss not in definite_fields])

            print('ALL POSSIBLE: ' + str(all_possible_fields))
            print('===================')

            #add the list of remaining possible fields to the map for this position
            position_to_field_names[position] = list(all_possible_fields)

            #if we definitely know which field is for this position go back through all the other entries in the map and
            #remove this field
            if len(all_possible_fields) == 1:
                definite_field = list(all_possible_fields)[0]
                for key in position_to_field_names:
                    if key == position:
                        continue
                    position_to_field_names[key] = [entry
                                                    for entry in position_to_field_names[key]
                                                    if entry != definite_field]
            if len(position_to_field_names[position]) == 1:
                break

        print(position_to_field_names)


# print(part1())
part2()
