from Utils.file_reader import read_lines


def get_bag_map(lines):
    bag_map = {}
    contain = 'contain'
    for line in lines:
        contains_index = line.find(contain)
        outer_bag = line[0:contains_index].replace('bags', '').replace('bag', '').replace(' ', '')
        inner_bags = line[contains_index + len(contain) + 1:len(line)].replace('bags', '').replace('bag', '').replace(
            ' ', '').replace('\n', '').replace('.', '')
        bag_map[outer_bag] = inner_bags
    return bag_map


def bags_containing_bag_colour(bag_map: dict, bag_colour):
    bag_list = []
    for outer_bag in bag_map.keys():
        if bag_colour in bag_map.get(outer_bag):
            bag_list.append(outer_bag)
    return bag_list


def part1():
    def populate_bag_list(bag_list):
        contain_directly = []
        for bag in bag_list:
            contain_directly.extend(bags_containing_bag_colour(bag_map, bag))

        complete_bag_list.append(set(contain_directly))

        if len(contain_directly) > 0:
            populate_bag_list(contain_directly)

    bag_map = get_bag_map(read_lines())
    complete_bag_list = []
    populate_bag_list(['shinygold'])
    unique_complete_bag_list = set.union(*complete_bag_list)
    print(unique_complete_bag_list)

    return len(unique_complete_bag_list)


def bags_within_bag_colour(bag_map: dict, bag_colour, multiplier):
    bag_list = {}
    if bag_colour in bag_map.keys():
        for bag in bag_map.get(bag_colour).split(','):
            if bag != 'noother':
                bag_list[bag[1:len(bag)]] = int(bag[0]) * multiplier
    return bag_list


def part2():
    def populate_bag_list(bag_map_to_chack):
        contained_directly = []
        for bag in bag_map_to_chack.keys():
            bags_within = bags_within_bag_colour(bag_map, bag, bag_map_to_chack.get(bag))
            if len(bags_within) > 0:
                contained_directly.append(bags_within)

        if len(contained_directly) > 0:
            complete_bag_list.append(contained_directly)

        if len(contained_directly) > 0:
            for bag_counts in contained_directly:
                populate_bag_list(bag_counts)

    bag_map = get_bag_map(read_lines())
    complete_bag_list = []
    populate_bag_list({'shinygold': 1})

    flat_list = []

    for thing in complete_bag_list:
        flat_list.extend(thing)

    final_map = {}

    for this_map in flat_list:
        for key in this_map.keys():
            if key in final_map.keys():
                final_map[key] = int(final_map.get(key)) + int(this_map.get(key))
            else:
                final_map[key] = int(this_map.get(key))

    print(final_map)
    return sum(final_map.values())


# print(part1())

print(part2())
