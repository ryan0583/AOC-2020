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


def print_node_list(node_list):
    print_str = "Node List is ..."
    for node in node_list:
        print_str += str(node)
    debug_print(debug, print_str)


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

        debug_print(debug, print_node(new_node) + "\n")

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
        debug_print(debug, "\nDone Node " + str(node) + " Count was " + str(node_count) + "\n")
        return node_count

    count = 0
    for node in node_list:
        count += count_node_orbits()
    return count


debug = False
file = open("input.txt", "r")
orbit_data = file.readlines()
print(count_orbits(parse_nodes()))
