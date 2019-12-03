import sys
sys.path.append('../')
from Utils.Utils import createGrid, debugPrint, printGrid

class WirePart:
    def __init__(self, char, stepNum):
        self.char = char
        self.stepNum = stepNum

    def get_stepNum(self):
        return self.stepNum

    def get_char(self):
        return self.char
    
    def __str__(self):
        return self.char

class Crossing:
    def __init__(self, x, y, totalSteps):
        self.x = x
        self.y = y
        self.totalSteps = totalSteps

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_totalSteps(self):
        return self.totalSteps
    
    def __str__(self):
        return "X"
 
def maxRange(instructions, posChar, negChar) :
    maxDist = 0
    minDist = 0
    runningTotal = 0
    for instruction in instructions :
        direction = instruction[0:1]
        distance = int(instruction[1:])
        if direction == posChar :
            runningTotal = runningTotal + distance
        elif direction == negChar :
            runningTotal = runningTotal - distance
        if runningTotal > maxDist :
            maxDist = runningTotal
        if runningTotal < minDist :
            minDist = runningTotal
    return (minDist, maxDist)

def drawWire1() :
    stepNum = 0
    xPos = portX
    yPos = portY
    for instruction in wire1Instructions :
        direction = instruction[0:1]
        distance = int(instruction[1:])
        if direction == "R" :
            for x in range(xPos + 1, xPos + 1 + distance) :
                stepNum += 1
                grid[yPos][x] = WirePart("~", stepNum)
            xPos = xPos + distance
        elif direction == "L" :
            for x in range(xPos - 1, xPos - 1 - distance, -1) :
                stepNum += 1
                grid[yPos][x] = WirePart("~", stepNum)
            xPos = xPos - distance
        elif direction == "D" :
            for y in range(yPos + 1, yPos + 1 + distance) :
                stepNum += 1
                grid[y][xPos] = WirePart("l", stepNum)
            yPos = yPos + distance
        elif direction == "U" :
            for y in range(yPos - 1, yPos - 1 - distance, -1) :
                stepNum += 1
                grid[y][xPos] = WirePart("l", stepNum)
            yPos = yPos - distance

def drawWire2AndDetermineCrossings() :
    global crossings
    crossings = list()
    global stepNum
    stepNum = 0
    xPos = portX
    yPos = portY
    for instruction in wire2Instructions :
        direction = instruction[0:1]
        distance = int(instruction[1:])        
        if direction == "R" :
            for x in range(xPos + 1, xPos + 1 + distance) :
                stepNum += 1
                placeWireAndAddCrossing("-", x, yPos)
            xPos = xPos + distance
        elif direction == "L" :
            for x in range(xPos - 1, xPos - 1 - distance, -1) :
                stepNum += 1
                placeWireAndAddCrossing("-", x, yPos)
            xPos = xPos - distance
        elif direction == "D" :
            for y in range(yPos + 1, yPos + 1 + distance) :
                stepNum += 1
                placeWireAndAddCrossing("|", xPos, y)
            yPos = yPos + distance
        elif direction == "U" :
            for y in range(yPos - 1, yPos - 1 - distance, -1) :
                stepNum += 1
                placeWireAndAddCrossing("|", xPos, y)
            yPos = yPos - distance
    return crossings

def placeWireAndAddCrossing(wireChar, x, y) :
    gridSpace = grid[y][x]
    if isinstance(gridSpace, WirePart) :
        crossing = Crossing(x, y, stepNum + gridSpace.get_stepNum())
        grid[y][x] = crossing
        crossings.append(crossing)
    else : 
        grid[y][x] = wireChar

def findMinCrossingPosition() :
    minCrossing = -1
    for crossing in crossings :
        dist = abs(crossing.get_y() - portY) + abs(crossing.get_x() - portX)
        if minCrossing == -1 or dist < minCrossing :
            minCrossing = dist
    return minCrossing

def findMinCrossingSteps() :
    minSteps = -1
    for crossing in crossings :
        if minSteps == -1 or crossing.get_totalSteps() < minSteps :
            minSteps = crossing.get_totalSteps()                 
    return minSteps

debug = False

debugPrint(debug, "reading file")
file = open("Input.txt", "r")
instructionList = file.read().splitlines()
wire1Instructions = instructionList[0].split(",")
wire2Instructions = instructionList[1].split(",")

debugPrint(debug, "finding range")
wire1XRange = maxRange(wire1Instructions, "R", "L")
wire1YRange = maxRange(wire1Instructions, "U", "D")
wire2XRange = maxRange(wire2Instructions, "R", "L")
wire2YRange = maxRange(wire2Instructions, "U", "D")

maxRight = max(wire1XRange[1], wire2XRange[1])
maxLeft = abs(min(wire1XRange[0], wire2XRange[0]))
xDimension = maxRight + maxLeft + 3

maxUp = max(wire1YRange[1], wire2YRange[1])
maxDown = abs(min(wire1YRange[0], wire2YRange[0]))
yDimension = maxUp + maxDown + 3

debugPrint(debug, "creating grid")
grid = createGrid(xDimension, yDimension)
portX = maxLeft + 1
portY = maxUp + 1
grid[portY][portX] = "o"

debugPrint(debug, "drawing wire 1")
drawWire1()

debugPrint(debug, "drawing wire 2")
crossings = drawWire2AndDetermineCrossings()

debugPrint(debug, "finding answers")
print(findMinCrossingPosition())
print(findMinCrossingSteps())
