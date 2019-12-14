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
    return list(list_map.values())


def create_chem_amounts(line):
    line = line.strip()
    split = line.split(" => ")
    key = ChemAmount(split[1].split()[0], split[1].split()[1])
    val_strs = split[0].split(", ")
    vals = list(map(lambda val_str: ChemAmount(val_str.split()[0], val_str.split()[1]), val_strs))
    return key, vals


def expand_chem(chem_amount, chem_map):
    if chem_amount == ORE:
        return [chem_amount]
    chem_expansion = chem_map.get(chem_amount)
    multiple = math.ceil(chem_amount.amount / chem_expansion[0].amount)
    return list(
        map(lambda expanded_chem_amount: ChemAmount(multiple * expanded_chem_amount.amount, expanded_chem_amount.chem),
            chem_expansion[1]))


def part1():
    lines = open("testinput.txt", "r").readlines()
    chem_map = {}
    for line in lines:
        key, vals = create_chem_amounts(line)
        chem_map[key] = key, vals

    fuel_chem_list = chem_map.get(FUEL)
    while len(fuel_chem_list[1]) > 1:
        expanded_list = []
        for chem_amount in fuel_chem_list[1]:
            expanded_list.extend(expand_chem(chem_amount, chem_map))
        chem_map[FUEL] = fuel_chem_list[0], consolidate_list(expanded_list)
        fuel_chem_list = chem_map.get(FUEL)

    print(fuel_chem_list[1][0].amount)


FUEL = ChemAmount("0", "FUEL")
ORE = ChemAmount("0", "ORE")

part1()
