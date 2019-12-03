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
    xPos = startX
    yPos = startY
    for instruction in instructions :
        direction = instruction[0:1]
        distance = int(instruction[1:])
        if direction == "R" :
            for x in range(xPos + 1, xPos + 1 + distance) :
                grid[yPos][x] = "~"
            xPos = xPos + 1 + distance
        elif direction == "L" :
            for x in range(xPos - 1 - distance, xPos - 1) :
                grid[yPos][x] = "~"
            xPos = xPos - 1 - distance,
        elif direction == "D" :
            for y in range(yPos + 1, yPos + 1 + distance) :
                grid[y][xPos] = "l"
            yPos = yPos + 1 + distance
        elif direction == "U" :
            for y in range(yPos - 1 - distance, yPos - 1) :
                grid[y][xPos] = "l"
            yPos = yPos - 1 - distance
        printGrid(grid)

def createGrid(xDimension, yDimension) :
    return [["." for x in range(xDimension)] for y in range(yDimension)] 

file = open("TestInput.txt", "r")
instructionList = file.read().splitlines()
wire1Instructions = instructionList[0].split(",")
wire2Instructions = instructionList[1].split(",")
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

drawWire1(wire1Instructions, portX, portY, grid) 

printGrid(grid)




print(wire1Instructions)
print(wire2Instructions)
#print(allInstructions)



