from Utils.debug_tools import debug_print


class Node:
    def __init__(self, name):
        self.name = name
        self.next_node = None

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name


class StepCount:
    def __init__(self, node_name, num_steps):
        self.node_name = node_name
        self.num_steps = num_steps

    def get_node_name(self):
        return self.node_name

    def get_num_steps(self):
        return self.num_steps

    def __str__(self):
        return self.node_name + ", " + str(self.num_steps)


def print_node_list(node_list):
    print_str = "Node List is ..."
    for node in node_list:
        print_str += str(node)


def parse_nodes():
    def create_node():
        new_node = Node(orbit_obj_name)
        for node in node_list:
            if node.get_name() == main_obj_name:
                new_node.set_next_node(node)
                break

        if new_node.get_next_node() is None:
            next_node = Node(main_obj_name)
            new_node.set_next_node(next_node)

        for node in node_list:
            next_node = node.get_next_node()
            if next_node is not None and next_node.get_name() == orbit_obj_name:
                node.set_next_node(new_node)

        return new_node

    node_list = []
    for orbit in orbit_data:
        split = orbit.split(")")
        main_obj_name = split[0].strip()
        orbit_obj_name = split[1].strip()
        node_list.append(create_node())

    return node_list


def print_node(node):
    print_str = str(node)
    next_node = node.get_next_node()
    while next_node is not None:
        print_str += " orbits " + str(next_node)
        next_node = next_node.get_next_node()
    return print_str


def count_orbits(node_list):
    def count_node_orbits():
        node_count = 0
        next_node = node.get_next_node()
        while next_node is not None:
            node_count += 1
            next_node = next_node.get_next_node()
        return node_count

    count = 0
    for node in node_list:
        count += count_node_orbits()
    return count


def find_node_for_name(node_list, name):
    for node in node_list:
        if node.get_name() == name:
            return node


def get_steps(node):
    steps = []
    step_count = 0
    next_node = node.get_next_node()
    while next_node is not None:
        step = StepCount(next_node.get_name(), step_count)
        debug_print(debug, step)
        steps.append(step)
        step_count += 1
        next_node = next_node.get_next_node()
    return steps


def find_common_node(you_steps, san_node):
    total_steps = 0
    step_count = 0
    found = False
    next_node = san_node.get_next_node()
    while not found and next_node is not None:
        for step in you_steps:
            if step.get_node_name() == next_node.get_name():
                debug_print(debug, "Common node is " + step.get_node_name())
                total_steps = step.get_num_steps() + step_count
                found = True
        step_count += 1
        next_node = next_node.get_next_node()
    return total_steps


def part_one():
    print(count_orbits(parse_nodes()))


def part_two():
    nodes = parse_nodes()
    you_node = find_node_for_name(nodes, "YOU")
    you_steps = get_steps(you_node)
    san_node = find_node_for_name(nodes, "SAN")
    print(find_common_node(you_steps, san_node))


debug = False
file = open("input.txt", "r")
orbit_data = file.readlines()
# part_one()
part_two()
