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
    def __init__(self, totalSteps):
        self.totalSteps = totalSteps

    def get_totalSteps(self):
        return self.totalSteps
    
    def __str__(self):
        return "X"
 
def maxPositive(instructions, posChar, negChar) :
    maxDist = 0
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
    return maxDist

def maxNegative(instructions, posChar, negChar) :
    maxDist = 0
    runningTotal = 0
    for instruction in instructions :
        direction = instruction[0:1]
        distance = int(instruction[1:])
        if direction == posChar :
            runningTotal = runningTotal + distance
        elif direction == negChar :
            runningTotal = runningTotal - distance
        if runningTotal < maxDist : 
            maxDist = runningTotal
    return maxDist

def printGrid(grid) :
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in grid]))

def drawWire1(instructions, startX, startY, grid) :
    stepNum = 0
    xPos = startX
    yPos = startY
    for instruction in instructions :
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

        #printGrid(grid)
        #print("\n")

def drawWire2(instructions, startX, startY, grid) :
    stepNum = 0
    xPos = startX
    yPos = startY
    for instruction in instructions :
        #print(stepNum)
        direction = instruction[0:1]
        distance = int(instruction[1:])
        
        if direction == "R" :
            for x in range(xPos + 1, xPos + 1 + distance) :
                stepNum += 1
                if isinstance(grid[yPos][x], WirePart) :
                    #print(str(stepNum) + ", " + str(grid[yPos][x].get_stepNum()))
                    grid[yPos][x] = Crossing(stepNum + grid[yPos][x].get_stepNum())
                else : 
                    grid[yPos][x] = "-"
            xPos = xPos + distance
        elif direction == "L" :
            for x in range(xPos - 1, xPos - 1 - distance, -1) :
                stepNum += 1
                #print(stepNum)
                if isinstance(grid[yPos][x], WirePart) :
                    #print(str(stepNum) + ", " + str(grid[yPos][x].get_stepNum()))
                    grid[yPos][x] = Crossing(stepNum + grid[yPos][x].get_stepNum())
                else : 
                    grid[yPos][x] = "-"
            xPos = xPos - distance
        elif direction == "D" :
            for y in range(yPos + 1, yPos + 1 + distance) :
                stepNum += 1
                if isinstance(grid[y][xPos], WirePart) :
                    #print(str(stepNum) + ", " + str(grid[y][xPos].get_stepNum()))
                    grid[y][xPos] = Crossing(stepNum + grid[y][xPos].get_stepNum())
                else :
                    grid[y][xPos] = "|"
            yPos = yPos + distance
        elif direction == "U" :
            for y in range(yPos - 1, yPos - 1 - distance, -1) :
                stepNum += 1
                if isinstance(grid[y][xPos], WirePart) :
                    #print(str(stepNum) + ", " + str(grid[y][xPos].get_stepNum()))
                    grid[y][xPos] = Crossing(stepNum + grid[y][xPos].get_stepNum())
                else :
                    grid[y][xPos] = "|"
            yPos = yPos - distance

        #printGrid(grid)
        #print("\n")

def findMinCrossingPosition(grid, portX, portY) :
    minCrossing = -1
    for y in range(0, len(grid)) :
        for x in range(0, len(grid[0])) :
            if isinstance(grid[y][x], Crossing) :
                dist = abs(y - portY) + abs(x - portX)
                if minCrossing == -1 or dist < minCrossing :
                    minCrossing = dist
    return minCrossing

def findMinCrossingSteps(grid, portX, portY) :
    minSteps = -1
    for y in range(0, len(grid)) :
        for x in range(0, len(grid[0])) :
            if isinstance(grid[y][x], Crossing) :
                #print(grid[y][x].get_totalSteps())
                if minSteps == -1 or grid[y][x].get_totalSteps() < minSteps :
                    minSteps = grid[y][x].get_totalSteps()
    print("\n")                    
    return minSteps
            

def createGrid(xDimension, yDimension) :
    return [["." for x in range(xDimension)] for y in range(yDimension)] 

file = open("Input.txt", "r")
instructionList = file.read().splitlines()
wire1Instructions = instructionList[0].split(",")
wire2Instructions = instructionList[1].split(",")

#print(wire1Instructions)
#print(wire2Instructions)

allInstructions = wire1Instructions + wire2Instructions

maxRight = max(maxPositive(wire1Instructions, "R", "L"), maxPositive(wire2Instructions, "R", "L"))
maxLeft = abs(min(maxNegative(wire1Instructions, "R", "L"), maxNegative(wire2Instructions, "R", "L")))
xDimension = maxRight + maxLeft + 3

maxUp = max(maxPositive(wire1Instructions, "U", "D"), maxPositive(wire2Instructions, "U", "D"))
maxDown = abs(min(maxNegative(wire1Instructions, "U", "D"), maxNegative(wire2Instructions, "U", "D")))
yDimension = maxUp + maxDown + 3

grid = createGrid(xDimension, yDimension)
portX = maxLeft + 1
portY = maxUp + 1
grid[portY][portX] = "o"

#print(wire1Instructions)
#print(wire2Instructions)
drawWire1(wire1Instructions, portX, portY, grid)
drawWire2(wire2Instructions, portX, portY, grid)

#printGrid(grid)
#print(findMinCrossingPosition(grid, portX, portY))
print(findMinCrossingSteps(grid, portX, portY))

#print(allInstructions)



