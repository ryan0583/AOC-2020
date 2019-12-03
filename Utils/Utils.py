def debugPrint(debug, toPrint) :
    if debug :
        print(toPrint)

def printGrid(debug, grid) :
    debugPrint(debug, '\n'.join(['\t'.join([str(cell) for cell in row]) for row in grid]))

def createGrid(xDimension, yDimension) :
    return [x[:] for x in [["."] * xDimension] * yDimension]    
