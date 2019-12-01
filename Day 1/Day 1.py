import math

def partOne(lines) :
    total=0
    for line in lines:
        total += calculateFuelPartOne(line)
    print(total)
    
def calculateFuelPartOne(line) :
    return math.floor(int(line)/3) - 2

def partTwo(lines) :
    total=0
    for line in lines:
        total += calculateFuelPartTwo(line)
    print(total)

def calculateFuelPartTwo(line) :
    fuel = 0
    nextFuel = math.floor(int(line)/3) - 2
    while nextFuel > 0:
        fuel += nextFuel
        nextFuel = math.floor(int(nextFuel)/3) - 2
    return fuel
    

file = open("Input.txt", "r")
lines = file.readlines()
partOne(lines)
partTwo(lines)
