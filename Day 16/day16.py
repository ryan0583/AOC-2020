import math

from Utils.file_reader import read_chunks


def get_valid_range(valid_row):
    colon_index = valid_row.index(': ')
    numeric_part = valid_row[colon_index + 2:]
    ranges = numeric_part.split(' or ')
    valid_ranges = []
    for range in ranges:
        range = [int(number) for number in range.split('-')]
        valid_ranges.append(range)
    return [valid_row[:colon_index], valid_ranges]


def find_completely_invalid(valids, number_rows):
    def check_valid(num_to_check):
        for range in valid_ranges:
            if int(range[0]) <= int(num_to_check) <= int(range[1]):
                return True
        return False

    valid_ranges = []
    for valid in valids:
        range = get_valid_range(valid)[1]
        valid_ranges.append(range[0])
        valid_ranges.append(range[1])

    invalids = []
    for index, number_row in enumerate(number_rows):
        for number in [int(num) for num in number_row.split(',')]:
            if not check_valid(number):
                invalids.append([index, number])

    return invalids


def part1():
    chunks = read_chunks('Input.txt')
    valids = chunks[0].split('\n')
    number_rows = chunks[2].split('\n')[1:]
    return sum([result[1] for result in find_completely_invalid(valids, number_rows)])


def part2():
    def populate_possible_field_map():
        for position in range(0, len(number_rows_ints[0])):
            all_possible_fields = set()
            for number in [number_row[position] for number_row in number_rows_ints]:
                this_number_fields = []
                for valid_row in valids:
                    field_name_and_ranges = get_valid_range(valid_row)
                    ranges = field_name_and_ranges[1]
                    if int(ranges[0][0]) <= int(number) <= int(ranges[0][1]) \
                            or int(ranges[1][0]) <= int(number) <= int(ranges[1][1]):
                        this_number_fields.append(field_name_and_ranges[0])

                if len(all_possible_fields) == 0:
                    all_possible_fields = set(this_number_fields)
                else:
                    all_possible_fields = set.intersection(all_possible_fields, this_number_fields)

                position_to_field_names[position] = list(all_possible_fields)

    def remove_definitely_known_fields():
        for key in position_to_field_names.keys():
            if len(position_to_field_names[key]) == 1:
                for other_key in position_to_field_names.keys():
                    if key == other_key:
                        continue
                    position_to_field_names[other_key] = [entry
                                                          for entry in position_to_field_names[other_key]
                                                          if entry != position_to_field_names[key][0]]

    chunks = read_chunks('Input.txt')
    valids = chunks[0].split('\n')
    number_rows = chunks[2].split('\n')[1:]
    completely_invalid = find_completely_invalid(valids, number_rows)
    remaining_number_rows = [number_row
                             for i, number_row in enumerate(number_rows)
                             if i not in [valid[0]
                                          for valid in completely_invalid]]

    number_rows_ints = [row.split(',') for row in remaining_number_rows]

    position_to_field_names = {}
    populate_possible_field_map()

    # Now go through the map, find positions for which we definitely know the field, and remove that
    # field from all the other positions. Keep doing that until all positions have only one possible field
    while len([fields for fields in position_to_field_names.values() if len(fields) > 1]) > 0:
        remove_definitely_known_fields()

    departure_positions = [key for key in position_to_field_names if 'departure' in position_to_field_names[key][0]]

    my_rows = [int(num_str) for num_str in chunks[1].split('\n')[1:][0].split(',')]

    return math.prod([num for index, num in enumerate(my_rows) if index in departure_positions])


print(part1())
print(part2())
