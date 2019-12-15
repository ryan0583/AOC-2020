import math


class ChemAmount:
    def __init__(self, amount, chem):
        self.amount = int(amount)
        self.chem = chem

    def __eq__(self, other):
        return self.chem == other.chem

    def __str__(self):
        return self.chem

    def __hash__(self):
        return hash(str(self))


def consolidate_list(chem_list):
    list_map = {}
    for chem_amount in chem_list:
        existing_chem_amount = list_map.get(chem_amount)
        if existing_chem_amount is None:
            list_map[chem_amount] = chem_amount
        else:
            existing_chem_amount.amount = existing_chem_amount.amount + chem_amount.amount
    return list(filter(lambda value: value.amount > 0, list(list_map.values())))


def create_chem_amounts(line):
    line = line.strip()
    split = line.split(" => ")
    key = ChemAmount(split[1].split()[0], split[1].split()[1])
    val_strs = split[0].split(", ")
    vals = list(map(lambda val_str: ChemAmount(val_str.split()[0], val_str.split()[1]), val_strs))
    return key, vals


def adjust_for_surplus(chem_amount, surplus_chem):
    chem_amount.amount = get_adjusted_chem_amount(chem_amount, surplus_chem, 1)


def get_adjusted_chem_amount(chem_amount, surplus_chem, multiple):
    # print(chem_amount.chem)
    # print(str(chem_amount.amount))

    surplus_chem_number = surplus_chem.get(chem_amount.chem)
    # print("SURPLUS: " + str(surplus_chem_number))
    if surplus_chem_number is not None:
        adjusted_chem_amount = multiple * chem_amount.amount - surplus_chem.get(chem_amount.chem, 0)
        if adjusted_chem_amount < 0:
            adjusted_chem_amount = 0
        # print("NEW CHEM AMOUNT: " + str(adjusted_chem_amount))
        remaining = surplus_chem_number - (chem_amount.amount * multiple)
        surplus_chem[chem_amount.chem] = remaining if remaining >= 0 else 0
        # print("NEW SURPLUS: " + str(surplus_chem[chem_amount.chem]))
        return adjusted_chem_amount
    # print("NEW CHEM AMOUNT: " + str(multiple * chem_amount.amount))
    return multiple * chem_amount.amount


def expand_chem(chem_amount, chem_map, surplus_chem):
    if chem_amount == ORE:
        return [chem_amount]

    if chem_amount.amount == 0:
        return []

    chem_expansion = chem_map.get(chem_amount)
    multiple = math.ceil(chem_amount.amount / chem_expansion[0].amount)

    surplus = multiple * chem_expansion[0].amount - chem_amount.amount
    exiting_surplus = surplus_chem.get(chem_amount.chem)
    if exiting_surplus is None:
        surplus_chem[chem_amount.chem] = surplus
    else:
        surplus_chem[chem_amount.chem] = exiting_surplus + surplus
    # print("WILL HAVE SURPLUS OF: " + str(surplus_chem[chem_amount.chem]))

    return list(
        map(lambda expanded_chem_amount: ChemAmount(
            get_adjusted_chem_amount(expanded_chem_amount, surplus_chem, multiple),
            expanded_chem_amount.chem),
            chem_expansion[1]))


def print_list(list_to_print):
    output = ""
    for chem_amount in list_to_print:
        output += str(chem_amount.amount) + chem_amount.chem + ", "
    print(output)


def create_chem_map(filename):
    lines = open(filename, "r").readlines()
    chem_map = {}
    for line in lines:
        key, vals = create_chem_amounts(line)
        chem_map[key] = key, vals
    return chem_map


def loop_body(chem_map, surplus_chem):
    fuel_chem_list = chem_map.get(FUEL)
    # print_list(fuel_chem_list[1])
    while len(fuel_chem_list[1]) > 1:
        expanded_list = []
        for chem_amount in fuel_chem_list[1]:
            adjust_for_surplus(chem_amount, surplus_chem)
            if chem_amount.amount > 0:
                expanded_list.extend(expand_chem(chem_amount, chem_map, surplus_chem))
        # print(surplus_chem)
        # print_list(expanded_list)
        chem_map[FUEL] = fuel_chem_list[0], consolidate_list(expanded_list)
        fuel_chem_list = chem_map.get(FUEL)
        # print_list(fuel_chem_list[1])
    return fuel_chem_list


def part1(filename):
    surplus_chem = {}
    chem_map = create_chem_map(filename)

    fuel_chem_list = loop_body(chem_map, surplus_chem)

    return fuel_chem_list[1][0].amount


def part2(filename):
    total_ore = 1000000000000
    surplus_chem = {}
    fuel_count = 0

    while total_ore > 0:
        print("ORE REMAINING: " + str(total_ore))
        chem_map = create_chem_map(filename)
        fuel_chem_list = loop_body(chem_map, surplus_chem)
        total_ore -= fuel_chem_list[1][0].amount
        if total_ore >= 0:
            fuel_count += 1

    return str(fuel_count)


FUEL = ChemAmount("0", "FUEL")
ORE = ChemAmount("0", "ORE")

# print(part1("input.txt"))
print(part2("input.txt"))
