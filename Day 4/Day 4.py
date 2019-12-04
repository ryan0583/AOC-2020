import sys
sys.path.append('../')
from Utils.Utils import debugPrint

def meetsCriteriaOne(value) :
    hasDoubleDigit = False
    numbersIncrease = True
    lastNum = -1
    nums = list(map(int, list(value)))
    for num in nums :
        if num < lastNum :
            numbersIncrease = False
            break
        if not hasDoubleDigit and num == lastNum :
            hasDoubleDigit = True
        lastNum = num
    return hasDoubleDigit and numbersIncrease

def meetsCriteriaTwo(value) :
    hasDoubleDigit = False
    lastWasDouble = False
    foundTripleCount = False
    numbersIncrease = True
    lastNum = -1
    nums = list(map(int, list(value)))
    for num in nums :
        if num < lastNum :
            numbersIncrease = False
            break

        if num == lastNum :
            if lastWasDouble :
                hasDoubleDigit = False
                lastWasDouble = False
                foundTripleCount = True
            else :
                hasDoubleDigit = True
                lastWasDouble = True
        elif foundTripleCount :
            break
        else :
            lastWasDouble = False

        #debugPrint(debug, hasDoubleDigit)
        #debugPrint(debug, lastWasDouble)
        #debugPrint(debug, "\n")
        
        lastNum = num
    return hasDoubleDigit and numbersIncrease

def partOne() :
    count = 0
    for value in range(numRange[0], numRange[1]) :
        if meetsCriteriaOne(str(value)) :
            count += 1
    print(count)

def partTwo() :
    count = 0
    for value in range(numRange[0], numRange[1]) :
        if meetsCriteriaTwo(str(value)) :
            debugPrint(debug, value)
            count += 1
    print(count)


debug = True
file = open("Input.txt", "r")
numRange = list(map(int, file.read().split("-")))
#partOne()
partTwo()
#print(meetsCriteriaTwo("112233"))
#print(meetsCriteriaTwo("123444"))
#print(meetsCriteriaTwo("123443"))
#print(meetsCriteriaTwo("112222"))
#print(meetsCriteriaTwo("577788"))
