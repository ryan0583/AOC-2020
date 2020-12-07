from itertools import chain

from Utils.file_reader import read_lines


def get_bag_map(lines):
    def strip_formatting(substring):
        return substring.replace('bags', '') \
            .replace('bag', '') \
            .replace(' ', '') \
            .replace('\n', '') \
            .replace('.', '')

    def get_key(this_line):
        contains_index = this_line.find(contain)
        return strip_formatting(this_line[0:contains_index])

    def get_value(this_line):
        contains_index = this_line.find(contain)
        return strip_formatting(this_line[contains_index + len(contain) + 1:len(this_line)])

    contain = 'contain'
    return {get_key(line): get_value(line) for line in lines}


def part1():
    def bags_containing_bag_colour(bag_colour):
        return {key for key in bag_map.keys() if bag_colour in bag_map.get(key)}

    def populate_bag_list(bag_list):
        if len(bag_list) == 0:
            return

        contain_directly = list(chain.from_iterable(map(bags_containing_bag_colour, bag_list)))
        complete_bag_list.update(set(contain_directly))
        populate_bag_list(contain_directly)

    bag_map = get_bag_map(read_lines())
    complete_bag_list = set()
    populate_bag_list(['shinygold'])

    return len(complete_bag_list)


def part2():
    def has_count(bag):
        return bag != 'noother'

    def bags_within_bag_colour(bag_count_item):
        bag_count_list = list(filter(has_count, bag_map.get(bag_count_item[0]).split(',')))
        return {bag[1:len(bag)]: int(bag[0]) * bag_count_item[1] for bag in bag_count_list}

    def bags_within_non_empty(bags_within):
        return len(bags_within) > 0

    def get_contained_directly(bag_count_items):
        return list(filter(bags_within_non_empty, map(bags_within_bag_colour, bag_count_items)))

    def populate_bag_list(bag_count_map):
        contained_directly = get_contained_directly(bag_count_map.items())

        if len(contained_directly) > 0:
            complete_list.extend(contained_directly)

        if len(contained_directly) > 0:
            for bag_count_direct_map in contained_directly:
                populate_bag_list(bag_count_direct_map)

    bag_map = get_bag_map(read_lines())
    complete_list = []
    populate_bag_list({'shinygold': 1})
    return sum(chain.from_iterable({this_map.values() for this_map in complete_list}))


print(part1())
print(part2())
