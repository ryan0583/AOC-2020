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
    lastWasDouble = False
    hasDoubleDigit = False
    numbersIncrease = True
    numConsec = 1
    lastNum = -1
    nums = list(map(int, list(value)))
    for num in nums :
        if num < lastNum :
            numbersIncrease = False
            break

        if num == lastNum :
            numConsec += 1
            if numConsec == 2 :
                lastWasDouble = True
            else :
                lastWasDouble = False
        else :
            if lastWasDouble :
                hasDoubleDigit = True
            lastWasDouble = False
            numConsec = 1

        #debugPrint(debug, hasDoubleDigit)
        #debugPrint(debug, foundOddCount)
        #debugPrint(debug, "\n")
        
        lastNum = num

    if lastWasDouble :
        hasDoubleDigit= True
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


debug = False
file = open("Input.txt", "r")
numRange = list(map(int, file.read().split("-")))
#partOne()
partTwo()
#print(meetsCriteriaTwo("112233")) #True
#print(meetsCriteriaTwo("123444")) #False
#print(meetsCriteriaTwo("123443")) #False
#print(meetsCriteriaTwo("112222")) #True
#print(meetsCriteriaTwo("577788")) #True
#print(meetsCriteriaTwo("111111")) #False
#print(meetsCriteriaTwo("122222")) #False
#print(meetsCriteriaTwo("234444")) #False
