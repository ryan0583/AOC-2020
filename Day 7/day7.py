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
    def count_bags(bag_list, complete_bag_list):
        new_count = 0
        contain_directly = []
        for bag in bag_list:
            contain_directly.extend(bags_containing_bag_colour(bag_map, bag))
            new_count += len(contain_directly)

        contain_directly = set(contain_directly)
        complete_bag_list.append(contain_directly)

        if len(contain_directly) > 0:
            count_bags(contain_directly, complete_bag_list)

    bag_map = get_bag_map(read_lines())
    complete_bag_list = []
    count_bags(['shinygold'], complete_bag_list)
    print(complete_bag_list)

    unique_complete_bag_list = set.union(*complete_bag_list)

    print(unique_complete_bag_list)

    print(len(unique_complete_bag_list))


part1()
