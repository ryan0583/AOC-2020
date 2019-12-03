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
            xPos = xPos + distance
        elif direction == "L" :
            for x in range(xPos - distance, xPos) :
                grid[yPos][x] = "~"
            xPos = xPos - distance
        elif direction == "D" :
            for y in range(yPos + 1, yPos + 1 + distance) :
                grid[y][xPos] = "l"
            yPos = yPos + distance
        elif direction == "U" :
            for y in range(yPos - distance, yPos) :
                grid[y][xPos] = "l"
            yPos = yPos - distance

        #printGrid(grid)
        #print("\n")

def drawWire2(instructions, startX, startY, grid) :
    xPos = startX
    yPos = startY
    for instruction in instructions :
        direction = instruction[0:1]
        distance = int(instruction[1:])
        
        if direction == "R" :
            for x in range(xPos + 1, xPos + 1 + distance) :
                if grid[yPos][x] == "~" or grid[yPos][x] == "l" :
                    grid[yPos][x] = "X"
                else : 
                    grid[yPos][x] = "-"
            xPos = xPos + distance
        elif direction == "L" :
            for x in range(xPos - distance, xPos) :
                if grid[yPos][x] == "~" or grid[yPos][x] == "l" :
                    grid[yPos][x] = "X"
                else : 
                    grid[yPos][x] = "-"
            xPos = xPos - distance
        elif direction == "D" :
            for y in range(yPos + 1, yPos + 1 + distance) :
                if grid[y][xPos] == "~" or grid[y][xPos] == "l" :
                    grid[y][xPos] = "X"
                else :
                    grid[y][xPos] = "|"
            yPos = yPos + distance
        elif direction == "U" :
            for y in range(yPos - distance, yPos) :
                if grid[y][xPos] == "~" or grid[y][xPos] == "l" :
                    grid[y][xPos] = "X"
                else :
                    grid[y][xPos] = "|"
            yPos = yPos - distance

        #printGrid(grid)
        #print("\n")

def findMinCrossingPosition(grid, portX, portY) :
    minCrossing = -1
    for y in range(0, len(grid)) :
        for x in range(0, len(grid[0])) :
            if grid[y][x] == "X" :
                dist = abs(y - portY) + abs(x - portX)
                if minCrossing == -1 or dist < minCrossing :
                    minCrossing = dist
    return minCrossing
            

def createGrid(xDimension, yDimension) :
    return [["." for x in range(xDimension)] for y in range(yDimension)] 

file = open("Input.txt", "r")
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

print(wire1Instructions)
print(wire2Instructions)
drawWire1(wire1Instructions, portX, portY, grid)
drawWire2(wire2Instructions, portX, portY, grid)

#printGrid(grid)
print(findMinCrossingPosition(grid, portX, portY))

#print(allInstructions)



