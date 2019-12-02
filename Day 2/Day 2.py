def calculateOutput(ints, noun, verb) :
    ints = list(ints)
    ints[1] = noun
    ints[2] = verb
    index = 0
    opcode = ints[index]
    while opcode != 99 :
        val = 0
        index1 = ints[index + 1]
        index2 = ints[index + 2]
        index3 = ints[index + 3]
        val1 = ints[index1]
        val2 = ints[index2]
        if opcode == 1 :
            val = val1 + val2
        else :
            val = val1 * val2
        ints[index3] = val
        index = index + 4
        opcode = ints[index]
    return ints[0]

def partOne(ints) :
    print(calculateOutput(ints, 12, 2))

def partTwo(ints) :
    exp = 19690720
    for noun in range(100) :
        for verb in range(100) :
            if calculateOutput(ints, noun, verb) == exp :
                print(100 * noun  + verb)
                break
            

file = open("input.txt", "r")
ints = list(map(int, file.read().split(",")))
partOne(ints)
partTwo(ints)

                
