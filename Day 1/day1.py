import math


def calculate_fuel(function_to_run):
    total = 0
    for line in lines:
        total += function_to_run(line)
    print(total)


def calculate_fuel_part_one(line):
    return math.floor(int(line) / 3) - 2


def calculate_fuel_part_two(line):
    fuel = 0
    next_fuel = math.floor(int(line) / 3) - 2
    while next_fuel > 0:
        fuel += next_fuel
        next_fuel = math.floor(int(next_fuel) / 3) - 2
    return fuel


file = open("Input.txt", "r")
lines = file.readlines()
calculate_fuel(calculate_fuel_part_one)
calculate_fuel(calculate_fuel_part_two)
